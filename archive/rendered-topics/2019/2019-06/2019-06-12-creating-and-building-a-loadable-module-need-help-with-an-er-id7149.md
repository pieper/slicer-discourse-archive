---
topic_id: 7149
title: "Creating And Building A Loadable Module Need Help With An Er"
date: 2019-06-12
url: https://discourse.slicer.org/t/7149
---

# Creating and building a Loadable Module: need help with an error

**Topic ID**: 7149
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/creating-and-building-a-loadable-module-need-help-with-an-error/7149

---

## Post #1 by @JamesCTilton (2019-06-12 22:21 UTC)

<p>Operating system: Red Hat Linux 7.6<br>
Slicer version: 4.10.2<br>
Expected behavior: A successful build of a test program<br>
Actual behavior:</p>
<p>I would like to create my own C++ application that calls Slicer<br>
functions with the C++ API.</p>
<p>From my reading of the documentation, it appears that to do this<br>
I need to create a Loadable Module. I attempted to do this using the<br>
Extension Wizard Module in Slicer.</p>
<p>The steps I took were:</p>
<p>Click ‘Create Extension’</p>
<p>Named my extension ‘SlicerTest’<br>
Used Type ‘default’<br>
Destination: /home/jtilton/src/SlicerPrograms</p>
<p>Clicked ‘Add module to extension’</p>
<p>Named it ‘SlicerTest’<br>
Type: loadable</p>
<p>Went to /home/jtilton/src/SlicerPrograms/SlicerTest/SlicerTest</p>
<p><span class="math"> mkdir build
</span> cd build<br>
$ cmake …</p>
<p>Got the error:<br>
CMake Error at Logic/CMakeLists.txt:20 (SlicerMacroBuildModuleLogic):<br>
Unknown CMake command “SlicerMacroBuildModuleLogic”.</p>
<p>Where did I go wrong?</p>
<p>Am I completely off base, or did I just miss some small thing?</p>

---

## Post #2 by @jcfr (2019-06-12 22:53 UTC)

<p>Hi James,</p>
<p>To build a loadable module (which is a plugin that can be loaded by Slicer),  you need to first have a build tree of Slicer.</p>
<p>You will then configure the SlicerTest module passing -DSlicer_DIR:PATH=/path/to/Slicer-build/Slicer-build</p>
<p>Once the module is built, the build tree will have a folder of the form /path/to/SlicerTest-build/lib/Slicer-4.11/qt-loadables-modules that contains the the plugin to be loaded.</p>
<p>This is the path to pass to Slicer using the additional-path option.</p>
<p>To save the trouble of passing option to Slicer, you should find a convenience launcher called “SlicerWithNameOfExtension” in the module build tree, starting this should be enough to start Slicer with you module loaded.</p>
<p>I suggest you read these two pages:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F</a></p>
<p>Hth</p>
<p>Jc</p>

---

## Post #3 by @JamesCTilton (2019-06-13 12:07 UTC)

<p>Thank you.</p>
<p>After I posted my questions, I found the instructions:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a></p>
<p>But your instructions are clearer and more direct.</p>
<p>Jim Tilton</p>

---

## Post #4 by @leemoncn (2020-01-19 09:01 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
I have the same problem.<br>
I used the same operation as JamesCTilton to create the module<br>
I run command    cmake -DSlicer_DIR:PATH=C:\S4R\Slicer-build …/<br>
It still error:<br>
CMake Error at Logic/CMakeLists.txt:20 (SlicerMacroBuildModuleLogic):<br>
Unknown CMake command “SlicerMacroBuildModuleLogic”.</p>
<p>Am i miss something?</p>

---
