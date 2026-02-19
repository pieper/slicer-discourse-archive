---
topic_id: 2570
title: "Align Two Segments To Each Other"
date: 2018-04-12
url: https://discourse.slicer.org/t/2570
---

# align two segments to each other 

**Topic ID**: 2570
**Date**: 2018-04-12
**URL**: https://discourse.slicer.org/t/align-two-segments-to-each-other/2570

---

## Post #1 by @katharina_hecker (2018-04-12 13:29 UTC)

<p>Operating system: Windows<br>
Slicer version:4.9<br>
Expected behavior: align the size of two segments to each other<br>
Actual behavior: when i wanted to try to set the same size parameters for two different volumes the image dimensions could not be changed, so that the following created segments had different sizes. It is very time consuming and inaccurate to align them with the transformation matrix. Is there another way to set the parameters/dimensions, so that I can integrate one of them in the other?</p>

---

## Post #2 by @cpinter (2018-04-12 14:52 UTC)

<p>I can only guess what you’re trying to do exactly, so can you please give us more information? Such as</p>
<ul>
<li>Do you segment one anatomical image or more? If you segment more are they from the acquisition or modality?</li>
<li>Are you trying to register two different segmentations, or you have a problem with the geometry of the images that represent the segments?</li>
</ul>

---

## Post #3 by @katharina_hecker (2018-04-12 15:08 UTC)

<p>Thanks for your reply!!!<br>
I am segmenting for each segment an image sequence. They are from acquisition…<br>
The images of those two image sequences are different in size. What I´m doing is: I´m creating out of those image sequences with ‘segment editor’ two segments. But it is hard to increase the properties of the first segment and align this perfectly to the size of the second segment (the first segment is just a part of the second segment (organ in body…)</p>

---

## Post #4 by @lassoan (2018-04-12 15:33 UTC)

<p>Registration using transform slider is certainly very hard. Fortunately, there are several other registration tools in Slicer that can be applicable. For example:</p>
<ul>
<li>Segment registration module (in Segment registration extension): Fully automatic registration between two segments. Supports both rigid and deformable transforms.</li>
<li>Fiducial registration wizard (in SlicerIGT extension): Landmark-based registration (you need to manually identify corresponding landmarks in the images).</li>
<li>Model registration (in SlicerIGT extension): Iterative closest point (ICP) based fully automatic rigid registration. You need to export segments to models (using Segmentations module), as this module expects model nodes as input. ICP can stuck into local minimum, so this method requires the segments to be already somewhat aligned when you start the registration.</li>
</ul>

---

## Post #5 by @katharina_hecker (2018-04-12 15:37 UTC)

<p>Thank you very much for your help!</p>

---

## Post #6 by @katharina_hecker (2018-04-12 15:49 UTC)

<p>Unfortunately I can´t find in Extensions the Segment registration module, can you maybe help me to get there?</p>

---

## Post #7 by @lassoan (2018-04-12 15:52 UTC)

<p>I’ve just checked and it is available for latest stable (Slicer-4.8.1), in Registration category.</p>

---

## Post #8 by @katharina_hecker (2018-04-12 15:58 UTC)

<p>Is it maybe also available for 4.9?</p>

---

## Post #9 by @cpinter (2018-04-12 16:05 UTC)

<p>Unfortunately the factory builds for 4.9 are down for a few days now. Also there is a Windows build system bug that prevents building extensions depending on other extensions (such as SegmentRegistration on SlicerRT) if there is one or more failing test in the extension, and this is why there are no SegmentRegistration builds for a while.</p>
<p>I can try to find you a successful build from the recent past, or I can do a custom build for you, it’s quite easy.</p>

---

## Post #10 by @lassoan (2018-04-12 16:07 UTC)

<p>In the meantime, you can do the registration in Slicer-4.8.1, save the result, and load it into 4.9.x.</p>

---

## Post #11 by @katharina_hecker (2018-04-12 17:04 UTC)

<p>Good, thank you for your help!</p>

---

## Post #12 by @cpinter (2018-04-12 18:13 UTC)

<p>I made a custom installer with a recent 4.9</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/7zj4lrcizq2invk/AACtTi0Y2y_Fv4Ky1TFhEDXXa?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/7zj4lrcizq2invk/AACtTi0Y2y_Fv4Ky1TFhEDXXa?dl=0" target="_blank" rel="noopener">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/7zj4lrcizq2invk/AACtTi0Y2y_Fv4Ky1TFhEDXXa?dl=0" target="_blank" rel="noopener">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Install Slicer, then install the extensions (SegmentRegistration last) in Extension Manager with the wrench icon in the top right. Make sure you wait a bit until it says the extension is installed, sometimes the message comes prematurely.</p>

---

## Post #13 by @katharina_hecker (2018-04-13 04:26 UTC)

<p>Thank you very much!</p>

---

## Post #14 by @stevenagl12 (2019-08-19 13:21 UTC)

<p>Is there any module that supports non-rigid ICP registration? Or something like parametric non-rigid registration with gaussian processes?</p>

---

## Post #15 by @lassoan (2019-08-19 14:04 UTC)

<p>Segment Registration extension supports non-linear warping (based on b-spline registration of distance maps). We tried various approaches and this worked the best for our applications. It was <a href="http://perk.cs.queensu.ca/contents/open-source-image-registration-mri-trus-fusion-guided-prostate-interventions" rel="nofollow noopener">tested extensively on prostate US/MRI registration</a>, <a href="http://perk.cs.queensu.ca/contents/validation-mri-us-registration-focal-hdr-prostate-brachytherapy-treatment" rel="nofollow noopener">used successfully in clinical work</a>, and worked surprisingly well for other applications, too.</p>

---
