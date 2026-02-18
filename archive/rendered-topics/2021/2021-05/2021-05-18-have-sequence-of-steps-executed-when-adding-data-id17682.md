# Have sequence of steps executed when adding data

**Topic ID**: 17682
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/have-sequence-of-steps-executed-when-adding-data/17682

---

## Post #1 by @Jonathan_Lesage (2021-05-18 19:54 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Reformatting views in .sliccerrc file remains active when adding a volume<br>
Actual behavior: Views reset to Axial, Sagittal, Coronal when adding data</p>
<p>Hi there,</p>
<p>In previous slicer versions I had some reformatting of the slicer views triggered upon opening slicer with .sliccerrc.py file that persisted when adding data. Now I notice that the views are still reformatted when I open slicer but when I add a new volume the views are reset (axial, sagittal, coronal). Is there a way to make the reformatting persist when loading data or alternatively have some python code run everytime a new volume is added?</p>
<p>Many thanks!</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #2 by @lassoan (2021-05-19 03:38 UTC)

<aside class="quote no-group" data-username="Jonathan_Lesage" data-post="1" data-topic="17682">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan_lesage/48/4693_2.png" class="avatar"> Jonathan_Lesage:</div>
<blockquote>
<p>have some python code run everytime a new volume is added?</p>
</blockquote>
</aside>
<p>See an example for this in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">script repository</a>.</p>
<aside class="quote no-group" data-username="Jonathan_Lesage" data-post="1" data-topic="17682">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan_lesage/48/4693_2.png" class="avatar"> Jonathan_Lesage:</div>
<blockquote>
<p>In previous slicer versions I had some reformatting of the slicer views triggered upon opening slicer with .sliccerrc.py file that persisted when adding data.</p>
</blockquote>
</aside>
<p>In Slicer Preview Releases you probably don’t need to use manual reformatting. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">enable “Reset field of view on show” and “Reset view orientation on show” options</a> in to automatically align slice views whenever a volume gets shown.</p>

---

## Post #3 by @Jonathan_Lesage (2021-05-31 18:43 UTC)

<p>Hi Andras,</p>
<p>Thank you, that works well, however it seems like the view will reset every time I apply a filter, attempt to compare volumes etc.</p>
<p>Fundamentally, I have a volume where IJK (X,Y,Z) is aligned with the RAS axes but the typically way to show the slice views in my industry is R(X) pointing to the right and A(Y) pointing downwards on the Axial slice, S(Z) pointing to the right and R(X) pointing upwards on the Sagital slice and S(Z) pointing right and A(Y) pointing down for the Coronal slice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1498c8e8446729500b5151af947874e29cc242a.jpeg" data-download-href="/uploads/short-url/rzTJfLH773HQxVCDrc7f1V8bxIS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1498c8e8446729500b5151af947874e29cc242a_2_690x421.jpeg" alt="image" data-base62-sha1="rzTJfLH773HQxVCDrc7f1V8bxIS" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1498c8e8446729500b5151af947874e29cc242a_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1498c8e8446729500b5151af947874e29cc242a_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1498c8e8446729500b5151af947874e29cc242a_2_1380x842.jpeg 2x" data-dominant-color="6C6C6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1530×934 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can do this with the following code at the beginning of my .slicerrc.py file using the reformatting widget, however, a way to do this which takes effect all of the time would be preferred. Is there a way to save the data differently or by default change the way the slice views are oriented? If I could get this working it would greatly simplify my life! I want to use Slicer for all of my nondestructive testing scan analysis but having these views constantly change into something unfamiliar makes it hard for me to present things to my colleagues.</p>
<pre><code class="lang-python">slicer.util.resetSliceViews()
viewNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
for viewNode in viewNodes:
  viewNode.SetSliceIntersectionVisibility(1)
displayNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLScalarVolumeDisplayNode')
NDTColor = slicer.util.getFirstNodeByName('NDT')
# displayNode.SetAndObserveColorNodeID('vtkMRMLColorTableNodeNDT')
displayNode.SetAndObserveColorNodeID(NDTColor.GetID())
displayNode.ScalarVisibilityOff()
slicer.mrmlScene.AddDefaultNode(displayNode)
slicer.util.selectModule('Reformat')
# Select Red slice
widget = slicer.modules.reformat.widgetRepresentation()
sliceNodeSelector = slicer.util.findChildren(widget, "SliceNodeSelector")[0]
sliceNodeSelector.setCurrentNodeID("vtkMRMLSliceNodeRed")
isslider = slicer.util.findChildren(widget, "ISSlider")[0]
isslider.value = 180
sliceNodeSelector.setCurrentNodeID("vtkMRMLSliceNodeGreen")
isslider = slicer.util.findChildren(widget, "ISSlider")[0]
isslider.value = -90
#
sliceNodeSelector.setCurrentNodeID("vtkMRMLSliceNodeYellow")
isslider = slicer.util.findChildren(widget, "ISSlider")[0]
isslider.value = 0
sliceNodeSelector.setCurrentNodeID("vtkMRMLSliceNodeYellow")
isslider = slicer.util.findChildren(widget, "LRSlider")[0]
isslider.value = 180
</code></pre>

---

## Post #4 by @lassoan (2021-05-31 19:31 UTC)

<aside class="quote no-group" data-username="Jonathan_Lesage" data-post="3" data-topic="17682">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan_lesage/48/4693_2.png" class="avatar"> Jonathan_Lesage:</div>
<blockquote>
<p>Thank you, that works well, however it seems like the view will reset every time I apply a filter, attempt to compare volumes etc.</p>
</blockquote>
</aside>
<p>This is a feature not a bug, because you can turn it off. If you run the CLI from Python then specify <code>update_display=False</code> (see details <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.cli.runSync">here</a>).</p>
<aside class="quote no-group" data-username="Jonathan_Lesage" data-post="3" data-topic="17682">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jonathan_lesage/48/4693_2.png" class="avatar"> Jonathan_Lesage:</div>
<blockquote>
<p>Fundamentally, I have a volume where IJK (X,Y,Z) is aligned with the RAS axes but the typically way to show the slice views in my industry is R(X) pointing to the right and A(Y) pointing downwards on the Axial slice, S(Z) pointing to the right and R(X) pointing upwards on the Sagital slice and S(Z) pointing right and A(Y) pointing down for the Coronal slice</p>
</blockquote>
</aside>
<p>Names and directions of slice view axes are completely customizable. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-slice-view-orientation">this example</a>.</p>

---

## Post #5 by @Jonathan_Lesage (2021-07-17 17:35 UTC)

<p>Hi Andras,</p>
<p>Thank you for the tip! This seems to be exactly what I need, however, I am having trouble determining how to set the elements so that the views are as I would like. What do the entries in the matrices correspond to? Is there some documentation on this. It is somewhat difficult to get a general idea of what is happening from the script example, although that is still quite useful!</p>
<p>Any further assistance would be greatly appreciated!</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #6 by @lassoan (2021-07-17 18:49 UTC)

<p>SliceToRAS transform is homogeneous linear transformation from Slice coordinate system to RAS coordinate system. You can look up homogeneous coordinate transforms on Wikipedia for details, but in short, the first column of the matrix specifies the direction of the x axis of the Slice coordinate system in the RAS coordinate system (y is the second column, z is the third column), and the fourth column specifies the Slice coordinate system origin in the RAS coordinate system.</p>
<p>Slice coordinate system origin is in the center and x direction = screen right, y direction = screen up, z = orthogonal to the screen (can point towards or away from the viewer, depending what is the preferred scrolling direction).</p>
<p>RAS coordinate system axis directions are x = patient right, y = patient anterior, s = patient superior.</p>
<p>You can find more examples and explanation in SlicerIGT tutorials and PerkLab Bootcamp training materials. These are all standard computer graphics concepts, so you should be able to find many other tutorials about it on the web (homogeneous coordinate systems and transforms).</p>

---

## Post #7 by @Jonathan_Lesage (2021-07-18 02:52 UTC)

<p>Hi Andras,</p>
<p>I finally have the slice views configured properly for my application. Thank you so much!</p>
<ul>
<li>Jon</li>
</ul>

---
