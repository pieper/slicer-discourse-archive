---
topic_id: 31849
title: "Wrong Volume Type When Exporting To File"
date: 2023-09-22
url: https://discourse.slicer.org/t/31849
---

# Wrong volume type when exporting to file

**Topic ID**: 31849
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/wrong-volume-type-when-exporting-to-file/31849

---

## Post #1 by @pim (2023-09-22 16:35 UTC)

<p>When performing the Mask Volume operation in the Segment Editor module, using a scalar volume and a segmentation node (converted from a labelmap) as inputs, I correctly obtain a new node as output which is a scalar volume.</p>
<p>However when exporting this output node to file, and importing that file again into Slicer, I realise that the volume is not a scalar volume anymore but a labelmap volume. Attempts to convert and save again yield the same result.</p>
<p>Is this intended behaviour? I am expected to use the output scalar volume in an external application but it seems impossible to obtain that, only the labelmap volume. Using Slicer v.5.2.2 r31382 and SegmentEditorExtraEffects v.f43df35.</p>
<p>Thank you in advance for any hint on how to deal with this issue.</p>

---

## Post #2 by @lassoan (2023-09-22 16:43 UTC)

<p>There are some heuristics to guess based on the filename how a volume should be interpreted by default: as a scalar volume or as a labelmap volume. If filename contains <code>label</code> or <code>seg</code> then it may be offered to be loaded as a labelmap by default. Although you can change the default in the “Add data” window (click “Show options” then uncheck “LabelMap”), it could be tedious to do that each time you load the image. Therefore, I would recommend to name the file differently.</p>

---

## Post #3 by @pim (2023-09-22 17:00 UTC)

<p>Oh I did not know this was a thing!</p>
<p>Thank you for clearing that up, I had never come across that information while browsing the documentation (quickly though I have to admit). Glad to know the files are actually containing the proper information though, which is all I needed to know!</p>

---
