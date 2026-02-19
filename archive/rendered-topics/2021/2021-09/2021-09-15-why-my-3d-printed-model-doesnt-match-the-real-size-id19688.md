---
topic_id: 19688
title: "Why My 3D Printed Model Doesnt Match The Real Size"
date: 2021-09-15
url: https://discourse.slicer.org/t/19688
---

# Why my 3D-printed model doesn't match the real size?

**Topic ID**: 19688
**Date**: 2021-09-15
**URL**: https://discourse.slicer.org/t/why-my-3d-printed-model-doesnt-match-the-real-size/19688

---

## Post #1 by @arezoo.movahed (2021-09-15 18:24 UTC)

<p>Hello,<br>
I remodel a human heart, actually I used my Mom’s CT Angiography data, and after segmentation, I exported a stl file and 3D-Print it.<br>
But the model is so big and doesn’t match the real size.<br>
I was wondering what should be done before exporting the stl file to have the real size?<br>
Your prompt response is highly appreciated.<br>
Sincerely,<br>
Arezoo</p>

---

## Post #2 by @lassoan (2021-09-15 18:27 UTC)

<p>The STL files that Slicer creates from DICOM CT files uses millimeter as unit by default. You can change that by specifying a custom “Size scale” in the “Export segments to files” window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29726b60be4928b228bf207ce71adc8d02f780fa.png" data-download-href="/uploads/short-url/5UEIz8Bah999dMNVZqTuYYjrVy2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29726b60be4928b228bf207ce71adc8d02f780fa.png" alt="image" data-base62-sha1="5UEIz8Bah999dMNVZqTuYYjrVy2" width="567" height="500" data-dominant-color="F2F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×606 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want the file to contain coordinate values in meter then set size scale to 0.001.</p>
<p>Make sure that you chose the corresponding unit in your 3D printing software.</p>

---
