---
topic_id: 11078
title: "Itk Filters In 3D Slicer"
date: 2020-04-11
url: https://discourse.slicer.org/t/11078
---

# Itk Filters in 3D slicer

**Topic ID**: 11078
**Date**: 2020-04-11
**URL**: https://discourse.slicer.org/t/itk-filters-in-3d-slicer/11078

---

## Post #1 by @loubna (2020-04-11 13:11 UTC)

<p>how can I use  itk filters in 3D slicer. I’d like to know how can i use ITK package inside my c++ loadable module for 3d Slicer 4.10. How can I import it in 3d slicer</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-04-12 14:25 UTC)

<p>Lots of Slicer components use ITK. You can have a look at modules in Modules\CLI or Libs\vtkITK library for examples.</p>

---

## Post #3 by @loubna (2020-04-12 16:36 UTC)

<p>I have checked the both folders but I don’t find the ITK filters that i want apply. However I find ITK-build folder with ITK solution.</p>
<p>I want use the following ITK filters in a c++ loadable module :  itk::BinaryFillholeImageFilter and *itkBinaryContourImageFilter . what I must do to be able to add :<br>
*<span class="hashtag">#include</span> &lt;itkBinaryContourImageFilter.h&gt; and<br>
<span class="hashtag">#include</span> “itkBinaryFillholeImageFilter.h” in my c++ loadable module.</p>
<p>Thank’s in advance</p>

---

## Post #4 by @loubna (2020-04-12 19:07 UTC)

<p>I just find. json files and not .h files “includes”</p>

---

## Post #5 by @lassoan (2020-04-12 21:44 UTC)

<p>Slicer downloads and builds entire ITK. You can include ITK headers and link ITK libraries to your modules as shown in the examples I linked above.</p>

---
