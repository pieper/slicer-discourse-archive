# Vtk.util cannot be found in ParrallelProcessing

**Topic ID**: 32730
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/vtk-util-cannot-be-found-in-parrallelprocessing/32730

---

## Post #1 by @wrc (2023-11-11 00:56 UTC)

<p>Hi, I want to transfer numpy array to vtkPoints in a script under the extension ParrallelProcessing. I use</p>
<pre><code class="lang-auto">import vtk
fp = vtk.vtkPoints()
fp.SetData(vtk.util.numpy_support.numpy_to_vtk(points))
</code></pre>
<p>but return</p>
<pre><code class="lang-auto">AttributeError: module 'vtk' has no attribute 'util'
</code></pre>
<p>However, vtk.util works fine in the main python script (not in ParrallelProcessing). Is there any limitation of the ParrallelProcessing? Thank you.</p>

---

## Post #2 by @pieper (2023-11-11 21:39 UTC)

<p>You’ll need to explicitly do <code>import vtk.util</code>.  The Slicer app imports several packages (vtk, ctk, qt…) but when you run in in the <code>PythonSlicer</code> environment you get Slicer’s python build but without the Slicer parts.</p>

---
