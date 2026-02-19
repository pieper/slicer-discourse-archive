---
topic_id: 18811
title: "Get A Leftmost Rightmost Coordinate With Simpleitk"
date: 2021-07-20
url: https://discourse.slicer.org/t/18811
---

# Get a leftmost/rightmost coordinate with SimpleITK

**Topic ID**: 18811
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/get-a-leftmost-rightmost-coordinate-with-simpleitk/18811

---

## Post #1 by @sandyaa0313 (2021-07-20 08:45 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.20200930</p>
<p>I create a labelmap volume node and read it as a SimpleITKimage.<br>
Now I show this labelmap volume in red, green and yellow slice window.<br>
I want to know how to get a leftmost/rightmost coordinate in slice window.<br>
Since I’m not familiar with SimpleITK, I have no idea about the problem.<br>
Thank you.</p>
<p>Here is my code:<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
labelmapVolumeNode.SetName(“Test_volume”)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)</p>
<p>test_volume = slicer.util.getNode(“Test_volume”)<br>
inputImage = sitkUtils.PullVolumeFromSlicer(test_volume)</p>

---

## Post #2 by @lassoan (2021-07-20 12:10 UTC)

<p>You can use <code>GetBounds</code> method of the volume node to get physical bounds (in RAS coordinate system).</p>
<p>Note that this is not very useful (gives just a rough approximation) in general, because the volume axes can be in arbitrary order and direction in physical space. If you want your code to be always accurate then you can use the IJKToRAS transform (that specifies origin, spacing, and IJK axis directions) and the image extent. You can get them by calling GetIJKToRAS method of the volume node and GetExtent method of the image data.</p>

---

## Post #3 by @sandyaa0313 (2021-07-21 07:47 UTC)

<p>I’m not sure whether I complete the IJKToRAS transform.<br>
However, I have the error says that “‘Image’ object has no attribute ‘GetExtent’”.<br>
Thanks a lot.</p>
<p>I import SimpleITK as below:</p>
<p>import SimpleITK as sitk<br>
import sitkUtils</p>
<p>Here is my code now:</p>
<p>test_volume = slicer.util.getNode(“Test_volume”)<br>
direction = vtk.vtkMatrix4x4()<br>
test_volume.GetRASToIJKMatrix(direction)<br>
test_volume.ApplyTransformMatrix(direction)<br>
image = sitkUtils.PullVolumeFromSlicer(test_volume)<br>
dims = image.GetExtent()</p>

---

## Post #4 by @sandyaa0313 (2021-07-21 10:25 UTC)

<p>Now I fixed the error, but I don’t understand the function output.<br>
From image.GetSize(), I get (283, 206, 265).<br>
From  vimage.GetExtent(), I get (0, 282, 0, 205, 0, 264).<br>
I’m not sure how to get the coordinate from them.<br>
Thank you.</p>
<p>Here is my code now:<br>
test_volume = slicer.util.getNode(“Test_volume”)<br>
direction = vtk.vtkMatrix4x4()<br>
test_volume.GetRASToIJKMatrix(direction)<br>
test_volume.ApplyTransformMatrix(direction)<br>
image = sitkUtils.PullVolumeFromSlicer(test_volume)<br>
direction = image.GetDirection()<br>
print(image.GetSize())<br>
vimage = test_volume.GetImageData()<br>
dims = vimage.GetExtent()<br>
print(dims)</p>
<p>The coordinates I want to get is where red arrow points to.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65eb4a3578b380ec8d41cfda62fccfa80a7eb9e1.png" data-download-href="/uploads/short-url/exCkvqa3oxpa4WIVw2YITTyfA7n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65eb4a3578b380ec8d41cfda62fccfa80a7eb9e1.png" alt="image" data-base62-sha1="exCkvqa3oxpa4WIVw2YITTyfA7n" width="536" height="499" data-dominant-color="F5F4F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×666 5.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-07-21 12:54 UTC)

<p>If you are interested in the bounding box of the content of a segment then you can get that directly from the segmentation object (in voxel coordinates). You can get oriented bounding box from Segment Statistics module.</p>
<p>There are so many kind of bounding boxes (aligned with image axes, patient axes, principal axes, oriented bounding box; potentially transformed using linear or non-linear transforms; in voxel or physical coordinate system) and so many ways to get them that it would help if you could write a bit about what would you like to use this for and how, because it would just take too much time to describe all the possibilities.</p>

---

## Post #6 by @sandyaa0313 (2021-07-23 09:03 UTC)

<p>My goal is to receive the volume of  red and blue area. Here is my algorithm.</p>
<ol>
<li>Get the leftmost and rightmost coordinate in red slice window.</li>
<li>Go through the image, and fill the hole by replacing 0 with 1, then the blue area can be created.</li>
</ol>
<p>My problems are:</p>
<ul>
<li>Because red and black area are two volume, I also wonder that if is possible to combine them into one labelmap volume. Since the the slice window can only show one labelmap in one time.</li>
<li>map and visualize the point in 2d slice into 3d view. I used TransformIndexToPhysicalPoint() and fiducial node before, but the position was weird.</li>
</ul>
<pre><code class="lang-auto"># It doesn't look like situated at the corner.
index= (image.GetSize()[0], image.GetSize()[1], image.GetSize()[2])
image.TransformIndexToPhysicalPoint(index)
</code></pre>
<p>I will explain my problem in detail below.</p>
<p>Now I’m trying to find the coordinate of green line in the red slice window. Just like the picture below. I want to go through every slice in red slice window and find the coordinates.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b336509dc577dd8c6b8d0210e2034e3f037c980.jpeg" data-download-href="/uploads/short-url/jRqtOVq7vgczRcOiW6PNG9EW8Za.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b336509dc577dd8c6b8d0210e2034e3f037c980.jpeg" alt="image" data-base62-sha1="jRqtOVq7vgczRcOiW6PNG9EW8Za" width="470" height="500" data-dominant-color="F0DEDE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">503×535 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269aef1b7485c3247c431997f334c76bb3829e70.jpeg" data-download-href="/uploads/short-url/5vw5u4tGBa5KEsWSDzTp9pKATde.jpeg?dl=1" title="image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269aef1b7485c3247c431997f334c76bb3829e70.jpeg" alt="image2" data-base62-sha1="5vw5u4tGBa5KEsWSDzTp9pKATde" width="547" height="500" data-dominant-color="F1ECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image2</span><span class="informations">560×511 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I first cut the image into 2d named target image for testing.<br>
Once I touch a point that value is not zero, I break the loop.<br>
I want to know how to check this point’s coordinate in 3d view, in order to check this code works. Then I can modify the parameters to find the coordinates of green line.<br>
Thank you.</p>
<p>Here is my code:</p>
<pre><code class="lang-auto">image = sitkUtils.PullVolumeFromSlicer(test_volume)
direction = image.GetDirection()
image = sitk.Flip(image, [direction[0] &lt; 0, direction[4] &lt; 0, direction[8] &lt; 0])
image_shape = image.GetSize()
target_img = image[0:image_shape[0]-1, 0:image_shape[1]-1, 0]
array = sitk.GetArrayFromImage(target_img)

for j in range(image_shape[0]-1):
    for k in range(image_shape[1]-1):
        if(array[k][j]&gt;0):
            # I want to know how to map this point to 3d view.
            print(k,j,array[k][j])
            break
</code></pre>

---

## Post #7 by @lassoan (2021-07-23 12:46 UTC)

<p>You cannot implement such low-level image processing in Python. They would be way too slow. For example to iterate through a tiny 100x100x100 image you would do 1 million iterations. In C++ or other low-level languages this would take a fraction of a second, while in Python in can take minutes.</p>
<p>Instead, you need to think about how you can implement a feature using high-level operations. For example, you can do the projection that you described above by copying the entire shape shifted by one pixel, repeated 100 times, and it would be magnitudes faster than implement iterating through each pixel of the image.</p>
<p>I guess you are still working on this:</p>
<aside class="quote quote-modified" data-post="5" data-topic="18451">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sandyaa0313/48/11566_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/do-projection-from-polydata-to-a-model-surface/18451/5">Do projection from polydata to a model surface</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve tried, but this module seems not to suit for my case. 
I already have chest model so I don’t have to use markup points to create the chest wall. 
Because the chest wall in breast reconstruction module is created by markup points, and markup points are situated on the breast model, it can create a closed model obviously. 
However, in my module, the chest wall model is from CT, and the breast model is from 3d scan, they are aligned but with some distance. 
I think these two modules have diffe…
  </blockquote>
</aside>

<p>I would recommend to have a look at the existing Slicer module for almost the same task (<a href="https://github.com/PerkLab/BreastReconstruction" class="inline-onebox">GitHub - PerkLab/BreastReconstruction: Tool for breast reconstruction surgery planning</a>) because we already have this kind of projection implemented in it.</p>

---

## Post #8 by @sandyaa0313 (2021-08-05 07:31 UTC)

<p>Ok! I understand. I’ll reconsider my project. Thanks for your patience.</p>

---
