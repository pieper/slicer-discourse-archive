# Slicer view resets on visibility change of nodes

**Topic ID**: 28591
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/slicer-view-resets-on-visibility-change-of-nodes/28591

---

## Post #1 by @S_Arbabi (2023-03-27 09:00 UTC)

<p>Hi,</p>
<p>I’m viewing a segmentation label on three MRI sequences. The volumes are registered, so I believe I should be able to switch between volumes and check the same slice of segmentation on three of the volumes easily, but when I show/hide a volume node, the other volume does not show from the same slice, but jumps to another slice where it’s defined as a starting point.</p>
<p>How can I make it easier?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-03-27 15:38 UTC)

<p>What you describe is the “Reset field of view on show” feature. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">turn it off in the right-click menu of the volume’s eye icon</a> in the  Data module.</p>

---
