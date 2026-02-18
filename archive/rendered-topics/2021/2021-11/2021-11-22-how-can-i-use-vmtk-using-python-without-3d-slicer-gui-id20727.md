# How can I use vmtk using python without 3D slicer GUI?

**Topic ID**: 20727
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/how-can-i-use-vmtk-using-python-without-3d-slicer-gui/20727

---

## Post #1 by @Amira_Noaman (2021-11-22 14:46 UTC)

<p>Hello everyone,<br>
I’ve just started using vmtk package in python. (windows OS).<br>
I’m not willing to use the GUI provided by 3D slicer now, I’ll be building the complete project with python code, is it possible? and if yes, may someone help me load dicom images?</p>
<p>Here’s the error message:</p>
<p>vmtkimagereader -ifile “patient\IMG0001.dcm” --pipe vmtkimagereader<br>
^<br>
SyntaxError: invalid syntax</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-11-22 18:38 UTC)

<p>I would recommend to get started with the Slicer GUI (if a GUI exists for the function you need). When you know exactly what you want to do and how then you can automate things using pure Python scripting. I’m not sure exactly what is the state of VMTK’s Python wrapping and availability in PyPI and conda, it may be available, and you may be able to make the VTK classes or even the PypeS interface work, but that is just way more difficult than installing VMTK with a few clicks in Slicer, segment the input image using Segment Editor, then extract centerline and compute metrics with another few clicks.</p>
<p>What is the end goal of the project? What is the specify task that you would like address first?</p>

---

## Post #3 by @Amira_Noaman (2021-11-23 00:06 UTC)

<p>Hello,<br>
We actually used 3D slicer before &amp; also Pyepad and they were very efficient, but using a pure python code for the job is a requirement for our thesis but we faced some difficulties so I was willing to find anyone here who used this before. The aim is to obtain the hessian analysis &amp; the eigenvectors and eigenvalues at each point of the image. I tried multiple approaches like downloading the vmtk as a package and activated an anaconda virtual environment and tried to access it in visual studio code where ‘import vmtk’ worked but it couldn’t read the modules like vmtkimagereader</p>

---

## Post #4 by @lassoan (2021-11-23 06:56 UTC)

<p>If all the features that you need work in Slicer then the simplest is to run VMTK in Slicer’s Python environment. You can either use the Slicer modules without GUI (just calling methods of module logic classes - see a complete example <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/041759968f0e39c11302e7ffdbfc973d3b83ff20/ExtractCenterline/ExtractCenterline.py#L1157-L1188">here</a>) or just use Python-wrapped VTK classes. PypeS interface may work, too, I have never tried those (they add a layer between you and VMTK classes, so it is harder to see what is actually happening), just used those as examples.</p>

---

## Post #5 by @Amira_Noaman (2021-11-23 18:00 UTC)

<p>First, I want to thank you so much for your replies, I really appreciate it <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=10" title=":pray:" class="emoji" alt=":pray:">.<br>
Can you please elaborate what are Python-wrapped VTK classes?</p>

---

## Post #6 by @lassoan (2021-11-23 19:15 UTC)

<p>All VMTK classes are Python-wrapped and readily available in the Python environment that Slicer provides. See an example <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/041759968f0e39c11302e7ffdbfc973d3b83ff20/ExtractCenterline/ExtractCenterline.py#L509-L513">here</a>.</p>

---

## Post #7 by @tigerhu7 (2022-09-15 01:18 UTC)

<p>Hello Amira,<br>
Have you tried using pypes?<br>
<a href="http://www.vmtk.org/tutorials/PypesProgrammatically.html" rel="noopener nofollow ugc">vmtk-pypes</a><br>
Even though it is not ‘pure python functions’, but ‘pypes wrapped functions’.</p>

---
