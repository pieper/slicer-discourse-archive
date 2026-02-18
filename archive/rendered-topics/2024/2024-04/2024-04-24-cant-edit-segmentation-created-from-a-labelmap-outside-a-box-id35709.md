# Can't edit segmentation created from a labelmap outside a box

**Topic ID**: 35709
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/cant-edit-segmentation-created-from-a-labelmap-outside-a-box/35709

---

## Post #1 by @Matteboo (2024-04-24 15:37 UTC)

<p>Hello,</p>
<p>I created a segmentation from a labelmap. I tried to edit this segmentation using the segment editor but I can’t get outside of a box that seems to be the smallest box around my segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e394e0b1fe8c65f56267b39a09ad0b183697f49.png" data-download-href="/uploads/short-url/mzIdm4WApvh7M5osI3xuelE9N5T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e394e0b1fe8c65f56267b39a09ad0b183697f49_2_690x299.png" alt="image" data-base62-sha1="mzIdm4WApvh7M5osI3xuelE9N5T" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e394e0b1fe8c65f56267b39a09ad0b183697f49_2_690x299.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e394e0b1fe8c65f56267b39a09ad0b183697f49_2_1035x448.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e394e0b1fe8c65f56267b39a09ad0b183697f49_2_1380x598.png 2x" data-dominant-color="525258"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×833 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In green you can see the segment from the lablemap in blue I tried to segment as far as possible.<br>
This happened on 5.6.2</p>
<p>I found a workaround where I create a new segmentation and move my segment in the new segmentation but I was wondering if a more elegant solution exists</p>

---

## Post #2 by @pieper (2024-04-24 16:54 UTC)

<p>Yes, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">change the geometry</a> of the segmentation.</p>

---

## Post #3 by @Matteboo (2024-04-25 12:01 UTC)

<p>Thank you, it worked<br>
As a bonus, here is how to do it in python</p>
<pre><code class="lang-auto">segmentation_node.SetReferenceImageGeometryParameterFromVolumeNode(volume_node)
</code></pre>

---
