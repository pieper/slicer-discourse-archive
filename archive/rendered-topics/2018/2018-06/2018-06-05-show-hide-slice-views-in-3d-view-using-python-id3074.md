# Show/hide slice views in 3D view using Python

**Topic ID**: 3074
**Date**: 2018-06-05
**URL**: https://discourse.slicer.org/t/show-hide-slice-views-in-3d-view-using-python/3074

---

## Post #1 by @ollih10 (2018-06-05 08:23 UTC)

<p>Hi developers,</p>
<p>I have a problem switching on the slice views on or off in the 3D view from Python permanently. The code I am using for i.e. switch on the red slice view is:</p>
<p>current_slice_node = slicer.mrmlScene.GetNodeByID(‘vtkMRMLModelDisplayNode1’)<br>
current_slice_node.VisibilityOn()</p>
<p>This code works well until one changes the position of the slice by i.e. scrolling in the slice view. I guess since the “eye” in the slice view is still “closed” the update will set the visibility again to 0 and the slice disappears. How can I prevent this from happening? Is there a way to directly manipulate the slice view by i.e. usig the modules logic to switch on slice rendering in 3D?</p>
<p>Slicer version is 4.8.1</p>

---

## Post #2 by @pieper (2018-06-05 12:28 UTC)

<p>Right - the slice models are controlled at a higher level and so the visibility and transform are controlled by the SliceNode, which is what is tied to the eye icon in the slice controller.</p>
<pre><code class="lang-auto">red = getNode('vtkMRMLSliceNodeRed')
red.SetSliceVisible(1)
</code></pre>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @ollih10 (2018-06-06 08:40 UTC)

<p>Thanks Steve. That was exactly what I was looking for.</p>

---

## Post #4 by @park (2022-02-09 02:00 UTC)

<p>Hi Steve</p>
<p>Is there any way to popup the 2D slice only one 3D view (e.g., view1) when using the multiple 3D views ?</p>

---

## Post #5 by @pieper (2022-02-09 15:46 UTC)

<p>Yes, you can set the ViewNodeIDs for the display node associated the with slice model.  Similar to what’s done in this snippet:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties</a></p>

---

## Post #6 by @park (2022-02-10 10:46 UTC)

<p>Thank you for your reply</p>
<p>I tried this code</p>
<pre><code class="lang-auto">red = getNode('vtkMRMLSliceNodeRed')
red. pointListDisplayNode.SetViewNodeIDs(["vtkMRMLViewNode2"]) 
red.SetSliceVisible(1)
</code></pre>
<p>But this one is not work</p>
<p><code>red. pointListDisplayNode.SetViewNodeIDs(["vtkMRMLViewNode2"])</code></p>
<ul>
<li>One more , I would like to remove 2D slices on View2 like this figure</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png" data-download-href="/uploads/short-url/uJvzFGF3cEe3GsQpEyMjaQ1G1M5.png?dl=1" title="sdsd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9_2_556x500.png" alt="sdsd" data-base62-sha1="uJvzFGF3cEe3GsQpEyMjaQ1G1M5" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7662e0774a0a59ba18021d13493e4ceb0aec5e9.png 2x" data-dominant-color="5A5668"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sdsd</span><span class="informations">823×739 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #7 by @pieper (2022-02-10 12:59 UTC)

<p>I don’t have an example that does exactly what you ask, maybe someone has time to write one for you.  If not, you need to study the code to see what the <code>SetViewNodeIDs</code> on a display node and figure out how to set that parameter on the model display nodes for the slices.  It’s not trivial but it can be done.</p>

---

## Post #8 by @park (2022-02-10 16:43 UTC)

<p>I solve this</p>
<p>It should use ‘vtkMRMLModelDisplayNode’ rather than ‘vtkMRMLSliceNode’</p>
<pre><code class="lang-auto">current_slice_node = slicer.mrmlScene.GetNodeByID('vtkMRMLModelDisplayNode1')
current_slice_node.SetViewNodeIDs([slicer.mrmlScene.GetFirstNodeByName("View1").GetID()])
current_slice_node.VisibilityOn()
</code></pre>
<p>Thank you</p>

---

## Post #9 by @mikebind (2022-02-10 17:07 UTC)

<p>As long as you know the ID of the model for the slice display, I think your approach will work.  However, here is how you would do it through the slice node:</p>
<pre><code class="lang-auto">greenSliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeGreen')
greenSliceNode.SetSliceVisible(True) # this will show the slice in all 3D views by default
greenSliceNode.AddThreeDViewID('vtkMRMLViewNode2') # This will show the slice in only View2
greenSliceNode.AddThreeDViewID('vtkMRMLViewNode1') # This will make the slice visible in View1 as well
greenSliceNode.RemoveThreeDViewID('vtkMRMLViewNode2') # This will make the slice no longer visible in View2
</code></pre>
<p>The logic here is that the slice is visible only in any 3D view which has been explicitly added to the list of 3D view IDs for that slice node, with the exception that, if no view IDs have been added, then the default behavior is for the slice to be visible in all 3D views.  If you don’t want the slice visible in 3D at all, then you use <code>SetSliceVisible(False)</code>.  This is very similar to the way <code>SetViewNodeIDs()</code> works on regular display nodes: if no view nodes are set, then the default is visible everywhere, but if any have been set explicitly, then the node is only visible in views on that list.</p>

---

## Post #10 by @pieper (2022-02-10 17:09 UTC)

<p>Glad you were able to figure this out <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <a class="mention" href="/u/park">@park</a>.   And thanks <a class="mention" href="/u/mikebind">@mikebind</a> for the extra details.</p>

---
