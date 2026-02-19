---
topic_id: 29429
title: "How Can I Do Fiducial Registration Using Python"
date: 2023-05-12
url: https://discourse.slicer.org/t/29429
---

# How Can I Do Fiducial Registration using Python?

**Topic ID**: 29429
**Date**: 2023-05-12
**URL**: https://discourse.slicer.org/t/how-can-i-do-fiducial-registration-using-python/29429

---

## Post #1 by @Berk_Gezgin (2023-05-12 14:43 UTC)

<p>I want to merge a DICOM and STL file with the Fiducial Registration method in Python. The files will be opened in an interface, an equal number of points will be placed on the models and merged based on those points. Is it possible to do this in Python? Is there any repo, keyword etc. that you can recommend?</p>

---

## Post #2 by @lassoan (2023-05-13 12:44 UTC)

<p>I would recommend to use SlicerIGT module’s Fiducial Registration Wizard module to do this. All you need to do is to add the input markup fiducial list nodes, the output transform node, and a vtkMRMLFiducialRegistrationWizardNode to the scene and set their parameters.</p>

---

## Post #3 by @Berk_Gezgin (2023-05-16 12:32 UTC)

<p>Thank you for your answer.</p>
<p>Is it possible to run this in a separate Python script from the Slicer programme? I’m working on a web based project where Fiducial Registration is a part of it, so I can’t use Slicer directly. Is it possible to install Slicer in a virtual environment? If not, what do you recommend as a separate method?</p>
<p>I also converted two STL files to PCD and merged them with the ICP algorithm, but I think this method is not useful. Because I want to merge a DICOM and STL file, not convert it to PCD.</p>
<p>Thank you again for your help!</p>

---

## Post #4 by @lassoan (2023-05-16 12:55 UTC)

<p>Yes, you can use all Slicer features without using the GUI. For example, you can run Slicer in a docker container (or directly on the host) and use its <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#remote-control">REST API to execute any commands</a>. Using the REST API has the advantage that you can achieve interactive update rates (dozens of command executions per second) even when you operate on large, complex data. If you start Slicer executable or a CLI module for each operation then you need to perform several additional time-consuming steps (write the inputs to file, wait for the executable to start, read data, and after the computation write data to file, and read the results from file). Slicer provides its own virtual Python environment, so you don’t need to install any Python distributions.</p>
<p>For more complex operations, you can also expose the entire interactive Slicer GUI in the web browser using novnc and websockets.</p>

---

## Post #5 by @Berk_Gezgin (2023-05-16 14:48 UTC)

<p>I’m relatively new to these topics. The project I’m working on will be developed using Django. Unfortunately, I don’t have an environment where I can run 3D Slicer. I need to set up my own virtual environment, install Slicer, and be able to invoke and use it. I also need to definite points on 3D images within Django. Fiducial registration should also be done within Django. Additionally, I require a tool in Django that allows me to view the results in the Axial, Sagittal, and Frontal planes.</p>

---

## Post #6 by @lassoan (2023-05-16 16:54 UTC)

<aside class="quote no-group" data-username="Berk_Gezgin" data-post="5" data-topic="29429">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/berk_gezgin/48/65862_2.png" class="avatar"> Berk_Gezgin:</div>
<blockquote>
<p>I don’t have an environment where I can run 3D Slicer</p>
</blockquote>
</aside>
<p>What is your environment? Why do you think you cannot run 3D Slicer in your environment?</p>
<p>As I described above, you don’t need to run Slicer as an interactive a GUI application, but you can use it as a web service.</p>

---

## Post #7 by @RafaelPalomar (2023-05-16 17:30 UTC)

<p>Hello,</p>
<p>below there is a link to a python implementation of the rigid body transformation algorithm (with reference to the paper). I implemented this long ago, but the code is simple (it may be still python 2 code), maybe you can make use of it</p>
<p><a href="https://gist.github.com/RafaelPalomar/e16030789f0a6c7fd0ab7a6151c85c95" rel="noopener nofollow ugc">https://gist.github.com/RafaelPalomar/e16030789f0a6c7fd0ab7a6151c85c95</a></p>

---
