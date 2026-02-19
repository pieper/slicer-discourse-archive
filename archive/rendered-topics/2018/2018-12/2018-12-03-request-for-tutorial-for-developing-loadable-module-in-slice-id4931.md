---
topic_id: 4931
title: "Request For Tutorial For Developing Loadable Module In Slice"
date: 2018-12-03
url: https://discourse.slicer.org/t/4931
---

# Request for Tutorial for Developing Loadable Module in Slicer

**Topic ID**: 4931
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/request-for-tutorial-for-developing-loadable-module-in-slicer/4931

---

## Post #1 by @zhenyu1995 (2018-12-03 02:56 UTC)

<p>Dear all,</p>
<p>My name is Ong Zhen Yu, a Malaysian undergraduate, pursuing bachelor’s degree in electrical and electronics. Currently, me and my team are working on a project to develop a loadable module in slicer to do auto-registration in 3D Slicer.</p>
<p>The purpose of this module is to input a STL model (which is previously extracted out from DICOM using threshold feature) and a Fiducial list (created by open-source face recognition system on RGBD camera) to do auto-registration and output a transform file which will display the linear transformation in terms of matrix elements.</p>
<p>However, we are having a problem of how to actually code the loadable module. We don’t know where to start and how should we connect between module file, logic file and module widget file. We had successfully create a widget using command Slicer.exe --designer but the widget created could not accept the STL model in slicer. And there is no clear tutorial or solution on the internet.</p>
<p>We will highly appreciate it if anyone could provide a clear guide on how to code loadable module and connect between the .h file and .cxx file. as we are still new to slicer coding. Thank you very much.</p>

---

## Post #2 by @jcfr (2018-12-03 04:36 UTC)

<p>Thanks for reaching out.</p>
<p>To get familiar with the extension manager and creating new modules, did you get a chance to go this tutorial: <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Developing_and_contributing_extensions_for_3D_Slicer" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Developing_and_contributing_extensions_for_3D_Slicer</a></p>

---
