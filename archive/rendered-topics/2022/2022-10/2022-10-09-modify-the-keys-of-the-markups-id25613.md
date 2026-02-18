# Modify the keys of the Markups

**Topic ID**: 25613
**Date**: 2022-10-09
**URL**: https://discourse.slicer.org/t/modify-the-keys-of-the-markups/25613

---

## Post #1 by @miniminic (2022-10-09 02:53 UTC)

<p>The measurement function of markups is currently right click to indicate the end, I want to change it to middle click to end, right click to rotate the model. I didn’t find anywhere in markups about mouse event handling, how I should do that.</p>

---

## Post #2 by @jay1987 (2022-10-09 05:44 UTC)

<p>you can read the code of vtkSlicerMarkupsWidget,may be help</p>

---

## Post #3 by @miniminic (2022-10-09 07:05 UTC)

<p>Ok, thanks. I’ll read it</p>

---

## Post #4 by @lassoan (2022-11-24 03:08 UTC)

<p>You can use the <code>SetEventTranslation</code> method to change keyboard and mouse event mapping to widget events. You can find examples on this forum and in the script repository.</p>

---

## Post #5 by @miniminic (2022-11-24 03:10 UTC)

<p>Yes, I have found this way. Thank you very much for your answer</p>

---
