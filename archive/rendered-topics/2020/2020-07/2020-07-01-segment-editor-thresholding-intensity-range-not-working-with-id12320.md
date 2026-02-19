---
topic_id: 12320
title: "Segment Editor Thresholding Intensity Range Not Working With"
date: 2020-07-01
url: https://discourse.slicer.org/t/12320
---

# Segment Editor; Thresholding intensity range not working with discrete Hounsfield Units of [0,1,2]

**Topic ID**: 12320
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/segment-editor-thresholding-intensity-range-not-working-with-discrete-hounsfield-units-of-0-1-2/12320

---

## Post #1 by @Linford_Briant (2020-07-01 13:33 UTC)

<p>Dear Slicer Community,</p>
<p>I have been using the Segment Editor to segment an image that takes on 3 discrete Hounsfield Units (0,1,2). The images contain 2 cells, cell1 is in HU=1, cell2 is in HU=2. The background is HU=0.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ccc913123b9ce0b6469aa70df44b842010ac748.png" data-download-href="/uploads/short-url/46LErnk8wH1kpZQe4fU4j9T3v7y.png?dl=1" title="screenshot_hu" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ccc913123b9ce0b6469aa70df44b842010ac748_2_690x474.png" alt="screenshot_hu" data-base62-sha1="46LErnk8wH1kpZQe4fU4j9T3v7y" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ccc913123b9ce0b6469aa70df44b842010ac748_2_690x474.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ccc913123b9ce0b6469aa70df44b842010ac748_2_1035x711.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ccc913123b9ce0b6469aa70df44b842010ac748_2_1380x948.png 2x" data-dominant-color="89898A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_hu</span><span class="informations">1564×1076 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I must not be using the Thresholding tool properly, because even if I set the intensity range correctly to get cell2 but not cell1 (thresholding with HU&gt;1.88) it will still segment both cells:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d275499ca34976e8207273e4e49cb80cb7f530dd.png" data-download-href="/uploads/short-url/u1Nyu2QTFLudTqvmeaoGx9gnSYl.png?dl=1" title="screenshot_hu1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d275499ca34976e8207273e4e49cb80cb7f530dd_2_690x473.png" alt="screenshot_hu1" data-base62-sha1="u1Nyu2QTFLudTqvmeaoGx9gnSYl" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d275499ca34976e8207273e4e49cb80cb7f530dd_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d275499ca34976e8207273e4e49cb80cb7f530dd_2_1035x709.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d275499ca34976e8207273e4e49cb80cb7f530dd_2_1380x946.png 2x" data-dominant-color="8A8783"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_hu1</span><span class="informations">1569×1076 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Alternatively, if I set the intensity range for threshold to be between 0.9 and 1.1 to segment out cell1 (and not cell2), it includes all the background!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e872b8dc6950883d8fc60c082c62c3e24dc7405b.png" data-download-href="/uploads/short-url/xakyYxUYQNysUxr26Xlq6N2JbNV.png?dl=1" title="screenshot_hu2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e872b8dc6950883d8fc60c082c62c3e24dc7405b_2_690x474.png" alt="screenshot_hu2" data-base62-sha1="xakyYxUYQNysUxr26Xlq6N2JbNV" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e872b8dc6950883d8fc60c082c62c3e24dc7405b_2_690x474.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e872b8dc6950883d8fc60c082c62c3e24dc7405b_2_1035x711.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e872b8dc6950883d8fc60c082c62c3e24dc7405b_2_1380x948.png 2x" data-dominant-color="E5DBC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_hu2</span><span class="informations">1564×1076 99.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What am I doing wrong? Any help would be really appreciated!!</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2020-07-01 16:21 UTC)

<p>This looks like a labelmap. Why don’t you import the volume as a labelmap and then convert to segmentation?</p>

---

## Post #3 by @Linford_Briant (2020-07-01 16:42 UTC)

<p>Thanks muratmaga for your help. How do I do this?</p>

---

## Post #4 by @muratmaga (2020-07-01 16:57 UTC)

<p>Go to <code>volumes</code> module, and then expand the Volume information, and click the convert to label map.<br>
Then go to <code>segmentations</code> module and under then import/export section, import the newly created labelmap as a segmentation.</p>

---

## Post #5 by @Linford_Briant (2020-07-02 19:20 UTC)

<p>OK, thanks muratmaga. Now I have done this, what do I do? How do I show them in 3D?</p>

---

## Post #6 by @Linford_Briant (2020-07-02 19:26 UTC)

<p>Working now, thank you!! <img src="https://emoji.discourse-cdn.com/twitter/star2.png?v=9" title=":star2:" class="emoji" alt=":star2:"></p>

---
