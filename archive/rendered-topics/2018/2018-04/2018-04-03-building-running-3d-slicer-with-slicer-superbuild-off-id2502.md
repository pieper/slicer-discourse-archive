---
topic_id: 2502
title: "Building Running 3D Slicer With Slicer Superbuild Off"
date: 2018-04-03
url: https://discourse.slicer.org/t/2502
---

# Building/Running 3D slicer with Slicer_SUPERBUILD=OFF

**Topic ID**: 2502
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/building-running-3d-slicer-with-slicer-superbuild-off/2502

---

## Post #1 by @RafaelPalomar (2018-04-03 14:23 UTC)

<p>Hi everyone,</p>
<p>I’ve managed to build 3DSlicer without the super-build mode by packaging/installing some of the underlying libraries for my Linux OS (Gentoo) and using some of the system libraries. After setting up the LD_LIBRARY_PATH and PYTHONPATH variables I’m able to start 3DSlicer but I get this error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/usr/lib/Slicer-4.8/qt-scripted-modules/DICOM.py", line 41, in __init__
    if slicer.mrmlScene.GetTagByClassName( "vtkMRMLScriptedModuleNode" ) != 'ScriptedModule':
AttributeError: 'vtkCommonCorePython.vtkObject' object has no attribute 'GetTagByClassName'
qSlicerPythonCppAPI::instantiateClass  - [ "DICOM" ] - Failed to instantiate scripted pythonqt class "DICOM" 0x7fb2fd398db8 
Fail to instantiate module  "DICOM" 
</code></pre>
<p>The symbol GetTagByClassName seems to have been built:</p>
<pre><code class="lang-auto">find -name "*.so" -exec nm --print-file-name {} \; | grep GetTagByClass

./bin/libMRMLCorePythonD.so:00000000001370e1 t _ZL32PyvtkMRMLScene_GetTagByClassNameP7_objectS0_
./bin/libMRMLCorePythonD.so:                 U _ZN12vtkMRMLScene17GetTagByClassNameEPKc
./bin/libqMRMLWidgets.so:                 U _ZN12vtkMRMLScene17GetTagByClassNameEPKc
./bin/libMRMLCore.so:0000000000550d0a T _ZN12vtkMRMLScene17GetTagByClassNameEPKc
</code></pre>
<p>Any ideas? Thanks in advance.</p>
<p>Best regards,<br>
Rafael Palomar</p>

---

## Post #2 by @pieper (2018-04-03 15:43 UTC)

<p>This indicates that the python-wrapped slicer libraries aren’t being loaded (perhaps they aren’t in the path where expected) so the MRML nodes, which are vtkObject subclasses, are only seen as vtkObjects.  Maybe easiest would be to compare you build layout to a SuperBuild layout and see where the differences are.  Either adjust the directory tree or the launcher paths should make it workable.</p>

---

## Post #3 by @jcfr (2018-04-03 18:12 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="1" data-topic="2502">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>build 3DSlicer without the super-build mode by packaging/installing some of the underlying libraries for my Linux OS (Gentoo) and using some of the system libraries.</p>
</blockquote>
</aside>
<h3><a name="p-10197-the-slicer_use_system_packagename-options-1" class="anchor" href="#p-10197-the-slicer_use_system_packagename-options-1" aria-label="Heading link"></a>the “Slicer_USE_SYSTEM_&lt;packageName&gt;” options</h3>
<p>Not sure if this is something you already figure out but you can build Slicer by specifying <code>Slicer_USE_SYSTEM_&lt;packageName&gt;</code> option when configuring it for any of the project associated with an <code>External_&lt;packageName&gt;</code> found in the <a href="https://github.com/Slicer/Slicer/tree/master/SuperBuild">SuperBuild</a> directory.</p>
<p>Looking at each individual <code>SuperBuild/External_*.cmake</code> file should also give some insight.</p>
<p>Using this approach will for example allow you to use VTKv9 on the system while ensuring the application launcher is downloaded and configured.</p>
<p>Also configuring with <code>Slicer_USE_SYSTEM_VTKv9</code> set to <code>ON</code> will also automatically require python to be on the system and ensure the launcher settings are configured accordingly.</p>
<p>To conclude:</p>
<ul>
<li>
<p>just starting Slicer using <code>bin/SlicerApp-real</code> is usually not recommended (unless you explicitly ensure the environment is correct).</p>
</li>
<li>
<p>I would also  recommend against setting <code>Slicer_USE_SUPERBUILD</code> to <code>OFF</code>, instead prefer setting the <code>Slicer_USE_SYSTEM_*</code> options</p>
</li>
</ul>

---

## Post #4 by @RafaelPalomar (2018-04-04 07:00 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/jcfr">@jcfr</a> for the tips. I’ll explore the alternatives you proposed; hopefully I can come up with a solution and post it here.</p>
<p>Best,<br>
Rafael.</p>

---

## Post #5 by @RafaelPalomar (2018-11-02 12:11 UTC)

<p>Hello,</p>
<p>I managed to build the packages in the superbuilld separately and get them installed. Then I also got 3D Slicer to build using the system libraries (I still have Slicer_USE_SUPERBUILD=OFF…having a superbuild was problematic for installing the packages). Now I am at the point where all dependences are installed in their own directory in /usr/lib64, in addition, 3D Slicer is installed in /usr.</p>
<p>Now the problem I’m facing is that when launching 3D Slicer (it does not matter if I use the launcher or just SlicerApp-real), required .so and .py libraries are not found. The problem is gone if I manually set PYTHONPATH and LD_LIBRARY_PATH.</p>
<p>Do you have any ideas on how to preserve the installation RPATH when building 3D Slicer?</p>
<p>Thanks in advance!</p>
<p>Best,<br>
Rafael.</p>

---

## Post #6 by @jcfr (2018-11-02 15:05 UTC)

<p>Thanks for the update <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<h3><a name="p-17312-make-install-with-superbuild-1" class="anchor" href="#p-17312-make-install-with-superbuild-1" aria-label="Heading link"></a>make install with superbuild</h3>
<blockquote>
<p>having a superbuild was problematic for installing the packages</p>
</blockquote>
<p>You could run <code>make install</code> from <code>Slicer-SuperBuild/Slicer-build</code></p>
<h3><a name="p-17312-rpath-2" class="anchor" href="#p-17312-rpath-2" aria-label="Heading link"></a>RPATH</h3>
<blockquote>
<p>preserve the installation RPATH when building 3D Slicer?</p>
</blockquote>
<p>I suggest you look at <a href="https://gitlab.kitware.com/cmake/community/wikis/doc/cmake/RPATH-handling" class="inline-onebox">Verifying connection...</a></p>
<h3><a name="p-17312-pythonpath-3" class="anchor" href="#p-17312-pythonpath-3" aria-label="Heading link"></a>PYTHONPATH</h3>
<blockquote>
<p>I manually set PYTHONPATH</p>
</blockquote>
<p>The launcher settings are used by both the launcher and the application to set env. variable. For example, in a macOS package, the launcher settings are used. That way settings are consistently manage.</p>
<p>The same could be done on Linux.</p>
<p>If not already read by the launcher, here is where the launcher settings are loaded from the application:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/01c28f0e8fbd2c169053a4a82af490f19c43b9ac/Base/QTCore/qSlicerCoreApplication.cxx#L237-L243" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/01c28f0e8fbd2c169053a4a82af490f19c43b9ac/Base/QTCore/qSlicerCoreApplication.cxx#L237-L243</a></p>
<p>Based on where the settings are installed on the system, we should tweak the following code:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/01c28f0e8fbd2c169053a4a82af490f19c43b9ac/Base/QTCore/qSlicerCoreApplication.cxx#L1161-L1173" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/01c28f0e8fbd2c169053a4a82af490f19c43b9ac/Base/QTCore/qSlicerCoreApplication.cxx#L1161-L1173</a></p>

---
