---
topic_id: 3608
title: "Extracting Centerlines Of A Cad Model Through A Python Scrip"
date: 2018-07-30
url: https://discourse.slicer.org/t/3608
---

# Extracting Centerlines of a CAD Model Through a Python Script in Slicer

**Topic ID**: 3608
**Date**: 2018-07-30
**URL**: https://discourse.slicer.org/t/extracting-centerlines-of-a-cad-model-through-a-python-script-in-slicer/3608

---

## Post #1 by @sisyphus_s (2018-07-30 09:16 UTC)

<p>Hello there,</p>
<p>I am very new and novice to Slicer. The project that I am currently involved with requires me to extract the center line of the 3D body organ’s model (e.g., intestine, etc.). More specifically, I need to prepare a python script whose output is the center line of a given model.</p>
<p>I am aware of “Vascular Modeling Toolkit” and its accompanied CenterLineComputation module. However, problems that I am currently facing are:</p>
<ol>
<li>When I use this addson and subsequently, generate and save the .vtk center line of the 3D model, the .vtk object is empty.</li>
<li>I need to find a tutorial to learn on how to write python extension (preferably extensions) under Slicer to automate the center line computation and saving the resulting center line.</li>
</ol>
<p>I will be grateful if you can kindly assist me on finding my right starting point.</p>
<p>I highly appreciate your cooperation.</p>
<p>Sincerely,<br>
Soheil</p>

---

## Post #2 by @lassoan (2018-07-30 10:28 UTC)

<p>You can segment the intestines using Segment Editor, then export the segment to labelmap, and get centerline points as markup fiducials using Extract skeleton module. You can create smooth line from markups using Markups to model extension. You need to use a recent <em>nightly</em> version of Slicer.</p>

---

## Post #3 by @sisyphus_s (2018-08-01 15:02 UTC)

<p>Dear Andras Lasso,</p>
<p>I am thankful for your kind reply and instructions for exporting the centerline. It is, indeed, very helpful.</p>
<p>However, it appears to be through the use of GUI. I highly appreciate it if you kindly advise how I may do this process through a Python script.</p>
<p>I thank you for your time and kind cooperation and look forward to hearing from you.</p>
<p>Sincerely,</p>
<p>Soheil</p>

---

## Post #4 by @lassoan (2018-08-02 07:31 UTC)

<p>All operations that are available through the GUI can be performed using Python scripting, too. You can run CLI module (such as “Extract skeleton”) from Python as <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">described here</a>. If you have issues figuring out how to perform any particular operation from Python then let us know.</p>

---

## Post #5 by @sisyphus_s (2018-08-27 05:29 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for your kind responses to my previous inquiries. I have been able to extract the centerlines from a 3D CAD model.</p>
<p>At this point, I need to do the same thing using a medical image. Is the “Centerline Computation” from Vascular Modeling Toolkit still applicable for medical images or there is another package/extension I need to use for this purpose. I am asking this question since all my attempt for using the aforementioned package on a .mrb image results in crashing the Slicer (the pop-up window with a message “Slicer stopped …”).</p>
<p>I thank you for your time and kind cooperation and look forward to hearing from you.</p>
<p>Sincerely,<br>
Soheil</p>

---

## Post #6 by @albert94 (2019-02-11 06:40 UTC)

<p>Hi, Soheil<br>
Have you solved your problem that the centerline computation causes crashing the Slicer? I encountered the same crashing Slicer problem when I used the centerline computation.</p>

---
