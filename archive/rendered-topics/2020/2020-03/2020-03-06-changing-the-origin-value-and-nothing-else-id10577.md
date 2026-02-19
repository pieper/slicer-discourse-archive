---
topic_id: 10577
title: "Changing The Origin Value And Nothing Else"
date: 2020-03-06
url: https://discourse.slicer.org/t/10577
---

# Changing the origin value, and nothing else

**Topic ID**: 10577
**Date**: 2020-03-06
**URL**: https://discourse.slicer.org/t/changing-the-origin-value-and-nothing-else/10577

---

## Post #1 by @giovform (2020-03-06 15:06 UTC)

<p>Hello, I wanted to set a new origin point (to the last slice loaded), without modifying anything else (the volume must remain at the same spot in the world coordinates). In simple terms I just want that:</p>
<pre><code>node.GetOrigin() == (0, 0, 0)
</code></pre>
<p>for the configuration in the picture bellow, instead of currently:</p>
<pre><code>node.GetOrigin() == (0, 0, -100)
</code></pre>
<p>Is it possible to do that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a4bb776b20a6839cea5007d5f0151a709240930.png" data-download-href="/uploads/short-url/fakPI64Sa6H4AXZbAis9tFvfAiI.png?dl=1" title="problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a4bb776b20a6839cea5007d5f0151a709240930_2_666x500.png" alt="problem" data-base62-sha1="fakPI64Sa6H4AXZbAis9tFvfAiI" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a4bb776b20a6839cea5007d5f0151a709240930_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a4bb776b20a6839cea5007d5f0151a709240930.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a4bb776b20a6839cea5007d5f0151a709240930.png 2x" data-dominant-color="B4B4B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem</span><span class="informations">800×600 20.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-03-06 15:24 UTC)

<p>Do you mean you want to also flip the directions?  Did you try just calling <code>SetOrigin</code>?  You can also use <code>volumeNode.SetKToRASDirection</code> and related methods.</p>

---

## Post #3 by @giovform (2020-03-06 15:26 UTC)

<p>Yes, I played around with some functions, but no success. I just really want to change the Origin point, but not translating the volume in the world as a consequence.</p>

---

## Post #4 by @pieper (2020-03-06 15:38 UTC)

<p>The way we <a href="https://www.slicer.org/wiki/Coordinate_systems">use the term</a>, changing the origin would move the actual data in physical space unless you shuffle the data and change the directions.  Can you give more info on what you need to achieve?</p>

---

## Post #5 by @giovform (2020-03-06 17:16 UTC)

<p>I managed to get the result I wanted by doind these two steps:</p>
<ol>
<li>
<p>Revert the order of the files loaded into Slicer (I am using ‘DICOMScalarVolumePlugin’). By doing this, my volume is loaded upside down, and the origin is anchored where I want in the volume, i.e. at the top:</p>
<p>loadables[0].files = loadables[0].files[::-1]</p>
</li>
<li>
<p>Apply a transform to rotate 180 degrees around the Sagittal or Coronal axis.</p>
</li>
</ol>
<p>This way I have the volume origin at (0, 0, 0), at the top of volume.</p>
<p>I wanted to know if there is a more elegant way to achieve this result.</p>

---

## Post #6 by @pieper (2020-03-06 17:30 UTC)

<p>It’s not clear to me why you need the origin to be at a specific spot.  For example <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html#sect_C.7.6.2.1.1">in dicom</a> only the relative values of origin matter, and then only if they are in the same frame of reference.</p>

---

## Post #7 by @fbordignon (2020-03-06 17:41 UTC)

<p><a class="mention" href="/u/giovform">@giovform</a> has multiple volumes with an outside-of-Slicer-coordinate of the volumes defined by the top (patient head). When he loads the volume into slicer and sets the volume origin, this coordinate is defined at the bottom (patient feet), hence he needs to shift the outside-coordinate by the height of the patient. When the user wants to inspect the volume and retrieve the outside-of-Slicer-coordinate, the slicer volume origin coordinate is shifted.<br>
We would like to set the imagedata (ijk) origin to start at the last slice (patient head), and increases as slices moves to the feet (I world direction).</p>

---

## Post #8 by @lassoan (2020-03-06 17:51 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="7" data-topic="10577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>We would like to set the imagedata (ijk) origin to start at the last slice (patient head), and increases as slices moves to the feet (I world direction).</p>
</blockquote>
</aside>
<p>You cannot expect to have a particular voxel (IJK) to physical (LPS) coordinate system mapping in an image file that you load. If your application only works with one particular slice order then you need to normalize the images after you load them in your own software.</p>
<p>If you really want to do this normalization in Slicer, then you can still do it (as in general, Slicer does not reorder slices when it loads or saves an image volume), it is really not the right place to do it.</p>

---

## Post #9 by @fbordignon (2020-03-06 18:26 UTC)

<p>Great Andras, I agree with you. But if you allow me, I am still curious about this issue.</p>
<p>Why does ImageData.setOrigin(0,0,-100) does not work for this case?<br>
Is it because slicer assumes ijk always starts at zero and goes up to the dimensions of the imagedata?<br>
Vtk seems to deal with this just fine, as the volume is rendered at the right position when I set the ImageData origin.<br>
Thank you for the insights and ideas.</p>

---

## Post #10 by @lassoan (2020-03-06 19:12 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="9" data-topic="10577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>Why does ImageData.setOrigin(0,0,-100) does not work for this case?</p>
</blockquote>
</aside>
<p><code>SetOrigin()</code> method of vtkImageData must not be used. Origin, spacing, and axis directions of volumes are stored in the volume node, not in the vtkImageData (origin in vtkImageData must be kept (0,0,0)). The reason is that until recently, vtkImageData could not store image orientation and therefore the complete image geometry had to be stored outside the image data object. You can modify the origin by calling <code>SetOrigin()</code> method of the volume node.</p>
<p>Once we upgrade to VTK9, we can switch to using vtkImageData for storing image geometry, but probably this will take about a year.</p>

---
