# Landmark registration morphing ? rigid registration as preprocessing?

**Topic ID**: 26621
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/landmark-registration-morphing-rigid-registration-as-preprocessing/26621

---

## Post #1 by @Nicolas_Tempier (2022-12-07 10:20 UTC)

<p>Hi !<br>
i want to registrate a 2D “really high resolution” (29000x26000) as floating image to a “normal” reference image (600x900)<br>
Knowing that the high resolution floating image is the same image as the reference one but histologically modified (which implies tissue intensity and morphology differences)</p>
<p>I was wondering if it was worth it to first make a rigid registration and then us landmark registration or to jump to landmark registration ?<br>
the goal being to have overlapping areas at the end to draw roi from histological image to reference image.<br>
Thanks already <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>N.</p>

---

## Post #2 by @lassoan (2022-12-07 22:06 UTC)

<p>The first step would be to downsample the high-resolution image to have approximately the same spacing as the reference image (the extra resolution does not add much value to the registration, as precision of the alignment is limited by the reference image). It would be also useful to crop the images so that they cover approximately the same region.</p>
<p>Then you can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration tools</a> as usual. Typically, you start with a landmark-based approximate rigid alignment, followed by automatic intensity based rigid+bspline image-based registration.</p>
<p>Most presets in the image registration tools are for 3D-to-3D registration, so you may need to tune the parameters to do 2D-to-2D registration.</p>

---

## Post #3 by @pieper (2022-12-08 20:06 UTC)

<p>If you are using the LandmarkRegistration module and the images can be loaded as Volumes in Slicer with proper spacing then you can leave them at the native resolution.  You should be able to place down landmarks at visible common reference points and then drag the points to make the images match.  ThinPlate spline with hot update can good for this once you get the hang of it.</p>

---

## Post #4 by @Nicolas_Tempier (2022-12-09 07:24 UTC)

<p>Ok thanks for your answers that is what I did, I was just wondering whether it was worth to first make a rigid registration, keep the transform, apply it to the high res image to keep the native resolution, then maybe do another registration maybe affine this time, do the same and at the end make the LandmarkRegistration OR just do the LandmarkRegistration but I think I got it right now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> thanks</p>

---
