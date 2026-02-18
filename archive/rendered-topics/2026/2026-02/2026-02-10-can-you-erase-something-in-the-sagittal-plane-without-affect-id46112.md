# Can you erase something in the sagittal plane, without affecting segmentations made in the axial plane?

**Topic ID**: 46112
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/can-you-erase-something-in-the-sagittal-plane-without-affecting-segmentations-made-in-the-axial-plane/46112

---

## Post #1 by @Severin (2026-02-10 15:22 UTC)

<p>Hello everyone,</p>
<p>My apologies, probably this has already been addressed previously and I am just not able to find the answer.</p>
<p>I am using Slicer 3D (5.8) with Biomedisa and segmented every 20th slice in the axial plane. I have also made a few sagittal segmentations as a try out, but it did not work well and therefore I want to remove them. However I do not want remove anything from the axial slices. Here is the sagittal plane I want to remove:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d396d245dcd26fbe080ae6944ee76cdadf57521d.jpeg" data-download-href="/uploads/short-url/ubNSx63ljKGOOVmM19Q42jQ9KdD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d396d245dcd26fbe080ae6944ee76cdadf57521d_2_510x500.jpeg" alt="image" data-base62-sha1="ubNSx63ljKGOOVmM19Q42jQ9KdD" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d396d245dcd26fbe080ae6944ee76cdadf57521d_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d396d245dcd26fbe080ae6944ee76cdadf57521d_2_765x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d396d245dcd26fbe080ae6944ee76cdadf57521d.jpeg 2x" data-dominant-color="5A423D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×784 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I remove (part of) it, also the axial segments are erased and you do not see the lines continuing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1fabee06facb65381acb615b5fec36c3950c857.jpeg" data-download-href="/uploads/short-url/tXz0HvV32VtecWeULU2ndjsQUgn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1fabee06facb65381acb615b5fec36c3950c857_2_481x500.jpeg" alt="image" data-base62-sha1="tXz0HvV32VtecWeULU2ndjsQUgn" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1fabee06facb65381acb615b5fec36c3950c857_2_481x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1fabee06facb65381acb615b5fec36c3950c857_2_721x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1fabee06facb65381acb615b5fec36c3950c857.jpeg 2x" data-dominant-color="453C3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">743×771 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If it would be possible to only  erase the sagittal plane, that would save a lot of work, thank you for your help!</p>
<p>Kind regards,</p>
<p>Severin</p>

---

## Post #2 by @pieper (2026-02-10 15:51 UTC)

<p>I’m not sure if Biomedsia users or developers are active here generally, so you might try looking at their site: <a href="https://biomedisa.info/">https://biomedisa.info/</a></p>

---
