---
topic_id: 22601
title: "Import Cso Segmentation Into Slicer"
date: 2022-03-19
url: https://discourse.slicer.org/t/22601
---

# Import CSO segmentation into Slicer

**Topic ID**: 22601
**Date**: 2022-03-19
**URL**: https://discourse.slicer.org/t/import-cso-segmentation-into-slicer/22601

---

## Post #1 by @Fabio_Nunes (2022-03-19 14:28 UTC)

<p>Dear 3D Slicer team,<br>
I’m working with CSO files (contour segmentation objects) that have been extracted from other programs. In my case, the CSO files represent the segmentation of the pericardium. I’ve tried the suggestion provided by Slicer docs ( Import an existing segmentation from volume file<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file" rel="noopener nofollow ugc">¶</a>, but it has failed with an error message “Error: Loading C:/Users/Desktop/patient.cso -  load failed.”</p>
<p>Any suggestions on how to load these segmentations?<br>
Thank you in advance.</p>

---

## Post #2 by @lassoan (2022-03-19 17:09 UTC)

<p>What software produces these CSO files? Do you have a specification and example files that you can share? Are there any readers for it in Python or C++? If yes, then it should be easy to set up a reader for it in Slicer.</p>

---

## Post #3 by @yangguang-ecnu (2023-03-06 06:42 UTC)

<p><a href="https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/Overviews/CSOOverview.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/Overviews/CSOOverview.html</a></p>

---

## Post #4 by @pieper (2023-03-06 13:59 UTC)

<p>We don’t have a reader for that format in Slicer, but I’m sure MeVisLab can export the data in a format Slicer can use (nrrd, nii, etc).</p>

---

## Post #5 by @mau_igna_06 (2024-02-04 00:51 UTC)

<p>I’ve found a dataset that has CBCTs and may have their segmentations in .cso</p>
<p>Is there a way to try to read them on Slicer? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @pieper (2024-02-04 15:04 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> it’s the same answer as given above : )</p>
<p>It appears that .cso files are MeVisLab specific and would probably need to be reverse engineered to implement a Slicer reader.  A more direct approach would be to install MeVisLab (it’s free for this purpose I believe) and figure out how to convert them in a batch process.  Either method should be workable.</p>

---
