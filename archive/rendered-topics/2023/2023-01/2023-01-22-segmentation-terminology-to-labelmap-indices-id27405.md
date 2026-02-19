---
topic_id: 27405
title: "Segmentation Terminology To Labelmap Indices"
date: 2023-01-22
url: https://discourse.slicer.org/t/27405
---

# Segmentation terminology to labelmap indices

**Topic ID**: 27405
**Date**: 2023-01-22
**URL**: https://discourse.slicer.org/t/segmentation-terminology-to-labelmap-indices/27405

---

## Post #1 by @muratmaga (2023-01-22 17:24 UTC)

<p>In the SegmentationCategoryTypeModified-DICOM Master.json file, there are these fields called <strong>3dSlicerIntergerLabel</strong> (like below).</p>
<p>I thought these were the unique ID numbers that will be used when exporting a segmentation to a labelmap. but that doesn’t appear to be the case. Without a color table, segmentations seems to be exported simply by assigning a sequential number to segments in the order they are listed in the segmentations hierarchy.</p>
<p>What is the purpose of this field, and more  importantly is it somehow possible to export labelmaps consistently if we use terminology, or regardless we will still need a color table for the correct conversion.</p>
<pre><code class="lang-auto">"CodeMeaning": "Occipital bone",
            "CodingSchemeDesignator": "SCT",
            "3dSlicerLabel": "occipital bone",
            "3dSlicerIntegerLabel": 151,
            "cid": "4028",
            "UMLSConceptUID": "C0028784",
            "CodeValue": "31640002",
            "contextGroupName": "CraniofacialAnatomicRegions",
            "SNOMEDCTConceptID": "31640002"
          },
</code></pre>

---

## Post #2 by @cpinter (2023-01-23 10:01 UTC)

<p>That number is the index of the color in the <code>GenericAnatomyColors</code> color table</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/755fceb21bf1234de6fcd936d0d367d027473273.png" data-download-href="/uploads/short-url/gKl85uDVG4ZtVTf10J5RpKwAHZx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/755fceb21bf1234de6fcd936d0d367d027473273_2_278x500.png" alt="image" data-base62-sha1="gKl85uDVG4ZtVTf10J5RpKwAHZx" width="278" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/755fceb21bf1234de6fcd936d0d367d027473273_2_278x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/755fceb21bf1234de6fcd936d0d367d027473273_2_417x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/755fceb21bf1234de6fcd936d0d367d027473273.png 2x" data-dominant-color="F1F1F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">458×823 63.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think you can preserve the indices by checking the <code>Use color table values</code> checkbox in Segmentations module, see here</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ca3295cc8dc52597c4d1ccb47e35a8214d8f57.png" data-download-href="/uploads/short-url/9OxFObJQkE1J1fOTCjPSreoSsFF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44ca3295cc8dc52597c4d1ccb47e35a8214d8f57_2_441x500.png" alt="image" data-base62-sha1="9OxFObJQkE1J1fOTCjPSreoSsFF" width="441" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44ca3295cc8dc52597c4d1ccb47e35a8214d8f57_2_441x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ca3295cc8dc52597c4d1ccb47e35a8214d8f57.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44ca3295cc8dc52597c4d1ccb47e35a8214d8f57.png 2x" data-dominant-color="ECECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">539×611 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m not sure why only the <code>User</code> type color tables show up (at least that’s what happened for me on Linux using 2022-11-13), maybe someone else knows. If not, then let me look in the latest version later.</p>

---

## Post #3 by @muratmaga (2023-01-23 16:02 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="27405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I’m not sure why only the <code>User</code> type color tables show up (at least that’s what happened for me on Linux using 2022-11-13), maybe someone else knows.</p>
</blockquote>
</aside>
<p>Thats the same behavior I am seeing. I cannot select a color table if I haven’t loaded/generated on in Slicer. I will also argue that this somewhat defeats the purpose of the having a segmentation terminology. If a proper segmentation terminology is used, the export to labelmap needs to happen automatically. I can envision a use case where the user assigns a terminology to a segmentation, and while it is being exported if there are “unnamed” segments (e.g., Segment_23) this generates a warning error about lack of terminology in the segment.</p>

---
