---
topic_id: 26712
title: "Help On Customizing Synchronization Behavior For Linked View"
date: 2022-12-13
url: https://discourse.slicer.org/t/26712
---

# Help on customizing synchronization behavior for linked views of different volumes

**Topic ID**: 26712
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/help-on-customizing-synchronization-behavior-for-linked-views-of-different-volumes/26712

---

## Post #1 by @Long_Zhang (2022-12-13 14:55 UTC)

<p>Hi,</p>
<p>When comparing two volumes of the same patient but different studies, it would be good to overlay the same portion together. Thus, I wondering how to customize the default behavior of scrolling, moving,  scalling operations, such that they are not simple broad casting physical position through different sliceviews, but with a specified offset to overlay the same part together.</p>
<p>An example looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b68e78bdeec7772fe947e5ffa8458afc813d0ada.jpeg" data-download-href="/uploads/short-url/q2Y8UswydnB1I92NnXLRi4ra2ZI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e78bdeec7772fe947e5ffa8458afc813d0ada_2_690x411.jpeg" alt="image" data-base62-sha1="q2Y8UswydnB1I92NnXLRi4ra2ZI" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e78bdeec7772fe947e5ffa8458afc813d0ada_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e78bdeec7772fe947e5ffa8458afc813d0ada_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e78bdeec7772fe947e5ffa8458afc813d0ada_2_1380x822.jpeg 2x" data-dominant-color="1F1F1F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1465×874 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance!</p>
<p>All the best,<br>
Long</p>

---

## Post #2 by @lassoan (2022-12-14 06:56 UTC)

<p>This is already supported: you can apply a the “offset” as a transform using Transforms module.</p>
<p>You can compute the correct alignment transform by <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">automatic or semi-automatic image registration</a>.</p>

---

## Post #5 by @Long_Zhang (2022-12-15 08:50 UTC)

<p>We already know the offset for each voxels for the two volumes. But we donot know how to customize the default behavior of scrolling, scaling, zooming, etc. to apply such values. In this way, the two volumes can be displayed in a way where the locations under the cursor are aligned. The transform is not nessary in this case as the two volumes are original DICOM volumes, and the offsets are manipulated.</p>

---

## Post #6 by @lassoan (2022-12-15 14:35 UTC)

<aside class="quote no-group" data-username="Long_Zhang" data-post="5" data-topic="26712">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/long_zhang/48/13519_2.png" class="avatar"> Long_Zhang:</div>
<blockquote>
<p>But we donot know how to customize the default behavior of scrolling, scaling, zooming, etc. to apply such values.</p>
</blockquote>
</aside>
<p>Linking of views sets the slice views to the same physical location. To make the content consistently aligned in all views I would recommend applying the known transform.</p>
<p>Of course, you can do everything in 3D Slicer, and if you want you can browse slices with arbitrary offset/rotation between them. There are many ways to achieve this. To recommend the most suitable method, could you describe your clinical end goal?</p>
<p>In the meantime, here is a simple method for offset slice browsing without any custom scripting:</p>
<ul>
<li>create a linear transforms <code>ReslicingTransform</code> and `OffsetTransform</li>
<li>set <code>ReslicingTransform</code> be a parent of <code>OffsetTransform</code></li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e2b7371738f93098668ab2c9cb27fbb67dc48d.png" data-download-href="/uploads/short-url/8g4X1dn9BZgAaVvW7JipwbOfWfX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e2b7371738f93098668ab2c9cb27fbb67dc48d.png" alt="image" data-base62-sha1="8g4X1dn9BZgAaVvW7JipwbOfWfX" width="690" height="269" data-dominant-color="2F3030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×341 9.08 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>use <code>Volume Reslice Driver</code> module to move the green and yellow slices with these transforms in <code>Transverse</code> mode</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/715467b3e87ee4561343add32b1f7bb9237d35d8.png" data-download-href="/uploads/short-url/gayN3ucSrjaNZV6TCgXC7MpgV4I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/715467b3e87ee4561343add32b1f7bb9237d35d8_2_495x500.png" alt="image" data-base62-sha1="gayN3ucSrjaNZV6TCgXC7MpgV4I" width="495" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/715467b3e87ee4561343add32b1f7bb9237d35d8_2_495x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/715467b3e87ee4561343add32b1f7bb9237d35d8_2_742x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/715467b3e87ee4561343add32b1f7bb9237d35d8_2_990x1000.png 2x" data-dominant-color="47433B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1021×1031 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>browse slices by adjusting the <code>ReslicingTransform</code></li>
<li>adjust offset between slices using <code>OffsetTransform</code></li>
</ul>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://aEk7aieNRkOsWG9r0fxBNAPBcOG.mp4">
  </div><p></p>

---
