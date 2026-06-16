---
title: "Project Triton / Project Acoustics — Pre-Computed Wave Acoustics"
type: source-summary
source_url: "https://www.microsoft.com/en-us/research/project/project-triton/"
source_author: "Nikunj Raghuvanshi 외 (Microsoft Research)"
source_published: 2017-03
sources: ["raw/articles/2026-06-16-gemini-deepresearch-sound-design.md"]
related: ["[[sound-design|사운드·음악 디자인]]", "[[gameplay-feedback-audio|게임플레이 피드백 오디오]]"]
created: 2026-06-16
updated: 2026-06-16
confidence: medium
---

**원문**: [microsoft.com/research/project/project-triton](https://www.microsoft.com/en-us/research/project/project-triton/) — Nikunj Raghuvanshi 외 (Microsoft Research)
> 출처 주의: Gemini Deep Research 보고서(raw/articles/2026-06-16-gemini-deepresearch-sound-design.md) 기반 요약. 1차 자료 재검증 권장 (confidence medium).

기하 레이트레이싱 음향이 못 푸는 *회절(diffraction)*을 파동 물리로 모델링한 공간 오디오 기술.

## 핵심 포인트

- **가로등 문제(Lamppost Problem)**: 음향 레이트레이싱은 빛처럼 직진만 가정해, 가는 기둥 뒤에서 소리가 갑자기 사라지는 왜곡 발생. 실제 소리는 모서리를 돌아 휘는 회절을 가짐.
- **오프라인 베이킹 → 런타임 저부하**: 3D 메시에서 파동 방정식으로 전파·반사·회절을 클러스터 연산 시뮬 → **구면조화함수(Spherical Harmonics)** 매트릭스로 압축 → 런타임은 CPU 부하 거의 없이 회절 감쇠·도어 포탈링(열린 문틈으로만 소리 새어나옴)을 매핑.
- 적용: Gears of War 4·Sea of Thieves·Borderlands 3.

> 💡 **핵심 인사이트:** 공간 오디오의 사실성은 반사뿐 아니라 *회절*을 얼마나 다루느냐에서 갈린다. 무거운 파동 연산을 오프라인 베이킹으로 옮기면 런타임 비용 없이 물리적 음향 전파를 얻는다 — HRTF 기반 실시간 필터링과 대비되는 접근.
