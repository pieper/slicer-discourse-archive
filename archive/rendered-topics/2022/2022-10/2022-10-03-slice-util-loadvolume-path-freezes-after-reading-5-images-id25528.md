---
topic_id: 25528
title: "Slice Util Loadvolume Path Freezes After Reading 5 Images"
date: 2022-10-03
url: https://discourse.slicer.org/t/25528
---

# slice.util.loadVolume(path) freezes after reading 5 images

**Topic ID**: 25528
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/slice-util-loadvolume-path-freezes-after-reading-5-images/25528

---

## Post #1 by @S_Arbabi (2022-10-03 14:04 UTC)

<p>I’m using loadVolume to read 6 nii files, extrat their array and save it in a dictionary.<br>
It works reading 5 of them but freezes on reading the 6’th one.</p>
<p>The 6’th file loads okay if I import it as a file in slicer manually, so the issue is not with the file.<br>
Also if I remove reading of first file, it can also read the 6’th one, so it seems like it has some issues with lack of memory or some resource usage.<br>
I checked the memory usage in task manager and it is (52% of ram ~ around 15G) on slicer.</p>
<p>Any ideas?</p>

---
