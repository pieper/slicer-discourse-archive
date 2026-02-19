---
topic_id: 5101
title: "Weird Behaviour When Loading Us Dicom"
date: 2018-12-17
url: https://discourse.slicer.org/t/5101
---

# Weird behaviour when loading US dicom

**Topic ID**: 5101
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/weird-behaviour-when-loading-us-dicom/5101

---

## Post #1 by @eddyogi (2018-12-17 03:01 UTC)

<p>Hello guys.  I’m new to 3dSlicer and I’m trying to work on my wife’s US.  I tried following tutorials which got me to load the dicom files.  Firstly I couldn’t load the dicom file using the dicom button and I am getting an error “Reference image in series does not contain geometry information, etc”  I am able to load the dicom directly by dragging and dropping but then I get this (please see attached photo).  What could be wrong here?  I’m assuming its the dicom file that is incorrect.  Is there a setting needed when saving the dicom file?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c995ac31cfb849e3915dd72d82e1477c68d84c6.jpeg" data-download-href="/uploads/short-url/mll2QJnlTQ29KrBB2woes5uljN4.jpeg?dl=1" title="3dSlicerScreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c995ac31cfb849e3915dd72d82e1477c68d84c6_2_690x388.jpeg" alt="3dSlicerScreenshot" data-base62-sha1="mll2QJnlTQ29KrBB2woes5uljN4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c995ac31cfb849e3915dd72d82e1477c68d84c6_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c995ac31cfb849e3915dd72d82e1477c68d84c6_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c995ac31cfb849e3915dd72d82e1477c68d84c6_2_1380x776.jpeg 2x" data-dominant-color="6F7C80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dSlicerScreenshot</span><span class="informations">1920×1080 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/1127b4485da8ab39eca784eeb5a30d9b3f83cd22.jpeg" data-download-href="/uploads/short-url/2rLbl86iNd6IDkkAd9VMSk0fNbI.jpeg?dl=1" title="3dSlicerScreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1127b4485da8ab39eca784eeb5a30d9b3f83cd22_2_690x388.jpeg" alt="3dSlicerScreenshot" data-base62-sha1="2rLbl86iNd6IDkkAd9VMSk0fNbI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1127b4485da8ab39eca784eeb5a30d9b3f83cd22_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1127b4485da8ab39eca784eeb5a30d9b3f83cd22_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1127b4485da8ab39eca784eeb5a30d9b3f83cd22_2_1380x776.jpeg 2x" data-dominant-color="6F7C80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dSlicerScreenshot</span><span class="informations">1920×1080 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-12-17 13:57 UTC)

<p>JPEG-compressed ultrasound sequences are unfortunately loaded with incorrect colors, if needed, we can provide script to fix the colors.</p>
<p>2D image sequence is loaded as a 3D image stack when using Add data interface, that’s why you see those patterns in yellow and green slice views.</p>
<p>What you would like to do with these ultrasound images?</p>

---

## Post #3 by @eddyogi (2018-12-20 13:49 UTC)

<p>Thank you for the reply.  I want to create a model for 3d printing.  I was able to get a new dicom data set and the sonographer saved the dicom data with and without a render (no idea what she meant) but I hope one of them will work.</p>

---
