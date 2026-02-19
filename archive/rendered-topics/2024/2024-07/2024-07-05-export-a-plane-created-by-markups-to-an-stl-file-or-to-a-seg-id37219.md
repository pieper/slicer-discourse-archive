---
topic_id: 37219
title: "Export A Plane Created By Markups To An Stl File Or To A Seg"
date: 2024-07-05
url: https://discourse.slicer.org/t/37219
---

# Export a plane created by Markups to an .stl file  or to a segment

**Topic ID**: 37219
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/export-a-plane-created-by-markups-to-an-stl-file-or-to-a-segment/37219

---

## Post #1 by @Piya (2024-07-05 17:00 UTC)

<p>Operating system: Windows 11 Home<br>
Slicer version: 5.6.2<br>
Expected behavior: I would like to export a plane created by Markups to an .stl file.<br>
Actual behavior: No option for an .stl file (only .json)</p>

---

## Post #2 by @muratmaga (2024-07-05 17:02 UTC)

<p>Please provide more information about what you are trying to do? Without that all I can say, try <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel" class="inline-onebox">GitHub - SlicerIGT/SlicerMarkupsToModel: 3D Slicer extension to create tube or closed surface model from markup fiducials</a></p>

---

## Post #3 by @lassoan (2024-07-05 17:25 UTC)

<p>You can export plane to markup to model using OpenAnatomy extension. It writes the result to OBJ or glTF file.</p>
<p>If you want to save as STL then you can export the plane to a model by using this code snippet:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/blob/16750d1e72c27c69c86bbc6193951d764642b0e0/OpenAnatomyExport/OpenAnatomyExport.py#L553-L573">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/16750d1e72c27c69c86bbc6193951d764642b0e0/OpenAnatomyExport/OpenAnatomyExport.py#L553-L573" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/16750d1e72c27c69c86bbc6193951d764642b0e0/OpenAnatomyExport/OpenAnatomyExport.py#L553-L573" target="_blank" rel="noopener">PerkLab/SlicerOpenAnatomy/blob/16750d1e72c27c69c86bbc6193951d764642b0e0/OpenAnatomyExport/OpenAnatomyExport.py#L553-L573</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="553" style="counter-reset: li-counter 552 ;">
          <li>def createPlaneModelFromMarkupsPlane(self,planeMarkup):</li>
          <li>  planeBounds = planeMarkup.GetPlaneBounds()</li>
          <li>  objectToWorld = vtk.vtkMatrix4x4()</li>
          <li>  planeMarkup.GetObjectToWorldMatrix(objectToWorld)</li>
          <li></li>
          <li>  # Create plane polydata</li>
          <li>  planeSource = vtk.vtkPlaneSource()</li>
          <li>  planeSource.SetOrigin(objectToWorld.MultiplyPoint([planeBounds[0], planeBounds[2], 0.0, 1.0])[0:3])</li>
          <li>  planeSource.SetPoint1(objectToWorld.MultiplyPoint([planeBounds[1], planeBounds[2], 0.0, 1.0])[0:3])</li>
          <li>  planeSource.SetPoint2(objectToWorld.MultiplyPoint([planeBounds[0], planeBounds[3], 0.0, 1.0])[0:3])</li>
          <li>  planeModel = slicer.modules.models.logic().AddModel(planeSource.GetOutputPort())</li>
          <li></li>
          <li>  # Copy props from markups to model</li>
          <li>  planeMarkupDisplayNode = planeMarkup.GetDisplayNode()</li>
          <li>  planeModelDisplayNode = planeModel.GetDisplayNode()</li>
          <li>  planeModelDisplayNode.SetColor(planeMarkupDisplayNode.GetSelectedColor())</li>
          <li>  planeOpacity = planeMarkupDisplayNode.GetFillOpacity()</li>
          <li>  planeModelDisplayNode.SetOpacity(planeOpacity)</li>
          <li>  planeModel.SetName(planeMarkup.GetName())</li>
          <li></li>
          <li>  return planeModel</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Piya (2024-07-06 00:37 UTC)

<p>I’d like to plan an ostetomy cutting plane and save it as an.stl file to submit to an engineer to create a cutting guide. Thank you very much for your information. I tried the MarkupsToModel extension but did not receive a model automatically. This means I need to first create a closed surface with fiducial points prior to getting a model, correct?</p>

---

## Post #5 by @Piya (2024-07-06 00:44 UTC)

<p>Thank you very much. I tried the OpenAnatomy extension. It appears straightforward, however I’m not sure why the export button is greyed out as seen in the picture.<br>
How can I apply the code snippet to 3dSlicer to get an STL file? I’ve never used it before.<br>
Thank you very much again for your help.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/243cbbf0bffc7b46ac0c266dea674a5fbf056650.png" data-download-href="/uploads/short-url/5azjioeHxRdVEcDIT8Tyce274FG.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/243cbbf0bffc7b46ac0c266dea674a5fbf056650_2_689x411.png" alt="Picture1" data-base62-sha1="5azjioeHxRdVEcDIT8Tyce274FG" width="689" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/243cbbf0bffc7b46ac0c266dea674a5fbf056650_2_689x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/243cbbf0bffc7b46ac0c266dea674a5fbf056650_2_1033x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/243cbbf0bffc7b46ac0c266dea674a5fbf056650.png 2x" data-dominant-color="C0BFD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">1206×720 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-07-06 01:31 UTC)

<p>You can use <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">BoneReconstructionPlanner extension</a> to fully automatically generate cutting guides for osteotomy directly in Slicern without a need to involve an engineer (or hugely simplify the work of an engineer).</p>
<p>The module is currently generates cutting guides for mandibular fibula flap reconstruction but it should not be hard to modify it to simpler procedures. <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> may be able to help.</p>

---

## Post #7 by @mau_igna_06 (2024-07-09 19:23 UTC)

<p>Hi</p>
<p>Thanks for the pin <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p><a class="mention" href="/u/piya">@Piya</a>, your workflow is indeed possible:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df88b9128e2946c0dbeebcc93e6101bb109bbcfa.jpeg" data-download-href="/uploads/short-url/vTtp0T3bJ8goTo8TtgoggMxIr3A.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df88b9128e2946c0dbeebcc93e6101bb109bbcfa_2_690x389.jpeg" alt="image" data-base62-sha1="vTtp0T3bJ8goTo8TtgoggMxIr3A" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df88b9128e2946c0dbeebcc93e6101bb109bbcfa_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df88b9128e2946c0dbeebcc93e6101bb109bbcfa_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df88b9128e2946c0dbeebcc93e6101bb109bbcfa_2_1380x778.jpeg 2x" data-dominant-color="A7ACB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1083 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please check the link below to implement this kind of resections:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/db73104d134b7cae44f303d5e7fcb6d209edcb9c/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2610">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/db73104d134b7cae44f303d5e7fcb6d209edcb9c/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2610" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/db73104d134b7cae44f303d5e7fcb6d209edcb9c/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2610" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/db73104d134b7cae44f303d5e7fcb6d209edcb9c/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2610</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="2600" style="counter-reset: li-counter 2599 ;">
          <li>    vtk.vtkMath.Cross(fibulaZ, anteriorDirection, fibulaX)
</li>
          <li>    fibulaX = fibulaX/np.linalg.norm(fibulaX)
</li>
          <li>  else:
</li>
          <li>    vtk.vtkMath.Cross(fibulaZ, posteriorDirection, fibulaX)
</li>
          <li>    fibulaX = fibulaX/np.linalg.norm(fibulaX)
</li>
          <li>  vtk.vtkMath.Cross(fibulaZ, fibulaX, fibulaY)
</li>
          <li>  fibulaY = fibulaY/np.linalg.norm(fibulaY)
</li>
          <li>
</li>
          <li>  return fibulaX, fibulaY, fibulaZ, fibulaOrigin
</li>
          <li>
</li>
          <li class="selected">def createMiterBoxesFromFibulaPlanes(self):
</li>
          <li>  parameterNode = self.getParameterNode()
</li>
          <li>  fibulaLine = parameterNode.GetNodeReference("fibulaLine")
</li>
          <li>  miterBoxDirectionLine = parameterNode.GetNodeReference("miterBoxDirectionLine")
</li>
          <li>  miterBoxSlotWidth = float(parameterNode.GetParameter("miterBoxSlotWidth"))
</li>
          <li>  miterBoxSlotLength = float(parameterNode.GetParameter("miterBoxSlotLength"))
</li>
          <li>  miterBoxSlotHeight = float(parameterNode.GetParameter("miterBoxSlotHeight"))
</li>
          <li>  miterBoxSlotWall = float(parameterNode.GetParameter("miterBoxSlotWall"))
</li>
          <li>  clearanceFitPrintingTolerance = float(parameterNode.GetParameter("clearanceFitPrintingTolerance"))
</li>
          <li>  biggerMiterBoxDistanceToFibula = float(parameterNode.GetParameter("biggerMiterBoxDistanceToFibula"))
</li>
          <li>  securityMarginOfFibulaPieces = float(parameterNode.GetParameter("securityMarginOfFibulaPieces"))
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This way you’d have the 3D boxes you can deliver to the engineer to create your guides.</p>
<p>I’d suggest you just do all the workflow inside Slicer to avoid friction. I can answer questions if there is intent to publish the code publicly</p>
<p>HIH,<br>
Mauro</p>

---

## Post #8 by @Piya (2024-07-12 09:08 UTC)

<p>Dear Mauro,   <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
Thank you for replying. Sorry for the delay in responding; I am still learning how to use the codes you provided. However, I must admit that I am unsure how to utilize or enter that code into the 3dSlicer. But I’ll try to learn more about this. Now I’m attempting to generate a rectangle and transform it to match the created plane; it works, but it’s not very precise.<br>
Best,<br>
Piya</p>

---

## Post #9 by @Piya (2024-07-28 01:34 UTC)

<p>Finally, I created .stl files for cutting planes by using</p>
<ol>
<li>IGT–&gt; create model: then create a cube object using a dimension measured from the created plane</li>
<li>IGT → Fusidal registration wizard: to move the created plane object to the mark-up plane<br>
In these ways, I can make models and export them as .stl files.</li>
</ol>

---
