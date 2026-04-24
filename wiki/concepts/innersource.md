---
title: "이너소스 (InnerSource)"
type: concept
sources: ["[[multiproject-innersource-report]]"]
related: ["[[dev-org-structure|개발 조직 구조]]", "[[multi-project-development|멀티 프로젝트 개발]]", "[[proprietary-engine-strategy|독자 엔진 전략]]"]
created: 2026-04-23
updated: 2026-04-23
confidence: high
---

오픈소스 개발 방식을 기업 내부(인트라넷) 에 적용하는 협업 모델. 코드·지식·의사결정 과정을 사내 전체에 투명하게 공개해 조직 내 사일로(silo)를 제거한다.

## 핵심 메커니즘

**Trusted Committer (TC)**
- 엔진·공유 라이브러리 등 특정 코드베이스의 "게이트키퍼"
- 외부 팀의 Pull Request를 리뷰하고 병합하는 권한 보유
- EA Frostbite 실패 패턴의 반대: 엔진 팀이 타 스튜디오의 기여를 막는 것이 아니라 **열어주는** 역할

**Pull Request 기반 엔진 개발**
- 게임 팀이 엔진 소스코드에 직접 PR을 제출
- 기다리는 것이 아니라 기여하는 구조 → 병목 원천 차단
- 캡콤 RE ENGINE 모델: 1,300명+ 개방 채널 + 하루 20건 직접 문의 → 병목 없음

**비동기 문서화 (Async Documentation)**
- 구두 전달 의존 탈피 → 변경 이유·맥락까지 텍스트로 기록
- 다른 팀이 질문 없이 코드를 이해하고 기여할 수 있는 기반

## 도입 사례

| 사례 | 적용 방식 |
|------|---------|
| [[capcom]] RE ENGINE | 전 개발자 소스 열람, 팀즈 채널 완전 개방, 전담 매니지먼트 유닛 |
| [[embark-studios]] | Rust 기반 코어 기술 GitHub 공개 → 외부 커뮤니티 기여 유도 |
| Ubisoft La Forge | 멀티 스튜디오 횡단 엔진 연구, Scalar 클라우드 스트리밍 공동 개발 |
| Riot Games | Zero Harm Comms 프레임워크로 스튜디오 간 지식 공유 |

## EA Frostbite — 반면교사

FPS 특화 엔진을 RPG 팀에 강제 이식, 엔진 팀을 비용 부서(Cost Center)로 취급하며 즉각 지원 불가. 이너소스와 정반대: 코드 폐쇄 + 강압적 중앙집중화 → 기술 부채·번아웃·인재 이탈.

## 성과 측정: 올바른 지표

파괴적 지표(코드 라인 수, 커밋 수)는 Goodhart's Law에 의해 목표 왜곡 유발. 이너소스 환경의 건강한 지표:

| 지표 | 측정 대상 |
|------|---------|
| Cycle Time | PR 제출 → 병합까지 시간 |
| Lead Time | 아이디어 → 배포까지 시간 |
| InnerSource Contribution Rate | 외부 팀 기여 PR 비율 |
| Unblocking Count | TC가 다른 팀 블로킹 해제한 건수 |

> 💡 **핵심 인사이트:** 이너소스는 단순한 코드 공유가 아니다. "엔진은 강제 규율이 아니라 게임 팀을 위한 협업적 서비스"라는 캡콤의 철학이 핵심이다. 기술 중앙화의 경제적 이점을 누리면서도 각 팀의 자율성을 보장하는 **소니 ICE 팀 모델**이 현재까지 가장 성공적인 하이브리드 구현이다.
