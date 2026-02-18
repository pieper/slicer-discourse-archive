# Dual energy series reconstruction

**Topic ID**: 4136
**Date**: 2018-09-18
**URL**: https://discourse.slicer.org/t/dual-energy-series-reconstruction/4136

---

## Post #1 by @opetne (2018-09-18 07:50 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
Hi folks!</p>
<p>I have a series of dog contrast head CT, made on Siemens Definition Flash with dual energy. I’d like to reconstruct the vasculature only. Do you have any suggestions how to do this? I could do the recons with the Syngovia so far but I’d like to make it with the Slicer. Is there any special module for that?<br>
I can make the series available if you’d like.</p>

---

## Post #2 by @lassoan (2018-09-18 19:32 UTC)

<p>Simple image subtraction using “Subtract scalar volumes” should work.</p>
<p>Most often there are submillimeter displacements between the images (even for cadavers, due to table motion, vibration, etc.) which cause subtraction artifacts at high-contrast areas - typically at bone edges. To suppress these artifacts, you need to use retrospective motion correction by spatially aligning the two volumes.</p>
<p>If your scanner or workstation software does not perform motion-correction on the exported images then you can do that in Slicer using SlicerElastix module.</p>

---

## Post #3 by @opetne (2018-09-20 12:41 UTC)

<p>Dear Andras,</p>
<p>I did the substracion but seems that it is not the solution for this case. For me it looks like that the bone and the contrast filled vessels are substracted from the series. My goal was to create an image what the original software does with a dual energy series that only the bones are substracted. In my case the filling of the arteries are not so well andt therefore I’d liek to substract the bones only and reconstruct the vasculature, if it’s possible.</p>
<p>Ors</p>

---
