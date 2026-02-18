# How to rotate a volume use volume center?

**Topic ID**: 31373
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/how-to-rotate-a-volume-use-volume-center/31373

---

## Post #1 by @icedream (2023-08-26 07:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d6648824fb064921dd8916422c5bf2d0eab5903.jpeg" data-download-href="/uploads/short-url/1UxlzuEYXiAxue4oEHufLcQ1tiX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d6648824fb064921dd8916422c5bf2d0eab5903_2_690x242.jpeg" alt="image" data-base62-sha1="1UxlzuEYXiAxue4oEHufLcQ1tiX" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d6648824fb064921dd8916422c5bf2d0eab5903_2_690x242.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d6648824fb064921dd8916422c5bf2d0eab5903_2_1035x363.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d6648824fb064921dd8916422c5bf2d0eab5903_2_1380x484.jpeg 2x" data-dominant-color="64656D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×674 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when i change the slider bar value of [LR],[PA],[IS]，the volume rotate by a centain point in 3d space but not the center of volume,how to make the rotate center to the center of the volume?</p>

---

## Post #2 by @ebrahim (2023-08-28 12:26 UTC)

<p>Rotation is about the origin, so you want to first translate the image so that (0,0,0) is the location in the image about which you want to center your rotations. You can do this by a separate transform that precedes the rotation, or you can go to the volume information (in the volumes module) and edit the origin.</p>

---

## Post #3 by @yulaomao (2023-08-29 00:53 UTC)

<p>I have written a simple module that can achieve this functionality. It allows for dragging and rotating models or volumes. The rotation center is the center point of the volume or model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6618f6ab3cd9060a5dfd722a505454fa2166ee6c.jpeg" data-download-href="/uploads/short-url/ezcbxxLgrHDjywkj3CkB2hOTofy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6618f6ab3cd9060a5dfd722a505454fa2166ee6c_2_690x285.jpeg" alt="image" data-base62-sha1="ezcbxxLgrHDjywkj3CkB2hOTofy" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6618f6ab3cd9060a5dfd722a505454fa2166ee6c_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6618f6ab3cd9060a5dfd722a505454fa2166ee6c_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/6618f6ab3cd9060a5dfd722a505454fa2166ee6c_2_1380x570.jpeg 2x" data-dominant-color="929398"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×788 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @yulaomao (2023-08-29 01:08 UTC)

<p>This is my git link：<a href="https://github.com/joifish0/transformModel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - joifish0/transformModel</a></p>

---
