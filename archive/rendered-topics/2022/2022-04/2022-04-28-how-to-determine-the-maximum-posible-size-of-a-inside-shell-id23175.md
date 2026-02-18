# How to determine the maximum posible size of a inside shell before extruding the external surface?

**Topic ID**: 23175
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/how-to-determine-the-maximum-posible-size-of-a-inside-shell-before-extruding-the-external-surface/23175

---

## Post #1 by @Ricardo_Vega (2022-04-28 16:46 UTC)

<p>Hello,<br>
I need to make some measurements for bone tunnels.<br>
Right now we are exporting a bone model to meshmixer, then we create a cilindre aligned on a defined axis inside the bone. We then manually increase the diameter until it extrudes the surface of the bone model.</p>
<p>I wanted to ask for some tips to make this process a little more automated. We need to measure 60 models and each with the cilindres at different angles.</p>
<p>Thank you.<br>
Ricardo Vega</p>

---

## Post #2 by @mau_igna_06 (2022-04-29 17:48 UTC)

<p>Im my opinion this can be automated.</p>
<p>First you need to get the anatomical axis of the long bone. Look at this code to get an idea of something you could improve:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/699c9970f163a14c7289dd8c8a7aa8b7346969d3/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3042">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/699c9970f163a14c7289dd8c8a7aa8b7346969d3/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3042" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/699c9970f163a14c7289dd8c8a7aa8b7346969d3/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3042" target="_blank" rel="noopener">SlicerIGT/SlicerBoneReconstructionPlanner/blob/699c9970f163a14c7289dd8c8a7aa8b7346969d3/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3042</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="3032" style="counter-reset: li-counter 3031 ;">
            <li>    combineModelsLogic.process(surgicalGuideModel, cylindersModelsList[i], surgicalGuideModel, 'difference')
</li>
            <li>
</li>
            <li>  for i in range(len(sawBoxesModelsList)):
</li>
            <li>    combineModelsLogic.process(surgicalGuideModel, sawBoxesModelsList[i], surgicalGuideModel, 'difference')
</li>
            <li>
</li>
            <li>  if surgicalGuideModel.GetPolyData().GetNumberOfPoints() == 0:
</li>
            <li>    slicer.mrmlScene.RemoveNode(surgicalGuideModel)
</li>
            <li>    slicer.util.errorDisplay("ERROR: Boolean operations to make mandible surgical failed")
</li>
            <li>
</li>
            <li>
</li>
            <li class="selected">def centerFibulaLine(self):
</li>
            <li>  parameterNode = self.getParameterNode()
</li>
            <li>  fibulaLine = parameterNode.GetNodeReference("fibulaLine")
</li>
            <li>  fibulaModelNode = parameterNode.GetNodeReference("fibulaModelNode")
</li>
            <li>
</li>
            <li>  shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
</li>
            <li>  intersectionsFolder = shNode.CreateFolderItem(self.getParentFolderItemID(),"Intersections")
</li>
            <li>
</li>
            <li>  lineStartPos = np.zeros(3)
</li>
            <li>  lineEndPos = np.zeros(3)
</li>
            <li>  fibulaLine.GetNthControlPointPositionWorld(0, lineStartPos)
</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can see my post about finding the anatomical axis also:<br>
<a href="https://discourse.slicer.org/t/approximate-anatomical-axis-curve-of-long-bone/">https://discourse.slicer.org/t/approximate-anatomical-axis-curve-of-long-bone/</a></p>
<p>Please let me know if you achieve it</p>
<p>Hope it helps</p>
<p>Mauro</p>

---
