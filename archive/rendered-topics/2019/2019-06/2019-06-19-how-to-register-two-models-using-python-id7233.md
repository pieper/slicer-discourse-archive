---
topic_id: 7233
title: "How To Register Two Models Using Python"
date: 2019-06-19
url: https://discourse.slicer.org/t/7233
---

# How to register two models using Python?

**Topic ID**: 7233
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/how-to-register-two-models-using-python/7233

---

## Post #1 by @timeanddoctor (2019-06-19 10:41 UTC)

<p>I went to calculater a transform between two models.<br>
Then I searched and found such module :<a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/ModelRegistration/ModelRegistration.py" rel="nofollow noopener">https://github.com/SlicerIGT/SlicerIGT/blob/master/ModelRegistration/ModelRegistration.py</a></p>
<p>but when I run this code in python cli, I get an error just like the post title.</p>
<pre><code class="lang-auto">def MR(inputSourceModel, inputTargetModel, outputSourceToTargetTransform, transformType=0, numIterations=100 ):    
    
  delayDisplay('Running iterative closest point registration')
  
  icpTransform = vtk.vtkIterativeClosestPointTransform()
  icpTransform.SetSource(inputSourceModel.GetPolyData() )
  icpTransform.SetTarget(inputTargetModel.GetPolyData() )
  icpTransform.GetLandmarkTransform().SetModeToRigidBody()
  if transformType == 1:
    icpTransform.GetLandmarkTransform().SetModeToSimilarity()
  if transformType == 2:
    icpTransform.GetLandmarkTransform().SetModeToAffine()
  icpTransform.SetMaximumNumberOfIterations( numIterations )
  icpTransform.Modified()
  icpTransform.Update()
  
  outputSourceToTargetTransform.SetAndObserveMatrixTransformToParent(vtk.vtkMatrix4x4())
          
  if slicer.app.majorVersion &gt;= 5 or (slicer.app.majorVersion &gt;= 4 and slicer.app.minorVersion &gt;= 11):
    outputSourceToTargetTransform.AddNodeReferenceID(slicer.vtkMRMLTransformNode.GetMovingNodeReferenceRole(), inputSourceModel.GetID())
    outputSourceToTargetTransform.AddNodeReferenceID(slicer.vtkMRMLTransformNode.GetFixedNodeReferenceRole(), inputTargetModel.GetID())
  
  return True


inputSourceModel = getNode("a")
inputTargetModel = getNode("b")
 
MR(inputSourceModel, inputTargetModel, "aTob", transformType=0, numIterations=100)
</code></pre>
<p>If I went to calculate a transform between two models, and which code is right?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2019-06-19 15:51 UTC)

<p>A transform node was expected and you passed a string instead. You don’t need to copy-paste code from modules but you can use module logic from another module or from the Python console. For example, this should do everything you need:</p>
<pre><code class="lang-python"># Get input and output nodes
sourceModel = getNode('Segment_1')
targetModel = getNode('Segment_2')
sourceToTargetTransform = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode")

# Register
import ModelRegistration
mrLogic = ModelRegistration.ModelRegistrationLogic()
mrLogic.run(sourceModel, targetModel, sourceToTargetTransform)

# Show results
sourceModel.SetAndObserveTransformNodeID(sourceToTargetTransform.GetID())
sourceModel.GetDisplayNode().SetOpacity(0.5)
targetModel.GetDisplayNode().SetOpacity(0.5)
</code></pre>
<p>If you need non-linear (warping) registration of nodes then you can use SegmentRegistration extension.</p>

---
