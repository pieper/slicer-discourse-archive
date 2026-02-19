---
topic_id: 45751
title: "Body Composition Measurements Sma Smd Sat Vat At L3 Level"
date: 2026-01-12
url: https://discourse.slicer.org/t/45751
---

# Body composition measurements (sma, smd, sat, vat) at L3 level

**Topic ID**: 45751
**Date**: 2026-01-12
**URL**: https://discourse.slicer.org/t/body-composition-measurements-sma-smd-sat-vat-at-l3-level/45751

---

## Post #1 by @goz (2026-01-12 16:36 UTC)

<p>Hello everyone, I need your help <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=15" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>
<p>I want to measure the sma cm 2,  smd hu, sat cm2 and vat cm2 values at L3 level  CT dicom images.</p>
<p>But the software gives me the cm 3 volume , sat and vat values ,</p>
<p>how can i find the sma -sat-vat cm 2 ?</p>

---

## Post #2 by @pieper (2026-01-12 17:21 UTC)

<p>Slicer calculates volumes in 3D.  If you only segment a single slice, you need to divide by the slice spacing to get an area.</p>

---

## Post #3 by @lassoan (2026-01-12 17:34 UTC)

<p>If you have a 3D segmentation, you can use “Segment Cross-Section Area” module in Sandbox extension to get cross-sectional area slice by slice.</p>

---

## Post #4 by @goz (2026-01-13 22:11 UTC)

<p>Thanks a lot with heart <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I use segment cross section area but i do everthing manually, when i choose the threshold it gives the whole segments.</p>
<p>When we enter threshold values, is it possible for the software to automatically segment fat and muscle in a single section ?</p>

---
