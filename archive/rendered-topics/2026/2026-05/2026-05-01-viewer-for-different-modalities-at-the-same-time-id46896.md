---
topic_id: 46896
title: "Viewer for different modalities at the same time"
date: 2026-05-01
url: https://discourse.slicer.org/t/46896
last_bumped: 2026-05-06T17:37:54.243Z
---

# Viewer for different modalities at the same time

**Topic ID**: 46896
**Date**: 2026-05-01
**URL**: https://discourse.slicer.org/t/viewer-for-different-modalities-at-the-same-time/46896

---

## Post #1 by @Sahar_KARIMI (2026-05-01 17:12 UTC)

<p>Good afternoon,</p>
<p>I am working with 3D-slicer viewer and I want to be able to visualize different sequences at the same time, lets say comparing 2 image modalities/sequences at the same time (one be main and other transparent on background maybe, something like that). I also want have this visualization while I am able to scroll through both different timelines and different slices. Is there any module or extension that can provide these features? Thank you very much in advance.</p>

---

## Post #2 by @mikebind (2026-05-02 17:55 UTC)

<p>This is a core Slicer feature, you just set one image as the foreground image an another as the background image.  I would suggest spending some time getting familiar with the Slicer interface here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#quick-start" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#quick-start</a></p>

---

## Post #3 by @Sahar_KARIMI (2026-05-06 15:23 UTC)

<p>Thank you very much. I have one question: in slicer viewer, we are able to visualize 2 different sequences at the same time by setting one in background and the other one in Frontend. Is there any possibility/ module to add more sequences to visualize at the same time back to back? I mean assume we have 4 series of T1 sequences for different time points and we want to see how tumor changes through time by scrolling in time through that 4 T1 series? Is this possible to do in 3D-slicer, any module or extension you can recommend me to use? Bcz it’s possible to do so for 2 series for example, so how about more?</p>
<p>Thank you very much for your help in advance,</p>
<p>SA</p>

---

## Post #4 by @mikebind (2026-05-06 17:37 UTC)

<p>This is possible, but slightly more complex, by using Sequences, which are also a part of the Slicer core.  This documentation should help you  <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#creating-sequences-from-a-set-of-nodes" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#creating-sequences-from-a-set-of-nodes</a></p>
<p>Once you’ve created the sequence, you can step through or play through the frames using the sequence browser toolbar (I think this will appear automatically, but if it doesn’t you can get it to show using View menu → Toolbars → Sequence browser (check box)</p>

---
