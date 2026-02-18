# How to change the default model's coordinate

**Topic ID**: 21209
**Date**: 2021-12-26
**URL**: https://discourse.slicer.org/t/how-to-change-the-default-models-coordinate/21209

---

## Post #1 by @slicer365 (2021-12-26 04:24 UTC)

<p>When I export model from Slicer</p>
<p>and I import it into another viewer software</p>
<p>the coordinate is wrong like this pic.</p>
<p>How to change the default.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1770a369a1567bd92df1b9824d629f9203cf45a.png" alt="捕获" data-base62-sha1="ys66Xdgb62VZ3SWWdaXRmTDWmy6" width="299" height="257"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8415520b12969058b85b452ded71bd0e3d6a260.png" alt="捕获" data-base62-sha1="szxt2urF1cBefN1FYPXq1vMfzRm" width="282" height="197"></p>

---

## Post #2 by @yulaomao (2021-12-27 03:03 UTC)

<p>You can select the export coordinate system in the segmentation module, such as Ras or LPS. However, generally, the default LPS coordinate system is exported, and there will be no problem viewing it in other software. Maybe the problem is that your software uses other coordinate systems, so you need to manually rotate the model and export it after curing.</p>

---

## Post #3 by @yulaomao (2021-12-27 03:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44c3e36b529a31fea2deadab2f8686fd5c76cf1e.png" data-download-href="/uploads/short-url/9Ok9IXLk5wVNbyvt6qYQy8e8HKK.png?dl=1" title="2021-12-27 10-59-25屏幕截图" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c3e36b529a31fea2deadab2f8686fd5c76cf1e_2_267x500.png" alt="2021-12-27 10-59-25屏幕截图" data-base62-sha1="9Ok9IXLk5wVNbyvt6qYQy8e8HKK" width="267" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c3e36b529a31fea2deadab2f8686fd5c76cf1e_2_267x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c3e36b529a31fea2deadab2f8686fd5c76cf1e_2_400x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44c3e36b529a31fea2deadab2f8686fd5c76cf1e_2_534x1000.png 2x" data-dominant-color="EBEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-12-27 10-59-25屏幕截图</span><span class="informations">613×1145 96.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
