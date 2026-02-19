---
topic_id: 18183
title: "Where Is The Code For Computation Of Centerline"
date: 2021-06-17
url: https://discourse.slicer.org/t/18183
---

# Where is the code for computation of centerline?

**Topic ID**: 18183
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/where-is-the-code-for-computation-of-centerline/18183

---

## Post #1 by @Bastien_Saunois (2021-06-17 12:37 UTC)

<p>Hi,</p>
<p>I am trying to use VMTK to compute the centerline of a hollowed cylinder with Python. But I can’t find the code responsible of computing the centerline.<br>
Could someone guide me to this certain code?</p>
<p>I would appreciate any help!</p>
<p>Thanks,</p>
<p>Bastien</p>

---

## Post #2 by @lassoan (2021-06-17 13:35 UTC)

<p><a href="https://github.com/vmtk/vmtk/tree/master/vtkVmtk">These C++ classes</a> are used from <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">this Python script</a> to get the vessel centerline. Probably the easiest is to get started with the VMTK GUI in 3D Slicer. If you find the code hard to interpret, then you can run the Extract Centerline module step by step using a Python debugger. You can find detailed description of all algorithmic details of VMTK in <a href="http://lantiga.github.io/media/AntigaPhDThesis.pdf">Luca Antiga’s PhD thesis</a>.</p>

---

## Post #3 by @Bastien_Saunois (2021-06-17 15:22 UTC)

<p>Thanks a lot for the scripts <a class="mention" href="/u/lassoan">@lassoan</a> !</p>
<p>Is it possible to use the centerline extraction without slicer?<br>
In my case I created the mesh of my cylinder on vtk and I want to extract the centerline of it without using slicer. I found <a href="https://github.com/vmtk/vmtk/blob/master/vmtkScripts/vmtkcenterlines.py" rel="noopener nofollow ugc">this python code</a> this morning, do you think it is worth exploring this script or not ?</p>

---

## Post #4 by @lassoan (2021-06-17 15:45 UTC)

<p>Yes, sure you can extract the centerline using VMTK classes in any environment, in any programming language.</p>
<p>The script that I linked implements a complete solution. It lets the user select input mesh or segmentation, performs all necessary preprocessing (to make sure that the computation is fast and robust), automatically detects vessel endpoints, allows the user adjust the endpoints (add/delete/move, specify inflow/outflow direction), computes the centerline and basic metrics, and displays results. All the GUI related features require 3D Slicer, but if you have your own GUI then you can rewrite those parts.</p>
<p>vmtkScripts/vmtkcenterlines.py is good, but it contains only the computation of the centerline, so you need to add a lot of things to get a complete solution. You can find other very useful code snippets for that in the same folder, but they still don’t contain everything (such as robust preprocessing and automatic centerline endpoints computation); and interactive GUI examples are extremely limited.</p>

---

## Post #5 by @Bastien_Saunois (2021-06-18 08:19 UTC)

<p>Thank you for taking the time to answer my questions. It is much clearer for me!</p>

---
