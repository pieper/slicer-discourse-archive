# DICOM file cannot be read

**Topic ID**: 37624
**Date**: 2024-07-30
**URL**: https://discourse.slicer.org/t/dicom-file-cannot-be-read/37624

---

## Post #1 by @AWEN (2024-07-30 13:29 UTC)

<p>I tried processing the slice with segmentation and updated the original slice to release a new DICOM file, but the updated file cannot be read and shown:</p>
<p>"Slicer has caught an application error, please save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: D:\D\S\S-0-build\ITK\Modules\ThirdParty\GDCM\src\gdcm\Source\Common\gdcmException.h:74 ():<br>
Impossible"</p>
<p>After a few attempts, the DICOM file that could be read before now cannot be read as well (, even the original unmodified file cannot be read). I tried to update the 3D Slicer from 5.4.0 to 5.6.2, but it doesn’t work… I don’t even have the true result to see if my experiment is correct.</p>
<p>Could you tell me how I can solve this problem please?<br>
That means a lot to me…</p>

---

## Post #2 by @pieper (2024-07-30 13:34 UTC)

<p>It sounds like your dicom data is bad in some way.  You indicated you modified the file in some way, which is probably the source of the issue.  it’s very hard to generate valid dicom files, but there are many examples and tools available so you should be able to accomplish what you need if you study carefully.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>
<p>If you are still not sure, you’ll need to share your overall goal and the exact data and steps that you follow so people can give you specific advice.</p>

---
