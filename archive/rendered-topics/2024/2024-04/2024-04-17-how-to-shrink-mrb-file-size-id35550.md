---
topic_id: 35550
title: "How To Shrink Mrb File Size"
date: 2024-04-17
url: https://discourse.slicer.org/t/35550
---

# How to shrink mrb file size?

**Topic ID**: 35550
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/how-to-shrink-mrb-file-size/35550

---

## Post #1 by @Stuart (2024-04-17 02:41 UTC)

<p>Operating system: OSX<br>
Slicer version:5.6.2<br>
Expected behavior: small file<br>
Actual behavior: large file</p>

---

## Post #2 by @lassoan (2024-04-17 02:43 UTC)

<p>MRB contains all the data that is in the scene with lossless compression. If you think that the size is unreasonable then please provide more information.</p>

---

## Post #3 by @Stuart (2024-04-17 13:53 UTC)

<p>I’m new to Slicer and appreciate your help.</p>
<p>Here’s the situation. I imported a file of 1417 dcm images, 399K each, for a total of 1.45GB. On this series I first identified a ROI of perhaps 20% of the volume and performed some straightforward segmentations on perhaps 5% of the voxels in that volume. I then saved all as a MRB file. This file size is 9.69GB. I’m working on this project with others and would like to share this file with others who also use Slicer.</p>
<p>My overarching question is how to produce a much smaller MRB file. I realize that I could separate the ROI into a separate MRB. Other that that, what else can I do to reduce the file size?</p>
<p>I greatly appreciate your help with this rather mundane question.</p>
<p>Stuart</p>

---

## Post #4 by @muratmaga (2024-04-17 14:15 UTC)

<p>After you extracted the ROI subvolume, remove the original dicom series and save your MRB again.</p>
<p>MRB saves everything you loaded into your scene. So removing things that you dont need will make your MRB smaller.</p>

---

## Post #5 by @Stuart (2024-04-17 15:16 UTC)

<p>Thanks; that helped a lot. The file went from 9.7 to 2.8GB.</p>

---

## Post #6 by @lassoan (2024-04-17 17:24 UTC)

<p>Which files are large? Is that file compressed already? Would you prefer faster opening of the scene or further reduction of the file size?</p>
<p>You may also choose to save all the files separately (.mrml scene file + separate file for each data set), which would make saving faster and would not be necessary to keep synchronizing unchanged files (e.g., source volume). If you work with others then you can share the folder that contains all these files via dropbox/onedrive/etc. and it will be synnchronized very effectively, as the files that are not modified will need to be transferred only once.</p>

---

## Post #7 by @Stuart (2024-04-17 19:09 UTC)

<p>Thanks. Now I realize that I was saving the dcm volume, both initial and cropped, multiple times. I just sent a reduced file, with just one cropped dcm volume, and ihe opened it just fine. An enormous reduction from 9.7GB to 350MB.</p>
<p>Thanks for your patience with newbies.</p>
<p>Stu</p>

---
