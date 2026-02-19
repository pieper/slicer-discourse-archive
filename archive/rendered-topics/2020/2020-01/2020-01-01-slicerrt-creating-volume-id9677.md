---
topic_id: 9677
title: "Slicerrt Creating Volume"
date: 2020-01-01
url: https://discourse.slicer.org/t/9677
---

# SlicerRT creating volume

**Topic ID**: 9677
**Date**: 2020-01-01
**URL**: https://discourse.slicer.org/t/slicerrt-creating-volume/9677

---

## Post #1 by @annigilus (2020-01-01 17:50 UTC)

<p>Greetings, everyone! And Happy New Year!<br>
I have a question: how can I create new volumes in my dicom series in Slicer (CTV, PTV, OAR) to calculate the dose on this particular volume? (Worked in PLUNC, it has such tool. Sure, Slicer has too) I’ll be grateful if you answer me how to do it or show some tutorial about that (can’t find it).<br>
I’m a rookie in SlicerRT, please, don’t be too strict <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2020-01-01 17:51 UTC)

<p>You can create segments (RT structure sets) using Segment Editor module. You can then compute DVH etc. for these segments. See <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Extensions/SlicerRT">documentation</a> for details.</p>

---
