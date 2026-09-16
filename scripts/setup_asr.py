r"""
음성 인식(faster-whisper) 설치·복구 스크립트

사용법:
    .venv/bin/python scripts/setup_asr.py            (macOS)
    .venv\Scripts\python.exe scripts\setup_asr.py    (Windows)

타임스탬프 스킬(.claude/skills/timestamp/SKILL.md)이 첫 사용 때 실행한다.
이미 준비돼 있으면 아무것도 설치하지 않고 바로 끝난다 (여러 번 실행해도 안전).

Windows에서 faster-whisper는 pip 설치가 성공해도 ctranslate2.dll을 불러오지 못하는
일이 흔하다 — Visual C++ 재배포 패키지(msvcp140.dll 등)가 없기 때문이다. 관리자 권한으로
재배포 패키지를 설치하는 대신, msvc-runtime 패키지의 DLL을 ctranslate2 폴더에 복사해
가상환경 안에서 해결한다.

DLL 로드 실패는 ImportError가 아니라 OSError로 나기 때문에, 확인은 전부 별도
프로세스로 돌린다 — 이 스크립트 자신이 같은 오류로 죽으면 복구를 할 수 없다.
"""

import glob
import os
import shutil
import subprocess
import sys


def probe(code):
    """별도 프로세스에서 코드를 실행해 성공 여부만 본다."""
    return subprocess.call(
        [sys.executable, "-c", code],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ) == 0


def pip_install(*packages):
    print(f"설치 중: {' '.join(packages)}", file=sys.stderr)
    return subprocess.call([sys.executable, "-m", "pip", "install", "-q", *packages]) == 0


def site_packages_dirs():
    import site
    dirs = list(sys.path)
    try:
        dirs += site.getsitepackages()
    except AttributeError:
        pass
    return dirs


def colocate_msvc_dlls():
    """msvc-runtime이 설치한 DLL을 ctranslate2 폴더 옆에 복사한다 (Windows 전용).

    ctranslate2는 지금 import가 깨져 있으므로 import하지 않고 폴더만 찾는다.
    """
    dst = next((os.path.join(p, "ctranslate2") for p in site_packages_dirs()
                if os.path.isdir(os.path.join(p, "ctranslate2"))), None)
    if dst is None:
        return 0

    copied = 0
    for src in (os.path.dirname(sys.executable), sys.prefix):
        for pattern in ("vcruntime140*.dll", "msvcp140*.dll", "concrt140*.dll"):
            for dll in glob.glob(os.path.join(src, pattern)):
                shutil.copy2(dll, dst)
                copied += 1
        if copied:
            break
    return copied


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if probe("import faster_whisper"):
        print("음성 인식 준비 완료")
        return 0

    installed = probe("import importlib.util, sys; "
                      "sys.exit(0 if importlib.util.find_spec('faster_whisper') else 1)")
    if not installed:
        if not pip_install("faster-whisper"):
            print("faster-whisper 설치에 실패했습니다.", file=sys.stderr)
            return 2
        if probe("import faster_whisper"):
            print("음성 인식 준비 완료")
            return 0

    # 설치는 됐는데 불러오지 못하는 상태
    if sys.platform != "win32":
        print("faster-whisper를 불러오지 못했습니다. 설치 로그를 확인해주세요.", file=sys.stderr)
        return 3

    print("DLL이 없어 복구합니다 (Visual C++ 런타임)", file=sys.stderr)
    if not pip_install("msvc-runtime"):
        print("msvc-runtime 설치에 실패했습니다.", file=sys.stderr)
        return 4

    copied = colocate_msvc_dlls()
    if copied == 0:
        print("복사할 DLL을 찾지 못했습니다.", file=sys.stderr)
        return 5

    if probe("import faster_whisper"):
        print(f"음성 인식 준비 완료 (DLL {copied}개 복구)")
        return 0

    print("DLL을 복사했지만 여전히 불러오지 못했습니다. "
          "Microsoft Visual C++ 재배포 패키지(x64) 설치가 필요할 수 있습니다.", file=sys.stderr)
    return 6


if __name__ == "__main__":
    sys.exit(main())
