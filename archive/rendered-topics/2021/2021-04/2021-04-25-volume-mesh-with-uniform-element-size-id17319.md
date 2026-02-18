# Volume mesh with uniform element size

**Topic ID**: 17319
**Date**: 2021-04-25
**URL**: https://discourse.slicer.org/t/volume-mesh-with-uniform-element-size/17319

---

## Post #1 by @michxu98 (2021-04-25 23:23 UTC)

<p>Hello,</p>
<p>I am trying to generate a volume mesh with uniform element size from a segmentation using Cleaver in the Segment Mesher module, however the output mesh does not seem to have uniform element sizes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/530d6f1d8188750200e3721f36fcf5e00474d2d8.png" data-download-href="/uploads/short-url/bQIpz5rvHLI34hT4vWIwW3jODTG.png?dl=1" title="Screenshot from 2021-04-25 18-27-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/530d6f1d8188750200e3721f36fcf5e00474d2d8_2_677x500.png" alt="Screenshot from 2021-04-25 18-27-42" data-base62-sha1="bQIpz5rvHLI34hT4vWIwW3jODTG" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/530d6f1d8188750200e3721f36fcf5e00474d2d8_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/530d6f1d8188750200e3721f36fcf5e00474d2d8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/530d6f1d8188750200e3721f36fcf5e00474d2d8.png 2x" data-dominant-color="A2A0AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-04-25 18-27-42</span><span class="informations">998×736 801 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Slicer version: 4.11.20210226</p>
<p>I have set the following parameters,<br>
Feature scaling: 0.60<br>
Sampling Rate: 1.00<br>
Rate of change of element size: 1.00</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-04-26 01:45 UTC)

<p>I think you need to set element size rate of change to 0 if you don’t want to change the element size.</p>

---
