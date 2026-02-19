---
topic_id: 1908
title: "Can One Segment Be Part Of Another One"
date: 2018-01-23
url: https://discourse.slicer.org/t/1908
---

# Can one segment be part of another one?

**Topic ID**: 1908
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/can-one-segment-be-part-of-another-one/1908

---

## Post #1 by @AnFr (2018-01-23 15:29 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8<br>
Expected behavior: segmented kidney should be an individual segment AND part of another segment (soft tissue)<br>
Actual behavior: as soon as I segmented the kidney and add another segment that overlaps that kidney, it disappears</p>
<p>For the same series, I am trying to segment the left kidney individually (I am using Segment Editor) and I want to compare the volume of bones to the volume of remaining body (tissue, organs (including that kidney), etc.).<br>
However, as soon as I add a new segment (total soft tissue) and also paint it over the kidney I have previously segmented, the whole kidney disappears and is now only a part of soft tissue and not an individual segment anymore.<br>
Is there a way so that my plan will work?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @cpinter (2018-01-23 15:43 UTC)

<p>You need to change “Overwrite other segments” from “All segments” to “None” on the very bottom of Segment Editor (after you selected an effect) to enable overlap.</p>
<p>To me having this as default would be better (I have to do undo then change this and draw again many times), but apparently for historical reasons (i.e. labelmaps) no overlap is the default.</p>

---

## Post #3 by @AnFr (2018-01-23 15:52 UTC)

<p>That was fast, Thank you! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
