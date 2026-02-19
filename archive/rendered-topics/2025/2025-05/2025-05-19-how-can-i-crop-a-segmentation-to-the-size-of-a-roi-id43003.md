---
topic_id: 43003
title: "How Can I Crop A Segmentation To The Size Of A Roi"
date: 2025-05-19
url: https://discourse.slicer.org/t/43003
---

# How can I crop a segmentation to the size of a ROI?

**Topic ID**: 43003
**Date**: 2025-05-19
**URL**: https://discourse.slicer.org/t/how-can-i-crop-a-segmentation-to-the-size-of-a-roi/43003

---

## Post #1 by @fabian34 (2025-05-19 13:39 UTC)

<p>I have several segmentations I want to 3d-print, that each consist of 15 segments (which are bones in my case). I only want to print a relevant area of the segmentation, due to material and time reasons. Also this area should be about the same size for each segmentation, so I want to have an as reproducible as possible cropping workflow.</p>
<p>How can I crop the segmentation to a certain size? Like I know how to create a ROI but is there a way to cut this part of the segmentation to print it? I tried several approaches but with no success, also there exists different information about features that could do it, but apparently don’t exist anymore on my slicer version (5.8.1).</p>
<p>What complicates the problem: the volumes have different orientations and sizes.</p>
<p>I am happy about any help!!</p>

---

## Post #2 by @lassoan (2025-05-19 13:45 UTC)

<p>In general, you would cut off unneded parts of segments using the “Scissors” effect. However, if you want to crop the entire segmentation to an ROI box then you can do it by a few clicks in <code>Segment Editor</code> module:</p>
<ul>
<li>click on the <code>Specify geometry</code> button (next to <code>Source volume</code> selector)</li>
<li>choose the ROI as <code>Source geometry</code> (and leave <code>Pad output</code> option disabled)</li>
<li>click <code>OK</code></li>
</ul>

---
