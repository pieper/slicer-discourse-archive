# Rendered Volume doesn't show up in the Filtering Input Volume Section

**Topic ID**: 28545
**Date**: 2023-03-23
**URL**: https://discourse.slicer.org/t/rendered-volume-doesnt-show-up-in-the-filtering-input-volume-section/28545

---

## Post #1 by @Ibrahim_Dolas (2023-03-23 14:20 UTC)

<p>Operating system: MacOS Ventura 13.1<br>
Slicer version: 5.2.2<br>
Expected behavior: After rendering the volume and cropping the 3d view, when I go to the Filtering-&gt;Denoising-&gt;Gradient Anisotropic Diffusion menu, I should see my volume in the Input Volume Section<br>
Actual behavior: My volume doesn’t show up</p>

---

## Post #2 by @lassoan (2023-03-24 04:32 UTC)

<p>Gradient anisotropic diffusion (and most other modules) requires a scalar volume. You can convert vector volumeto scalar volume using “Vector to scalar volume” module.</p>

---
