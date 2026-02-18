# Automatic segmentation and generation of .stl from large amount of tiff image stacks

**Topic ID**: 4381
**Date**: 2018-10-12
**URL**: https://discourse.slicer.org/t/automatic-segmentation-and-generation-of-stl-from-large-amount-of-tiff-image-stacks/4381

---

## Post #1 by @johan (2018-10-12 21:48 UTC)

<p>Operating system: Ubuntu Linux 18 LTS<br>
Slicer version: 4.9.0-2018-10-09 r27464</p>
<p>Hello,</p>
<p>I am currently doing the following manually using the GUI</p>
<ol>
<li>Load .tif stack, deselect labelmap and single image after clicking “show options”</li>
<li>Volumes module: deactivate interpolate</li>
<li>Crop volume module: create new volume, select input volume, fix ROI, select a region for cropping, deselect interpolated cropping and apply</li>
<li>Create 3 new segmentations based on this cropped volume with different threshold values</li>
<li>Create a closed surface with smoothing factor changed to 0.0</li>
<li>Export stl files</li>
</ol>
<p>I have a huge amount of data that i need to process in the same way, so i need to automate this process using the python interface. What i have currently is the code at <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a> (thank you lassoan!) where only the first line of code differs so far.</p>
<pre>
[success, loadedVolumeNode] = slicer.util.loadVolume(stack.tiff, returnNode=True)

## Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(loadedVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("pores")

## Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(loadedVolumeNode)

## Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","100")
effect.setParameter("MaximumThreshold","100")
effect.self().onApply()

## Clean up
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

## Make segmentation results visible in 3D
segmentationNode.CreateClosedSurfaceRepresentation()

## Make sure surface mesh cells are consistently oriented
surfaceMesh = segmentationNode.GetClosedSurfaceRepresentation(addedSegmentID)
normals = vtk.vtkPolyDataNormals()
normals.AutoOrientNormalsOn()
normals.ConsistencyOn()
normals.SetInputData(surfaceMesh)
normals.Update()
surfaceMesh = normals.GetOutput()

## Write to STL file
writer = vtk.vtkSTLWriter()
writer.SetInputData(surfaceMesh)
writer.SetFileName("something.stl")
writer.Update()
</pre>
<p>This extracts a .stl file, which i cannot open. It looks like nothing is selected in the segmentation step, which i think is related to the labelmap during import of data.</p>
<p>So my question is, is there any documentation resource where i can find the necessary function calls and properties for this, or has someone else done anything similar? I am very grateful for any pointers in the right direction!</p>
<p>Best regards,<br>
Johan</p>

---

## Post #2 by @lassoan (2018-10-12 22:45 UTC)

<p>Tiff files are not well suited for 3D image storage.  You can still use them but you need to do extra steps:</p>
<ul>
<li>Make sure you have a grayscale (single-component scalar) image and not an RGB image. Use Vector to Scalar Volume module to convert RGB image to grayscale.</li>
<li>Set correct image spacing. Spacing within the slice may be correct already (image DPI can be stored in Tiff header), but spacing between slices is most probably incorrect. Use SetSpacing method of the volume node to adjust spacing.</li>
</ul>

---

## Post #3 by @johan (2018-10-13 05:37 UTC)

<p>Thank you for your reply!</p>
<p>The tiff files are pre-processed (converted to grayscale and segmented using opencv2 and numpy) before i load them into slicer. But it seems that slicer might try to treat them anyway as RGB if i dont manually uncheck “labelmap”. This is why i would want to find documentation for the loadVolume method in slicer.util.</p>
<p>Regarding the spacing, i do not set it when doing the procedure manually and the resulting .stl seems OK. The lenght scale is off, however the relative dimensions between pixels and layers are correct so i can live with that. I will anyway check the SetSpacing method!</p>
<p>Let me clarify my problem again; i need to do all operations using the python interface, as the dataset is <em>huge</em>. The data is from multiple metal cylinders which has been molten, and ct-scanned while solidifying in a synchrotron (500 stacks of 2000x2000x2000 pixels and layers)</p>

---

## Post #4 by @jcfr (2018-10-13 10:28 UTC)

<aside class="quote no-group" data-username="johan" data-post="3" data-topic="4381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan/48/2275_2.png" class="avatar"> johan:</div>
<blockquote>
<p>This is why i would want to find documentation for the loadVolume method in slicer.util</p>
</blockquote>
</aside>
<p>Passing <code>labelmap=0</code> doing <code>slicer.loadVolume("/path/to/volume", properties={'labelmap':0})</code></p>
<p>See <a href="https://github.com/Slicer/Slicer/blob/4aba9eba8c23de28b4ee52a9c682609c728bdbc9/Base/Python/slicer/util.py#L400-L410">https://github.com/Slicer/Slicer/blob/4aba9eba8c23de28b4ee52a9c682609c728bdbc9/Base/Python/slicer/util.py#L400-L410</a></p>
<p>Setting <code>returnNode=True</code> will also return the node that you can than transform using the Vector to Scalar Volume module discussed by <a class="mention" href="/u/lassoan">@lassoan</a> . The <code>VectorToScalarVolumeLogic</code> recently added by <a class="mention" href="/u/phcerdan">@phcerdan</a> should be helpful.</p>
<aside class="quote no-group" data-username="johan" data-post="3" data-topic="4381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan/48/2275_2.png" class="avatar"> johan:</div>
<blockquote>
<p>The data is from multiple metal cylinders which has been molten, and ct-scanned while solidifying in a synchrotron (500 stacks of 2000x2000x2000 pixels and layers)</p>
</blockquote>
</aside>
<p>There are two approaches:</p>
<p>(1) From a shell (or python) script, call Slicer 500 times passing an other python script able to process one stack</p>
<p>(2) Do processing of all stack within Slicer, for this to work you will have to make sure to unload the previous stack before processing the next one</p>

---

## Post #5 by @lassoan (2018-10-13 14:36 UTC)

<aside class="quote no-group" data-username="johan" data-post="3" data-topic="4381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan/48/2275_2.png" class="avatar"> johan:</div>
<blockquote>
<p>segmented using opencv2</p>
</blockquote>
</aside>
<p>How do you segment using opencv2? Do you use 3D processing algorithms or apply 2D methods slice by slice?</p>

---
