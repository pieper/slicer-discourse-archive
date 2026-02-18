# Offline 3D reconstruction from .mhd file using SlicerIGSIO extension

**Topic ID**: 36602
**Date**: 2024-06-05
**URL**: https://discourse.slicer.org/t/offline-3d-reconstruction-from-mhd-file-using-slicerigsio-extension/36602

---

## Post #1 by @Viktor_Sokolov (2024-06-05 09:35 UTC)

<p>Hello everyone!<br>
I have a few questions about how to use the SlicerIGSIO tool for offline 3D reconstruction. The available tutorial only shows reconstruction in the Plus App.</p>
<ol>
<li>Should I load the .mhd/.mha file as a Volume or Sequence Metafile? When I load it as a Volume, I am unable to see the transforms. When I load it as a Sequence Metafile, I see all the transforms but cannot scroll through the frames. I am trying to “drag and drop” my frame to the transform as in this <a href="https://www.youtube.com/watch?v=2vXeJxYFou4&amp;list=WL&amp;index=20" rel="noopener nofollow ugc">video</a>, but as I said it doesn’t work this way.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3022d8f18d622d322a7e48ed8e0fafce7d8fb8a.jpeg" alt="drag" data-base62-sha1="ng2uCKnMxuzinhap8lQtjTRJCb0" width="503" height="321"></li>
<li>In the reconstruction app the button “apply” for some reason is not available:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcacb6c1f3f937dd1a88c13e8274844b728b903c.jpeg" data-download-href="/uploads/short-url/A3gmlgsWRpA1xp0CmrueOWBe9ZO.jpeg?dl=1" title="3d_rec_app" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcacb6c1f3f937dd1a88c13e8274844b728b903c_2_690x368.jpeg" alt="3d_rec_app" data-base62-sha1="A3gmlgsWRpA1xp0CmrueOWBe9ZO" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcacb6c1f3f937dd1a88c13e8274844b728b903c_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcacb6c1f3f937dd1a88c13e8274844b728b903c_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcacb6c1f3f937dd1a88c13e8274844b728b903c.jpeg 2x" data-dominant-color="6C6A67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_rec_app</span><span class="informations">1171×626 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---

## Post #2 by @Sunderlandkyl (2024-06-05 13:57 UTC)

<p>When loading as a sequence metafile, you use the sequence browser to move through the time points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98be958d5101a4aeb936371a83013c23bd537761.png" data-download-href="/uploads/short-url/lNeTOy3mi8CvXIkVhnEEPO53kCB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98be958d5101a4aeb936371a83013c23bd537761.png" alt="image" data-base62-sha1="lNeTOy3mi8CvXIkVhnEEPO53kCB" width="690" height="35" data-dominant-color="3D4141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×36 4.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You also won’t be able to click apply for “Recorded sequence reconstruction” until you select a SequenceBrowser.</p>

---

## Post #3 by @Viktor_Sokolov (2024-06-06 08:20 UTC)

<p>Thank you; it seems that everything almost works. However, after pressing the apply button, the frame plane in the 3D view moves in  the scan direction, but the reconstructed volume does not appear behind it<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c0d3f0edca8b240f767c370cec1d6762170982.jpeg" data-download-href="/uploads/short-url/iEHcAoUguiy2iRDqEYU1a74e4qS.jpeg?dl=1" title="no_volume_rendering" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c0d3f0edca8b240f767c370cec1d6762170982_2_690x326.jpeg" alt="no_volume_rendering" data-base62-sha1="iEHcAoUguiy2iRDqEYU1a74e4qS" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c0d3f0edca8b240f767c370cec1d6762170982_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c0d3f0edca8b240f767c370cec1d6762170982_2_1035x489.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c0d3f0edca8b240f767c370cec1d6762170982_2_1380x652.jpeg 2x" data-dominant-color="7F787C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">no_volume_rendering</span><span class="informations">1390×657 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
.</p>

---

## Post #4 by @Viktor_Sokolov (2024-06-07 07:55 UTC)

<p>For someone struggling with the same problem, <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI&amp;t=500s" rel="noopener nofollow ugc">this video</a> shows how to render a volume and actually see it in 3D.</p>

---
