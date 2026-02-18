# Alveolar inferior nerve displacement study

**Topic ID**: 27054
**Date**: 2023-01-05
**URL**: https://discourse.slicer.org/t/alveolar-inferior-nerve-displacement-study/27054

---

## Post #1 by @TomB (2023-01-05 13:48 UTC)

<p>Hello,</p>
<p>I am trying to study the alveolar nerve displacement before and after wisdom teeth extraction.<br>
The first solution that came to me was to superimpose the two Dicoms with a landmark registration and then measure the disp’acement with the ruler tool. But this solution was not precise enough…<br>
So I tried to segment both AINs to create two STL models and then do a surface registration.<br>
But I have a lot of difficulties analysing the displacement with segment statistics…</p>
<p>Could you help me with segment statistics?<br>
Do you have an other idea on how to analyse the AIN displacement accurately and efficiently  ?</p>
<p>Thank you for your advice!</p>

---

## Post #2 by @cpinter (2023-01-07 10:15 UTC)

<p>You could try measuring their displacement with the Segment Comparison module in the SlicerRT extension. The Hausdorff metrics tells you maximum and average distances in mm.</p>

---
