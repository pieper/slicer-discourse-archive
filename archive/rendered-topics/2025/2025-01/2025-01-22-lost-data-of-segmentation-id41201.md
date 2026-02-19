---
topic_id: 41201
title: "Lost Data Of Segmentation"
date: 2025-01-22
url: https://discourse.slicer.org/t/41201
---

# Lost data of segmentation

**Topic ID**: 41201
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/lost-data-of-segmentation/41201

---

## Post #1 by @yuvaraj_bigwigs (2025-01-22 02:13 UTC)

<p>Hi guys I am new to slicer tool. I did segmentation using segmentation option in slicer and I accidentally saved it as .nhrd file Instead of .nrrd file.if  I try loading the .nhrd file it show Cannot load file.What should I do Any suggestions??Is there any way to retake my segmentation using this .nhrd file??</p>

---

## Post #2 by @lassoan (2025-01-22 02:19 UTC)

<p>The .nhdr file (I assume the .nhrd was just a typo) format stores the header and data in two separate files. It should be no problem to load it as long as you have the data file (with .raw or .raw.gz extension) in the same folder.</p>

---
