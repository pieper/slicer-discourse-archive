# Extract pixel values from reformatted red slice

**Topic ID**: 29004
**Date**: 2023-04-19
**URL**: https://discourse.slicer.org/t/extract-pixel-values-from-reformatted-red-slice/29004

---

## Post #1 by @bserrano (2023-04-19 10:40 UTC)

<p>Hi,</p>
<p>We want to extract pixel values from reformatted red slice to obtain a perpendicular view. To do that, we use endoscopy module in the following way:</p>
<pre><code class="lang-auto">    # Get curve info 
    curveNode = slicer.util.getNode(curveName)
    pointsCurve = vtk.util.numpy_support.vtk_to_numpy(curveNode.GetCurve().GetPoints().GetData())
    modelNode = slicer.util.getNode("model_" + curveName)

    # Set endoscopy params
    pointsEndoscopy = slicer.util.arrayFromModelPoints(modelNode)    
    endoscopyGUI = slicer.modules.endoscopy.widgetRepresentation().self()
    endoscopyGUI.flyTo(0)
   
    # Storage vectors
    volumeNodes_slices = []
    voxels_slices = []
    curvePoints = []

    for index in range(0, len(pointsEndoscopy)-1): 
        
        sliceNodeID = "vtkMRMLSliceNodeRed"
        
        # Get image data from slice view
        sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
        appLogic = slicer.app.applicationLogic()
        sliceLogic = appLogic.GetSliceLogic(sliceNode)
        sliceLayerLogic = sliceLogic.GetBackgroundLayer()
        reslice = sliceLayerLogic.GetReslice()
        reslicedImage = vtk.vtkImageData()
        reslicedImage.DeepCopy(reslice.GetOutput())
        
        # Create new volume node using resliced image
        volumeNodeResliced = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
        volumeNodeResliced.SetIJKToRASMatrix(sliceNode.GetXYToRAS())
        volumeNodeResliced.SetAndObserveImageData(reslicedImage)
        volumeNodeResliced.CreateDefaultDisplayNodes()
        volumeNodeResliced.CreateDefaultStorageNode()
        
        volumeNodes_slices.append(volumeNodeResliced)
        
        # Get voxels as a numpy array
        voxels = slicer.util.arrayFromVolume(volumeNodeResliced)
        voxels_slices.append(voxels)

        # Save voxels as .npy

</code></pre>
<p>The problem is that pixel values in .npy file do not match with the values in slicer.<br>
For example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d166f90fdb14f4d149d6549a66be4e2be92a841.png" data-download-href="/uploads/short-url/aZWPGOerbMyH5V2ri1giuke4Csx.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d166f90fdb14f4d149d6549a66be4e2be92a841.png" alt="imagen" data-base62-sha1="aZWPGOerbMyH5V2ri1giuke4Csx" width="355" height="375" data-dominant-color="838EA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">494×521 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d13e230bec44c7fe52c09f9af139c1ba3315da29.png" alt="imagen" data-base62-sha1="tR2UYI65QpWnSZ096wkRDN0bkNP" width="282" height="254"></p>
<p>Left: .npy file → HU = 470 in vessel center<br>
Right: red slice → HU = 419 in vessel center</p>

---

## Post #2 by @lassoan (2023-04-20 04:31 UTC)

<p>If you computed the coordinates correctly then probably the difference is due to interpolation. You can use nearest neighbor instead of interpolation if you want to see exactly matching values.</p>
<p>However, if you want to extract orthogonal slices along a curve then you don’t need to implement any new computations. Instead, you can use Curved Planar Reformat module in the Sandbox extension. It gives you all the reformatted slices conveniently in a 3D array.</p>

---

## Post #3 by @bserrano (2023-04-20 07:07 UTC)

<p>Yes, it was due to interpolation.</p>
<p>However, we have observed another strange behaviour. The images saved as .npy with name “index” correspond to a flyTo(index+1) of the endoscopy module and we don’t know why there is no index correspondence (see code in the previous post).</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2023-04-20 11:45 UTC)

<p>Rendering pipeline update is limited by the screen refresh rate, while data may be modified thousands of times per second. If you capture data from the rendering pipeline then make sure you call <code>slicer.util.forceRenderAllViews()</code> before. The rendering pipeline is not intended for acquiring data for quantitative analysis, as it is optimized for visualization. Currently, there are not significant limitations (other than lower refresh rate and image resolution and field of view limited to display resolution at later stages of the pipeline, and your data potentially impacted by user’s visualization choices such as interpolation/nearest neighbor), but in the future we may implement features like dynamically lowering of rendering resolution when visualizing very large data sets, etc.</p>
<p>Reslicing/resampling the original image is a more robust way of extracting pixel values from reformatted slices. The non-linear transform based method that <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/CurvedPlanarReformat/CurvedPlanarReformat.py">Curved Planar Reformat</a> module uses is particularly powerful because it allows transforming any nodes between the world coordinate system and the straightened coordinate system.</p>

---
