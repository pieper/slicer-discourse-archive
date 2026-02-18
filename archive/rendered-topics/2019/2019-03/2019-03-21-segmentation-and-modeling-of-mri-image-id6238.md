# Segmentation and modeling of MRI image

**Topic ID**: 6238
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/segmentation-and-modeling-of-mri-image/6238

---

## Post #1 by @ZiyunLiang (2019-03-21 14:18 UTC)

<p>Hi,</p>
<p>I want to implement the segmentation of bladder from pelvic floor MRI images and then implement 3D reconstruction of the organ in a python scripted module.<br>
I currently created a model which can predict by each pixel of the MRI image. The model returns a  (227,227,30) matrix of value 0 and 1. (the MRI image has 30 images with 227*227 pixels). In the matrix, 1 indicates this pixel is a part of bladder and 0 is not. This model tells the position of the segmented organ in the image.<br>
For the 3D Modeling part, I think the <em>Show 3D</em> and  <em>Fill between slices</em> of the Segment Editor module will do it. But how can I segment the organ by the matrix predicted by my model? Does anyone have any idea how to implement this?</p>
<p>Thanks for your time!<br>
Andrea</p>

---

## Post #2 by @cpinter (2019-03-21 14:26 UTC)

<p>The data you call model we call binary labelmap. Please load is to Slicer as a labelmap (choose labelmap in the options of the load window, or convert it to labelmap after loading in the Volumes module), then import it as a segmentation (right-click labelmap in Data module and choose import labelmap to segmentation).</p>

---

## Post #3 by @ZiyunLiang (2019-03-21 14:49 UTC)

<p>Hi, thanks so much for your help.<br>
Your idea seems practical but I’m sorry I didn’t completely understand. I load MRI images in the format .gz to Slicer, and the model is a .h5 file which is made of a convolutional neural network. My model can predict the MRI images to a (227,227,30) matrix. What should I load to Slicer? I’m new to Slicer so sorry for lack of knowledge.</p>

---

## Post #4 by @lassoan (2019-03-21 15:06 UTC)

<p>Save the “model” (we call it labelmap volume) as a .nrrd or .mha file and you will be able to load it as segmentation or labelmap volume.</p>

---

## Post #5 by @ZiyunLiang (2019-03-21 15:27 UTC)

<p>Hi, thanks for answering.<br>
I’m a little confused. The “model” is a deep convolutional neural network, how can I load it as volume?</p>

---

## Post #6 by @pieper (2019-03-21 15:58 UTC)

<p><a class="mention" href="/u/ziyunliang">@ZiyunLiang</a>, what you call the “matrix” (output of your neural network “model”) is what we call a labelmap, so if you load that into Slicer, you can make it into a what Slicer calls a “model” which is a triangulated surface. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #7 by @cpinter (2019-03-21 16:14 UTC)

<p>That’s right. matrix = labelmap, not model as I said.</p>
<p>You cannot import your model to Slicer, but if it’s python or C++ or Matlab, then you can integrate it within a new module.</p>

---

## Post #8 by @ZiyunLiang (2019-03-22 09:01 UTC)

<p>Hi, really appreciate your help and explanation, I have figured out a way to implement this now. However, I still got a problem when I’m trying to write it in my scripted python module.<br>
When I’m trying to convert my volume to labelmap by using <code>Volumes</code>  module,  <code>Volume information</code>  section, and  <code>Convert to label map</code><br>
I used the code</p>
<blockquote>
<p>volumeNode=slicer.util.getNode(‘vtkMRMLScalarVolumeNode1’)<br>
labelmap=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.Volumes.logic().CreateLabelVolumeFromVolume(vtkMRMLScene,label map,volumeNode)</p>
</blockquote>
<p>But there is something wrong.</p>
<blockquote>
<p>AttributeError: ‘module’ object has no attribute ‘Volumes’</p>
</blockquote>
<p>I don’t have much experience in writing python code in 3d Slicer so please help me out.  What is the correct way of realizing this?</p>
<p>Thanks for your time!</p>

---

## Post #9 by @jamesobutler (2019-03-22 09:22 UTC)

<p>You have the case wrong which is causing the attribute error.</p>
<pre><code class="lang-python">slicer.modules.Volumes.logic().CreateLabelVolumeFromVolume(vtkMRMLScene,label map,volumeNode)
</code></pre>
<p>should be</p>
<pre><code class="lang-python">slicer.modules.volumes.logic().CreateLabelVolumeFromVolume(vtkMRMLScene,label map,volumeNode)
</code></pre>
<p>A tip is also to press {TAB} after any period to see the available options in an auto-complete type of way.</p>

---

## Post #10 by @ZiyunLiang (2019-03-22 09:26 UTC)

<p>Hi, thanks for the quick response and the tip, I’ll keep that in mind. I tried this but I think I’m still implementing this function wrong. What should the vtkMRMLScene be?</p>
<blockquote>
<p>NameError: name ‘vtkMRMLScene’ is not defined</p>
</blockquote>

---

## Post #11 by @jamesobutler (2019-03-22 09:36 UTC)

<p>Yes any variable needs to be defined as well. In this case, vtkMRMLScene wasn’t defined. We can instead use “slicer.mrmlScene” which is defined.</p>
<pre><code class="lang-python">slicer.modules.volumes.logic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelmap, volumeNode)
</code></pre>

---

## Post #12 by @ZiyunLiang (2019-03-22 09:40 UTC)

<p>Hi James,<br>
Thanks so much for your help. It’s working now.<img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #13 by @cpinter (2019-03-22 13:29 UTC)

<p>Instead of this approach, I’d load the volume as labelmap to begin with:</p>
<p><code>slicer.util.loadLabelVolume('d:/path/to/Voulme.nrrd',{})</code></p>

---

## Post #14 by @ZiyunLiang (2019-03-22 13:37 UTC)

<p>This is indeed an easier way to do this. Thanks:smiley:</p>

---
