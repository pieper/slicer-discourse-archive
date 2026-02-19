---
topic_id: 10737
title: "Using Slicercat"
date: 2020-03-18
url: https://discourse.slicer.org/t/10737
---

# Using SlicerCat

**Topic ID**: 10737
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/using-slicercat/10737

---

## Post #1 by @rbahegne (2020-03-18 17:43 UTC)

<p>Hello i tried to follow the tutorial : <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="nofollow noopener">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> to build a custom version of slicer bundled with my own extension (sistream).</p>
<p>Everything when quite fine till Step 6 (build step).</p>
<p>After few errors easily fixed, our repository, Sistream is checked out and built, other error appeared that i did not manage to fix :</p>
<p>The build can’t find vtkMRMLMultiVolumeNode.h which is include in some file in my extension. In a regular slicer build this file is located in /Slicer-SuperBuild-Debug/MultiVolumeExplorer/MRML/ and it is correctly linked in the according CMakeList in my extension. Since the extension is bundled in the same project i would assume that Slicer_DIR environnement variable to be set for the extension alone was kind of automated. I tried to compile in a IDE setting variable with no result.</p>
<p>Is it a problem to bundled an extension which target include files from regular slicer modules ? Or do i just need another CMake declaration to make things right ?</p>

---

## Post #2 by @Sam_Horvath (2020-03-18 18:01 UTC)

<p>Hi!</p>
<p>The default SlicerCustomAppTemplate tries to make a very “stripped down” version of Slicer, and so disables some functionality by default.  This includes MultiVolume support.</p>
<p>In the CMakeLists.txt of the custom app you will need to turn ON MultiVolume support:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/90a68547d6ce9da7131b0d5a7097ed95e0036b58/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L90" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/90a68547d6ce9da7131b0d5a7097ed95e0036b58/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L90" target="_blank" rel="nofollow noopener">KitwareMedical/SlicerCustomAppTemplate/blob/90a68547d6ce9da7131b0d5a7097ed95e0036b58/{{cookiecutter.project_name}}/CMakeLists.txt#L90</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="80" style="counter-reset: li-counter 79 ;">
<li># Slicer options</li>
<li>option(BUILD_TESTING                            "Build application test suite"                        ON)</li>
<li>option(Slicer_BUILD_DOCUMENTATION               "Build documentation (Doxygen, sphinx, ...)"          OFF)</li>
<li>if(WIN32)</li>
<li>  option(Slicer_BUILD_WIN32_CONSOLE             "Build application executable as a console app"       OFF)</li>
<li>endif()</li>
<li>
</li>
<li>option(Slicer_BUILD_DICOM_SUPPORT               "Build application with DICOM support"                ON)</li>
<li>option(Slicer_BUILD_DIFFUSION_SUPPORT           "Build application with Diffusion support"            OFF)</li>
<li>option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT    "Build application with ExtensionManager support"     OFF)</li>
<li class="selected">option(Slicer_BUILD_MULTIVOLUME_SUPPORT         "Build application with MultiVolume support"          OFF)</li>
<li>option(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT "Build application with parameter serializer support" OFF)</li>
<li>option(Slicer_USE_PYTHONQT                      "Build application with Python support"               ON)</li>
<li>option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)</li>
<li>option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            OFF)</li>
<li>
</li>
<li>option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)</li>
<li>option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)</li>
<li>option(Slicer_BUILD_CompareVolumes              "Build application with ChangeTrackerPy module"       OFF)</li>
<li>option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)</li>
<li>option(Slicer_BUILD_SurfaceToolbox              "Build application with SurfaceToolbox module"        OFF)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>You can also enable this when configuring with CMake, as there will be a checkbox option to turn it on.</p>

---

## Post #3 by @rbahegne (2020-03-19 16:46 UTC)

<p>Thanks a lot that was the thing.</p>
<p>I did work nicely, yet i have a few questions concerning errors i came by. I fetch thoses Slicer sources :</p>
<blockquote>
<h1>Slicer sources</h1>
<p>include(FetchContent)<br>
if(NOT DEFINED slicersources_SOURCE_DIR)</p>
<h1>Download Slicer sources and set variables slicersources_SOURCE_DIR and slicersources_BINARY_DIR</h1>
<p>FetchContent_Populate(slicersources<br>
GIT_REPOSITORY git://github.com/Slicer/Slicer<br>
GIT_TAG        v4.10.2<br>
GIT_PROGRESS   1<br>
)<br>
else()<br>
set(slicersources_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/slicersources-subbuild)<br>
endif()</p>
</blockquote>
<p>I encountered :</p>
<ul>
<li>
<p>/yourproject/slicersources-src/Modules/CLI/ResampleDTIVolume/Data/Baseline/Brain_slice.nrrd is missing —&gt; your can get it from another regular slicer build</p>
</li>
<li>
<p>Jsons located at /yourproject/slicersources-src/Base/QTCore/Testing/Data/input are expected to be found compressed as tar.gz —&gt; compressed them manually to fullfill that expectation</p>
</li>
</ul>
<p>This can be solved easily but if I can avoid doing it each time i build a new project, i would be glad. Maybe this is linked to the version of slicer checkouted, or the build options.</p>

---

## Post #4 by @Sam_Horvath (2020-03-19 19:11 UTC)

<p>So, the first is definitely an issue related to the older version of Slicer used.  The second is more mysterious.  I am running a test SlicerCAT build with the most recent Slicer hash to see if it builds clean.</p>
<p>We have a testing dashboard for the CustomAppTemplate here: <a href="http://slicer.cdash.org/index.php?project=SlicerCustomAppTemplate" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerCustomAppTemplate</a>  which builds the custom app framework using the most recent Slicer hash.</p>

---

## Post #5 by @Sam_Horvath (2020-03-20 19:15 UTC)

<p>So, it looks like the template is building cleanly with the most recent Slicer nightly hash<br>
<a href="https://github.com/Slicer/Slicer/commit/9be2a42e72089851dff44722c632307fa8415d85" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/9be2a42e72089851dff44722c632307fa8415d85</a></p>
<p>You could try building with that Slicer version and see if there are any issues.</p>

---

## Post #6 by @rbahegne (2020-03-23 08:02 UTC)

<p>Yes with the last master branch, it builds fine. Thing is we wanted to stay on a release version, do you know when the next release version will be out ?</p>

---

## Post #7 by @lassoan (2020-03-23 13:41 UTC)

<p>We plan to release it within a couple of weeks. You can see the list of open issues here: <a href="https://github.com/Slicer/Slicer/milestone/1">https://github.com/Slicer/Slicer/milestone/1</a></p>

---
