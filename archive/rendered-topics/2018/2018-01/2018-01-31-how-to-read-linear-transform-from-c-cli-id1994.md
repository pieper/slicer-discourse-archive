---
topic_id: 1994
title: "How To Read Linear Transform From C Cli"
date: 2018-01-31
url: https://discourse.slicer.org/t/1994
---

# How to read linear transform from C++ CLI

**Topic ID**: 1994
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/how-to-read-linear-transform-from-c-cli/1994

---

## Post #1 by @dzenanz (2018-01-31 22:03 UTC)

<p>Slicer used to write <code>.h5</code> or <code>.tfm</code> files when a transform needed to be passed to a CLI:</p>
<pre><code>&lt;transform type="linear" fileExtensions=".tfm,.h5,.hdf5,.mat,.txt"&gt;
  &lt;longflag&gt;transform0&lt;/longflag&gt;
  &lt;description&gt;...&lt;/description&gt;
  &lt;label&gt;rigid transform 0&lt;/label&gt;
  &lt;channel&gt;input&lt;/channel&gt;
&lt;/transform&gt;
</code></pre>
<p>but now a CLI gets <code>--transform0 C:/Temp/Slicer/BDBAI_AAAAAAAABFECHIFA.mrml#vtkMRMLLinearTransformNode1</code> which <strong>itk::TransformFileReader</strong> cannot read. How to force Slicer to write an ITK-readable transform?</p>

---

## Post #2 by @lassoan (2018-01-31 22:50 UTC)

<p>Which Slicer version does this? Many CLI modules uses transforms with ITK readers - do they work correctly?</p>

---

## Post #3 by @dzenanz (2018-01-31 22:52 UTC)

<p>1aa2f026195e7f8206748867cca4a6fc46197f7c from 2018-01-27</p>

---

## Post #4 by @ihnorton (2018-02-01 02:01 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="1" data-topic="1994">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>How to force Slicer to write an ITK-readable transform?</p>
</blockquote>
</aside>
<p>Are you using the “force executable” setting in Settings-&gt;Modules?</p>

---

## Post #5 by @lassoan (2018-02-01 03:56 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Many CLI modules uses transforms with ITK readers - do they work correctly?</p>
<p>For example, “Resample Scalar/Vector/DWI volume” module works correctly for me, writing the transform to .h5 file.</p>
<details>
<summary>
Full command line</summary>
<p>Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/D/S4R/Slicer-build/lib/Slicer-4.9/cli-modules/Release/ResampleScalarVectorDWIVolume.exe --Reference C:/Users/msliv/AppData/Local/Temp/Slicer/CCCEE_vtkMRMLScalarVolumeNodeB.nrrd --transformationFile C:/Users/msliv/AppData/Local/Temp/Slicer/CCCEE_vtkMRMLLinearTransformNodeE.h5 --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0,0,0 --size 0,0,0 --direction_matrix 0,0,0,0,0,0,0,0,0 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/msliv/AppData/Local/Temp/Slicer/CCCEE_vtkMRMLScalarVolumeNodeB.nrrd C:/Users/msliv/AppData/Local/Temp/Slicer/CCCEE_vtkMRMLScalarVolumeNodeD.nrrd</p>
</details>
<p>It uses this XML:</p>
<pre><code>&lt;transform fileExtensions=".h5"&gt;
  &lt;name&gt;transformationFile&lt;/name&gt;
  &lt;label&gt;Transform Node&lt;/label&gt;
  &lt;flag&gt;-f&lt;/flag&gt;
  &lt;longflag&gt;--transformationFile&lt;/longflag&gt;
  &lt;default/&gt;
  &lt;channel&gt;input&lt;/channel&gt;
&lt;/transform&gt;
</code></pre>
<p>You can add the few missing tags to your XML file (name, default, flag) and see if it makes a difference.</p>

---

## Post #6 by @dzenanz (2018-02-01 16:17 UTC)

<p>After changing the <code>fileExtensions=".tfm,.h5,.hdf5,.mat,.txt"</code> into <code>fileExtensions=".tfm"</code> and recompiling the problem went away. Then I changed back into the original, and the transforms are still being written normally (as <code>.tfm</code> files). Perhaps changes to CMake code made the difference. I explicitly added this (trying to fix an unrelated linking error with tests):</p>
<pre><code>find_package(SlicerExecutionModel REQUIRED)
include(${SlicerExecutionModel_USE_FILE})

set(MABMIS_ITK_COMPONENTS
  ITKIOImageBase
  ITKTransform
  ITKIOTransformBase
  ITKIOXML
  )
find_package(ITK 4.6 COMPONENTS ${MABMIS_ITK_COMPONENTS} REQUIRED)
set(ITK_NO_IO_FACTORY_REGISTER_MANAGER 1) # See Libs/ITKFactoryRegistration/CMakeLists.txt
include(${ITK_USE_FILE})

find_package(Slicer)
include(${Slicer_USE_FILE})
</code></pre>
<p>But why would any of this make a difference?</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Disabling “Prefer executable CLIs” passes the images via pointer, but does not seem to affect transforms.</p>

---

## Post #7 by @fedorov (2018-02-02 13:00 UTC)

<p>Are you running CLI a executable or shared library?</p>

---

## Post #8 by @fedorov (2018-02-02 13:04 UTC)

<p>Sorry for the noise, I was on the phone and didn’t see the full thread.</p>

---

## Post #9 by @lassoan (2018-02-02 13:57 UTC)

<p>I think you need to force recompilation after you change the module description XML. I noticed in the past that XML file changes did not take effect with a simple build.</p>

---
