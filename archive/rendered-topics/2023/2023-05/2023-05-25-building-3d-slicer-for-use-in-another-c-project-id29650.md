# Building 3D Slicer for use in another C++ project

**Topic ID**: 29650
**Date**: 2023-05-25
**URL**: https://discourse.slicer.org/t/building-3d-slicer-for-use-in-another-c-project/29650

---

## Post #1 by @Robotech7 (2023-05-25 15:10 UTC)

<p>Hello, please let me know if it is possible to build the 3D Slicer source code as libraries for reuse in another C++ project without significant modifications to the CMakeLists.txt files. I only need the /Modules/Loadable directory and MRML. Currently, the build wraps the C++ code for use in Python. Is it also possible to do the same for C++?</p>

---

## Post #2 by @lassoan (2023-05-25 15:22 UTC)

<p>MRML core library is independent from the Slicer application and just depends on VTK, ITK and maybe a few other commonly used basic libraries. It would be easy to carve it out and use it in another application. In fact, we plan to do this within 1-2 years (and make MRML available on PyPI to make it easily usable in any Python-based project).</p>
<p>Slicer loadable modules (/Modules/Loadable folder content) rely on the Slicer application, so probably the easiest way to reuse it in another project is to port the existing code into Slicer modules.  Alternatively, you can launch a Slicer application and run the loadable modules in that process. You can disable all modules that you don’t need, but slicer startup can still take several seconds (and it may take some time to read all the input data), so if you need to perform quick operations frequently then it may be better to launch Slicer once and keep it running, and use its REST API, OpenIGTLink, or other interprocess communication methods to operate it.</p>

---

## Post #3 by @Robotech7 (2023-05-26 01:23 UTC)

<p>Thank you for your quick response, we have another question. Is it possible to build and reuse the code in Modules/Loadable/Markups/VtkWidgets in a project that is based on pure VTK and ITK? We need this to build web assembly (wasm) widgets from a slicer. Building pure VTK and ITK is very easy to do in web assembly (wasm), but there are problems when using the C++ code of Slicer.</p>

---

## Post #4 by @lassoan (2023-05-26 03:27 UTC)

<p>In Slicer, VTK widgets and logic classes are well isolated from Qt GUI classes, so it should be possible to just extract VTK widgets and all classes they use and add it to your application. It is not trivial, as you may need to bring in a few hundred classes (MRML core, displayable managers, module MRML and logic classes).</p>

---

## Post #5 by @Robotech7 (2023-05-26 04:42 UTC)

<p>Thank you for your response. Could you please provide any examples of displaying widgets from Modules/Loadable/Markups/VtkWidgets? We need this example to build our application and also to understand how and where the interaction with MRML occurs.</p>

---

## Post #6 by @lassoan (2023-05-26 04:50 UTC)

<p>There are no standalone examples. You can see how these classes are used in 3D Slicer.</p>

---

## Post #7 by @jcfr (2023-05-26 06:53 UTC)

<aside class="quote no-group" data-username="Robotech7" data-post="3" data-topic="29650">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/robotech7/48/66115_2.png" class="avatar"> Robotech7:</div>
<blockquote>
<p>a project that is based on pure VTK and ITK? We need this to build web assembly (wasm) widgets from a slicer. Building pure VTK and ITK is very easy to do in web assembly (wasm),</p>
</blockquote>
</aside>
<p>Worth noting that we (<a class="mention" href="/u/thewtex">@thewtex</a> with help of many) have been working on infrastructure to build VTK &amp; ITK classes to webassembly. To learn more you should look into the following:</p>
<ul>
<li><a href="https://wasm.itk.org/">https://wasm.itk.org/</a></li>
<li><a href="https://gitlab.kitware.com/vtk/vtk-wasm-docker">https://gitlab.kitware.com/vtk/vtk-wasm-docker</a></li>
</ul>
<p>This means that after we transition core Slicer component as independent VTK &amp; ITK packages, we will be able to have them published as both Python and npm packages.</p>
<p><a href="https://github.com/SCIInstitute/ITKCleaver">ITKCleaver</a> is an example this, it is now available on <code>PyPI</code> and <code>npm</code>:</p>
<ul>
<li><a href="https://itk-wasm-cleaver-typescript-docs.netlify.app/#/">https://itk-wasm-cleaver-typescript-docs.netlify.app/#/</a></li>
<li><a href="https://pypi.org/project/itk-cleaver/">https://pypi.org/project/itk-cleaver</a></li>
</ul>

---
