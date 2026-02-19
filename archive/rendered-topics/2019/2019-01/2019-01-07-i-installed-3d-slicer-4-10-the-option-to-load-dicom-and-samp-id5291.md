---
topic_id: 5291
title: "I Installed 3D Slicer 4 10 The Option To Load Dicom And Samp"
date: 2019-01-07
url: https://discourse.slicer.org/t/5291
---

# i installed 3d slicer 4.10. the option to load DICOM and sample data do not work

**Topic ID**: 5291
**Date**: 2019-01-07
**URL**: https://discourse.slicer.org/t/i-installed-3d-slicer-4-10-the-option-to-load-dicom-and-sample-data-do-not-work/5291

---

## Post #1 by @ali_adib (2019-01-07 02:54 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-01-07 02:56 UTC)

<p>Make sure your temporary folder is writeable, does not have special characters in its name, and you have enough space there. You can change temporary folder location in menu: Edit / Application Settings / Modules / Temporary directory.</p>

---

## Post #3 by @ali_adib (2019-01-07 09:53 UTC)

<p>thank you for your feedback</p>
<p>i still have the same problem although i installed the program again.</p>
<p>attached 2 screenshot of the error massages.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/f/fde9af5e2a9b1a42e9f5d8c93d807b703467a40b.jpeg" data-download-href="/uploads/short-url/Aedt0zUZDekG5ZHO21atcTNhA1l.jpeg?dl=1" title="DICOM.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fde9af5e2a9b1a42e9f5d8c93d807b703467a40b_2_690x215.jpeg" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fde9af5e2a9b1a42e9f5d8c93d807b703467a40b_2_690x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fde9af5e2a9b1a42e9f5d8c93d807b703467a40b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fde9af5e2a9b1a42e9f5d8c93d807b703467a40b.jpeg 2x" data-dominant-color="909091"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOM.JPG</span><span class="informations">942×294 31.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/c/c3e5808802127cdbe22d727bff8ef556c174d5c8.jpeg" data-download-href="/uploads/short-url/rWYOnT70IpnwdHdlQbctqTbVdmU.jpeg?dl=1" title="sample data.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3e5808802127cdbe22d727bff8ef556c174d5c8_2_690x214.jpeg" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3e5808802127cdbe22d727bff8ef556c174d5c8_2_690x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3e5808802127cdbe22d727bff8ef556c174d5c8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3e5808802127cdbe22d727bff8ef556c174d5c8.jpeg 2x" data-dominant-color="8C8C8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample data.JPG</span><span class="informations">1009×313 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2019-01-07 13:38 UTC)

<p>It looks like something is wrong with the installation.  Have a look in the log file for clues (look in the Help -&gt; Report a bug menu).</p>

---
