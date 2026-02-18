# Segmentation editor not working

**Topic ID**: 39654
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/segmentation-editor-not-working/39654

---

## Post #1 by @Giovanni_Nicoletto (2024-10-11 12:07 UTC)

<p>Hi everyone,<br>
I was trying to create a segmentation of a face from a full head file. The problem Is that when I try to edit my new segmentation, threshold, scissor and all the other tools don’t affect the head. I think I’m missing something before starting to edit but I can’t resolve the problem.</p>

---

## Post #2 by @lassoan (2024-10-11 12:09 UTC)

<p>When you created the segmentation, you had another volume selected, which covered a different region. You can change the segmentation’s geometry as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>.</p>

---
