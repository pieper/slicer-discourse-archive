# Changing a single segment 2 different colors

**Topic ID**: 41562
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/changing-a-single-segment-2-different-colors/41562

---

## Post #1 by @BDhoth (2025-02-07 16:41 UTC)

<p>Is it possible to circle an area of a segment and turn it a different color? Ex. I have the ventricles segmented and would like the inferior half to be a different color than the superior portion. Is there a simple way to do this? Thank you!</p>

---

## Post #2 by @mikebind (2025-02-07 17:58 UTC)

<p>I don’t think there is a one-step tool that does this, but it is easy to achieve in a few steps in a few different ways.  Here are two options:</p>
<ol>
<li>Using masking settings:  Assuming your initial segment is S.  Add a new segment T, select it and choose the Paint tool. Adjust masking settings so “Editable area” is “Inside S”, then paint the area you want to have a different color.  If you have “Modify other segments” as “overwrite all” or “overwrite visible”, then S will be erased where you paint in T.</li>
<li>Using logical operations:  Add new segment T and use “Logical operators” copy to make T a duplicate of S.  Make sure “allow overlap” is chosen in the “Modify other segments” masking setting, to avoid having T erase S completely. Use Scissors (or any other modification tool you want) to get rid of the part of T that corresponds to the part of S you want to remain the original color. Lastly, select segment S, and use logical operators subtract to subtract T from S.</li>
</ol>
<p>Either method will give you two separate segments which you can color independently and which, combined, compose your original segment.</p>

---

## Post #3 by @BDhoth (2025-02-07 18:42 UTC)

<p>Thank you! That makes perfect sense.</p>

---
