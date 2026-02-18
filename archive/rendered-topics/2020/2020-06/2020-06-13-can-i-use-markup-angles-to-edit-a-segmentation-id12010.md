# Can I use markup angles to edit a segmentation?

**Topic ID**: 12010
**Date**: 2020-06-13
**URL**: https://discourse.slicer.org/t/can-i-use-markup-angles-to-edit-a-segmentation/12010

---

## Post #1 by @Mohammad_Tanjib_Rahm (2020-06-13 05:47 UTC)

<p>I am trying to keep only the region of segmentation that is inside the markup angle and get rid of the rest. So far I have tried the scissor tool. It gets the job done. But I am looking for a faster method. Is there any way I can use the markup angle ROI to edit the segmentation?</p>

---

## Post #2 by @lassoan (2020-06-13 14:18 UTC)

<p>There is almost nothing really inside an angle widget (it is just two thin line segments). Would you like to cut segments with a plane placed at a certain angle?</p>
<p>Can you tell a bit more about the clinical problem and what you are trying to achieve?</p>

---

## Post #3 by @Mohammad_Tanjib_Rahm (2020-06-13 16:38 UTC)

<p>Yes. I am trying to circumstantially divide a segmentation of Left Ventricle into 6 regions. If I could cut segments with plane at a certain angle that would work as well.</p>

---

## Post #4 by @lassoan (2020-06-13 17:24 UTC)

<p>Can you write a bit more about your clinical application? Are you segmenting valve leaflets on 3D ultrasound (maybe CAVC, if you need to split to 6 regions)? We are doing lots of these and may be able to give you more specific advice if we know what exactly you need.</p>

---

## Post #5 by @Mohammad_Tanjib_Rahm (2020-06-13 17:45 UTC)

<p>We are trying to assess cardiac microstructure on different regions of Left Ventricle. For that we are using MRI data.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4c91e674cbd54a873d0ca13c2b9a8c4f901cb7.jpeg" data-download-href="/uploads/short-url/1t6P9klRTAcAQMjvnFlyPVi0naL.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4c91e674cbd54a873d0ca13c2b9a8c4f901cb7_2_338x500.jpeg" alt="Capture" data-base62-sha1="1t6P9klRTAcAQMjvnFlyPVi0naL" width="338" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4c91e674cbd54a873d0ca13c2b9a8c4f901cb7_2_338x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4c91e674cbd54a873d0ca13c2b9a8c4f901cb7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4c91e674cbd54a873d0ca13c2b9a8c4f901cb7.jpeg 2x" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">494×730 63.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> . I am trying to divide them to AHA regions according to the image attached.</p>
<p>ref: American Heart Association Writing Group on Myocardial Segmentation and Registration for Cardiac Imaging:, et al. “Standardized myocardial segmentation and nomenclature for tomographic imaging of the heart: a statement for healthcare professionals from the Cardiac Imaging Committee of the Council on Clinical Cardiology of the American Heart Association.”  <em>Circulation</em>  105.4 (2002): 539-542.</p>

---

## Post #6 by @lassoan (2020-06-14 05:10 UTC)

<p>Probably the best tool to partition a structure like this is the Dynamic modeler module. You can place all the cutting planes and create models from all intersection combinations. One example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d48aff4d371f2b944144f4f19724d0f8526feba1.jpeg" data-download-href="/uploads/short-url/ukf1ujUlCphXOfxZrR9qPHE22MF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d48aff4d371f2b944144f4f19724d0f8526feba1_2_690x418.jpeg" alt="image" data-base62-sha1="ukf1ujUlCphXOfxZrR9qPHE22MF" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d48aff4d371f2b944144f4f19724d0f8526feba1_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d48aff4d371f2b944144f4f19724d0f8526feba1_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d48aff4d371f2b944144f4f19724d0f8526feba1_2_1380x836.jpeg 2x" data-dominant-color="B6B5B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1369 649 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Extracting all the 17 segments would be somewhat tedious, so probably it would worth to write a short script to automate this.</p>
<p>Assuming you can partition the LV wall with these cutting planes, what is the next step? What would you like to compute? Volumes, thickness, or their changes throughout the cardiac cycle, …? How many data sets do you plan to analyze?</p>

---
