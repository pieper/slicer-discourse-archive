# Building an extension

**Topic ID**: 19823
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/building-an-extension/19823

---

## Post #1 by @Aamir_Khan (2021-09-23 11:09 UTC)

<p>Hi,</p>
<p>I am trying to develop an extension. Here, I would select three fiducial points and on pressing an apply button the volume would transform to a customized coordinate frame. I have developed the logic and it works as intended in the command line interface of the Slicer. But I am facing difficulty in making the widget for the same. I have tried to find solutions for the same and also went through the tutorials suggested, but to no avail.</p>
<p>It would be really helpful if anyone could suggest me some extensions in Python which I could look at to get more understanding for this?</p>
<p>Thanks.</p>

---

## Post #2 by @Alex_Vergara (2021-09-23 12:08 UTC)

<p>You may want to look at <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/OpenDose3D/Gamma.py" rel="noopener nofollow ugc">this subextension</a></p>

---

## Post #3 by @mikebind (2021-09-23 17:35 UTC)

<p>As a suggestion, use the “Extension Wizard” module form the “Developer Tools” extension.  It will create a working python module which includes an “Apply” button and helpful comments and example code in that module.  Then you can modify that module incrementally to get it to function the way you want your module to work. For example, you can paste your working logic functions into the logic of the template module and change it so that pressing the “Apply” button runs your logic instead of the template function. Also, the easiest way to create the UI you want is to start with this template module open in Slicer and then click “Edit UI” in the “Reload and Test” section at the top of the module.  This will launch QtDesigner, where you can modify the UI as you wish in a relatively straightforward graphical way. If you don’t see the “Reload and Test” section at the top of the template module, it is because you have not enabled “Developer Mode”, which you can do by Edit menu → Application Settings → Developer → check the box next to Enable Developer Mode.</p>

---

## Post #4 by @Aamir_Khan (2021-09-23 18:05 UTC)

<p>Thanks Alex, for the link. It proved quite helpful in progressing with my workflow.</p>
<p>I am still trying to figure out how to present the option of selecting a point by clicking on the CT volume, in my widget extension.</p>
<p>Thanks.</p>

---

## Post #5 by @mikebind (2021-09-23 21:41 UTC)

<p>You can use a qSlicerMarkupsPlaceWidget in your module for easy interactive point placement.  Helpful resources available <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html" rel="noopener nofollow ugc">here</a> and <a href="https://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html" rel="noopener nofollow ugc">here</a>.</p>

---
