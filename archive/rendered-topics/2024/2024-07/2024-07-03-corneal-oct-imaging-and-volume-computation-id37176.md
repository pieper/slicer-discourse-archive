---
topic_id: 37176
title: "Corneal Oct Imaging And Volume Computation"
date: 2024-07-03
url: https://discourse.slicer.org/t/37176
---

# Corneal OCT imaging and volume computation

**Topic ID**: 37176
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/corneal-oct-imaging-and-volume-computation/37176

---

## Post #1 by @Roman_Chudzinski (2024-07-03 13:36 UTC)

<p>Hello, i’m new to using 3DSlicer and want some advice to know if my project is doable.</p>
<p>I want to use optical coherence tomography of the cornea to estimate the volume of a region of interest. I want to do a manual contouring of the region of interest in each 2D image and use 3D slicer to estimate the volume.</p>
<p>I would like to export images from a CASIA2 ( Tomey ) or Anterion ( Heidelberg engineering).</p>
<p>Does some of have any advices ? Have ever work with this kind of images ?</p>
<p>Thank you for you help.</p>

---

## Post #2 by @lassoan (2024-07-03 13:43 UTC)

<p>Yes, these should be all doable in Slicer.</p>
<p>If you install the <code>Sandbox</code> extension then Slicer will be able to load OCT files. By default, only Topcon OCT image (<code>.fda</code>) files are recognized, but by changing <a href="https://github.com/PerkLab/SlicerSandbox/blob/c8ddc755e602f518a049c1f2070aa3b15a4396d4/ImportOCT/ImportOCT.py#L42">this</a> line you can enable other file types as well (for example Heidelberg). You can find the list of all supported formats in the <a href="https://pypi.org/project/oct-converter/">oct-converter</a> project page.</p>
<p>If you provide a sample image (upload to dropbox, onedrive, etc. and post the link here) then we can make sure the Slicer can properly read the file.</p>

---

## Post #3 by @Roman_Chudzinski (2024-07-21 17:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="37176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>e (upload to dropbox, onedrive, etc. and post the link here) then we can make sure the Slicer can properly</p>
</blockquote>
</aside>
<p>Hello, thank you very much for you answer.</p>
<p>I’ve been working on it, i did download sandbox and modify the oct-converter line.</p>
<p>For the anterion i did export it as DICOM file from the device. I manage to open it with slicer but with an error. There is no geometry provided. It’s radial images from the cornea ( and whole anterior segment).</p>
<p>For the CASIA2, despite the sand box i can’t open it. It’s .casia2 files.</p>
<p>Here is a weetransfert with test images</p>
<p><a href="https://we.tl/t-jlK3kzHPAo?utm_campaign=TRN_TDL_05&amp;utm_source=sendgrid&amp;utm_medium=email&amp;trk=TRN_TDL_05" rel="noopener nofollow ugc">https://we.tl/t-jlK3kzHPAo</a></p>
<p>Thank you<br>
Roman</p>

---
