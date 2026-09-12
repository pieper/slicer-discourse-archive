---
topic_id: 48121
title: "Correct workflow for loading 4D CT cardiac data"
date: 2026-09-11
url: https://discourse.slicer.org/t/48121
last_bumped: 2026-09-11T19:34:56.306Z
---

# Correct workflow for loading 4D CT cardiac data

**Topic ID**: 48121
**Date**: 2026-09-11
**URL**: https://discourse.slicer.org/t/correct-workflow-for-loading-4d-ct-cardiac-data/48121

---

## Post #1 by @arumiat (2026-09-11 10:01 UTC)

<p>Hi Slicer Community,</p>
<p>I have a .nii file which is a 4D-gated cardiac CT but I am struggling to load it in Slicer in a way whereby I can watch the heart beating. Is there a specific workflow I need to follow.</p>
<p>So far I have</p>
<ul>
<li>Add Data</li>
<li>make sure ‘Volume’ is checked</li>
<li>go to Sequences module</li>
</ul>
<p>But I am not seeing any of the green buttons for playing the sequence - they are all greyed out.</p>
<p>It could be the case the file is missing the header or something?</p>
<p>Happy to share the file if needed.</p>

---

## Post #2 by @pieper (2026-09-11 16:10 UTC)

<p>See this conversation for context: <a href="https://discourse.slicer.org/t/4d-nifti-flipped-and-rotated-about-90-deg/48056" class="inline-onebox">4D NifTi flipped and rotated about 90-deg</a></p>

---

## Post #3 by @Deep_Learning (2026-09-11 19:34 UTC)

<p>I would suggest making an nii.gz for each phase.  These are read in normally.  Then they are added to a Sequence.  This definately works.</p>

---
