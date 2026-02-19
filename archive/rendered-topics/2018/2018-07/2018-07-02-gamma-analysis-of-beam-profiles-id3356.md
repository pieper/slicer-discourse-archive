---
topic_id: 3356
title: "Gamma Analysis Of Beam Profiles"
date: 2018-07-02
url: https://discourse.slicer.org/t/3356
---

# Gamma Analysis of beam profiles

**Topic ID**: 3356
**Date**: 2018-07-02
**URL**: https://discourse.slicer.org/t/gamma-analysis-of-beam-profiles/3356

---

## Post #1 by @AGul (2018-07-02 13:32 UTC)

<p>Hi.<br>
How Can I calculate gamma index of two beam profiles acquired with to different detectors in 3D slicer. I have data in MS excel.</p>

---

## Post #2 by @cpinter (2018-07-03 10:50 UTC)

<p>The Dose Comparison module in the SlicerRT extension calculates gamma index for dose volumes.</p>
<p>Is your data a dose distribution or a PDD-like 1D profile?</p>

---

## Post #3 by @AGul (2018-07-03 12:17 UTC)

<p>My data is 1 D distribution (PDD and Off axis profile) in MS Excel.</p>

---

## Post #4 by @cpinter (2018-07-03 12:23 UTC)

<p>There is no tool with user interface for that. We have two extensions for dosimetry: Gel Dosimetry Analysis and Film Dosimetry Analysis. They can take yo through the whole process, but even those cannot calculate gamma between two PDDs. However, it is an extremely simple calculation, which you can even do in Excel. You need to decide how much of your workflow you want to do in Slicer. If it’s way more than this comparison, then we can write a simple script that can do this. But since your data is in Excel, which Slicer cannot produce, it is probably mostly in Matlab + Excel.<br>
If you give us more information, then we can help, but at this point I can only do guesswork.</p>

---

## Post #5 by @AGul (2018-07-03 12:29 UTC)

<p>Thank you very much for your detailed reply. Can you please write a script in Excel, for example for Gamma (2%, 2mm), for me so that i can understand it. Thanking you in advance.</p>

---

## Post #6 by @cpinter (2018-07-03 14:26 UTC)

<p>This is the Slicer forum. For Excel questions, please ask for help on the Microsoft forums.</p>

---
