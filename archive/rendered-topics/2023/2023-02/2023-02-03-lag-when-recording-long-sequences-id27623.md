# Lag when recording long sequences

**Topic ID**: 27623
**Date**: 2023-02-03
**URL**: https://discourse.slicer.org/t/lag-when-recording-long-sequences/27623

---

## Post #1 by @hgueziri (2023-02-03 19:31 UTC)

<p>Hi all,</p>
<p>I am currently using the Sequences module to record the transforms of tracked instruments. I have 7 instruments (transforms updated via PLUS/OpenIGTLink connector). At the beginning, everything works well but after a few minutes of recording, there is a significant lag which affects the quality of the recording. When I stop the recording, the lag disappears and everything goes back to normal.</p>
<p>I want to record 5-10 min of tracking (3000+ frames). I noticed when I hide the Sequences module, the lag is slightly reduced (and usually starts later in the recording). I first thought it has to do with too many Qt widgets being created inside the QTableWidget under “Edit” tab. But it keeps happening even when it is hidden.</p>
<p>I am using Slicer 4.11, Windows 10, 32 Gb of memory.</p>
<p>Has anyone tried to record a long sequence in Slicer? Is there a workaround to avoid the lag?<br>
I tried Slicer 5.2 and I have the same issue, I’d prefer using Slicer 4.11 for compatibility with python 3.6 and other libraries I am using.</p>
<p>Thanks</p>

---
