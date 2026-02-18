# Getting ROI bounds from vtkMRMLMarkupsROINode

**Topic ID**: 19852
**Date**: 2021-09-25
**URL**: https://discourse.slicer.org/t/getting-roi-bounds-from-vtkmrmlmarkupsroinode/19852

---

## Post #1 by @masadcv (2021-09-25 15:47 UTC)

<p>I am looking into switching from <code>vtkMRMLAnnotationROINode</code> to <code>vtkMRMLMarkupsROINode</code> node for selecting ROI bounding box within a volume.</p>
<p>Previously I have been using <code>GetBounds()</code> function to quickly get bounding box of the ROI from <code>vtkMRMLAnnotationROINode</code>. The code looked like as follows:</p>
<pre><code class="lang-auto">roiNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLAnnotationROINode")
roi_points_ras = [0.0] * 6
roiNode.GetBounds(roi_points_ras)
selected_roi = convertRasToIJK(roi_points_ras)
</code></pre>
<p>Now with the <code>vtkMRMLMarkupsROINode</code>, I am trying to get the same functionality. But it seems like it does not have a <code>GetBounds()</code> function with similar output. How can I achieve the same with this node?</p>
<p>Here is my code until now:</p>
<pre><code class="lang-auto">roiNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsROINode")
center = [0] * 3
roiNode.GetCenter(center)
roi_points_ras = [(x-s/2, x+s/2) for x, s in zip(center, roiNode.GetSize())]
roi_points_ras=[item for sublist in roi_points_ras for item in sublist]
selected_roi = convertRasToIJK(roi_points_ras)
</code></pre>
<p>Maybe I am missing something here and perhaps there is a starightforward way of getting roi bounding box in IJK coordinate space with <code>vtkMRMLMarkupsROINode</code>. If this is the case, kindly can someone guide me how to achieve the above.</p>
<p>Many thanks!<br>
Muhammad</p>

---

## Post #2 by @jamesobutler (2021-09-25 18:37 UTC)

<aside class="quote no-group" data-username="masadcv" data-post="1" data-topic="19852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masadcv/48/10632_2.png" class="avatar"> masadcv:</div>
<blockquote>
<p>Now with the <code>vtkMRMLMarkupsROINode</code> , I am trying to get the same functionality. But it seems like it does not have a <code>GetBounds()</code> function with similar output.</p>
</blockquote>
</aside>
<p>I believe you must be mistaken as the new ROI node type does have a <code>GetBounds()</code> method with results just like the previous.</p>
<pre data-code-wrap="python"><code class="lang-python">old_roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
old_roi.SetRadiusXYZ(5,10,15)
old_roi_bounds = [0]*6
old_roi.GetBounds(old_roi_bounds)
print(old_roi_bounds)
# [-5.0, 5.0, -10.0, 10.0, -15.0, 15.0]

new_roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
new_roi.SetRadiusXYZ(5,10,15)
new_roi_bounds = [0]*6
new_roi.GetBounds(new_roi_bounds)
print(new_roi_bounds)
# [-5.0, 5.0, -10.0, 10.0, -15.0, 15.0]
</code></pre>

---

## Post #3 by @masadcv (2021-09-27 15:55 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<pre><code class="lang-auto">new_roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
new_roi.SetRadiusXYZ(5,10,15)
new_roi_bounds = [0]*6
new_roi.GetBounds(new_roi_bounds)
print(new_roi_bounds)
# [-5.0, 5.0, -10.0, 10.0, -15.0, 15.0]
</code></pre>
</blockquote>
</aside>
<p>This works only in latest preview build (4.13). In stable release (4.11) it gives the following output:</p>
<pre><code class="lang-auto">new_roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
new_roi.SetRadiusXYZ(5,10,15)
new_roi_bounds = [0]*6
new_roi.GetBounds(new_roi_bounds)
print(new_roi_bounds)
# [0, 0, 0, 0, 0, 0]
</code></pre>
<p>Any ideas how I can support both versions?</p>

---

## Post #4 by @jamesobutler (2021-09-27 16:22 UTC)

<p>An option when there aren’t many differences is to do something like the following:</p>
<pre data-code-wrap="python"><code class="lang-python">if slicer.app.majorVersion &gt;= 5 or (slicer.app.majorVersion == 4 and slicer.app.minorVersion &gt;= 13):
  # do code for Slicer 4.13 preview and later
  new_roi.GetBounds(new_roi_bounds)  # or new_roi.GetBoundsROI(new_roi_bounds)
  print(new_roi_bounds)
  # [-5.0, 5.0, -10.0, 10.0, -15.0, 15.0]
else:
  # do code for Slicer 4.11.20210226 and older
  new_roi.GetBoundsROI(new_roi_bounds)
  print(new_roi_bounds)
  # [-5.0, 5.0, -10.0, 10.0, -15.0, 15.0]
</code></pre>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> May be able to tell what is the preferred method for getting bounds for this object. Either <code>GetBounds</code> or <code>GetBoundsROI</code>.</p>
<p>Another option is this could be accomplished by setting up different branches with support for each version as indicated below.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-index" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-index</a></p>
<blockquote>
<p>Extension developers have to make sure that the extension description in each branch of the Extensions index is compatible with the corresponding Slicer version. Extension developers often create the same branches ( <code>master</code> , <code>4.11</code> , <code>4.13</code> , …) in their repository and they specify this branch name in the extensions descriptor file.</p>
</blockquote>

---

## Post #5 by @Sunderlandkyl (2021-09-27 17:51 UTC)

<p>Because the new Markups ROI can be rotated freely, using a normal bounds with 6 values doesn’t always work. GetBounds()/GetRASBounds() returns the axis-aligned bounds, so it will be correct if the ROI is axis-aligned. In the image below, the magenta cube will be the bounds that are returned by GetBounds() if the ROI is rotated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a9d16bcc446b40ee95cc05f7005e4c05d98266c.png" data-download-href="/uploads/short-url/3NqYtIdRA4GnQgXFeb0Jhsofgg4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a9d16bcc446b40ee95cc05f7005e4c05d98266c.png" alt="image" data-base62-sha1="3NqYtIdRA4GnQgXFeb0Jhsofgg4" width="480" height="500" data-dominant-color="9D8AB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">513×534 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The way to get the OBB in any orientation would be to use the GetPlanes()/GetPlanesWorld() functions, which return the planes for the 6 faces of the ROI.</p>
<p>If you are checking whether or not a point is in the ROI, also consider the IsPointInROI()/IsPointInROIWorld() functions.</p>
<p>GetBoundsROI() returns the bounds in the axis-aligned ROI coordinate system, with the center of the ROI at (0,0,0). It is mostly used internally, and should probably be made into a protected function.</p>

---

## Post #6 by @lassoan (2021-09-27 19:52 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="5" data-topic="19852">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>GetBoundsROI() returns the bounds in the axis-aligned ROI coordinate system, with the center of the ROI at (0,0,0). It is mostly used internally, and should probably be made into a protected function.</p>
</blockquote>
</aside>
<p>Yes, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> please make it protected to make the API simpler (we can later re-add, if we find that it is needed). Also add your explanation to the ROI node API documentation (developers may not think about the impact of that the ROI can be rotated).</p>

---

## Post #7 by @Sunderlandkyl (2021-09-27 21:20 UTC)

<p>I’ve made a PR to remove the function here: <a href="https://github.com/Slicer/Slicer/pull/5905" class="inline-onebox" rel="noopener nofollow ugc">ENH: Remove vtkMRMLMarkupsROINode::GetBoundsROI() and add documentation by Sunderlandkyl · Pull Request #5905 · Slicer/Slicer · GitHub</a>.</p>

---
