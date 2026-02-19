---
topic_id: 3403
title: "Dce Analysis Fitted Signal Curve Does Not Make Sense"
date: 2018-06-26
url: https://discourse.slicer.org/t/3403
---

# DCE analysis - Fitted signal curve does not make sense

**Topic ID**: 3403
**Date**: 2018-06-26
**URL**: https://discourse.slicer.org/t/dce-analysis-fitted-signal-curve-does-not-make-sense/3403

---

## Post #1 by @bmb777 (2018-06-26 21:02 UTC)

<p>Is the issue with the Output Fitted Data 4D a common issue? I believe I am having the same difficulty with viewing the fitted results as what is shown above and wonder if there is a way to fix/work around this. Specifically the output 4D data shows a flat baseline for all the voxels similar to what Sharon showed in post 25.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9466df47f0ddfba7acc8fb05d0c1579119764c36.jpeg" data-download-href="/uploads/short-url/laP4et5uyI4rQzM3ivFKDwJ62we.JPG?dl=1" title="Output%20fitted" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9466df47f0ddfba7acc8fb05d0c1579119764c36_2_644x500.JPG" alt="Output%20fitted" data-base62-sha1="laP4et5uyI4rQzM3ivFKDwJ62we" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9466df47f0ddfba7acc8fb05d0c1579119764c36_2_644x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9466df47f0ddfba7acc8fb05d0c1579119764c36.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9466df47f0ddfba7acc8fb05d0c1579119764c36.jpeg 2x" data-dominant-color="F8F7F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Output%20fitted</span><span class="informations">955×741 71.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @fedorov (2018-07-02 13:35 UTC)

<p><a class="mention" href="/u/bmb777">@bmb777</a> no, it should not be a common issue. This needs to be investigated, but I am strapped on time right now, and have no one to delegate.</p>
<p>Could you possibly <a href="https://github.com/QIICR/PkModeling/issues/new">submit an issue to PkModeling</a> and include a pointer to a dataset that allows to reproduce this problem?</p>

---

## Post #3 by @bmb777 (2018-07-03 15:39 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a><br>
edit 2: The issue was cause by me prescribing the AIF  with units of milliseconds rather than seconds. Changing this corrected the issue.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/155dffcff7a02921af0c75286e2c9534a753a76e.jpeg" data-download-href="/uploads/short-url/331q064JAywaIraW93qVExZlmTY.JPG?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/155dffcff7a02921af0c75286e2c9534a753a76e_2_690x461.JPG" alt="Capture3" data-base62-sha1="331q064JAywaIraW93qVExZlmTY" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/155dffcff7a02921af0c75286e2c9534a753a76e_2_690x461.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/155dffcff7a02921af0c75286e2c9534a753a76e_2_1035x691.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/155dffcff7a02921af0c75286e2c9534a753a76e.jpeg 2x" data-dominant-color="F9F9F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1086×726 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @fedorov (2018-07-06 15:05 UTC)

<p><a class="mention" href="/u/bmb777">@bmb777</a> I am glad you resolved it, and I really appreciate that you took the time to post the resolution back to the forum! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---
