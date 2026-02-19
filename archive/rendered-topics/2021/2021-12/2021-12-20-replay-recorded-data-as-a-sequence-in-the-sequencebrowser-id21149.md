---
topic_id: 21149
title: "Replay Recorded Data As A Sequence In The Sequencebrowser"
date: 2021-12-20
url: https://discourse.slicer.org/t/21149
---

# Replay recorded data as a sequence in the SequenceBrowser

**Topic ID**: 21149
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/replay-recorded-data-as-a-sequence-in-the-sequencebrowser/21149

---

## Post #1 by @lb123 (2021-12-20 16:19 UTC)

<p>Hi,</p>
<p>I recorded a tracked video using the Plus Remote module from Slicer IGT. The recording had been stored as a .igs.mha file.<br>
I can replay the recording using Plus Toolkit and the video and the tracking data is visible in Slicer through IGTLink.</p>
<p>However I cannot play/stop the video using the SequenceBrowser. Do you know  how I can solve this issue?</p>
<p>Thanks you</p>

---

## Post #2 by @lassoan (2021-12-21 05:28 UTC)

<p>If you install SlicerIGSIO extension then igs.mha file is offered to be loaded as “IGSIO Sequence”. You can replay this sequence using Sequences module (Browse tab).</p>
<p>Things work similarly in the latest Slicer Stable Release, too, but it is quite old and the new Slicer Preview Release will soon be the new stable, so I would recommend to switch to the preview release now.</p>

---
