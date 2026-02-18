# Body composition

**Topic ID**: 36467
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/body-composition/36467

---

## Post #1 by @Kennyb0yy (2024-05-29 13:52 UTC)

<p>Hello everyone,</p>
<p>I am trying to segment multiple structures in an abdominal ct. There are 5 structures that I would like marked individually: Psoas muscle, Other skeletal muscle, Subcutaeous fat, intramuscular fat and visceral fat.</p>
<p>I’m fairly new to the app and I’m having a hard time figuring out the fastest and most efficient way to do it.</p>
<p>any suggestions? is there an established extension that can do it?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2024-05-29 13:59 UTC)

<p>You can segment muscles on CT using TotalSegmentator or MONAIAuto3DSeg extension. You can combine the segments with thresholding to obtain intramuscular fat.</p>

---
