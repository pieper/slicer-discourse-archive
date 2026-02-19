---
topic_id: 3736
title: "Margin Calculator Extension"
date: 2018-08-12
url: https://discourse.slicer.org/t/3736
---

# Margin calculator extension

**Topic ID**: 3736
**Date**: 2018-08-12
**URL**: https://discourse.slicer.org/t/margin-calculator-extension/3736

---

## Post #1 by @aseman (2018-08-12 07:11 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D slicer experts:<br>
I want to work with some modules of margin calculator extension , but I don’t know any thing about it. can you help me and introduce a comperhensive tutorial about this extension (and it’s modules)?<br>
thanks a lot</p>

---

## Post #2 by @lassoan (2018-08-12 08:57 UTC)

<p>Since Margin and Logical operators effects are available in Segment Editor module, I would recommend using them instead of the standalone Margin Calculator extension.</p>

---

## Post #3 by @cpinter (2018-08-12 21:16 UTC)

<p>The Margin Calculator extension was created by one of our collaborators, but since then has been abandoned. If it has any feature that Segment Editor cannot do and you need it for your project, I’m happy to guide you in resurrecting it.</p>

---

## Post #4 by @aseman (2018-08-13 13:56 UTC)

<p>Hi 3D slicer experts<br>
Thanks for your response. I want to calculate the random and systematic errors . I think that the modules of this extension can calculate these errors . can you guide me?<br>
Thanks a lot</p>

---

## Post #5 by @gcsharp (2018-08-13 14:37 UTC)

<p>The Segment editor does not compute random and systematic errors.  You will need to implement this yourself.  The formula is very simple, and you can do this in Excel.</p>
<p>(By the way, I never used the Margin Calculator, but I don’t think it computes random and systematic errors.  Instead, I think you are supposed to supply these as inputs.)</p>

---

## Post #6 by @lassoan (2018-08-14 04:38 UTC)

<p>Do you mean computing random and systematic errors of segmentation? Do you have multiple segmentations of the same structure?</p>

---

## Post #7 by @cpinter (2018-08-14 12:37 UTC)

<p>I believe the Margin Calculator can calculate such errors, see description on page<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MarginCalculator" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MarginCalculator</a><br>
“Motion simulation for systematic and random errors”</p>
<p>The dashboard shows that it builds fine on Linux and Mac, but not on Windows.<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=MarginCalculator" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=MarginCalculator</a><br>
It shouldn’t be too hard to fix. <a class="mention" href="/u/aseman">@aseman</a> do you want to give it a try?</p>

---
