---
topic_id: 31773
title: "Slicer Crashes When Deleting Segments From Totalsegmentator"
date: 2023-09-18
url: https://discourse.slicer.org/t/31773
---

# Slicer crashes when deleting segments from TotalSegmentator segmentation result

**Topic ID**: 31773
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-deleting-segments-from-totalsegmentator-segmentation-result/31773

---

## Post #1 by @hepato (2023-09-18 15:46 UTC)

<p>When I use Total segmentator ,slicer breakdown when I delete some 3d data which I do not need ,just as screenshot pictures</p>
<p>can anyone tell me how to resolve this problem?<br>
is there something wrong with my computer?  hardware  not good enough to  run this program？or just slicer software error?</p>
<p>slicer version 5.4 .0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc932e603ec3205162142b6a87cfc745d6cc257e.jpeg" data-download-href="/uploads/short-url/A2nEIs8ASXe3ZxBOG1MbqS9W6Xs.jpeg?dl=1" title="截屏2023-09-18 23.39.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc932e603ec3205162142b6a87cfc745d6cc257e_2_690x422.jpeg" alt="截屏2023-09-18 23.39.48" data-base62-sha1="A2nEIs8ASXe3ZxBOG1MbqS9W6Xs" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc932e603ec3205162142b6a87cfc745d6cc257e_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc932e603ec3205162142b6a87cfc745d6cc257e_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc932e603ec3205162142b6a87cfc745d6cc257e_2_1380x844.jpeg 2x" data-dominant-color="9A9296"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-09-18 23.39.48</span><span class="informations">1920×1177 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ec0a37ff84b13b8cce66ab4219e35d838db462.png" data-download-href="/uploads/short-url/ap65E2EdgaOSUprdEdqvDmo8EJs.png?dl=1" title="qwqw" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec0a37ff84b13b8cce66ab4219e35d838db462_2_690x441.png" alt="qwqw" data-base62-sha1="ap65E2EdgaOSUprdEdqvDmo8EJs" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ec0a37ff84b13b8cce66ab4219e35d838db462_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ec0a37ff84b13b8cce66ab4219e35d838db462.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ec0a37ff84b13b8cce66ab4219e35d838db462.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">qwqw</span><span class="informations">832×532 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-19 02:14 UTC)

<p>Thanks for reporting this issue. Could you please check if you can reproduce this with the latest Slicer Preview Release?</p>
<p>I could not reproduce this issue on my computer based on what you described (Slicer correcyly deleted the selected segments and did not crash). Does this happen all the time or just randomly in some cases? Would you be able to record a screen capture video that shows what you do exactly after TotalSegmentator has finished the segmentation?</p>

---

## Post #3 by @hepato (2023-09-19 12:07 UTC)

<p>Thanks for your answer！<br>
It happened recently ，not in all cases，just in some cases.<br>
I use slicer of version 5.4.0.<br>
Acording to your answer，I reinstall the slicer of Preview Release version（5.5.0 2023-09-13）.And slicer do not crash again!<br>
Thank you!</p>

---

## Post #4 by @Jmarcs (2023-09-20 17:10 UTC)

<p>It is a real issue in 5.4 One solution for the moment . You may duplicate the segment and delete the original segment. 3dslicer doesn’t crash</p>

---
