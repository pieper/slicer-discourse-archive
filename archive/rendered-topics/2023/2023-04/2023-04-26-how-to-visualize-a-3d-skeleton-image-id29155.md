# How to visualize a 3D skeleton image

**Topic ID**: 29155
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/how-to-visualize-a-3d-skeleton-image/29155

---

## Post #1 by @Peidi_Xu (2023-04-26 21:31 UTC)

<p>I have a simple 3D binary in .nii.gz form, where voxel value 1 means foreground and 0 means background. So it is a skeleton because every foreground voxel has a thickness of one, e.g., it is the output after running skimage.morphology.skeletonize_3d.</p>
<p>I am just wondering what is the best way to visualize such binary image in 3D slicer, because the standard show 3D option in segmentation editor generates very disconnected structures even with smoothing set to 0.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fac35f3115cda09f1c638f5eedb31a462e40ee6.png" data-download-href="/uploads/short-url/6NJoR8x0P4lgUIxWzpMLn32vFtQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fac35f3115cda09f1c638f5eedb31a462e40ee6_2_690x345.png" alt="image" data-base62-sha1="6NJoR8x0P4lgUIxWzpMLn32vFtQ" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fac35f3115cda09f1c638f5eedb31a462e40ee6_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fac35f3115cda09f1c638f5eedb31a462e40ee6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fac35f3115cda09f1c638f5eedb31a462e40ee6.png 2x" data-dominant-color="9FA2D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">922×462 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-04-26 21:39 UTC)

<p>Image skeletonization is a very limited algorithm that provides relatively inaccurate and non-realistic centerline points (e.g., flow direction and radius is not taken into account), the points are not connected, and radius information is lost.</p>
<p>I would recommend to use Slicer’s <a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">VMTK extension</a> to extract centerline trees, which does not have any of the above limitations.</p>

---
