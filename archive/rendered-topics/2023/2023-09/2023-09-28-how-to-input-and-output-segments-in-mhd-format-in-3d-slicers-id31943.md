---
topic_id: 31943
title: "How To Input And Output Segments In Mhd Format In 3D Slicers"
date: 2023-09-28
url: https://discourse.slicer.org/t/31943
---

# How to input and output segments in mhd format in 3D slicers.

**Topic ID**: 31943
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/how-to-input-and-output-segments-in-mhd-format-in-3d-slicers/31943

---

## Post #1 by @sun-wanqing (2023-09-28 03:03 UTC)

<p>I currently have T1 data in nrrd format and annotated segmentation data in nrrd format. I hope to convert them into mhd format data. For volume, I can choose the mhd format when saving, but for files in seg.nrrd format, what should I do?</p>

---

## Post #2 by @lassoan (2023-09-28 03:07 UTC)

<p>MetaImage (mha/mhd) file format cannot store information about image dimensions in a standard way, therefore we do not support saving segmentations into this format. If your segments are not overlapping then you can export the segmentation into a labelmap volume (e.g., by right-clicking on the segmentation in Data module) and you can save that labelmap volume in mhd format.</p>
<p>Why do you need to use mhd format? What software does not support nrrd format just mhd?</p>

---

## Post #3 by @sun-wanqing (2023-09-28 03:13 UTC)

<p>Thank you very much for your reply. I want to use it for deep learning training in the future because I only know how to read and train in mhd format. I tried the method you mentioned, which means that each label can only be saved as a binary lablemap. If there are 6  labels, I need to save them as 6 mhds. I will consider whether nrrd can be used for training.</p>

---

## Post #4 by @lassoan (2023-09-28 03:21 UTC)

<aside class="quote no-group" data-username="sun-wanqing" data-post="3" data-topic="31943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sun-wanqing/48/67673_2.png" class="avatar"> sun-wanqing:</div>
<blockquote>
<p>I only know how to read and train in mhd format</p>
</blockquote>
</aside>
<p>Reading images from nrrd is just as easy as reading from mhd.</p>
<p>You can use <a href="https://pypi.org/project/slicerio/">slicerio Python package</a> in your deep learning code to read segmentation files including metadata. It handles overlapping segments and identifies segments by name or terminology (and not based on label values, which can change, depending on what segments you had in the segmentation file in what order).</p>
<p>You may also use just pynrrd Python package but then you need to parse the segment metadata yourself.</p>

---
