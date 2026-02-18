# Register two 2D images (EPID and DRR)

**Topic ID**: 45057
**Date**: 2025-11-12
**URL**: https://discourse.slicer.org/t/register-two-2d-images-epid-and-drr/45057

---

## Post #1 by @ruju (2025-11-12 22:07 UTC)

<p>Hi,</p>
<p>I would like to register two 2D images in 3D Slicer, one is an EPID image and the other is a computed DRR. Unfortunately, the EPID image does not contain any geometric information, so it is placed arbitrarily when loaded into 3D Slicer.</p>
<p>I tried using the Transform module, but applying the coordinates of the DRR’s position as transformation parameters does not align the EPID with the DRR plane. I also attempted registration with the General Registration (BRAINS) module, but it did not work because the images are 2D and lack a third dimension. Do you have any suggestions on how to correctly align or register 2D images in 3D Slicer?</p>
<p>Thanks in advance for your help!</p>

---
