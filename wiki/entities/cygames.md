---
title: "Cygames (사이게임즈)"
type: entity
sources: ["[[cedec2026-granblue-relink-battle|CEDEC 2026 Relink 배틀 제작]]"]
related: ["[[granblue-fantasy-relink|GRANBLUE FANTASY: Relink]]", "[[combat-companion-ai|전투·조력 AI 동반자 설계]]", "[[mobile-gamedev|모바일 게임 개발]]", "[[ip-adaptation-design|IP 적응 설계]]"]
created: 2026-07-30
updated: 2026-07-30
confidence: medium
---

**Cygames**는 일본 도쿄 소재 개발사·퍼블리셔(2011 설립, 사이버에이전트 계열). 모바일 IP(그랑블루 판타지·섀도우버스·우마무스메 등)를 **콘솔·PC 액션 게임으로 확장**하는 흐름의 대표 사례로, CEDEC에 매년 다수 세션을 낸다.

> 💡 **핵심 특징 — 캐릭터 게임의 스케일 문제:** 다캐릭터 IP를 액션으로 옮기면 *캐릭터 수 × 스타일 수*가 곧 개발 부하가 된다. Relink는 28캐릭터 × 3 마스터 스타일 = 84 플레이 스타일을 *공통 데이터 포맷 + 파라미터 조정*으로 감당했다. → [[cedec2026-granblue-relink-battle]]

## 개발 방식

- **"80점보다 30점을 최속으로"** — 최소 애니메이션으로 며칠, 때로는 당일 검증
- 플래너·엔지니어·아티스트가 캐릭터 콘셉트를 함께 언어화해 중복 이터레이션 방지
- 동료 AI(Character AI + Meta AI)와 어시스트 모드가 **동일 아키텍처**를 공유 → 접근성 기능이 자동 플레이 QA 도구까지 겸용

## 관련 위키 페이지

- [[granblue-fantasy-relink|GRANBLUE FANTASY: Relink]] — 대표 콘솔 액션 타이틀
- [[combat-companion-ai|전투·조력 AI 동반자 설계]] — 동료 AI 이중 구조
- [[mobile-gamedev|모바일 게임 개발]] — 모바일 IP의 콘솔 확장 맥락
