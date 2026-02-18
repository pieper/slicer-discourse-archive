# Problem when loading non-dicom data

**Topic ID**: 6022
**Date**: 2019-03-05
**URL**: https://discourse.slicer.org/t/problem-when-loading-non-dicom-data/6022

---

## Post #1 by @Clara (2019-03-05 10:12 UTC)

<p>Slicer version: 4.10.1<br>
Operating system: Windows 64 bit</p>
<p>Hi all!</p>
<p>I am having an important issue when loading volumes in .img, .nii, or nrrd. My problem is that sometimes the program is able to load the volume in any of these formats but sometime it is not, it crashes or it doesn’t do anything. I have checked the size of the volumes and it doesn’t matter, i mean, it is able to load a volume of, for instance, 1 gb in format nii, but it is not able to load another file in the same size and format.</p>
<p>Any suggestion is welcomed. Thanks.</p>

---

## Post #2 by @dp1991 (2019-03-05 13:10 UTC)

<p>Hi<br>
data in the any format must be corrected and proportional with it’s format<br>
u can not save any data with any format<br>
do u understand my mean ??</p>

---

## Post #3 by @lassoan (2019-03-05 13:34 UTC)

<p>We need more specific information to investigate file loading problems. If there is no usable hints in the application log, then the best is if you can send us example data sets that cannot be loaded (you can send a link in a private message if you prefer not to share the data publicly).</p>

---

## Post #4 by @Clara (2019-03-18 08:49 UTC)

<p>Hi!  I realized I was not saving the data correctly from Matlab in the nrrd format. I suppose that in the case of img or nii I am having kind of the same problem. Thank you for your help! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #5 by @cpinter (2019-03-18 13:17 UTC)

<p>For Matlab-Slicer communication I suggest using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" rel="nofollow noopener">MatlabBridge</a> extension. That way you won’t have such problems.</p>

---
