---
topic_id: 1900
title: "Loadable Module Crashing Binary Slicer"
date: 2018-01-22
url: https://discourse.slicer.org/t/1900
---

# Loadable module crashing binary Slicer

**Topic ID**: 1900
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/loadable-module-crashing-binary-slicer/1900

---

## Post #1 by @kanderle (2018-01-22 14:52 UTC)

<p>I have an error with my loadable module. I’ve built the Slicer stable version (revision 26489) and I’ve built my module against it without errors. The module works as intended when I launch the built Slicer version. However, if I try to launch module with the binary Slicer release (downloaded from the website, the 4.8.0 version - same as the built revision) the Slicer crashes before opening and I get the following error:<br>
“terminate called after throwing an instance of ‘H5::DataSpaceIException’”</p>
<p>Has anyone encountered such an error and do you know how to fix it? I’m using Slicer on Linux.</p>
<p>Best regards,<br>
Kristjan</p>

---

## Post #2 by @ihnorton (2018-01-22 14:59 UTC)

<p>Generally speaking, mixing self-built binaries with <a href="http://slicer.org">slicer.org</a> packaged versions is not supported (for any OS). The linux factory runs a relatively old OS and compiler suite in order to maximize system library compatibility, which means there can easily be ABI mismatches if you build with newer default compilers. You can see the factory version information <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#VM:_Linux">here</a>.</p>
<p>Given the error message, the specific problem might be mixing different HDF5 libraries in the same process, which is unlikely to work due to e.g. mismatched allocators (and other possible problems).</p>

---

## Post #3 by @lassoan (2018-01-22 18:54 UTC)

<p>If your extension is open-source then you can submit it to the Slicer extension index and Slicer factory machines will build it for you on all platforms and make available for download through the extension manager.</p>
<p>If it’s a proprietary module, then you have to distribute your custom extension along with your custom-built Slicer. You can include your extension in the Slicer package (so that you have a single installer) and can set custom application name, settings, etc. (see full set of customization options <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CONFIGURE_and_generate_Slicer_solution_files">here</a>).</p>

---

## Post #4 by @kanderle (2018-01-24 11:23 UTC)

<p>I think that’s a good idea and I will submit it to Slicer extension index.</p>
<p>A different question on that regard - my module depends on Segment Comparison Module from Slicer RT extension. I can change the cmake files so that it builds on my machine, but I don’t know how to do it properly so it can also be build anywhere. Do you have maybe an example that I could follow?</p>

---

## Post #5 by @cpinter (2018-01-24 12:57 UTC)

<p>Extension dependencies can be set in the main CMakeLists file, for example<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/CMakeLists.txt#L19" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SegmentRegistration/blob/master/CMakeLists.txt#L19" target="_blank" rel="nofollow noopener">SlicerRt/SegmentRegistration/blob/master/CMakeLists.txt#L19</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
<li>set(SEGMENTREGISTRATION_VERSION_PATCH "0")</li>
<li>set(SEGMENTREGISTRATION_VERSION ${SEGMENTREGISTRATION_VERSION_MAJOR}.${SEGMENTREGISTRATION_VERSION_MINOR}.${SEGMENTREGISTRATION_VERSION_PATCH})</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li>set(EXTENSION_HOMEPAGE "https://github.com/SlicerRt/SegmentRegistration")</li>
<li>set(EXTENSION_CATEGORY "Registration")</li>
<li>set(EXTENSION_CONTRIBUTORS "Csaba Pinter (PerkLab, Queen's University)")</li>
<li>set(EXTENSION_DESCRIPTION "Segment registration is an extension that contains generic and more specialized modules for registering two delineations of the same structure, and propagating other segmented structures from one dataset to the other (also called fusion or contour propagation).")</li>
<li>set(EXTENSION_ICONURL "https://github.com/SlicerRt/SegmentRegistration/raw/master/Logo/SegmentRegistration_Logo_128.png")</li>
<li>set(EXTENSION_SCREENSHOTURLS "https://www.slicer.org/w/images/a/a1/20170526_ProstatMRIUSContourPropagation.png https://www.slicer.org/w/images/1/15/20160329_MRIUS_1500.gif")</li>
<li class="selected">set(EXTENSION_DEPENDS SlicerProstate SlicerRT)</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li>find_package(Slicer COMPONENTS ConfigurePrerequisites REQUIRED)</li>
<li>project(SegmentRegistration)</li>
<li>find_package(Slicer REQUIRED)</li>
<li>include(${Slicer_USE_FILE})</li>
<li>
</li>
<li>find_package(SlicerProstate REQUIRED)</li>
<li>find_package(SlicerRT REQUIRED)</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The factory machines do the building properly, and when someone installs your extension (in Extension Manager) that depends on another, dependent extensions are automatically installed too.</p>
<p>Expecting people to manually build everything is not reasonable anyway, so if your module is not in an extension yet, then it’s time to make one.<br>
If for some reason you don’t want to do that, you can create packages yourself by building the “package” project. It generates a zip file that you can install from Extension Manager using a menu option under the wrench icon next to the search bar.</p>

---

## Post #6 by @kanderle (2018-01-26 10:36 UTC)

<p>I’ve made changes to CMakeList file to include SlicerRT, however I still get error when compiling:</p>
<p>/usr/bin/ld: cannot find -lplmsys<br>
/usr/bin/ld: cannot find -lplmbase<br>
/usr/bin/ld: cannot find -ldevillard<br>
/usr/bin/ld: cannot find -lnkidecompress<br>
/usr/bin/ld: cannot find -lplmutil<br>
/usr/bin/ld: cannot find -lspecfun<br>
/usr/bin/ld: cannot find -lplmdose<br>
/usr/bin/ld: cannot find -llbfgs<br>
/usr/bin/ld: cannot find -lplmregister</p>
<p>Which I guess are the missing plastimatch libraries? My CMake knowledge is pretty poor, so I don’t know how to change the CMakeList file to include the missing libraries.</p>

---

## Post #7 by @gcsharp (2018-01-26 14:02 UTC)

<p>If I understand correctly what you are trying to do, there should be no need to link with those libraries.  You should only need to link with the SlicerRT shared libraries.</p>
<p>How did you get the list of library dependencies?</p>

---

## Post #8 by @kanderle (2018-01-29 10:34 UTC)

<p>The list of library dependencies shows when I run the make command.<br>
Maybe my two CMakeLists files will help. Here is the main one:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/CMakeLists.txt" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/CMakeLists.txt" target="_blank" rel="nofollow noopener">gsi-biomotion/slicer-dirqa/blob/kristjanBranch/CMakeLists.txt</a></h4>
<pre><code class="lang-txt">cmake_minimum_required(VERSION 2.8.9)

set(EXTENSION_NAME SlicerDIRQA)

#-----------------------------------------------------------------------------
set(EXTENSION_NAME "RegistrationQualityExtension")
set(EXTENSION_HOMEPAGE "https://github.com/gsi-biomotion/slicer-dirqa")
set(EXTENSION_CATEGORY "Registration")
set(EXTENSION_CONTRIBUTORS "Kristjan Anderle (GSI), Tobias Brandt (University Clinic of Erlangen), Daniel Richter (University Clinic of Erlangen), Jens Woelfelschneider (University Clinic of Erlangen)")
set(EXTENSION_DESCRIPTION "Deformable image registration (DIR) quality assessment tool.")
set(EXTENSION_ICONURL "http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/LoadableExtensionTemplate/LoadableExtensionTemplate.png?revision=21746&amp;view=co")
set(EXTENSION_SCREENSHOTURLS "http://wiki.slicer.org/slicerWiki/images/4/42/Slicer-r19441-LoadableExtensionTemplate-screenshot.png")
set(EXTENSION_DEPENDS SlicerRT)


#-----------------------------------------------------------------------------
find_package(Slicer COMPONENTS ConfigurePrerequisites REQUIRED)
project(SlicerDIRQA)
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})
</code></pre>

  This file has been truncated. <a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/CMakeLists.txt" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>And the one in Logic subfolder, where the SegementationComparision module is needed:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/RegistrationQualityModule/Logic/CMakeLists.txt" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/RegistrationQualityModule/Logic/CMakeLists.txt" target="_blank" rel="nofollow noopener">gsi-biomotion/slicer-dirqa/blob/kristjanBranch/RegistrationQualityModule/Logic/CMakeLists.txt</a></h4>
<pre><code class="lang-txt">project(vtkSlicer${MODULE_NAME}ModuleLogic)

set(KIT ${PROJECT_NAME})

set(${KIT}_EXPORT_DIRECTIVE "VTK_SLICER_${MODULE_NAME_UPPER}_MODULE_LOGIC_EXPORT")

set(${KIT}_INCLUDE_DIRECTORIES
  ${vtkSlicerSegmentComparisonModuleLogic_INCLUDE_DIRS}
  ${vtkSlicerMarkupsModuleMRML_INCLUDE_DIRS}
  ${vtkSlicerAnnotationsMRML_INCLUDE_DIRS}
  ${vtkSlicerSegmentationsModuleMRML_INCLUDE_DIRS}
  ${vtkSlicerVolumesModuleLogic_INCLUDE_DIRS}
  
)

set(${KIT}_SRCS
  vtkSlicer${MODULE_NAME}Logic.cxx
  vtkSlicer${MODULE_NAME}Logic.h
  vtkMRMLRegistrationQualityNode.cxx
  vtkMRMLRegistrationQualityNode.h
</code></pre>

  This file has been truncated. <a href="https://github.com/gsi-biomotion/slicer-dirqa/blob/kristjanBranch/RegistrationQualityModule/Logic/CMakeLists.txt" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
