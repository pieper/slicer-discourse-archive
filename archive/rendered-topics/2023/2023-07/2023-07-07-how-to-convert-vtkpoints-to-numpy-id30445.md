# How to convert vtkPoints to numpy?

**Topic ID**: 30445
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/how-to-convert-vtkpoints-to-numpy/30445

---

## Post #1 by @wrc (2023-07-07 08:06 UTC)

<p>Hello, I want to convert vtkPoints to numpy. I used</p>
<pre><code class="lang-auto">vtk.util.numpy_support.vtk_to_numpy(vtkPoints)
</code></pre>
<p>But I got</p>
<pre><code class="lang-auto">  File "/Applications/Slicer.app/Contents/bin/Python/vtkmodules/util/numpy_support.py", line 220, in vtk_to_numpy
    shape = vtk_array.GetNumberOfTuples(), \
AttributeError: 'vtkmodules.vtkCommonCore.vtkPoints' object has no attribute 'GetNumberOfTuples'
</code></pre>
<p>How to solve this problem?<br>
Thank you very much.</p>

---

## Post #2 by @cpinter (2023-07-07 08:55 UTC)

<p>You can use <code>slicer.util.arrayFromModelPoints</code> if you have a model node or if it makes sense to create one. Otherwise check out the implementation of said function.</p>

---
