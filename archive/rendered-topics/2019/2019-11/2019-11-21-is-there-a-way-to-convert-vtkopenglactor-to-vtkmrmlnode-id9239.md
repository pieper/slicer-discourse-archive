---
topic_id: 9239
title: "Is There A Way To Convert Vtkopenglactor To Vtkmrmlnode"
date: 2019-11-21
url: https://discourse.slicer.org/t/9239
---

# Is there a way to convert vtkOpenGLActor to vtkMrmlNode?

**Topic ID**: 9239
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-convert-vtkopenglactor-to-vtkmrmlnode/9239

---

## Post #1 by @JaceYang (2019-11-21 06:40 UTC)

<pre><code>I want to use the mouse to pick 3D object in the 3D view.So I use the vtkPropPicker and get a vtkOpenGLActor.Then I can modify the property(like color) of this vtkActor.
But when I convert this vtkActor to vtkMRMLNode using SafeDownCast,the program crashes.
The father class of vtkActor and vtkMRMLNode are both vtkObject.Is there a way to convert vtkOpenGLActor to vtkMRMLNode?
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/844b8d2aaa05e97c1c87777e02686023d5ea4257.png" data-download-href="/uploads/short-url/iSkTrFRlnHUh2WgzcDetVZamXqf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/844b8d2aaa05e97c1c87777e02686023d5ea4257_2_690x450.png" alt="image" data-base62-sha1="iSkTrFRlnHUh2WgzcDetVZamXqf" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/844b8d2aaa05e97c1c87777e02686023d5ea4257_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/844b8d2aaa05e97c1c87777e02686023d5ea4257_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/844b8d2aaa05e97c1c87777e02686023d5ea4257_2_1380x900.png 2x" data-dominant-color="EFF2F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1888×1234 415 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/445c1485fddefea5cbdb382df1cdd68440dfe46a.png" data-download-href="/uploads/short-url/9KJKqytNtZXyeZAPE5MsgcLIRzc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/445c1485fddefea5cbdb382df1cdd68440dfe46a_2_690x489.png" alt="image" data-base62-sha1="9KJKqytNtZXyeZAPE5MsgcLIRzc" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/445c1485fddefea5cbdb382df1cdd68440dfe46a_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/445c1485fddefea5cbdb382df1cdd68440dfe46a_2_1035x733.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/445c1485fddefea5cbdb382df1cdd68440dfe46a_2_1380x978.png 2x" data-dominant-color="A2A3A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1904×1350 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The properties of the vtkOpenGLActor can be modified. But the properties of the segments are not changed with the vtkOpenGLActor.So how to build the connection between the vtkOpenGLActor and the vtkMRMLSegmentationNode?</p>

---

## Post #2 by @lassoan (2019-11-21 13:26 UTC)

<p><code>vtkMRMLNode</code> is not a <code>vtkActor</code>, so downcasting will not work. Instead, you can use the model <a href="https://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#adfed38f8e4568690d0856dc8a6a7d12a">displayable manager’s GetIDByActor method</a> to get model display node from a VTK actor (you can get access to the model displayable manager as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_displayable_manager_of_a_certain_type_for_a_certain_view">here</a>).</p>
<p>Note that the model displayable manager already has a <a href="https://apidocs.slicer.org/master/classvtkMRMLModelDisplayableManager.html#a29878f62c281afc9431cc9474f85533b">picker</a> that you can use and get the ID of the picked display node directly.</p>

---

## Post #4 by @JaceYang (2019-11-22 09:06 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df89eb5f818fa9c57d74ad4aed352dccfd9f74c6.png" alt="image" data-base62-sha1="vTvXWPytDr5dOacOYeMaNHIdYj4" width="468" height="257"><br>
when I click this,the function qSlicerSegmentationsModuleWidget::onSegmentSelectionChanged is called.</p>
<p>when I click in 3D view the function vtkThreeDViewInteractorStyle::OnLeftButtonDown() is called.<br>
Is there a way when I click in 3D view the function  qSlicerSegmentationsModuleWidget::onSegmentSelectionChanged will be called?</p>

---

## Post #5 by @JaceYang (2019-11-22 09:07 UTC)

<p>thank you very much!</p>

---

## Post #6 by @lassoan (2019-11-22 14:18 UTC)

<p>You can use the segment editor widget’s setCurrentSegmentID method to select a segment as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">examples in script repository</a> (e.g., “mask a volume with segments and compute histogram for each region”). You can get picked segment ID from vtkMRMLSegmentationsDisplayableManager3D.</p>

---

## Post #7 by @JaceYang (2019-11-29 01:45 UTC)

<p>Actually we want a function that when I click in the 3D render view, the segment I click will be selected.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f476e3f417daa6fbebd3e5ffbde73a6e2ddd0aa.png" data-download-href="/uploads/short-url/i9XG33xt3o6SG7jLBmgO5C0mK4G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f476e3f417daa6fbebd3e5ffbde73a6e2ddd0aa_2_690x332.png" alt="image" data-base62-sha1="i9XG33xt3o6SG7jLBmgO5C0mK4G" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f476e3f417daa6fbebd3e5ffbde73a6e2ddd0aa_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f476e3f417daa6fbebd3e5ffbde73a6e2ddd0aa_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f476e3f417daa6fbebd3e5ffbde73a6e2ddd0aa_2_1380x664.png 2x" data-dominant-color="BEC0BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1577×759 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
