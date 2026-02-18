# Structures segmented in either Arterial/Venous phases are slightly misaligned when switching view to the other phase

**Topic ID**: 23748
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/structures-segmented-in-either-arterial-venous-phases-are-slightly-misaligned-when-switching-view-to-the-other-phase/23748

---

## Post #1 by @rjk (2022-06-07 07:53 UTC)

<p>Operating system: macOS 12.3.1<br>
Slicer version: 5.0.2<br>
Expected behavior: arterial+ venous phases align perfectly<br>
Actual behavior: slight offset between structures between A and V phases, e.g., a structure segmented in phase A will be in a slightly different position when switching view to phase V.</p>
<p>Is there a way in settings to account for this minor discrepancy?</p>

---

## Post #2 by @mau_igna_06 (2022-06-07 08:57 UTC)

<p>Maybe this is the error i s smoothing <a class="mention" href="/u/lassoan">@lassoan</a> pointed out asometime ago in vtk forum</p>

---

## Post #3 by @rjk (2022-06-07 08:59 UTC)

<p>This occurs in segmentations that have not gone through any smoothing yet, if I’m understanding your comment correctly (novice user).</p>

---

## Post #4 by @mau_igna_06 (2022-06-07 09:02 UTC)

<p>If the phases you mean are different timestamps then it is not that, you should register them to match</p>

---
