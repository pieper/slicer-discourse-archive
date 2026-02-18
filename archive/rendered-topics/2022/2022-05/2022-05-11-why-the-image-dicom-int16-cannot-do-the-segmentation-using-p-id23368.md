# Why the image dicom int16 cannot do the segmentation using PetTumorSegmentation Extension?

**Topic ID**: 23368
**Date**: 2022-05-11
**URL**: https://discourse.slicer.org/t/why-the-image-dicom-int16-cannot-do-the-segmentation-using-pettumorsegmentation-extension/23368

---

## Post #1 by @akmal871026 (2022-05-11 05:13 UTC)

<p>Dear all,</p>
<p>I have data set image dicom SPECT (link as attached). The type is int16. I want to apply the PetTumorSegmentation extension to do the volume segmentation.</p>
<p>But it cannot function well.</p>
<p>Anyone can help?</p>
<p><a href="https://drive.google.com/file/d/1deV8TerFMK8zPm3FoFLzovOQG_UVtu10/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1deV8TerFMK8zPm3FoFLzovOQG_UVtu10/view?usp=sharing</a></p>

---

## Post #2 by @lassoan (2022-05-12 02:44 UTC)

<p>Most DICOM files are int16, so that should not cause any issue.</p>
<p>Which Slicer version are you using?</p>
<p>As I see, PETTumorSegmentation Extension was developed for Slicer-4.6 or around that time. We are now at Slicer-4.13, transitioning to Slicer-5.0. I would recommend to update the extension for current Slicer version. Try to contact the original extension developers first and if they don’t respond then we can guide you through how to do the update.</p>

---

## Post #3 by @akmal871026 (2022-05-12 16:19 UTC)

<p>I Used 4.11 version. On the website is 4.11 version. How to get 4.13 version?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d07092e00dd8f8c64257fb6d31d61b558e3e0fc.png" data-download-href="/uploads/short-url/hQ2KZZASrtQjP5Ud2rsgiTdT8le.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d07092e00dd8f8c64257fb6d31d61b558e3e0fc_2_690x388.png" alt="Untitled" data-base62-sha1="hQ2KZZASrtQjP5Ud2rsgiTdT8le" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d07092e00dd8f8c64257fb6d31d61b558e3e0fc_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d07092e00dd8f8c64257fb6d31d61b558e3e0fc_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d07092e00dd8f8c64257fb6d31d61b558e3e0fc_2_1380x776.png 2x" data-dominant-color="F4F5F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1920×1080 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-05-12 18:14 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="3" data-topic="23368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>I Used 4.11 version.</p>
</blockquote>
</aside>
<p>You also said that you’ve tried the PETTumorSegmentation extension “But it cannot function well”.</p>
<p>Do you mean you installed the extension and something did not work as you expect? Was that with Slicer-4.11?</p>
<p>Or do you mean that you did not find PETTumorSegmentation in the extension manager?</p>

---

## Post #5 by @akmal871026 (2022-05-13 02:07 UTC)

<p>Yah…I mean PetTumorSegmentation was not function as well usually.</p>
<p>Before that, I used very well.</p>

---

## Post #6 by @lassoan (2022-05-13 04:14 UTC)

<p>Sorry, I’m confused. What do you mean by <code>PetTumorSegmentation was not function as well usually</code>?</p>
<p>Have you used PETTumorSegmentation extension? Using what Slicer versions?<br>
With which Slicer version it “functioned well” and with which Slicer version it did not function “as well”? What exactly it did not do correctly?</p>

---

## Post #7 by @akmal871026 (2022-05-16 14:45 UTC)

<p>I already used PetTumorSegmentation extension in 3D Slicer version 4.11. No problem have.</p>
<p>But just used that image, the PetTumorSegmentation cannot do the segmentation</p>

---
