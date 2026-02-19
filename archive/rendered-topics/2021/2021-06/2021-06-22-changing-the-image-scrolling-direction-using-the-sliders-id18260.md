---
topic_id: 18260
title: "Changing The Image Scrolling Direction Using The Sliders"
date: 2021-06-22
url: https://discourse.slicer.org/t/18260
---

# Changing the image scrolling direction using the sliders

**Topic ID**: 18260
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/changing-the-image-scrolling-direction-using-the-sliders/18260

---

## Post #1 by @spycolyf (2021-06-22 01:50 UTC)

<p>One of my physician users stated that with most image viewers, the Axial image scroll bar scrolls from left to right displaying superior to inferior, respectively. For coronals and sagittals, from anterior to posterior (I believe)  However, Slicer displays the images from Inferior to Superior as you scroll from left to right…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8256470784cdf29c0820cd9825ac446edd26220a.png" alt="image" data-base62-sha1="iB0V1yIqKhN2VxmO7bu4TSyNpp0" width="270" height="272"></p>
<p>Is it possible to change the scroll orientation of the scroll bar so that Axial scrolling left to right displays superior to inferior slice order?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-06-22 04:57 UTC)

<p>Most image viewers don’t show slices along any particular anatomical axis, just show 2D images, in the order they were acquired. Since most common patient orientation is head-first supine, it appears that the scroll bar goes from superior to inferior, but actually the viewer is just browsing a list and does not know anything about orientations. In case of feet-first acquisitions or 3D acquisitions the order of slices may not be from superior to inferior, so users should not rely on this order.</p>
<p>Slicer is a true 3D viewer and you actually browse slices along designated physical directions, regardless of what order the slices were acquired or reconstructed. You can easily assign any physical axis directions to each slice view, as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-slice-view-orientation">this example</a>.</p>
<p>If you prefer to have patient left on screen right and scroll from superior to inferior then you probably want to use this sliceToRAS matrix:</p>
<ul>
<li>first column: screen right → patient left, in RAS: (-1, 0, 0)</li>
<li>second column: screen up → patient anterior, in RAS: (0, 1, 0)</li>
<li>third column: scroll direction → patient inferior, in RAS: (0, 0, -1)</li>
</ul>
<pre><code class="lang-python"># Axial slice axes:
#  -1     0     0
#   0     1     0
#   0     0    -1
axialSliceToRas=vtk.vtkMatrix3x3()
axialSliceToRas.SetElement(0,0, -1)
axialSliceToRas.SetElement(2,2, -1)
</code></pre>

---

## Post #3 by @spycolyf (2021-06-22 15:19 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I’m not touching this one as my release date is approaching fast. Therefore, they can live with this one.</p>

---
