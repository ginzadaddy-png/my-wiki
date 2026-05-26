---
title: "흥행 예측 지표"
type: concept
sources: ["[[firstlook-signals-of-success]]", "[[gdc25-balatro-marketing]]", "[[gdc25-steam-new-rules]]", "[[steam-next-fest-wishlist-benchmarks-2025]]", "[[zukowski-next-fest-strategy]]", "[[ign-generations-in-play-2026]]", "[[zrconsulting-steam-forecaster-2026]]"]
related: ["[[marketing-strategy|마케팅 전략]]", "[[indie-business-strategy|인디 비즈니스 전략]]", "[[game-market-trends|게임 시장 트렌드]]", "[[subscription-economy-gaming|구독 경제와 게이밍]]", "[[audience-discovery-systems|오디언스 발견 시스템]]", "[[steam-revenue-forecasting|Steam 매출 예측 모델]]", "[[forecasting-vs-launch-metrics|예측 vs 측정 비교]]"]
created: 2026-04-20
updated: 2026-05-18
confidence: high
---

게임 출시 전후 흥행 여부를 예측하는 데 사용하는 지표. 겉보기 수치(인지도 지표)와 실제 행동 기반 지표로 나뉘며, 업계는 오랫동안 전자에 과의존해왔다.

## 가짜 신호 (인지도 지표)

- 유튜브 트레일러 조회수 → 수동적 반응, 구매 의도로 이어지지 않음
- 스팀 위시리스트 → "밸브 달러"로서 알고리즘 가치는 있지만 93%가 예측 실패 경험
- 소셜 미디어 도달률 · 인플루언서 노출 → 화제성 ≠ 수익

## 진짜 신호 (행동 기반 지표)

| 지표 | 예측력 | 비고 |
|------|--------|------|
| 플레이 시간 | 1위 (41%) | 돈으로 살 수 없는 유저의 시간 |
| 재플레이 비율 | 2위 (30%) | 게임의 루프 완성도를 반영 |
| 1·7일 차 유지율 | 3위 (29%) | 출시 후 리텐션 예측 |
| 소셜 적극 참여 | 발표 기준 51% | 리뷰·공유·토론 = 노력이 수반된 행동 |

## 디스코드 지표의 역설

- 단순 서버 규모를 중시하는 개발사: **5%**
- 깜짝 흥행의 숨겨진 시그널로 디스코드 성장세를 꼽은 개발사: **48%**

디스코드는 "가입·참여 비용"이 있는 플랫폼 — 진성 유저만 남는다.

> 💡 **핵심 인사이트:** AAA·AA 개발사 93%가 흥행 예측에 실패했다. 문제는 겉으로 드러나는 수치가 아닌 **유저의 실제 행동**을 측정하지 못한 데 있다.

## 스팀 넥스트 페스트 위시리스트 벤치마크 ([[steam-next-fest-wishlist-benchmarks-2025]])

182개 게임 설문 기반 정량 데이터.

**사전 위시리스트 수 = 가장 강력한 예측변수 (r=0.825)**

| 사전 위시리스트 | SNF 중 획득 위시리스트 (중간값) |
|---------------|-------------------------------|
| 0–999 | 322 |
| 1,000–9,999 | 1,006 |
| 10,000–99,999 | 5,215 |
| 100,000+ | 12,882 |

- 데모 전환율(~20% 적정): 성과 상관관계 r=0.457. 낮으면 품질보다 프레젠테이션 미스매치 가능성이 높음
- SNF 성과 티어: Diamond(10,000+) / Gold(7,000–9,999) / Silver(1,000–6,999) / Bronze(0–999)

## Next Fest 2026-02 업데이트 ([[zukowski-next-fest-strategy]])

크리스 즈코프스키 4번 페스트 종합 분석 (2024-06 → 2026-02):

**기대치 단순화**

| 등급 | 위시리스트 |
|---|---|
| 마케팅 부진 | 1,000 이하 |
| 중간 | 2,000~3,000 |
| 상위 95p (Top 100) | ~15,000 |
| 슈퍼 바이럴 (페스트별 3~5개) | 30,000~60,000 |

**핵심 발견 — 알고리즘 효율화**: Crashlands 2(2024-06, 624만 노출 → 15,987 위시리스트) vs How Many Dudes?(2026-02, 64만 노출 → 14,740 위시리스트). **노출 1/10이지만 위시리스트는 거의 같음** → Valve가 "낭비된 노출" 정밀화.

**전략적 결론**:
- Next Fest는 검증이 아니라 **마케팅 부스터** — 이미 잘 마케팅된 게임이 더 잘됨
- **데모는 페스트 1개월 이상 전 출시** — 95p 슈퍼어너 10개 중 9개가 1개월 이전 출시
- "쉐도우 드롭" 메타는 데이터로 부정 — Tomas Sala 사례는 누적 자산 있는 예외
- **출시 직전 마지막 1번 페스트만 사용** 권장
- **"Friendslop" 코옵 게임 점유**: 플레이는 많지만 위시리스트 비율 낮음 — 일반 유저 유입 시그널

## 세대 OS 기반 출시 시그널 ([[ign-generations-in-play-2026]])

기존 흥행 예측은 *플랫폼·시간·재플레이*를 보지만, 세대별로 *어떤 시그널이 더 의미 있는가*가 다름. IGN 6,250명 조사 데이터.

**Day-of-release 시청·플레이 commit** — 세대별 출시일 압박:

| 세대 | Day-of-release commit | Livestream content engagement |
|---|---|---|
| Gen Z | **59%** | +18% over-index |
| Millennials | 평균 | — |
| Gen X | 47% (유일하게 절반 미만) | -12% under-index |

→ Gen Z 타깃 게임은 *day-1 동시 시청·디스코드 활성도·트위치 시청 시간*이 retention 예측 변수. "조용한 출시일" = Gen Z 이탈 시그널.

**게임 액세스 방식 분포 — 인텐트 측정** ([[subscription-economy-gaming]] 참조):

| 방식 | Gen X | Millennials | Gen Z |
|---|---|---|---|
| 풀가격 구매 | 42% | 38% | 20% |
| 구독으로 플레이 | 33% | 29% | 21% |
| F2P | 30% | 32% | **46%** |

해석:
- *Gen X·M 타깃 게임*은 풀가격 구매 전환율이 흥행의 1차 지표
- *Gen Z 타깃 게임*은 F2P 다운로드·구독 라이브러리 노출이 1차 지표 → "Will they buy?"보다 "Will they reside?"가 핵심 질문
- 가격 정책 = 인텐트 신호. 풀가격 = commitment / 구독 = experimentation / F2P = optionality

**구독·해지 패턴 — 라이브 서비스 의존 시 주의**:
- Gen Z 59% / Millennials 53% / Gen X 37%가 *단일 콘텐츠 위해 구독·해지*
- → 출시 직후 구독 가입 spike는 retention 시그널이 아님. 30·60·90일 잔존이 진짜 지표

**커뮤니티 활동 — Gen Z retention의 leading indicator**:
- Gen Z +20%가 UGC 때문에 게임 잔류
- Discord/Reddit/Twitch 활성도가 흥행 예측 시그널 (디스코드 지표의 역설 항목 참조)
- UGC·모드·커뮤니티 콘텐츠 생산량이 retention의 진짜 신호

> 💡 **세대 OS 시사:** 같은 출시 데이터(위시리스트·plays·revenue)도 *어느 세대 청자에 의해 만들어졌는가*에 따라 retention 전망이 다름. Gen Z 비중 높은 위시리스트는 60일 잔존 낮을 가능성 (구독·F2P 라이프사이클), Gen X·M 비중 높은 위시리스트는 풀가격 commit 가능성 높음.

## ZR Forecaster 정량 모델 ([[zrconsulting-steam-forecaster-2026]])

ZR Consulting의 Steam Revenue Forecaster (2026)는 위 행동 기반 지표들을 *재현 가능한 정량 모델*로 통합. 자세한 모델은 [[steam-revenue-forecasting|Steam 매출 예측 모델]] concept 참고. 핵심 정량:

### Wishlist conversion 정량 기준
- Week-1 median: **0.15×** (15%)
- 가격 $10 초과 시 **0.10×** (33% drop)
- 서브장르 분산: median에서 ±10×

### Review tier multiplier (discoverability gate)
| Tier | Multiplier |
|---|---|
| Negative | 0.25× |
| Mixed | 0.55× |
| Mostly Positive | 1.0× |
| Very Positive | 1.15× |
| Overwhelmingly Positive | 1.4× |

한 tier drop = 매출 반토막 가능. *첫 시간 polish·크래시 0·리뷰 응답*이 비대칭 ROI.

### Time distribution (Year 1)
- 런치월 ~38%
- 월 3·6 Steam-wide sale 시점에 lift
- Year 2 add-on: Year 1의 +35%

### Launch context lifts
- Demo at launch: +8% conversion
- Next Fest 참여: +4% conversion + 런치월 비중 ↑

### Refund rate 벤치마크
- 평균 7% (Steam aggregate)
- 단편: 10-15%
- 장편: 3-7%

### 8 Drivers — Sensitivity Ranking (tornado)
1. Wishlists at launch (±40% 범위)
2. Pre-launch buzz (1.0~2.5×)
3. Review score (0.25~1.4×)
4. Post-launch wishlists (사전의 0.7×)
5. Price
6. Refund rate
7. Organic / non-wishlist (5-50%)
8. Seasonal/launch discount

> ⚠️ ZR 본인 명시: *"30~50% 편차 가능. 예측이 아닌 계획 도구."* 1차 데이터(GameDiscoverCo·Zukowski·Valve)는 high confidence, ZR 자체 calibration(buzz multiplier·post-launch ratio·time distribution 등)은 medium confidence.

## Bad Launch Recovery — 런치 첫 달이 90% 결정 ([[zukowski-bad-launch-recovery-2024]])

Zukowski가 2024년 출시 게임 전수 분석. **런치 후 첫 달이 결과의 90%를 결정**한다는 통념을 정량 증거로 뒷받침.

### 핵심 통계
- 2024 출시 게임: **18,239개**
- "Weak launch" (첫 30일 review <150) 게임 중 → 1년 뒤 500+ review로 회복한 사례: **28개 (0.156%)**
- 즉 *bad launch 후 회복 확률 = 0.16%*

### 회복 시 5가지 메커니즘 — 거의 모두 luck 또는 word of mouth

| 메커니즘 | 사례 수 | 대표 사례 | 복제 가능성 |
|---|---|---|---|
| **Slow & Steady** (word of mouth) | 10 | HOLE 3,237 reviews·Pih 1,070 | 낮음 (게임이 본질적으로 좋아야) |
| **Viral Moment** (단일 creator) | 6 | BRUTALISTICK VR 920 (Bucky 41-video) | 매우 낮음 (luck) |
| **Slow + Viral 결합** | 6 | The Bonerooms 2,256·Inari 2,126 | 매우 낮음 |
| **Free-to-Keep trick** ⚠️ 비추천 | 4 | Caribbean Crashers ($0.99): 1,337 reviews 중 *유료 37개만* | 평점·미래 할인 파괴 |
| **Abnormal behavior** (봇 추정) | 1 | SPY-der PIG: 매월 정확히 100 reviews·전원 4.6시간 플레이 | 추천 안 함 |

### 회복 시도 가치 있는 6가지 조건 (Zukowski 진단)

다음 *모두 해당*해야 회복 시도 가치 있음:

1. **Coming soon page 짧음** (180일 미만으로 출시) — 마케팅 부족 명확
2. **데모 출시 안 했음**
3. **Median playtime 2.5시간 이상** — *게임이 진짜 재미있다는 강력한 신호*
4. **장르가 horror·Adult·friendslop** — 회복한 28개 중 21% horror, 14% friendslop, 11% adult (hidden gem hunter fanbase)
5. **출시 전 크리에이터 outreach 300명 미만**
6. **발견한 크리에이터 1명이 multiple stream으로 깊이 좋아함**

### 회복 시도 절차 (1개월 try then move on)

1. 버그 패치 + 작은 free content update (배포 보류)
2. 한 달간 가능한 모든 크리에이터에 beta branch outreach
3. *다음 discount window* 기다림
4. 가격을 *지난 historic low보다 10% 더 낮게*
5. "Update visibility round" 사용
6. **Free-to-Keep 트릭은 하지 말 것**

1개월 시도 후 결과 없으면: *다음 게임으로 넘어갈 것*

### "Mostly Positive인데 안 팔린다" — Survivorship Bias

```
"Mostly Positive 평점 = 잘 팔린다"는 통념
→ 실제: 안 좋아한 사람은 *사지도 않음* → 부정적 review 자체가 없음
→ Mostly Positive = "산 사람만 본 결과"의 survivorship bias
```

→ 평점만 보고 흥행 예측 금지. *언급량·creator coverage·median playtime*이 더 정확한 leading indicator.

### Valve "no black marks" 주장과의 정합성

Valve 공식 입장: "Steam algorithm은 과거 부진을 처벌하지 않음. 매출만 본다."

Zukowski 해석: *visibility는 충분히 줬는데 게임이 흥분을 못 만든 경우*. Discovery Queue·Popular Upcoming·New & Trending에 다 노출됐는데 "eh not for me" 반응이 누적. 즉 *알고리즘 처벌이 아니라 시장 평가*가 한 번 내려진 후 뒤집기 어렵다는 의미.

> 💡 **시사:** 런치 첫 달 진단 = *그 게임의 최종 결과*. 출시 후 마케팅 강화로 회복 노력은 *0.16% 확률에 베팅*. 동일 시간·예산을 *다음 게임 런치 전 마케팅에 투입*하는 것이 ROI 높음.
