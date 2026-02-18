# Diffusion tensor image corregistration

**Topic ID**: 9293
**Date**: 2019-11-25
**URL**: https://discourse.slicer.org/t/diffusion-tensor-image-corregistration/9293

---

## Post #1 by @Gonzalo_Rojas_Costa (2019-11-25 13:46 UTC)

<p>Operating system: Ubuntu<br>
Slicer version: 3.6.3, 4.10.2<br>
Expected behavior:  How can I do the corregistration of corticospinal tract to mprage volumetric image?<br>
Actual behavior: I am processing the corticospinal tract, but I need to do the corregistration to mprage volumetric image.</p>

---

## Post #2 by @pieper (2019-11-25 23:52 UTC)

<p>Often the structural and diffusion images will be in the same space.  If not, when you convert DWI to DTI, you also get a baseline volume, which can be used for registration.  If you only have a DTI, you could try different derived scalars for registration.</p>

---
