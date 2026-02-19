---
topic_id: 20900
title: "How To Find Specific Voxel On Image On 3D Slicer"
date: 2021-12-03
url: https://discourse.slicer.org/t/20900
---

# How to find specific voxel on image on 3D Slicer?

**Topic ID**: 20900
**Date**: 2021-12-03
**URL**: https://discourse.slicer.org/t/how-to-find-specific-voxel-on-image-on-3d-slicer/20900

---

## Post #1 by @N.Arjmandi (2021-12-03 12:56 UTC)

<p>How to find voxel with specific ijk coordinates ( for example, voxel (205, 140,  52) ) on an 3D image?( location of the voxel in the image)</p>

---

## Post #3 by @ebrahim (2021-12-03 21:16 UTC)

<p>I think I misunderstood the question in my first resposne-- you want to convert from an index to spatial coordinates based on the image voxel size.</p>
<p>Here’s a way in the python console:</p>
<pre><code class="lang-auto">node = getNode("the name of your volume node")
imageData = node.GetImageData() # Get the underlying vtkImageData
p = [0,0,0]
imageData.TransformContinuousIndexToPhysicalPoint(205,140,52, p) # Stores answer in p
print(p)
</code></pre>
<p>See <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#acabf9f09dd9e6ab412004c747edc846f" rel="noopener nofollow ugc"><code>vtkImageData::TransformContinuousIndexToPhysicalPoint</code></a></p>
<p>IDK if there’s some other way to get this without the console</p>

---

## Post #4 by @mikebind (2021-12-03 22:12 UTC)

<p>It is possible to see this information interactively in the Data Probe (typically present in the lower left of the screen) as well.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45773a8f27eadd22b2f8436e402aec7874b8755a.png" alt="image" data-base62-sha1="9Uwoimkkjqo9swYwmSbFKOOdMJY" width="343" height="155"></p>
<p>The 3D spatial coordinates of the point the mouse is hovering over are shown in the top line (in the screenshot above the RAS coordinates of this point would be (-58.2, 12.4, -3.8)) and the voxel IJK index for the foreground, background, and label images voxels under the mouse focal point are shown below that. For example, in the screenshot, the voxel of the volume named ParcT1 with IJK coordinate (232,257,37) is located at (-58.2, 12.4, -3.8) in the world coordinate system.</p>
<p>This can be handy for cross-referencing, but it requires you to manually navigate to the point you are interested in, so for most purposes you probably want something more like <a class="mention" href="/u/ebrahim">@ebrahim</a> 's solution.</p>

---
