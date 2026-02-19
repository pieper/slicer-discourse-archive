---
topic_id: 7011
title: "Problem With Opening Mmrl File"
date: 2019-06-03
url: https://discourse.slicer.org/t/7011
---

# Problem with opening .mmrl file

**Topic ID**: 7011
**Date**: 2019-06-03
**URL**: https://discourse.slicer.org/t/problem-with-opening-mmrl-file/7011

---

## Post #1 by @sali (2019-06-03 16:38 UTC)

<p>Operating system:Mac, windows, linux<br>
Slicer version:4.8.0<br>
Expected behavior:<br>
Actual behavior:<br>
Dear 3D Slicer users<br>
I have done segmentation in my CT images and I saved the data in .mmrl files, till two month ago, I could reopen this .mmrl file and change some parts of that, but today I tried to reopen this file, but it is not possible and after choosing this file with 3dSlicer, the software will be close automatically,<br>
What should I do for solving this problem?<br>
Thanks in advance,</p>

---

## Post #2 by @pieper (2019-06-03 18:24 UTC)

<p>Hi -</p>
<p>mrml files are just the descriptive part (implemented as xml) and they point to other data files, so one possibility is if for some reason the other files were deleted or renamed the mrml file won’t be able to load.   You should be able to look at the log file when loading for clues (under Help-&gt;Report a bug) and also you should try updating to the latest version of Slicer (4.10.2).</p>
<p>HTH</p>

---
