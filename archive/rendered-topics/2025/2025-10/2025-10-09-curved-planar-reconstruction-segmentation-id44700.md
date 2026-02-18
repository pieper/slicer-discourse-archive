# curved planar reconstruction segmentation

**Topic ID**: 44700
**Date**: 2025-10-09
**URL**: https://discourse.slicer.org/t/curved-planar-reconstruction-segmentation/44700

---

## Post #1 by @hltkrgz (2025-10-09 02:00 UTC)

<p>Hi, I am trying to segment coronary plaques, but when I upload the curved planar images we get from our provider to 3dslicer, all slices are different nodes, and I can’t segmentate them together. i think this is due to our images reconstructed as a ribbon. how can i overcome this. I tried using DICOM patcher to clean up, I tried Slicer morph image stacks, they don’t work.</p>

---

## Post #2 by @lassoan (2025-10-09 02:04 UTC)

<p>In the DICOM module, you can check the “Advanced” checkbox and then choose to load the entire series as a single 3D image. However, you may then lose the slice positions and orientations.</p>
<p>You could instead do CPR in Slicer, which maintains a two-way mapping between the original and the curved space, so any segmentations or annotations that you do in one space can be automatically transformed to the other.</p>

---

## Post #3 by @hltkrgz (2025-10-09 02:16 UTC)

<p>Thank you for the response. Do i need a specific module for this. because on the database page when i pick advanced and click examine, nothing happens i cant see a choice for single 3d image</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3892cb625779150f6388ee5c79498a2b6b3e8ba5.png" data-download-href="/uploads/short-url/84tf86NKfSnCvOeFs9RWapti3VH.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3892cb625779150f6388ee5c79498a2b6b3e8ba5_2_649x499.png" alt="1" data-base62-sha1="84tf86NKfSnCvOeFs9RWapti3VH" width="649" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3892cb625779150f6388ee5c79498a2b6b3e8ba5_2_649x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3892cb625779150f6388ee5c79498a2b6b3e8ba5_2_973x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3892cb625779150f6388ee5c79498a2b6b3e8ba5_2_1298x998.png 2x" data-dominant-color="EFF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1561×1201 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2025-10-09 02:24 UTC)

<p>The <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#curved-planar-reformat">Curved Planar Reformat module</a> is in the Sandbox extension.</p>

---
