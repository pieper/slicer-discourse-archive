---
topic_id: 1319
title: "Error With Converting Ras To Ijk Coordinates"
date: 2017-10-30
url: https://discourse.slicer.org/t/1319
---

# Error With Converting RAS to IJK coordinates

**Topic ID**: 1319
**Date**: 2017-10-30
**URL**: https://discourse.slicer.org/t/error-with-converting-ras-to-ijk-coordinates/1319

---

## Post #1 by @lpott005 (2017-10-30 13:47 UTC)

<p>Hello Slicer Community,</p>
<p>I was using this older post as a guide to convert RAS to IJK coordinates: <a href="http://slicer-devel-archive.65872.n3.nabble.com/Get-coordinates-from-Fiducials-td4034132.html" rel="nofollow noopener">http://slicer-devel-archive.65872.n3.nabble.com/Get-coordinates-from-Fiducials-td4034132.html</a></p>
<p>But when I use “volumeNode.GetRASToIJKMatrix(rasToIJK)” I get an “AttributeError: ‘NoneType’ object has no attribute ‘GetRASToIJKMatrix’” Error call.</p>
<p>I’m using the Python interactor in 4.7.0, if that helps.</p>

---

## Post #2 by @ihnorton (2017-10-30 13:48 UTC)

<p>It means that <code>volumeNode</code> is not pointing to a node – probably the call to <code>getNode(name)</code> or a similar call failed. You can check this in the python interactor:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n = getNode("foo")
&gt;&gt;&gt; print(n)
None
</code></pre>

---

## Post #3 by @lpott005 (2017-10-30 14:17 UTC)

<p>Good call- I added print statements for everything up to that and I notice two things.</p>
<p>After <code>print(volumeNode)</code>, the interactor just returns an empty line. And after <code>print(volumeNode)</code>, the interactor returns “None”. Any pointers for how to fix that?</p>

---

## Post #4 by @ihnorton (2017-10-30 14:34 UTC)

<p><code>volumeNode</code> is still not set to a MRML node… Whatever call you are making to assign <code>volumeNode</code> is failing (e.g.: <code>volumeNode = ...</code>), so you need to start there and figure out why.</p>
<p>There’s not much more we can say without some code demonstrating the problem. Please post a short example of what you are doing using data from the <a href="https://www.slicer.org/wiki/SampleData">Sample Data</a>.</p>

---

## Post #5 by @lpott005 (2017-10-31 12:58 UTC)

<p>I just want to get the transformation for RAS to IJK- I’m working with an older library that needs the voxel coordinates, not the mm coordinates.</p>
<p>I downloaded the sample data “MR-Head”, and placed a fiducial at (0,0,0) and used the same code- I gave me the same error though.</p>

---

## Post #6 by @ihnorton (2017-10-31 13:29 UTC)

<pre><code class="lang-auto">volumeNode = slicer.util.getNode("FOO")
print volumeNode
</code></pre>
<blockquote>
<p>None</p>
</blockquote>
<pre><code class="lang-auto">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
sampleDataLogic.downloadMRHead()

volumeNode = slicer.util.getNode("MRHead")
print volumeNode
</code></pre>
<blockquote>
<p>vtkMRMLScalarVolumeNode (0x7fe62896cff0)<br>
ID: vtkMRMLScalarVolumeNode2<br>
Class: vtkMRMLScalarVolumeNode<br>
…</p>
</blockquote>
<pre><code class="lang-auto">mat = vtk.vtkMatrix4x4()
volumeNode.GetRASToIJKMatrix(mat)
print mat
</code></pre>
<blockquote>
<p>vtkMatrix4x4 (0x7fe628ecd4b0)<br>
Debug: Off<br>
Modified Time: 9287983<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Elements:<br>
0 -1 0 133.929<br>
-0 0 -1 116.786<br>
0.769233 0 0 66.6502<br>
-0 0 -0 1</p>
</blockquote>

---

## Post #7 by @lpott005 (2017-10-31 13:56 UTC)

<p>Wonderful, thanks so much!</p>

---
