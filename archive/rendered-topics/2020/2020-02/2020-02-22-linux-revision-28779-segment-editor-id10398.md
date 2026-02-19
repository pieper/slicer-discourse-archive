---
topic_id: 10398
title: "Linux Revision 28779 Segment Editor"
date: 2020-02-22
url: https://discourse.slicer.org/t/10398
---

# Linux revision 28779 - Segment editor

**Topic ID**: 10398
**Date**: 2020-02-22
**URL**: https://discourse.slicer.org/t/linux-revision-28779-segment-editor/10398

---

## Post #1 by @manjula (2020-02-22 21:25 UTC)

<p>When i try  use Island effects, Slicer exist with the following error message,</p>
<p>error: [/***************/Slicer-4.11.0-2020-02-19-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>This happens with large files (3-4 gb ) only so maybe it running out of memory ?</p>

---

## Post #2 by @lassoan (2020-02-22 21:55 UTC)

<p>Could you try to crop/resample the volume to be smaller and try how much memory it needs then? Can you allocate a lot of swap space (keys say 100GB) and see if it helps?</p>

---

## Post #3 by @manjula (2020-02-22 22:40 UTC)

<p>yes i never checked, my Swap size. It was 1 GB on linux mint. increasing did help !</p>

---

## Post #4 by @lassoan (2020-02-23 01:15 UTC)

<p>Do you mean that increasing swap size solved the problem and the application does not crash anymore?</p>

---

## Post #5 by @manjula (2020-02-23 08:27 UTC)

<p>sorry for the confusion. I never looked at my Swap settings before.  I use LVM+ LUKS so i created a separate swapfile with 20 GB and high priority. Also adjusted the swappiness to 10.  How ever the still the program crashes on those steps. Also new swap partition not even close to get full when the program crashes.</p>

---
