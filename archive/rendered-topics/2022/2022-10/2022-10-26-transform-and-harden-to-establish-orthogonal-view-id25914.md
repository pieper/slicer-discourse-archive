---
topic_id: 25914
title: "Transform And Harden To Establish Orthogonal View"
date: 2022-10-26
url: https://discourse.slicer.org/t/25914
---

# Transform and Harden to establish Orthogonal view

**Topic ID**: 25914
**Date**: 2022-10-26
**URL**: https://discourse.slicer.org/t/transform-and-harden-to-establish-orthogonal-view/25914

---

## Post #1 by @juliangallaun (2022-10-26 18:06 UTC)

<p>Hello Everyone, I have a problem with my scanned fish heads (from µCT, tiff-files).</p>
<p>My scans are shifted and I wand to bring them in an standardized orthogonal view. I tried to replicate it like in this video:" <a href="https://www.youtube.com/watch?v=AOqeJtE04YM" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=AOqeJtE04YM</a> " but it doesn’t stay hardened in the programmed position.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0289d8b0287defbf6c86cc8d6931e5f5ae6c8869.png" data-download-href="/uploads/short-url/mshX79wzvBxUcsdTu5NGKASc1H.png?dl=1" title="Unbenannt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0289d8b0287defbf6c86cc8d6931e5f5ae6c8869_2_522x500.png" alt="Unbenannt" data-base62-sha1="mshX79wzvBxUcsdTu5NGKASc1H" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0289d8b0287defbf6c86cc8d6931e5f5ae6c8869_2_522x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/0289d8b0287defbf6c86cc8d6931e5f5ae6c8869_2_783x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0289d8b0287defbf6c86cc8d6931e5f5ae6c8869.png 2x" data-dominant-color="41414D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unbenannt</span><span class="informations">919×879 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here I select Transfrom to connect the Volume with the predefined Transform file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4bf9284ddc152d5ca4c0a92993bfa046e1468c.png" data-download-href="/uploads/short-url/1BW1uRuX1Y1YWAoXHZFYtvF2VEo.png?dl=1" title="Unbenannt1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4bf9284ddc152d5ca4c0a92993bfa046e1468c_2_514x500.png" alt="Unbenannt1" data-base62-sha1="1BW1uRuX1Y1YWAoXHZFYtvF2VEo" width="514" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4bf9284ddc152d5ca4c0a92993bfa046e1468c_2_514x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b4bf9284ddc152d5ca4c0a92993bfa046e1468c_2_771x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b4bf9284ddc152d5ca4c0a92993bfa046e1468c.png 2x" data-dominant-color="41404B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unbenannt1</span><span class="informations">900×874 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now the position of the volume in the red window is correct (and in the others too), I want to lock this transformation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ace9cc6851e4e4f87385aca7171faf537963a55.png" data-download-href="/uploads/short-url/hwoUOKJtztSkjMXhmcR2ahCHmU5.png?dl=1" title="Unbenannt2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ace9cc6851e4e4f87385aca7171faf537963a55_2_536x499.png" alt="Unbenannt2" data-base62-sha1="hwoUOKJtztSkjMXhmcR2ahCHmU5" width="536" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ace9cc6851e4e4f87385aca7171faf537963a55_2_536x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ace9cc6851e4e4f87385aca7171faf537963a55_2_804x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ace9cc6851e4e4f87385aca7171faf537963a55.png 2x" data-dominant-color="41404C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unbenannt2</span><span class="informations">930×866 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After hardening it and closing and opening the eye icon again, its shifted in at a new angel.</p>
<p>My main goal is to shift the voxels or slices according to an orthogonal view of my sample.</p>

---

## Post #2 by @muratmaga (2022-10-26 20:59 UTC)

<p>Can you expand the slice view toolbar and make sure that the orientation is not shown as “reformat”?</p>

---

## Post #3 by @lassoan (2022-10-27 05:46 UTC)

<aside class="quote no-group" data-username="juliangallaun" data-post="1" data-topic="25914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juliangallaun/48/9545_2.png" class="avatar"> juliangallaun:</div>
<blockquote>
<p>After hardening it and closing and opening the eye icon again, its shifted in at a new angel.</p>
</blockquote>
</aside>
<p>It is due to Slicer automatically setting the slice views to match the image axes by default. You can turn off this feature by right-clicking on the eye icon and unchecking “Reset… on show” checkboxes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9ea074fc8fa9daea76632101d7f91e78ddd75d5.png" data-download-href="/uploads/short-url/qwFJCQERfLcjJI8JdJsZQWkcGRT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9ea074fc8fa9daea76632101d7f91e78ddd75d5_2_690x165.png" alt="image" data-base62-sha1="qwFJCQERfLcjJI8JdJsZQWkcGRT" width="690" height="165" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9ea074fc8fa9daea76632101d7f91e78ddd75d5_2_690x165.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9ea074fc8fa9daea76632101d7f91e78ddd75d5_2_1035x247.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9ea074fc8fa9daea76632101d7f91e78ddd75d5_2_1380x330.png 2x" data-dominant-color="393F44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1447×347 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
