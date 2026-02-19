---
topic_id: 4438
title: "Image Size Formatting"
date: 2018-10-17
url: https://discourse.slicer.org/t/4438
---

# Image size/formatting

**Topic ID**: 4438
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/image-size-formatting/4438

---

## Post #1 by @Michael_Shorofsky (2018-10-17 15:07 UTC)

<p>When I am loading DICOM images into Slicer 4.9 the images are only taking up the bottom corner of the available window. Zooming in does not make the images bigger in the given RYG screens. I am pretty new to this program so any help would be greatly appreciated. Also, when I upload these images in Slicer 4.8 they take up the full boxes. Attached is an image.</p>
<p>Thanks!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29d65f74d8482369b5d77f9e2a451ecbeae9fcf1.jpeg" data-download-href="/uploads/short-url/5Y6ROOCYqw1jg0GdqI7u7Og0hBT.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d65f74d8482369b5d77f9e2a451ecbeae9fcf1_2_690x427.jpeg" alt="Capture" data-base62-sha1="5Y6ROOCYqw1jg0GdqI7u7Og0hBT" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d65f74d8482369b5d77f9e2a451ecbeae9fcf1_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d65f74d8482369b5d77f9e2a451ecbeae9fcf1_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29d65f74d8482369b5d77f9e2a451ecbeae9fcf1_2_1380x854.jpeg 2x" data-dominant-color="74747A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">2736×1697 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-10-17 15:11 UTC)

<p>I’ve never seen this error on Windows (I heard people having similar issues on Mac with earlier version of VTK and Qt).</p>
<p>Have you built Slicer yourself or it is an official release that you’ve downloaded?<br>
Could you try latest nightly version of Slicer?<br>
What is your system configuration?<br>
What graphics card do you have? What is the driver version?<br>
What is the resolution of your monitor?<br>
Do you use any special desktop size scaling setting, virtual desktop, or application compatibility setting?</p>

---

## Post #3 by @Michael_Shorofsky (2018-10-17 22:35 UTC)

<p>Hey,</p>
<p>This is the nightly build that I have been using. The weird part is when I use Slicer 4.8 version it is the normal sizing.</p>

---

## Post #4 by @lassoan (2018-10-18 00:03 UTC)

<p>Could you please answer the questions above? Without that it’s impossible to guess what the issue could be.</p>

---

## Post #5 by @Michael_Shorofsky (2018-10-18 00:20 UTC)

<p>Sorry!</p>
<p>Could you try latest nightly version of Slicer? - Downloaded it about an hour ago it was still showing the same.<br>
What is your system configuration? - Windows 10 Pro 64 Bit Driver Version 24.20.100.6136. Driver Date 5/25/2018<br>
What graphics card do you have? What is the driver version? Intel® HD Graphics 620.<br>
What is the resolution of your monitor? 2736x1824<br>
Do you use any special desktop size scaling setting, virtual desktop, or application compatibility setting?  Nope</p>

---

## Post #6 by @lassoan (2018-10-18 00:51 UTC)

<p>Is this a laptop? What brand/model? Is it connected to external display or multiple displays? Do you use a dock to connect to external monitors?</p>
<p>To resolve the problem, you can adjust application scaling options by right-clicking on Slicer.exe, click Compatibility tab, Change high DPI settings, and try all available options.</p>

---

## Post #7 by @Michael_Shorofsky (2018-10-18 01:13 UTC)

<p>It is a surface pro 2017. And there are no external or dual displays.</p>

---

## Post #8 by @Michael_Shorofsky (2018-10-18 01:23 UTC)

<p>Thanks so much. I was able to get it fixed by changing the DPI in the capability.</p>
<p>Your program is great and I am loving it for our research.</p>
<p>Thanks!</p>

---

## Post #9 by @lassoan (2018-10-18 01:37 UTC)

<p>Thank you.</p>
<p>Which high-DPI option fixed the issue?</p>

---

## Post #10 by @Michael_Shorofsky (2018-10-18 01:49 UTC)

<p>see attached photo. I had to check the box that is checked in the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/3/33c66b5f369303abf84031fdb4366a2fd44ffc77.jpeg" data-download-href="/uploads/short-url/7o1sGoNixqDeiHAXawtYJ3Y3o6r.jpeg?dl=1" title="Capture1.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c66b5f369303abf84031fdb4366a2fd44ffc77_2_667x499.jpeg" width="667" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c66b5f369303abf84031fdb4366a2fd44ffc77_2_667x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c66b5f369303abf84031fdb4366a2fd44ffc77_2_1000x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c66b5f369303abf84031fdb4366a2fd44ffc77.jpeg 2x" data-dominant-color="D4D8DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1.JPG</span><span class="informations">1292×968 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
