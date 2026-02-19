---
topic_id: 3956
title: "Warning Plugin Failed Dicomtid1500Plugin See Python Console"
date: 2018-08-31
url: https://discourse.slicer.org/t/3956
---

# Warning: Plugin failed: DICOMTID1500Plugin See python console for error message

**Topic ID**: 3956
**Date**: 2018-08-31
**URL**: https://discourse.slicer.org/t/warning-plugin-failed-dicomtid1500plugin-see-python-console-for-error-message/3956

---

## Post #1 by @TingtingYu (2018-08-31 03:08 UTC)

<p>Hi,</p>
<p>I tried to import a folder with DICOM images. One of the DICOM image named StrctrSets.dcm cannot be loaded individually. I opened the DICOM module, then I chose one patient, one study, and clicked advanced and examine button. Then I got this. Would you mind explaining what that means and how to fix it?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a047ff6d96c9158e6767f39f540182deb74d9dc.png" alt="image" data-base62-sha1="cQkC1jSJk6ig3R9NjDidSZMbyOM" width="273" height="107"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5590f2f0deae21e92d255965c23f7700a651d723.png" data-download-href="/uploads/short-url/ccX8tIk1zVLjmdnGDNJiIZoJWfx.png?dl=1" title="%E6%8D%951" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5590f2f0deae21e92d255965c23f7700a651d723_2_690x92.png" alt="%E6%8D%951" data-base62-sha1="ccX8tIk1zVLjmdnGDNJiIZoJWfx" width="690" height="92" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5590f2f0deae21e92d255965c23f7700a651d723_2_690x92.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5590f2f0deae21e92d255965c23f7700a651d723_2_1035x138.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5590f2f0deae21e92d255965c23f7700a651d723_2_1380x184.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E6%8D%951</span><span class="informations">1427×191 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @lassoan (2018-08-31 05:00 UTC)

<p>You don’t need DICOMTID1500Plugin for loading RT structure sets and CTs, so you can safely ignore the error. If the error is annoying then you can disable this plugin (in the list above Load button) or uninstall Reporting extension. If you don’t use the latest nightly version of Slicer, then try that, the TID importer error might have been fixed already.</p>

---

## Post #3 by @TingtingYu (2018-08-31 09:05 UTC)

<p>Hi Andras,</p>
<p>Thank you for your quick reply. I tried the latest nightly version but still have the some problem. Although this issue is not that matter for loading RT structure sets and CTs, I am still wondering why StrctrSets.dcm cannot be loaded individually and what is TID, is this a extension?</p>
<p>Best,<br>
Tingting</p>

---

## Post #4 by @lassoan (2018-08-31 12:07 UTC)

<p><a href="http://dicom.nema.org/medical/dicom/current/output/html/part16.html#sect_TID_1500">TID1500</a> is a DICOM structured report template that Slicer’s reporting extension can read/write.</p>

---

## Post #5 by @TingtingYu (2018-08-31 14:19 UTC)

<p>Hi Andras,</p>
<p>Thank you. Thank you for your help.</p>
<p>Best,<br>
Tingting</p>

---
