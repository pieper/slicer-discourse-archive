---
topic_id: 48572
title: "Computational requirements"
date: 2026-10-22
url: https://discourse.slicer.org/t/48572
last_bumped: 2026-10-22T20:10:55.959Z
---

# Computational requirements

**Topic ID**: 48572
**Date**: 2026-10-22
**URL**: https://discourse.slicer.org/t/computational-requirements/48572

---

## Post #1 by @Bernadett (2026-10-22 18:00 UTC)

<p>Hello,</p>
<p>I’m new to the 3D Slicer program. I’d like to seek help with the computational requirements for my project. I’m currently using a computer with the following specifications: 32 GB of installed RAM, iCore ™ i7-9700CPU @ 3GHz, 8GB graphics card (multiple GPUs installed).</p>
<p>I need to carry out bone segmentation from full-body CT scans. Scan slice thickness is 1mm.</p>
<p>When I work on the model, during the cleaning process the computer regularly freezes for up to 20 minutes at regular times.</p>
<p>I’m wondering if the above specifications are just not powerful enough and would like to ask your opinion about the listed specifications. Could you please advise me on this? I’ve just begun my PhD.</p>
<p>Thank you very much.</p>
<p>Bernadett</p>

---

## Post #2 by @pieper (2026-10-22 19:21 UTC)

<p>Your computer is probably okay, but maybe your workflow could be optimized.  One of the big costs of segmentation in current slicer is rebuilding the surface models (the show 3d button on) when you don’t need it.  You can try turning that off while doing things like cleaning up islands or doing detailed segmentations.  If that doesn’t help, tell us what operation is running when you notice the slowdowns.  Also you can look at the memory load on your computer, since some operations may be causing the data to swap to disk and that can be slow (depending on your OS there are different tools you can use for this).</p>

---

## Post #3 by @Bernadett (2026-10-22 20:10 UTC)

<p>Thank you for your answer. I will follow your advice and will come back to the thread if I still experience issues. Thank you again.</p>

---
