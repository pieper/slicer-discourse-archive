# How to creat .stl model from DICOM USING 3D Slicer?

**Topic ID**: 22100
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/how-to-creat-stl-model-from-dicom-using-3d-slicer/22100

---

## Post #1 by @Moh_d_Al-Watary (2022-02-22 02:36 UTC)

<p>Dear Friend, wish you are doing fine.<br>
I am working on a project in which I need to use .stl files from CT scan in DICOM format. So I need to change the format to. stl and creat 3d model how could this be done?<br>
Also, I want to do a superimposition of two different times CT using 3D Slicer: I am using CMReg…Surface Regi… but I do not know why it is not working? I had the CT in good relation but the mesh formed away from both CT, and when I use Model to model distance the numbers wrong as showed by mesh statistics… Could you please help me in this?<br>
Thank you again and wish to hear from you soon.</p>

---

## Post #2 by @lassoan (2022-02-23 07:14 UTC)

<aside class="quote no-group" data-username="Moh_d_Al-Watary" data-post="1" data-topic="22100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moh_d_al-watary/48/14124_2.png" class="avatar"> Moh_d_Al-Watary:</div>
<blockquote>
<p>I am working on a project in which I need to use .stl files from CT scan in DICOM format. So I need to change the format to. stl and creat 3d model how could this be done?</p>
</blockquote>
</aside>
<p>You will need to segment the image. See more information here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="Moh_d_Al-Watary" data-post="1" data-topic="22100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moh_d_al-watary/48/14124_2.png" class="avatar"> Moh_d_Al-Watary:</div>
<blockquote>
<p>I want to do a superimposition of two different times CT using 3D Slicer: I am using CMReg…Surface Regi… but I do not know why it is not working?</p>
</blockquote>
</aside>
<p>Surface registration cannot be used for registering images, only two meshes, and only if they are initially transformed close to each other. See more information about applicable registration techniques here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---
