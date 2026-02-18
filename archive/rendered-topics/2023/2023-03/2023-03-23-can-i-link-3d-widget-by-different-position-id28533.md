# Can I Link 3D widget by different position?

**Topic ID**: 28533
**Date**: 2023-03-23
**URL**: https://discourse.slicer.org/t/can-i-link-3d-widget-by-different-position/28533

---

## Post #1 by @1023185654 (2023-03-23 06:25 UTC)

<p>Hi, developers， I saw that slicer’s current 3D window link function can only support setting the focus, position and orientation of two cameras in the same parameter for link, If I want to see P and A linked, when I click on a 3D window and the camera in the other window will sync to the current camera’s position, I want to realize the linkage of two different positions. Do you have any good suggestions？</p>

---

## Post #2 by @1023185654 (2023-03-23 06:27 UTC)

<p>Now the linkage behavior looks like the one shown below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8e9380c8f2e51a869405f3b63e1a0f6fce78887.png" data-download-href="/uploads/short-url/qnNwtDThYFvVNNOYeNdzfRbGi9h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8e9380c8f2e51a869405f3b63e1a0f6fce78887_2_690x237.png" alt="image" data-base62-sha1="qnNwtDThYFvVNNOYeNdzfRbGi9h" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8e9380c8f2e51a869405f3b63e1a0f6fce78887_2_690x237.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8e9380c8f2e51a869405f3b63e1a0f6fce78887_2_1035x355.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8e9380c8f2e51a869405f3b63e1a0f6fce78887.png 2x" data-dominant-color="9B9CCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×462 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
From A to L<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e1fbc26b4aabf8dae1b92bd8da35513b9603883.png" data-download-href="/uploads/short-url/khhN8XDKiu4pll4b9yJ63jOkNVh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e1fbc26b4aabf8dae1b92bd8da35513b9603883_2_690x234.png" alt="image" data-base62-sha1="khhN8XDKiu4pll4b9yJ63jOkNVh" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e1fbc26b4aabf8dae1b92bd8da35513b9603883_2_690x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e1fbc26b4aabf8dae1b92bd8da35513b9603883_2_1035x351.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e1fbc26b4aabf8dae1b92bd8da35513b9603883.png 2x" data-dominant-color="9B9CCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×432 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @1023185654 (2023-03-23 06:31 UTC)

<p>Here’s how I expect the linkage to behave<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b904956f7df9dae0b4eaa9652ceafa1784266c46.png" data-download-href="/uploads/short-url/qoK9sJ6Aaam86EwFowBn2a8sO4C.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b904956f7df9dae0b4eaa9652ceafa1784266c46_2_690x236.png" alt="image" data-base62-sha1="qoK9sJ6Aaam86EwFowBn2a8sO4C" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b904956f7df9dae0b4eaa9652ceafa1784266c46_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b904956f7df9dae0b4eaa9652ceafa1784266c46_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b904956f7df9dae0b4eaa9652ceafa1784266c46.png 2x" data-dominant-color="9A9BCA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1186×407 51.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Same rotation trajectory as before， Below is the image I want to look like<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf519d2105139f87d133b2f994ca191cd4dd8fb.png" data-download-href="/uploads/short-url/qFTW0Kahlg6cZQKKk2M6xWYVU4H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf519d2105139f87d133b2f994ca191cd4dd8fb_2_690x236.png" alt="image" data-base62-sha1="qFTW0Kahlg6cZQKKk2M6xWYVU4H" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf519d2105139f87d133b2f994ca191cd4dd8fb_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf519d2105139f87d133b2f994ca191cd4dd8fb_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf519d2105139f87d133b2f994ca191cd4dd8fb.png 2x" data-dominant-color="9A9BCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1261×432 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is a very special case</p>

---
