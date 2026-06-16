---
source: "https://gemini.google.com/share/c963d0d4f312"
author: "Gemini Enterprise (Deep Research)"
published: 2026-06-16
title: "Sekiro: Shadows Die Twice 전투 디자인 중심 효과음(Combat Sound Design) 실증적 검증 및 분석 보고서"
---

> Gemini Enterprise Deep Research 산출물 (Ginza 위키 sekiro/combat-sound). 2026-06-16 수집. 1차 출처 인용 포함 + 팩트체크 매트릭스 부록. 주파수 수치 등 일부는 커뮤니티(Steam/Reddit/Medium) 출처라 confidence 차등.

## 체간 시스템과 청각 피드백
공방 상태별 음향 차별화(주파수/감쇄/음색/전술 의미):
- **완벽 패링(탄해내기)**: 2~8kHz 고주파 피크, 긴 청명한 쇠울림 잔향, 맑은 "CLANG" → 주도권 획득·적 체간 누적. (출처: Steam Community·Medium Gatherer — 커뮤니티)
- **일반 가드(타이밍 실패)**: 저·중주파 억제, 극히 짧은 감쇄, 둔탁한 "ding" → 자기 체간 누적 경고. (커뮤니티)
- **위험 공격(危)**: 고주파 신디 경보, 모노포닉 링잉 → 가드불가(찌르기/하단/잡기) 경고.
- **간파하기(미키리, 見切り)**: 중저음 부스트, 칼날 밟는 마찰+뼈 타격 → 찌르기 저지·체간 대량 파괴.
- **인살(Deathblow)**: 전대역 관통 임팩트 + 오케스트레이션 악센트 수초 잔향 → 일격필살 보상.
- 근거: 청각 피질이 트랜지언트를 시각반응(~200-250ms)보다 ~100ms 빠르게 처리. 잇신/겐이치로 난무(Floating Passage)에서 검 궤적을 눈이 아닌 *고주파 타격음 리듬*으로 포착.

## 검격 효과음 4단계 레이어링
1) 공격 예비음(Whoosh, 속도·방향) → 2) 물리적 타격음(금속 충돌 고주파) → 3) 관통·쓸림음(뼈·살점 마찰) → 4) 이탈 공진·잔향(Ringout + 리버브). 타격 시 압축 에너지 방출 후 하모닉 배음 배가 + 긴 잔향 꼬리(두꺼운 파형) → 사실 복사보다 큰 쾌감·공간 정위감. (학술: Thiparpakul et al. 2020, MGR vs Sekiro 비교)

## 효과음 제작 — 검증 결과
- **공중 부양(Free-hanging) 폴리**: FromSoft 1차 출처엔 **없음 → "미확인"**. 기원은 사운드 엔지니어 David Dumais의 재현 튜토리얼(2024-10-28, daviddumaisaudio.com). 책상/스탠드에 칼날을 줄로 매달아 진동 간섭 없이 순수 금속 배음(Overtone Ringout) 수집.
- **Ogawa Sound 'KATANA'/'MOTION SFX' 사용 → 확인(1차).** 오가와 사운드 공식 성과 포스트(2022-02-22). 'SOUND MODEL KIT SERIES vol.2 KATANA'(96kHz/32bit, 230개 부품: 충돌·칼집 마찰·코등이 떨림 등)를 칼-칼 맞부딪침에, vol.3 'MOTION SFX'를 갈고리 와이어 액션에 적용.

## 다이내믹 오디오 상태 전이
탐색(정적 환경 배음: 바람·나뭇잎·까마귀) → 경계(앰비언스 억제 + 저음 퍼커션 루프·불협 합성) → 전투(풀 오케스트라+전통 타악 페이드인). 보스전이 극단적 템포 컨트롤러: 파계승(Corrupted Monk) 테마는 동양 포크댄스 형식 + 체력 단계에 따라 템포 점진 가속 → "칼날 사이의 춤(Dance between the blades)".

## 작곡 크레딧 — 확인
- 키타무라 유카(Yuka Kitamura): 리드(~60%+). 블러드본/다크소울3/엘든링식 멜랑콜리 오케스트라. 에마·겐이치로·검성 잇신 등 인간형 보스 = 정돈된 박자 → 패링 박자 감각 수립.
- 아사쿠라 노리유키(Noriyuki Asakura): 외부 공동, 8트랙. 천주(Tenchu)·바람의 검심 음악감독. 올빼미(Great Shinobi Owl)·원령(Apparitions) 테마 + 환경 6트랙. 비정형 록+국악(샤쿠하치/시노부에) 불협 변박 → 올빼미의 변칙성과 동기화, 전술적 불확실성 자극. (출처: vgmdb 93488·104710)

## 근접 액션 전투 효과음 비교
| 게임 | 기술 지향 | 청각의 메커닉 지배도 | 공방 판독 단차 |
|---|---|---|---|
| Sekiro | 물리 사실주의·금속 배음 증폭 | 지배적(1차 전투 제어) | 극명(CLANG vs ding) |
| Elden Ring | 서사 판타지 대규모 오케스트라·앰비언스 | 보조(구르기 타이밍·시각 프레임) | 둔탁·마모된 충돌 |
| Ghost of Tsushima | 사극(찬바라) 질감·자연 앰비언스 | 예술·감상(미장센) | 칼날 접촉음 뚜렷하나 시각과 동행 |
| Metal Gear Rising | SF 신디·왜곡 | 감정 자극(아드레날린) | 잡음 마찰 강, 프레임 음조 단차 부재 |
| Nioh | 하이브리드 고속 타격 | 기능적(잔심·피격 한계) | 속도로 인해 무기 속성 위주 |
세키로만 순수 기계적 물리음 고주파 잔향으로 신경계 조건반사 제어 → UI 안 보고 청각만으로 선공-후공 전환 인지.

## 게임플레이 피드백 오디오 일반 원칙
사운드 = 미적 화장품 아닌 1차 피드백 채널(Primary Feedback Channel).
1) 동적 정보 전달성: 주파수·음압을 상태 변수(Posture/Guard Quality)와 고정밀 동기 → 보지 않고도 피드백 폐루프.
2) 주파수 위계: 고주파=완벽 성공, 저주파 탁한 노이즈=미흡 → 질감의 쾌/불쾌로 가이드.
3) 배음·잔향 보상(Sonic Validation): 긴 Ringout/리버브로 조작 정당성·카타르시스 → 버튼 입력 본능 유발.

## 1차 출처 팩트체크 매트릭스
| 항목 | 상태 | 출처 |
|---|---|---|
| 작곡 분담(Kitamura 60%/Asakura 8트랙) | 검증완료 | vgmdb 104710·93488 |
| Ogawa KATANA/MOTION SFX 사용 | 검증완료 | ogawasound-online.com 공식 포스트 2022-02-22 |
| CEDEC Awards 2020 | 검증완료(정정) | 세키로=우수상(Excellence), 최우수상(Grand)=FF7R(MASTS). CGWORLD 2020-07-16·Gamer 2020-09-03 |
| 공중부양 폴리 | 1차 미확인 | David Dumais Audio 2024-10-28 (재현 가이드) |
| 4단계 레이어링 | 검증완료(학술) | Thiparpakul et al., ResearchGate 2020-03 |

## (A) 위키 추가 후보
| 페이지 | 분류 | 근거 |
|---|---|---|
| 게임플레이 피드백 오디오(Gameplay Feedback Audio) | 개념 | 사운드를 상태변수와 1:1 결합한 1차 피드백 채널 |
| 조립식 효과음 모델(SOUND MODEL KIT/Ogawa) | 엔티티/기법 | 효과음 부품화로 프레임 단위 어쿠스틱 싱크 |
| 전술 불협화(Asakura 비전형 배치) | 예술/서사 | 질서 클래식 vs 불협 록-민요가 전술 인지에 주는 자극 |
| 음향 감쇠 곡선·조작 동기화 | 물리음향/인지 | 배음·리버브 꼬리가 버튼 타이밍 인지에 주는 효능 |

## (B) ingest 후보 1차 출처
| 제목 | 저자/발행 | 발행 | URL | 우선 |
|---|---|---|---|---|
| The Satisfaction of Sword's Sound Effect... (MGR & Sekiro) | Thiparpakul, Jiravansirikul, Dheandhanoo / ResearchGate | 2020-03 | https://www.researchgate.net/publication/341628293 | 최상 |
| 【Achievements】OGAWA SOUND used for SEKIRO | OGAWA SOUND 공식 | 2022-02-22 | https://www.ogawasound-online.com/en/post/【achievements】ogawa-sound-s-sound-effect-material-was-used-for-sekiro-shadows-die-twice | 최상 |
| SEKIRO OST (크레딧) | FromSoftware / VGMdb | 2020-03-27 | https://vgmdb.net/album/93488 | 최상 |
| CEDEC AWARDS 2020 결과 | CESA/CEDEC 운영위 | 2020-09-03 | https://www.gamer.ne.jp/news/202009030062/ | 상 |
| Sword Impact Sound Design - Sekiro | David Dumais | 2024-10-28 | https://www.daviddumaisaudio.com/sword-impact-sound-design/ | 중 |
