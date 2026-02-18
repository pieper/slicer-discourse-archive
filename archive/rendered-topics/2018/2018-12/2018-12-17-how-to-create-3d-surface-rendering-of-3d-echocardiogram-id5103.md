# how to create 3d surface rendering of 3D echocardiogram

**Topic ID**: 5103
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/how-to-create-3d-surface-rendering-of-3d-echocardiogram/5103

---

## Post #1 by @gptruncus (2018-12-17 03:02 UTC)

<p>Operating system:Mac or Windows(have both)<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, another user posted asking to create a surface rendering of a heart CT/MRI, and Im wondering how to do this with the below posted 3D echocardiogram image. either create a surface rendering or create a 3d blood pool and then a surface/shell of that?</p>
<p>Sincerely, Greg<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/606f5a2f11ce347c18c24c4bbb98fd00b83bc8c0.jpeg" data-download-href="/uploads/short-url/dL6pjB6NrSDM44trUF4TiIhw2li.jpeg?dl=1" title="36%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606f5a2f11ce347c18c24c4bbb98fd00b83bc8c0_2_690x495.jpeg" alt="36%20PM" data-base62-sha1="dL6pjB6NrSDM44trUF4TiIhw2li" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606f5a2f11ce347c18c24c4bbb98fd00b83bc8c0_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606f5a2f11ce347c18c24c4bbb98fd00b83bc8c0_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/606f5a2f11ce347c18c24c4bbb98fd00b83bc8c0_2_1380x990.jpeg 2x" data-dominant-color="A9A9AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">36%20PM</span><span class="informations">2104×1512 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-12-17 04:20 UTC)

<p>You can use Segment Editor module for this. Cardiac ultrasound segmentation is not easy, you need to spend some time learning it and the process is quite labor intensive.</p>
<p>Our collaborators at CHOP typically use Paint effect with intensity masking for leaflet segmentation from 4D US. We have recently implemented intensity masking for Grow from seeds effect, which may make the process a bit more efficient. Getting better at acquiring 3D/4D images may also make segmentation a bit easier.</p>
<p>We have developed cardiac US segmentation module, which performs some masking and other pre-processing operations that help with segmentation. We plan to release this module within about 6-12 months in SlicerHeart extension.</p>

---

## Post #3 by @gptruncus (2018-12-17 23:00 UTC)

<p>Thank you.<br>
When looking for Slicerheart on windows 10 computer I get : No extensions found for win:64-bit, revision: ‘27662’.<br>
Do I need to upgrade anything on computer?</p>

---

## Post #4 by @lassoan (2020-10-11 02:51 UTC)

<p>A post was split to a new topic: <a href="/t/segement-4d-cardiac-echo-image/13984">Segement 4D cardiac echo image</a></p>

---
