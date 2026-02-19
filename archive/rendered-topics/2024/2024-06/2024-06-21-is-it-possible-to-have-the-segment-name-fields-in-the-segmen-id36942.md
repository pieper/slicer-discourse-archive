---
topic_id: 36942
title: "Is It Possible To Have The Segment Name Fields In The Segmen"
date: 2024-06-21
url: https://discourse.slicer.org/t/36942
---

# Is it possible to have the segment name fields in the segment editor be like a combobox?

**Topic ID**: 36942
**Date**: 2024-06-21
**URL**: https://discourse.slicer.org/t/is-it-possible-to-have-the-segment-name-fields-in-the-segment-editor-be-like-a-combobox/36942

---

## Post #1 by @user543 (2024-06-21 18:35 UTC)

<p>We have a set of preset segment names that we would like to use, and it would speed up the workflow if the names can be set as the user starts typing to pick it more quickly from the list. Is this something that can be done easily or would we need to build a custom slicer to be able to make changes to the segment editor widget?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2024-06-21 18:44 UTC)

<p>Yes, this is already available. You can double-click on the colored box next to the segment’s name and you can select your segment from a list. If you want to work with a reduced list then you can define your custom terminology file. It is a simple text file that lists name, color, and standard terminology code for each segment. It is very important to always use standard terminology code to specify what is in a segment because often there are many synonyms and different spellings for the same structure.</p>
<p>I’ve provided detailed description on how to create a terminology file <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/UsingStandardTerminology.md#specifying-term-for-a-segment-during-segmentation">here</a>.</p>

---

## Post #3 by @user543 (2024-06-21 20:03 UTC)

<p>That’s great! Thanks a lot.</p>

---
