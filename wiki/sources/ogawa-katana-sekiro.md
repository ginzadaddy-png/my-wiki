---
title: "OGAWA SOUND 'KATANA'·'MOTION SFX' 라이브러리 — 세키로 적용 (공식 성과)"
type: source-summary
source_url: "https://www.ogawasound-online.com/en/post/【achievements】ogawa-sound-s-sound-effect-material-was-used-for-sekiro-shadows-die-twice"
source_author: "OGAWA SOUND (공식)"
source_published: 2022-02-22
sources: ["raw/articles/2026-06-16-gemini-deepresearch-sekiro-combat-sound.md"]
related: ["[[sekiro|세키로]]", "[[sound-design|사운드·음악 디자인]]", "[[gameplay-feedback-audio|게임플레이 피드백 오디오]]"]
created: 2026-06-16
updated: 2026-06-16
confidence: medium
---

**원문**: [ogawasound-online.com (공식 성과 포스트)](https://www.ogawasound-online.com/en/post/【achievements】ogawa-sound-s-sound-effect-material-was-used-for-sekiro-shadows-die-twice) — OGAWA SOUND, 2022-02-22
> 출처 주의: Gemini Deep Research 보고서(raw/articles/2026-06-16-gemini-deepresearch-sekiro-combat-sound.md)가 인용한 오가와 사운드 공식 포스트. 보고서 단계에서 1차 교차검증됨. 직접 재확인 권장 (confidence medium).

[[sekiro|세키로]]의 검격 효과음이 *전적으로 인하우스 폴리만으로* 만들어진 게 아니라, 일본 전문 오디오사 OGAWA SOUND의 조립식 효과음 라이브러리를 도입했음을 보여주는 1차 근거.

## 핵심 포인트

- **'SOUND MODEL KIT SERIES vol.2 KATANA'**: 96kHz/32bit float 고해상도, 충돌음·칼집 마찰음·코등이 떨림(Tsuba ringing) 등 **230개 부품 음원**. 칼-칼 맞부딪침(sword-to-sword clash) 설계의 핵심 성분으로 사용.
- **'SOUND MODEL KIT SERIES vol.3 MOTION SFX'**: 갈고리 로프 와이어의 고속 공중이동 마찰 질감에 병행 사용.
- 개발진은 부품 음원을 *프레임별 공격·방어 단계*에 맞춰 정밀 배치·결합.

> 💡 **핵심 인사이트:** "최고의 전투 효과음"이 반드시 100% 자체 녹음을 뜻하진 않는다. 세키로는 *부품화된 전문 라이브러리(조립식 KIT)*를 프레임 단위 어쿠스틱 싱크에 맞춰 재조립해 최상의 쇳소리 반응을 만들었다 — 효과음의 모듈화 운용 사례.
