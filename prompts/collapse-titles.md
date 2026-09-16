# 제목 · 썸네일 문구 · 댓글 유도 규칙 (FINALIZE 단계)

## 1. 제목 후보 10개

### 우선 패턴
- "한때 OO였던 XX는 왜 사라졌을까"
- "OO까지 했던 XX는 왜 무너졌을까"
- "세계 1위였던 XX가 몰락하는 데 걸린 시간"
- "모두가 쓰던 XX는 왜 사라졌을까"
- "XX를 무너뜨린 결정적인 선택"
- "OO을 발명하고도 몰락한 회사"

### 규칙
- 제목에 **구체적 숫자**를 넣는다: 전성기 숫자 · 1위 · 점유율 · 사용자 수 · 매출 · 재계 순위 · 매장 수 · 몰락에 걸린 연수
- 10개 중 최소 6개에 숫자 포함
- 패턴별로 골고루: 위 6개 패턴 각 1개 이상 + 자유형 4개
- 길이 20~35자. 유튜브 모바일에서 잘리지 않게 핵심 단어를 앞에
- 몰락 원인의 정답은 제목에서 말하지 않는다 ("XX를 무너뜨린 결정적인 선택"처럼 존재만 암시)
- 각 제목 뒤에 한 줄 메모: 어떤 시청자 심리를 노리는지 (향수 / 호기심 / 경제 관심 / 논쟁)
- 1번은 **추천 제목**으로 표시하고 이유 한 줄

### 예시 (노키아)
1. 세계 1위, 점유율 40%였던 노키아가 무너지는 데 걸린 시간 ← 추천
2. 스마트폰을 먼저 만들고도 몰락한 회사
3. 지구인 절반이 쓰던 휴대폰은 왜 사라졌을까

## 2. 썸네일 문구 10개

### 규칙
- **3~6글자 또는 짧은 한 문장**
- 제목 내용을 그대로 반복하지 않는다
- **전성기 모습과 몰락 후 모습을 대비**시키는 구성 우선 (예: "1위 → 매각", "5,000개 → 0")
- 숫자 하나만 크게 박는 안을 2개 이상 포함
- 각 문구에 어울리는 이미지 컨셉 한 줄 (전성기 사진 / 폐점 매장 / 창업자 얼굴 / 주가 차트 등)

### 예시
- 왜 망했나
- 1위의 몰락
- 모두 사라졌다
- 이 선택 하나
- 6년 만에
- 결국 파산
- 그때 팔았다면
- 40% → 3%

## 3. 썸네일 이미지 프롬프트 5개

사용자가 이미지 생성 도구(ChatGPT·Gemini 등)에 그대로 붙여넣을 **영어 프롬프트**를 5개 만든다.
각 프롬프트 위에 그 그림이 무엇인지 **한국어 한 줄 설명**을 붙인다.

### 컨셉 슬롯 5개 (몰락 장르 고정)

| # | 컨셉 | 무엇을 그리나 |
|---|------|--------------|
| 1 | **전성기 ↔ 현재 좌우 분할** | 한 화면을 세로로 갈라 왼쪽은 붐비던 전성기, 오른쪽은 같은 장소의 지금. 이 장르에서 가장 강한 구도 |
| 2 | **홀로 남은 전성기의 상징물** | 그 브랜드를 상징하던 물건 하나가 텅 빈 공간에 버려져 있는 장면 |
| 3 | **숫자가 실물이 된 초현실** | 하락 그래프·무너지는 숫자 기둥·바닥으로 꺼지는 점유율을 물리적 구조물로 |
| 4 | **결정적 선택의 순간** | 갈림길, 두 개의 문, 책상 위 두 장의 서류. 한쪽은 밝고 한쪽은 어둡게 |
| 5 | **자리를 잃은 사람** | 문 닫힌 매장 앞에 선 직원·점주의 표정 클로즈업. 과장된 표정 |

### 프롬프트 작성 규칙

- **영어로 쓴다.** 한 문단, 마침표로 이어지는 서술형
- 반드시 넣는다: `Photorealistic`, 16:9 가로 구도, **하단 35~40%를 비워둔다**(문구 자리) → `lower third of the frame left empty and uncluttered for text overlay`
- **색 대비로 시간을 표현한다**: 전성기 쪽은 따뜻하고 채도 높게(`warm saturated golden tones`), 몰락 쪽은 차갑고 바래게(`cold desaturated faded tones, overcast light`)
- 사람이 나오면 표정을 과장한다 (`exaggerated expression of disbelief`)
- **실존 브랜드 로고·상표·실존 인물 얼굴을 요구하지 않는다.** 생성이 거부되거나 초상권 문제가 생긴다. `generic unbranded` 로 쓰고, 로고는 편집에서 얹는다
- **이미지 안에 글자를 넣지 않는다**: `no text, no letters, no signage copy` 를 넣는다. 문구는 편집에서 얹는다
- 한국 소재면 배경을 명시한다 (`in a Korean shopping street`, `1990s Seoul`)

### 예시 (1번 슬롯)

```
Photorealistic split composition in a wide 16:9 frame, divided vertically down the center. On the left, a crowded 1990s Korean shopping street storefront at its peak, packed with customers, warm saturated golden tones, generic unbranded signage. On the right, the exact same storefront today, shutters down, empty pavement, cold desaturated faded tones under overcast light. A single figure stands at the dividing line looking toward the empty side with an exaggerated expression of disbelief. The lower third of the frame is left empty and uncluttered for text overlay. No text, no letters, no signage copy.
```

## 4. 댓글 유도 질문 3개

영상 마지막에 "좋아요와 구독 부탁드립니다"만 넣지 않는다. **주제와 연결된 질문**을 던진다.
대본에는 3개 중 1개만 들어가고, 나머지 2개는 고정 댓글·커뮤니티 게시용으로 완성본에 남긴다.

### 유형
- 선택 질문: "여러분이 당시 CEO였다면 어떤 선택을 했을까요?"
- 생존 가능성: "이 회사는 당시 살아남을 방법이 있었다고 보시나요?"
- 향수: "여러분이 기억하는 이 브랜드의 전성기는 언제였나요?"
- 다음 주제: "다음 영상에서 다뤘으면 하는 몰락한 기업이 있다면 댓글로 남겨주세요."

### 규칙
- 3개 중 최소 1개는 **논쟁이 생기는 질문** (MISTAKE #2의 선택을 두고 찬반이 갈리게)
- 최소 1개는 시청자 개인 경험을 묻는 향수형
- 대본에 넣는 1개는 ENDING 해석 문장 바로 뒤, 자연스럽게 이어지는 것으로

## 5. 출력 위치

| 결과물 | 들어가는 곳 |
|--------|------------|
| 제목 10개 | `output/02_썸네일제목.md` 제목 후보 + `_work/기획서.md` 3번 |
| 썸네일 문구 10개 | `output/02_썸네일제목.md` 썸네일 문구 + `_work/기획서.md` 4번 |
| 이미지 프롬프트 5개 | `output/02_썸네일제목.md` 만 |
| 추천 제목 1개 | `output/03_업로드정보.md` 제목 (02의 1번을 그대로) |
| 댓글 유도 1번 | 대본(ENDING) → `output/01_대본.txt` |
| 댓글 유도 2번 | `output/03_업로드정보.md` 고정 댓글 |
| 댓글 유도 3번 | `_work/기획서.md` 10번 (커뮤니티 게시용) |

파일 형식은 `collapse-output.md` 참조.
