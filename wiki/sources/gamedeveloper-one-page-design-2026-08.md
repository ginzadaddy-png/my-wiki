---
title: "Game Developer — 원페이지 디자인 문서 (Stone Librande, 2026-08)"
type: source-summary
source_url: "https://www.gamedeveloper.com/design/pushing-the-limits-in-simulating-a-city-one-page-at-a-time"
source_author: "Danielle Riendeau (Game Developer)"
source_published: 2026-08-07
sources: []
related: ["[[design-documentation|디자인 문서화]]", "[[vision-statement|비전 선언문]]", "[[designer-empowerment|디자이너 도구화]]", "[[dev-org-structure|개발 조직 구조]]", "[[masahiro-sakurai|사쿠라이 마사히로]]", "[[producer-role|프로듀서 역할]]"]
created: 2026-08-10
updated: 2026-08-10
confidence: medium
---

**원문**: [Pushing the limits in Simulating a City, One Page at a Time](https://www.gamedeveloper.com/design/pushing-the-limits-in-simulating-a-city-one-page-at-a-time) — Game Developer, Danielle Riendeau, 2026-08-07

**보조 원전**: 같은 저자의 [The goal of design is to efficiently communicate ideas](https://www.gamedeveloper.com/design/-the-goal-of-design-is-to-efficiently-communicate-ideas-) (2026-07-16) + [Video: One-page designs](https://www.gamedeveloper.com/design/video-one-page-designs) (2023-08-08, Librande의 GDC 2010 강연 소개). 세 편 모두 Stone Librande의 *원페이지 디자인* 방법론을 다루며, 본 페이지는 이를 종합한다.

Stone Librande(당시 EA, 현 Riot 디자인 리드)가 **SimCity(2013) 전 제작 기간을 오직 한 장짜리 설계 문서만으로 굴려본 실험**의 기록. 게임 디자인 문서(GDD)의 고전적 문제 — *아무도 안 읽는다* — 에 대한 형식 차원의 대답이다.

## 전통적 GDD의 진단

Librande가 2010년 GDC에서 든 문제는 세 가지다.

- **아무도 읽지 않는다** — 장문 GDD도, 위키로 옮긴 버전도 마찬가지
- **관계가 끊긴다** — 위키 형식은 설계 요소 사이의 연결을 유지하지 못한다
- **디자인 바이블 포맷이 실무에서 다루기 어렵다**

## 대안 — 주석 달린 한 장

핵심은 "짧게 쓰기"가 아니라 **형식을 글에서 그림으로 바꾸기**다.

- 다이어그램·순서도·매트릭스·스토리보드를 쓰되 *읽히는 선에서만*
- 여백을 넉넉히 두고 중앙 이미지 + 맥락을 주는 주석
- 건축 도면·엔지니어링 스키매틱·아동 교육 자료에서 시각 전략을 빌려온다
- **사무실 벽에 걸고 싶을 만큼** 매력적으로 만드는 것이 실제 목표

> **"한 장에 이것저것 욱여넣으면 안 된다. 상대적으로 단순하게, 서로 맞물려야 한다."** (Librande)

## SimCity 실험 — 어디까지 밀 수 있나

5명 팀에서 시작해 프리프로덕션부터 출시까지 전 주기를 원페이지로 굴렸다. *"어디까지 밀어붙일 수 있는지, 그리고 거기서 뭘 배우는지"* 가 스스로 건 질문이었다.

| 사례 | 내용 |
|---|---|
| **초기 도시 맵** | 실제 미국 도시를 참고. 단 *실측 지표에는 예술적 재량*을 뒀다 — 진짜 도시는 주차장이 너무 많다 |
| **멀티플레이 교역** | 한 장에 그려보니 초기 구상이 지저분했다 → **자원 낭비 전에 조기에 잘라냄** |
| **Coal City 매트릭스** | 프로듀서가 *"제조 플랜트 등급·모듈·보조 장난감까지 전부, 소화 가능한 형태로"* 한 장에 담아 달라고 요청 |

복잡도가 올라가자 스프레드시트·CSV를 끌어들여 **색상 코딩과 시각적 장치를 입힌 차트-다이어그램 혼합 문서**로 진화시켰고, 결국 *한 벽면 디자인*, *한 방 디자인*까지 확장했다. 저자는 **복잡한 시스템은 결국 여러 장을 필요로 한다**는 한계를 그대로 인정한다.

> 💡 **핵심 인사이트:** 원페이지의 진짜 값어치는 산출물이 아니라 **제약이 강제하는 사고**에 있다. 한 장에 담으려면 설계를 완전히 이해해야 하고, 여러 대안을 검토해야 하고, *"지금 이 문서에서 정말 전달해야 할 가장 중요한 것은 무엇인가"* 를 물어야 한다. 즉 이 방법은 더하기가 아니라 **덜어내기를 훈련시키는 도구**다.

## 초안은 예쁘고 틀린다

Librande의 Spore 사례 — 첫 시안은 보기에 좋았지만("드림캐처 같았다") 설계를 정확히 표현하지 못했다. **못생긴 스프레드시트를 거치는 여러 차례 개정** 끝에야 제대로 된 다이어그램이 나왔다. 원페이지는 한 번에 나오는 산출물이 아니라 반복의 결과다.

## 배포가 접근성보다 중요하다

> **"팀에 정말 중요한 할 말이 있다면, 그걸 그들에게 *가져가야* 한다."** (Librande)

- 인쇄해서 눈에 띄는 곳에 붙인다. 디지털(Miro 보드)과 물리(화이트보드·출력물) 양쪽 다
- 시작은 동료가 자기 사무실에 원페이지를 걸어둔 걸 본 것 — *만질 수 있고 보이는* 문서의 힘을 확인한 계기
- 문서를 *어딘가에 두고 찾아오게 하는* 방식과 반대되는 태도

## 장기 효과

포스트모템에서 확인된 것은 **다이어그램이 수년 뒤에도 여전히 유효**했다는 점이다.

> **"우리는 아직도 그걸 계속 참조한다. 프로젝트가 최상위 레벨부터 가장 작은 디테일까지 정리된 방식은 큰 승리였다."**

## 기존 위키 연결

- [[design-documentation]]: 이 소스가 해당 개념 페이지의 기준 자료
- [[vision-statement]]: 한 문장으로 팀을 정렬하는 축의 *문서 형식* 대응물. 비전이 *왜·무엇을*이라면 원페이지는 *어떻게 생겼는지*를 같은 밀도로 압축한다
- [[masahiro-sakurai]]: 사쿠라이의 *"기획서는 두께가 아니라 읽는 사람이 그림을 그릴 수 있느냐"* 와 정확히 같은 명제 — 서구·일본 두 계보가 독립적으로 도달한 지점
- [[designer-empowerment]]: 디자이너 산출물의 형식을 바꿔 팀 전체가 읽을 수 있게 만드는 접근
- [[producer-role]]: SimCity 사례에서 원페이지를 *요구한 쪽*이 프로듀서였다는 점 — 정렬 도구로서의 수요

> ⚠️ **자료 성격:** 세 기사 모두 Game Developer 편집장이 Librande의 GDC 강연(2010·2013)을 소개·재조명한 **2차 정리물**이다. 강연 원본(GDC Vault) 자체는 미확인. 정량 데이터가 없는 방법론 자료이므로 confidence medium.
