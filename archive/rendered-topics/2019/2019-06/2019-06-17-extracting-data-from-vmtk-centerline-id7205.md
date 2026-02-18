# Extracting Data from VMTK Centerline

**Topic ID**: 7205
**Date**: 2019-06-17
**URL**: https://discourse.slicer.org/t/extracting-data-from-vmtk-centerline/7205

---

## Post #1 by @joshWilliams (2019-06-17 19:00 UTC)

<p>Hi,</p>
<p>I am using VMTK’s centreline computation tool to extract a skeleton of a respiratory system (from a stl file, converted to binary label map). I have previewed the skeleton and pressed start to begin extracting data (this took a long time, my computer thought slicer stopped responding at several intervals but I continued running - maybe this is a factor).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/148c9d3aef1c0ab109cfa9b57dcb57261f61d200.png" data-download-href="/uploads/short-url/2VMOsDteIf5AIBFIzBylrK2kCCQ.png?dl=1" title="Screenshot%20from%202019-06-17%2019-02-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148c9d3aef1c0ab109cfa9b57dcb57261f61d200_2_345x230.png" alt="Screenshot%20from%202019-06-17%2019-02-11" data-base62-sha1="2VMOsDteIf5AIBFIzBylrK2kCCQ" width="345" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148c9d3aef1c0ab109cfa9b57dcb57261f61d200_2_345x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148c9d3aef1c0ab109cfa9b57dcb57261f61d200_2_517x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/148c9d3aef1c0ab109cfa9b57dcb57261f61d200_2_690x460.png 2x" data-dominant-color="BFBFDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-06-17%2019-02-11</span><span class="informations">3000×2000 370 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, eventually it finished and I have this skeleton. My issue is now, <strong>how to extract data on coordinates i.e. end points and branch points?</strong></p>
<p>The <a href="https://www.slicer.org/wiki/Modules:VMTK_in_3D_Slicer_Tutorial:_Coronary_Artery_Centerline_Extraction" rel="noopener nofollow ugc">tutorial on this</a> uses an older version of Slicer than I have and appears fairly straight forward, however there are no clear means to extract data from the module on this version.</p>
<p>Any help would be greatly appreciated.</p>
<p>Best,<br>
Josh</p>

---

## Post #2 by @lassoan (2019-06-17 19:44 UTC)

<p>Result of centerline detection is a <a href="https://vtk.org/doc/nightly/html/classvtkPolyData.html" rel="nofollow noopener">vtkPolyData</a> that you can access by calling:</p>
<pre><code class="lang-auto">centerlineModel = getNode('CenterlineComputationModel')
centerlinePoly = centerlineModel.GetPolyData()
</code></pre>
<p>You can then access point positions as you would do for any vtkPolydata. For example:</p>
<p>Get first point position:</p>
<pre><code class="lang-python">centerlinePoly.GetPoints().GetPoint(0)
</code></pre>
<p>Get point IDs of the first line segment:</p>
<pre><code class="lang-python">pointIds = vtk.vtkIdList()
centerlinePoly.GetLines().GetCell(0, pointIds)
</code></pre>

---

## Post #3 by @joshWilliams (2019-06-18 14:36 UTC)

<p>Thanks for your fast reply Andras. I followed your code through and it works fine up to the last line which returns nothing, as shown below:</p>
<pre><code>&gt;&gt;&gt; centerlineModel = getNode('CenterlineComputationModel')
&gt;&gt;&gt; centerlinePoly = centerlineModel.GetPolyData()
&gt;&gt;&gt; centerlinePoly.GetPoints().GetPoint(0)
(-236.95960998535156, 237.93817138671875, 101.977294921875)
&gt;&gt;&gt; 
&gt;&gt;&gt; pointIds = vtk.vtkIdList()
&gt;&gt;&gt; centerlinePoly.GetLines().GetCell(0, pointIds)
&gt;&gt;&gt; print centerlinePoly.GetLines().GetCell(0, pointIds)
None
</code></pre>
<p>Can you give any advice on how to proceed? My intention was to use the centerline computation to extract coordinates of centerpoints and branch points (and I was hoping these would be clearly defined in the output file for ease of scripting the recognition of this, is this so?).</p>
<p>Apologies but I am a complete newbie when it comes to vtk and 3D Slicer.</p>
<p>If it helps, I found the ID list to be empty<br>
<code>&gt;&gt;&gt; pointIds = vtk.vtkIdList()</code><br>
<code>&gt;&gt;&gt; print pointIds</code><br>
vtkIdList (0x6562580)<br>
Debug: Off<br>
Modified Time: 98975746<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Number of Ids: 0</p>

---

## Post #4 by @lassoan (2019-06-18 14:39 UTC)

<p><code>pointIds</code> is a <a href="https://vtk.org/doc/nightly/html/classvtkIdList.html" rel="nofollow noopener">vtkIdList</a> object, contain a list of point IDs. For example, you can get number of points in it using <code>GetNumberOfIds</code> and get Nth point ID using <code>GetId</code>. Check out <a href="https://lorensen.github.io/VTKExamples/site/" rel="nofollow noopener">VTK examples</a> site to see examples of using VTK objects in Python.</p>

---
