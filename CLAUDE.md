# collapse-script

유튜브 **몰락 다큐멘터리** 채널 대본 제작 도구. "대본 만들어줘 — 노키아" 한마디로 적합도 평가 → 리서치 → 스토리 설계 → 집필 → 검수 → 완성본(기획서·대본·제목·썸네일)까지 진행한다.

## 스킬 라우팅

아래 요청이 오면 **반드시 해당 SKILL.md를 먼저 읽고 그대로 따를 것.**

| 사용자가 말하면 | 읽을 파일 | 하는 일 |
|----------------|-----------|---------|
| "대본 만들어줘" · "몰락 대본" · "이어서 해줘" · "대본 다시 써줘" · "제목만 뽑아줘" | `.claude/skills/collapse-script/SKILL.md` | 몰락 다큐 대본 전체 파이프라인 (상태 감지 → 자동 진행) |
| "타임스탬프 채워줘" · "타임스탬프 넣어줘" (+ 완성 영상) | `.claude/skills/timestamp/SKILL.md` | 완성 영상 전사 → `03_업로드정보.md`의 챕터 시각을 실측값으로 교체 |

- 대본/스크립트/제목/썸네일 관련 요청은 표현이 달라도 collapse-script로
- 주제(기업·브랜드·인물·산업)만 있으면 시작한다. 나머지 입력값은 `config/profile.md`의 기본값을 쓴다.

## 폴더 구조

```
collapse-script/
├── CLAUDE.md
├── scripts/
│   ├── setup_asr.py                  # 음성 인식 설치·DLL 복구 (첫 1회, 멱등)
│   └── timestamp.py                  # 완성 영상 전사 (faster-whisper)
├── config/profile.md                 # 채널 기본값 (길이·시청자·톤·분당 글자수)
├── prompts/                          # 단계별 상세 규칙 (Lazy Load)
│   ├── pd-guide.md                   # PD 판단 가이드 (앵글 선택·함정·구조 체크리스트)
│   ├── collapse-structure.md         # 13단계 스토리 구조 + 리텐션 + 원인 3개 규칙
│   ├── collapse-style.md             # 문체 규칙 + 금지 표현 + TTS 규칙
│   ├── collapse-research.md          # 리서치 항목 + 사실 확인 규칙
│   ├── collapse-titles.md            # 제목·썸네일·댓글 유도 규칙
│   ├── collapse-review.md            # 적합도 평가 + 최종 검수 12항목
│   └── collapse-output.md            # 완성본 출력 템플릿 (4파일)
└── projects/{주제-kebab-case}/
    ├── _work/                        # 중간 산출물
    │   ├── brief.md
    │   ├── evaluation.md
    │   ├── research.md
    │   ├── plan.md
    │   ├── draft.md
    │   ├── review.md
    │   └── 기획서.md                 # 13항목 (적합도·구조·원인·편집 노트·반전·이탈 구간)
    └── output/                       # 완성본 3종
        ├── 01_대본.txt               # TTS용 순수 나레이션
        ├── 02_썸네일제목.md          # 제목 후보 10 + 썸네일 문구 10 + 영문 이미지 프롬프트 5
        └── 03_업로드정보.md          # 제목·설명글·태그·고정 댓글 (유튜브에 그대로 붙여넣기)
```

## 크로스 플랫폼 규칙

macOS와 Windows에서 함께 쓴다. 폴더 생성·이동·삭제는 셸 명령 대신 Python 또는 도구(Write/Glob)로 처리한다.

```bash
python -c "import os; os.makedirs('projects/nokia-collapse/_work', exist_ok=True)"
```

## 파일 인코딩
모든 산출물은 UTF-8. `output/01_대본.txt`는 나레이션 외 텍스트(제목·장면번호·연출지시·괄호·특수문자)를 넣지 않는다.
