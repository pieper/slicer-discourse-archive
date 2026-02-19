---
topic_id: 20408
title: "Volume With Negative Spacing Turns In Strange Behaviour Bug"
date: 2021-10-28
url: https://discourse.slicer.org/t/20408
---

# Volume with negative spacing turns in strange behaviour (bug?)

**Topic ID**: 20408
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/volume-with-negative-spacing-turns-in-strange-behaviour-bug/20408

---

## Post #1 by @keri (2021-10-28 22:37 UTC)

<p>Hi,</p>
<p>When I try to add volume with negative spacing in <code>X</code> direction to Slicer I get strange behavior.</p>
<p>For example here is the python code to generate volume and add it to the Slicer (based on example in script repo):</p>
<pre><code class="lang-cpp">nodeName = "MyNewVolume"
imageSize = [10, 10, 10]
imageOrigin = [0.0, 0.0, 0.0]
imageSpacing = [-1.0, 1.0, 1.0] # `X` spacing is negative

scalars = vtk.vtkDoubleArray()
scalars.SetName("my_scalars")

for i in range(0, imageSize[0]*imageSize[1]*imageSize[2]):
    v = scalars.InsertNextValue(i)

# Create an image volume
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.GetPointData().SetScalars(scalars)
# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()
</code></pre>
<p>Then I go to the <code>Data</code> module and add the volume to the renderers.<br>
On each slice view I click the button to visualize the volume in 3D view.<br>
Then I go to the <code>Volumes</code> module and then after zooming in/out I can see something similar on the picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1d965b6f541dba02cc99bf2081d06be3b63a6b4.jpeg" data-download-href="/uploads/short-url/n5MDWUHMAp3NYgqOc6CiN1Y4efq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1d965b6f541dba02cc99bf2081d06be3b63a6b4_2_690x335.jpeg" alt="image" data-base62-sha1="n5MDWUHMAp3NYgqOc6CiN1Y4efq" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1d965b6f541dba02cc99bf2081d06be3b63a6b4_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1d965b6f541dba02cc99bf2081d06be3b63a6b4_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1d965b6f541dba02cc99bf2081d06be3b63a6b4_2_1380x670.jpeg 2x" data-dominant-color="8CAAA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1546×751 91.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Originally the volume has <code>nx = ny = nz = 10</code> points.<br>
If I set the <code>nx</code> to some positive value then there is nothing bad hapen.</p>
<p>I tested it only in Slicer 4.11.2 (see window title) on Ubuntu 20.04 and also in SlicerCAT.</p>
<p>Can’t say for sure but as I far as I know <code>vtkImageData</code> is supposed to work fine with negative spacings and negative origin (at least I could visualize it, can’t say anything about filtering).</p>

---

## Post #2 by @mikebind (2021-10-28 23:02 UTC)

<p>What would a volume with negative spacing mean?  My understanding is that the spacing values are the physical lengths between adjacent voxels, which could not sensibly be negative.  Image directions, on the  other hand, could indicate that increasing voxel index values along a dimension correspond to an increasing and negative spatial coordinate value, but this is separate from specifying the size of the voxel itself.</p>

---

## Post #3 by @keri (2021-10-28 23:25 UTC)

<p>I would not give much phisical sense to spacing. I think the phisical or any other meaning should have the grid that is created (in this case the gfid is given by the image). Spacing is just a mean to create the grid and nothong more.</p>
<p>My special use case is the following:<br>
I have few gigabytes (or eve more) of scalar data that should be displayed as vtkImageData. But the data is loaded to the RAM and if I use only positive spacing then I would need either to rearrange the data (very bad solution) or apply transforms or mirror filter. Ok I can do that but I always keep in mind why devellopers dont want add negave spacings <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I dont know is it such a big deal or it is a matter of phisics?</p>

---

## Post #4 by @pieper (2021-10-28 23:41 UTC)

<p>Definitely spacing is a distance and should never be negative.  <a class="mention" href="/u/mikebind">@mikebind</a> is correct that direction vectors can have negative elements because they are relative to a reference frame.  In Slicer we always have unit spacing and zero origin in the <code>vtkImageData</code> and encode origin, spacing, and directions in the <code>ijkToRAS</code> matrix (which is another name for index to physical).</p>

---

## Post #5 by @keri (2021-10-29 00:02 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for response,</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="20408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>In Slicer we always have unit spacing and zero origin</p>
</blockquote>
</aside>
<p><code>unit spacing</code> mean the spacing should always be equal to 1 or <code>unit</code> mean that spacing has some units (meter or millimeter or something)? Also does Slicer suppose that the origin should always be set to 0 and should not be set to any other (positive or negative) value?</p>

---

## Post #6 by @pieper (2021-10-29 00:27 UTC)

<p>It just means that we use the <code>vtkImageData</code> as an array to hold only index space values.  All the physical space values are in the <code>ijkToRAS</code> matrix.  Yes, as a concept spacing should always be positive even if the data type is inherently signed.  Generally people don’t have checks for such things for efficiency.</p>

---

## Post #7 by @lassoan (2021-10-29 01:24 UTC)

<p>Spacing values are the column norms of the orientation section (top-left 3x3 submatrix) of the IJK to RAS matrix, so these values are always positive. You can write negative values in the orientation submatrix, but ITK and VTK put some limitations on these, and since we use ITK and VTK throughout Slicer, these limitations apply to Slicer, too:</p>
<ul>
<li>the IJK to RAS matrix must be orthogonal</li>
<li>IJK axes form a right-handed coordinate system (determinant of IJK to RAS matrix must be positive)</li>
<li>the above restrictions are not universally enforced and they are specifically allowed in certain classes, such as in the image class and image IO classes (therefore it is allowed to read an image with arbitrary IJK to RAS matrix and store it in a VTK or ITK image until it is converted to an image that conforms to the requirements).</li>
</ul>
<p>If you only need to do certain image processing or visualization steps then you can test that they work correctly your non-conformant image. If you want to allow a user to do arbitrary operations on the image then you must resample the voxel array so that you have an orthogonal IJK to RAS matrix with positive determinant.</p>
<p>If the only issue is right-handedness then you can mirror the voxel array along any axis. The easiest is to do it along the third axis, which is simply reorder slices. This is a very fast operation, even for huge volumes.</p>

---

## Post #8 by @keri (2021-10-29 11:54 UTC)

<p>Thank all for the informative answers.<br>
I will keep in that mind</p>

---
