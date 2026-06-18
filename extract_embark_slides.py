#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Embark 캐릭터 파이프라인 슬라이드 추출 + 보고서 캐러셀 삽입 스크립트
- Cowork 샌드박스에서는 (a) 영상 다운로드 제한 (b) 브라우저 base64 반출 차단 (c) save_to_disk 미지원
  으로 이미지 바이트를 보고서에 넣을 수 없어, 제약 없는 로컬(Claude Code/터미널)에서 실행하도록 분리함.
- 추출 지점(timestamp)과 크롭 좌표는 Cowork에서 영상을 직접 재생·캡쳐해 '검증 완료'한 값임.

필요: yt-dlp, ffmpeg  (예: pip install yt-dlp / brew|choco install ffmpeg)
실행: python extract_embark_slides.py   (이 파일은 my-wiki 루트에 있다고 가정)
"""
import os, re, glob, subprocess, sys

VID_URL = "https://www.youtube.com/watch?v=UFeC-VBbO90"  # Embark "Freedom Through Structure" GDC 2026
HERE    = os.path.dirname(os.path.abspath(__file__))
PRES    = os.path.join(HERE, "wiki", "presentations")
REPORT  = os.path.join(PRES, "ai-asset-pipeline-2026-report.html")

# 검증된 슬라이드 지점(초) — 1:17(타이틀), 2:TECHNOLOGIES, 3:CONNECTION TO HOUDINI, 4:(중반), 5:HEAVY LIFTING/WRAP
FRAMES = [(1, 17), (2, 339), (3, 579), (4, 918), (5, 1420)]
# 1920x1080 프레임 기준 슬라이드 영역(우측 발표자 화면 제외): x=0, y=170, w=1360, h=860
CROP = "crop=1360:860:0:170"

def run(cmd):
    print("·", " ".join(cmd)); subprocess.run(cmd, check=True)

def main():
    if not os.path.isfile(REPORT):
        sys.exit(f"보고서를 못 찾음: {REPORT}")
    # 1) 영상 다운로드 (1080p 이하 비디오 트랙)
    run(["yt-dlp", "-f", "bv*[height<=1080]+ba/b[height<=1080]",
         "-o", os.path.join(HERE, "_embark.%(ext)s"), VID_URL])
    vid = glob.glob(os.path.join(HERE, "_embark.*"))[0]

    # 2) 프레임 추출 + 크롭 → presentations/embark-slide-N.jpg
    imgs = []
    for i, t in FRAMES:
        out = os.path.join(PRES, f"embark-slide-{i}.jpg")
        run(["ffmpeg", "-y", "-ss", str(t), "-i", vid, "-frames:v", "1",
             "-vf", CROP, "-q:v", "3", out])
        imgs.append(f"embark-slide-{i}.jpg")
    print("저장:", imgs)

    # 3) 캐러셀 HTML 생성 (좌우 삼각형 버튼 + 카운터)
    slide_imgs = "\n          ".join(
        f'<img class="emcar-img" src="{src}" alt="Embark 캐릭터 파이프라인 슬라이드 {i+1}" '
        f'style="display:{"block" if i==0 else "none"};width:100%;border-radius:6px">'
        for i, src in enumerate(imgs))
    carousel = f'''<figure>
      <div class="fig-box">
        <div class="emcar" id="emcar-embark">
          <style>
          .emcar{{position:relative;max-width:780px;margin:0 auto}}
          .emcar-img{{display:block;width:100%}}
          .emcar-btn{{position:absolute;top:50%;transform:translateY(-50%);width:46px;height:46px;border:none;border-radius:50%;background:rgba(20,20,19,.55);color:#fff;font-size:18px;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:2;transition:background .2s}}
          .emcar-btn:hover{{background:rgba(194,96,63,.92)}}
          .emcar-btn.prev{{left:10px}} .emcar-btn.next{{right:10px}}
          .emcar-counter{{position:absolute;bottom:10px;right:12px;background:rgba(20,20,19,.62);color:#fff;font-size:12px;padding:3px 10px;border-radius:999px;z-index:2;font-variant-numeric:tabular-nums}}
          </style>
          {slide_imgs}
          <button class="emcar-btn prev" aria-label="이전 슬라이드" onclick="emcarMove('emcar-embark',-1)">&#9664;</button>
          <button class="emcar-btn next" aria-label="다음 슬라이드" onclick="emcarMove('emcar-embark',1)">&#9654;</button>
          <div class="emcar-counter">1 / {len(imgs)}</div>
        </div>
      </div>
      <figcaption><b>Embark 발표 슬라이드</b> GDC 2026 "Freedom Through Structure: Character Pipelines at Embark"에서 추출(우측 발표자 화면 제외). 좌우 &#9664; &#9654; 버튼으로 넘겨 보세요. (출처: SideFX·Houdini YouTube)</figcaption>
    </figure>
    <script>function emcarMove(id,d){{var c=document.getElementById(id);var im=c.querySelectorAll('.emcar-img');var cur=0;for(var i=0;i<im.length;i++){{if(im[i].style.display!=='none'){{cur=i;break;}}}}im[cur].style.display='none';var n=(cur+d+im.length)%im.length;im[n].style.display='block';var ct=c.querySelector('.emcar-counter');if(ct)ct.textContent=(n+1)+' / '+im.length;}}</script>'''

    # 4) 보고서의 기존 UFeC 썸네일 figure를 캐러셀로 교체
    html = open(REPORT, encoding="utf-8").read()
    pat = re.compile(
        r'<figure>\s*<div class="fig-box">\s*'
        r'<img src="https://i\.ytimg\.com/vi/UFeC-VBbO90/maxresdefault\.jpg".*?</figure>',
        re.S)
    new_html, n = pat.subn(carousel, html, count=1)
    if n == 0:
        snippet = os.path.join(HERE, "embark_carousel_snippet.html")
        open(snippet, "w", encoding="utf-8").write(carousel)
        print(f"[주의] 보고서에서 UFeC 썸네일 figure를 못 찾았습니다. 캐러셀을 {snippet} 로 저장했으니 수동 삽입하세요.")
    else:
        open(REPORT, "w", encoding="utf-8").write(new_html)
        print("보고서에 캐러셀 삽입 완료:", REPORT)

    os.remove(vid)
    print("\n완료. 배포 시 presentations/embark-slide-*.jpg 가 public/presentations/ 로 복사되는지 확인하세요")
    print("(Quartz Assets emitter가 자동 복사하는 게 일반적이나, 누락되면 deploy.yml에 jpg copy step 추가).")

if __name__ == "__main__":
    main()
