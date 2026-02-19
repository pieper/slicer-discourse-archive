---
topic_id: 18793
title: "How To Get A Roi To Fit Volume In The Volume Rendering Modul"
date: 2021-07-19
url: https://discourse.slicer.org/t/18793
---

# How to get a ROI to fit volume in the Volume Rendering module with python?

**Topic ID**: 18793
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/how-to-get-a-roi-to-fit-volume-in-the-volume-rendering-module-with-python/18793

---

## Post #1 by @jumbojing (2021-07-19 00:06 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a><br>
How to get a ROI to fit volume in the Volume Rendering module with python?</p>

---

## Post #2 by @jumbojing (2021-07-19 00:08 UTC)

<p>Or how to get the center of a volume with python?</p>

---

## Post #3 by @Juicy (2021-07-19 00:50 UTC)

<p>I have recently used the crop volume module in python in order to fit an ROI to a volume:</p>
<pre><code class="lang-auto"># Get the first volume in the scene
volumeNode = slicer.util.getNode("vtkMRMLScalarVolumeNode1")
# Create a new ROI
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
# Make new parameter node in order to use the crop volume module programmatically
crop_module = slicer.vtkMRMLCropVolumeParametersNode()
# Add parameter node to the scene
slicer.mrmlScene.AddNode(crop_module)
# Set the volume as the input volume in the crop volume module
crop_module.SetInputVolumeNodeID(volumeNode.GetID())
# Set output volume as the same volume to overwrite original volume (only needed if you actually want to crop the volume)
crop_module.SetOutputVolumeNodeID(volumeNode.GetID())
# Set the input ROI
crop_module.SetROINodeID(roiNode.GetID())
# Use the Fit ROI to Volume function of the crop volume module
slicer.modules.cropvolume.logic().FitROIToInputVolume(crop_module)

</code></pre>

---

## Post #4 by @jumbojing (2021-07-19 00:55 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="3" data-topic="18793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<pre><code class="lang-auto"># Create a new ROI
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
# Make new parameter node in order to use the crop volume module programmatically
crop_module = slicer.vtkMRMLCropVolumeParametersNode()
# Add parameter node to the scene
slicer.mrmlScene.AddNode(crop_module)
# Set the volume as the input volume in the crop volume module
crop_module.SetInputVolumeNodeID(volumeNode.GetID())
# Set output volume as the same volume to overwrite original volume (only needed if you actually want to crop the volume)
crop_module.SetOutputVolumeNodeID(volumeNode.GetID())
# Set the input ROI
crop_module.SetROINodeID(roiNode.GetID())
# Use the Fit ROI to Volume function of the crop volume module
slicer.modules.cropvolume.logic().FitROIToInputVolume(crop_module)
</code></pre>
</blockquote>
</aside>
<p>Great! Thank you very much!</p>

---

## Post #5 by @Panda (2021-07-20 06:24 UTC)

<p><a class="mention" href="/u/juicy">@Juicy</a> I too did the same, however, how did you set the dimensions for the ROI in this code?</p>

---

## Post #6 by @Juicy (2021-07-20 06:31 UTC)

<p>Hi Panda,</p>
<p>The dimensions of the ROI do not need to be entered. The code uses the functionality of the crop volume module to fit an ROI to the same dimensions as the volume. The dimensions depend on which input volume you choose. Do this with the first line of the code. You can type the name of the volume instead of ‘vtkMRMLScalarVolumeNode1’</p>

---

## Post #7 by @jumbojing (2021-07-25 12:14 UTC)

<aside class="quote no-group quote-modified" data-username="jumbojing" data-post="4" data-topic="18793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<aside class="quote no-group quote-modified" data-username="Juicy" data-post="3" data-topic="18793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<pre><code class="lang-auto">&gt; # Create a new ROI
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
# Make new parameter node in order to use the crop volume module programmatically
crop_module = slicer.vtkMRMLCropVolumeParametersNode()
# Add parameter node to the scene
slicer.mrmlScene.AddNode(crop_module)
# Set the volume as the input volume in the crop volume module
crop_module.SetInputVolumeNodeID(volumeNode.GetID())
# Set output volume as the same volume to overwrite original volume (only needed if you actually want to crop the volume)
crop_module.SetOutputVolumeNodeID(volumeNode.GetID())
# Set the input ROI
crop_module.SetROINodeID(roiNode.GetID())
# Use the Fit ROI to Volume function of the crop volume module
slicer.modules.cropvolume.logic().FitROIToInputVolume(crop_module)
&gt; ```
</code></pre>
</blockquote>
</aside>
</blockquote>
</aside>
<pre><code class="lang-auto">roiNode.SetName("ROI")
roiNode.SetXYZ(PP)
roiNode.SetRadiusXYZ(50, 50, 50)
</code></pre>
<p>我是这样定义ROI大小的…</p>

---

## Post #8 by @lassoan (2022-02-24 20:21 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-fit-roi-to-volume-in-pythond/22168">How to fit ROI to volume in Pythond</a></p>

---

## Post #10 by @sabasa (2022-02-24 18:28 UTC)

<p>Hi,</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Actually I want to Fit the ROI to the volume in the “Crop Volume” module. My Dicom file is oriented and I need to have an oriented volume for cropping. I can do it directly in 3D Slicer but I want to automate this process and I want to do it by Jupyter.</p>
<p>The code didn’t work for me. I need to pass my volume as an input of slicer.modules.crop volume.logic().FitROIToInputVolume(crop_module) function but it just accepts cropped volume as an input. Is there any solution to this problem?</p>
<p>I need to have the attached image by Jupyter.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4a8341146271f60cc0fa6c32aef4aaaad120cff.png" alt="Screenshot (10)" data-base62-sha1="wCNeIpCTe0aHlUyG4YGSNawjXb1" width="662" height="330"></p>

---

## Post #11 by @lassoan (2022-02-24 23:36 UTC)

<p>The example above works well, but I’ve added an updated code snippet to the script repository that uses a markup ROI instead of the old annotation ROI: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume</a></p>

---

## Post #12 by @sabasa (2022-02-25 17:01 UTC)

<p>Yes the previous code worked but not in the way I expected.</p>
<p>When I press the “Fit to Volume” in 3D slicer (first attached image), the image I attached in previous post, was shown<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8c1300ab51043f608f4efcd87c1a30901074a42.jpeg" data-download-href="/uploads/short-url/zuAjy8gCNUes8Io2dhAX0vSbWYG.jpeg?dl=1" title="expl2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8c1300ab51043f608f4efcd87c1a30901074a42_2_368x500.jpeg" alt="expl2" data-base62-sha1="zuAjy8gCNUes8Io2dhAX0vSbWYG" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8c1300ab51043f608f4efcd87c1a30901074a42_2_368x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8c1300ab51043f608f4efcd87c1a30901074a42.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8c1300ab51043f608f4efcd87c1a30901074a42.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">expl2</span><span class="informations">476×646 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I run the code, I got not-oriented volume for cropping(second attached image).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff3104dc78548de91a9997db8a9eec3d0d3927b5.png" alt="expl" data-base62-sha1="ApwMdlb73vIb03S59tdZtXITSHb" width="497" height="346"></p>
<p>My question is about having oriented volume in the same orientation of the Dicom(image attached to the previous post).</p>
<p>Is there any other function to use?</p>

---

## Post #13 by @lassoan (2022-02-25 17:39 UTC)

<p>If you want to rotate the ROI to match the volume axis directions then you can add this line to the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume">code snippet</a>:</p>
<pre><code class="lang-python">slicer.modules.cropvolume.logic().SnapROIToVoxelGrid(cropVolumeParameters)
</code></pre>

---

## Post #14 by @sabasa (2022-02-25 18:05 UTC)

<p>It worked. Thank you so much for your help.</p>

---
