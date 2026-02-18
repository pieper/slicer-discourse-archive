# How to resample curve nodes programmatically?

**Topic ID**: 16395
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/how-to-resample-curve-nodes-programmatically/16395

---

## Post #1 by @akshay_pillai (2021-03-05 18:43 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
I just need to automatically resample a centerline curve to 20 control points from more than 100, similar to the resample section in markups module. Can anyone tell me where I can find documentation on the resample function or any code for it?</p>

---

## Post #2 by @lassoan (2021-03-05 18:55 UTC)

<p>Resampling is implemented in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsCurveNode.cxx">curve node</a>. Note that you can access this function from anywhere, not just from Slicer GUI and Python console, but from a command-line script, Jupyter, etc. so there should be no need to reimplement this feature outside Slicer.</p>

---

## Post #3 by @akshay_pillai (2021-03-05 18:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>an access this function from anywhere, not just from Slicer GUI and Python console, but from a command-line script</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I want to access it from the python console. Can you tell me how I can do that?</p>

---

## Post #4 by @lassoan (2021-03-05 19:23 UTC)

<p>For example, if name of your curve node is “C” then you can resample at 10mm sampling distance like this:</p>
<pre><code class="lang-python">getNode('C').ResampleCurveWorld(10)
</code></pre>

---

## Post #5 by @akshay_pillai (2021-03-10 15:37 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> , is there any way I can do this to vtkPolyData? I want to resample the vtkpolydata in the python code for extract centerline(centerline extraction logic)</p>

---

## Post #6 by @lassoan (2021-03-10 15:43 UTC)

<p><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">Extract centerline</a> module already does this. You can use this module as is or extract the code that you need from it.</p>

---

## Post #7 by @akshay_pillai (2021-03-10 15:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks.  I see that extract centerline has these :<br>
centerlineFilter.SetCenterlineResampling(0)<br>
centerlineFilter.SetResamplingStepLength(1.0)</p>
<p>but they are set to 0 and 1. Do I have to change one of these for the actual resampling like resampleCurveWorld(10) above? I’m sorry if this is a stupid question</p>

---

## Post #8 by @lassoan (2021-03-10 15:59 UTC)

<p>You can resample the centerline either in centerlineFilter (by enabling CenterlineResampling and setting the ResamplingStepLength you need) or later using the curve node. Currently, no resampling is performed, so the distances in the output curve depend on the resolution of the input mesh only.</p>

---

## Post #9 by @akshay_pillai (2021-03-10 16:56 UTC)

<p>Thanks, that worked.</p>

---

## Post #10 by @Chuan (2023-09-20 20:06 UTC)

<p>Hi Akshay,</p>
<p>Recently I met a similar question with you. Basically, I have 50 nodes’ coordinates (with a dimension of 50*3), and I want to resample this curve with 100 equidistance nodes.<br>
Do you know how to use Python to get there?</p>
<p>Best,<br>
Chuan</p>

---

## Post #11 by @Chuan (2023-09-21 07:39 UTC)

<p>Hi Lassoan,</p>
<p>It looks very powerful, just I am sorry I still feel confused.<br>
Do you have an example of using ResampleCurveWorld in Python to resample my data?<br>
Because now I seem to have several questions.</p>
<ol>
<li>It looks I need to call c program in Python for this function, but I am not sure.</li>
<li>I don’t know what is correct format of my curve node. Here you mentioned, ‘name of my curve node is C’<br>
I consider as C is an adarray with a dimension of 50*3 (50 points with 3 dimension), is that correct?</li>
<li>And in python, what will be back after calling this function?</li>
</ol>
<p>Best regards,<br>
Siyuan</p>

---

## Post #12 by @lassoan (2023-09-21 14:46 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="16395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>Do you have an example of using ResampleCurveWorld in Python to resample my data?</p>
</blockquote>
</aside>
<p>See above, for example: <code>getNode('C').ResampleCurveWorld(10)</code></p>
<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="16395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>It looks I need to call c program in Python for this function, but I am not sure.</p>
</blockquote>
</aside>
<p>Many of core algorithms and data classes are implemented in C++, but all these classes are directly available in Python. You can call these functions the same way as any other Python function.</p>
<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="16395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>I don’t know what is correct format of my curve node. Here you mentioned, ‘name of my curve node is C’</p>
</blockquote>
</aside>
<p>In the example, I got the curve node (the object represents a curve) from the scene by its name (<code>C</code>). However, if you implement a module then the user will selec the curve node in the module’s GUI; or if you implement a processing script then probably you create the curve, so you have the object in a variable already (you don’t need to retrieve the node from the scene).</p>
<aside class="quote no-group" data-username="Chuan" data-post="11" data-topic="16395">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>I consider as C is an adarray with a dimension of 50*3 (50 points with 3 dimension), is that correct?</p>
</blockquote>
</aside>
<p>A <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsCurveNode.html">curve node</a> stores control point positions and other properties of the curve.</p>
<p>The easiest way to access the control point positions is via <code>slicer.util</code> functions:</p>
<ul>
<li>get point positions: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsControlPoints">slicer.util.arrayFromMarkupsControlPoints()</a></li>
<li>set point positions: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateMarkupsControlPointsFromArray">slicer.util.updateMarkupsControlPointsFromArray()</a></li>
</ul>
<p>See many Python examples for manipulating curves and other markups in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">script repository</a>.</p>

---

## Post #13 by @Chuan (2023-10-06 08:45 UTC)

<p>Thanks! Very clear to me!</p>

---
