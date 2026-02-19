---
topic_id: 11322
title: "Display Two 2D Images Simultaneously"
date: 2020-04-27
url: https://discourse.slicer.org/t/11322
---

# Display two 2D images simultaneously

**Topic ID**: 11322
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/display-two-2d-images-simultaneously/11322

---

## Post #1 by @rohan_n (2020-04-27 23:46 UTC)

<p>Hello,<br>
I would like to display two 2D images at the same time in the Slicer window. For example, show image1 in the red slice and image2 in the yellow slice.<br>
What would be the syntax of the code that would allow me to do this from a scripted module?<br>
Thanks,<br>
Rohan</p>

---

## Post #2 by @jamesobutler (2020-04-28 01:14 UTC)

<p>There are some great examples here in the Slicer script repository for this use case <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_volume_in_slice_views" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_volume_in_slice_views</a></p>

---

## Post #3 by @rohan_n (2020-04-28 21:55 UTC)

<p>Thank you James.<br>
I’m trying this out with an example numpy array because I will have to start out with numpy array. Unfortunately, I’m still confused about how to go from this part:</p>
<pre><code>img = np.zeros((50,50))
img[10:40,20:30] = 1
imgvect = img.ravel()
vtk_data_array = numpy_support.numpy_to_vtk(num_array=imgvect, array_type=vtk.VTK_FLOAT)
img_vtk = vtk.vtkImageData()
img_vtk.SetDimensions(img.shape[0],img.shape[1],1)
inputVolume.SetAndObserveImageData(img_vtk)
</code></pre>
<p>to this part:</p>
<pre><code>slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(n.getID())
</code></pre>
<p>I’m not sure what I put in place of n.getID() or what data type conversions are needed.<br>
Thanks,<br>
Rohan</p>

---

## Post #4 by @jamesobutler (2020-04-28 22:28 UTC)

<p>Using your numpy array you can update a volume node with that array using <code>updateVolumeFromArray</code> which can be found at <a href="https://github.com/Slicer/Slicer/blob/bd90449b32d23551133d954824f629e79aab0989/Base/Python/slicer/util.py#L1288-L1294" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/bd90449b32d23551133d954824f629e79aab0989/Base/Python/slicer/util.py#L1288-L1294</a></p>
<pre><code class="lang-python">new_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
slicer.util.updateVolumeFromArray(new_volume_node, my_numpy_array)
slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(new_volume_node.GetID())  # setvolume node as the foreground volume of the Red slice widget.
</code></pre>

---

## Post #5 by @rohan_n (2020-04-28 23:00 UTC)

<p>Thanks again, the 3 lines of code above solved my problem.</p>

---

## Post #6 by @rohan_n (2020-05-19 23:14 UTC)

<p>Hi,<br>
I have another follow-up about this.<br>
This method of displaying different images in red and yellow slices doesn’t seem to work if I’ve already done something like this earlier:</p>
<pre><code class="lang-auto">slicer.util.setSliceViewerLayers(background=self.inputSelector.currentNodeID)
</code></pre>
<p>In this case, self.inputSelector.currentNodeID remains in view even after I’ve done this:</p>
<pre><code class="lang-auto">slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(n.getID())
</code></pre>
<p>How do I get around this issue?</p>

---

## Post #7 by @lassoan (2020-05-19 23:35 UTC)

<p><code>slicer.util.setSliceViewerLayers</code> only changes views that are currently displayed. It is a convenience method only, so if you need a different behavior then you can go one level lower (accessing view widgets, as you do it in your second example). Also note that there is a difference between setting foreground and background volumes.</p>

---
