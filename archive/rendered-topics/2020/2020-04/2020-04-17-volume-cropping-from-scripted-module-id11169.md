---
topic_id: 11169
title: "Volume Cropping From Scripted Module"
date: 2020-04-17
url: https://discourse.slicer.org/t/11169
---

# Volume Cropping from Scripted Module

**Topic ID**: 11169
**Date**: 2020-04-17
**URL**: https://discourse.slicer.org/t/volume-cropping-from-scripted-module/11169

---

## Post #1 by @rohan_n (2020-04-17 23:21 UTC)

<p>Hello,</p>
<p>I am using Slicer 4.11.0 on a Windows 10 computer and developing a Python scripted module.</p>
<p>I want to call a function from my scripted module that will allow the user to select a 3D region of interest, then once the user selects this region, I want to return to the processing steps in my scripted module and use the voxel coordinates of the user selected region.</p>
<p>Unfortunately, I don’t know the syntax for calling Slicer’s CropVolume module from my scripted module, and I don’t know any other methods in Python for creating a GUI that looks similar to the CropVolume module.</p>
<p>Any help would be greatly appreciated. If I can create a GUI that looks similar to the CropVolume module but takes a 3D numpy array as an input, that would be the preferred method. Otherwise, using CropVolume module would be fine.</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #3 by @lassoan (2020-04-17 23:35 UTC)

<p>You can find examples of creating and manipulating Annotation ROI node from Python in this old module: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/e7f07bb303e26fde0a010cc528bf36b4759b963c/PlusRemote/PlusRemote.py">https://github.com/SlicerIGT/SlicerIGT/blob/e7f07bb303e26fde0a010cc528bf36b4759b963c/PlusRemote/PlusRemote.py</a></p>
<p>You can use crop volume module via <a href="http://apidocs.slicer.org/master/classvtkSlicerCropVolumeLogic.html">Crop Volume module logic</a>. You can access module logic by calling</p>
<pre><code>cropVolumeLogic = slicer.modules.cropvolume.logic()</code></pre>

---

## Post #4 by @fedorov (2020-04-18 01:58 UTC)

<p>A more recent example is SliceTracker, which is using this function from SlicerDevelopmentToolbox: <a href="https://github.com/QIICR/SlicerDevelopmentToolbox/blob/master/SlicerDevelopmentToolboxUtils/mixins.py#L614-L623">https://github.com/QIICR/SlicerDevelopmentToolbox/blob/master/SlicerDevelopmentToolboxUtils/mixins.py#L614-L623</a>.</p>

---

## Post #5 by @rohan_n (2020-04-20 19:18 UTC)

<p>Thank you both for the help! I’ll look through this code and reply here if I have follow-up questions.</p>

---

## Post #6 by @rohan_n (2020-04-21 20:26 UTC)

<p>Hello,<br>
After looking through these links, I’m aware that you input roi into CropVolume module like this</p>
<pre><code>cropVolumeParameterNode.SetROINodeID(roi.GetID())
</code></pre>
<p>But unfortunately I’m still not sure how to allow the user to interactively define roi through a GUI that displays the input volume. Are there any simple examples that go through this?<br>
Or maybe you could tell me which lines of code in the links you already shared do this part?</p>
<p>Thanks again,<br>
Rohan Nadkarni</p>

---

## Post #7 by @fedorov (2020-04-21 20:42 UTC)

<p>Rohan, if I were you, I would simply create an ROI widget automatically:</p>
<pre><code class="lang-python">r=slicer.vtkMRMLAnnotationROINode()
slicer.mrmlScene.AddNode(r)
</code></pre>
<p>you can initialize its position based on the geometry of the volume you need to crop. Then once the user is done positioning and adjusting the ROI, they could click a button, and you would call CropVolume logic passing the ROI and input volume. I don’t think you need any additional GUI to do that - ROI visualization and resizing is handled by Slicer, it’s a core widget.</p>
<p>Does this make sense?</p>

---

## Post #8 by @rohan_n (2020-04-21 22:20 UTC)

<p>Thanks Andrey! I’ll  probably be able to figure out the button part on my own.<br>
Other than that, I now know how to implement everything I need for ROI selection from scripted module.</p>

---
