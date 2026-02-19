---
topic_id: 38080
title: "Dicom Database View"
date: 2024-08-28
url: https://discourse.slicer.org/t/38080
---

# DICOM Database View 

**Topic ID**: 38080
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/dicom-database-view/38080

---

## Post #1 by @CTuser (2024-08-28 12:27 UTC)

<p>Two Questions:</p>
<ol>
<li>Is there a way to adjust the column width on the DATA → DICOM Database Results page? Right now I can’t see the full date added. I have maximized the the 3D Slicer window and Date Added is still not fully visible (see below).</li>
<li>Can the Date Scan was obtained be added to the view below?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83ae66214e530f7e6056a819db55bf0ba02dae0d.png" data-download-href="/uploads/short-url/iMUcbUqBqhqwozlvqJ717zfObnf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ae66214e530f7e6056a819db55bf0ba02dae0d_2_690x233.png" alt="image" data-base62-sha1="iMUcbUqBqhqwozlvqJ717zfObnf" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ae66214e530f7e6056a819db55bf0ba02dae0d_2_690x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ae66214e530f7e6056a819db55bf0ba02dae0d_2_1035x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83ae66214e530f7e6056a819db55bf0ba02dae0d.png 2x" data-dominant-color="F8F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1274×431 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-08-28 13:15 UTC)

<ol>
<li>The interaction is maybe not obvious but if you drag the spacer between the column header on the right and the scroll bar you can make the <code>Date added</code> field wider.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65a338a498cba0ed4dc2296b7b3853b6d5ec336.png" alt="image" data-base62-sha1="z9kIdufsJRe92psXdc943nYN98a" width="104" height="56"></p>
<ol start="2">
<li>The <code>Study date</code> is the day of the scan as recorded in the dicom header.</li>
</ol>

---
