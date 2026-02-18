# Registration MRI breast with segmentation

**Topic ID**: 16703
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/registration-mri-breast-with-segmentation/16703

---

## Post #1 by @Mgi (2021-03-22 22:46 UTC)

<p>Hi Everyone!</p>
<p>I am working with 3D slicer 4.11.2 version on windows. I want to register intra subject breast substraction mri images, where I made one ROI segmentation, with DWI b0 images. Could you tell me which is the better slicer module to make the registration including the segmented ROI.</p>
<p>I am a novice in registration field. Hope for any kind help or comment, thanks a lot!</p>

---

## Post #2 by @lassoan (2021-03-23 05:10 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">This documentation page</a> should help you getting started. If you can post a few screenshot and experience with some of the registration methods and can tell a bit more about your constraints (time, accuracy, robustness, availability of expert for semi-automatic methods, etc.) then we can give more specific advice.</p>

---

## Post #3 by @Mgi (2021-03-23 13:42 UTC)

<p>Thank you! <a class="mention" href="/u/lassoan">@lassoan</a>  I’m going to explain more about what I want to do:<br>
Already made:</p>
<ol>
<li>I generate 1 frame of the subtraction mri image from the dynamic images using Multivolume module</li>
<li>I segmented one ROI from the subtraction breast mri image using Segment editor module<br>
Now:</li>
<li>I want to register the subtraction mri image with the DWI b0 image (intrasubject), acquired in the same study</li>
<li>I want to use the segmentation made early (step 2) in the DWI b0 image (Then I need the registration process include the transformations to the segmented ROI)</li>
<li>I want to calculate the ADC for different b values in DWI images</li>
</ol>
<p>Hope for any kind help or comment, thanks a lot!</p>

---

## Post #4 by @lassoan (2021-03-24 17:07 UTC)

<p>Registration for compensating minor displacements due to patient motion during an imaging session should be quite straightforward if there are some common features between the images. You can try SlicerElastix default registration presets.</p>
<p>The computed transform can be applied to any nodes, including segmentations.</p>
<aside class="quote no-group" data-username="Mgi" data-post="3" data-topic="16703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b19c9b/48.png" class="avatar"> Mgi:</div>
<blockquote>
<p>I want to calculate the ADC for different b values in DWI images</p>
</blockquote>
</aside>
<p>If you need help with this then it is better to create a new topic; and keep this topic focused on registration.</p>

---
