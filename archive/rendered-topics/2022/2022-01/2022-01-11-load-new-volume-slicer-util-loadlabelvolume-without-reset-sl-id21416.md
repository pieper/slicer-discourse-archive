---
topic_id: 21416
title: "Load New Volume Slicer Util Loadlabelvolume Without Reset Sl"
date: 2022-01-11
url: https://discourse.slicer.org/t/21416
---

# Load new volume (slicer.util.loadLabelVolume) without reset slicer layout

**Topic ID**: 21416
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/load-new-volume-slicer-util-loadlabelvolume-without-reset-slicer-layout/21416

---

## Post #1 by @CSConstantino (2022-01-11 19:25 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
When I load a new volume using “slicer.util.loadLabelVolume”, the slicer always resets the layout. But I would like to keep the previous one. Can you help me?</p>
<p>Thank you!</p>

---

## Post #2 by @CSConstantino (2022-01-12 09:20 UTC)

<p>It was solved by adding the flag show=False, as follows: “slicer.util.loadLabelVolume(fileName, properties={‘show’:False}”</p>
<p>Thank you.</p>

---
