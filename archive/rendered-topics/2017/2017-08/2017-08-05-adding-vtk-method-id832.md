---
topic_id: 832
title: "Adding Vtk Method"
date: 2017-08-05
url: https://discourse.slicer.org/t/832
---

# Adding VTK method?

**Topic ID**: 832
**Date**: 2017-08-05
**URL**: https://discourse.slicer.org/t/adding-vtk-method/832

---

## Post #1 by @hherhold (2017-08-05 19:28 UTC)

<p>VTK provides a method for determining the center of mass of a dataset. See:</p>
<p><a href="https://itk.org/Wiki/VTK/Examples/Cxx/PolyData/CenterOfMass" class="onebox" target="_blank" rel="nofollow noopener">https://itk.org/Wiki/VTK/Examples/Cxx/PolyData/CenterOfMass</a></p>
<p>I’m interested in adding this capability to an extension in Slicer, the goal being to determine the center of mass of a given segment.</p>
<p>I’ve done some reading of the source (I know C++ and a little python) but I am very much a newbie on the architecture of Slicer. I’m wondering if someone has done something similar (adding VTK method and accessing it through python for an Extension GUI) that I can borrow/steal.</p>
<p>Thanks in advance,</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2017-08-05 20:08 UTC)

<p>Hi Hollister -</p>
<p>Yes, pretty much all vtk functionality is accessible through python and easy to use in a python scripted extension.</p>
<p>These two programming tutorials are a good start:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers</a></p>
<p>Also you can find examples the script repository here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>
<p>For example, if you have created a default segmentation with a surface mode, you can do this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n = getNode('Segmentation')
&gt;&gt;&gt; s = n.GetSegmentation()
&gt;&gt;&gt; ss = s.GetSegment('Segment_1')
&gt;&gt;&gt; pd = ss.GetRepresentation('Closed surface')
&gt;&gt;&gt; com = vtk.vtkCenterOfMass()
&gt;&gt;&gt; com.SetInputData(pd)
&gt;&gt;&gt; com.Update()
&gt;&gt;&gt; com.GetCenter()
(33.686966862924784, 10.410245678682282, 5.923210996529306)
</code></pre>

---

## Post #3 by @hherhold (2017-08-05 23:05 UTC)

<p>Hi Steve,</p>
<p>That’s <em>exactly</em> what I was looking for!</p>
<p>Thank you very much!</p>
<p>-Hollister</p>

---
