---
title: "소규모 팀 개발 전략"
type: concept
sources: ["[[gdc25-astrobot]]", "[[gdc26-expedition33-programmers]]", "[[expedition33-ue5-interview]]", "[[gdc26-ghost-of-yotei]]", "[[gdc26-arc-raiders-reset]]", "[[gdc2023-asobo-how-to-make-aaa-small-team]]", "[[gdc2026-embark-character-pipeline]]", "[[itoi-miyamoto-dialogue-2024]]", "[[gdc-helldivers2-team-scaling]]", "[[pilestedt-helldivers2-preproduction-lesson]]"]
related: ["[[team-asobi|팀 아소비]]", "[[sandfall-interactive|샌드폴 인터랙티브]]", "[[sucker-punch-productions|서커펀치 프로덕션]]", "[[embark-studios|엠바크 스튜디오]]", "[[asobo-studio|Asobo Studio]]", "[[arrowhead-game-studios|애로우헤드]]", "[[helldivers-2|헬다이버스 2]]", "[[rapid-prototyping|빠른 프로토타이핑]]", "[[designer-empowerment|디자이너 도구화]]", "[[vision-statement|비전 선언문]]", "[[data-driven-development|데이터 기반 개발]]", "[[art-pipeline-design|아트 파이프라인 설계]]", "[[constraint-driven-creativity|제약 기반 창의성]]", "[[shigeru-miyamoto|미야모토 시게루]]", "[[reports/how-small-teams-ship-big-games|소규모 팀 종합 아티클]]"]
created: 2026-04-13
updated: 2026-07-06
confidence: high
---

소수 인원으로 대작을 완성한 스튜디오들의 공통 전략.

**1. 명확한 반복 구조**
- [[team-asobi|팀 아소비]] (65명): 2주 주기 프로토타이핑, 103회 전체 리뷰, 6주 플레이테스트
- [[sandfall-interactive|샌드폴 인터랙티브]] (~40명): 역할 분리(프로그래머=도구, 디자이너=콘텐츠)로 병목 제거

**2. 도구와 엔진을 내 편으로**
- 엔진에 손대지 않기: 버전 업 비용 방지, 최신 버그 수정 무상 획득 (샌드폴)
- 서드파티 플러그인·UE 마켓플레이스 적극 활용 (샌드폴)
- UE5 고수준 기능(루멘, 나나이트, 메타사운드, 메타휴먼)을 한계까지 밀어붙이기
- *아트 파이프라인 공유*: Embark는 Arc Raiders + The Finals가 같은 Houdini/USD 파이프라인 공유 → 멀티 프로젝트 가능 → [[art-pipeline-design|아트 파이프라인 설계]]. ⚠️ 흔히 인용되는 "360명"은 **회사 전체 규모**(엠바크 자사 목표 표현; 제3자 집계는 약 300명대)이지 *특정 게임 개발팀이 아니다* — Arc Raiders 프로젝트 팀은 리셋 후 약 25명 코어(아래 6번)

**3. 범위 통제**
- 불필요한 콘텐츠 과감히 삭제: 아스트로봇 오픈 레벨 1개 폐기
- 단순함 추구: 버튼 수·단어 수·기능 수 최소화 (팀 아소비)

**4. 팀 전체의 생산 기여**
- 모든 직군이 브레인스토밍 참여 (팀 아소비)
- [[designer-empowerment|디자이너 도구화]]: 프로그래머가 만든 도구로 디자이너가 콘텐츠 직접 제작 (샌드폴)

**5. 잘라내기 문화 (서커펀치)**
- "cutting is sharpening" — 매주 컷 미팅, 팀원 누구나 "이게 정말 필요한가?" 질문 가능
- 빈 맵 구역 삭제: 채우려는 강박을 버리고 30분 만에 더 나은 풍경으로 전환
- [[vision-statement|비전 선언문]]이 잘라내기의 기준: 만트라에 맞지 않으면 과감히 제거

**6. 강제된 집중 — 팀 리셋 (엠바크)**
- [[arc-raiders|아크 레이더스]]: 120명 → 25명으로 팀 축소. 이것이 오히려 집중을 만들어냄
- "좋은 것을 더 좋게 다듬을 여유가 없다. 지금 해결해야 할 문제에만 집중" — 카이오 브라가
- 아이디어가 훌륭해도 현재 문제와 무관하면 보류: "그게 지금 어떤 문제를 해결하는 건가요?"
- [[data-driven-development|데이터 기반 개발]]로 우선순위를 객관화: 3일 버스트 사이클 + 바구니 시스템

**7. 제약으로 공통 언어 만들기 (Asobo)**

[[asobo-studio|Asobo Studio]] (약 20명 아티스트, [[a-plague-tale-requiem|A Plague Tale: Requiem]]):
- "One Time Period, One Place, One Style" — 중세·남부 프랑스·클로드 로랭 회화로 창작 범위 고정
- 레이토모티프 "Focus on what matters": Megascans 보조 에셋 대체, Midpoly 메시, Displacement→Blend Map 재활용
- Fast Level Building: Day 1 블록아웃 → 1~2주 폴리시 — 방향 검증 먼저, 완성도는 나중

**8. 최소 인원으로 시작하기 — 닌텐도 원점 ([[shigeru-miyamoto|미야모토 시게루]])**

[[itoi-miyamoto-dialogue-2024|이토이 × 미야모토 대담]]에서 미야모토가 밝힌 닌텐도식 팀 구성 — 우리 위키의 여러 사례와 같은 결론에 닿는다:
- 최종 100~200명 프로젝트도 **처음엔 5명으로 시작**하고 30명을 넘기지 않는다.
- **초기 팀에 디자이너를 일부러 넣지 않는다**: 디자이너가 있으면 의존하게 되고 그림 완성을 기다리느라 지연된다. TV 화면에 매직으로 그리면 1분, 디자이너 경유하면 이틀 — 초기엔 직접 대충 그려 즉시 실험.
- **책임자는 디렉터 한 명**: 사람이 많으면 책임자도 애매해지고 반응이 느려진다. 틀리더라도 명확한 비전을 가진 한 명이 빠른 답을 만든다.
- "올스타 팀을 짜 오면 *너는 필요 없겠네*" — 부족함을 직접 메우다 한계에 부딪힐 때 비로소 인원을 늘린다.

**9. 스케일업의 함정 — 헬다이버스 2 반면교사 ([[arrowhead-game-studios|애로우헤드]])**

약 105명으로 2,000만+ 히트를 낸 [[helldivers-2|헬다이버스 2]]는 "소규모 대작"의 전형이지만, *어떻게 만들면 안 되는지*도 함께 보여준다:
- 개발 시작 약 20명 → 출시 약 105명 → 현재 약 130명. 그러나 총 7년 11개월(계획보다 4년+ 초과)
- 원인: **프리프로덕션(비전·범위 검증)을 생략하고 곧장 대규모 프로덕션 직행** — Pilestedt "정말 나쁜 생각이었다"
- 교훈(차기작): *작은 팀으로 프리프로덕션부터.* → 위 8번(닌텐도 최소 인원 시작)·[[rapid-prototyping|검증 먼저]]와 정확히 수렴. **검증 없이 스케일업하면 결정 비용을 가장 비싼 단계(프로덕션)에서 치른다.**

> 💡 **핵심 인사이트:** 소규모의 해답은 '덜 만드는 것'이 아닌 '더 잘 나누는 것'. 제약이 명확한 구조를 설계할 때 팀 전체가 생산적이 된다. Asobo의 사례는 한 가지를 더 추가한다 — **제약이 명확할수록 의사결정 비용이 줄어든다**: 시대·장소·스타일이 정해지면 팀은 "어떻게 만들까"에만 집중할 수 있다.
