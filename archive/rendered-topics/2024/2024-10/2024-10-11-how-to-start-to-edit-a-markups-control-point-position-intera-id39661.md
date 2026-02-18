# How to start to edit a markups control point position interactively with code

**Topic ID**: 39661
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/how-to-start-to-edit-a-markups-control-point-position-interactively-with-code/39661

---

## Post #1 by @mau_igna_06 (2024-10-11 17:33 UTC)

<p>Hi</p>
<p>My requirement is to have 3 points with labels “A”, “B” and “C”; and have a GUI with 3 checkable buttons with texts “A”, “B” and “C”. When a button is checked then interactive mode should allow to edit point position with the corresponding label (or add it if it did not exist yet).<br>
Also, the number of control points and their labels are fixed.</p>
<p>For example when button “B” is pressed, placement mode should start to modify the control point position with label “B”. If the button “B” is unchecked maybe the control point should be “unset” or “reset” or “missing”, I’m not sure about this.</p>
<p>How do I implement the workflow mentioned in the example?</p>
<p>Hope you can help,<br>
Mauro</p>

---

## Post #2 by @mau_igna_06 (2024-10-11 20:31 UTC)

<p>I don’t have 3 classes like in the example, I have around 30.<br>
I think, there is no documentation in the use of “unset”, “reset” or “missing” for control points, or markups edition by code.<br>
Anyway, I will just create 30 markupFiducialNodes with one control point each for my use case</p>

---

## Post #3 by @mikebind (2024-10-11 21:52 UTC)

<p>Have you looked at making a markups template?  <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#creating-template-landmarks" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a><br>
It would provide some of the features you are looking for.</p>

---
