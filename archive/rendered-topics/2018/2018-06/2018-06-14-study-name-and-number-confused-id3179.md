---
topic_id: 3179
title: "Study Name And Number Confused"
date: 2018-06-14
url: https://discourse.slicer.org/t/3179
---

# Study name and number, confused

**Topic ID**: 3179
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/study-name-and-number-confused/3179

---

## Post #1 by @Ash_Alarfaj (2018-06-14 12:19 UTC)

<p>hi<br>
When I tried to review image name. the programme shows me the wrong path(name of study). I review it from python interactor. as you can see in the attachment. actually,<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c24b993567e71f45e7676743b41a2af491aacebb.png" data-download-href="/uploads/short-url/rIOB5EqWvv5rM9qrS30QGj5ydFV.png?dl=1" title="study%20path%2C" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c24b993567e71f45e7676743b41a2af491aacebb_2_690x387.png" alt="study%20path%2C" data-base62-sha1="rIOB5EqWvv5rM9qrS30QGj5ydFV" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c24b993567e71f45e7676743b41a2af491aacebb_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c24b993567e71f45e7676743b41a2af491aacebb_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c24b993567e71f45e7676743b41a2af491aacebb.png 2x" data-dominant-color="B1B4B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">study%20path%2C</span><span class="informations">1366×768 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> in one file I save V1,V2,V3 but when I segment and save V1 or V3 and open it again and see the python it shows in both case V2.</p>
<p>I am wondering how I can check the image name so I can make sure I have worked on right one</p>

---

## Post #2 by @lassoan (2018-06-23 03:57 UTC)

<p>When you deal with DICOM files, file names do not matter, they are not taken into account anywhere. All information (instance UIDs, patient id, name, study information, image slice positions, etc) are all retrieved from the file content. Note that whenever you change anything in a DICOM file, you also need to regenerate the unique identifier (SOP instance UID) value in the file.</p>

---
