---
topic_id: 34487
title: "Fixing Image Spacing For Ultrasound Images"
date: 2024-02-23
url: https://discourse.slicer.org/t/34487
---

# Fixing image spacing for ultrasound images

**Topic ID**: 34487
**Date**: 2024-02-23
**URL**: https://discourse.slicer.org/t/fixing-image-spacing-for-ultrasound-images/34487

---

## Post #1 by @Arian_Amini (2024-02-23 02:51 UTC)

<p>Hello,</p>
<p>I recently began using 3D Slicer to measure ultrasound images, but the ruler isn’t at a 1:1 scale with the ultrasound images (see attached). Other forum posts state that this is an image spacing issue that can be fixed in the “Volume Information” tab, but I’m unsure on how I would determine the correct spacing. Would there also be a way to automate this or not need to do it for every image I work with? I would appreciate any help on this.</p>
<p>Thank you,<br>
Arian</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8598c04ad1d690ccc99b78d59e69667daa77cbc.jpeg" data-download-href="/uploads/short-url/uRUZchaf5vzoQ58K4TjFKJgBL7m.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8598c04ad1d690ccc99b78d59e69667daa77cbc_2_656x500.jpeg" alt="image" data-base62-sha1="uRUZchaf5vzoQ58K4TjFKJgBL7m" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8598c04ad1d690ccc99b78d59e69667daa77cbc_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8598c04ad1d690ccc99b78d59e69667daa77cbc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8598c04ad1d690ccc99b78d59e69667daa77cbc.jpeg 2x" data-dominant-color="1D1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">806×614 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-02-23 02:56 UTC)

<p>Do you read the image from DICOM or you load screenshots from jpg/png/tiff files?</p>

---

## Post #3 by @Arian_Amini (2024-02-23 03:41 UTC)

<p>I load them as a JPG, and then save them as a NRRD file, and then I open the NRRD file and work on that.</p>

---

## Post #4 by @David_Clunie (2024-02-25 14:40 UTC)

<p>In traditional DICOM Ultrasound images, since different areas of the screen image may have different information, the pixel size information is specific to “regions” and, if present at all, may be in the <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.5.5.html" rel="noopener nofollow ugc">US Region Calibration Module</a>, specifically in PhysicalDeltaX and PhysicalDeltaY, with corresponding units in PhysicalUnitsXDirection and PhysicalUnitsYDirection.</p>

---

## Post #5 by @lassoan (2024-02-26 03:37 UTC)

<p><a class="mention" href="/u/arian_amini">@Arian_Amini</a> How did you acquire the jpegs: took screenshots, exported from DICOM, …?</p>

---

## Post #6 by @Arian_Amini (2024-03-08 19:46 UTC)

<p>I apologize for the long delay in responding. I have been away the past 2 weeks. I am actually unsure how the jpeg files are obtained. Someone else operates the US and the images are shared with us as JPEG files. I can ask them about that if that would be helpful. Sorry for the lack of info</p>

---

## Post #7 by @lassoan (2024-03-08 20:21 UTC)

<p>The best would be to get the ultrasound images in DICOM format. Those files store the correct image spacing.</p>

---

## Post #8 by @Arian_Amini (2024-03-08 20:24 UTC)

<p>Ok got it, I’ll try to get my hands on them. In the case that wouldn’t be possible, would I be out of luck or would there still be a possible solution? Thanks for all your help thus far!</p>

---

## Post #9 by @lassoan (2024-03-08 22:04 UTC)

<p>You can compute scale factor by dividing the size of the depth marker line in physical size (as shown in the image) by the line length indicated by the line markup. Then use this value in the first two diagonal value of a transformation matrix (in Transforms module).</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Is there a module for this in SlicerMorph extension?</p>

---

## Post #10 by @Arian_Amini (2024-03-08 22:22 UTC)

<p>Perfect, thank you so much Andras! It seems like I’ll be able to acquire the DICOM files anyways, so hopefully the issue will resolve itself once I start working with those. I appreciate your help.</p>

---

## Post #11 by @muratmaga (2024-03-08 22:35 UTC)

<p>No,</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="34487">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Is there a module for this in SlicerMorph extension?</p>
</blockquote>
</aside>
<p>No, it is simple enough with length tool and python console as calculator, we didn’t bother…</p>

---
