---
topic_id: 9550
title: "Slicerigt Collect Points To Model Node"
date: 2019-12-18
url: https://discourse.slicer.org/t/9550
---

# SlicerIGT Collect Points to Model Node

**Topic ID**: 9550
**Date**: 2019-12-18
**URL**: https://discourse.slicer.org/t/slicerigt-collect-points-to-model-node/9550

---

## Post #1 by @rprueckl (2019-12-18 16:00 UTC)

<p>This is probably a bug report:<br>
Slicer 4.10.2, SlicerIGT revision 00ff9bf</p>
<p>I try to use the ‘Collect Points’ module to collect points into a model node with the following settings (autocollect on):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b279d9f00af647c10a69e9e0d9b5989401cf9a77.png" alt="image" data-base62-sha1="psS3pmUQZnPTq5A0knSaBFvedzF" width="484" height="194"><br>
Then, in the transforms module, I change the translation of <code>LinearTransform_3</code> with the sliders.<br>
The points displayed by the model are quite weird:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43fdc3dcdfaaa402671dae276f5aa3510d280be7.png" alt="image" data-base62-sha1="9HtG8PjxPs4laSwsbvfCJTm6VqD" width="307" height="370"></p>
<p>Only, when I click ‘Delete the last point from the output node’, the data displays correctly:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86541ce5267952b01e0cc3d01cf2666c402d13db.png" alt="image" data-base62-sha1="jakbUbDJZCm0aE9jAnBCAGsR6c3" width="499" height="442"></p>
<p>I am not able to find the part of the code that causes the problem here. I would be grateful for any help.</p>

---

## Post #2 by @Sunderlandkyl (2019-12-18 16:12 UTC)

<p>Thanks for reporting this issue, it seems to happen in both 4.10 and 4.11. There seems to be a problem with the Model observers.</p>
<p>I’ll take a look at it.</p>

---

## Post #3 by @Sunderlandkyl (2019-12-18 16:29 UTC)

<p>I’ve created a <a href="https://github.com/SlicerIGT/SlicerIGT/commit/3bb92384069b8dd27064c43d3ff78f612f2dc3c5" rel="nofollow noopener">fix</a>. It should be available in the 4.11 release tomorrow.</p>

---
