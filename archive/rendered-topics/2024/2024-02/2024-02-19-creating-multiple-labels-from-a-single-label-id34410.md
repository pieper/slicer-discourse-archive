---
topic_id: 34410
title: "Creating Multiple Labels From A Single Label"
date: 2024-02-19
url: https://discourse.slicer.org/t/34410
---

# Creating multiple labels from a single label

**Topic ID**: 34410
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/creating-multiple-labels-from-a-single-label/34410

---

## Post #1 by @doc87 (2024-02-19 20:32 UTC)

<p>Hi all<br>
I have some ct scans that give me all vertebrae labelled as one segment. I have been trying to figure out how to convert into individual segments where each segment is a specific vertebra but haven’t been able to do.<br>
I have tried using the erase tool to demarcate each vertebra as separated but still the segment editor recognizes them as a single label.<br>
Any suggestions or ideas would be great!<br>
Thanks</p>

---

## Post #2 by @muratmaga (2024-02-20 04:06 UTC)

<p>If you have all vertebrae as a single segment, then you should be able to use a number of different effects in segment editor to separate them out.</p>
<ol>
<li>If vertebrae are not touching, easiest would be using the Island tool with the option separate islands into segments.</li>
<li>For the ones that remained connected after <span class="hashtag-raw">#1</span>, you can use the scissors tool with FILL option. Make sure the active segment is an empty one and Editable Area of the Masking options is set to Inside Segment_XXX, where Segment_XXX is the segment that contains the remaining vertebra.</li>
</ol>

---

## Post #3 by @doc87 (2024-02-20 16:32 UTC)

<p>This worked!! Thanks a lot</p>

---
