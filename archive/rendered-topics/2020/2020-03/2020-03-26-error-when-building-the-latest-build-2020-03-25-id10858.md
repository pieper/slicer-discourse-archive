---
topic_id: 10858
title: "Error When Building The Latest Build 2020 03 25"
date: 2020-03-26
url: https://discourse.slicer.org/t/10858
---

# Error when building the latest build (2020-03-25)

**Topic ID**: 10858
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/error-when-building-the-latest-build-2020-03-25/10858

---

## Post #1 by @Fangwen_Zhai (2020-03-26 18:04 UTC)

<p>I just tried building the <a href="https://github.com/Slicer/Slicer/commit/90a0ba80ff91ca250abede254262c6313b180e52" rel="noopener nofollow ugc">latest code</a> and got several errors.  My building environment includes VS 2017, windows 10. After some searching, I found these errors are all related to itkv5 compatibility as listed below.</p>
<blockquote>
<p>Error	C2039	‘SetNumberOfThreads’: is not a member of ‘itk::MultiThreaderBase’	ExpertAutomatedRegistrationLib	…\slicersources-src\modules\cli\expertautomatedregistration\itkregistrationhelper\itkImageToImageRegistrationMethod.txx	39</p>
</blockquote>
<p>In the ITK <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md" rel="noopener nofollow ugc">migration guide</a>, it is recommended to change ‘SetNumberOfThreads’ to ‘SetNumberOfWorkUnits’.</p>
<p>And the following errors maybe related to the ITK_LEGACY_REMOVE flag which is still off in External_ITK.cmake.</p>
<blockquote>
<p>Error	C3668	‘itk::InverseDisplacementFieldTransform&lt;double,3&gt;::ComputeJacobianWithRespectToPosition’: method with override specifier ‘override’ did not override any base class methods	MRMLCore (Core-Libs\MRMLCore\MRMLCore)	…\slicersources-src\libs\mrml\core\vtkITKTransformInverse.h	198	<br>
Error	C3668	‘itk::InverseDisplacementFieldTransform&lt;double,3&gt;::ComputeInverseJacobianWithRespectToPosition’: method with override specifier ‘override’ did not override any base class methods	MRMLCore (Core-Libs\MRMLCore\MRMLCore)	…\slicersources-src\libs\mrml\core\vtkITKTransformInverse.h	216	<br>
Error	C3668	‘itk::InverseThinPlateSplineKernelTransform&lt;double,3&gt;::ComputeJacobianWithRespectToPosition’: method with override specifier ‘override’ did not override any base class methods	MRMLCore (Core-Libs\MRMLCore\MRMLCore)	…\slicersources-src\libs\mrml\core\vtkITKTransformInverse.h	283	<br>
Error	C2440	‘initializing’: cannot convert from ‘const std::list&lt;itk::SmartPointer&lt;itk::TransformBaseTemplate&gt;,std::allocator&lt;_Ty&gt;&gt; *’ to ‘TransformListType *’	MRMLCore (Core-Libs\MRMLCore\MRMLCore)	…\slicersources-src\Libs\MRML\Core\vtkMRMLTransformStorageNode.cxx	166	<br>
Error	C2039	‘TerminateThread’: is not a member of ‘itk::PlatformMultiThreader’	SlicerBaseLogic	…\slicersources-src\Base\Logic\vtkSlicerApplicationLogic.cxx	93	<br>
Error	C2039	‘SpawnThread’: is not a member of ‘itk::PlatformMultiThreader’	SlicerBaseLogic	…\slicersources-src\Base\Logic\vtkSlicerApplicationLogic.cxx	187</p>
</blockquote>
<p>Any suggestions or workaround?</p>

---

## Post #2 by @lassoan (2020-03-26 18:53 UTC)

<p>Do you build Slicer according to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a> or do you have a special configuration (such as trying to build Slicer with an externally built ITK)?</p>

---

## Post #3 by @Fangwen_Zhai (2020-03-26 19:10 UTC)

<p>Yes, I followed the build instructions. When building the nightly version around December 2019, everything was OK. I notice that the superbuild’s ITK has been updated from pre-v5.1b01 to v5.1rc01 in January and it seems to be the reason.</p>

---

## Post #4 by @lassoan (2020-03-26 19:40 UTC)

<p>If you built Slicer months ago then you need to rebuild it from scratch (delete the entire Slicer build folder, which contains ITK, VTK, … build trees).</p>

---

## Post #5 by @Fangwen_Zhai (2020-03-26 20:23 UTC)

<p>Thanks, I’ll try again.</p>

---

## Post #6 by @Fangwen_Zhai (2020-03-27 08:06 UTC)

<p>After cleaning the build directory and rebuild the whole project, now it works.</p>

---
