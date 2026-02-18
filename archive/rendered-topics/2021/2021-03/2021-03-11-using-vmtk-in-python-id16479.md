# Using VMTK in Python

**Topic ID**: 16479
**Date**: 2021-03-11
**URL**: https://discourse.slicer.org/t/using-vmtk-in-python/16479

---

## Post #1 by @RafaelPalomar (2021-03-11 14:37 UTC)

<p>Hello,</p>
<p>I’m trying to use the functionality of VMTK in the python interpreter (Slicer stable 20210226, Linux. Slicer-VMTK extension installed from the extension manager). When trying to <code>import vtkvmtk</code> I ge the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/rafael/src/Slicer-stable/build/Slicer-build/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py", line 9, in &lt;module&gt;
    from .vtkvmtkCommonPython import *
ImportError: attempted relative import with no known parent package
</code></pre>
<p>Is this expected? Is there any other way to make use of VMTK in the Slicer python interpreter?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-03-11 14:48 UTC)

<p>We import VMTK like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L503" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L503" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L503</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="493" style="counter-reset: li-counter 492 ;">
<li>    normals.SplittingOff()</li>
<li>    normals.Update()</li>
<li>
<li>    return normals.GetOutput()</li>
<li>
<li>def extractNonManifoldEdges(self, polyData, nonManifoldEdgesPolyData=None):</li>
<li>    '''</li>
<li>    Returns non-manifold edge center positions.</li>
<li>    nonManifoldEdgesPolyData: optional vtk.vtkPolyData() input, if specified then a polydata is returned that contains the edges</li>
<li>    '''</li>
<li class="selected">    import vtkvmtkDifferentialGeometryPython as vtkvmtkDifferentialGeometry</li>
<li>    neighborhoods = vtkvmtkDifferentialGeometry.vtkvmtkNeighborhoods()</li>
<li>    neighborhoods.SetNeighborhoodTypeToPolyDataManifoldNeighborhood()</li>
<li>    neighborhoods.SetDataSet(polyData)</li>
<li>    neighborhoods.Build()</li>
<li>
<li>    polyData.BuildCells()</li>
<li>    polyData.BuildLinks(0)</li>
<li>
<li>    edgeCenterPositions = []</li>
<li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It could be nice to fix this and and also the error message at startup (<a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" class="inline-onebox">Fail to instantiate module “vtkvmtk” error reported at startup · Issue #22 · vmtk/SlicerExtension-VMTK · GitHub</a>) but we have been holding off changes until VTK9 update and VTK’s new remote module support is in place (see <a href="https://discourse.vtk.org/t/rfc-toward-supporting-distribution-of-vtk-based-modules-on-pypi/4873" class="inline-onebox">RFC: Toward supporting distribution of VTK based modules on PyPI - Support - VTK</a>).</p>

---

## Post #3 by @RafaelPalomar (2021-03-11 16:21 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>! That solved the problem.</p>

---

## Post #4 by @RafaelPalomar (2021-03-12 09:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16479">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It could be nice to fix this and and also the error message at startup (<a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/22" rel="noopener nofollow ugc">Fail to instantiate module “vtkvmtk” error reported at startup · Issue #22 · vmtk/SlicerExtension-VMTK · GitHub</a>)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Is this a matter of where Slicer-VMTK  installs the files, or is Slicer that needs to accommodate the plugin infrastructure?</p>

---

## Post #5 by @lassoan (2021-03-27 18:36 UTC)

<p>It is just a matter of where Slicer-VMTK installs VMTK DLLs. For example, the DLLs could be in a subdirectory inside the scripted module folder and not directly in the module folder.</p>

---
