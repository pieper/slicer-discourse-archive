# CenterLine strange error - Using `--no-main--window`

**Topic ID**: 26696
**Date**: 2022-12-12
**URL**: https://discourse.slicer.org/t/centerline-strange-error-using-no-main-window/26696

---

## Post #1 by @lucas_sd (2022-12-12 15:36 UTC)

<p>Hi everybody,</p>
<p>Im using the module for obtain the centerline from a segmentation. I created a module wich call the centerline module and it works fine. When I run the same code but using slicer --no-main–window, the program crash always in the same line of code.</p>
<p>Its strange, its the same code and the same inputs. When I run it as a module I get the centerline but when I run it like a py code using slicer --no-main-window, it doesnt.</p>
<p>Aways crash in this line, and I put also the lines that I use for work with ExtractCenterLine.</p>
<p>In another case, there is other way to work with ExtractCenterLine different?</p>
<p>Thanks, Lucas.</p>
<pre><code class="lang-auto"># The line of problems.
preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)
</code></pre>
<pre><code class="lang-auto"># Preprocess the surface
inputSurfacePolyData = extractLogic.polyDataFromNode(segmentationNode, segmentID)
targetNumberOfPoints = 5000.0
decimationAggressiveness = 4
subdivideInputSurface = False
preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)

# Extract the centerline
centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "Centerline curve")
centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, pointListNode)
centerlinePropertiesTableNode = None
extractLogic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode)
</code></pre>

---

## Post #2 by @lassoan (2022-12-12 17:47 UTC)

<p>The application main window takes care of many tasks. It would be practically impossible to test all the features of the application with and without main window. Some years ago we tried, but it just took too much of our time, and for creating simplified applications (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">slicelets</a>) we found that having a main window and just hiding unwanted elements works much better. The <code>--no-main-window</code> only exists for component-level testing, and for application-level tests or using application features.</p>

---

## Post #3 by @lucas_sd (2022-12-13 14:56 UTC)

<p>Hi Andras, thanks for your help and comments. Finally, I managed to use <code>-no-main-window</code>.</p>
<p>This is my line:</p>
<pre><code class="lang-auto">./Slicer --python-script 'myscript.py' --testing --no-splash --no-main-window 
</code></pre>
<p>I removed <code>--testing</code> and it worked. Maybe those comments can be useful for other people.</p>
<p>Thanks, Lucas.</p>

---

## Post #4 by @chir.set (2022-12-13 15:22 UTC)

<aside class="quote no-group" data-username="lucas_sd" data-post="3" data-topic="26696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucas_sd/48/17087_2.png" class="avatar"> lucas_sd:</div>
<blockquote>
<p>Maybe those comments can be useful for other people.</p>
</blockquote>
</aside>
<p>Oh yes, I think they would help me install/uninstall extensions from local packages without fully launching Slicer, thanks ! Still have to test.</p>

---
