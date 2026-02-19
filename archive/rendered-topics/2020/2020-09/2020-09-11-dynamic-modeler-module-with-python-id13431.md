---
topic_id: 13431
title: "Dynamic Modeler Module With Python"
date: 2020-09-11
url: https://discourse.slicer.org/t/13431
---

# Dynamic Modeler Module with python?

**Topic ID**: 13431
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/dynamic-modeler-module-with-python/13431

---

## Post #1 by @apparrilla (2020-09-11 00:52 UTC)

<p>Slicer: 4.11.0-2020-07-04 r29204 Win10</p>
<p>I want to use Dynamic Modeler Module Plane Cut tool (and others) with python. Is there any documentation published?</p>
<p>Thanks.</p>

---

## Post #2 by @Sunderlandkyl (2020-09-11 14:54 UTC)

<p>No documentation pages have been published yet, although one should probably be created.</p>
<p>You can display all of the input node references for a tool using the following:</p>
<pre><code class="lang-auto">planeCutTool = slicer.vtkSlicerDynamicModelerPlaneCutTool()
for i in range(planeCutTool.GetNumberOfInputNodes()):
  print(planeCutTool.GetNthInputNodeReferenceRole(i))
</code></pre>
<p>The node references can be used to create a dynamic modeler node:</p>
<pre><code class="lang-auto">dynamicModelerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLDynamicModelerNode")
dynamicModelerNode.SetToolName("Plane cut")
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputModel", inputmodelNode.GetID())
dynamicModelerNode.SetNodeReferenceID("PlaneCut.InputPlane", inputPlaneNode.GetID())
dynamicModelerNode.SetNodeReferenceID("PlaneCut.OutputPositiveModel", outputModel.GetID())
slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(dynamicModelerNode)
</code></pre>

---

## Post #3 by @apparrilla (2020-09-18 18:38 UTC)

<p>Thanks so much <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>.<br>
Just a bit more info:</p>
<ul>
<li>I need to add more than one InputPlane</li>
<li>I should like to look around with Parameters (Operation Type)</li>
</ul>
<p>Thanks on advance!</p>

---

## Post #4 by @Sunderlandkyl (2020-09-18 19:34 UTC)

<p>Sure, then you can use:</p>
<ul>
<li>AddNodeReferenceID instead of SetNodeReferenceID for the plane node</li>
<li>SetAttribute(“OperationType”, type), where type is “Union”, “Intersection”, or “Difference”.</li>
</ul>

---

## Post #5 by @apparrilla (2020-09-19 00:10 UTC)

<p>It works like a charm, wonderfull.<br>
Thanks</p>

---

## Post #6 by @lassoan (2020-09-19 15:18 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you add these to the documentation in header files? Thank you!</p>

---

## Post #7 by @tpereira (2021-07-02 17:20 UTC)

<p>This has been very helpful, but if I wanted to create a new model for the output is there a way I could do that. Or a way to create an empty model I could output too.</p>

---

## Post #8 by @lassoan (2021-07-09 04:27 UTC)

<p>You can create a new model node as any other node (<code>slicer.mrmlScene.AddNewNodeByClass</code>). See a complete example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-hollow-model-from-boundary-of-solid-segment">here</a>.</p>

---

## Post #9 by @lassoan (2022-10-31 19:23 UTC)

<p>A post was split to a new topic: <a href="/t/show-hide-output-model-in-python-script/25988">Show/hide output model in Python script</a></p>

---

## Post #10 by @dimitris (2025-04-09 18:03 UTC)

<p>Hi,</p>
<p>I am a new member.<br>
Following your code in the case of curve cut tool I get:<br>
CurveCut.InputModel<br>
CurveCut.InputCurve<br>
CurveCut.InsidePoint</p>
<p>But then, if i try to implement an analogous code (eg in a case of sphere with a closed curve resampled and constrained)<br>
I get the error: ‘[VTK] Output node missing!’<br>
Does this error indicate that’ plane cut’ example is not applicable in a ‘curve cut’ case or am I doing something wrong?<br>
Here is the code I use:</p>
<p>inputModel = slicer.util.getNode(‘SphereModel’)<br>
inputCurve = slicer.util.getNode(‘CC’)<br>
insidePoint = slicer.util.getNode(‘F’)</p>
<p>outputPositive = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”, “CutModel_Positive”)<br>
outputPositive.CreateDefaultDisplayNodes()<br>
outputNegative = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”, “CutModel_Negative”)<br>
outputNegative.CreateDefaultDisplayNodes()</p>
<p>dynamicModelerNode  = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLDynamicModelerNode”)<br>
dynamicModelerNode.SetToolName(“Curve cut”)<br>
dynamicModelerNode.SetNodeReferenceID(“CurveCut.InputModel”, inputModel.GetID())<br>
dynamicModelerNode.SetNodeReferenceID(“CurveCut.InputCurve”, inputCurve.GetID())<br>
dynamicModelerNode.SetNodeReferenceID(“CurveCut.InsidePoint”, insidePoint.GetID())<br>
dynamicModelerNode.SetNodeReferenceID(“CurveCut.OutputPositiveModel”, outputPositive.GetID())<br>
dynamicModelerNode.SetNodeReferenceID(“CurveCut.OutputNegativeModel”, outputNegative.GetID())</p>
<p>dynamicModelerNode.SetAttribute(“StraightCut”, “true”)<br>
dynamicModelerNode.SetAttribute(“Operation”,  “Split”)<br>
dynamicModelerNode.SetAttribute(“InsideSurface”, “true”)<br>
dynamicModelerNode.SetAttribute(“OutsideSurface”, “true”)</p>
<p>slicer.modules.dynamicmodeler.logic().RunDynamicModelerTool(dynamicModelerNode)</p>
<p>Thanks in advance!</p>

---
