# Slicer IGT extension build errors in visual studio 2019

**Topic ID**: 19236
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/slicer-igt-extension-build-errors-in-visual-studio-2019/19236

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-08-17 17:52 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I was able to build slicer both on debug and release mode. I would like to build Slicer IGT extension which is required for my project but I am getting several errors.</p>
<p>Steps I have used to build is from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ/Extensions - Slicer Wiki</a></p>
<p>source = SlicerIGT cloned file</p>
<p>Add entry :<br>
Slicer_DIR = Slicer_build folder from released build version of Slicer<br>
and QT added</p>
<p>I didn’t see errors in Cmake configuration and generation (using GUI) but while building in Visual studio 2019 , I received several errors. like ,</p>
<p>23&gt;Done building project “vtkSlicerPathExplorerModuleMRMLPythonD.vcxproj” – FAILED.<br>
30&gt;Done building project “vtkSlicerTransformProcessorModuleMRMLPythonD.vcxproj” – FAILED.</p>
<p>What could be the reasons ?</p>
<p>Thank you for feedbacks and corrections.</p>

---

## Post #2 by @lassoan (2021-08-17 18:06 UTC)

<p>SlicerIGT builds without error using VS2019 using v142 (VS2019) toolset, see on the <a href="https://slicer.cdash.org/build/2362938">dashboard</a>.</p>
<p>Make sure you use the latest Slicer master version and that you choose Debug/Release that matches the  chosen Slicer_DIR. You need to use completely different build trees for Debug and Release builds.</p>

---
