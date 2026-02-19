---
topic_id: 26064
title: "Convert Stl To Mhd"
date: 2022-11-04
url: https://discourse.slicer.org/t/26064
---

# Convert stl to mhd

**Topic ID**: 26064
**Date**: 2022-11-04
**URL**: https://discourse.slicer.org/t/convert-stl-to-mhd/26064

---

## Post #1 by @Trailer (2022-11-04 11:18 UTC)

<p>Hello,</p>
<p>I have an stl with 3 cylinders. I would like to be able to convert it to mhd format.</p>
<p>Is it possible to do this with Slicer? What steps are needed?</p>
<p>Would really appreciate the help!</p>
<p>I will leave the stl here: <a href="https://we.tl/t-qM1jgJUcDY" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>
<p>Best regards</p>

---

## Post #2 by @cpinter (2022-11-04 11:46 UTC)

<p>You can load the STL, then convert it to a segmentation node using the “Convert model to segmentation node” option in the Data module (as explained <a href="https://discourse.slicer.org/t/how-to-edit-an-stl-file-using-segment-editor/17559/13">here</a> very recently as well), then convert the segmentation to labelmap, finally save the labelmap to mhd using the Save data button.</p>
<p>Note that without specifying a reference volume the resolution of the volume will be 1mm x 1mm x 1mm.</p>

---

## Post #3 by @Trailer (2022-11-04 12:07 UTC)

<p>Is it possible to segregate the individual cylinder when exporting to mhd?</p>

---

## Post #4 by @cpinter (2022-11-04 12:47 UTC)

<p>Can you please be more specific about what you want?</p>

---
