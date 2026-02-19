---
topic_id: 15140
title: "Quick Color Assignment"
date: 2020-12-19
url: https://discourse.slicer.org/t/15140
---

# Quick color assignment

**Topic ID**: 15140
**Date**: 2020-12-19
**URL**: https://discourse.slicer.org/t/quick-color-assignment/15140

---

## Post #1 by @NoobForSlicer (2020-12-19 03:28 UTC)

<p>hello, I was wondering if there is an easy way to assign colors to segmentation.</p>
<p>As for now I have to always acces each segmentation and then pick each color separately for each segmentation.</p>
<p>is there some easy way to assign colors to all segments right away?</p>

---

## Post #2 by @NoobForSlicer (2020-12-19 03:48 UTC)

<p>hmm I saw colors in subject hierarchy but those colors do not match the colors I chose in segment editor</p>

---

## Post #3 by @lassoan (2020-12-19 05:32 UTC)

<p>You can create a custom terminology file with name, color, standard terms to describe what the segment contains (category, type, modifier, anatomic region, etc. - see <a href="https://dicom.innolitics.com/ciods/segmentation/segmentation-image/00620002">DICOM standard for segmentation storage</a>) and import and use that in the Segment editor’s terminology editor. See examples of terminology files in your Slicer installation in <code>share\Slicer-4.13\qt-loadable-modules\Terminologies</code> subfolder.</p>
<p>You may also find this topic relevant: <a href="https://discourse.slicer.org/t/segment-editor-specified-terminology-item-in-settings-is-partially-taken-into-account/13114" class="inline-onebox">Segment editor : specified terminology item in settings is partially taken into account</a></p>

---

## Post #4 by @NoobForSlicer (2020-12-20 21:37 UTC)

<p>ohh Thanks Lassoan Andras, God bless you sir for your help</p>

---
