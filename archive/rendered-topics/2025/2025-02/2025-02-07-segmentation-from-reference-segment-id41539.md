---
topic_id: 41539
title: "Segmentation From Reference Segment"
date: 2025-02-07
url: https://discourse.slicer.org/t/41539
---

# Segmentation from reference segment

**Topic ID**: 41539
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/segmentation-from-reference-segment/41539

---

## Post #1 by @slicerpy (2025-02-07 07:46 UTC)

<p>Hello,<br>
I’m looking to automate a somewhat complex manual segmentation and trimming process. I would like to explore all the available options for this. Specifically, I’m wondering if Slicer has a feature to segment based on a reference segment that has already been manually segmented.</p>
<p>Initially, I want to do this through the UI, but Eventually, I would like to implement the process through a Python script.</p>
<p>Could you provide more insight into how this could be achieved?</p>

---

## Post #2 by @cpinter (2025-02-12 14:39 UTC)

<p>It is impossible to tell anything really useful without knowing anything about the structures you want to segment. With this much information all I can think of are 1) training a DL model for your needs or 2) Creating a generic initial seeding for Grow from seeds, adapting it to the current image and run GrowCut.</p>
<p>If you want better advice, I suggest providing more details.</p>

---
