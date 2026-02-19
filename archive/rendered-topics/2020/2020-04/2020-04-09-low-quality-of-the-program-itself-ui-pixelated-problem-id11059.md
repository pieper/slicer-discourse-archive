---
topic_id: 11059
title: "Low Quality Of The Program Itself Ui Pixelated Problem"
date: 2020-04-09
url: https://discourse.slicer.org/t/11059
---

# Low quality of the program itself (UI pixelated problem)

**Topic ID**: 11059
**Date**: 2020-04-09
**URL**: https://discourse.slicer.org/t/low-quality-of-the-program-itself-ui-pixelated-problem/11059

---

## Post #1 by @Jakub_Balicki (2020-04-09 16:08 UTC)

<p>Hello,<br>
I’ve downloaded 3slicer on ubuntu and I have this strange problem where UI is pixelated as shown on the attached image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f09a1bb03693d16dfb010781496655d11b073ec.png" data-download-href="/uploads/short-url/i7Ph1W42yD6doNM9pdJMWMcn9y4.png?dl=1" title="Screenshot from 2020-04-09 15-33-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f09a1bb03693d16dfb010781496655d11b073ec_2_690x388.png" alt="Screenshot from 2020-04-09 15-33-16" data-base62-sha1="i7Ph1W42yD6doNM9pdJMWMcn9y4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f09a1bb03693d16dfb010781496655d11b073ec_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f09a1bb03693d16dfb010781496655d11b073ec_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f09a1bb03693d16dfb010781496655d11b073ec_2_1380x776.png 2x" data-dominant-color="C1C0C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-04-09 15-33-16</span><span class="informations">1920×1080 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve tried different versions of the program and the problem still occurs.</p>

---

## Post #2 by @lassoan (2020-04-09 17:17 UTC)

<p>Probably your sysytem settings for Qt application scaling need some tuning. See for example <a href="https://techienotes.blog/2019/01/21/fix-qt-apps-scaling-issue-on-hidpi-screens-on-ubuntu/">here</a> specifications <a href="https://doc.qt.io/qt-5/highdpi.html#high-dpi-support-in-qt">here</a>.</p>

---
