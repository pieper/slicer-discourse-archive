# Blank out surrounding areas outside of segmented regions of interests in volume

**Topic ID**: 5566
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/blank-out-surrounding-areas-outside-of-segmented-regions-of-interests-in-volume/5566

---

## Post #1 by @xmc2018_ucl (2019-01-29 17:22 UTC)

<p>Hi</p>
<p>I am new to Slicer and I want to do multi-stages segmentation: 1. segment only lungs from CT images; 2. segment only vessels from the segmented lungs</p>
<p>I am wondering if I can load segmented lung mask (using chest imaging platform) and then only segment inside of the regions of the masks (using VMTK)? I tried VMTK first, but then it segments not only vessels but also a lot of surrounding areas so I was thinking if I do it in multi-stage, it might achieve better results (lung first, then inside of lung, vessels)</p>
<p>Many thanks</p>

---

## Post #2 by @lassoan (2019-01-30 00:51 UTC)

<p>You can use masking settings in the Segment Editor to allow painting only inside a selected segment.</p>
<p>You can also blank out areas outside/inside segmented regions using Mask volume effect (available after you install SegmentEditorExtraEffects extension) as shown in this video:</p>
<div class="lazyYT" data-youtube-id="xZwyW6SaoM4" data-youtube-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @lassoan (2023-03-21 03:04 UTC)



---
