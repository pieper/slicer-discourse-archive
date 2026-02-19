---
topic_id: 9124
title: "How To Create A Clone Fiducials Then Transform The Original"
date: 2019-11-13
url: https://discourse.slicer.org/t/9124
---

# How to create a clone Fiducials then transform the original fiducials onto the clone fiducials

**Topic ID**: 9124
**Date**: 2019-11-13
**URL**: https://discourse.slicer.org/t/how-to-create-a-clone-fiducials-then-transform-the-original-fiducials-onto-the-clone-fiducials/9124

---

## Post #1 by @ihsanas (2019-11-13 06:19 UTC)

<p>Hi,</p>
<p>Using this code i created 3 markup fiducials,</p>
<pre><code>slicer.modules.markups.logic().AddFiducial(random.random()*5.0 ,random.random()*5.0,random.random()*5.0) 
</code></pre>
<p>I want to create another 3 clone fiducials close to these fiducials( same identical to original fiducials) then I want to transform my original fiducials to the clone fiducials. This is how I’m transforming using a matrix transform. This code only gets 1 markup fiducials after I name that to F, but not the randomized 3 fiducials point.</p>
<p>basically, I want is slicer.util.getNode()  will get the fiducial point I created randomly using code slicer.modules.markups.logic().AddFiducial()</p>
<pre><code>    F1 = slicer.util.getNode('F')

    transformMatrixNP = np.array(
        [[1, 0, 0, 10],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]])

    transformMatrixVTK = vtk.vtkMatrix4x4()
    for row in range(4):
        for col in range(4):
            transformMatrixVTK.SetElement(row, col, transformMatrixNP[row, col])

    F1.ApplyTransformMatrix(transformMatrixVTK)</code></pre>

---

## Post #2 by @lassoan (2019-11-14 01:49 UTC)

<p>It is not completely clear what you would like to achieve but if you use a recent Slicer Preview version then this example should help you get started:</p>
<pre><code class="lang-python">import numpy as np

pointCoordsNP = np.random.rand(5,3)*30

transformMatrixNP = np.array(
    [[1, 0, 0, 10],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]])

originalFidNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
slicer.util.updateMarkupControlPointsFromArray(originalFidNode, pointCoordsNP)

transformedFidNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
slicer.util.updateMarkupControlPointsFromArray(transformedFidNode, pointCoordsNP)
transformedFidNode.ApplyTransformMatrix(slicer.util.vtkMatrixFromArray(transformMatrixNP))
transformedControlPointsNP = slicer.util.arrayFromMarkupsControlPoints(transformedFidNode)

print(pointCoordsNP)
print(transformedControlPointsNP)
</code></pre>

---

## Post #3 by @ihsanas (2019-11-14 12:30 UTC)

<p>basically this is what I want to do, <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a24576bbe42899ed52a38ebbf0c326b30d6f4593.jpeg" data-download-href="/uploads/short-url/n9waTuMx8KToI49bb2SFVaXGCNZ.jpeg?dl=1" title="IMG_20191114_202130" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a24576bbe42899ed52a38ebbf0c326b30d6f4593_2_666x500.jpeg" alt="IMG_20191114_202130" data-base62-sha1="n9waTuMx8KToI49bb2SFVaXGCNZ" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a24576bbe42899ed52a38ebbf0c326b30d6f4593_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a24576bbe42899ed52a38ebbf0c326b30d6f4593_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a24576bbe42899ed52a38ebbf0c326b30d6f4593_2_1332x1000.jpeg 2x" data-dominant-color="A0A19E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20191114_202130</span><span class="informations">4000×3000 1.26 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-11-14 14:41 UTC)

<p>The example script does this or something very similar. If you want to compute the transform automatically then you can use Fiducial registration wizard module in SlicerIGT extension.</p>

---

## Post #5 by @ihsanas (2019-11-14 15:00 UTC)

<p>Can you help me to understand it very easily , I want to perform this manually?</p>

---

## Post #6 by @lassoan (2019-11-14 15:11 UTC)

<p>By manually do you mean using GUI or Python scripting?</p>

---

## Post #7 by @ihsanas (2019-11-14 15:17 UTC)

<p>Most probably python scripting. I’m adding python codes in the dicom python file .<br>
Right now i know how to create randomly Fiducials and Matrix transformation of that fiducials.</p>
<p>So now , i will do registration of a fiducials onto another fiducials.<br>
so , lets say ,i created  2 fiducial side by side and now i want 1 of the fiducial to be transformed onto another fiducial. can u please explain me how should i approach this situation?</p>

---

## Post #8 by @lassoan (2019-11-14 15:23 UTC)

<p>This sounds like basic landmark registration. See <a href="http://www.slicerigt.org/wp/user-tutorial/">U-12 SlicerIGT tutorial</a> for step-by-step instructions.</p>

---

## Post #9 by @ihsanas (2019-11-14 15:34 UTC)

<p>Thanks for your reply but i was looking for how to do that by coding.</p>

---

## Post #10 by @lassoan (2019-11-14 15:44 UTC)

<p>To perform landmark registration from Python, add a <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/MRML/vtkMRMLFiducialRegistrationWizardNode.h">vtkMRMLFiducialRegistrationWizardNode</a> node to the scene, set input markup fiducial nodes (<code>SetAndObserveFromFiducialListNodeId</code> and <code> SetAndObserveToFiducialListNodeId</code>), output transform node (<code>SetOutputTransformNodeId</code>), and optionally other registration parameters, then call <code>SetUpdateModeToAuto()</code> to enable computation of the output transform automatically. You can verify if you have set all parameters correctly in the Fiducial registration wizard module GUI.</p>

---

## Post #11 by @ihsanas (2019-11-14 15:56 UTC)

<p>thank you sir , another thing how to get transform between nodes?</p>

---

## Post #12 by @lassoan (2019-11-14 17:37 UTC)

<p>You can get transformation matrix between two nodes by calling <a href="https://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#acbab274893b3d11cac30c4ee8a036f96">slicer.vtkMRMLTransformNode.GetMatrixTransformBetweenNodes</a> method.</p>

---

## Post #13 by @ihsanas (2019-11-14 19:28 UTC)

<p>sir , after a create a node using this code  slicer.modules.markups.logic().AddFiducial(4.0, 7.0, 10.0) , how can i get this node or call this node to use it again?</p>

---

## Post #14 by @lassoan (2019-11-14 19:42 UTC)

<p>I’ve described <a href="https://discourse.slicer.org/t/how-to-create-a-clone-fiducials-then-transform-the-original-fiducials-onto-the-clone-fiducials/9124/10">above</a> what exact method you need to call. Transform is computed (and recomputed if any of the inputs change) automatically if UpdateMode is set to Auto.</p>

---
