# Image Orientation in SlicerIGTs Volume Reslice Driver

**Topic ID**: 42526
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/image-orientation-in-slicerigts-volume-reslice-driver/42526

---

## Post #1 by @Khaleel_Ur_Rehman (2025-04-10 18:13 UTC)

<p>Hi, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, I am using volume reslice driver to visualize registration and tracking using an optical tracking system. The reslice driver is working good. As you might know that the driver has the generic Axial, Coronal, Sagittal View and also cross sectional views called Inplane, Inplane 90 and Transverse through which i can get a view of the whole anatomy. I am more interested towards the latter modes as they provide a proper cross sectional view. But the issue is that unlike the axial, coronal and saggital modes where the images in the MPR stay static even with changes in the drivers orientation, the inplane, inplane 90 and transverse mode are rotating with the rotation of the driver. Instead of the image rotating in the MPR, i want the driver to rotate in the visualization without compromising the cross sectional view. I also looked into the volumereslicedriver logic. Do let me know a solution through which i can make changes from the python console itself rather than building the extension.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be8bd38a6dfc2ea986c46183c5fb5a167ac414b3.png" data-download-href="/uploads/short-url/rbEilvwffgvyjtfOGreS9O1FhHZ.png?dl=1" title="Screenshot 2025-04-10 111808" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be8bd38a6dfc2ea986c46183c5fb5a167ac414b3.png" alt="Screenshot 2025-04-10 111808" data-base62-sha1="rbEilvwffgvyjtfOGreS9O1FhHZ" width="287" height="500" data-dominant-color="171C22"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-10 111808</span><span class="informations">844×1467 33.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-04-10 18:23 UTC)

<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="42526">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p>i want the driver to rotate in the visualization without compromising the cross sectional view</p>
</blockquote>
</aside>
<p>Please explain this in more detail, with a few illustrative pictures. But if it turns out that none of the reslicing modes in Volume Reslice Driver does exactly what you need then it is really easy to implement your own logic in a short Python script. You can add an observer to the reslicing transform and then update the slice position and orientation in the callback function. For example, if you want to reduce spinning of the image around the slice plane normal then you can run <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position">this code snippet</a> in the callback function.</p>

---
