---
topic_id: 19141
title: "Rgy Views From Numpy Array"
date: 2021-08-10
url: https://discourse.slicer.org/t/19141
---

# RGY views from numpy array

**Topic ID**: 19141
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/rgy-views-from-numpy-array/19141

---

## Post #1 by @shatz (2021-08-10 13:50 UTC)

<p>When I first import my imaging file, it looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f2b4c2570e29c0aef334261baf6d9a781c4611e.jpeg" data-download-href="/uploads/short-url/6JhcJNllzLFiz5tEeWhd3S3tBrU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2b4c2570e29c0aef334261baf6d9a781c4611e_2_690x438.jpeg" alt="image" data-base62-sha1="6JhcJNllzLFiz5tEeWhd3S3tBrU" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2b4c2570e29c0aef334261baf6d9a781c4611e_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2b4c2570e29c0aef334261baf6d9a781c4611e_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f2b4c2570e29c0aef334261baf6d9a781c4611e_2_1380x876.jpeg 2x" data-dominant-color="5D5D69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1219 99.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I then get it as a numpy array through <code>arr = array("imaging")</code> and write it as a new volume by doing <code>addVolumeFromArray(arr, name="newarray")</code>, it looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31ff248d58dd66b949654cb8c3c48b95f654eeb6.jpeg" data-download-href="/uploads/short-url/78i2i038MRvCmwOtufDb8ctZ530.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31ff248d58dd66b949654cb8c3c48b95f654eeb6_2_690x435.jpeg" alt="image" data-base62-sha1="78i2i038MRvCmwOtufDb8ctZ530" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31ff248d58dd66b949654cb8c3c48b95f654eeb6_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31ff248d58dd66b949654cb8c3c48b95f654eeb6_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31ff248d58dd66b949654cb8c3c48b95f654eeb6_2_1380x870.jpeg 2x" data-dominant-color="545460"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2368×1493 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like for the views to correspond to eachother. So for example, the red “R” view would be a top-down view of the patient in the new volume as well.</p>
<p>Is there any way to keep all the formatting of the volume it came from?</p>

---

## Post #2 by @lassoan (2021-08-10 14:04 UTC)

<p>A simple numpy array cannot store the image geometry (image origin, spacing, and axis directions = IJK to RAS matrix). You need to copy the IJKToRASMatrix from the original volume to the new volume.</p>
<pre><code class="lang-python">ijkToRas = vtk.vtkMatrix4x4()
originalVolumeNode.GetIJKToRASMatrix(ijkToRas)
newVolumeNode.SetIJKToRASMatrix(ijkToRas)
</code></pre>

---
