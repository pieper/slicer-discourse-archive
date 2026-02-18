# Problems with files from Visible Human

**Topic ID**: 30018
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/problems-with-files-from-visible-human/30018

---

## Post #1 by @Guido_Resmini (2023-06-13 17:23 UTC)

<p>Version: 5.2.2<br>
OS: Windows 11<br>
Dear all, I’m having problems uploading files (.fro, .fre, .t1, .t2, .pd) downloaded from Visible Human.<br>
Here is a screenshot of the error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68eda920bcf9a8054489d3037ec1a31956e06614.png" alt="Screenshot 2023-06-13 121347" data-base62-sha1="eYeQeHiF4Bcoi8xQQliJ0QFVUXy" width="436" height="217"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3d8036354166a1793a2721095d99b847c58795.png" data-download-href="/uploads/short-url/xZzoYFUa7lqCEy61rXvIT1xHLet.png?dl=1" title="Screenshot 2023-06-13 121613" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3d8036354166a1793a2721095d99b847c58795.png" alt="Screenshot 2023-06-13 121613" data-base62-sha1="xZzoYFUa7lqCEy61rXvIT1xHLet" width="690" height="468" data-dominant-color="393E44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-13 121613</span><span class="informations">761×517 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I’ve also tried to open these files from another PC (with Windows 10) and using older versions of 3D Slicer, but I got the same error. I could only open them using Slicer 4.3.0.<br>
Does anybody have the same problem or know which can be the solution?</p>

---

## Post #2 by @pieper (2023-06-14 13:08 UTC)

<p>The visible human radiology data is in an old GE format that isn’t used much anymore and I guess ITK support is not maintained (Slicer uses ITK for reading these formats).</p>
<p>For now you could save from Slicer 4.3.0 into nrrd to use with newer Slicer.</p>
<p>Also, FYI, these datasets have been converted to DICOM format and are scheduled to be released as part of the Imaging Data Commons in the next few weeks.  You can keep an eye out here and <a class="mention" href="/u/fedorov">@fedorov</a> has said he plans to make an announcement once that data is released.</p>

---

## Post #3 by @fedorov (2023-07-17 21:36 UTC)

<p>Visible Human dataset has been harmonized to standard DICOM and released in NCI Imaging Data Commons in the latest data release. See details here: <a href="https://discourse.canceridc.dev/t/idc-july-2023-release/457" class="inline-onebox">IDC July 2023 release - Announcements - Imaging Data Commons</a>.</p>

---
