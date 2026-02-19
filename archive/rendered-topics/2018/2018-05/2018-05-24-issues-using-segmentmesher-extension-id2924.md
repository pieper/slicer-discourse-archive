---
topic_id: 2924
title: "Issues Using Segmentmesher Extension"
date: 2018-05-24
url: https://discourse.slicer.org/t/2924
---

# Issues Using SegmentMesher Extension

**Topic ID**: 2924
**Date**: 2018-05-24
**URL**: https://discourse.slicer.org/t/issues-using-segmentmesher-extension/2924

---

## Post #1 by @gswai123 (2018-05-24 20:17 UTC)

<p>Operating system: macOS High Sierra (10.13.4)<br>
Slicer version: 4.9.0 (Nightly Build)</p>
<p>Hello,</p>
<p>I am very new to 3D Slicer (this is my third day using it). I want to be able to make a volumetric mesh from a brain scan for finite element analysis using the SegmentMesher Extension. I have created a segmentation (I think) using the sample data MRBrainTumor1. I input my segmentation and the correct parameters for Cleaver, as instructed here: <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a>. However, I get the following error when I hit Apply: "Error: ‘module’ object has no attribute ‘STARTUPINFO’ ". Does anybody know what I’m doing wrong? I’m attaching a screenshot of what my 3D slicer looks like.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d6806cd6f46d820ec01885bde39359f7ba91dcf.png" data-download-href="/uploads/short-url/mstQ0cPv9X2e2bDQGkpsbn6X4KP.png?dl=1" title="08%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d6806cd6f46d820ec01885bde39359f7ba91dcf_2_690x396.png" alt="08%20PM" data-base62-sha1="mstQ0cPv9X2e2bDQGkpsbn6X4KP" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d6806cd6f46d820ec01885bde39359f7ba91dcf_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d6806cd6f46d820ec01885bde39359f7ba91dcf_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d6806cd6f46d820ec01885bde39359f7ba91dcf.png 2x" data-dominant-color="C0C4CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">08%20PM</span><span class="informations">1214×698 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-05-24 20:33 UTC)

<p>Thanks for reporting this. I’ve updated the module so that it should work now. You can either apply <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/e124d6c25cdf05cb7aff2961abd1fe1127bb98c8">this change</a> on your local copy of SegmentMesher.py or re-install the SegmentMesher extension tomorrow.</p>

---
