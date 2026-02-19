---
topic_id: 28228
title: "Image Loaded From Tiff Stack Appears Distorted"
date: 2023-03-08
url: https://discourse.slicer.org/t/28228
---

# Image loaded from tiff stack appears distorted

**Topic ID**: 28228
**Date**: 2023-03-08
**URL**: https://discourse.slicer.org/t/image-loaded-from-tiff-stack-appears-distorted/28228

---

## Post #1 by @studyskin (2023-03-08 02:11 UTC)

<p>hi, does anybody know how i can fix my models being loaded warped? ive tried loading it with slicermorph and normal<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0be097c262911436b55b5e69a0b76ad022f7b5eb.jpeg" data-download-href="/uploads/short-url/1H4rhyqgJIolWVn6OIm5zvjGn9x.jpeg?dl=1" title="slicerotteris" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be097c262911436b55b5e69a0b76ad022f7b5eb_2_690x388.jpeg" alt="slicerotteris" data-base62-sha1="1H4rhyqgJIolWVn6OIm5zvjGn9x" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be097c262911436b55b5e69a0b76ad022f7b5eb_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be097c262911436b55b5e69a0b76ad022f7b5eb_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be097c262911436b55b5e69a0b76ad022f7b5eb_2_1380x776.jpeg 2x" data-dominant-color="7E7F86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerotteris</span><span class="informations">1920×1080 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c4c99fb9101f89e4e8c8acf0aaedb882e0e1edd.jpeg" data-download-href="/uploads/short-url/8BqLvaq2ESjVGa3PLoa2nr8MBAN.jpeg?dl=1" title="slicerottermodel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c4c99fb9101f89e4e8c8acf0aaedb882e0e1edd_2_690x388.jpeg" alt="slicerottermodel" data-base62-sha1="8BqLvaq2ESjVGa3PLoa2nr8MBAN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c4c99fb9101f89e4e8c8acf0aaedb882e0e1edd_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c4c99fb9101f89e4e8c8acf0aaedb882e0e1edd_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c4c99fb9101f89e4e8c8acf0aaedb882e0e1edd_2_1380x776.jpeg 2x" data-dominant-color="7E8285"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerottermodel</span><span class="informations">1920×1080 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
, thank you to anyone who can help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @muratmaga (2023-03-08 03:46 UTC)

<aside class="quote no-group" data-username="studyskin" data-post="1" data-topic="28228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/82dd89/48.png" class="avatar"> studyskin:</div>
<blockquote>
<p>fix my models being loaded warped</p>
</blockquote>
</aside>
<p>This is an issue with incorrect image spacing. most likely you have anisotropic data (i.e., one dimension of image is of different resolution than the others).</p>
<p>Please check with whoever gave you the dataset (or download it from), and enter the correct spacing values into the SlicerMorph’s <code>ImageStacks</code> module during import.</p>

---
