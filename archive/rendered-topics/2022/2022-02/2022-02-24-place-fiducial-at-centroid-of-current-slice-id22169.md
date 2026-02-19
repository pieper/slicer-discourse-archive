---
topic_id: 22169
title: "Place Fiducial At Centroid Of Current Slice"
date: 2022-02-24
url: https://discourse.slicer.org/t/22169
---

# Place fiducial at centroid of current slice

**Topic ID**: 22169
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/place-fiducial-at-centroid-of-current-slice/22169

---

## Post #1 by @jmhuie (2022-02-24 21:23 UTC)

<p>Hi All,</p>
<p>I am trying to create a python script that will place a fiducial at the centroid of a currently visible slice of a segment. Unfortunately, I am running into a few road blocks. Specifically, I am not sure how to grab the current slice number and coordinates of the segmented pixels that are currently contained in it to calculate the centroid. I need to be able to do this on the fly for both transformed and untransformed volumes. Any insights or suggestions would be greatly appreciated.</p>
<p>Here is an example photo (not much to actually see)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba51e29958160dba6db50c3a8b648decb3888997.png" data-download-href="/uploads/short-url/qAgflTX0F5eepcFd6Tr9Gp6qKmr.png?dl=1" title="Screen Shot 2022-02-24 at 4.20.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51e29958160dba6db50c3a8b648decb3888997_2_690x431.png" alt="Screen Shot 2022-02-24 at 4.20.41 PM" data-base62-sha1="qAgflTX0F5eepcFd6Tr9Gp6qKmr" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51e29958160dba6db50c3a8b648decb3888997_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51e29958160dba6db50c3a8b648decb3888997_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51e29958160dba6db50c3a8b648decb3888997_2_1380x862.png 2x" data-dominant-color="171818"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-24 at 4.20.41 PM</span><span class="informations">3584×2240 458 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-02-25 07:27 UTC)

<p>In general, there is no such thing as slice number in this case, as the slice view normal does not have to be parallel to any of the segmentation axes.</p>
<p>Instead, what you need is to extract a cross-section from the segment using the slice’s SliceToRAS transform. You can see an example <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CrossSectionAnalysis/CrossSectionAnalysis.py#L1094-L1154">how it is done for segmentation closed surface representation</a> in the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md">Cross-section analysis module</a> in SlicerVMTK.</p>
<p>Cross-section analysis module may be potentially interesting for you, as it allows convenient reslicing of segments along a line (it can be straight or curved) and measures cross-sections, finds minimum/maximum cross-sectional area, exports results to a table, etc.</p>

---

## Post #3 by @jmhuie (2022-02-27 15:57 UTC)

<p>Thanks Andras,</p>
<p>The SlicerVMTK extension does seem very relevant, but on first glance I don’t fully understand what it is doing.</p>
<p>Instead, I have designed a work around that seems to work pretty well for now. I’m essentially 1) creating an MarkupsRoI around the desired “slice” or “index”, 2) creating a blank scalar volume that matches those dimensions, 3) export a labelmap of the segment with the dimensions of the blank reference volume, 4) converting the labelmap to a segmentation node and then calculating the centroid of the “slice”.</p>
<p>I will admit that it sounds a bit clunky and there’s a slight delay with larger volumes, but I do not think it’s much slower (if at all) than the VMTK cross-section analysis module when handling larger volumes</p>

---

## Post #4 by @jumbojing (2022-07-17 04:01 UTC)

<p>I also want to know howto get the centroid…</p>

---
