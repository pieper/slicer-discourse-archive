# Move transform not image when using volume reslice driver

**Topic ID**: 8712
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/move-transform-not-image-when-using-volume-reslice-driver/8712

---

## Post #1 by @Prashant_Pandey (2019-10-08 22:08 UTC)

<p>Hi,</p>
<p>We are developing a navigation system for use with CT images and optically tracked tools. We’re using the volume reslice driver to reslice the image views in real-time with respect to tool position and orientation, but our surgeons would prefer to if the image was still (still resliced) and the tool moved around it. At the moment the tool is stationary and the image moves around it.</p>
<p>Also, how do you reslice an image based on an abitrary axis? We have cylindrical models (representing screws) placed in our image, and would like to reslice our slice views along the axes of these models.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-10-08 22:51 UTC)

<p>These are all completely configurable. You need to set up your transform tree keeping in mind that the root of the transform tree is the renderer world coordinate system. So, objects in that coordinate system will be stationary in the viewers (unless of course you move the slice view plane or camera).</p>
<p>Usually we define coordinate system for positioning screw model and use the same transform in volume reslice driver to align the views with the screw.</p>
<p>Reconfiguring these on the GUI involves switching between modules and change a number of parameters, so once you figured out what visualization modes you need, it can make sense to implement their setup in Python (probably 10-15 lines of code).</p>

---

## Post #3 by @Prashant_Pandey (2019-10-09 04:55 UTC)

<p>I’m not sure I totally understand your solution. Here is the transform tree:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e662e11753830dfa63ee9df260280ce9323e25.png" alt="image" data-base62-sha1="nf4WVBMXJjgULiC14LT3Fq5DNfD" width="388" height="361"></p>
<p>For reslicing I set GuideTipToGuide as the driver. The CT (CT_crop) is the image of interest. From my understanding the root here is the RAS coordinate system, and the CT image is in that coordinate system?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60422571b87f26a63ac147056f1bf5692fb74097.png" alt="image" data-base62-sha1="dJxyoYK7ZAijSFolbeOBYQUf02j" width="455" height="352"></p>

---

## Post #4 by @lassoan (2019-10-09 11:36 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="3" data-topic="8712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>the root here is the RAS coordinate system, and the CT image is in that coordinate system?</p>
</blockquote>
</aside>
<p>Exactly. This means that the CT image will be always stationary.</p>
<p>For example, if you want your CT image to move in the 3D view when the patient moves then you can use the Tracker coordinate system as root (and rearrange the transform tree accordingly).</p>
<p>Alternatively, you can make objects appear as moving on screen (even if they are stationary in the root coordinate system), by translating/rotating slice view planes or 3D view’s camera.</p>

---

## Post #5 by @Prashant_Pandey (2019-10-09 17:32 UTC)

<p>Sorry I think I wasn’t clear from the beginning.</p>
<p>The CT <strong>is</strong> stationary in the 3D viewer as expected and as desired by our surgeons. However, the CT is not stationary in the <strong>red/yellow slices</strong> when using the volume reslice driver and setting the driver to GuideTipToGuide. Instead the tool model (‘Locator_GuideToReference’ from the tree above) has stationary pose while the CT’s pose changes as the tool is moved. We would like it so that the tool is moving around and the CT is fixed in translation and rotation while being resliced in the <strong>slice views</strong>. Perhaps I need to calculate a new RASToGuideTip transform by inversing and chaining the existing transforms, and use that as the driver?</p>

---

## Post #6 by @lassoan (2019-10-09 22:33 UTC)

<p>Volume reslice driver has modes that force the slice orientation to an anatomical direction and just take the position from the tool transform.</p>
<p>You can display the tool model as projection to visualize out-of-plane parts of the model (configurable in Models module).</p>
<p>You can also define custom rules for computing slice pose from tool pose. See this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_a_normal_vector_and_position" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_a_normal_vector_and_position</a></p>

---

## Post #7 by @Prashant_Pandey (2019-10-12 01:58 UTC)

<p>Thanks, I will take a look at that example.</p>

---

## Post #8 by @lassoan (2019-10-15 22:45 UTC)

<p>2 posts were split to a new topic: <a href="/t/clipping-of-models-is-too-slow/8788">Clipping of models is too slow</a></p>

---
