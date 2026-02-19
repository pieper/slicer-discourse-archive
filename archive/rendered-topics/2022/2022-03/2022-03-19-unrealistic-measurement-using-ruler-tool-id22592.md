---
topic_id: 22592
title: "Unrealistic Measurement Using Ruler Tool"
date: 2022-03-19
url: https://discourse.slicer.org/t/22592
---

# Unrealistic measurement using Ruler tool

**Topic ID**: 22592
**Date**: 2022-03-19
**URL**: https://discourse.slicer.org/t/unrealistic-measurement-using-ruler-tool/22592

---

## Post #1 by @Diana_Song (2022-03-19 00:05 UTC)

<p>Hello,<br>
I’m still very new to 3D slicer, and am trying to use the ruler tool to measure the size of the lymph nodes on 2D breast mammograms. The measurements were unrealistically large (like 100-500mm +, which is 10 cms). I’m wondering if there’s anything I did wrong. The mammograms are from a public dataset and are digitalized film mammograms.</p>
<p>Many thanks,<br>
Diana</p>

---

## Post #2 by @ebrahim (2022-03-19 01:29 UTC)

<p>It sounds like a problem with image spacing. If you right click on the volume node and click on “Edit Properties” then this will take you to the Volumes module. There you can expand the “Volume Information” and inspect the spacing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ac4775f5a8fc418f9f35f22f89389f58082bba5.png" data-download-href="/uploads/short-url/hw3b49caRz1lslnZsKy8EU9KcCx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ac4775f5a8fc418f9f35f22f89389f58082bba5_2_526x500.png" alt="image" data-base62-sha1="hw3b49caRz1lslnZsKy8EU9KcCx" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ac4775f5a8fc418f9f35f22f89389f58082bba5_2_526x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ac4775f5a8fc418f9f35f22f89389f58082bba5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ac4775f5a8fc418f9f35f22f89389f58082bba5.png 2x" data-dominant-color="E4E3E2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">625×594 59.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Diana_Song (2022-03-22 01:49 UTC)

<p>Hi Ebrahim,</p>
<p>Thank you so much for the direction. I checked the volume information and they are all 0mm in the image origin. Does this look odd to you? Is there a way to look up how to modify any of these to get the correct spacing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad3e01920661ebfae81189b8ab92413e48b7e33.jpeg" data-download-href="/uploads/short-url/1xMImQfHDxGI1SVNw2X86oexx9F.jpeg?dl=1" title="Screen Shot 2022-03-21 at 9.44.55 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ad3e01920661ebfae81189b8ab92413e48b7e33_2_690x364.jpeg" alt="Screen Shot 2022-03-21 at 9.44.55 PM" data-base62-sha1="1xMImQfHDxGI1SVNw2X86oexx9F" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ad3e01920661ebfae81189b8ab92413e48b7e33_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ad3e01920661ebfae81189b8ab92413e48b7e33_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ad3e01920661ebfae81189b8ab92413e48b7e33_2_1380x728.jpeg 2x" data-dominant-color="404040"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-03-21 at 9.44.55 PM</span><span class="informations">1920×1014 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Many thanks!</p>

---

## Post #5 by @muratmaga (2022-03-22 03:01 UTC)

<p>It is the image spacing tab you need to pay attention to. It is reporting 1mm for each axis. I am not familiar with US modality to know whether that’s too large or not.</p>

---

## Post #6 by @Diana_Song (2022-03-22 14:16 UTC)

<p>Thank you for helping!<br>
It turns out the DICOM file didn’t have the information on the image spacing so Slicer is using the default of 1mm I guess.</p>

---

## Post #7 by @DIV (2022-03-24 03:32 UTC)

<aside class="quote no-group" data-username="Diana_Song" data-post="1" data-topic="22592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diana_song/48/14713_2.png" class="avatar"> Diana_Song:</div>
<blockquote>
<p>mammograms are from a public dataset</p>
</blockquote>
</aside>
<p>To confirm the issue, you could also consider posting a link or a sample.<br>
—DIV</p>

---

## Post #8 by @lassoan (2022-03-25 22:37 UTC)

<p>Pixel spacing cannot be defined for images that are acquired with a cone-beam projection (such as a mammogram, which is acquired by single X-ray point source and a planar detector), because the spacing depends on distance from the source. Objects that are closer to the generator will appear larger.</p>
<p>If the image contains source to image distance, detector size, and source to object distance then you can compute some approximate spacing. If you need more accurate spacing then you need to have a calibration object (any object of known physical size) in approximately the same image plane  as your object that you want to measure.</p>
<p>Still, the measurements may be inaccurate due to foreshortening: an elongated object may be actually longer than it looks in the projection image if it is not parallel to the image plane.</p>
<p>Moreover, mammograms are also most often acquired with strong tissue compression, which unpredictably deforms tissues depending on their stiffness.</p>
<p>For accurate size measurements you would need to use DBT, MRI, or CT imaging instead of simple 2D mammograms.</p>

---
