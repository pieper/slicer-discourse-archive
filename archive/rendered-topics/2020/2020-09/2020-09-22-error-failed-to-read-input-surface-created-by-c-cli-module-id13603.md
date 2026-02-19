---
topic_id: 13603
title: "Error Failed To Read Input Surface Created By C Cli Module"
date: 2020-09-22
url: https://discourse.slicer.org/t/13603
---

# Error: failed to read input surface created by C++ CLI module

**Topic ID**: 13603
**Date**: 2020-09-22
**URL**: https://discourse.slicer.org/t/error-failed-to-read-input-surface-created-by-c-cli-module/13603

---

## Post #1 by @Farah (2020-09-22 08:33 UTC)

<p>Hi,</p>
<p>I have compiled CLI module with slicer to use it within slicer.<br>
The module input is vtk volume geometry (contains points, elements, stresses) then it calculates the average stresses on the surface to get a vtp surface geometry (output).<br>
When I used the module in slicer I got this error that slicer failed to read input surface.<br>
Kindly note the log file, Can someone help me solve this issue, please?</p>
<p>Many thanks,<br>
Farah</p>
<pre><code class="lang-auto">[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Session start time .......: 2020-09-22 16:22:57
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Slicer version ...........: 4.11.0-0000-00-00 (revision 3037 / 0) win-amd64 - not installed release
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Memory ...................: 8058 MB physical, 14584 MB virtual
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Application path .........: D:/S4R/Slicer-build/bin/Release
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Additional module paths ..: D:/AAA_build/lib/Slicer-4.11/qt-scripted-modules, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/Debug, D:/AAA_build/lib/Slicer-4.11/cli-modules/Debug, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/Release, D:/AAA_build/lib/Slicer-4.11/cli-modules/Release, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/MinSizeRel, D:/AAA_build/lib/Slicer-4.11/cli-modules/MinSizeRel, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/RelWithDebInfo, D:/AAA_build/lib/Slicer-4.11/cli-modules/RelWithDebInfo
[DEBUG][Python] 22.09.2020 16:22:58 [Python] (D:\S4R\python-install\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[DEBUG][Python] 22.09.2020 16:22:59 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 22.09.2020 16:23:00 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.09.2020 16:23:00 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.09.2020 16:23:00 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 22.09.2020 16:23:13 [] (unknown:0) - Empty filename passed to function
[INFO][VTK] 22.09.2020 16:23:24 [vtkMRMLModelStorageNode (0000027E69D360D0)] (D:\S4\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:380) - ReadDataInternal (vtkMRMLModelStorageNode1): File C:/Users/farah/Desktop/stress.vtk does not contain coordinate system information. Assuming LPS.
[DEBUG][Qt] 22.09.2020 16:23:24 [] (unknown:0) - "Model" Reader has successfully read the file "C:/Users/farah/Desktop/stress.vtk" "[0.23s]"
[DEBUG][Qt] 22.09.2020 16:23:26 [] (unknown:0) - Switch to module:  "AAA_AverageStress"
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - Found CommandLine Module, target is  D:/AAA_build/lib/Slicer-4.11/cli-modules/Release/AAA_AverageStress.exe
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - AAA_AverageStress command line: 

D:/AAA_build/lib/Slicer-4.11/cli-modules/Release/AAA_AverageStress.exe --numSegments 4 C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeE.vtp C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeF.vtp
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - AAA_AverageStress standard output:

vtkDebugLeaks has found no leaks.
[ERROR][VTK] 22.09.2020 16:23:37 [vtkSlicerCLIModuleLogic (0000027E677C03B0)] (D:\S4\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - AAA_AverageStress standard error:

ERROR: Failed to read input surface from C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeE.vtp
[ERROR][VTK] 22.09.2020 16:23:37 [vtkSlicerCLIModuleLogic (0000027E677C03B0)] (D:\S4\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - AAA_AverageStress completed with errors
[INFO][VTK] 22.09.2020 16:23:37 [vtkMRMLScene (0000027E6FDAFA40)] (D:\S4\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear

</code></pre>

---

## Post #2 by @Farah (2020-09-25 05:04 UTC)

<p>Hi,</p>
<p>I have compiled CLI module with slicer to use it within slicer. (all succeeded no failure)<br>
The module input is vtk volume geometry (contains points, elements, stresses) then it calculates the average stresses on the surface to get a vtp surface geometry (output).<br>
When I used the module in slicer I got this error that slicer failed to read input surface. it seems the module couldn’t find vtk directory although it is included in cmake.txt.<br>
Kindly note the log file, cmake module and cmake extension.<br>
Can someone help me solve this issue, please?</p>
<p>Many thanks,<br>
Farah</p>
<pre><code class="lang-auto">[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Session start time .......: 2020-09-22 16:22:57
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Slicer version ...........: 4.11.0-0000-00-00 (revision 3037 / 0) win-amd64 - not installed release
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Memory ...................: 8058 MB physical, 14584 MB virtual
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Application path .........: D:/S4R/Slicer-build/bin/Release
[DEBUG][Qt] 22.09.2020 16:22:57 [] (unknown:0) - Additional module paths ..: D:/AAA_build/lib/Slicer-4.11/qt-scripted-modules, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/Debug, D:/AAA_build/lib/Slicer-4.11/cli-modules/Debug, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/Release, D:/AAA_build/lib/Slicer-4.11/cli-modules/Release, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/MinSizeRel, D:/AAA_build/lib/Slicer-4.11/cli-modules/MinSizeRel, D:/AAA_build/lib/Slicer-4.11/qt-loadable-modules/RelWithDebInfo, D:/AAA_build/lib/Slicer-4.11/cli-modules/RelWithDebInfo
[DEBUG][Python] 22.09.2020 16:22:58 [Python] (D:\S4R\python-install\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[DEBUG][Python] 22.09.2020 16:22:59 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 22.09.2020 16:23:00 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 22.09.2020 16:23:00 [Python] (D:\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 22.09.2020 16:23:00 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 22.09.2020 16:23:13 [] (unknown:0) - Empty filename passed to function
[INFO][VTK] 22.09.2020 16:23:24 [vtkMRMLModelStorageNode (0000027E69D360D0)] (D:\S4\Libs\MRML\Core\vtkMRMLModelStorageNode.cxx:380) - ReadDataInternal (vtkMRMLModelStorageNode1): File C:/Users/farah/Desktop/stress.vtk does not contain coordinate system information. Assuming LPS.
[DEBUG][Qt] 22.09.2020 16:23:24 [] (unknown:0) - "Model" Reader has successfully read the file "C:/Users/farah/Desktop/stress.vtk" "[0.23s]"
[DEBUG][Qt] 22.09.2020 16:23:26 [] (unknown:0) - Switch to module:  "AAA_AverageStress"
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - Found CommandLine Module, target is  D:/AAA_build/lib/Slicer-4.11/cli-modules/Release/AAA_AverageStress.exe
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - ModuleType: CommandLineModule
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - AAA_AverageStress command line: 

D:/AAA_build/lib/Slicer-4.11/cli-modules/Release/AAA_AverageStress.exe --numSegments 4 C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeE.vtp C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeF.vtp
[DEBUG][Qt] 22.09.2020 16:23:37 [] (unknown:0) - AAA_AverageStress standard output:

vtkDebugLeaks has found no leaks.
[ERROR][VTK] 22.09.2020 16:23:37 [vtkSlicerCLIModuleLogic (0000027E677C03B0)] (D:\S4\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - AAA_AverageStress standard error:

ERROR: Failed to read input surface from C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeE.vtp
[ERROR][VTK] 22.09.2020 16:23:37 [vtkSlicerCLIModuleLogic (0000027E677C03B0)] (D:\S4\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2048) - AAA_AverageStress completed with errors
[INFO][VTK] 22.09.2020 16:23:37 [vtkMRMLScene (0000027E6FDAFA40)] (D:\S4\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear
</code></pre>
<pre><code class="lang-auto">#-----------------------------------------------------------------------------
set(MODULE_NAME AAA_AverageStress)

#-----------------------------------------------------------------------------

#
# SlicerExecutionModel
#

#-----------------------------------------------------------------------------
set(MODULE_INCLUDE_DIRECTORIES
  ${vtkITK_INCLUDE_DIRS}
  )

set(MODULE_SRCS
  )

set(MODULE_TARGET_LIBRARIES
  ${VTK_LIBRARIES}
  )

#-----------------------------------------------------------------------------
SEMMacroBuildCLI(
  NAME ${MODULE_NAME}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  ADDITIONAL_SRCS ${MODULE_SRCS}
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()
</code></pre>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 2.8.9)

project(AAA_AverageStress)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "http://www.example.com/Slicer/Extensions/AAA_AverageStress")
set(EXTENSION_CATEGORY "AAA")
set(EXTENSION_CONTRIBUTORS "Grand Joldes (The University of Western Australia, ISML)")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/AAA_AverageStress.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/AAA_AverageStress/Screenshots/1.png")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(AAA_AverageStress)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_CPACK})
</code></pre>

---

## Post #3 by @Andinet_Enquobahrie (2020-09-25 12:56 UTC)

<p>Is the following file the input vtp file that you specified in your module? Do you have this file in your system?</p>
<aside class="quote no-group" data-username="Farah" data-post="2" data-topic="13603">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/41988e/48.png" class="avatar"> Farah:</div>
<blockquote>
<p><code>C:/Users/farah/AppData/Local/Temp/Slicer/JHBC_vtkMRMLModelNodeE.vtp</code></p>
</blockquote>
</aside>

---

## Post #4 by @lassoan (2020-09-25 14:00 UTC)

<p>If you use the latest master version then you need to enable “Preserve CLI module data files” option in developer section in application settings to keep the CLI input/output files after execution.</p>

---

## Post #5 by @Farah (2020-09-29 03:32 UTC)

<p>No, it is not my input file,<br>
this folder is the slicer directory.</p>

---

## Post #7 by @Farah (2020-09-29 03:42 UTC)

<p>Thank you Andras for your reply,</p>
<p>Unfortunately, this didn’t solve the issue, the only thing that it saved this vtp file in the slicer directory “JHBC_vtkMRMLModelNodeE.vtp” but couldn’t read it,<br>
Do you think older version of slicer would solve this issue (i.e. slicer 4.10.2) ?</p>
<p>Many thanks,<br>
Farah</p>

---

## Post #8 by @lassoan (2020-09-29 04:30 UTC)

<p>Could you please attach an example .vtp file that is created but could not be read? (upload somewhere and post the link here)</p>

---

## Post #9 by @Farah (2020-09-29 05:13 UTC)

<p>Kindly note the attached link:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cloudstor.aarnet.edu.au/plus/3rdparty-apps/cloudstortheme/core/img/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://cloudstor.aarnet.edu.au/plus/s/5uOGRuKzeEIVjWK" target="_blank" rel="noopener nofollow ugc">CloudStor</a>
  </header>
  <article class="onebox-body">
    <img src="https://cloudstor.aarnet.edu.au/plus/3rdparty-apps/cloudstortheme/core/img/favicon-fb.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://cloudstor.aarnet.edu.au/plus/s/5uOGRuKzeEIVjWK" target="_blank" rel="noopener nofollow ugc">CloudStor - CloudStor is powered by AARNet</a></h3>

<p>AAAavg_stress_Slicer is publicly shared</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
stress.vtk is my input file, it has node coordinates, elements (cells), and stresses.<br>
CCI_vtkMRMLModelNodeE.vtp is the created vtp file it contains only the node coordinates and stresses (of stress.vtk).
<p>Thank you Andras,<br>
Farah</p>

---

## Post #10 by @lassoan (2020-09-29 13:34 UTC)

<p>The vtp file that the CLI module created is valid, but it is just a point cloud. You need to copy cells from the input data set (triangles, polygons, vertices, …). Alternatively, you can just leave it as a point cloud but then in Slicer you need to apply a glyph filter to create some displayable geometry, for example using a glyph filter:</p>
<pre data-code-wrap="python"><code class="lang-python">inputPointCloud = getNode('CCI_vtkMRMLModelNodeE')
glypher=vtk.vtkGlyph3D()
glypher.SetInputConnection(inputPointCloud.GetPolyDataConnection())
model = slicer.modules.models.logic().AddModel(glypher.GetOutputPort())
model.GetDisplayNode().SetScalarVisibility(True)
model.GetDisplayNode().SetActiveScalarName("S:Mises")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b27b273d1ece546676076caa57037bf39f69c86b.png" data-download-href="/uploads/short-url/psUQlWnhpGQAcFWDNEdBrkx2IB5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b27b273d1ece546676076caa57037bf39f69c86b_2_690x477.png" alt="image" data-base62-sha1="psUQlWnhpGQAcFWDNEdBrkx2IB5" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b27b273d1ece546676076caa57037bf39f69c86b_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b27b273d1ece546676076caa57037bf39f69c86b_2_1035x715.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b27b273d1ece546676076caa57037bf39f69c86b.png 2x" data-dominant-color="A69CB1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1162×804 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Farah (2020-09-29 15:58 UTC)

<p>Thankyou very much Andreas for this solution and your valuable time,</p>
<p>but what I am interested in is that my extension should take the input file (stress.vtk) and calculate the average stresses through thickness and write the output file which is the outer surface of this geometry only (surface without thickness with the averaged stress values).</p>
<p>After trying a lot with slicer platform, I tried to run this extension using command line, it asks about the following files: (ITKFactoryRegistration.dll) (vtkIO-8.2.dll) (vtkFilters-8.2.dll) (vtkCommon-8.2.dll), I found the vtk.dll files and copied them from slicer built folder to my built extension folder but I couldn’t find ITKFactoryRegistration.dll anywhere.</p>
<p>I think the extension is not able to call some required files. Although it was compiled with old version of slicer (I think in 2014) and working perfectly.</p>
<p>Many thanks,<br>
Farah</p>

---

## Post #12 by @Farah (2020-10-01 05:15 UTC)

<p>Hi Andreas,</p>
<p>I would like to thank you for your support.<br>
I managed to solve the problem and the extension is working now using the command line.</p>
<p>Thanks again,<br>
Farah</p>

---

## Post #13 by @lassoan (2020-10-01 13:53 UTC)

<p>Which extension and which module in it are you using?</p>
<p>Does it generate different VTP file than that you attached?</p>

---

## Post #14 by @Farah (2020-10-06 05:23 UTC)

<p>This extension is created by Prof. Grand Joldes and used within BioPARR software for aneurysm stress calculations, it is not available on github.</p>
<p>I just copied the required vtk.dll files (generated from slicer building) to the extension folder and run it through the command line not through slicer.</p>
<p>Many thanks,<br>
Farah</p>

---

## Post #15 by @lassoan (2020-10-06 16:08 UTC)

<p>In general, DLL files are not portable across different software versions. In some cases they might accidentally work, but in general, if there is a DLL version mismatch then the application is expected to crash.</p>

---
