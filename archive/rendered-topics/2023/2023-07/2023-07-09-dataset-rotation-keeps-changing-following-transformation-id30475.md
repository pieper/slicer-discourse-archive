# Dataset rotation keeps changing following transformation

**Topic ID**: 30475
**Date**: 2023-07-09
**URL**: https://discourse.slicer.org/t/dataset-rotation-keeps-changing-following-transformation/30475

---

## Post #1 by @rsanaei (2023-07-09 17:45 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.2.2<br>
Expected behavior: hardened transform is not supposed to change arbitrarily<br>
Actual behavior: I am trying to stereotaxially rotate a few dicom datasets. Upon hardening the transform, and resampling, the transformed node seems to rotate randomly when I disable and re-enable visibility or when I apply the transform or switch to None. This always happens after resampling; also the resampled dataset does not show the same rotation as the initially transformed dataset. This seems to persist no matter what resampling module I use. It is quite frustrating. Am I doing anything wrong?</p>

---

## Post #2 by @pieper (2023-07-09 18:43 UTC)

<p>Transforms can be tricky, but I don’t know of any bugs that would lead to unpredictable behavior.  If you think there’s a bug, provide a step-by-step report with public data of what you did, what you expected, and what happened instead.  Use a few screenshots as needed to clarify.</p>

---

## Post #3 by @lassoan (2023-07-10 03:57 UTC)

<p>Note that by default when you show an image, the slice view axes are snapped to the closest axes of the image. You can disable this in the right-click menu of the eye icon in the Data module.</p>

---

## Post #4 by @rsanaei (2023-07-10 06:36 UTC)

<p>Thank you both for your replies. I have since figured out that resampling is best done without hardening the transform first and using the ‘Resample Scalar /Vector /DWI Volume module’. That said the buggy behaviour of transform persists. See below.</p>
<p>Here is how the original volume looks like (after a quick non-interpolating crop):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66f68fa6357ca5e28f4547494f6f3ac42d4902c0.jpeg" data-download-href="/uploads/short-url/eGQXjP9LuQ5yh9BPDvMfwxgBJEA.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66f68fa6357ca5e28f4547494f6f3ac42d4902c0_2_690x373.jpeg" alt="1" data-base62-sha1="eGQXjP9LuQ5yh9BPDvMfwxgBJEA" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66f68fa6357ca5e28f4547494f6f3ac42d4902c0_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66f68fa6357ca5e28f4547494f6f3ac42d4902c0_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66f68fa6357ca5e28f4547494f6f3ac42d4902c0_2_1380x746.jpeg 2x" data-dominant-color="6D6F76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1801×975 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When a linear transform is created and applied (by right clicking under the transform column in the Data module), all works ok as shown below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/756c641bd8ce25804b1633741c3f660118b23bf4.jpeg" data-download-href="/uploads/short-url/gKM5D1dvqJe4S5yxRQSsSjcS0w4.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756c641bd8ce25804b1633741c3f660118b23bf4_2_690x373.jpeg" alt="2" data-base62-sha1="gKM5D1dvqJe4S5yxRQSsSjcS0w4" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756c641bd8ce25804b1633741c3f660118b23bf4_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756c641bd8ce25804b1633741c3f660118b23bf4_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756c641bd8ce25804b1633741c3f660118b23bf4_2_1380x746.jpeg 2x" data-dominant-color="7C7E84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1807×978 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the volume is made hidden and visible in succession, while keeping the transform applied, the following happens (the presentation does not resemble the original volume nor the transformed volume):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d318a8d29e64fc2ded88f16d66cc546ac6e1f7.jpeg" data-download-href="/uploads/short-url/zE3a2twh2azBLyZDk5xZk24d8nJ.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d318a8d29e64fc2ded88f16d66cc546ac6e1f7_2_690x371.jpeg" alt="3" data-base62-sha1="zE3a2twh2azBLyZDk5xZk24d8nJ" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d318a8d29e64fc2ded88f16d66cc546ac6e1f7_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d318a8d29e64fc2ded88f16d66cc546ac6e1f7_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9d318a8d29e64fc2ded88f16d66cc546ac6e1f7_2_1380x742.jpeg 2x" data-dominant-color="76787E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1804×972 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @rsanaei (2023-07-10 06:37 UTC)

<p>This only solves when the volume is made hidden, None applied under the transform followed by making the volume visible again and reapplying the transform then.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77a16dd987ded9ad64d5f297353311b67c9869e1.jpeg" data-download-href="/uploads/short-url/h4iG6Z01BUN3MkU7vywN5zZDcnD.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a16dd987ded9ad64d5f297353311b67c9869e1_2_690x373.jpeg" alt="4" data-base62-sha1="h4iG6Z01BUN3MkU7vywN5zZDcnD" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a16dd987ded9ad64d5f297353311b67c9869e1_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a16dd987ded9ad64d5f297353311b67c9869e1_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77a16dd987ded9ad64d5f297353311b67c9869e1_2_1380x746.jpeg 2x" data-dominant-color="7C7E84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1804×976 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Right clicking on the menu of the eye icon in the Data module and changing the setting did not help.</p>

---

## Post #6 by @lassoan (2023-07-10 13:51 UTC)

<aside class="quote no-group" data-username="rsanaei" data-post="1" data-topic="30475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rsanaei/48/66727_2.png" class="avatar"> rsanaei:</div>
<blockquote>
<p>the transformed node seems to rotate randomly when I disable and re-enable visibility</p>
</blockquote>
</aside>
<p>Everything you describe looks good to me and shows the intended behavior of the application. The node does not rotate randomly, but it if “Reset view orientation on show” option is enabled then the slice view is rotated automatically to the closest volume axis when the volume is shown.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b22bc656dc750e8f9fcc2cc0cbd8726519d9684.png" data-download-href="/uploads/short-url/hzj9jvwMGAUjbbFt3DOUIvNyRLK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b22bc656dc750e8f9fcc2cc0cbd8726519d9684_2_690x272.png" alt="image" data-base62-sha1="hzj9jvwMGAUjbbFt3DOUIvNyRLK" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b22bc656dc750e8f9fcc2cc0cbd8726519d9684_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b22bc656dc750e8f9fcc2cc0cbd8726519d9684_2_1035x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b22bc656dc750e8f9fcc2cc0cbd8726519d9684.png 2x" data-dominant-color="343937"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1151×454 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can always set view to a standard orientation using the view controller (colored bar above each slice view), or you can set arbitrary view orientations using LR/PA/IS sliders in Reformat module.</p>
<p>If you still find the application behavior unintuitive then please add some annotations on the screenshots that indicate what you would have expected to see; or share a screen capture video.</p>

---

## Post #7 by @rsanaei (2023-07-11 04:14 UTC)

<p>Thanks very much Andras. That actually prevents the unpredictable behaviour - in my case, I still needed to hide and untick that option before re-enabling visibility to get the intuitive result. The issue however, does not happen to me when I use for example the chest-ct sample dataset from slicer’s website. As an end user who only uses 3D Slicer occasionally, if I may have a suggestion, it would be best if that option is unticked by default unless of course there is a particular reason to have it as is. Many thanks for your time and help.</p>

---

## Post #8 by @lassoan (2023-07-11 19:15 UTC)

<p>The option is enabled by default based on feedback from lots of users. Most people only uses 2D image review software, which regurgitates the original 2D slices. When Slicer showed the slices in standard anatomical orientations then these users did not understand what’s all this and reported it as a bug.</p>
<p>Since we changed the default a few years ago, I only remember question/complaint from a long-time Slicer power user and now from you. Since the option is remembered in the application settings (even when the application is restarted), it should cause minimal disruption for those who prefer to see reformatted slices.</p>

---

## Post #9 by @rsanaei (2023-07-12 14:20 UTC)

<p>Thanks Andras. It makes sense. I doubt I will ever forget the fix anyway given the amount of frustration that caused me, haha. Also, I am very impressed by how reachable and responsive you are. Much appreciated.</p>

---
