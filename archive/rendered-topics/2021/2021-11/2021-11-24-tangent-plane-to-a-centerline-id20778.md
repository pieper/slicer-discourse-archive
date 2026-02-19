---
topic_id: 20778
title: "Tangent Plane To A Centerline"
date: 2021-11-24
url: https://discourse.slicer.org/t/20778
---

# Tangent plane to a centerline

**Topic ID**: 20778
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/tangent-plane-to-a-centerline/20778

---

## Post #1 by @bserrano (2021-11-24 16:20 UTC)

<p>Is there any way to obtain planes tangent to a centerline?</p>
<p>Thanks</p>

---

## Post #2 by @bserrano (2021-11-25 15:54 UTC)

<p>is it possible to obtain tangent planes to a centerline in a similar way that perpendicular plane when using cross-section analysis?</p>

---

## Post #3 by @lassoan (2021-11-25 21:23 UTC)

<p>I’ve added a second (“longitudinal”) slice to Cross-section analysis module in SlicerVMTK extension. It will be available for the Slicer Preview Release tomorrow.</p>
<p>Alternatively, you can use the Endoscopy module to create a reslicing transform along a curve. That transform can be used for driving a slice view (normal and tangent directions), using “Volume reslice driver” module in SlicerIGT extension.</p>

---

## Post #5 by @bserrano (2021-11-26 12:00 UTC)

<p>Thanks for the addition of the longitudinal view. I am trying to get orthogonal planes, but “axial” and “long” planes are not so by default. I can manage to adjust the longitudinal plane manually to obtain a perpendicular plane but is there any way to obtain orthogonal planes automatically?</p>
<p>Is it possible to avoid “endoscopic 3d view” in Endoscopy module? So I can view where the plane is instead of going inside?<br>
Example: this view</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60c16e47cd06e8b014b2aefda4e9f6a73c3b971d.png" alt="imagen" data-base62-sha1="dNWga9cAQEHiykaZ1XKazfVJ0gR" width="303" height="279"></p>
<p>Many thanks <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @bserrano (2021-11-29 08:40 UTC)

<p>Regarding avoidind endoscopy 3d view: Already done that deleting the current camera in module “cameras”.</p>

---

## Post #7 by @lassoan (2021-11-29 14:01 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="5" data-topic="20778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Thanks for the addition of the longitudinal view. I am trying to get orthogonal planes, but “axial” and “long” planes are not so by default.</p>
</blockquote>
</aside>
<p>The views are always orthogonal and longitudinal (tangential), the additional sliders are just for specifying the additional degrees of freedoms for rotations (orientation of the view up vector in slice view and rotation of the curve normal vector).</p>
<p>Depending on the resolution of the input image and radius of the extracted vessel, the centerline may be noisy. You can fix that by resampling the curve with less control points (10-20?) in Markups module’s Resample section.</p>
<aside class="quote no-group" data-username="bserrano" data-post="5" data-topic="20778">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Is it possible to avoid “endoscopic 3d view” in Endoscopy module? So I can view where the plane is instead of going inside?</p>
</blockquote>
</aside>
<p>You can go to Cameras module, create a new camera, and then choose this new camera in Endoscopy module. This will effectively disable the camera animation, because the new camera is not used in any 3D view,</p>

---

## Post #8 by @bserrano (2025-06-05 06:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="20778">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The views are always orthogonal and longitudinal (tangential), the additional sliders are just for specifying the additional degrees of freedoms for rotations (orientation of the view up vector in slice view and rotation of the curve normal vector).</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>I’ve been working with planes that are perpendicular and tangential (longitudinal) to a centerline in Slicer.</p>
<p>I understand that the views are always orthogonal and tangential to the centerline, and that additional sliders control degrees of freedom like the rotation of the curve’s normal vector.</p>
<p>My question is: How does Slicer determine the orientation of the tangential plane when the rotation angle is set to 0°?</p>
<p>Specifically, how does it know how to align the up vector or normal to separate, for example, a vessel into superior and inferior zones in a consistent way? (see figure)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe3e8c164d00c26f60dadea65067371c9b288e51.jpeg" data-download-href="/uploads/short-url/Ah9hCN1i8CbohgQUZImIoEyqM5b.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3e8c164d00c26f60dadea65067371c9b288e51_2_690x382.jpeg" alt="imagen" data-base62-sha1="Ah9hCN1i8CbohgQUZImIoEyqM5b" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3e8c164d00c26f60dadea65067371c9b288e51_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3e8c164d00c26f60dadea65067371c9b288e51_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe3e8c164d00c26f60dadea65067371c9b288e51.jpeg 2x" data-dominant-color="88C188"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1300×720 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance!</p>

---

## Post #9 by @lassoan (2025-06-07 15:06 UTC)

<p>Establishing a stable  and consistent curve coordinate system is a complex task, but thanks to contributions by VMTK and Slicer developers, the <a href="https://github.com/Slicer/vtkAddon/blob/main/vtkParallelTransportFrame.h">vtkParallelTransportFrame</a> class has been developed that solves this very nicely.</p>
<p>For tangential plane you need two axis directions. One is the curve’s tangent vector, which is trivial to compute. The other is the curve normal, which is the hard task, because it has to be orthogonal to the curve at every point and change smoothly along the curve. This is computed by the parallel transport frame algorithm, starting from an initial normal (or binormal) direction specified by <code>PreferredInitialNormalVector</code> (or <code>PreferredInitialBinormalVector</code> properties). You can get the parallel transport frame object from the curve node by calling <code>GetCurveCoordinateSystemGeneratorWorld()</code>.</p>

---
