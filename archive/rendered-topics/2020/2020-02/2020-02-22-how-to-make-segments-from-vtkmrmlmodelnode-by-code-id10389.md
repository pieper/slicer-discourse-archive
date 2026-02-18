# How to make segments from vtkMRMLModelNode by code

**Topic ID**: 10389
**Date**: 2020-02-22
**URL**: https://discourse.slicer.org/t/how-to-make-segments-from-vtkmrmlmodelnode-by-code/10389

---

## Post #1 by @apparrilla (2020-02-22 01:10 UTC)

<p>Hi,<br>
I have some ModelNodes from .vtk files attacked to lineartransforms.<br>
With this code i get new segments for each model in segmentation but with wrong location.<br>
How to fix segments position?</p>
<blockquote>
<p>name = model.GetName()<br>
abstransform = model.GetParentTransformNode().GetTransformFromParent()<br>
applyTransform = vtk.vtkTransformPolyDataFilter()<br>
applyTransform.SetTransform(abstransform )<br>
applyTransform.SetInputData(model.GetPolyData())<br>
applyTransform.Update()<br>
surface = applyTransform.GetOutput()<br>
# Remove point arrays to make sure they don’t affect display color<br>
while surface.GetPointData().GetNumberOfArrays()&gt;0:<br>
surface.GetPointData().RemoveArray(0)<br>
segmentation.AddSegmentFromClosedSurfaceRepresentation(surface, name, [1,1,1])</p>
</blockquote>
<p>Thanks on advance!</p>

---

## Post #2 by @Juicy (2020-02-22 02:41 UTC)

<p>I don’t understand exactly what you are trying to do but would hardening the transform help?</p>
<p>Take a look at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_harden_a_transform_.3F" rel="nofollow noopener">this page.</a> For an example of how to harden the transform using python.</p>
<p>Otherwise perhaps you have to also put the new segments in the linear transform so they also end up in the same location as the models?</p>

---

## Post #3 by @lassoan (2020-02-22 03:11 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="10389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>With this code i get new segments for each model in segmentation but with wrong location.</p>
</blockquote>
</aside>
<p>If you load the .vtk files as models (using File / Add data) do they appear at the correct position?</p>

---

## Post #4 by @apparrilla (2020-02-22 09:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="10389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you load the .vtk files as models (using File / Add data) do they appear at the correct position?</p>
</blockquote>
</aside>
<p>No, they appear but in wrong position.</p>

---

## Post #5 by @apparrilla (2020-02-22 10:27 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="2" data-topic="10389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>Otherwise perhaps you have to also put the new segments in the linear transform so they also end up in the same location as the models?</p>
</blockquote>
</aside>
<p>I tried it before, but individual segments are not transformable nodes.<br>
To harden model transform works right.<br>
Thanks so much.</p>

---
