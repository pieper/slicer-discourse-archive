# Curved planar Reformat Resampling transformation

**Topic ID**: 16182
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/curved-planar-reformat-resampling-transformation/16182

---

## Post #1 by @FloCo (2021-02-24 13:39 UTC)

<p>Hi everyone,</p>
<p>I have been trying to do a curved planar reformat for a while until I discovered the Curved Planar Reformat module recently which does exactly what I need so thank you for this module !<br>
Since I tried to implement the same on myself before and got problems for very tortuous<br>
centerlines, I am curious about your implementation since it works really well in any cases.</p>
<p>I understand how displacements and the grid are calculated with Frenet-Serret frame but I really don’t have good skills in C++ and I can’t find out what is done in the resamplescalarvectordwivolume file. Do you use global ThinPlanSpline transform with all displacements you found ? How do you handle cases with different information of displacements for very close voxels (tortuous centerlines) ?</p>
<p>Thanks for any information.</p>

---

## Post #2 by @lassoan (2021-02-24 15:40 UTC)

<aside class="quote no-group" data-username="FloCo" data-post="1" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>I am curious about your implementation since it works really well in any cases</p>
</blockquote>
</aside>
<p>It is indeed amazing how it was possible to combine work of very smart people (Luca Antiga’s centerline extraction in VMTK, David Gobbi’s transformation framework in VTK, <span class="mention">@piper</span>’s idea of generating a dense displacement field using 4 corner points of a series of slices) to create a robust and powerful curved planar reformat approach, which is distortion free (within in the straightened volume slices and along the centerline), fast, and it is also invertible, so any objects (positions, lines, curves, images, models) defined in the straightened space can be transformed to the original space and vice versa. There is a chance that this has not been done like this before, but I did not have the time to do literature search and write up a paper about this.</p>
<p>If you were interested in having a highly cited an impactful academic paper then you could write up how this module works and evaluate its performance on a few use cases. I would not spend time with writing this by myself, but would be happy to help someone writing it.</p>
<aside class="quote no-group" data-username="FloCo" data-post="1" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>I understand how displacements and the grid are calculated with Frenet-Serret frame</p>
</blockquote>
</aside>
<p>As it turns out, it is actually not a Frenet-Serret frame. That would be unusable, as it is undefined where the curve has low curvature and there are huge spins in the frame at inflection points. Instead, when Frenet-Serret class is used with “consistency” option enabled, then actually it computes a parallel transport frame.</p>
<aside class="quote no-group" data-username="FloCo" data-post="1" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>can’t find out what is done in the resamplescalarvectordwivolume file</p>
</blockquote>
</aside>
<p>That’s an ITK filter and all it does is that it resamples an image with a displacement field specified by a transform. The transform is a grid transform created from 4 corner points of slice planes determined by parallel transfer frame. The illustrations here explain the method quite nicely: GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished implementations but can be useful to users</p>
<aside class="quote no-group" data-username="FloCo" data-post="1" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>Do you use global ThinPlanSpline transform with all displacements you found ?</p>
</blockquote>
</aside>
<p>We don’t use thin-plate spline for this at all, mostly because it would be hard to control distortion.</p>
<aside class="quote no-group" data-username="FloCo" data-post="1" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>How do you handle cases with different information of displacements for very close voxels (tortuous centerlines) ?</p>
</blockquote>
</aside>
<p>We just rely on the parallel transport frame to determine minimum-rotation frame, then use this to extract an exact, non-distorted frame from the original image space. The advantage of this that there is no distortion within the “z” slices of the straightened volume (so you can make accurate measurements anywhere within a z slice), all the distance measurements are correct along the centerline, and distortion gradually increases as you get farther from the centerline, so you can make pretty good 3D measurements close to the centerline.</p>
<p>If you have very tortuous centerline then some regions will be simply duplicated, but these regions are always lie farther from the centerline, so that you can safely ignore them. They can only cause problems with the inverse computation (as one region in the original image is mapped to several regions in the straightened image), so if you need inverse computation then it is advisable to reduce the slice size.</p>

---

## Post #3 by @FloCo (2021-02-25 09:24 UTC)

<p>First of all, thank you for your fast and very complete answer !</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is a chance that this has not been done like this before, but I did not have the time to do literature search and write up a paper about this.</p>
</blockquote>
</aside>
<p>Unfortunately I don’t have access to many papers to do a lot of literature but that’s the first time I see this kind of process indeed. I am not looking for academic papers since I am not in the research field anymore but it would be really interesting to have a paper on this approach.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The illustrations here explain the method quite nicely: GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished implementations but can be useful to users</p>
</blockquote>
</aside>
<p>From the illustrations I understand that we can control the problem of tortuous centerline by reducing the slice size or by having a lowest curve resolution. This avoid planes to get mixed and the transform stays invertible.<br>
What I am not sure to understand is that the displacement field is only calculated from 4 corner points of each slice planes. Then the displacement field must be interpolated for each slice from the 4 corner points and between each slice I guess ? Do you use a simple linear interpolation ?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We don’t use thin-plate spline for this at all, mostly because it would be hard to control distortion.</p>
</blockquote>
</aside>
<p>I thought about thin-plate spine because it’s a common method to smooth interpolation even if it has a high computational cost. When I tried it I got a lot of distortions indeed but I only used points from the centerline and not from corner points as you do, I can try to see the difference.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The advantage of this that there is no distortion within the “z” slices of the straightened volume (so you can make accurate measurements anywhere within a z slice)</p>
</blockquote>
</aside>
<p>I think the distorsion within the “z” slices depend on the curve resolution. It can avoid to mix planes between them but it will also lose information about the centerline. I guess it’s better to reduce slice size as you said if I want to keep the inverse computation.</p>

---

## Post #4 by @lassoan (2021-02-25 18:47 UTC)

<aside class="quote no-group" data-username="FloCo" data-post="3" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>What I am not sure to understand is that the displacement field is only calculated from 4 corner points of each slice planes. Then the displacement field must be interpolated for each slice from the 4 corner points and between each slice I guess ? Do you use a simple linear interpolation ?</p>
</blockquote>
</aside>
<p>We use linear interpolation, but by replacing vtkGridTransform by vtkBSplineTransform you can get bspline interpolation. However, then you would introduce distortion and you could no longer do accurate measurements in slices. It may be added as an option to the reformat module if somebody finds an application where smoother displacement field is more important then quantitative measurements.</p>
<aside class="quote no-group" data-username="FloCo" data-post="3" data-topic="16182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/2bfe46/48.png" class="avatar"> FloCo:</div>
<blockquote>
<p>I thought about thin-plate spine because it’s a common method to smooth interpolation even if it has a high computational cost. When I tried it I got a lot of distortions indeed but I only used points from the centerline and not from corner points as you do, I can try to see the difference.</p>
</blockquote>
</aside>
<p>We tried thin-plate spline transforms with control points added at certain distances from the centerline, but it did not work well. Distortion was very unpredictable and hard to control, and computation was much slower.</p>

---

## Post #5 by @FloCo (2021-02-26 07:17 UTC)

<p>That’s all clear thank you very much for your time. I’ll continue to use 3D Slicer and see if I have other questions or ideas to implement.</p>

---
