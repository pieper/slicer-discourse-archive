---
topic_id: 25018
title: "I Try To Replace Markups With Model In Markupstomodel But"
date: 2022-08-31
url: https://discourse.slicer.org/t/25018
---

# I try to replace `markups` with `model` in `MarkupsToModel` , but

**Topic ID**: 25018
**Date**: 2022-08-31
**URL**: https://discourse.slicer.org/t/i-try-to-replace-markups-with-model-in-markupstomodel-but/25018

---

## Post #1 by @jumbojing (2022-08-31 02:55 UTC)

<p>I try to replace <code>markups</code> with <code>model</code> in <code>MarkupsToModel</code> , but…<img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">, what’s wrong?</p>
<pre data-code-wrap="python"><code class="lang-python">def fids2Mod(fids, curve=True):
#     if isinstance(fids,str):
    fids = slicer.util.getNode(fids)

    outputModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLModelNode())
    outputModel.CreateDefaultDisplayNodes()
    outputModel.GetDisplayNode().SetSliceIntersectionVisibility(True)
    outputModel.GetDisplayNode().SetColor(1,0,0)

    markupsToModel = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsToModelNode())

    markupsToModel.SetAutoUpdateOutput(True)
    markupsToModel.SetAndObserveModelNodeID(outputModel.GetID())
    markupsToModel.SetAndObserveMarkupsNodeID(fids.GetID())
    if curve:
        markupsToModel.SetModelType(0)
        markupsToModel.SetTubeRadius(0.05)
        markupsToModel.SetTubeLoop(1)
        markupsToModel.SetCurveType(0)
</code></pre>
<pre data-code-wrap="python"><code class="lang-python"># while mn is model
fids2Mod(mn,curve=False)
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20">? got None???<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e8a2e216f7f9e21ce9082d6ff6d5414b772095.png" data-download-href="/uploads/short-url/pJniHPVrrGk7x0wdtzUweF9bsp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02e8a2e216f7f9e21ce9082d6ff6d5414b772095_2_690x397.png" alt="image" data-base62-sha1="pJniHPVrrGk7x0wdtzUweF9bsp" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02e8a2e216f7f9e21ce9082d6ff6d5414b772095_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e8a2e216f7f9e21ce9082d6ff6d5414b772095.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e8a2e216f7f9e21ce9082d6ff6d5414b772095.png 2x" data-dominant-color="EBEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">980×564 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto"># mn is model
fids2Mod(mn,curve=True)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c654b7dbb39ce01e76b1b54dce4259702e4f302b.png" data-download-href="/uploads/short-url/siw2UQCwH23HL4m9b88hZNodelB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c654b7dbb39ce01e76b1b54dce4259702e4f302b_2_690x244.png" alt="image" data-base62-sha1="siw2UQCwH23HL4m9b88hZNodelB" width="690" height="244" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c654b7dbb39ce01e76b1b54dce4259702e4f302b_2_690x244.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c654b7dbb39ce01e76b1b54dce4259702e4f302b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c654b7dbb39ce01e76b1b54dce4259702e4f302b.png 2x" data-dominant-color="DBDBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">755×268 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jumbojing (2022-08-31 03:03 UTC)

<pre data-code-wrap="python"><code class="lang-python"># fids is markups
fids2Mod(f"{mn}s",curve=False)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32b6edd49fa678e7edc947c8ed4a5936a6fd1b7f.png" data-download-href="/uploads/short-url/7eDNqfIGkul52nUc2BoYuVazei3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b6edd49fa678e7edc947c8ed4a5936a6fd1b7f_2_690x215.png" alt="image" data-base62-sha1="7eDNqfIGkul52nUc2BoYuVazei3" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b6edd49fa678e7edc947c8ed4a5936a6fd1b7f_2_690x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b6edd49fa678e7edc947c8ed4a5936a6fd1b7f_2_1035x322.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b6edd49fa678e7edc947c8ed4a5936a6fd1b7f_2_1380x430.png 2x" data-dominant-color="EBD8DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1470×460 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2022-08-31 03:34 UTC)

<p>Regardless of input node type (markups fiducial or model node), you’ll get the same output model for the same input points. If you get empty results for model node input then most likely the input model node points are not set correctly. If you provide example data (saved as a .mrb file, uploaded to dropbox/onedrive) and the code snippet that you expect to work after loading that scene, then I can have a closer look.</p>

---

## Post #4 by @jumbojing (2022-08-31 16:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a href="https://drive.google.com/file/d/1GbFIoHrlZdyE1hQu2vRvfJqFtaB2j-Cm/view?usp=sharing" rel="noopener nofollow ugc">theFile</a></p>

---

## Post #5 by @lassoan (2022-09-03 03:17 UTC)

<p>Everything works well for me, I just had to delete the extra points (for example, in <code>3_xPMods</code> keep only 31 to 61). If you are reconstructing a tool trajectory path then I would recommend to only start recording when you start pulling back the tool.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ea50c3885556cdbe728271abad04f946dc1808f.png" data-download-href="/uploads/short-url/dvguIcgfYkeNX3ZiiRS7F0gSd5l.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ea50c3885556cdbe728271abad04f946dc1808f_2_561x500.png" alt="image" data-base62-sha1="dvguIcgfYkeNX3ZiiRS7F0gSd5l" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ea50c3885556cdbe728271abad04f946dc1808f_2_561x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ea50c3885556cdbe728271abad04f946dc1808f_2_841x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ea50c3885556cdbe728271abad04f946dc1808f_2_1122x1000.png 2x" data-dominant-color="9C9CD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1250×1114 78.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I copy the point coordinates into a model then “Markups to model” module creates the exact same tube from that.</p>
<pre data-code-wrap="python"><code class="lang-python">markupsPoints = getNode('3_xPMods')

# Get point coordinates as numpy array
coords = arrayFromMarkupsControlPoints(markupsPoints)

# Create new model node and allocate points
modelNode=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
pts = vtk.vtkPoints()
pts.SetNumberOfPoints(len(coords))
pd = vtk.vtkPolyData()
pd.SetPoints(pts)
modelNode.SetAndObservePolyData(pd)

# Copy point coordinates from markup to model
outCoords = arrayFromModelPoints(modelNode)
outCoords[:] = coords
</code></pre>
<p>Closed surface reconstruction worked well, too:</p>
<pre data-code-wrap="python"><code class="lang-python">outputModel = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
outputModel.CreateDefaultDisplayNodes()
outputModel.GetDisplayNode().SetSliceIntersectionVisibility(True)
outputModel.GetDisplayNode().SetColor(1,0,0)

markupsToModel = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsToModelNode")
markupsToModel.SetAndObserveInputNodeID(fids.GetID())
markupsToModel.SetAndObserveOutputModelNodeID(outputModel.GetID())
slicer.modules.markupstomodel.logic().UpdateOutputModel(markupsToModel)
</code></pre>
<p>If you want to reconstruct an open surface then the simplest is to use a closed curve:</p>
<pre data-code-wrap="python"><code class="lang-python"># Convert any markup node type into a closed curve node
outputCurve = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsClosedCurveNode")
outputCurve.SetCurveTypeToLinear()
updateMarkupsControlPointsFromArray(outputCurve, arrayFromMarkupsControlPoints(fids))

# Get surface area
areaMeasurement = outputCurve.GetMeasurement('area')
areaMeasurement.SetEnabled(True)
slicer.modules.models.logic().AddModel(areaMeasurement.GetMeshValue())
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50f8fe6dce8ceb3a1f2512477ba80a6e16270547.png" data-download-href="/uploads/short-url/byjFcrq0HjO77hRMEXFMJyj7Xuv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f8fe6dce8ceb3a1f2512477ba80a6e16270547_2_690x290.png" alt="image" data-base62-sha1="byjFcrq0HjO77hRMEXFMJyj7Xuv" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f8fe6dce8ceb3a1f2512477ba80a6e16270547_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50f8fe6dce8ceb3a1f2512477ba80a6e16270547_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50f8fe6dce8ceb3a1f2512477ba80a6e16270547.png 2x" data-dominant-color="A7A0BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1250×526 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jumbojing (2022-09-03 04:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Is there a way to sort the index of the points (np.array) according to the clockwise or counterclockwise and adjacent nearest points?</p>

---

## Post #7 by @lassoan (2022-09-03 12:23 UTC)

<p>Sorting is only available for polynomial fitting, along an approximately linear trajectory. You would need to implement sorting for a circular trajectory yourself.</p>
<p>What is your overall goal?</p>

---
