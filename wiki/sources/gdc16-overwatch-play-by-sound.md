---
title: "[GDC16] Overwatch — The Elusive Goal: Play by Sound"
type: source-summary
source_url: "https://gdcvault.com/play/1023010/Overwatch-The-Elusive-Goal-Play"
source_author: "Scott Lawlor, Tomas Neumann (Blizzard)"
source_published: 2016-03-14
sources: ["raw/articles/2026-06-16-gemini-deepresearch-sound-design.md"]
related: ["[[gameplay-feedback-audio|게임플레이 피드백 오디오]]", "[[sound-design|사운드·음악 디자인]]", "[[combat-design|전투 디자인]]"]
created: 2026-06-16
updated: 2026-06-16
confidence: medium
---

**원문**: [gdcvault.com/play/1023010](https://gdcvault.com/play/1023010/Overwatch-The-Elusive-Goal-Play) — Scott Lawlor·Tomas Neumann (Blizzard), GDC 2016
> 출처 주의: Gemini Deep Research 보고서(raw/articles/2026-06-16-gemini-deepresearch-sound-design.md) 기반 요약. GDC Vault 1차 강연 재검증 권장 (confidence medium).

경쟁형 FPS에서 오디오를 *"모니터를 꺼도 플레이 가능"*한 수준의 1차 전술 피드백으로 끌어올린 오버워치 사례.

## 핵심 포인트

- **최대 위협 시스템(Greatest Threat System)**: 정적 거리 감쇠를 버리고 매 프레임 *나를 조준 중인가·투사체를 격발했나·뒤편 근접인가*로 위협 스코어를 계산 → RTPC로 적대 영웅은 볼륨·명료도 최대, 아군·비위협은 백그라운드로 강제 덕킹해 믹스 선명도 보존.
- **발소리 피아 식별**: 아군 발소리는 주파수를 깎고, 적은 영웅별 시그니처(윈스턴 패드음·정크랫 의족 목재음·로드호그 쇠사슬)로 필터링 → 형상을 안 보고도 침투 방향·영웅 식별.
- **스마트 피드백**: 치유 시 체력 비례 피치 상승으로 완치 타이밍 감각, 타격 쾌감음은 맥주병 마개 "pssht" 역재생.

> 💡 **핵심 인사이트:** 청각 인지(~80–100ms)가 시각 해석보다 빠르다는 전제 위에서, 믹스를 *전술 위협도*로 실시간 재조정하면 사운드가 화면 밖 정보를 보정하는 1차 입력 장치가 된다. [[gameplay-feedback-audio]]의 대표 사례.
