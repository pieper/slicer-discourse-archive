---
topic_id: 16802
title: "Compute The Transformation Based On Selected Local Coordinat"
date: 2021-03-28
url: https://discourse.slicer.org/t/16802
---

# Compute the transformation based on selected local coordinate system

**Topic ID**: 16802
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/compute-the-transformation-based-on-selected-local-coordinate-system/16802

---

## Post #1 by @Tekk_ya (2021-03-28 18:12 UTC)

<p>Hi 3DSlicer community,</p>
<p>I have a question about computing the transformation matrix for a desired local coordinate system. To be more specific, I have two 3D models, one is a 3D model in its original position, the second is the transformed 3D model using an unknown rigid body transformation. My main goal is to compute the translation and rotation based on the local coordinate system of the 3D model. The local coordinate system can be computed based on the prior knowledge from the 3D model. Basically, I want the rotation angles in terms of yaw, pitch, and roll computed based on the local coordinate axes and the origin which is the center of the mass of the model.</p>
<p>Let’s assume that I have the local coordinate axes and the center of the mass of the object. Is it possible to compute the yaw, pitch, and roll angles based on the desired local coordinate axes?<br>
My original idea was to compute the transformation using the fiducial registration module based on predefined landmarks. Then to decompose it based on the desired local coordinate axes. However, I am not sure if it is the best way to do it or if there is some easier way to do it directly in the 3DSlicer?</p>
<p>Thanks in advance for your help and suggestions</p>

---

## Post #2 by @lassoan (2021-04-03 02:39 UTC)

<p>Fiducial registration wizard module can compute the transform that you can directly apply to the “From” model. See additional registration options here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---

## Post #3 by @Tekk_ya (2021-04-03 10:36 UTC)

<p>Dear Andras,</p>
<p>Thanks for your reply. I think my question is a bit different from what fiducial registration wizard is computing. Please correct me if I am wrong. I have a desired coordinate system in 3D (please check the below image, here the desired coordinate system is x’y’z’ in green color, and the transformed object has is represented as the red vectors). I am interested in computing both translation and rotation values (yaw, pitch, roll) between red and green vectors. I want to compute these values with respect to the x’y’z’ and not just transfer the green coordinate to the red one. I would assume both translation and rotation should be decomposed with respect to the x’y’z’.</p>
<p>Thanks for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dcce3e185f5908cb432500a4588da05804fdc57.png" data-download-href="/uploads/short-url/4fCOWWF9EqSGp9ULM1IKu0dCuUL.png?dl=1" title="coord_question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dcce3e185f5908cb432500a4588da05804fdc57_2_517x297.png" alt="coord_question" data-base62-sha1="4fCOWWF9EqSGp9ULM1IKu0dCuUL" width="517" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dcce3e185f5908cb432500a4588da05804fdc57_2_517x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dcce3e185f5908cb432500a4588da05804fdc57_2_775x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dcce3e185f5908cb432500a4588da05804fdc57.png 2x" data-dominant-color="EDF0F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">coord_question</span><span class="informations">985×566 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-04-03 12:40 UTC)

<p>You can represent a transformation (translation and rotation) in a non-ambiguous way, using a 4x4 homogeneous transformation matrix.</p>
<p>There are then many ways how to decompose this matrix to a series rotations and translations. Rotation can be decomposed by using many variants of Euler angles, Roll-Pitch-Yaw, etc. You can use <a href="https://discourse.slicer.org/t/calculation-of-numerical-data-for-transformation/8064/7">one method that is available in VTK</a> or look up other conversion formulae on Google. The problem with these representations that they are ambiguous and unstable (suffer from gimbal lock), so you need to choose the rotation axes order very carefully, in a way that it makes the most sense and it is the most stable for your application.</p>

---
