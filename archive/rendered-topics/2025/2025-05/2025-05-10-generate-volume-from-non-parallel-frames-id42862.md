---
topic_id: 42862
title: "Generate Volume From Non Parallel Frames"
date: 2025-05-10
url: https://discourse.slicer.org/t/42862
---

# Generate volume from non parallel frames. 

**Topic ID**: 42862
**Date**: 2025-05-10
**URL**: https://discourse.slicer.org/t/generate-volume-from-non-parallel-frames/42862

---

## Post #1 by @derradji (2025-05-10 11:00 UTC)

<p>Hi<br>
I’m using an endocavity linear ultrasound. The patient is scanned by rotating the probe on its own axe. So the série is a set of  a non parallel frames.<br>
I get from the device (mindray z60) only one file per series containing the all frames of the sequence.<br>
On 3dslicer, I get a volume with parallel frames in the three axes.<br>
Question how can I retransform  to get the correct volume ( a rectangular frames rotating around the edge of the frames)<br>
Thanks</p>

---

## Post #2 by @lassoan (2025-05-10 11:39 UTC)

<p>Welcome to the Slicer community <a class="mention" href="/u/derradji">@derradji</a> !<br>
The good news is that there are two modules in Slicer that can do this:</p>
<ul>
<li>SlicerIGT extension’s <a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/VolumeReconstruction">Volume Reconstruction</a> module can reconstruct a volume from arbitrarily oriented slices.</li>
<li>SlicerHeart extension’s <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/KretzFileReader">KretzFileReader</a> module can reconstruct a volume from a rotational sweep.</li>
</ul>
<p>Volume reconstructor module is probably simpler to make work on your data, as all you need is to have the image slices in a sequence node, with each slice pose correctly set from the DICOM file. This can be achieved by updating the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/DicomUltrasoundPlugin/DicomUltrasoundPlugin.py">DicomUltrasoundPlugin</a> Python script to recognize your DICOM volume. As a quick test, you can convert the inage stack and add orientation information using <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598/10">this Python script</a>.</p>
<p>KretzFileReader module contains both the DICOM reader and rotational volume reconstructor in one module and it is implemented in C++, so it is a bit more difficult to adapt to your data. However, since it is specifically developed to reconstruct rotational sweeps, it can create output volumes without holes at higher resolution.</p>
<p>If you provide an anonymized image then I can help with the implementation.</p>

---

## Post #3 by @derradji (2025-05-24 18:56 UTC)

<p>Hi there<br>
Sorry for my poor English.<br>
Sorry for my latency. I’m using 3dslicer 4.8.1 because I’m using an aged computer.<br>
I will soon update it.<br>
Thank you for your response. After some tries. I was able to re export the volume in a new série as multiple parallel frames.<br>
That is not what I want really.<br>
Thé probe when rotating around it’s axis is creating a series of frames (I get one file with extension *.Dcm containing the all frames). On 3d slicer I get always a cube or parraleleped volume and not a cylindric volume.<br>
I don’t know if I’m explaining right my idea.<br>
I need to transform the file dcm into a new one correctly reformatted to get in final a cylindric volume.</p>

---

## Post #4 by @lassoan (2025-06-02 01:04 UTC)

<p>The image frames are loaded as a stack that appear as a rectangular block if you render them as a volume. You’ll get the cylindrical volume when you follow the steps I described in my answer above.</p>

---

## Post #5 by @derradji (2025-07-13 16:31 UTC)

<p>now i’m using 3dslicer 5.8.1<br>
i upload an anonymised dicom file which contain one serie of 134 frames taken with the probe by rotating it around its own axe. aproxi 90° to 120°.<br>
<a href="https://drive.google.com/file/d/1QLypsNcrA_wgOpKbHF0ahg0f6kzwPeXB/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1QLypsNcrA_wgOpKbHF0ahg0f6kzwPeXB/view?usp=sharing</a>.<br>
i get slicerIGT and slicerheart modules . I’m novice with scripting ;so i need some to reconstruct the volume in the right way.</p>

---

## Post #6 by @derradji (2025-07-18 17:18 UTC)

<p>Finally I find my way and get my first volume reconstruction by rotation of the frames in one série.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c66eb2b2c0ec253d6422810110168ba2bfdd929d.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4af08e3e32097899a2669337632aa93ac3166376.png" data-video-base62-sha1="sjpHVSDnNskzDLuQFrZx9WH7Kc5.mp4">
  </div><br>
I do it using a python script. Thanks for the help.<p></p>

---
