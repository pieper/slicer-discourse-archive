# Access AnnotationROINode without knowing the ID

**Topic ID**: 16777
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/access-annotationroinode-without-knowing-the-id/16777

---

## Post #1 by @pll_llq (2021-03-26 13:34 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/vulcan_salute.png?v=12" title=":vulcan_salute:" class="emoji" alt=":vulcan_salute:" loading="lazy" width="20" height="20"></p>
<p>I’m in python and when I create a volume rendering for a scalar volume node using <code>UpdateDisplayNodeFromVolumeNode</code> from <code>modules.volumerendering.logic</code>, the AnnotationROINode is created automatically.</p>
<p>I want to rename the default AnnotationROINode so that when I work with many volumes their ROI nodes are clearly identifiable in the Subject Hierarchy view.</p>
<p>I use this snippet from the docs to create the volume rendering:</p>
<pre data-code-wrap="python"><code class="lang-python">volumeNode = myAwesomeVolumeNode

logic = slicer.modules.volumerendering.logic()

displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())

logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)

freshlyCreatedDefaultAnnotationROINode = ...
</code></pre>
<p>I can see the connection to the AnnotationROI in the Data module if I select the Volume Node.<br>
How do I see this link from python? Is there a way to access the AnnotationROINode without searching for it explicitly by id, name or classname?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1af902a66c52524d3aa697183647dc46bf59c03.png" data-download-href="/uploads/short-url/n4l0VQPCrLGYpInQ5gy9ep90Gsz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af902a66c52524d3aa697183647dc46bf59c03_2_567x500.png" alt="image" data-base62-sha1="n4l0VQPCrLGYpInQ5gy9ep90Gsz" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af902a66c52524d3aa697183647dc46bf59c03_2_567x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1af902a66c52524d3aa697183647dc46bf59c03.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1af902a66c52524d3aa697183647dc46bf59c03.png 2x" data-dominant-color="E8EBEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">846×746 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-03-26 18:05 UTC)

<p>Looks like you can create the ROI yourself and pass it in.  You could create the volume property and ROI with logical names before calling the method.</p>
<p><a href="https://apidocs.slicer.org/master/classvtkSlicerVolumeRenderingLogic.html#a0dd5b03b39e2f70a3edadd7b1c41cbf9" class="onebox" target="_blank" rel="noopener">https://apidocs.slicer.org/master/classvtkSlicerVolumeRenderingLogic.html#a0dd5b03b39e2f70a3edadd7b1c41cbf9</a></p>

---

## Post #3 by @pll_llq (2021-03-26 18:23 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I’ve tried calling the <code>UpdateDisplayNodeFromVolumeNode</code> but it appeared to me that it didn’t change anything in the scene and when I tried to turn on volume rendering from the UI the “AnnotationROI_3” still appeared.<br>
As another similar workaround I’ve used for now is creating, naming and registering the node manually using the code like in the attached snippet. I probably miss attaching the roi to the volume because despite that the volume rendering works as expected I create these nodes manually I can’t see the “link” in the data module widget.</p>
<p>here’s the snippet</p>
<pre><code class="lang-python">myVolume = pNode.GetNodeReference('myVolume')

ROINode = slicer.vtkMRMLAnnotationROINode()
ROINode.SetName('myVolumeAnnotationROI')
ROINode.Initialize(slicer.mrmlScene)
ROINode.SetRadiusXYZ(50, 50, 100)
ROINode.SetInteractiveMode(1)
ROINode.SetDisplayVisibility(1)

volumeRenderingDisplayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(myVolume)
propertyNode = volumeRenderingDisplayNode.GetVolumePropertyNode()

volumeRenderingDisplayNode.SetAndObserveROINodeID(ROINode.GetID())

volumeRenderingDisplayNode.SetCroppingEnabled(1)
volumeRenderingDisplayNode.VisibilityOn()
</code></pre>
<p>I’ve seen that the <code>AnnotationROINode</code> has a <code>.GetVolumeNodeID</code> method that should <a href="http://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#a7334c9c43ffc2d6736bdf1e5d4b58c34" rel="noopener nofollow ugc">“Get/Set for the volume node ID associated with this ROI”</a> but it’s empty by default. Do I need to use the setter here to link the ROI with the volume?</p>

---

## Post #4 by @pieper (2021-03-26 19:32 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="3" data-topic="16777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>Do I need to use the setter here to link the ROI with the volume?</p>
</blockquote>
</aside>
<p>I’m not sure about that, I haven’t tried.</p>
<p>But do you ever add <code>ROINode</code> to the scene?  If not probably <code>ROINode.GetID()</code> returns null.</p>
<p>You might switch to creating the node with <code>slicer.mrmlScene.AddNewNodeByClass</code> so you know it’s in the scene with a valid id.</p>

---

## Post #5 by @pll_llq (2021-03-26 19:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="16777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You might switch to creating the node with <code>slicer.mrmlScene.AddNewNodeByClass</code> so you know it’s in the scene with a valid id.</p>
</blockquote>
</aside>
<p>Thanks, will try this.</p>

---

## Post #6 by @lassoan (2021-05-11 04:57 UTC)

<p>Note that we are phasing out Annotations module. If you are building anything new then you may consider using markups ROI instead of annotations ROI. Markups ROI has a number of important advantages, such as you can rotate it without applying a transform.</p>

---

## Post #7 by @pll_llq (2021-05-11 05:21 UTC)

<p>Yes I remember that you mentioned thin in the call. What’s the timeline for such depreciation and are there isage examples in the script repository?</p>

---

## Post #8 by @lassoan (2021-05-11 05:43 UTC)

<p>Probably we will remove annotations module in a year or so. You can find markups manipulation examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">script repository</a> and we can add more examples as questions are asked.</p>

---

## Post #9 by @pll_llq (2021-05-11 05:49 UTC)

<p>Thanks, will look deeper into it.</p>
<p>By the way, will removal of annotations module break older extensions and custom apps that use it?</p>

---

## Post #10 by @lassoan (2021-05-11 13:42 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="9" data-topic="16777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>By the way, will removal of annotations module break older extensions and custom apps that use it?</p>
</blockquote>
</aside>
<p>Yes, that’s why we remove annotations module slowly, in several phases. We have already stopped developing and fixing Annotations module and stated that the module is deprecated. Next step is to update all core modules and extensions to support markups as well, then change modules to create markups node instead by default, then hide Annotations module GUI, and finally remove the module completely. The last step will probably only happen in a few years when some Slicer changes would require too much work to keep Annotations module working. See current plan in the <a href="https://github.com/Slicer/Slicer/wiki/Roadmap">Roadmap</a>.</p>

---
