# Downsampling NRRDs prior to importation?

**Topic ID**: 23004
**Date**: 2022-04-18
**URL**: https://discourse.slicer.org/t/downsampling-nrrds-prior-to-importation/23004

---

## Post #1 by @chris (2022-04-18 21:03 UTC)

<p>Operating system: Windows 10 Enterprise Version 21H2 with 128 GB of installed RAM<br>
Slicer version: 4.11.20210226<br>
Expected behavior: I am working on a geometric morphometrics project with micro-CT scans of fish skeletons. I am trying to increase the resolution so that I can proceed with anatomical landmarks, but I cannot find a way to downsample the images prior to importation. I checked on the 3D Slicer Documentation and one suggestion is to use the Resize Image (BRAINS) module to downsample the fish scans. However, I am new to 3D Slicer and I cannot find any tutorials which explain how to downsample nrrd files prior to importation. I have attached below two screenshots, the one on the top is the desired resolution and the one on the bottom is the current resolution.<br>
Thanks,<br>
Christian<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17a92d9a6e8e1a9377a59ee09dce94eceb2a8e4e.jpeg" data-download-href="/uploads/short-url/3njrxVcidVaiJegOLaW5vA82hoa.jpeg?dl=1" title="Fish-CT-Scan-standard-headshot (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17a92d9a6e8e1a9377a59ee09dce94eceb2a8e4e_2_690x349.jpeg" alt="Fish-CT-Scan-standard-headshot (1)" data-base62-sha1="3njrxVcidVaiJegOLaW5vA82hoa" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17a92d9a6e8e1a9377a59ee09dce94eceb2a8e4e_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/17a92d9a6e8e1a9377a59ee09dce94eceb2a8e4e_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17a92d9a6e8e1a9377a59ee09dce94eceb2a8e4e.jpeg 2x" data-dominant-color="403830"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fish-CT-Scan-standard-headshot (1)</span><span class="informations">1137×576 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90f98da849a145ee179b80324b8d8f259801bba1.png" data-download-href="/uploads/short-url/kGvq7Azbk18E5FN3GxruwP22ZFf.png?dl=1" title="Capture 04 18 2022" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90f98da849a145ee179b80324b8d8f259801bba1_2_690x376.png" alt="Capture 04 18 2022" data-base62-sha1="kGvq7Azbk18E5FN3GxruwP22ZFf" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90f98da849a145ee179b80324b8d8f259801bba1_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90f98da849a145ee179b80324b8d8f259801bba1_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/90f98da849a145ee179b80324b8d8f259801bba1_2_1380x752.png 2x" data-dominant-color="BBBDDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture 04 18 2022</span><span class="informations">1920×1048 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-04-18 22:17 UTC)

<p>The <code>unu</code> utility is very powerful for this kind of task.  You can use the <code>resample</code> subcommand.</p>
<p><a href="http://teem.sourceforge.net/unrrdu/" class="onebox" target="_blank" rel="noopener">http://teem.sourceforge.net/unrrdu/</a></p>

---

## Post #3 by @muratmaga (2022-10-28 02:40 UTC)

<aside class="quote no-group" data-username="chris" data-post="1" data-topic="23004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/958977/48.png" class="avatar"> chris:</div>
<blockquote>
<p>have attached below two screenshots, the one on the top is the desired resolution and the one on the</p>
</blockquote>
</aside>
<p>İf you want rendering look like this, change the rendering technique to composite with shading from MİP.</p>

---
