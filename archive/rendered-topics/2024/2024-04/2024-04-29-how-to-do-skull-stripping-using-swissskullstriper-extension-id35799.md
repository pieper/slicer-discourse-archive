# How to do skull stripping using SwissSkullStriper Extension

**Topic ID**: 35799
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/how-to-do-skull-stripping-using-swissskullstriper-extension/35799

---

## Post #1 by @dorsa (2024-04-29 14:13 UTC)

<p>Hi All,</p>
<p>I’m trying to process Brain MRI images. and the first thing I would like to is to remove the Skull using the SwissSkullstripping extension but Unfortunately I can’t find any guide on how to do it from scratch and how to get the best results and the options which can be used.</p>
<p>Could someone help me regarding it.</p>
<p>thank you.</p>

---

## Post #2 by @lassoan (2024-04-29 14:15 UTC)

<p>See step-by-step tutorial in the extension’s documentation: <a href="https://github.com/lassoan/SlicerSwissSkullStripper?tab=readme-ov-file#basic-workflow" class="inline-onebox">GitHub - lassoan/SlicerSwissSkullStripper: Slice4 extension for the Swiss Skull Stripper</a></p>
<p>Note that there are many new AI based skull stripping tools, which may have higher computation requirements but they may provide better quality segmentation. For example, you can try <a href="https://github.com/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction">HDBrainExtraction extension</a>.</p>

---
