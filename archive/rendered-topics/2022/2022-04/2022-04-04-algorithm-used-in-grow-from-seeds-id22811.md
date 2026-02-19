---
topic_id: 22811
title: "Algorithm Used In Grow From Seeds"
date: 2022-04-04
url: https://discourse.slicer.org/t/22811
---

# Algorithm used in grow from seeds

**Topic ID**: 22811
**Date**: 2022-04-04
**URL**: https://discourse.slicer.org/t/algorithm-used-in-grow-from-seeds/22811

---

## Post #1 by @MPhilip (2022-04-04 09:15 UTC)

<p>Hi<br>
Could you please guide me to relevant documentation of grow from seeds effect implemented on 3D slicer detailing the algorithm used?<br>
I have found this paper in the documentation, * The method uses an improved version of the grow-cut algorithm described in <em>Liangjia Zhu, Ivan Kolesov, Yi Gao, Ron Kikinis, Allen Tannenbaum. An Effective Interactive Medical Image Segmentation Method Using Fast GrowCut, International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), Interactive Medical Image Computing Workshop, 2014.</em> is this the same paper the tool is developed based on? if no, could you please share the link to the paper?<br>
I have also found this <a href="https://discourse.slicer.org/t/algorithm-used-for-growing-seeds/11817">thread</a>, but could not find the relevant paper.</p>
<p>Thanks</p>

---

## Post #2 by @gaoyi.cn (2022-04-04 09:51 UTC)

<p>Yes that’s the paper this module is based on.</p>
<p>Please let us know if there is anything we could of help</p>
<p>yi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png" data-download-href="/uploads/short-url/8lHbc8ewzqTHYpSOyVLQwZxlrCe.png?dl=1" title="841F8A606C9E466C9FD5610F03B4BC6F.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png" alt="841F8A606C9E466C9FD5610F03B4BC6F.png" data-base62-sha1="8lHbc8ewzqTHYpSOyVLQwZxlrCe" width="690" height="1" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 2x" data-dominant-color="BECCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841F8A606C9E466C9FD5610F03B4BC6F.png</span><span class="informations">708×2 103 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @MPhilip (2022-08-03 10:05 UTC)

<p><a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> Thanks for the above response.<br>
A follow-up question. So the grow from seeds technique can be considered as a region growing based segmentation method or graph-based segmentation method? I can see graph cut is a graph based segmentation, but not sure about growcut.</p>
<p>I hope you would help.</p>
<p>Thanks</p>

---

## Post #4 by @gaoyi.cn (2022-08-03 10:34 UTC)

<p>“So the grow from seeds technique can be considered as a region growing based segmentation method or graph-based segmentation method?”</p>
<p>Though intuitively it can be understood as a region growing method, to be precise, neither.</p>
<p>It builds a graph whose edge weights are related with the pixel intensity difference in between, and then it find the shortest distance based on such weight design through an adaptive Dijkstra algorithm.</p>
<p>Region growing does not consider the distances to the seeds, it only grows to a new pixel if local intensity difference is small. Therefore I does not has a “global view”.</p>
<p>Graph cut may be similar, but it can not handle multi-object simultaneous segmentation because a multi-way cut is NP-hard.</p>
<p>HTH and please let me know if more detail is needed.</p>
<p>Best,</p>
<p>yi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png" data-download-href="/uploads/short-url/8lHbc8ewzqTHYpSOyVLQwZxlrCe.png?dl=1" title="841F8A606C9E466C9FD5610F03B4BC6F.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png" alt="841F8A606C9E466C9FD5610F03B4BC6F.png" data-base62-sha1="8lHbc8ewzqTHYpSOyVLQwZxlrCe" width="690" height="1" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 2x" data-dominant-color="BECCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841F8A606C9E466C9FD5610F03B4BC6F.png</span><span class="informations">708×2 103 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @MPhilip (2022-08-03 10:58 UTC)

<p>Hi <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> . Thanks for your quick response.</p>
<p>But could you help me decide which category of segmentation method grow from seeds falls to? Eg thresholding, region growing, graph cut(as you answered it doesn’t fall into either of these-graph cut/ region growing), model-based segmentation method etc.  I believe watershed is a region growing based method.</p>
<p>When I tried to implement watershed and grow from seeds in the 3D slicer, the segmented tumours looked almost identical and it required more user intervention than thresholding. I was going through almost all the slices to mark out the tumour and background before clicking on the apply button. Otherwise, it was not giving the required outcome. Is it designed to behave so as it is a semi-automatic method?</p>
<p>Many thanks in advance</p>

---
