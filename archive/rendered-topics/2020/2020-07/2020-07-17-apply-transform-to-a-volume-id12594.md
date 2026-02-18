# Apply transform to a volume

**Topic ID**: 12594
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/apply-transform-to-a-volume/12594

---

## Post #1 by @Stweie (2020-07-17 12:33 UTC)

<p>I used python script to use the landmark registration plugin and applied a custom transformation matrix like following:<br>
transformed_node = slicer.util.getNode(“Transform”)<br>
transformed_node.SetMatrixTransformToParent(reg_mat)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b5c849f59b387fe2944ae35fb9aef14681054fc.png" data-download-href="/uploads/short-url/fjLj7kNErnEr67dVZT3NdW7Vfn6.png?dl=1" title="seg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_690x304.png" alt="seg" data-base62-sha1="fjLj7kNErnEr67dVZT3NdW7Vfn6" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_1380x608.png 2x" data-dominant-color="848381"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">seg</span><span class="informations">1643×726 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now as denoted in the picture, the transformation works perfectly on the red circled area. However, I want to also apply in green cirlced area. Which is the “Moving” volume. How can I achieve that?<br>
I can grab all the volume node by using</p>
<pre><code> for sliceViewName in layoutManager.sliceViewNames():
...   view = layoutManager.sliceWidget(sliceViewName).sliceView()
...   sliceNode = view.mrmlSliceNode()
...   sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
...   compositeNode = sliceLogic.GetSliceCompositeNode()
...   print('Slice view ' + str(sliceViewName))
...   print('  Name: ' + sliceNode.GetName())
...   print('  ID: ' + sliceNode.GetID())
</code></pre>
<p>When I try to apply a tranform matrix on one of nodes in the green area, I got bellow error:<br>
<code>AttributeError: 'MRMLCorePython.vtkMRMLSliceNode' object has no attribute 'SetMatrixTransformToParent'</code><br>
So, My question is how I can apply then change in the green area, which is seen in the read area using the same transformation matrix?</p>

---

## Post #2 by @lassoan (2020-07-17 16:16 UTC)

<p>You need to apply transform to a volume, not to the slice node (vtkMRMLSliceNode). If the transform is applied to the volume, then it is used in all views. Probably what you actually mean is that you would like to see the transformed moving image in the second row (instead of the original moving image). See slice viewer documentation for instructions for setting background/foreground volume: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view</a></p>

---

## Post #3 by @Stweie (2020-07-18 17:57 UTC)

<p>You are correct. I want to see the transformed moving image in the second row instead of showing the original moving image.  But using python script /command line.   How can I trigger that ? Can you provide any example script or command line ?</p>
<p>Thanks : )</p>

---

## Post #4 by @lassoan (2020-07-18 18:47 UTC)

<p>There are many examples for this in the script repository, for example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images</a></p>

---

## Post #5 by @Stweie (2020-07-20 10:12 UTC)

<p>I looked into the code snippet you shared. And tried to do it like below snippet.</p>
<p><code>tnode = slicer.util.getNode("Transform")</code></p>
<pre><code> for sliceViewName in layoutManager.sliceViewNames():
      compositeNode = layoutManager.sliceWidget(sliceViewName).sliceLogic().GetSliceCompositeNode()
     compositeNode.SetForegroundVolumeID(tnode.GetID())
</code></pre>
<p>But as you said, I need to apply the transform into a volume, not volume node.  So obviously I am getting here wrong output. In the second row I did not get the expected change.</p>
<p>So, How can I get the transformed volume not the volume node and replace the green circled area  with the transformed volume view, shown in red circled area?</p>

---

## Post #6 by @lassoan (2020-07-22 14:07 UTC)

<p><code>compositeNode.SetForegroundVolumeID</code> expects a volume node’s ID as input. You tried to use the transform node’s ID.</p>

---

## Post #7 by @Stweie (2020-07-22 18:50 UTC)

<p>May be I failed to explain.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b5c849f59b387fe2944ae35fb9aef14681054fc.png" data-download-href="/uploads/short-url/fjLj7kNErnEr67dVZT3NdW7Vfn6.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_690x304.png" alt="" data-base62-sha1="fjLj7kNErnEr67dVZT3NdW7Vfn6" role="presentation" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b5c849f59b387fe2944ae35fb9aef14681054fc_2_1380x608.png 2x" data-dominant-color="848381"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1643×726 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The red circled area shows the transformed moving volume overlayed on the fixed volume. In the green circled area I want to show the transformed moving volume instead of original moving volume. That is why I tried to take the transformed volume node ID and replace the view of the green circled volume with the transformed one.</p>

---

## Post #8 by @lassoan (2020-07-23 01:26 UTC)

<p>If you want to show the transformed volume node in the second row then you can call <code>compositeNode.SetForegroundVolumeID(transformedVolumeNode.GetID())</code> for the slice views of the second row (where <code>transformedVolumeNode</code> is the transformed moving volume node).</p>

---

## Post #9 by @Stweie (2020-07-28 09:23 UTC)

<p>Hi Andras,<br>
Although, the view change works, in case I set a new landmark on the overlayed volume, it does not show the default ‘yellow colored’ landmark ID ( L0, L1 …etc). Is it because of the overlay ? Or there is other way to make the landmark visible on the overlayed volume ?</p>

---

## Post #10 by @lassoan (2020-07-28 19:30 UTC)

<p>Each landmark (markups fiducial) list node is set up to be shown in certain views. You can add all the view node IDs where you want the landmarks to appear in the landmark node’s display node (or remove all the view node IDs from the landmark node’s display node - then the landmark node is displayed in all views).</p>

---
