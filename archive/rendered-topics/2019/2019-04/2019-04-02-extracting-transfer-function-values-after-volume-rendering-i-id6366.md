---
topic_id: 6366
title: "Extracting Transfer Function Values After Volume Rendering I"
date: 2019-04-02
url: https://discourse.slicer.org/t/6366
---

# Extracting transfer function values after Volume rendering in 3D Slicer

**Topic ID**: 6366
**Date**: 2019-04-02
**URL**: https://discourse.slicer.org/t/extracting-transfer-function-values-after-volume-rendering-in-3d-slicer/6366

---

## Post #1 by @nish91 (2019-04-02 11:49 UTC)

<p>I render a NifTI volume using ‘Volume rendering’ module in 3D Slicer as shown in the figure below. However, I would like to replicate exactly the same using python and VTK without using 3D Slicer. For that I need to extract the values of the transfer function used for rendering the volume. Could anoyone let me know how I can achieve that in 3D Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7782c08b76aa446ee7ac40070bc0ca06e042bf97.png" data-download-href="/uploads/short-url/h3eX9ETswvOwE3dEFeCfFKPWisD.png?dl=1" title="Selection_095" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7782c08b76aa446ee7ac40070bc0ca06e042bf97_2_690x307.png" alt="Selection_095" data-base62-sha1="h3eX9ETswvOwE3dEFeCfFKPWisD" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7782c08b76aa446ee7ac40070bc0ca06e042bf97_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7782c08b76aa446ee7ac40070bc0ca06e042bf97_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7782c08b76aa446ee7ac40070bc0ca06e042bf97_2_1380x614.png 2x" data-dominant-color="7C7E93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_095</span><span class="informations">3687×1642 577 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-04-02 12:25 UTC)

<p>Sure, the code’s all in <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/VolumeRendering/MRMLDM" rel="nofollow noopener">the Volume Rendering Module Displayable Manager</a>.  Of course consider building on the Slicer code and contributing back improvements if you can.</p>

---
