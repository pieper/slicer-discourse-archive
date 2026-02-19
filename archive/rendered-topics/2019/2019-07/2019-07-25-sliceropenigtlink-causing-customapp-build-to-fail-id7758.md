---
topic_id: 7758
title: "Sliceropenigtlink Causing Customapp Build To Fail"
date: 2019-07-25
url: https://discourse.slicer.org/t/7758
---

# SlicerOpenIGTLink causing CustomApp build to fail

**Topic ID**: 7758
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/sliceropenigtlink-causing-customapp-build-to-fail/7758

---

## Post #1 by @jamesobutler (2019-07-25 16:56 UTC)

<p>I’m trying to get a custom app to build with the SlicerOpenIGTLink remote extension included. However, I keep running into this CMake Error as seen below. If I comment out the SlicerOpenIGTLink specification in my customapp CMakeLists.txt the build completes successfully without errors.</p>
<pre><code class="lang-auto">56&gt;-- Configuring extension directory: SlicerOpenIGTLink
56&gt;-- Checking EXTENSION_NAME variable
56&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED
56&gt;-- Checking MODULE_NAME variable
56&gt;-- Checking MODULE_NAME variable - NOTDEFINED
56&gt;-- Checking PROJECT_NAME variable
56&gt;-- Checking PROJECT_NAME variable - SlicerOpenIGTLink
56&gt;-- Setting EXTENSION_NAME ......................: SlicerOpenIGTLink
56&gt;-- Checking EXTENSION_NAME variable
56&gt;-- Checking EXTENSION_NAME variable - SlicerOpenIGTLink
56&gt;-- Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h
56&gt;-- Looking for decorator header qSlicerOpenIGTLinkIFModuleWidgetsPythonQtDecorators.h - Not found
56&gt;-- Configuring Loadable module: OpenIGTLinkIF [qSlicerOpenIGTLinkIFModuleExport.h]
56&gt;CMake Error at C:/MyCustomApp/SlicerOpenIGTLink/OpenIGTLinkIF/Testing/CMakeLists.txt:29 (list):
56&gt;  list sub-command INSERT requires at least three arguments.
56&gt;
56&gt;
56&gt;-- Looking for decorator header qSlicerOpenIGTLinkRemoteModuleWidgetsPythonQtDecorators.h
56&gt;-- Looking for decorator header qSlicerOpenIGTLinkRemoteModuleWidgetsPythonQtDecorators.h - Not found
56&gt;-- Configuring Loadable module: OpenIGTLinkRemote [qSlicerOpenIGTLinkRemoteModuleExport.h]
</code></pre>
<p>I can also build the extension separately and targeting my regular Slicer build which used defaults CMakeLists.txt configuration.</p>
<p>So maybe there is some Slicer build subproject dependency that I need to have checked. Is there an easy way/suggested route for finding out what this may be? Or is my issue something else?</p>
<pre><code class="lang-auto">option(Slicer_BUILD_DICOM_SUPPORT               "Build application with DICOM support"                OFF)
option(Slicer_BUILD_DIFFUSION_SUPPORT           "Build application with Diffusion support"            OFF)
option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT    "Build application with ExtensionManager support"     ON)
option(Slicer_BUILD_MULTIVOLUME_SUPPORT         "Build application with MultiVolume support"          OFF)
option(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT "Build application with parameter serializer support" ON)
option(Slicer_USE_NUMPY                         "Build application with NUMPY support"                ON)
option(Slicer_USE_PYTHONQT                      "Build application with Python support"               ON)
option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)
option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            ON)

option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)
option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)
option(Slicer_BUILD_CompareVolumes              "Build application with ChangeTrackerPy module"       OFF)
option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)
</code></pre>

---

## Post #2 by @lassoan (2019-07-25 18:20 UTC)

<p>Could you print values of <code>Slicer_LAUNCH_COMMAND</code>, <code>launch_index</code>, and <code>Slicer_ADDITIONAL_LAUNCHER_SETTINGS</code> CMake variables right before the failing line?</p>

---

## Post #3 by @jamesobutler (2019-07-25 19:04 UTC)

<p><code>Slicer_LAUNCH_COMMAND</code> = C:/SonoEQApp/Slicer-build/SonoEQ.exe;–launch<br>
<code>launch_index</code> = 1<br>
<code>Slicer_ADDITIONAL_LAUNCHER_SETTINGS</code> = (Blank) - Nothing printed here</p>

---

## Post #4 by @lassoan (2019-07-25 19:40 UTC)

<p>Thank you, this explains the problem. When an extension is built as part of Slicer then there is no need for additional launcher settings (since everything is installed into the main application’s build tree).</p>
<p>Could you please test if this fix works?<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerOpenIGTLink/commit/130cf26e10dd8e7e385ae959b9f7b4f64e3fb60a" target="_blank" rel="nofollow noopener">github.com/lassoan/SlicerOpenIGTLink</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">
    <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/lassoan/SlicerOpenIGTLink/commit/130cf26e10dd8e7e385ae959b9f7b4f64e3fb60a" target="_blank" rel="nofollow noopener">BUG: Fix build error when the extension is bundled with the main application</a>
</h4>

  <pre class="message" style="white-space: normal;">Fixes this error (occurring because ${Slicer_ADDITIONAL_LAUNCHER_SETTINGS} is empty):
56&gt;-- Configuring Loadable module: OpenIGTLinkIF [qSlicerOpenIGTLinkIFModuleExport.h]
56&gt;CMake Error at C:/MyCustomApp/SlicerOpenIGTLink/OpenIGTLinkIF/Testing/CMakeLists.txt:29 (list):
56&gt; list sub-command INSERT requires...</pre>

<div class="date">
  by <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">lassoan</a>
  on <a href="https://github.com/lassoan/SlicerOpenIGTLink/commit/130cf26e10dd8e7e385ae959b9f7b4f64e3fb60a" target="_blank" rel="nofollow noopener">07:38PM - 25 Jul 19 UTC</a>
</div>

<div class="github-commit-stats">
  changed <strong>1 files</strong>
  with <strong>7 additions</strong>
  and <strong>3 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @jamesobutler (2019-07-25 21:25 UTC)

<p>Yes, that appears to solve that specific CMake error as I was able to see it configure correctly prior to the Slicer project building.</p>
<p>I’ve taken a little while to respond because I stopped that build from continuing and decided to try with a clean build with my customapp CMakeLists.txt again since I had been playing around with other dependencies enabling/disabling them.  Right now my build is running into errors because it tried to build OpenIGTLinkIO subproject (as part of SlicerOpenIGTLink) prior to the main VTK project being run. I’m using MP flags to speed up build time.</p>

---
