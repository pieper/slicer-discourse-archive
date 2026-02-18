# Can't import DICOM data

**Topic ID**: 835
**Date**: 2017-08-07
**URL**: https://discourse.slicer.org/t/cant-import-dicom-data/835

---

## Post #1 by @hide (2017-08-07 11:10 UTC)

<p>Operating system:microsoft surface pro, windows10<br>
Slicer version:4.6.2<br>
Actual behavior:<br>
Hello<br>
I installed 3D slicer 4.6.2.<br>
Iget errors as below  trying to import DICOM data.<br>
I don`t know what to do.<br>
Please let me know.</p>
<p>Sincerely</p>
<hr>
<p>Slicer has caught an internal error.<br>
You may be able to continue from this point, but results are undefined.<br>
Suggested action is to save your work and restart.<br>
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a><br>
The message detail is:<br>
Exception thrown in event: Calling methods on uninitialized ctkDICOMItem</p>

---

## Post #2 by @pieper (2017-08-07 15:33 UTC)

<p>Here are some suggestions:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #3 by @hide (2017-08-07 20:33 UTC)

<p>thanks for your reply.<br>
I try.</p>

---

## Post #4 by @cpinter (2017-08-07 20:48 UTC)

<p>Please use the most recent nightly build, 4.6.2 is 10 months old at this point. If the problem persists, then please send us the log file.</p>

---

## Post #5 by @hide (2017-08-08 12:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a944b7cb0ced768d7d27fe0850f62cfb2e9add7.jpeg" data-download-href="/uploads/short-url/3N88l7RgnoJPmXsryPNyMISaiVN.jpg?dl=1" title="error image new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1a944b7cb0ced768d7d27fe0850f62cfb2e9add7_2_690x388.jpg" alt="error image new" data-base62-sha1="3N88l7RgnoJPmXsryPNyMISaiVN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1a944b7cb0ced768d7d27fe0850f62cfb2e9add7_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1a944b7cb0ced768d7d27fe0850f62cfb2e9add7_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a944b7cb0ced768d7d27fe0850f62cfb2e9add7.jpeg 2x" data-dominant-color="F3F3F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error image new</span><span class="informations">1280×720 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
thanks a lot.<br>
I tried to use nightly build 4.7, but couldn`t import DICOM data in tha same way.<br>
I attach the log files.</p>
<p>Sincerely</p>

---

## Post #6 by @lassoan (2017-08-08 12:17 UTC)

<p>Thanks fore reporting. Instead of sending a screenshot, could you please attach the log (as text, from menu: Help / Report a bug; log is available for the last 10 sessions, not just the current)? Before submitting, have a look at the text and scrub any patient information, if there is any.</p>

---

## Post #7 by @lassoan (2017-08-08 12:19 UTC)

<p>DICOM files path may be too long. Choose a shorter one, for example C:\SlicerDB. Also, shorten path of DICOM files before importing them, using <code>DICOM Patcher</code> module.</p>

---

## Post #8 by @hide (2017-08-08 15:51 UTC)

<p>thanks a lot.<br>
As you say, using DICOM patcher, I could import my DICOM data.<br>
I will contact you if I need additional information.</p>
<p>Sincerely</p>

---

## Post #11 by @gstarbuck (2019-05-24 15:02 UTC)

<p>This fixed the same issue for me - it seems that the slice names were too long.</p>

---
