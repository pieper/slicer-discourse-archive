---
topic_id: 15682
title: "Merge Scalars Of Two Models"
date: 2021-01-26
url: https://discourse.slicer.org/t/15682
---

# Merge scalars of two models

**Topic ID**: 15682
**Date**: 2021-01-26
**URL**: https://discourse.slicer.org/t/merge-scalars-of-two-models/15682

---

## Post #1 by @Honza_Hecko (2021-01-26 21:18 UTC)

<p>Hi,<br>
can I have a question? I have merged two models by extension CMFreg. One of them has Scalars (Unipolar, Bipolar, LAT) and the second is a model from CT (SegmentEditor). I want (maybe need) to move Scalars from one model to the other. The first model is .vtk. Is there some opinion haw to make that?<br>
Thank you so much for your answer and wish you nice days.<br>
Honza</p>

---

## Post #2 by @timeanddoctor (2021-01-27 02:56 UTC)

<p>You can import this models and then use the module merge models.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fabae24f7248854353bdd6b3dda457e58c88009.png" data-download-href="/uploads/short-url/bmNxGRlFPkLZIsraS6JNscKB84V.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fabae24f7248854353bdd6b3dda457e58c88009.png" alt="image" data-base62-sha1="bmNxGRlFPkLZIsraS6JNscKB84V" width="569" height="500" data-dominant-color="CDCDCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">622×546 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-01-27 03:36 UTC)

<p>If you want to keep the models separate and just copy the scalar data then you can achieve it by following these steps:</p>
<ul>
<li>install ModelToModelDistance extension and use Model to model distance module to compute vector that moves points of one surface to the other (based on closest point of one surface on the other) - result will be stored in <code>PointToPointVector</code> point array of the output mesh</li>
<li>use vtkWarpVector filter with <code>PointToPointVector</code> to warp the model to match the surface of the other model</li>
<li>use vtkProbeFilter to get scalar values for each point</li>
<li>copy over the point data to the original (unwarped) mesh</li>
</ul>
<p>The first step is running the module, the other steps are running a VTK filter (few lines of Python code each). See examples of running VTK filters on model nodes in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #4 by @Honza_Hecko (2021-01-28 07:41 UTC)

<p>Hello,<br>
the method with the merge model was not able to convert the scalars. Method by Andras I was able to perform the first steps, but these:</p>
<p>use vtkWarpVector filter with PointToPointVector to warp the model to match the surface of the other model<br>
use vtkProbeFilter to get scalar values for each point<br>
copy over the point data to the original (unwarped) mesh</p>
<p>would I need to elaborate perhaps in more detail?<br>
thank you for answer</p>

---

## Post #5 by @Honza_Hecko (2021-01-28 08:05 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30a234f0257a3e23dcabba6113f79d47e2049f50.jpeg" data-download-href="/uploads/short-url/6WerAFU9yKXqP2UkSZw2V5Ff1HG.jpeg?dl=1" title="Bez názvu" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30a234f0257a3e23dcabba6113f79d47e2049f50_2_256x500.jpeg" alt="Bez názvu" data-base62-sha1="6WerAFU9yKXqP2UkSZw2V5Ff1HG" width="256" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30a234f0257a3e23dcabba6113f79d47e2049f50_2_256x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30a234f0257a3e23dcabba6113f79d47e2049f50_2_384x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30a234f0257a3e23dcabba6113f79d47e2049f50_2_512x1000.jpeg 2x" data-dominant-color="A7A8B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bez názvu</span><span class="informations">1948×3792 845 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
