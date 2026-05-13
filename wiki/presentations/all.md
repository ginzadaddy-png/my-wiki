---
title: "프레젠테이션 카탈로그"
type: catalog
created: 2026-05-12
updated: 2026-05-12
---

← [홈으로](../index.md)

위키 콘텐츠를 기반으로 제작한 HTML 슬라이드 모음. 각 슬라이드는 단일 HTML 파일로 제작되어 브라우저에서 그대로 열람 가능. 추후 slide 생성 도구로 갱신·확장.

## 슬라이드 목록

| 제목 | 주제 | 출처 | 위키 페이지 | 슬라이드 |
|------|------|------|------|------|
| Steam 마케팅 전략 | 인디·중소 스튜디오용 Steam 출시·마케팅 종합 | [[marketing-strategy]], [[launch-metrics]], [[zukowski-next-fest-strategy]] | <a href="https://ginzadaddy-png.github.io/quartz/presentations/steam-marketing-strategy/">steam-marketing-strategy</a> | <a href="https://ginzadaddy-png.github.io/quartz/presentations/steam-marketing-strategy-deck.html" target="_blank" rel="noopener">전체 화면 열기 ↗</a> |

## 사용 규칙

- 슬라이드는 위키 콘텐츠를 *재구성*한 것 — 원전(concept·source) 페이지가 항상 truth source
- 슬라이드 갱신 시: 카탈로그의 출처 wikilink는 그대로 두고 슬라이드 HTML 파일만 교체
- **저장 경로**: `wiki/presentations/[슬러그]-deck.html` 한 곳으로 통일 (루트 `presentations/`는 deprecated)
- **wrapper 페이지**: 같은 폴더에 `[슬러그].md`로 만들어 위키 페이지로 노출 (iframe 임베드 + 전체 화면 열기 버튼)
- **slug 충돌 회피 (중요)**: 슬라이드 HTML은 반드시 `-deck` 접미사. wrapper md (`[슬러그].md`)와 슬라이드 HTML (`[슬러그].html`)이 같은 이름이면 Quartz의 ContentPage·Assets emitter가 같은 slug로 인식해 *.html URL이 wrapper md를 응답하는 무한 재귀 발생*
- 신규 슬라이드 추가 시: `-deck.html` 업로드 + wrapper md 작성 + 본 카탈로그에 행 추가 + `wiki/index.md` 카운트·섹션 갱신
- 파일 명명 규칙: 슬라이드 `[주제-슬러그]-deck.html`, wrapper `[주제-슬러그].md` (소문자·하이픈, base 슬러그는 공유)
- 링크 규칙: 카탈로그·index의 표 안 슬라이드 링크는 raw HTML + **완전 절대 URL** 사용 (`<a href="https://ginzadaddy-png.github.io/quartz/presentations/[슬러그]-deck.html" target="_blank" rel="noopener">전체 화면 열기 ↗</a>`) — Quartz가 root-relative path는 변형(`.html` 제거·baseUrl 처리)하지만 외부 절대 URL은 그대로 둠. markdown link도 같은 이유로 회피.
