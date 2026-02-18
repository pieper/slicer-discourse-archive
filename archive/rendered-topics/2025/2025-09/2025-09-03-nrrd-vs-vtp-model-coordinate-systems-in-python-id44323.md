# Nrrd vs vtp model coordinate systems in Python

**Topic ID**: 44323
**Date**: 2025-09-03
**URL**: https://discourse.slicer.org/t/nrrd-vs-vtp-model-coordinate-systems-in-python/44323

---

## Post #1 by @elisedl1 (2025-09-03 03:46 UTC)

<p>Hello,</p>
<p>My model (.vtp) and image (.nrrd) align in slicer correctly. I am trying to use the model and image information in Python, but they do not visually align when plotted; they are in different coordinate systems (world vs physical)? Is there an easy way to convert the vtp mesh to align with the nrrd CT image in Python?</p>
<p>TLDR: what is the conversion that slicer does internally to a model to align it with a given reference image?</p>
<p>Thanks!</p>

---

## Post #2 by @elisedl1 (2025-09-03 04:07 UTC)

<p>As an update - I was able to get it aligned by the following steps:</p>
<p>- mesh points are world coordinates in LPS</p>
<p>- NRRD image are in voxels</p>
<p>- slicer applies image origin and direction to mesh → converts mesh coordinates to voxel space?</p>
<p>- world → voxel: voxel=(mesh_points−origin)*inv(direction)/spacing</p>
<p>- shift mesh so image origin is (0,0,0)</p>
<p>- apply inverse of image direction</p>
<p>- convert physical to voxel indices (divide by spacing)</p>
<p>If I am using the mesh information inside a registration algorithm, should I do this conversion within Python?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4884388a07f0966fb01337901d4d13e1d65fc2.png" data-download-href="/uploads/short-url/fSsmDmmNL2lXI6cysfae2eN8O9Y.png?dl=1" title="Screenshot 2025-09-03 at 12.06.19 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4884388a07f0966fb01337901d4d13e1d65fc2_2_545x499.png" alt="Screenshot 2025-09-03 at 12.06.19 AM" data-base62-sha1="fSsmDmmNL2lXI6cysfae2eN8O9Y" width="545" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4884388a07f0966fb01337901d4d13e1d65fc2_2_545x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4884388a07f0966fb01337901d4d13e1d65fc2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4884388a07f0966fb01337901d4d13e1d65fc2.png 2x" data-dominant-color="262628"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-03 at 12.06.19 AM</span><span class="informations">615×564 75.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
