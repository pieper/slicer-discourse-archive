---
topic_id: 17279
title: "Metric Test Module Error"
date: 2021-04-23
url: https://discourse.slicer.org/t/17279
---

# Metric Test Module Error!

**Topic ID**: 17279
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/metric-test-module-error/17279

---

## Post #1 by @HodaGH (2021-04-23 15:20 UTC)

<p>Hi all,</p>
<p>I’m using macOS Mojave. I get this following error when I try to get the MMI value while having a transform file. I tried other transform files too but I get the same error. And no error without a transform file. The transform file is created by Elastix in Slicer and I didn’t change anything as the error suggests.</p>
<p>Metric Test standard error:</p>
<p>HDF5-DIAG: Error detected in HDF5 (1.10.4) thread 0:<br>
<span class="hashtag">#000:</span> /Volumes/D/S/S-0-build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5F.c line 370 in itk_H5Fis_hdf5(): unable open file<br>
major: File accessibilty<br>
minor: Not an HDF5 file<br>
<span class="hashtag">#001:</span> /Volumes/D/S/S-0-build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5Fint.c line 802 in itk_H5F__is_hdf5(): unable to open file<br>
major: Low-level I/O<br>
minor: Unable to initialize object<br>
<span class="hashtag">#002:</span> /Volumes/D/S/S-0-build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5FD.c line 734 in itk_H5FD_open(): open failed<br>
major: Virtual File Layer<br>
minor: Unable to initialize object<br>
<span class="hashtag">#003:</span> /Volumes/D/S/S-0-build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5FDsec2.c line 346 in H5FD_sec2_open(): unable to open file: name = ‘/private/var/folders/8b/yp3srf4s2svdnn_j_cwbvnyw0000gn/T/Slicer-hodagh/BGIFF_AxHfaeGHIabfDA.mrml#vtkMRMLLinearTransformNode1’, errno = 2, error message = ‘No such file or directory’, flags = 0, o_flags = 0<br>
major: File accessibilty<br>
minor: Unable to open file<br>
Exception caught!</p>
<p>itk::ExceptionObject (0x7f977a655490)<br>
Location: “unknown”<br>
File: /Volumes/D/S/S-0-build/ITK/Modules/IO/TransformBase/src/itkTransformFileReader.cxx<br>
Line: 128<br>
Description: itk::ERROR: itk::ERROR: TransformFileReaderTemplate(0x7f977a6540e0): Could not create Transform IO object for reading file /private/var/folders/8b/yp3srf4s2svdnn_j_cwbvnyw0000gn/T/Slicer-hodagh/BGIFF_AxHfaeGHIabfDA.mrml#vtkMRMLLinearTransformNode1<br>
File does not exists!  Tried to create one of the following:<br>
HDF5TransformIOTemplate<br>
HDF5TransformIOTemplate<br>
MatlabTransformIOTemplate<br>
MatlabTransformIOTemplate<br>
TxtTransformIOTemplate<br>
TxtTransformIOTemplate<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>

---

## Post #2 by @lassoan (2021-05-08 00:39 UTC)

<p>The problem is that by default (if transform file extension is not specified) then Slicer uses a mini-scene to pass a transform to a CLI module (so that you can get the complete transform tree, not just a single transform). Most CLI modules specify a file extension (such as .h5) and use ITK transform reader without problems. However, there seem to be modules that don’t specify a file extension and still want to use ITK transform reader - this does not work.</p>
<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/6a9cb52eb1a93b031c7388ee5688a28a709fa7b4">changed the behavior in Slicer to use .h5 file format by default</a>, which will fix this issue. The fix will be available in Slicer Preview Release from tomorrow.</p>
<p>However, you may find that the Metric Test Module is only applicable for a very narrow use case. You may achieve much more with writing a short Python script</p>

---

## Post #3 by @HodaGH (2021-05-10 16:53 UTC)

<p>Thank you very much Andras. Would you elaborate more on what you meant by narrow use case? I mean what can I achieve in addition to the MI value?</p>

---

## Post #4 by @lassoan (2021-05-11 04:36 UTC)

<p>It only works for a specific transform type. Also, a single mutual information value is not usable for much: you would need to take many metric samples and analyze the distribution instead. For example, the registration is accurate if you have the optimum near the MI metric minimum; robust if the metric surface is smooth and there are no local minima nearby the global minimum.</p>

---
