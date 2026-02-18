# Slicer CLI module compilation error: undefined reference to `itk::GeometryUtilities

**Topic ID**: 2100
**Date**: 2018-02-16
**URL**: https://discourse.slicer.org/t/slicer-cli-module-compilation-error-undefined-reference-to-itk-geometryutilities/2100

---

## Post #1 by @MachadoL (2018-02-16 17:24 UTC)

<p>Hellow friends,</p>
<p>I’m very much a beginner in the 3DSlicer development world. I’m struggling with a compilation problem.<br>
I created a CLI module through Slicer “Extension Manager” and started to change it according to my goals.<br>
I then go to Cmake-gui to generate and configure. And sounds that everything went well except for two <strong>warnings</strong>:</p>
<pre><code class="lang-auto">CMake Warning (dev) at /home/leonardo/General_Sources/Slicer/CMake/SlicerMacroExtractRepositoryInfo.cmake:95 (message):
  Skipping repository info extraction: directory
  [/home/leonardo/Desktop/Modulos-Source/Modulos_to_Slicer/CSIM] is not a
  GIT, SVN or CVS checkout
Call Stack (most recent call first):
  /home/leonardo/General_Sources/Slicer/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:122 (SlicerMacroExtractRepositoryInfo)
  /home/leonardo/General_Sources/Slicer/CMake/SlicerExtensionCPack.cmake:219 (include)
  CMakeLists.txt:27 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.


Furthermore **in the QT compilation step** it happen as follows:

1) When I creat and execute my CLI module **directly** (**Without Extension Wizard**):

I use the following **CMakeLists.txt**:

#####################################
#-----------------------------------------------------------------------------
project(TextureProcessingV8)

cmake_minimum_required( VERSION 2.6 )

set(MODULE_NAME TextureProcessing)

if(NOT Slicer_SOURCE_DIR)
  find_package(Slicer REQUIRED)
  include(${Slicer_USE_FILE})
endif()

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  #LOGO_HEADER ${Slicer_SOURCE_DIR}/Resources/ITKLogo.h
  ADDITIONAL_SRCS
    Plot/HistogramPlot.cxx
    Percents/PercentileCalc.cxx
    Features/HistoFeat.cxx
    CoocurrenceFeat/CoocurrenceFeat.cxx
    ShapeFeatures/ShapeFeat.cxx
    RunLengthFeat/RunLengthFeat.cxx
    Normalization/Normalize.cxx
    Gradient/GradientFeat.cxx		 	

  TARGET_LIBRARIES ${ITK_LIBRARIES}
  )

#add_subdirectory(Texture)

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

########################################################

**No ERROR Occurred AT ALL**

2) When I insert the same CLI source code inside the **EXTENSION WIZARD** Pre-built files:

I use the following CMakeLists.txt for the **MODULE**
##############################################


#-----------------------------------------------------------------------------
set(MODULE_NAME TextureProcessing)

#-----------------------------------------------------------------------------

#
# SlicerExecutionModel
#
find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})

#
# ITK
#
set(${PROJECT_NAME}_ITK_COMPONENTS
  ITKIOImageBase
  ITKSmoothing
  )
find_package(ITK 4.6 COMPONENTS ${${PROJECT_NAME}_ITK_COMPONENTS} REQUIRED)
set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt
include(${ITK_USE_FILE})

#-----------------------------------------------------------------------------
set(MODULE_INCLUDE_DIRECTORIES
  )

set(MODULE_SRCS
  )

set(MODULE_TARGET_LIBRARIES
  ${ITK_LIBRARIES}
  )

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  ADDITIONAL_SRCS ${MODULE_SRCS}
Plot/HistogramPlot.cxx
    Percents/PercentileCalc.cxx
    Features/HistoFeat.cxx
    CoocurrenceFeat/CoocurrenceFeat.cxx
    ShapeFeatures/ShapeFeat.cxx
    RunLengthFeat/RunLengthFeat.cxx
    Normalization/Normalize.cxx
    Gradient/GradientFeat.cxx
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

#############################################################

And the following **CMakeLists.txt for the EXTENSION**:

The following **Errors OCCUR**:

**error: undefined reference to `itk::GeometryUtilities::HyperSphereRadiusFromVolume(int, double)'**
**/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:372: **

**error: undefined reference to `itk::GeometryUtilities::HyperSpherePerimeter(int, double)'**
**/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:373: **

**error: undefined reference to `itk::GeometryUtilities::HyperSphereRadiusFromVolume(int, double)'**
**/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:372: **

**error: undefined reference to `itk::GeometryUtilities::HyperSpherePerimeter(int, double)'**
**/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:373:'** 

I really can't find the solution.
I appreciate any contributions!!!!

</code></pre>

---

## Post #2 by @lassoan (2018-02-16 19:15 UTC)

<p>This is just a warning that CMake cannot automatically detect your source code repository URL. You can safely ignore it.</p>

---

## Post #3 by @lassoan (2018-02-16 20:41 UTC)

<p>To fix the undefined reference error mentioned in the title, make sure you have included the ITK header file where GeometryUtilities is declared in.</p>

---

## Post #4 by @MachadoL (2018-02-16 20:56 UTC)

<p>Auh… Thank you very much for the feedback.<br>
Unfortunately I didn’t finish my question before submitting the post. I’m<br>
sorry.</p>
<p>But the final part of the problem I’m struggling is error:<br>
‘Undefined reference’</p>
<p>I’ll post the complete error log soon as I get the chance.</p>
<p>Thanks a lot for now.</p>

---

## Post #5 by @MachadoL (2018-02-26 16:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, this is the complete version of my question. Would love to hear any help.</p>
<p>I’m very much a beginner in the 3DSlicer development world. I’m struggling with a compilation problem.<br>
I created a CLI module through Slicer “Extension Manager” and started to change it according to my goals.<br>
I then go to Cmake-gui to generate and configure. And sounds that everything went well except for two <strong>warnings</strong>:</p>
<pre><code class="lang-auto">CMake Warning (dev) at /home/leonardo/General_Sources/Slicer/CMake/SlicerMacroExtractRepositoryInfo.cmake:95 (message):
  Skipping repository info extraction: directory
  [/home/leonardo/Desktop/Modulos-Source/Modulos_to_Slicer/CSIM] is not a
  GIT, SVN or CVS checkout
Call Stack (most recent call first):
  /home/leonardo/General_Sources/Slicer/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake:122 (SlicerMacroExtractRepositoryInfo)
  /home/leonardo/General_Sources/Slicer/CMake/SlicerExtensionCPack.cmake:219 (include)
  CMakeLists.txt:27 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.
</code></pre>
<p>Furthermore <strong>in the QT compilation step</strong> it happen as follows:</p>
<ol>
<li>When I creat and execute my CLI module <strong>directly</strong> (<strong>Without Extension Wizard</strong>):</li>
</ol>
<p>I use the following <strong>CMakeLists.txt</strong>:</p>
<pre><code class="lang-auto">#####################################
#-----------------------------------------------------------------------------
project(TextureProcessingV8)

cmake_minimum_required( VERSION 2.6 )

set(MODULE_NAME TextureProcessing)

if(NOT Slicer_SOURCE_DIR)
  find_package(Slicer REQUIRED)
  include(${Slicer_USE_FILE})
endif()

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  #LOGO_HEADER ${Slicer_SOURCE_DIR}/Resources/ITKLogo.h
  ADDITIONAL_SRCS
    Plot/HistogramPlot.cxx
    Percents/PercentileCalc.cxx
    Features/HistoFeat.cxx
    CoocurrenceFeat/CoocurrenceFeat.cxx
    ShapeFeatures/ShapeFeat.cxx
    RunLengthFeat/RunLengthFeat.cxx
    Normalization/Normalize.cxx
    Gradient/GradientFeat.cxx		 	

  TARGET_LIBRARIES ${ITK_LIBRARIES}
  )

#add_subdirectory(Texture)

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

########################################################
</code></pre>
<p><strong>No ERROR Occurred AT ALL</strong></p>
<ol start="2">
<li>When I insert the same CLI source code inside the <strong>EXTENSION WIZARD</strong> Pre-built files:</li>
</ol>
<p>I use the following CMakeLists.txt for the <strong>MODULE</strong></p>
<pre><code class="lang-auto">##############################################


#-----------------------------------------------------------------------------
set(MODULE_NAME TextureProcessing)

#-----------------------------------------------------------------------------

#
# SlicerExecutionModel
#
find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})

#
# ITK
#
set(${PROJECT_NAME}_ITK_COMPONENTS
  ITKIOImageBase
  ITKSmoothing
  )
find_package(ITK 4.6 COMPONENTS ${${PROJECT_NAME}_ITK_COMPONENTS} REQUIRED)
set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt
include(${ITK_USE_FILE})

#-----------------------------------------------------------------------------
set(MODULE_INCLUDE_DIRECTORIES
  )

set(MODULE_SRCS
  )

set(MODULE_TARGET_LIBRARIES
  ${ITK_LIBRARIES}
  )

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  ADDITIONAL_SRCS ${MODULE_SRCS}
Plot/HistogramPlot.cxx
    Percents/PercentileCalc.cxx
    Features/HistoFeat.cxx
    CoocurrenceFeat/CoocurrenceFeat.cxx
    ShapeFeatures/ShapeFeat.cxx
    RunLengthFeat/RunLengthFeat.cxx
    Normalization/Normalize.cxx
    Gradient/GradientFeat.cxx
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()

#############################################################
</code></pre>
<p>And the following <strong>CMakeLists.txt for the EXTENSION</strong>:</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.5)

project(TextureAnalysis)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/CSIM")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "John Doe (AnyWare Corp.)")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/CSIM.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/CSIM/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a space separated string, a list or 'NA' if any

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(TextureProcessing)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
</code></pre>
<p>The following <strong>Errors OCCURED</strong>:</p>
<p><strong>error: undefined reference to `itk::GeometryUtilities::HyperSphereRadiusFromVolume(int, double)’</strong><br>
/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:372:</p>
<p><strong>error: undefined reference to `itk::GeometryUtilities::HyperSpherePerimeter(int, double)’</strong><br>
/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:373:</p>
<p><strong>error: undefined reference to `itk::GeometryUtilities::HyperSphereRadiusFromVolume(int, double)’</strong><br>
/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:372:</p>
<p><strong>error: undefined reference to `itk::GeometryUtilities::HyperSpherePerimeter(int, double)’</strong><br>
/usr/local/Slicer/ITKv4/Modules/Filtering/LabelMap/include/itkShapeLabelMapFilter.hxx:373:’</p>
<p>I really can’t find the solution.<br>
I appreciate any contributions!!!</p>

---

## Post #6 by @lassoan (2018-02-26 16:58 UTC)

<p>Please upload your extension to github and post the link here so that I can have a look. Thanks!</p>

---

## Post #7 by @MachadoL (2018-02-26 16:59 UTC)

<p>Ok. Thank you very much. I’ll take a time… once I’m also starting with git and everything… But I’ll do it right away.<br>
Thank you!</p>

---

## Post #8 by @MachadoL (2018-02-26 20:43 UTC)

<p>Dr. Lasso,</p>
<p>I just added you to my github project. Hope you can check it out!</p>
<p>Thank you very much!</p>

---

## Post #9 by @lassoan (2018-02-27 14:45 UTC)

<p>The solution was to adjust the CMakeLists.txt:</p>
<ul>
<li>add <code>ITKLabelMap</code> to <code>${PROJECT_NAME}_ITK_COMPONENTS</code>
</li>
<li>add <code>${CMAKE_CURRENT_SOURCE_DIR}</code> to <code>MODULE_INCLUDE_DIRECTORIES</code>
</li>
<li>add <code>${SlicerExecutionModel_EXTRA_EXECUTABLE_TARGET_LIBRARIES}</code> to <code>target_link_libraries(${CLP}Test ${CLP}Lib ...)</code> (probably old version of Extension Wizard was used, that’s why it was missing)</li>
</ul>
<p>See details here:<br>
<a href="https://github.com/MachadoLF/CLI-Module---Texture-Feature-Extractor/pull/1" class="onebox" target="_blank">https://github.com/MachadoLF/CLI-Module---Texture-Feature-Extractor/pull/1</a></p>

---

## Post #10 by @MachadoL (2018-02-27 17:25 UTC)

<h2>Thank you very much, Dr. Lasso.</h2>
<p>It completely fixed my problems!!!</p>
<p>I tested change by change and saw that the <strong>first one</strong> (add ITKLabelMap to ${PROJECT_NAME}_ITK_COMPONENTS) had already solved <strong>ALL</strong> my issues without even doing the additional ones.</p>
<p>In this case, is it <strong>necessary</strong> to make the additional changes you mentioned? Or is it only something like <em>good programming practices</em>?</p>
<p>What do you think?</p>
<p>Thanks a lot for your feedback!!!</p>

---

## Post #11 by @lassoan (2018-02-27 18:01 UTC)

<p>Most often, header files are in a single directory, as when you have files that are not tightly linked, you compile them as separate libraries.</p>
<p>In some cases, you use relative paths, but then the usually you add the base folder to the list of include directories and you define paths relative to that (and never use <code>./</code> or <code>../</code> in the <code>#include</code> directive).</p>

---

## Post #12 by @MachadoL (2018-02-27 18:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="2100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>add ${CMAKE_CURRENT_SOURCE_DIR} to MODULE_INCLUDE_DIRECTORIES</p>
</blockquote>
</aside>
<p>Your last comment is related to this change?</p>

---

## Post #13 by @lassoan (2018-02-27 19:58 UTC)

<p>Yes. It adds the source code top-level directory to the include paths. So, if you need to refer to a header file then you can always do that relative to this top-level directory and you don’t need to reach it by prepending <code>../../</code> to the header file name.</p>

---

## Post #14 by @MachadoL (2018-02-27 20:08 UTC)

<p>Ok! I got it! Thank you very much. Everything worked out nice and smoothly. And thanks for the tips with programming.</p>
<p>Thanks again!</p>
<p>Machado, L.</p>

---

## Post #15 by @lassoan (2020-09-25 06:21 UTC)

<p>A post was merged into an existing topic: <a href="/t/error-failed-to-read-input-surface-compiled-cli-module/13603/2">Error: failed to read input surface\ compiled CLI module</a></p>

---
