# Strange Behaviour Scripting with Curve Maker Extension [Solved]

**Topic ID**: 575
**Date**: 2017-06-26
**URL**: https://discourse.slicer.org/t/strange-behaviour-scripting-with-curve-maker-extension-solved/575

---

## Post #1 by @_jmichael (2017-06-26 21:23 UTC)

<p>I’m working with the 3D slicer extension <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/CurveMaker" rel="nofollow noopener">CurveMaker</a> that makes line/curve models based on fiducials. I wrote a simple convenience function (below) in python that sends all of the sets of MarkupsFiducial in the scene to CurveMaker and the function works <strong>but</strong> only if, since opening Slicer, I have first navigated to the CurveMaker module. If I haven’t, attempting to access ‘slicer.modules.CurveMakerWidget’ returns, "object has no attribute ‘CurveMakerWidget’ ".</p>
<p>How do I avoid this problem without requiring user interaction? Am I breaking best-practices by trying to access the logic through the widget? or is this simply a bug/shortcoming in the module?</p>
<pre><code>def sendAllFiducialsToCurveMaker():
  N = slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLMarkupsFiducialNode')
  ####
  #line below returns "AttributeError: 'module' object has no attribute 'CurveMakerWidget' " 
  #unless I have first navigated to the Curve Maker module
  cml = slicer.modules.CurveMakerWidget.logic 
  ####
  for i in xrange(N):
    cml.SourceNode = slicer.mrmlScene.GetNthNodeByClass(i,'vtkMRMLMarkupsFiducialNode')
    outputModel = slicer.vtkMRMLModelNode()
    slicer.mrmlScene.AddNode(outputModel)
    cml.DestinationNode = outputModel
    cml.generateCurveOnce()</code></pre>

---

## Post #2 by @pieper (2017-06-26 21:50 UTC)

<p>The module widget is created “lazily” so as you saw it only exists after visiting the module once.</p>
<p>You can do this programmatically with something like this:</p>
<pre><code class="lang-auto">mainWindow = slicer.util.mainWindow()
mainWindow.moduleSelector().selectModule('CurveMaker')
</code></pre>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @lassoan (2017-06-26 22:01 UTC)

<p>I would recommend to use “Markups to model” module in SlicerIGT extension.</p>
<p>It does everything that CurveMaker but much more (for example it can handle any number of models, not just one; it can also generate surfaces) and it is a full-featured module: saving/reloading state to the scene works well, initialization is done properly (no need to open the module GUI), it is faster (fully implemented in C++), etc.</p>

---

## Post #4 by @_jmichael (2017-06-27 13:53 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, both excellent solutions. Also re-assuring to know I hadn’t missed something obvious.</p>
<p>Thanks for your help!</p>

---
