---
topic_id: 6737
title: "Slicerrt Dose And Colorbar"
date: 2019-05-09
url: https://discourse.slicer.org/t/6737
---

# SlicerRT, dose and colorbar

**Topic ID**: 6737
**Date**: 2019-05-09
**URL**: https://discourse.slicer.org/t/slicerrt-dose-and-colorbar/6737

---

## Post #1 by @PaoloZaffino (2019-05-09 14:55 UTC)

<p>Hi all,<br>
I have a CT with a dose cube and I can import and visualize them in Slicer (v.4.10).</p>
<p>At this point would like to show also a colorbar for the dose.</p>
<p>Do you have any suggestion?</p>
<p>Thank you very much.<br>
Paolo</p>

---

## Post #2 by @cpinter (2019-05-09 15:14 UTC)

<p>Go to the Isodose module and use the checkboxes on the bottom. You <em>don’t</em> actually need to calculate an isodose for showing the scalar bars, just check the boxes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e60e06ceaaf43a04484b414c8ac438319e9494d1.png" data-download-href="/uploads/short-url/wP9RWpUPjL8F5w6co282AB5Iqxr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e60e06ceaaf43a04484b414c8ac438319e9494d1_2_690x386.png" alt="image" data-base62-sha1="wP9RWpUPjL8F5w6co282AB5Iqxr" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e60e06ceaaf43a04484b414c8ac438319e9494d1_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e60e06ceaaf43a04484b414c8ac438319e9494d1_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e60e06ceaaf43a04484b414c8ac438319e9494d1_2_1380x772.png 2x" data-dominant-color="918E87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1660×929 348 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @PaoloZaffino (2019-05-09 15:26 UTC)

<p>Thanks a lot <a class="mention" href="/u/cpinter">@cpinter</a>!<br>
I thought I had to compute isodose first.</p>
<p>Paolo</p>

---

## Post #4 by @cpinter (2019-05-09 16:38 UTC)

<aside class="quote no-group" data-username="PaoloZaffino" data-post="3" data-topic="6737">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paolozaffino/48/81052_2.png" class="avatar"> PaoloZaffino:</div>
<blockquote>
<p>I thought I had to compute isodose first</p>
</blockquote>
</aside>
<p>No, you do NOT have to calculate isodose. Just the checkbox, that’s all</p>

---
