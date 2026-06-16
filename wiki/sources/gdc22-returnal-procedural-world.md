---
title: "[GDC22] Never The Same Twice: Procedural World Handling in 'Returnal'"
type: source-summary
source_url: "https://gdcvault.com/play/1028093"
source_author: "Ethan Watson (Housemarque)"
source_published: 2022-03
sources: ["raw/articles/2026-06-16-gemini-deepresearch-roguelike.md"]
related: ["[[roguelike|로그라이크]]", "[[pcg-pure-vs-hybrid|완전 절차생성 vs 하이브리드]]", "[[level-design-principles|레벨 디자인 원칙]]", "[[aaa-scaling-strategy|AAA 도전 전략]]"]
created: 2026-06-16
updated: 2026-06-16
confidence: medium
---

**원문**: [gdcvault.com/play/1028093](https://gdcvault.com/play/1028093) — Ethan Watson (Housemarque), GDC 2022
> 출처 주의: 본 요약은 Gemini Enterprise Deep Research 보고서(raw/articles/2026-06-16-gemini-deepresearch-roguelike.md, 2026-06-16)가 인용·정리한 내용을 옮긴 것으로, GDC Vault 1차 강연을 직접 확인하지 않았다. 인용 수치·표현은 1차 재검증 권장 (confidence medium).

AAA 스케일 3D 로그라이크가 절차적 월드를 어떻게 다루는지에 대한 하우스마크의 포스트모템. 2D·탑다운 아케이드 슈터에 최적화돼 있던 스튜디오가 언리얼 엔진 4로 고화질 3인칭 탄막 슈터를 만들며 겪은 구조적 충돌을 가감 없이 노출한다.

## 핵심 포인트

- **격자 그리드 조립의 포기**: 2D 로그라이크의 표준인 격자형 타일 조립은 고정밀 3D에서 그래픽 부자연스러움·물리 충돌 판정 깨짐을 유발 → 크기·높이가 제각각인 **비정형 룸을 유기적으로 조립하는 자유형 레이아웃**으로 전환.
- **수작업 공간 제약 매핑**: 룸별 잠금(Lockdown)·전투 구역을 안정 검증하기 위해 디자이너가 오목 입체 볼륨(Concave Volume)과 안전 연결점(Safe Connection Points)을 손수 매핑해 조립 제약식을 생성.
- **개발 리스크**: 기술적 마찰·복잡한 종속성으로 "개발 기간 전체의 절반 동안 플레이 불가능한 빌드가 장기 방치"됐다고 증언.
- **장르 규칙 수정 압박**: 고속 이동사격 + 물리 회피의 과도한 인지 부하가 난이도 불만으로, 런이 3시간을 상회하는 장기화로 이어져 결국 세이브 스컴 논란을 차단하며 플레이 중간 보존 **SUSPEND 임시 세이브**를 긴급 도입.

> 💡 **핵심 인사이트:** 2D 로그라이크의 PCG 관행은 3D AAA로 그대로 이식되지 않는다. 그리드를 포기하고 자유형 레이아웃 + 수작업 공간 제약으로 가야 하며, 런 길이·세이브 같은 *장르 규칙 자체*도 AAA 플레이 맥락에 맞춰 수정해야 한다. [[aaa-scaling-strategy|중소·신생 영역의 AAA 도전]]이 겪는 비용 구조의 한 단면.
