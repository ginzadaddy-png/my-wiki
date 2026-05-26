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

## 실행 결과 기록 표 (실제 실행 후 채우기)

| # | 쿼리 | 검색 top-3 slug | 답변 품질 (1~5) | 한계 노출? | 메모 |
|---|---|---|---|---|---|
| 1 | Astro Bot 어느 스튜디오 | | | | |
| 2 | MDA 프레임워크 뭐야 | | | | |
| 3 | Sekiro 전투 디자인 | | | | |
| 4 | retention 인사이트 | | | | |
| 5 | Sony 자회사 PS5 독점 | | | | |
| 6 | Switch 2 출시일 | | | | |
| 7 | FromSoftware vs Team Asobi | | | | |
| 8 | AAA 스케일링 전략 | | | | |

**Phase 1 완료 트리거 체크**:
- [ ] 위키 기반 답변이 챗 UI에서 정상 출력 (쿼리 1·2·8 중 2개 이상 답변 품질 3 이상)
- [ ] 키워드 한계 노출 케이스 2개 이상 발견 (쿼리 4·5·6·7 중 2개 이상에서 "한계 노출?" Y)
- [ ] `core/`가 Streamlit 없이 import해서 작동 (이미 검증 완료)

---

## Phase 2~4에서 추가할 평가

- **Phase 2 종료 시**: 쿼리 4·5·7을 RAG 도입 후 재실행. 차이 측정 → Phase 3 진입 여부 결정
- **Phase 4 종료 시**: 30개 셋으로 확장 (현 8개 + 답 있음 12개 + 답 없음 10개 추가). 사람 채점
