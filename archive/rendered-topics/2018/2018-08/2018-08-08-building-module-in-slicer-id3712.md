---
topic_id: 3712
title: "Building Module In Slicer"
date: 2018-08-08
url: https://discourse.slicer.org/t/3712
---

# Building Module in Slicer

**Topic ID**: 3712
**Date**: 2018-08-08
**URL**: https://discourse.slicer.org/t/building-module-in-slicer/3712

---

## Post #1 by @kamrul079 (2018-08-08 20:14 UTC)

<p>I am developing a 3D slicer module for augmented reality application for the video based navigation system. I had already built slicer 4.8.1 from the source file using Cmake and visual studio 2013 version. I had built slicer.exe file. But after that how to build a module and add up the camera (NDI Polaris)? I don’t know how to do that.  Is there any tutorial so that I can do that by myself?</p>

---

## Post #2 by @Sam_Horvath (2018-08-08 20:37 UTC)

<p>Here an an intro tutorial for programming python modules: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial</a></p>
<p>This page has an overview of the different types of modules, with guides for getting started for the different types:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules</a></p>
<p>For connecting to the NDI Polaris, the best approach would be the SlicerOpenIGTLink extension (<a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink</a>, available in the extension manager) with PLUS Toolkit handling the interaction with the camera (<a href="https://plustoolkit.github.io/" rel="nofollow noopener">https://plustoolkit.github.io/</a>, <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceNDI.html</a>)</p>
<p>The SlicerIGT extension (<a href="http://www.slicerigt.org/wp/" rel="nofollow noopener">http://www.slicerigt.org/wp/</a>) may also have some good resources, depending on what you are trying to do.</p>

---
