---
topic_id: 5858
title: "Registration Of Mri To Ct For The Spine"
date: 2019-02-20
url: https://discourse.slicer.org/t/5858
---

# Registration of MRI to CT for the Spine

**Topic ID**: 5858
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/registration-of-mri-to-ct-for-the-spine/5858

---

## Post #1 by @triple_axel (2019-02-20 22:25 UTC)

<p>Hi, sorry to bother you all again. I have to registered the T1 to T2 scans just fine using the Brainsfit Module, however with regards of T2 to CT scans I am having a bit of trouble.<br>
I already used “Fudicial Registration” to get initial allignment for the registration, but when I attempt to use non-deformable registration it seems like the scans automatically get cropped. (This occurs in a multitued of the other registration phases as well) and the scans are not as alligned as I want them to be.</p>
<p>I was wondering if there are any resources for spine registration? Or what parameter needs to be changed so at least the entire scan is not cropped to a specific location in the spine.</p>
<p>Original:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a56d58c4dcfb9a1afc9aaaded8648b22628ea6f.jpeg" data-download-href="/uploads/short-url/aBDnciWzkuSFBYZN9ArHMfIKqBx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a56d58c4dcfb9a1afc9aaaded8648b22628ea6f_2_647x500.jpeg" alt="image" data-base62-sha1="aBDnciWzkuSFBYZN9ArHMfIKqBx" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a56d58c4dcfb9a1afc9aaaded8648b22628ea6f_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a56d58c4dcfb9a1afc9aaaded8648b22628ea6f_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a56d58c4dcfb9a1afc9aaaded8648b22628ea6f_2_1294x1000.jpeg 2x" data-dominant-color="424242"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1807×1395 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After Registration:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/067c7857a01d8648c76de8e60ffd3d0ac31a0af3.jpeg" data-download-href="/uploads/short-url/VnxwETx0QRa31xdlGv7UB8AP3J.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067c7857a01d8648c76de8e60ffd3d0ac31a0af3_2_655x499.jpeg" alt="image" data-base62-sha1="VnxwETx0QRa31xdlGv7UB8AP3J" width="655" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067c7857a01d8648c76de8e60ffd3d0ac31a0af3_2_655x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067c7857a01d8648c76de8e60ffd3d0ac31a0af3_2_982x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/067c7857a01d8648c76de8e60ffd3d0ac31a0af3_2_1310x998.jpeg 2x" data-dominant-color="313130"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1826×1392 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @RICARDO_GUIMARAES (2019-12-16 02:37 UTC)

<p>Hi triple_axel,<br>
Did you solve this problem with registration?<br>
I´m having the same issue in version 4.11.0<br>
authought I sucessfuly performed a landmark registration in ver 4.8<br>
impossible to register with fiducials…<br>
How do you aquire yor MRI images?<br>
tks</p>

---

## Post #3 by @lassoan (2019-12-16 22:20 UTC)

<p>You can use latest stable or preview release (currently 4.10 or 4.11). Do not use anything older.</p>
<p>Landmark registration always works (I would recommend Fiducial registration wizard module in SlicerIGT extension), but it requires some effort to place the points accurately.</p>
<p>Ifnyou segment vertebrae, then you can use Segment Registration extension to compute transforms based on that</p>
<p>Intensity-based automatic image registration (e.g., SlicerElastix) should work well, too, but you may need a reasonable initial alignment (less than 10mm and 10 deg error) and images need to be cropped to approximately the same anatomical region.</p>
<p>Probably the best is to combine methods: do initial approximate alignment using landmark registration, then crop the images to the region of interest and register using Elastix. If this works well then you can write a simple scripted module that automates these steps, so that you don’t need to click many times and switch between several volumes.</p>

---
