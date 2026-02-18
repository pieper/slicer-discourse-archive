# Lung Vessels Diameters using VMTK

**Topic ID**: 24211
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/lung-vessels-diameters-using-vmtk/24211

---

## Post #1 by @Vir (2022-07-06 18:31 UTC)

<p>Hello<br>
I am working with lung vessels volumetric file (. img) which is a binary image . I want to extract the diameters of each vessels . Is there a way to extract these values using 3d slicer VMTK extension .<br>
Below is , how the volumetric image looks like .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a18a88245f5b0c37d3aad600b9b6efc2b8ce6db7.jpeg" data-download-href="/uploads/short-url/n33FTDSAlj1PICP9NXzLqn1MjA3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a18a88245f5b0c37d3aad600b9b6efc2b8ce6db7_2_541x500.jpeg" alt="image" data-base62-sha1="n33FTDSAlj1PICP9NXzLqn1MjA3" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a18a88245f5b0c37d3aad600b9b6efc2b8ce6db7_2_541x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a18a88245f5b0c37d3aad600b9b6efc2b8ce6db7_2_811x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a18a88245f5b0c37d3aad600b9b6efc2b8ce6db7.jpeg 2x" data-dominant-color="8180BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">813×751 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you in advance</p>

---

## Post #2 by @lassoan (2022-07-07 02:52 UTC)

<p>You can use Extract centerline module in Slicer (provided by SlicerVMTK extension) for this. For such extremely complex vascular tree you need to use the “Network” output. If you select an output node for “Network properties” then you’ll get a table containing the average radius value (and length, curvature, etc.) for each branch.</p>

---

## Post #3 by @Vir (2022-07-13 19:29 UTC)

<p>Thank you very much for the response.</p>
<p>However as this is a binary image file. Is there a way to select the entire image as a segmentation as that would be the input for the extract centerline module. I don’t know if it makes sense.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2072886a799f44b804141fb14bd33d2505eeaa2f.jpeg" data-download-href="/uploads/short-url/4D2FcKnqqLSByJfKSswGKkP1SSr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2072886a799f44b804141fb14bd33d2505eeaa2f_2_690x210.jpeg" alt="image" data-base62-sha1="4D2FcKnqqLSByJfKSswGKkP1SSr" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2072886a799f44b804141fb14bd33d2505eeaa2f_2_690x210.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2072886a799f44b804141fb14bd33d2505eeaa2f_2_1035x315.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2072886a799f44b804141fb14bd33d2505eeaa2f_2_1380x420.jpeg 2x" data-dominant-color="908C99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×587 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you in advance</p>

---

## Post #4 by @lassoan (2022-07-14 12:13 UTC)

<p>Yes, you can select the entire segmentation as input in Extract centerline module. If you don’t have a segmentation yet then you can use Segment Editor module for segmenting the image. If you already have a binary labelmap then you can<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">load it as a segmentation</a>.</p>

---

## Post #5 by @Eserval (2022-07-14 14:32 UTC)

<p>Hello Vir,</p>
<p>Really nice work. I don’t know the final applicability you are using the extracted vessels diameter, but I’d like to ask a question for you and the other colleagues about this topic.<br>
Is there a great correlation between the extracted vessel diameter by the CT segmentation and the reality? For us, thoracic surgeons, it is an important preoperative data since may help to plan the vessel treatment. Sometimes I think that there is a huge difference between the 3D model and the real size observed intraoperatively.</p>

---

## Post #6 by @chir.set (2022-07-14 15:09 UTC)

<aside class="quote no-group" data-username="Eserval" data-post="5" data-topic="24211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eserval/48/14650_2.png" class="avatar"> Eserval:</div>
<blockquote>
<p>Sometimes I think that there is a huge difference between the 3D model and the real size observed intraoperatively.</p>
</blockquote>
</aside>
<p>Blood vessel metrics are influenced by hemodynamics, whether on the CT table or on the surgery table. They won’t be exactly the same at blood systolic pressure of 6 or 16. Clamped arteries will still have lower diameters than measured on CT scans. For example, an infra-renal aorta measured at 28 mm on CT scan may require a 22 mm prosthesis at surgery, this is quite common.</p>

---
