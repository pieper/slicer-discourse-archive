---
topic_id: 5878
title: "Build Light Weight Robot Igt Module"
date: 2019-02-21
url: https://discourse.slicer.org/t/5878
---

# Build Light Weight Robot IGT module

**Topic ID**: 5878
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/build-light-weight-robot-igt-module/5878

---

## Post #1 by @Mary7291 (2019-02-21 22:07 UTC)

<p>Operating system:Win 7<br>
Slicer version: build slicer V. 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello everybody,</p>
<p>I tried to build the Light Weight Robot IGT module after building the Slicer on my system. After fixing all the compilation errors, I faced with error LNK 2005 as follows which i have no idea how to fix.</p>
<hr>
<p>Error LNK2005 “public: static class vtkIGTLToMRMLString * __cdecl vtkIGTLToMRMLString::New(void)” (?New@vtkIGTLToMRMLString@<span class="mention">@SAPEAV1</span>@XZ) already defined in vtkIGTLToMRMLString.obj</p>
<p>project: vtkSlicerLightWeightRobotIGTModuleMRML</p>
<p>file:vtkSlicerOpenIGTLinkIFModuleMRML.lib(vtkSlicerOpenIGTLinkIFModuleMRML.dll)</p>
<hr>
<p>This error is appeared when i add the “vtkSlicerOpenIGTLinkIFModuleMRML.lib” to the linker of the “vtkSlicerLightWeightRobotIGTModuleMRML” project in configuration properties in visual studio.</p>
<p>I would be so appreciated if anyone could help me to fix the error.</p>

---

## Post #2 by @lassoan (2019-02-21 22:23 UTC)

<p>Support for STRING message type is now part of OpenIGTLinkIF. You can remove vtkIGTLToMRMLString class from LightWeightRobotIGT.</p>
<p>vtkIGTLToMRMLString in LightWeightRobotIGT saved text data to vtkMRMLAnnotationTextNode, while OpenIGTLinkIF uses <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/master/OpenIGTLinkIF/MRML/vtkMRMLTextNode.h" rel="nofollow noopener">vtkMRMLTextNode</a>, so LightWeightRobotIGT need to be updated accordingly.</p>

---

## Post #3 by @Mary7291 (2019-02-22 18:52 UTC)

<p>Thanks Mr. Lasso,<br>
I can fix the errors and build the module based on your suggestion.</p>
<p>But another problem is how to use and install the module in Slicer. I add the path containing the following folder to the “edit—application settings—modules—additional module paths” and then restart the Slicer.<br>
**<br>
the path is:<br>
E:\LightWeightRobotIGT\B\lib\Slicer-4.11\qt-loadable-modules<br>
**<br>
But it seems that there is no changes after restarting the Slicer and even there is no additional module in all modules.</p>
<p>I am waiting for your guidance…</p>

---

## Post #4 by @lassoan (2019-02-22 20:09 UTC)

<p>You need to add SlicerOpenIGTLink extension paths to additional module paths. Third-party DLLs need to be added to the same folder where module DLLs are or you need to use the generated additional launcher settings .ini file (that should take care of both the additional module paths and third-party library paths).</p>

---

## Post #5 by @lassoan (2019-02-22 20:10 UTC)

<p>Once things are working, please send a pull request with your changes so that we can review, give feedback, merge them. Thank you!</p>

---

## Post #6 by @Mary7291 (2019-02-27 20:18 UTC)

<p>Dear Mr. Lasso,</p>
<p>you mean that the OpenIGTLink is the third party for the LightWeightRobotIGT?<br>
I built the OpenIGTLink but unfortunately there is no .dll file in OpenIGTLink library folder, there exist just .lib and .exp files.</p>
<p>Besides, how can i use the additional launcher settings .ini file?</p>
<p>I am so interesting to use this module and Slicer and i would be so appreciated if you could help me through.</p>

---

## Post #7 by @lassoan (2019-02-27 20:20 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you help <a class="mention" href="/u/mary7291">@Mary7291</a> with details steps? Thanks!</p>

---

## Post #8 by @Sunderlandkyl (2019-02-27 20:44 UTC)

<p>Note that the path for a module should look like the following:<br>
E:\d\s\SlicerOpenIGTLinkD\inner-build\lib\Slicer-4.11\qt-loadable-modules\Debug<br>
If your extension includes Python modules, then you also need to add:<br>
E:\d\s\SlicerOpenIGTLinkD\inner-build\lib\Slicer-4.11\qt-scripted-modules</p>
<p>You need to specify the additional-module-paths for SlicerOpenIGTLink, as well as one of the following:</p>
<ol>
<li>
<p>Within SlicerOpenIGTLink build, third-party DLLs are in the folder:<br>
E:\d\s\SlicerOpenIGTLinkD/bin/Release or E:\d\s\SlicerOpenIGTLinkD/bin/Debug<br>
and<br>
Copy the DLLs from the folder above to:<br>
E:\d\s\SlicerOpenIGTLinkD\inner-build\lib\Slicer-4.11\qt-loadable-modules\Release or E:\d\s\SlicerOpenIGTLinkD\inner-build\lib\Slicer-4.11\qt-loadable-modules\Debug</p>
</li>
<li>
<p>You can start Slicer with the following option:<br>
Slicer.exe --launcher-additional-settings E:\d\s\SlicerOpenIGTLinkD\inner-build\AdditionalLauncherSettings.ini</p>
</li>
</ol>

---

## Post #9 by @Mary7291 (2019-02-28 09:42 UTC)

<p>Thanks Mr. Sunderland,</p>
<p>The SlicerOpenIGTLink is now added to Slicer modules based on your guidance.</p>
<p>I want to use the LightWeightRobotIGT module which it’s source code can be found here:<br>
<a href="https://github.com/SNRLab/LightWeightRobotIGT" rel="nofollow noopener">https://github.com/SNRLab/LightWeightRobotIGT</a> .<br>
The qt loadable modules are built after building the module in VS2015. The path to the lib folder is as follows:<br>
E:\LightWeightRobotIGT\B\lib\Slicer-4.11\qt-loadable-modules\Release.</p>
<p>Would you please guide me through the installing the module in Slicer?</p>

---

## Post #10 by @Sunderlandkyl (2019-02-28 16:51 UTC)

<p>Can you upload your changes to the LightWeightRobotIGT to a GitHub branch somewhere?</p>
<p>If everything compiles correctly, you should only need to add E:\LightWeightRobotIGT\B\lib\Slicer-4.11\qt-loadable-modules\Release to the additional-module-paths.</p>

---

## Post #11 by @Mary7291 (2019-02-28 19:40 UTC)

<p>(Scenario 1) I was built the LightWeightRobotIGT (LWRIGT) module based on the OpenIGTLink and OpenIGTLinkIF which can be found from:<br>
<a href="https://github.com/openigtlink/OpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/OpenIGTLink</a>,<br>
and<br>
<a href="https://github.com/openigtlink/OpenIGTLinkIF" rel="nofollow noopener">https://github.com/openigtlink/OpenIGTLinkIF</a>.<br>
This way and after building the above two modules, the LWRIGT was compiled in VS2015 and the errors were fixed step by step by adding the header and library files to the corresponding project in VS.</p>
<p>(Scenario 2) But now and based on your guidance i found another url as: <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink</a>, which i could load the OpenIGTLink Extension to the module paths after building this extension.</p>
<p>Please let me know if there is any difference in building the LWRIGT module based on these two scenarios…</p>

---

## Post #12 by @Sunderlandkyl (2019-02-28 20:35 UTC)

<p>OpenIGTLink and OpenIGTLinkIF are compiled as part of the SlicerOpenIGTLink extension.</p>
<p>What you will need to do is add SlicerOpenIGTLink as a dependency of LightWeightRobotIGT.<br>
For example, the SlicerIGSIO extension depends on the Sequences extension:(<a href="https://github.com/IGSIO/SlicerIGSIO/blob/master/CMakeLists.txt" rel="nofollow noopener">https://github.com/IGSIO/SlicerIGSIO/blob/master/CMakeLists.txt</a>)</p>
<p>You will then need to get LightWeightRobotIGT to compile using SlicerOpenIGTLink instead of using openigtlink/OpenIGTLinkIF.</p>

---

## Post #13 by @Mary7291 (2019-03-01 20:43 UTC)

<p>I am trying to build the module based on your suggestion by adding these two lines to the CMake:</p>
<hr>
<p>set(EXTENSION_DEPENDS “SlicerOpenIGTLink”)<br>
and<br>
find_package(SlicerOpenIGTLink REQUIRED</p>
<hr>
<p>But after compiling the project in VS, the error which says that it can not open the ‘vtkIGTLTOMRMLBASE.h’ file is appeared. On the other hand there is no such file in any of the ‘Slicer OpenIGTLink’ folders to add to the VC/VC++ configuration properties.</p>
<p>would you please help me to substitute the file or please let me know  that if something wrong will happen by adding the  ‘vtkIGTLTOMRMLBASE.h’ file from ‘OpenIGTLinkIF’ folder??<br>
<a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #14 by @Sunderlandkyl (2019-03-01 21:08 UTC)

<p>What is vtkIGTLTOMRMLBASE used for?</p>
<p>The process to convert IGTL messages to MRML nodes is already done by SlicerOpenIGTLink.</p>

---
