---
topic_id: 44495
title: "Draw Tube Scripting"
date: 2025-09-16
url: https://discourse.slicer.org/t/44495
---

# Draw tube scripting

**Topic ID**: 44495
**Date**: 2025-09-16
**URL**: https://discourse.slicer.org/t/draw-tube-scripting/44495

---

## Post #1 by @bserrano (2025-09-16 12:27 UTC)

<p>Hi all,</p>
<p>I am trying to automate the <strong>“Draw Tube”</strong> effect in Segment Editor using Python, but I am stuck at two points:</p>
<ol>
<li>
<p>How to pass an existing <strong>centerline</strong> to the effect programmatically (similar to setting <code>"Radius"</code> or <code>"Interpolation"</code> via <code>setParameter()</code>).</p>
</li>
<li>
<p>How to trigger the <strong>“Import”</strong> button automatically via code after setting the parameters.</p>
</li>
</ol>
<p>Here is what I have so far:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setActiveEffectByName("Draw tube")
effect = segmentEditorWidget.activeEffect()

effect.setParameter("Radius", 0.3)
effect.setParameter("Interpolation", "CARDINAL_SPLINE")  # or "LINEAR"

</code></pre>
<p>I want to fully automate the workflow: use an existing <strong>MarkupsCurveNode</strong> as the centerline, generate the tube segment, and “import” it, without any manual interaction.</p>
<p>Could someone please advise:</p>
<ul>
<li>
<p>What is the correct parameter name for passing a centerline to the Draw Tube effect?</p>
</li>
<li>
<p>How can I simulate clicking the Import button programmatically in Python?</p>
</li>
<li>
<p>Why does setting <code>"Interpolation"</code> update the GUI but <code>"Radius"</code> does not, and how should I set the radius properly so the interface updates as well?</p>
</li>
</ul>
<p>Thank you in advance!</p>

---

## Post #2 by @bserrano (2025-09-16 13:01 UTC)

<p>I’ve just found the solution.</p>
<pre><code class="lang-auto">
curveNode=getNode('Centerline_Curve_left_2')
effect.self().markupNodeSelector.setCurrentNodeID(curveNode.GetID())
 
effect.self().importButton.click()
</code></pre>

---

## Post #3 by @bserrano (2025-09-17 09:49 UTC)

<p>Correction:<br>
Radius value is set with:<br>
<code>effect.self().radiusSpinBox.value = 0.3</code></p>
<p>instead of:<br>
<code>effect.setParameter("Radius", 0.3)</code></p>

---

## Post #4 by @cpinter (2025-09-17 11:26 UTC)

<p>Thank you for posting the solution so that others can learn from it <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @SANTIAGO_PENDON_MING (2026-02-03 08:02 UTC)

<p>Hi to everyone!</p>
<p>Using the DrawTube scriptable effect I found a concerning situation:</p>
<pre data-code-wrap="python"><code class="lang-python">def updateModelFromMarkup(self, inputMarkup, outputModel):
“”"Update model to enclose all points in the input markup list“”"interpolationName = self.scriptedEffect.parameter(“Interpolation”)polynomialFitType = slicer.vtkMRMLMarkupsToModelNode.MovingLeastSquaresif interpolationName == “LINEAR”:interpolationType = slicer.vtkMRMLMarkupsToModelNode.Linearelif interpolationName == “CARDINAL_SPLINE”:interpolationType = slicer.vtkMRMLMarkupsToModelNode.CardinalSplineelif interpolationName == “KOCHANEK_SPLINE”:interpolationType = slicer.vtkMRMLMarkupsToModelNode.KochanekSplineelif interpolationName == “GLOBAL_POLYNOMIAL”:interpolationType = slicer.vtkMRMLMarkupsToModelNode.PolynomialpolynomialFitType = slicer.vtkMRMLMarkupsToModelNode.GlobalLeastSquareselif interpolationName == “MOVING_POLYNOMIAL”:interpolationType = slicer.vtkMRMLMarkupsToModelNode.PolynomialpolynomialFitType = slicer.vtkMRMLMarkupsToModelNode.MovingLeastSquares


NumberOfLineSegmentsBetweenControlPoints = self.scriptedEffect.integerParameter("NumberOfLineSegmentsBetweenControlPoints")

markupsToModel = slicer.modules.markupstomodel.logic()
# Create tube from points
markupsToModel.UpdateOutputCurveModel( inputMarkup, outputModel,
  interpolationType, False, self.radius, 8, NumberOfLineSegmentsBetweenControlPoints, True, 3,
  slicer.vtkMRMLMarkupsToModelNode.RawIndices, self.curveGenerator,
  polynomialFitType )
</code></pre>
<p>In this fuction (from SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py)  the number of points in the surface to do the tube faces is set to 8 and this can not be modified. Why? If I set this to 32 for example the generated segment is much smoother than with 8.</p>
<p>In my case, I work with a big cylinder and using 8 points produce a very narrow output.</p>

---

## Post #6 by @cpinter (2026-02-05 09:28 UTC)

<p>One option is that someone (or someone with the help of an LLM) adds a parameter in the effect for the resolution of the tube.</p>
<p>The other option is that you open the python file in your installed extension and simply change this number. It is a hack, but since this code is Python and it is interpreted, it will work after restarting Slicer.</p>

---
