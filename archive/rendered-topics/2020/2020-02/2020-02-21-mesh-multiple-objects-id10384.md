# Mesh multiple objects

**Topic ID**: 10384
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/mesh-multiple-objects/10384

---

## Post #1 by @Aep93 (2020-02-21 16:38 UTC)

<p>Hello all,<br>
I have multiple parts of an organ (which are in contact with each other) and I want to mesh them in a way that they be conformal (having same nodes on their contact region). I can generate separate meshes for each part separately but they are not conformal.<br>
I do not want to use segmentmesher because it gives me volumetric mesh and I do not want it. Can any body help me with it?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-02-21 17:04 UTC)

<p>Segment mesher is your best bet for a smooth conformal mesh that actually share node IDs. You can run the volumetric mesh through a geometry filter to keep only surface elements.</p>
<p>You can get conformal meshes from Segmentations if you disable surface smoothing before export (but the result will be non-smooth mesh) and somewhat more smooth and still mostly conformal meshes using Model Maker module.</p>

---

## Post #3 by @Aep93 (2020-02-21 17:32 UTC)

<p>Thank you very much for your response. Can you please tell me how should I convert volumetric mesh to surface through geometry filter?<br>
Thank you in advance.</p>

---

## Post #4 by @lassoan (2020-02-21 20:08 UTC)

<p>You can copy-paste this code to the Python console to extract the surface and put it into a new mode node.</p>
<pre><code class="lang-python">volMesh=getNode('Model').GetMesh()
extractSurface=vtk.vtkGeometryFilter()
extractSurface.SetInputData(volMesh)
extractSurface.Update()
slicer.modules.models.logic().AddModel(extractSurface.GetOutput())
</code></pre>
<p>You can extract a specific material by adding vtkThreshold filter before vtkGeometryFilter.</p>

---

## Post #5 by @Aep93 (2020-02-21 21:20 UTC)

<p>Thank you very much for your response. I was able to convert it to the surface. Is there any way to just keep the parts of the shapes which are in contact. I mean now I have some surfaces which inside is empty but for a very thin tissue (Like eardrum) what I need is just a surface not a close region that I have in my model or segmentation. Thank you in advance</p>

---

## Post #6 by @lassoan (2020-02-21 23:54 UTC)

<p>With latest “curve drawing on surface” feature (to be announced next week, but already available in latest Slicer Preview Release) you can extract one side of a surface very easily:</p>
<ul>
<li>Draw a closed curve on the surface</li>
<li>Make the curve snap to surface (enable Markups module / Curve settings / Curve type → shortest distance on surface, model node → model node that you would like to cut)</li>
<li>Copy-paste this code snippet to the Python console</li>
</ul>
<pre><code class="lang-python"># Get input data
curveNode = getNode('C')
modelNode = getNode('Segment_1')
extractLargestPart = False

# Get VTK data objects from MRML nodes
curvePoints = curveNode.GetCurvePointsWorld()
meshToClip = modelNode.GetMesh()  # we should apply transform to World

# Clip model with curve
loop = vtk.vtkSelectPolyData()
loop.SetLoop(curvePoints)
loop.GenerateSelectionScalarsOn()
loop.SetInputData(meshToClip)
loop.SetSelectionModeToLargestRegion()
clip = vtk.vtkClipPolyData()
clip.InsideOutOn()
clip.SetInputConnection(loop.GetOutputPort())
clip.GenerateClippedOutputOn()
clip.Update()
clippedOutput = clip.GetOutput() if extractLargestPart else clip.GetClippedOutput()

# Remove unused points
cleaner = vtk.vtkCleanPolyData()
cleaner.SetInputData(clippedOutput)
cleaner.Update()
cleanedClippedOutput = cleaner.GetOutput()

# Save result to new node
clippedModel = slicer.modules.models.logic().AddModel(cleanedClippedOutput)
clippedModel.GetDisplayNode().SetActiveScalarName("")
clippedModel.GetDisplayNode().BackfaceCullingOff()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc5ca7f5c110a99c4e6f486259509c985a206a84.png" data-download-href="/uploads/short-url/qSkhjhs7T3UhE9xFRgZG2oMZkj2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc5ca7f5c110a99c4e6f486259509c985a206a84_2_690x419.png" alt="image" data-base62-sha1="qSkhjhs7T3UhE9xFRgZG2oMZkj2" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc5ca7f5c110a99c4e6f486259509c985a206a84_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc5ca7f5c110a99c4e6f486259509c985a206a84_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc5ca7f5c110a99c4e6f486259509c985a206a84_2_1380x838.png 2x" data-dominant-color="BEC2DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 421 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There are of course many alternative methods to edit and combine meshes - using VTK filters and/or using numpy.</p>

---

## Post #7 by @Aep93 (2020-02-29 02:54 UTC)

<p>Thank you very much for your response.</p>

---

## Post #8 by @Aep93 (2020-03-02 16:41 UTC)

<p>Hello,<br>
Should the curve have specific properties? I tried the code with some simple geometries and it worked, but when I try it with a more complex medel, it does not work. Here is my model and the fitted curve:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5066800fcfc474ec94ce3977714ba04d35de666d.jpeg" data-download-href="/uploads/short-url/btfNOekWZtKremrjafgbYuDLia1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5066800fcfc474ec94ce3977714ba04d35de666d_2_690x475.jpeg" alt="image" data-base62-sha1="btfNOekWZtKremrjafgbYuDLia1" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5066800fcfc474ec94ce3977714ba04d35de666d_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5066800fcfc474ec94ce3977714ba04d35de666d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5066800fcfc474ec94ce3977714ba04d35de666d.jpeg 2x" data-dominant-color="8490A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1011×697 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And the result I get is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e11a6a75cfd04103362662a406b1b3880feb84.png" data-download-href="/uploads/short-url/2PRlU3s48CrLqZja3IGuOo4uBWk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13e11a6a75cfd04103362662a406b1b3880feb84_2_557x500.png" alt="image" data-base62-sha1="2PRlU3s48CrLqZja3IGuOo4uBWk" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13e11a6a75cfd04103362662a406b1b3880feb84_2_557x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e11a6a75cfd04103362662a406b1b3880feb84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e11a6a75cfd04103362662a406b1b3880feb84.png 2x" data-dominant-color="9C9ED3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">777×697 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I tried to change “extractLargestPart” to true in the code but in that case, what I get is the whole model without any cut. Do you have any idea about what should I do regarding this problem?<br>
Thanks</p>

---

## Post #9 by @lassoan (2020-03-02 17:11 UTC)

<p>We experienced it, too, that vtkSelectPolyData filter was “not robust” (behavior might have been correct, but not what we expected) when there were holes or other errors in the mesh.</p>
<p>Holes can easily break selection of “one side” of the surface, because a hole connects the two sides of a surface, so you actually don’t have two separate sides of the surface anymore. This is the correct behavior, but maybe it would result in a more intuitive behavior if an option was added to the selection filter to stop at feature edges (where there is a sudden change in cell normals).</p>

---

## Post #10 by @Aep93 (2020-03-02 17:21 UTC)

<p>Thank you very much. So for now you think the best way is to smooth the model as much as possible? and is there anyway to fill the holes in an existing model or I should do the segmentation from beginning?<br>
Thanks.</p>

---

## Post #11 by @lassoan (2020-03-02 17:48 UTC)

<p>Yes, smoothing and hole filling should make the surfaces closed and manifold. You can use Segment Editor’s Smoothing effect.</p>
<p>If you don’t have a segmentation just a model (surface mesh) then you can try Surface Toolbox module’s smoothing, cleaning, hole filling functions. If they are not effective then you can import the model into a segmentation node and use Segment Editor.</p>

---

## Post #12 by @Aep93 (2020-03-02 21:03 UTC)

<p>Thank you very much for your help.</p>

---
