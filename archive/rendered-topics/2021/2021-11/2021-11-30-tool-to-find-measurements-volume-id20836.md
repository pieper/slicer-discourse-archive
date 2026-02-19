---
topic_id: 20836
title: "Tool To Find Measurements Volume"
date: 2021-11-30
url: https://discourse.slicer.org/t/20836
---

# Tool to find measurements/volume?

**Topic ID**: 20836
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/tool-to-find-measurements-volume/20836

---

## Post #1 by @Maddie (2021-11-30 04:08 UTC)

<p>Hello! I am working on the reproductive morphology of genitalia through CT scans. The segmentations are done for each view and I have a 3D model. I was wondering if there was a way for me to find the total volume the penis of my model (green, yellow, teal, and blue) took up in the vagina (pink). Or any other tool that could help me find this. Thanks.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684356f5379b8dc2af13e1b653cf208e5ed79e57.png" alt="Screen Shot 2021-11-29 at 9.57.43 PM" data-base62-sha1="eSlVKMgbiBNZY0MMDbgbEWxQePl" width="345" height="347"></p>

---

## Post #2 by @muratmaga (2021-11-30 04:22 UTC)

<p>If these models are derived from segmentations of these structures, then you can easily merge those four segments into a separate segment (via the logical operation tool -use add), and then use the Segment Statistics to calculate the volume of the combined segment.</p>
<p>You can of course do this on individual segments, but from screenshot it appears there are overlaps, so if you simply add up the volumes of individual segments, you might overestimate.</p>

---
