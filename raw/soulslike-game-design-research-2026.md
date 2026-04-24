# 소울라이크 게임 디자인 분석 — 프롬소프트웨어 중심 종합 리서치

출처: 웹 리서치 종합 (2026-04)
주요 참고: Game Informer 미야자키 인터뷰(2024), Gameopedia 분석, GamesRadar, Game Developer, GameRant

---

## 1. 소울라이크의 정의와 장르 기원

### 프롬소프트웨어의 자기 인식
- 미야자키 히데타카: "프롬소프트웨어가 소울라이크 장르를 발명했다고 말하지 않겠다"
- 대신 "당시 시장에서 빠져 있던 것과 우리의 게임 디자인이 겹쳤다"는 표현 사용
- 데몬즈 소울(2009) 이후 이 장르적 공백을 채우는 타이틀들이 등장

### 장르 정의 요소 (Wikipedia/학술 기준)
1. **방법론적 전투** — 빠른 반사보다 패턴 학습과 전략적 접근
2. **가혹한 난이도** — 실패가 핵심 게임플레이 루프의 일부
3. **위험-보상 진행** — 리소스 손실을 감수하며 전진
4. **환경 기반 스토리텔링** — 대사 대신 공간과 아이템으로 세계관 전달
5. **interconnected world** — 루프와 지름길로 연결된 세계

---

## 2. 난이도 철학 — "공정한 가혹함"

### 미야자키의 핵심 발언 (Game Informer, 2024)
> "단순히 난이도를 높이는 것이 아니라, 공정하게 높이는 것이다."
> "플레이어가 죽었을 때 왜 죽었는지 이해하고, 그것이 정당하다고 느낀다면 — 그것이 우리가 만들려는 게임이다."

### 난이도 조절 불가 원칙
- 미야자키: "난이도를 낮추는 옵션은 게임 자체를 부수는 것"
- 이유: 난이도가 단순한 장벽이 아니라 **감정적 보상의 전제조건**이기 때문
- "고통을 이겨냈을 때의 성취감, 그 감정이 게임의 핵심 가치"

### 공정성의 구체적 설계 원칙
- **사전 학습 기회 제공**: 잡몹이 보스 어택 패턴의 축소판 (다크소울의 해골 워리어 → 스켈레톤 로드)
- **환경적 힌트**: 위험 구역 직전에 아이템이나 시체 등 시각적 경고
- **패턴 인식 가능성**: 모든 공격은 읽을 수 있는 텔레그래프 존재 (단, 그것이 쉽지는 않음)

---

## 3. 핵심 전투 시스템 디자인

### 스태미나 시스템
- 공격, 방어, 구르기 모두 스태미나 소모
- 스태미나 고갈 시: 공격 불가 + 가드 브레이크 취약
- 설계 의도: **모든 행동이 리소스 커밋**. 공격 한 번이 결과를 낳는 무게감

### 죽음 루프 (Death Loop) 메커니즘
- 사망 시 소지 소울(혹은 룬) 전량 드롭
- 사망 지점으로 돌아가면 회수 가능
- 다시 사망하면 영구 소멸

**설계 의도 분석:**
- 탐험 자체를 위험-보상 구조로 만듦
- "조금만 더 가면 회수 가능"이라는 심리적 긴장감 유지
- Lords of the Fallen 개발팀: "죽음 사이클을 개선하고 싶었다" — 역으로 이 루프의 설계 완성도를 증명

### 보스 설계 방법론

**공격 텔레그래프 계층화:**
- 1페이즈: 느린 공격 + 명확한 선딜
- 2페이즈: 새로운 콤보 추가, 속도 증가
- 학습 곡선이 보스 자체 내에서 완결됨

**가독성의 역설:**
- 덜 성공한 소울라이크 클론들은 텔레그래프가 너무 명확 → 긴장감 소멸
- 프롬소프트웨어: "읽을 수 있지만 쉽지 않은" 균형점 추구
- 성공적 보스 = 충분한 학습 후 "내가 완전히 이해했다"는 순간의 카타르시스

**보스 환경 설계:**
- 보스 아레나 자체가 이야기 — 王座, 폐허, 자연환경 등
- 보스 외형/행동이 세계관 로어와 연결 (예: 말레니아의 부패꽃 모티프)

---

## 4. 세계관 전달 방식

### 환경 스토리텔링 원칙
- **빈 왕좌**: 설명 없이 권력 공백 암시
- **쌓인 시체들**: 이 경로로 많은 이들이 도전했음을 시사
- **아이템 배치 위치**: 아이템 설명문(lore text)과 물리적 위치의 일치

### 의도적 모호성 (Intentional Ambiguity)
- 미야자키: "플레이어가 가이드 없이, 미지의 상태로 경험하길 원한다"
- "경이로움의 감각(sense of wonder)"이 첫 플레이의 핵심 가치
- 명확한 설명의 부재 = 플레이어 상상력 참여 유도

### 아이템 설명문 (Item Descriptions)
- 100~200자 내외의 짧은 텍스트
- 직접적 서술 금지 — 단편적 사실과 암시만
- 플레이어가 복수의 아이템 설명을 조합해 스스로 서사 구성

---

## 5. 레벨 디자인 원칙

### 루프와 지름길의 문법
- **지름길 열기 순간**: 소울 디자인의 핵심 감정 중 하나
- 문/엘리베이터/게이트로 루프 형성 → 공간 재인식 순간
- "이 문이 거기로 연결됐구나"라는 순간의 보상

### 구역 독특성
- 각 구역마다 기억에 남는 고유 요소 필수
- 플레이어가 정신적 지도(mental map) 구성 가능하도록 설계
- 하나의 끝에서 다른 끝을 바라보며 "저기가 목표"를 인식할 수 있게

### 다크소울 → 엘든링 진화
| 요소 | 다크소울 | 엘든링 |
|------|---------|--------|
| 구조 | 컴팩트 수직 레이어 | 레거시 던전 + 오픈 필드 분리 |
| 유도 | 보닥불 위치, 공간 레이아웃 | 황금 나뭇잎, NPC 힌트, 필드 랜드마크 |
| 자유도 | 상대적으로 선형 | 비선형, 우회 항상 가능 |
| 난이도 접근 | 막힌 벽을 뚫는 방식 | 막히면 다른 방향으로 이동 가능 |

---

## 6. 소울라이크가 잘못 이해되는 것들

출처: Game Developer — "What Everyone Gets Wrong about Soulslike Design"

### 오해 1: "단순히 어렵게 만들면 소울라이크"
- 실제: 난이도는 수단, **공정성과 학습 가능성**이 핵심
- 무조건 어렵기만 한 게임 ≠ 소울라이크

### 오해 2: "죽음 = 패널티"
- 실제: 죽음 = **정보**. 보스 패턴 한 사이클을 배우는 과정
- 사망이 좌절이 아니라 학습 피드백이 되어야 함

### 오해 3: "이야기가 없다"
- 실제: 이야기가 없는 게 아니라 **전달 방식이 다름**
- 플레이어가 적극적으로 세계를 해석해야 하는 참여형 서사

---

## 7. 장르 영향력과 미래

### 장르 영향
- Hollow Knight, Nioh, Lies of P, Sekiro 등 파생작들의 공통점: 프롬 공식의 특정 요소 강화·변형
- "소울라이케이션(Soulsification)" — 학술 논문 수준의 현상으로 분석됨 (Springer Nature, 2024)

### 미야자키의 미래 방향 (2024)
- "자유와 난이도의 조합이 다음 게임의 큰 힌트"
- 프롬소프트웨어는 다양한 장르에 걸쳐 복수 프로젝트 개발 중
- 미야자키 외 다른 디렉터들도 참여 — "새로운 프롬소프트웨어를 보여줄 수 있을 것"

---

## 참고 출처

- [Miyazaki on Difficulty — Game Informer (2024)](https://gameinformer.com/interview/2024/06/24/from-softwares-hidetaka-miyazaki-discusses-his-approach-to-difficulty)
- [What Everyone Gets Wrong about Soulslike Design — Game Developer](https://www.gamedeveloper.com/design/what-everyone-gets-wrong-about-soulslike-design)
- [FromSoftware's Influence: A Legacy of Challenge and Discovery — Brig News (2025)](https://brignews.com/2025/03/07/fromsoftwares-influence-a-legacy-of-challenge-and-discovery/)
- [Difficulty, Deception and Death: The Design of a Souls-Like — Gameopedia](https://gameopedia.com/blogs/difficulty-deception-and-death-the-design-of-a-souls-like)
- [Future FromSoft games will build on freedom and difficulty — GamesRadar (2024)](https://www.gamesradar.com/games/open-world/future-fromsoft-games-will-build-on-elden-rings-combination-between-freedom-and-difficulty-director-hidetaka-miyazaki-says/)
- [8 Most Influential FromSoftware Mechanics — GameRant](https://gamerant.com/most-influential-fromsoftware-mechanics-ranked/)
- [The Soulsification of video games — Springer Nature (2024)](https://link.springer.com/article/10.1007/s11042-024-19628-4)
