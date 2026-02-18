# Help Installing vtkITK module

**Topic ID**: 13451
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/help-installing-vtkitk-module/13451

---

## Post #1 by @rohan_n (2020-09-11 20:51 UTC)

<p>Hello,<br>
This isn’t exactly a Slicer question, but I thought someone on these forums may be able to help.<br>
I want to use vtkITK.vtkITKIslandMath<br>
However, I would prefer to use it on a regular Python installation instead of 3D Slicer.<br>
Can you pip install the module vtkITK? If so what is the syntax for this?<br>
python -m pip install vtkITK<br>
didn’t work for me.</p>

---

## Post #2 by @lassoan (2020-09-11 21:03 UTC)

<p>ITK island math filter may be available on PyPI via ITK or SimpleITK Python package.</p>
<p>If you want to use vtkITK package then you need to use the Python virtual environment provided by Slicer.</p>

---

## Post #3 by @rohan_n (2020-09-11 23:07 UTC)

<p>Thanks. I’ve decided to run this in Slicer. If you don’t mind, could you also let me know how to convert my image, which is a SimpleITK object, into a format that can be accepted by the vtkITKIslandMath filter? And also how to convert the output of this filter back into a SimpleITK object?</p>

---

## Post #4 by @lassoan (2020-09-12 04:07 UTC)

<p>You can pass volumes between SimpleITK and Slicer scene using stikUtils. See example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK</a></p>

---

## Post #5 by @rohan_n (2020-09-14 17:49 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="13451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>vtkITK.vtkITKIslandMath</p>
</blockquote>
</aside>
<p>Thanks, unfortunately vtkITKIslandMath only takes vtkAlgorithmOutput as an input, and I’m not sure how to get that.</p>

---

## Post #6 by @lassoan (2020-09-14 17:55 UTC)

<p>Since vtkITKIslandMath is derived from <a href="https://vtk.org/doc/nightly/html/classvtkSimpleImageToImageFilter.html">vtkSimpleImageToImageFilter</a>, it can use both data (<code>SetInputData()</code>) and connection (<code>SetInputConnection()</code>) as input, just as any other VTK filter.</p>

---

## Post #7 by @dbtruong (2023-06-12 15:32 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, What is vtkITKIslandMath used for when the input is a binary image?</p>

---

## Post #8 by @lassoan (2023-07-02 11:43 UTC)

<p>vtkITKIslandMath assigns unique label value to each connected region in an image. See details in its <a href="https://apidocs.slicer.org/master/classvtkITKIslandMath.html">documentation</a>.</p>

---

## Post #9 by @dbtruong (2023-07-03 01:33 UTC)

<p>Does vtk have any similar library? <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #10 by @lassoan (2023-07-03 02:06 UTC)

<p>I don’t think VTK has such filter. We only add those ITK filters to vtkITK that do not have an equivalent in VTK.</p>

---
