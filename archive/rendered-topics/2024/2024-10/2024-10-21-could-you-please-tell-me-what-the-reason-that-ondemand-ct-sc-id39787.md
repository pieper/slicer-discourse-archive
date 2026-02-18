# Could you please tell me what the reason that Ondemand CT scan files (DCM) are not readable by a slicer?

**Topic ID**: 39787
**Date**: 2024-10-21
**URL**: https://discourse.slicer.org/t/could-you-please-tell-me-what-the-reason-that-ondemand-ct-scan-files-dcm-are-not-readable-by-a-slicer/39787

---

## Post #1 by @AlinaPanowa11 (2024-10-21 23:36 UTC)

<p>Good afternoon. Could you please tell me what the reason that Ondemand CT scan files (DCM) are not readable by a slicer? When uploading images, I only get the starting image.</p>

---

## Post #2 by @lassoan (2024-10-21 23:40 UTC)

<p>Ondemand scanners generate invalid DICOM files. See details in this topic:</p>
<aside class="quote quote-modified" data-post="4" data-topic="28870">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/patientname-and-rus-language-trouble/28870/4">PatientName and rus language - trouble</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The DICOM files have multiple sever DICOM non-conformities. The most serious are: 


CharacterSet is not saved in the file. It seems that the file uses Windows-1251 code page, which is not even a valid DICOM character set.

XRayTubeCurrent field is stored incorrectly (it must be an integer value, the value is 4.1 - see <a href="http://dclunie.blogspot.com/2008/11/dicom-exposure-attribute-fiasco.html" class="inline-onebox">David Clunie's Blog: The DICOM Exposure attribute fiasco</a>)

There are also some incorrectly generated UIDs. 
I would recommend to contact your device manufacturer and report these …
  </blockquote>
</aside>

<p>Please report the issues to the manufacturer. Until the manufacturer fixes its software you can use the workaround described in that topic.</p>

---

## Post #3 by @AlinaPanowa11 (2024-10-22 10:47 UTC)

<p>Thank you. I will try.</p>

---
