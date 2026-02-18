# 3D reconstruction from 2D line scan images

**Topic ID**: 28245
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/3d-reconstruction-from-2d-line-scan-images/28245

---

## Post #1 by @Mack (2023-03-09 02:32 UTC)

<p>Dear Community,</p>
<p>I am new to 3DSlicer, and my question is about reconstructing a 3D model from 2D images which are not horizontal slices in the conventional CT definition.<br>
Basically, we are acquiring line scan images of rocks at different view angles. I attach a sketch of what and how we are imaging.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eed3451a326dc34160453dfdb65bbd157c1f816.jpeg" data-download-href="/uploads/short-url/dxL5ATkDgy3LblgJ2wWtVAQKCPk.jpeg?dl=1" title="Sketch of 2D image acquisition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eed3451a326dc34160453dfdb65bbd157c1f816_2_690x388.jpeg" alt="Sketch of 2D image acquisition" data-base62-sha1="dxL5ATkDgy3LblgJ2wWtVAQKCPk" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eed3451a326dc34160453dfdb65bbd157c1f816_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eed3451a326dc34160453dfdb65bbd157c1f816_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eed3451a326dc34160453dfdb65bbd157c1f816.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sketch of 2D image acquisition</span><span class="informations">1280×720 71.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How could we retrieve a volume/voxel size from our image stack (done at different view angles)?</p>
<p>Is there a way to tell 3DSlicer that the default view is the frontal plane and not the axial plane of a regular CT acquisition?</p>
<p>What we are missing in our acquisition is the axial/transverse plane which needs to be reconstructed.</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @pieper (2023-03-09 14:49 UTC)

<p>It sounds like <a href="https://www.openrtk.org/">RTK could help</a> although I’m not sure it handles this particular task.</p>

---
