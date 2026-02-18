# Rotation not account with brainfit

**Topic ID**: 2572
**Date**: 2018-04-12
**URL**: https://discourse.slicer.org/t/rotation-not-account-with-brainfit/2572

---

## Post #1 by @Cyril (2018-04-12 16:50 UTC)

<p>Hello Slicer Community,<br>
We have created CT and MRI numerical phantom to test the accuracy of registration software. With very simple form like an ellispsoide and just two value 0 for the background and 700 for the ellipsoide. If we translate them Brainfit succeed to register them with a very good accuracy (less then one voxel) but if there is rotation he do not apply any rotation.  We try to increase the number of point or use mask but it didn’t solve the problem. You can access the image with this link.<br>
<a href="https://drive.google.com/drive/folders/1WSGeMJ8vlPdEiVRLPBNIiH7ChLy48hPS?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1WSGeMJ8vlPdEiVRLPBNIiH7ChLy48hPS?usp=sharing</a>!<br>
Do you have any clues?<br>
Thank you,<br>
Cyril Jaudet, PhD<br>
Centre françois Baclesse,<br>
Caen, France</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/296d3786c794f7359ba138bcc61a139e4bc039b7.png" data-download-href="/uploads/short-url/5UtzunhiREYhoWXBkKVlKVjzI4n.png?dl=1" title="registration_rotation_problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/296d3786c794f7359ba138bcc61a139e4bc039b7_2_690x388.png" alt="registration_rotation_problem" data-base62-sha1="5UtzunhiREYhoWXBkKVlKVjzI4n" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/296d3786c794f7359ba138bcc61a139e4bc039b7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/296d3786c794f7359ba138bcc61a139e4bc039b7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/296d3786c794f7359ba138bcc61a139e4bc039b7_2_1380x776.png 2x" data-dominant-color="8C8B92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registration_rotation_problem</span><span class="informations">1920×1080 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-04-12 19:31 UTC)

<p>In general, you need to have a reasonably close initial alignment. In cases like this, automatic alignment methods may work (try all options available in “Initialize Transform Mode”). You could probably also increase the capture range of the registration by tuning optimization parameters (steps sizes, relaxation factor, etc). Finally, you can also try <a href="https://github.com/lassoan/SlicerElastix/">SlicerElastix</a> instead of BRAINS.</p>

---
