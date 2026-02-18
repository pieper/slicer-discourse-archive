# Run TotalSegmentator on MultiVolume

**Topic ID**: 31073
**Date**: 2023-08-03
**URL**: https://discourse.slicer.org/t/run-totalsegmentator-on-multivolume/31073

---

## Post #1 by @StArsenkov (2023-08-03 09:43 UTC)

<p>Hello,<br>
I’m trying to use TotalSegmentator, and it was working perfectly until now, but for some reason today, I can’t use it. The problem is that I can’t use the desired volume for input, and the only issue I’ve seen is that the volume I’m trying to use is a MRMLMulti, whereas the ones I can select as inputs are Scalar. Is this a known issue (requiremet), and what can I do about it?</p>

---

## Post #2 by @lassoan (2023-08-09 17:46 UTC)

<p>TotalSegmentator can only work on a 3D volume (and not on 4D MultiVolume).</p>
<p>You can enable “Current frame copy” in MultiVolumeExplorer module to create a 3D volume of the current time point. However, Sequences module will replace MultiVolume module (as it is more generic, supports time sequence of not only images but any other data types), so I would recommend to use Sequences module instead, by opening in the menu: Edit / Application Settings / DICOM / Preferred multi-volume format → volume sequence; restart Slicer, and then load the image again.</p>

---

## Post #3 by @StArsenkov (2023-08-10 07:56 UTC)

<p>Thank you very much!</p>

---
