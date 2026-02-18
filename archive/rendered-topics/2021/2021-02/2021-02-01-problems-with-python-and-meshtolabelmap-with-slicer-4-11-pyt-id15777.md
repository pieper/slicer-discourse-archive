# Problems with Python and meshtolabelmap with Slicer 4.11 (python module worked on Slicer 4.10)

**Topic ID**: 15777
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/problems-with-python-and-meshtolabelmap-with-slicer-4-11-python-module-worked-on-slicer-4-10/15777

---

## Post #1 by @Christian_Nell (2021-02-01 18:36 UTC)

<p>I am scripting a module in 3D Slicer using python and the script worked on Slicer 4.10 but now that I’ve updated to the new version 4.11 part of the script is not working. Specifically, a part where I create a handle for a keychain and it is added to the new keychain image. Here is the part I think is not working, which is the call to meshtolabelmap. I don’t know if the new version of python is different with the function call parameters or what it is. I’ve included some surrounding code to give some insight into what is going on. The tempDirectory “saves” has the handle path but the file itself is empty. Again, this worked on Slicer 4.10 with the exact same code.</p>
<pre><code>handle = makeHandle()
handleNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', "handle")
handleNode.SetAndObservePolyData(handle)
handleNode.CreateDefaultDisplayNodes()
handleNode.CreateDefaultStorageNode()

path = slicer.util.tempDirectory("saves")
handlePath = path + "/handle.nrrd"

handleParams = {'reference' : blankVolumeNode.GetID(), 'mesh' : handleNode.GetID(), 'labelMap': handleBLM.GetID(), 'value' : 255}
process = slicer.cli.run(slicer.modules.meshtolabelmap, None, handleParams, wait_for_completion=True)
slicer.util.saveNode(handleBLM,handlePath)

############################################
############################################
# Save surfaces and then load via simpleITK
############################################
############################################


left = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(leftBLM.GetName()))
right = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(rightBLM.GetName()))
handleVol = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(handleBLM.GetName()))



############################################
############################################
# Use simpleITK to combine, smooth and fill holes
############################################
############################################

orFilter = sitk.OrImageFilter()
brain = orFilter.Execute(right,left)
or2Filter = sitk.OrImageFilter()
keychain = or2Filter.Execute(brain,handleVol)
</code></pre>
<p>I’ve added the make handle function as well just incase (even though it creates a handle and shows it in slicer).</p>
<pre><code>def makeHandle():
    fn = vtk.vtkParametricTorus()
    fn.SetRingRadius((rightBound-leftBound)/5)
    fn.SetCrossSectionRadius((rightBound-leftBound)/15)
    #vtk.FlipNormalsOn()
    source = vtk.vtkParametricFunctionSource()
    source.SetParametricFunction(fn)
    source.Update()

    trans = vtk.vtkTransform()
    trans.RotateX(90)
    trans.Translate(midline,topBound + handleShift,halfway)
    # vtk generate normals
    # communicate with SLACK
    rotate = vtk.vtkTransformPolyDataFilter()
    rotate.SetTransform(trans)
    rotate.SetInputConnection(source.GetOutputPort())
    rotate.Update()

    return rotate.GetOutput()</code></pre>

---

## Post #2 by @lassoan (2021-02-01 21:40 UTC)

<p>I would recommend to import all meshes, labelmaps, etc. into a segmentation node as segments, combine everything there, and export the results to model. You can find examples for all kinds of processing in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">script repository</a>.</p>
<p>There are many things you can do with Segment editor, such as add text (if you install SegmentEditorExtraEffects extension), do some local smoothing or other touch-up.</p>
<p>Automatic creation of brain keychain sounds cool, by the way. Can you attach a photo of a 3D-printed end result?</p>

---

## Post #3 by @Christian_Nell (2021-02-05 20:25 UTC)

<p>Sure, here you go. There is another script I made that makes nametags for the keychains and places them in a dynamically sized print scene based on how big the printer is. Here is an example of what it looks like. Also, I will try what you said and let you know how it goes. Thank you for the response!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ec9022845dcf69971ca185ab72a0b2ad45586c.jpeg" data-download-href="/uploads/short-url/n6rHOvTgMI0Ripolkv1taYSA2ja.jpeg?dl=1" title="Screen Shot 2021-02-05 at 3.25.17 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1ec9022845dcf69971ca185ab72a0b2ad45586c_2_640x500.jpeg" alt="Screen Shot 2021-02-05 at 3.25.17 PM" data-base62-sha1="n6rHOvTgMI0Ripolkv1taYSA2ja" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1ec9022845dcf69971ca185ab72a0b2ad45586c_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1ec9022845dcf69971ca185ab72a0b2ad45586c_2_960x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ec9022845dcf69971ca185ab72a0b2ad45586c.jpeg 2x" data-dominant-color="C0C0C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-05 at 3.25.17 PM</span><span class="informations">1268×990 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcd3c751205f85d7ef6a83a2ecc21a569188425c.jpeg" data-download-href="/uploads/short-url/vvwMaQZCnzVOUQ6e34pk4ja9vwE.jpeg?dl=1" title="Screen Shot 2021-02-05 at 3.25.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcd3c751205f85d7ef6a83a2ecc21a569188425c_2_640x500.jpeg" alt="Screen Shot 2021-02-05 at 3.25.29 PM" data-base62-sha1="vvwMaQZCnzVOUQ6e34pk4ja9vwE" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcd3c751205f85d7ef6a83a2ecc21a569188425c_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dcd3c751205f85d7ef6a83a2ecc21a569188425c_2_960x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcd3c751205f85d7ef6a83a2ecc21a569188425c.jpeg 2x" data-dominant-color="DFDFE3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-05 at 3.25.29 PM</span><span class="informations">1268×990 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d842034ace575c6588b39f75103eed8ec433c74.jpeg" data-download-href="/uploads/short-url/8MccDTn9Yq5ZNbm3yngrVmGt7aQ.jpeg?dl=1" title="Brain1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d842034ace575c6588b39f75103eed8ec433c74_2_567x500.jpeg" alt="Brain1" data-base62-sha1="8MccDTn9Yq5ZNbm3yngrVmGt7aQ" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d842034ace575c6588b39f75103eed8ec433c74_2_567x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d842034ace575c6588b39f75103eed8ec433c74_2_850x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d842034ace575c6588b39f75103eed8ec433c74_2_1134x1000.jpeg 2x" data-dominant-color="6C6457"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brain1</span><span class="informations">1919×1691 364 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
