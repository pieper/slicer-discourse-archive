# Temporal calibration data from fCal into 3D slicer

**Topic ID**: 39739
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/temporal-calibration-data-from-fcal-into-3d-slicer/39739

---

## Post #1 by @jonortegav (2024-10-17 03:29 UTC)

<p>Hello <a class="mention" href="/u/cpinter">@cpinter</a>,</p>
<p>As I am new in the 3D slicer community I can just reply 3 times in a topic. So I create this topic to respond you from (<a href="https://discourse.slicer.org/t/temporal-calibration-in-3d-slicer/33876" class="inline-onebox">Temporal calibration in 3D slicer</a>) topic</p>
<p>if I don’t misunderstood, you mean that i should define " LocalTimeOffsetSec = 0.1038" in the NDI tracking device (Tracker device) (see figure1) according to this temporal calibration (see figure2)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ec9889cc1e35bf105d67532409ad19a197c14f.png" data-download-href="/uploads/short-url/x5HcoBIE4CyWnZ8sQcamSUel7Lp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ec9889cc1e35bf105d67532409ad19a197c14f.png" alt="image" data-base62-sha1="x5HcoBIE4CyWnZ8sQcamSUel7Lp" width="544" height="500" data-dominant-color="242323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">921×845 44.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15b79e1efcb62d8a75bafcdfff4235a0a04a6c2.png" data-download-href="/uploads/short-url/yr93xd3dRPOxqalUZo6RfduhVke.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15b79e1efcb62d8a75bafcdfff4235a0a04a6c2_2_690x389.png" alt="image" data-base62-sha1="yr93xd3dRPOxqalUZo6RfduhVke" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15b79e1efcb62d8a75bafcdfff4235a0a04a6c2_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15b79e1efcb62d8a75bafcdfff4235a0a04a6c2_2_1035x583.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15b79e1efcb62d8a75bafcdfff4235a0a04a6c2.png 2x" data-dominant-color="EFEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1087×613 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Correct me if I am wrong</p>

---

## Post #2 by @lassoan (2024-10-17 03:31 UTC)

<p>When you complete the temporal calibration and save the device set configuration file, the temporal calibration result is saved into the file and you don’t need to write the value there manually.</p>

---

## Post #3 by @jonortegav (2024-10-17 05:58 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a> for your help !</p>

---

## Post #4 by @MReza (2025-11-12 15:17 UTC)

<p>Hello everyone,</p>
<p>After running temporal calibration in fCal, the software reports the estimated lag and shows the “before” and “after” correction plots. However, in the “after” plot I still see a residual offset between the two systems on the X-axis. How can I address this remaining offset? Is there any study showing its impact on 3D reconstruction accuracy?</p>
<p>Also, how should I interpret the differences between the peak positions, which show sizable offsets in both X and Y? I repeated the calibration several times, but the latency does not appear constant and the plots never align well. I tried to consult the Plus Toolkit user manual, but the page is currently unreachable. Thank you in advance for any guidance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a04dbd26a03d41b2301114699e1b4d40a0c8fd8.png" data-download-href="/uploads/short-url/f7T1kNDM1FbHd2UYqwSy8YgRvza.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a04dbd26a03d41b2301114699e1b4d40a0c8fd8.png" alt="Picture1" data-base62-sha1="f7T1kNDM1FbHd2UYqwSy8YgRvza" width="419" height="475"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">419×475 62.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
