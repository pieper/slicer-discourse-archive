---
topic_id: 20940
title: "Duplication Of Segmentation Node On Crash"
date: 2021-12-07
url: https://discourse.slicer.org/t/20940
---

# Duplication of Segmentation node on crash

**Topic ID**: 20940
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/duplication-of-segmentation-node-on-crash/20940

---

## Post #1 by @hherhold (2021-12-07 02:08 UTC)

<p>I’m not sure exactly how this happened, but it likely involved a crash at some point. I noticed I had excessive memory usage upon loading a project, and when I looked at the Data module, I found that I had two identical Segmentation nodes. Somewhere along the line, one of them was duplicated and I unknowingly saved it, at which point it was reloaded.</p>
<p>The really disconcerting thing about it is that there were TWO segmentation nodes with the exact same name, and in the Save dialog, they have the exact same filename, so I suspect one could overwrite the other.</p>
<p>I will work to find a sequence of events to replicate this, but can anyone think of an instance where a Segmentation node might get duplicated?</p>
<p>Thanks, and sorry for the vague nature of the report.</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2021-12-07 02:09 UTC)

<p>Oh, this is with nightly 12/3 on MacOS. Although I suspect the crash occurred with a nightly from perhaps a week or two ago - I update about every 5-10 days.</p>

---
