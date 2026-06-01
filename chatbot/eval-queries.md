# Phase 1 평가 쿼리 셋

작성일: 2026-05-21
용도: API 키 받자마자 `streamlit run app.py`에 던질 검증 쿼리. 키워드 검색 한계 노출 케이스 2개 이상 확인이 Phase 1 완료 트리거.

위키 현황(2026-05-21): entities 59 · concepts 54 · comparisons 12 · sources 115.

---

## 쿼리 1 — 단순 entity 조회 (난이도: 쉬움)

**Q**: "Astro Bot은 어느 스튜디오가 만들었어?"

- **기대 검색 hit**: `astro-bot`, `team-asobi` (둘 다 entity)
- **기대 답**: 팀 아소비(team-asobi)가 개발, Sony Interactive Entertainment 산하
- **검증 포인트**: 키워드 `astro`·`bot`이 entity 페이지 제목 매치 → 점수 높음. Phase 1 검색이 정상 작동하는지 기본 확인

---

## 쿼리 2 — 단순 concept 정의 (난이도: 쉬움)

**Q**: "MDA 프레임워크가 뭐야?"

- **기대 검색 hit**: `mda-framework` (concept)
- **기대 답**: Mechanics → Dynamics → Aesthetics 3계층 게임 설계 프레임워크 요약
- **검증 포인트**: 한글 쿼리 → 영문 슬러그 매칭 어려울 수 있음. 키워드 토크나이저가 `mda`·`프레임워크`를 어떻게 처리하는지 확인. `프레임워크` 매치되면 본문에서 발견

---

## 쿼리 3 — 두 페이지 결합 (난이도: 중간)

**Q**: "Sekiro의 전투 디자인 특징은?"

- **기대 검색 hit**: `sekiro` (entity) + `combat-design` 또는 `combat-philosophy` (concept/comparison)
- **기대 답**: 패링·posture·1:1 검극·FromSoftware 디자인 철학 결합 답변
- **검증 포인트**: 단일 페이지로 부족, *두 페이지 정보 결합*해야 좋은 답. 검색 top-5에 entity+concept 둘 다 들어오는지 확인

---

## 쿼리 4 — 추상 테마 (난이도: 어려움 — **키워드 한계 노출 후보**)

**Q**: "retention 관련 인사이트는?"

- **기대 검색 hit (이상)**: `live-service-design`, `launch-metrics`, `player-trust-design`, `subscription-economy-gaming`
- **기대 검색 hit (실제 예상)**: 위 페이지들이 `retention` 영문 단어를 잘 안 쓰면 검색 실패 → 점수 0 또는 무관 페이지 top 진입
- **검증 포인트**: **키워드 검색 한계 노출 핵심 케이스**. "retention"·"리텐션"·"유지율" 다 시도해서 결과 비교. 한국어 의미 검색 한계 = Phase 2 RAG 동기. *Phase 1 완료 트리거 한 케이스*

---

## 쿼리 5 — 관계 추론 (난이도: 어려움 — **graph 필요 후보**)

**Q**: "Sony가 모회사인 스튜디오 중 PS5 독점작을 만든 곳은?"

- **기대 답**: Team Asobi (Astro Bot), Sucker Punch (Ghost of Tsushima/Yotei), Sony Santa Monica (God of War), Naughty Dog (TLoU), Insomniac (Spider-Man 2)
- **검증 포인트**: 단일 페이지에 답 없음. *여러 entity 페이지 + 모회사 관계* 필요. Phase 1 키워드 검색은 `sony`·`PS5`·`독점` 매치되는 페이지 무더기 반환 → Claude가 합리적으로 종합하는지 보기. **Phase 3 graph 필요성 직접 측정 케이스**

---

## 쿼리 6 — 위키에 답 없음 (난이도: 어려움 — **hallucination 평가**)

**Q**: "Nintendo Switch 2 출시일은?"

- **기대 답**: "위키에 관련 페이지 없음" 또는 "Nintendo 페이지는 있으나 Switch 2 출시일 정보는 없음"
- **검증 포인트**: `nintendo` 키워드 검색은 페이지 hit하지만 *그 페이지에 답이 없음*. Claude가 hit된 페이지만 보고 "모른다"고 답하는지, 학습 데이터로 환각해서 답하는지 측정. **Phase 4 hallucination 평가의 사전 시그널**

---

## 쿼리 7 — 다중 entity 비교 (난이도: 중간)

**Q**: "FromSoftware와 Team Asobi의 개발 방식 차이는?"

- **기대 검색 hit**: `fromsoftware`, `team-asobi` (entity 2개) + `rapid-prototyping`, `studio-culture` (concept)
- **기대 답**: 둘 다 entity 페이지 정보 + 개발 철학 차이 종합 (FromSoftware는 장인적·실험적, Team Asobi는 빠른 프로토타이핑)
- **검증 포인트**: 키워드 검색이 *두 entity 모두* top-5에 올리는지. 단일 키워드 매치만 잘 잡으면 둘 중 하나만 top에 들 가능성

---

## 쿼리 8 — comparison 직접 조회 (난이도: 쉬움)

**Q**: "AAA 스튜디오들의 스케일링 전략 비교는?"

- **기대 검색 hit**: `aaa-scaling-strategy` (comparison)
- **기대 답**: 해당 comparison 페이지 내용 요약
- **검증 포인트**: comparison 페이지가 검색 대상에 정상 포함되는지(`iter_wiki_pages` 함수가 comparisons/ 폴더도 yield하는지). 키워드 `AAA`·`스케일링` 매치 확인

---

## 실행 결과 기록 표 (2026-06-01 실행, BOM 수정 후)

모델: `claude-sonnet-4-6`. 8회 호출. 검색 = 키워드(제목×3·본문×1).

| # | 쿼리 | 검색 top-3 slug(score) | 품질 (1~5) | 한계 노출? | 메모 |
|---|---|---|---|---|---|
| 1 | Astro Bot 어느 스튜디오 | carless-genres(4)·publisher-deal(3)·catalog-econ(2) | **1** | **Y — 교차언어** | astro-bot.md 존재하나 영문 쿼리"Astro Bot"가 한글 제목"아스트로봇"과 매칭 안 됨 → "없음" 오답 |
| 2 | MDA 프레임워크 뭐야 | mda-framework(5)·gmtk-mda(4)·skyrim(3) | 5 | N | 정확·풍부. 한글 쿼리가 영문 슬러그 제목과 매칭 잘 됨 |
| 3 | Sekiro 전투 디자인 | combat-philosophy(16)·combat-design(13)·gow(8) | **2** | **Y — 길이 편향** | sekiro.md 존재하나 긴 concept 페이지들이 raw 빈도로 압도 → entity 누락 |
| 4 | retention 인사이트 | game-utility(4)·live-service(4)·about(3) | 5 | N | 매우 우수. "retention" 영어 단어가 위키 본문에 그대로 존재 → 키워드 적중 |
| 5 | Sony 자회사 PS5 독점 | marketing-channels(11)·EA(8)·engine-vs-ue5(7) | **1** | **Y — 관계 추론** | 산하 entity 다수 존재하나 키워드가 엉뚱한 페이지 잡음. 다중 hop 필터 필요 |
| 6 | Switch 2 출시일 | steam-forecast(20)·catalog(19)·catalog(19) | 5 | N (의도) | **hallucination 회피 성공** — 위키에 없는 정보 "모른다" 정직 거절 |
| 7 | FromSoftware vs Team Asobi | rapid-proto(10)·multi-project(9)·dev-org(8) | 4 | N | 둘 다 양호. 본문 한·영 혼용이라 매칭됨. 비교 레이어까지 정리 |
| 8 | AAA 스케일링 전략 | aaa-scaling(15)·marketing(10)·pearl-abyss(10) | 5 | N | 우수. comparison 페이지 1위 정상 진입 |

**품질 분포**: 5점 4개(Q2·4·6·8) · 4점 1개(Q7) · 2점 1개(Q3) · 1점 2개(Q1·5)

---

## 발견된 키워드 검색 한계 3가지 (Phase 2·3 동기)

1. **교차언어 매칭 불가** (Q1) — 영문 쿼리 ↔ 한글 제목/본문 토큰이 안 맞음. 페이지가 있어도 못 찾음.
   → **Phase 2 multilingual 임베딩(BGE-M3)** 강력 동기. 영문↔한글 의미 매칭 필요.
2. **길이 편향** (Q3) — raw term frequency가 긴 concept 페이지에 유리. 정작 주제의 짧은 entity 페이지가 밀림.
   → **Phase 2 청크 정규화 + 의미 검색** 동기. 페이지 길이 무관한 관련도 측정 필요.
3. **관계 추론 불가** (Q5) — "Sony 자회사 중 X" 같은 다중 hop 필터를 키워드로 못 풂.
   → **Phase 3 graph** 동기. relations 필드 + NetworkX 필요. (Phase 2 끝 측정에서 재확인)

## 긍정 신호

- **hallucination 회피 작동** (Q6) — 시스템 프롬프트 "위키에 없으면 명시" 규칙이 정상 동작. Phase 4 평가의 핵심 지표 사전 통과.
- **영어 키워드 본문 적중 시 우수** (Q4) — 키워드 검색도 용어가 위키에 그대로 있으면 잘 작동.
- **comparison·concept 페이지 검색 정상** (Q2·8) — `iter_wiki_pages`가 전 폴더 정상 yield.

## 부수 수정 (이번 검증 중 발견)

- **BOM 버그 수정**: 위키 .md 20개가 UTF-8 BOM으로 시작 → frontmatter 파싱 실패(type=unknown, title 누락). `wiki_loader`가 `utf-8-sig`로 읽도록 수정. *역설적으로* 이 수정이 Q1의 교차언어 한계를 드러냄 (BOM 버그가 slug-fallback 제목으로 우연히 영문 쿼리를 돕고 있었음).
- **`.env` override 버그**: 셸 환경의 빈 `ANTHROPIC_API_KEY`가 `.env`를 가림 → `load_dotenv(override=True)`로 수정.

---

## Phase 1 완료 트리거 체크 ✅

- [x] 위키 기반 답변이 정상 출력 — Q2·4·7·8 품질 4~5, Q6 올바른 거절 (목표: 2개 이상 품질 3+ → **5개 충족**)
- [x] 키워드 한계 노출 케이스 2개 이상 — **3개 발견** (Q1 교차언어·Q3 길이편향·Q5 관계추론)
- [x] `core/`가 Streamlit 없이 import해서 작동 — 검증 완료

→ **Phase 1 완료.** Phase 2(RAG)의 동기가 실측 데이터로 뒷받침됨.

---

## Phase 2 RAG 결과 (2026-06-01, BGE-M3 + Chroma)

색인: 1409 청크, dim=1024, cosine. 검색 = 의미검색(쿼리 임베딩 → top-k 청크 → 페이지 묶음).
score = 코사인 유사도 (1 - distance), 높을수록 유사.

| # | 쿼리 | RAG top-3 slug(유사도) | 품질 | 키워드 대비 |
|---|---|---|---|---|
| 1 | Astro Bot 어느 스튜디오 | team-asobi(0.55)·astro-bot(0.54)·embark(0.49) | **5** | **1→5 교차언어 해결** |
| 2 | MDA 프레임워크 | mda-framework(0.62)·gmtk-mda(0.56)·player-trust(0.53) | 5 | = (더 풍부) |
| 3 | Sekiro 전투 디자인 | **sekiro(0.61)**·adam-millard(0.52)·combat-phil(0.49) | **5** | **2→5 길이편향 해결** |
| 4 | retention 인사이트 | live-service(0.61)·game-utility(0.58)·subscription(0.58) | 5 | = (세대분석 심화) |
| 5 | Sony 자회사 PS5 독점 | team-asobi(0.55)·arrowhead(0.53)·sony-santa-monica(0.52) | **4** | **1→4 대폭 개선** (Arrowhead=퍼블리셔지 모회사 아님까지 구별) |
| 6 | Switch 2 출시일 | spiderman-2(0.57)·helldivers-2(0.56)·rdr2(0.55) | 5 | **catalog 페이지서 "Switch 2 2025-06" 발굴** (키워드는 놓침) |
| 7 | FromSoftware vs Team Asobi | small-team(0.57)·asobo(0.54)·aaa-scaling(0.54) | 4 | = (FromSoftware 페이지 부재 정직 고지) |
| 8 | AAA 스케일링 | **aaa-scaling(0.67)**·embark-quarter(0.56)·small-studio-goty(0.55) | 5 | = (더 풍부) |

**품질 분포**: 5점 6개 · 4점 2개 (Phase 1: 5점 4·4점 1·2점 1·1점 2 → **전 항목 4점 이상으로 상승**)

### 핵심 성과
- **Phase 1 키워드 실패 3개(Q1·Q3·Q5) 전부 해결**:
  - Q1 교차언어 — 청크 임베딩의 한글 제목 프리픽스가 영문 쿼리와 의미 매칭
  - Q3 길이편향 — 의미 유사도가 raw 빈도 압도. sekiro 1위 직격
  - Q5 관계추론 — 관련 Sony 스튜디오 정확 retrieval + Arrowhead 구별. 단순 다중 hop은 여전히 graph가 더 정밀할 영역
- **Q6**: 키워드가 완전히 놓친 "Switch 2 (2025-06)" 언급을 catalog 페이지에서 발굴. grounding 정확(환각 아님)

### Phase 2 완료 트리거 ✅
- [x] 추상 질문(retention)에 적절한 페이지 top-5 진입 — live-service-design 1위(0.61)
- [x] 임베딩 갱신 워크플로우 end-to-end 작동 — `build_index.py` 1409 청크 색인 성공
- [x] RAG가 키워드 대비 품질 향상 실측 — 5점 4→6개, 1·2점 전멸

→ **Phase 2 완료.** Phase 3(graph) 진입 여부는 다중 hop 쿼리 추가 측정 후 결정 (아래).

## Phase 3 진입 측정 결과 (2026-06-01) — 진입 결정

`run_phase3_measure.py`로 진짜 2-hop+ 관계 쿼리 5개를 RAG로 실행. 로드맵 v2 조건: 3개+ 못 풀면 Phase 3 진입.

| # | 쿼리 (필요 추론) | RAG top-3 | 판정 |
|---|---|---|---|
| M1 | Astro Bot 팀의 모회사가 소유한 다른 스튜디오 (game→studio→parent→siblings) | arrowhead·team-asobi·embark | ❌ 형제 열거 실패 |
| M2 | GoW 스튜디오와 같은 모회사 스튜디오들 (2-hop siblings) | god-of-war-2018·gow-combat·io-interactive | ❌ "없음" |
| M3 | Sucker Punch+Naughty Dog 공통 모회사의 다른 자회사 (join) | naughty-dog·raw-fury·sucker-punch | ❌ 공통=Sony만, 자회사 열거 실패 |
| M4 | FromSoftware와 같은 소울라이크 다른 스튜디오 (genre hop) | dark-souls·soulslike·fromsoftware | ❌ 게임만, 스튜디오 매핑 실패 |
| M5 | Ghost of Tsushima 모회사가 퍼블리싱한 PS5 독점작 (2-hop) | sucker-punch·astro-bot·kojima | ❌ 체인만, 독점작 열거 실패 |

**5/5 실패** (조건 3개 초과). **→ Phase 3 진입 확정.**

### 패턴 진단
RAG는 개별 사실(Team Asobi→Sony)은 정확하나, *"X와 R 관계인 모든 엔티티 열거"* 하는 역방향 traversal·join을 못 함. 형제·자회사 페이지는 쿼리와 의미적으로 가깝지 않고 `parentOf` 엣지로만 연결되기 때문 — 의미 검색의 본질적 한계. graph에 엣지가 있으면 `neighbors(sony, depth=1)` 한 번으로 풀림.

### Phase 3 범위 (전제)
현재 `relations:`는 신규 entity에만 존재(Phase 1 규칙). graph 작동 전제 = **기존 entity mass-retrofit**(원문 quote 강제 + 사람 spot check) + NetworkX graph build + 쿼리 도구 3개(find_by_relation·path_between·neighbors).

## Phase 3 결과 (2026-06-01) — graph 통합 후 M1~M5 재실행

retrofit: 게임 26개 relations + 모회사 entity 5개 신규(sony-interactive-entertainment·microsoft·krafton·take-two-interactive·bandai-namco). graph: 266 노드·73 엣지(developedBy 31·publishedBy 21·parentOf 13·genre 5·platform 3). agent는 Claude tool-use로 graph 도구 6개(resolve_entity·get_relations·get_children·get_siblings·find_by_relation·find_path) 호출.

| # | RAG only (Phase 2) | RAG + Graph (Phase 3) | 판정 |
|---|---|---|---|
| M1 형제 스튜디오 | ❌ 열거 실패 | get_siblings로 SIE 자회사 5개 전부 | ✅ |
| M2 같은 모회사 | ❌ "없음" | santa-monica 형제 4개 | ✅ |
| M3 공통 모회사+자회사 | ❌ 부분 | 공통 SIE + get_children 전부 | ✅ |
| M4 soulslike 장르 | ❌ 부분 | find_by_relation(genre,in) 3개 + RAG로 Lies of P·Nioh 보완 | ✅ |
| M5 퍼블리싱 독점작 | ❌ 열거 실패 | publishedBy(in) 8개 열거 + platform 데이터 갭 정직 고지 | ✅ |

**5/5 해결** (RAG 0/5 → graph 5/5).

### 핵심 성과
- 관계 추론(역방향 traversal·join·열거)은 graph가 결정적. RAG가 본질적으로 못 푸는 영역을 메움
- agent가 관계 질문을 감지해 자동으로 graph 도구 호출 (시스템 프롬프트 라우팅)
- **데이터 정직성**: M5에서 platform 관계가 비어 있자 agent가 "graph에 platform 정보 부족"이라 명시 — 환각 없이 한계 고지

### 알려진 갭 / 향후
- **platform·genre 데이터 희소**: platform entity 페이지 부재로 "PS5 독점" 같은 플랫폼 필터 불완전. 향후 platform 노드(ps5·ps4·switch·pc) 도입 시 M5 완전 해결
- mass-retrofit은 게임·주요 모회사 중심. 일부 퍼블리셔(Focus·WB·Kepler 등)는 entity 미생성

### Phase 3 완료 트리거 ✅
- [x] 관계 따라가야 답 나오는 질문 정확히 답함 — M1~M5 5/5 (목표 3개+)
- [x] retrofit spot check — 추론 항목(⚠️) 사용자 검수 후 적용, 환각 매핑 0

→ **Phase 3 완료.** 다음: Phase 4(hybrid 라우팅 정리 + 클라우드 배포 + 30개 평가셋 사람 채점).

## Phase 4에서 추가할 평가

- 30개 셋으로 확장 (현 8개 + 답 있음 12개 + 답 없음 10개 추가). 사람 채점.

## Phase 4에서 추가할 평가

- 30개 셋으로 확장 (현 8개 + 답 있음 12개 + 답 없음 10개 추가). 사람 채점.
