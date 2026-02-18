# Crop segment using shapeNode

**Topic ID**: 43822
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/crop-segment-using-shapenode/43822

---

## Post #1 by @bserrano (2025-07-23 09:38 UTC)

<p>Hi all,</p>
<p>I’m working with a segment representing a tubular geometry, and I have a <code>vtkMRMLMarkupsShapeNode</code> representing a cylinder placed at the end of this structure.</p>
<p>I’d like to crop or cut the segment using the plane defined by the cylinder’s base (the red line).</p>
<p>Is there a recommended way to use the shape node’s geometry — particularly the cylinder’s plane — to perform this kind of clipping on the segment?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2cb268e5971d505cc11da04661076b096316b5a.png" data-download-href="/uploads/short-url/u4Lw3dWBgDwfTm8tYGm5vgnRgtc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2cb268e5971d505cc11da04661076b096316b5a.png" alt="image" data-base62-sha1="u4Lw3dWBgDwfTm8tYGm5vgnRgtc" width="524" height="311"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">524×311 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2025-07-23 10:07 UTC)

<p>A GUI method:</p>
<ul>
<li>convert the segment to a model in the Data module (A)</li>
<li>convert the shape to a model using this <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface?ref_type=heads" rel="noopener nofollow ugc">module</a> (B)</li>
<li>perform (A - B) difference in the Combine models module</li>
<li>convert the result to a segmentation in the Data module.</li>
</ul>
<p>Alternatively, scripting in python would be faster. You would need to apply vtkPlane and vtkCutter on the segment’s closed surface representation.</p>

---

## Post #3 by @bserrano (2025-07-23 10:12 UTC)

<p>Many thanks, I’ll try it. Is there any possibility of doing this directly using segmentation nodes instead of models?</p>

---

## Post #4 by @chir.set (2025-07-23 10:29 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="43822">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>using segmentation nodes instead of models?</p>
</blockquote>
</aside>
<p>Yes, you can create a segment from the shape and then use the <code>Logical operators</code> effect.</p>

---

## Post #5 by @chir.set (2025-07-23 10:33 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="43822">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>apply vtkPlane and vtkCutter on the segment’s closed surface representation.</p>
</blockquote>
</aside>
<p>Erratum : <code>vtkCutter</code> won’t be useful actually, but <code>vtkClipPolyData</code> and/or <code>vtkClipClosedSurface</code> would be more appropriate.</p>

---

## Post #6 by @bserrano (2025-07-23 10:38 UTC)

<p>Thanks, how can I do that?</p>

---

## Post #7 by @chir.set (2025-07-23 11:48 UTC)

<p>VTK classes are very well documented with example code available. For instance, the <a href="https://vtk.org/doc/nightly/html/classvtkClipClosedSurface.html" rel="noopener nofollow ugc">vtkClipClosedSurface</a> online page points to <a href="https://vtk.org/doc/nightly/html/c2_vtk_t_3.html#c2_vtk_t_vtkClipClosedSurface" rel="noopener nofollow ugc">sample</a> use cases.</p>

---

## Post #8 by @bserrano (2025-07-23 12:00 UTC)

<p>I am trying but I cannot figure out how to convert the ‘vtkMRMLMarkupsShapeNode’ (cylinder) to model. Lastly I tryied with markups to model, but it only creates a triangle with the 3 points that define the cylinder</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd48b76d24ed5b4fbad3ba6522d1ffc1d8a5e66f.png" data-download-href="/uploads/short-url/A8EAQYlP3CvHF6UrVQG2QrcPT7p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd48b76d24ed5b4fbad3ba6522d1ffc1d8a5e66f.png" alt="image" data-base62-sha1="A8EAQYlP3CvHF6UrVQG2QrcPT7p" width="159" height="198"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">159×198 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @chir.set (2025-07-23 13:00 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="8" data-topic="43822">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>how to convert the ‘vtkMRMLMarkupsShapeNode’ (cylinder) to model</p>
</blockquote>
</aside>
<p>You can get the polydata of the Shape node like <a href="https://gitlab.com/chir-set/Tools7/-/blob/023b72cbb85e48ce53d91bf70ca34219f8d002d1/MarkupsToSurface/MarkupsToSurface.py#L467" rel="noopener nofollow ugc">here</a>.</p>
<p>And create a model from the polydata as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/models.html#show-a-simple-surface-mesh-as-a-model-node" rel="noopener nofollow ugc">there</a>.</p>

---

## Post #10 by @bserrano (2025-07-23 13:18 UTC)

<p>It works <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=14" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>This is the code, just in case is useful for anybody else:</p>
<pre><code class="lang-auto">shapeNode = getNode('MyMarkupsCylinder')
nodePolyData = shapeNode.GetShapeWorld()
modelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", "MyModel")
modelNode.SetAndObservePolyData(nodePolyData)
modelNode.CreateDefaultDisplayNodes()
modelNode.GetDisplayNode().SetColor(1, 0, 0)
</code></pre>
<p>Then I imported modelNode as segment using Segmentations module.</p>

---
