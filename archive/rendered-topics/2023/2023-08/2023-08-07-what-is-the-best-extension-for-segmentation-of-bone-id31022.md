---
topic_id: 31022
title: "What Is The Best Extension For Segmentation Of Bone"
date: 2023-08-07
url: https://discourse.slicer.org/t/31022
---

# What is the best extension for segmentation of bone?

**Topic ID**: 31022
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/what-is-the-best-extension-for-segmentation-of-bone/31022

---

## Post #1 by @rbumm (2023-08-07 09:40 UTC)

<p>What is the best extension for segmentation of bone for trauma and orthopedic surgeons ?</p>
<p>The extenson should segment and solidify bone from CT, and f.e. divide structures like acetabulum and femor head or the carpal bones.</p>
<p>Optimatlly allow for transformations / repositions of fracture fragments.</p>

---

## Post #2 by @pieper (2023-08-07 12:30 UTC)

<p>For the pelvis, TotalSegmentator or the MONAI Label model trained on the same data are options if you haven’t already tried it.  Depending on the extent of trauma they may fail.  For bones that aren’t included in those models it’s a tough problem that should ultimately be solvable by the same approach but I don’t know of a model that’s been made available yet.  Traditionally people use grow from seeds, scissors, wrap solidify, etc.</p>
<p>Repositioning can be done with splitting islands, exporting segments, and setting transforms.  Positioning the fragments should be relatively easy with the interaction modes in the viewers.</p>

---

## Post #3 by @rbumm (2023-08-07 12:39 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> just wanted to be sure I did not miss an existing project.</p>

---

## Post #4 by @lassoan (2023-08-12 16:53 UTC)

<p>3 posts were split to a new topic: <a href="/t/automatic-spine-segmentation/31116">Automatic spine segmentation</a></p>

---
