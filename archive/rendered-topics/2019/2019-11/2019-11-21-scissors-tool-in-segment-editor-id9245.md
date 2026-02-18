# Scissors tool in segment editor

**Topic ID**: 9245
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/scissors-tool-in-segment-editor/9245

---

## Post #1 by @BreadBoxGuy (2019-11-21 12:39 UTC)

<p>I have a hollow model, and I would like to remove part of the wall so I can see the inside surface of the structure. Currently, I’m using the erase tool to remove part of the wall but using the scissor tool seems to be quicker however I am unable to restrict it to make just a cut through one of the walls of the hollow object. Is this possible or is that a feature that could be added?</p>

---

## Post #2 by @lassoan (2019-11-21 12:46 UTC)

<p>You can restrict cutting depth using masking options (e.g., create a mask that contains the region that you want to allow cutting into). However, usually it is simpler to cut all the way through, then add back the parts you want to keep using a second cut - as shown in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">Craniotomy segmentation recipe</a>.</p>

---

## Post #3 by @lassoan (2023-03-21 03:14 UTC)



---
