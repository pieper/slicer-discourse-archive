# Scaling Segmentation in 3D space

**Topic ID**: 32784
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/scaling-segmentation-in-3d-space/32784

---

## Post #1 by @lena_b (2023-11-13 17:50 UTC)

<p>Hello, Is there a feature where you can scale a segmentation? I have used the Warping Tool in the Fiducial Registration Wizard, but for certain objects it requires too many points. Are there x, y, z sliders (for example) in another module where you can scale the size of a segmentation in all three dimensions? Thanks in advance for any help!</p>

---

## Post #2 by @pieper (2023-11-13 18:20 UTC)

<p>You could put it in a linear transform and type the scale factors in the diagonal of the matrix and then harden the transform.</p>

---

## Post #3 by @lena_b (2023-11-14 03:00 UTC)

<p>Hi Steve, thanks for the quick response! Where could I type the scale factors?</p>

---

## Post #4 by @pieper (2023-11-14 15:05 UTC)

<p>You can enter them in the diagonals of the matrix in this interface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f07f7829e09faf035a5e073fb998f6ee82fa03c.png" data-download-href="/uploads/short-url/8ZB9gHOaAzRdTiUpPKsiAoCnF3S.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f07f7829e09faf035a5e073fb998f6ee82fa03c_2_507x500.png" alt="image" data-base62-sha1="8ZB9gHOaAzRdTiUpPKsiAoCnF3S" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f07f7829e09faf035a5e073fb998f6ee82fa03c_2_507x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f07f7829e09faf035a5e073fb998f6ee82fa03c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f07f7829e09faf035a5e073fb998f6ee82fa03c.png 2x" data-dominant-color="E7E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">510×502 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lena_b (2023-11-14 20:01 UTC)

<p>Thanks for sending the screenshot! I am having trouble getting it to work for my case. The diagonal of the matrix will change the size of the segmentation object? As in, stretching it in the x-dimension (for example).</p>

---

## Post #6 by @pieper (2023-11-14 21:11 UTC)

<p>For example, here the segmentation (green) has been transformed so that it’s 1.5 x bigger than the MRHead that was used to define it originally.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cce545d46b9d0e09349779ce7bd8666d84676f6.jpeg" data-download-href="/uploads/short-url/deZZ9kQzzZVSJGZ7rHZLP6pqQN8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cce545d46b9d0e09349779ce7bd8666d84676f6_2_690x415.jpeg" alt="image" data-base62-sha1="deZZ9kQzzZVSJGZ7rHZLP6pqQN8" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cce545d46b9d0e09349779ce7bd8666d84676f6_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cce545d46b9d0e09349779ce7bd8666d84676f6_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cce545d46b9d0e09349779ce7bd8666d84676f6_2_1380x830.jpeg 2x" data-dominant-color="888C8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1157 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lena_b (2023-11-16 22:15 UTC)

<p>This is very helpful, thank you! When I use this, it does increase the scale like you mentioned, but it appears to translate the segmentation, is this what you would expect?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea3d5eaab99a7ae5bbf7732b3f236762ed21444.jpeg" data-download-href="/uploads/short-url/8W8CoLUyfT7GiIPg8ywSGqmoIrG.jpeg?dl=1" title="Screenshot 2023-11-16 at 5.13.36 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea3d5eaab99a7ae5bbf7732b3f236762ed21444_2_598x500.jpeg" alt="Screenshot 2023-11-16 at 5.13.36 PM" data-base62-sha1="8W8CoLUyfT7GiIPg8ywSGqmoIrG" width="598" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea3d5eaab99a7ae5bbf7732b3f236762ed21444_2_598x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea3d5eaab99a7ae5bbf7732b3f236762ed21444_2_897x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea3d5eaab99a7ae5bbf7732b3f236762ed21444_2_1196x1000.jpeg 2x" data-dominant-color="5B5D6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-16 at 5.13.36 PM</span><span class="informations">1470×1228 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db59f5b56bfd7744b2475129c44a737ef108dcbc.jpeg" data-download-href="/uploads/short-url/vitiQC4UduaiCUEP2PWzjricgws.jpeg?dl=1" title="Screenshot 2023-11-16 at 5.14.25 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db59f5b56bfd7744b2475129c44a737ef108dcbc_2_598x500.jpeg" alt="Screenshot 2023-11-16 at 5.14.25 PM" data-base62-sha1="vitiQC4UduaiCUEP2PWzjricgws" width="598" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db59f5b56bfd7744b2475129c44a737ef108dcbc_2_598x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db59f5b56bfd7744b2475129c44a737ef108dcbc_2_897x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db59f5b56bfd7744b2475129c44a737ef108dcbc_2_1196x1000.jpeg 2x" data-dominant-color="5B5E6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-16 at 5.14.25 PM</span><span class="informations">1470×1228 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2023-11-16 22:23 UTC)

<p>It’s a scale around the origin, so if your segmentation is not centered yes, I would expect it to move.  You can center the volume in the Volume Module Volume Information pane with the Center Volume button first.  Then you can create a segmentation that will be centered (center of the volume will be at the origin.  If you want to control that more you can translate the centered segmentation first so that the center is in the place you want to scale with respect to.</p>

---
