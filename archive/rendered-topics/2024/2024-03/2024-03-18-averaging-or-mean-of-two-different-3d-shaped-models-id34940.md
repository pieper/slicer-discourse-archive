# Averaging or Mean of two different 3D shaped models 

**Topic ID**: 34940
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/averaging-or-mean-of-two-different-3d-shaped-models/34940

---

## Post #1 by @Aadarsh_Salve (2024-03-18 02:52 UTC)

<p>Hello, I have two different shaped 3D models of Human Ears and I want to create an average /mean of them. Could you please help me out with the code or method to create it?</p>

---

## Post #2 by @edwardwang1 (2024-03-20 14:39 UTC)

<p>Hi,</p>
<p>SlicerSALT was mentioned in a previous thread (<a href="https://discourse.slicer.org/t/averaging-3d-models/6660" class="inline-onebox">"Averaging" 3D models</a>) but I don’t have personal experience with it.</p>
<p>For a research project previously, I’ve used the <a>GIAS2</a> package in Python to build a statistical shape model from a number of mandibles. One of the components of the shape model is an average structure. The only caveat is that I do not know if it will work with only 2 samples.</p>

---

## Post #3 by @Aadarsh_Salve (2024-03-22 19:52 UTC)

<p>Thank you so much for your help!</p>

---

## Post #4 by @Aadarsh_Salve (2024-03-26 21:27 UTC)

<p>Hi, can you help me out with the steps on how to get an average for multiple ear sample?</p>

---

## Post #5 by @muratmaga (2024-03-27 01:20 UTC)

<p>If you have landmarks, this is doable through the GPA module of SlicerMorph extension.</p>

---

## Post #6 by @edwardwang1 (2024-03-27 16:41 UTC)

<p>Hi,</p>
<p>In my project I exported my models as .ply files, and ran them through the GIAS2 pipeline, which is linked in my earlier post.</p>

---

## Post #7 by @Aadarsh_Salve (2024-03-27 17:57 UTC)

<p>Thanks, I’ll probably go through them and use them as a reference.</p>

---
