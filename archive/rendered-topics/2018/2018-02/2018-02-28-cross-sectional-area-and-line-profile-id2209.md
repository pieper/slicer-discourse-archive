# Cross-sectional area and line profile

**Topic ID**: 2209
**Date**: 2018-02-28
**URL**: https://discourse.slicer.org/t/cross-sectional-area-and-line-profile/2209

---

## Post #1 by @stevenagl12 (2018-02-28 16:34 UTC)

<p>Hi, I am wondering how you would go about creating a graph in slicer of the cross sectional area changes as you go from one side of a model to another, and the same for the line profiles for the cross-section as you go from one side to another. Also, if possible, is there a method to extract the average line profile from a mesh? To give you more background, I am trying to perform these analyses on meshes of clavicles that I segmented to analyze radiodensity and cross-sectional area differences.</p>

---

## Post #2 by @lassoan (2018-02-28 18:22 UTC)

<blockquote>
<p>how you would go about creating a graph in slicer of the cross sectional area changes as you go from one side of a model to another</p>
</blockquote>
<p>You can use <a href="https://www.vtk.org/doc/nightly/html/classvtkCutter.html">vtkCutter</a> to get cross-section polygons along the line profile and VTK can compute the cross-sectional area. Probably 10-15 lines of simple Python script.</p>
<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="2209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>is there a method to extract the average line profile from a mesh?</p>
</blockquote>
</aside>
<p>You can convert your model to Segmentation, export to labelmap, use Extract Skeleton module to get points along the centerline, and can fit a line to these centerline points.</p>

---

## Post #3 by @stevenagl12 (2018-03-01 16:07 UTC)

<p>Once you get the skeleton, how can you get the line profile in slicer? Also, is it possible to give me an example script for the vtkCutter?</p>

---

## Post #4 by @lassoan (2018-03-01 16:27 UTC)

<p>Skeleton can return markup fiducials (in recent nightly versions), which you can use with MarkupsToModel module to generate a smooth, interpolated line. You go along that line and generate a cutting plane (compute plane position and normal using basic vector algebra) and set it as input to vtkCutter.</p>
<p>VTK examples website contains fully functional examples for all VTK classes. For example, here is one for vtkCutter: <a href="https://lorensen.github.io/VTKExamples/site/Java/Miscellaneous/Cutter/">https://lorensen.github.io/VTKExamples/site/Java/Miscellaneous/Cutter/</a></p>

---

## Post #5 by @stevenagl12 (2018-03-01 16:33 UTC)

<p>I’m confused how this gives you a line profile for intensity values?</p>

---

## Post #6 by @lassoan (2018-03-01 16:46 UTC)

<p>I though you mean cross-sectional area profile. Intensity profile along a line is even simpler, see <a href="https://github.com/lassoan/SlicerLineProfile/blob/master/LineProfile/LineProfile.py">https://github.com/lassoan/SlicerLineProfile/blob/master/LineProfile/LineProfile.py</a></p>

---

## Post #7 by @stevenagl12 (2018-03-06 02:46 UTC)

<p>That helped thank you.</p>

---

## Post #8 by @Jojobus (2018-03-27 07:05 UTC)

<p>Hi everyone,</p>
<p>About the LineProfile.py script, I don’t know how to implement it as a additional module in 3D Slicer.</p>
<p>Can anyone may give me the instructions or a tutorial link in this purpose, please?</p>
<p>Sorry if the question seems too much straightforward.</p>
<p>Jonathan</p>

---

## Post #9 by @lassoan (2018-03-27 20:52 UTC)

<p>Have you completed the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Programming_Tutorial">Slicer programming tutorial</a> yet? It would be a good start. If you have questions then let us know.</p>

---

## Post #10 by @ycpan (2019-11-26 00:04 UTC)

<p>I know it’s been a while since this question was last asked, but I wanted to give a more detailed solution on how I personally installed the Line Profile extension.</p>
<ol>
<li>Download the entire github repository and extract the folder from .zip</li>
<li>Go to Slicer --&gt; Extension Wizard module --&gt; Select Extension</li>
<li>Select the entire folder that you just extracted</li>
</ol>
<p>Once you do all these steps, you should see Line Profile in your extensions.</p>

---

## Post #11 by @uwo27 (2020-01-09 20:03 UTC)

<p>I’ve followed all the steps detailed by ycpan but this error message popped up "The ._LineProfile module could not be registered.</p>

---

## Post #12 by @lassoan (2020-01-09 21:42 UTC)

<p>We have added line profile module to SlicerSandbox extension (in Examples category), so you don’t need to manually download and install the module anymore.</p>

---
