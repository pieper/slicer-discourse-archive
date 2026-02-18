# How to access and manipulate segmentation node as a numpy array?

**Topic ID**: 34110
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/how-to-access-and-manipulate-segmentation-node-as-a-numpy-array/34110

---

## Post #1 by @tueboesen (2024-02-02 10:32 UTC)

<p>I have a segmentation node, which is a object of type <code>&lt;MRMLCorePython.vtkMRMLSegmentationNode(0xcf8dfe0) at 0x7f89a3712a00&gt;</code></p>
<p>So if I understand this correctly then that means it can have any number of binary segmentations attached to it.</p>
<p>From this segmentation node I can follow/tweak the procedure done in SegmentEditorEffect.py to get the following:</p>
<pre><code class="lang-auto">       segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
        visibleSegmentIds = vtk.vtkStringArray()
        segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(visibleSegmentIds)

        sourceVolumeNode = slicer.vtkMRMLScalarVolumeNode()
        slicer.mrmlScene.AddNode(sourceVolumeNode)
        sourceVolumeNode.SetAndObserveTransformNodeID(segmentationNode.GetTransformNodeID())
        slicer.vtkSlicerSegmentationsModuleLogic.CopyOrientedImageDataToVolumeNode(self.scriptedEffect.sourceVolumeImageData(), sourceVolumeNode)

        mergedLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
        slicer.mrmlScene.AddNode(mergedLabelmapNode)
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, visibleSegmentIds, mergedLabelmapNode, sourceVolumeNode)

        labelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))
        labelImage_np = sitk.GetArrayFromImage(labelImage)
</code></pre>
<p>This now allows me to extract all the binary segmentations from the segmentation node and returns them all in a single 3D numpy array, where the values of the array are either 0,1,2,… with 0 meaning there is no segmentation label for that point, 1=segment_1, 2=segment_2 as so on.</p>
<p>This was quite a few steps to get there, but so far so good. Now with the numpy array I can do my own manipulation of these segments and get a new segmentation, which I would like to then load back into the original segmentation node. But so far I have been unable to do this correctly.</p>
<p>I have looked at the documentation and I see that there are some methods called<br>
<code>slicer.util.arrayFromVolume</code> and <code>updateVolumeFromArray</code>, which gives the underlying numpy array for a volume, which would be the ideal case if I could do something similar for the segmentation, since that would allow direct manipulation of the numpy array, and then the nodes are automatically updated with this information if I understand correctly? but I guess nothing like this exist for the segmentation node?</p>
<p>So, how can I manipulate a segmentation node as a numpy array, and make sure the manipulation is also done in the segmentation node?</p>

---

## Post #2 by @tueboesen (2024-02-02 12:09 UTC)

<p>Based on a suggestion I read on this forum, I tried the following approach, where I try to insert the numpy data back into the segmentation node by:</p>
<ol>
<li>Creating a labelmapvolume</li>
<li>Set the labelmapvolume voxels to the numpy array</li>
<li>Convert labelmap to segmentation node</li>
</ol>
<p>So in total the code looks like this:</p>
<pre><code class="lang-auto">    def onApply(self):
        # Make sure the user wants to do the operation, even if the segment is not visible
        print(self.scriptedEffect.confirmCurrentSegmentVisible())
        if not self.scriptedEffect.confirmCurrentSegmentVisible():
            return
        #
        # Get list of visible segment IDs, as the effect ignores hidden segments.
        segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
        visibleSegmentIds = vtk.vtkStringArray()
        segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(visibleSegmentIds)
        if visibleSegmentIds.GetNumberOfValues() == 0:
            logging.info("Smoothing operation skipped: there are no visible segments")
            return

        # This can be a long operation - indicate it to the user
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

        # Allow users revert to this state by clicking Undo
        self.scriptedEffect.saveStateForUndo()


        # Export source image data to temporary new volume node.
        # Note: Although the original source volume node is already in the scene, we do not use it here,
        # because the source volume may have been resampled to match segmentation geometry.
        sourceVolumeNode = slicer.vtkMRMLScalarVolumeNode()
        slicer.mrmlScene.AddNode(sourceVolumeNode)
        sourceVolumeNode.SetAndObserveTransformNodeID(segmentationNode.GetTransformNodeID())
        slicer.vtkSlicerSegmentationsModuleLogic.CopyOrientedImageDataToVolumeNode(self.scriptedEffect.sourceVolumeImageData(), sourceVolumeNode)

        # Generate merged labelmap of all visible segments, as the filter expects a single labelmap with all the labels.
        mergedLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
        slicer.mrmlScene.AddNode(mergedLabelmapNode)
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, visibleSegmentIds, mergedLabelmapNode, sourceVolumeNode)

        # Read input data from Slicer into SimpleITK
        labelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))
        backgroundImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(sourceVolumeNode.GetName()))

        Image_np = sitk.GetArrayFromImage(backgroundImage)
        labelImage_np = sitk.GetArrayFromImage(labelImage)
        m = labelImage_np != 0
        m2 = np.sum(m,axis=(1,2))
        idx = np.argmax(m2)
        print(labelImage_np.shape)


        # Do the segmentation 
        labelImage_np[idx] = dummy(Image_np[idx], labelImage_np[idx])

        # Create a labelmap volume node
        mergedLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()


        # Set the labelmap volume nodes voxels to the numpy array
        slicer.util.updateVolumeFromArray(mergedLabelmapNode, labelImage_np)

        # Convert labelmap to segmentation node
        slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(mergedLabelmapNode, segmentationNode)

        # slicer.mrmlScene.RemoveNode(sourceVolumeNode)
        # slicer.mrmlScene.RemoveNode(mergedLabelmapNode)

        qt.QApplication.restoreOverrideCursor()
        return
</code></pre>
<p>This appends the segmentation nodes to the previous ones rather than replacing them (which I honestly haven’t quite figured out is what I want or not). But the big problem is that something clearly goes wrong with the geometry when these new segmentations are added. The segmentations are once again added to the wrong layer and if I look at the print output of my segmentation node I see the following:</p>
<pre><code class="lang-auto">print(segmentationNode)
vtkMRMLSegmentationNode (0xcdfb210)
  ID: vtkMRMLSegmentationNode1
  ClassName: vtkMRMLSegmentationNode
  Name: Segmentation
  Debug: false
  MTime: 283168
  Description: (none)
  SingletonTag: (none)
  HideFromEditors: false
  Selectable: true
  Selected: false
  UndoEnabled: false
  Node references:
    display [displayNodeRef]: vtkMRMLSegmentationDisplayNode1
    labelmapConversionColorTableNode [labelmapConversionColorTableNodeRef]: (none)
    referenceImageGeometryRef: vtkMRMLScalarVolumeNode1
    storage [storageNodeRef]: (none)
    transform [transformNodeRef]: (none)
  TransformNodeID: (none)
  DisplayNodeIDs[0]: vtkMRMLSegmentationDisplayNode1
  Segmentation:    Debug: Off
    Modified Time: 901287
    SourceRepresentationName:  Binary labelmap
    Number of segments: 4
    Segments:
      Segment_1:
        Name: Segment_1
        Color: (0.501961, 0.682353, 0.501961)
        NameAutoGenerated: true
        ColorAutoGenerated: true
        Debug: Off
        Modified Time: 465810
        Representations:
          Binary labelmap:
            ClassName: vtkOrientedImageData
            Origin: 0 0 0
            Spacing: 0.705556 0.705556 0.705556
            Extent: 237 1731 592 1525 5 5
            Scalar type: unsigned char
            Number of components: 1
            IJKToRASDirections:
              -1 0 0 
              0 -1 0 
              0 0 1 
        Tags:
            Segmentation.Status: inprogress
            TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^
      Segment_2:
        Name: Segment_2
        Color: (0.945098, 0.839216, 0.568627)
        NameAutoGenerated: true
        ColorAutoGenerated: true
        Debug: Off
        Modified Time: 775336
        Representations:
          Binary labelmap:
            ClassName: vtkOrientedImageData
            Origin: 0 0 0
            Spacing: 0.705556 0.705556 0.705556
            Extent: 237 1731 592 1525 5 5
            Scalar type: unsigned char
            Number of components: 1
            IJKToRASDirections:
              -1 0 0 
              0 -1 0 
              0 0 1 
        Tags:
            Segmentation.Status: inprogress
            TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^
      Label_1:
        Name: Label_1
        Color: (0.694118, 0.478431, 0.396078)
        NameAutoGenerated: true
        ColorAutoGenerated: true
        Debug: Off
        Modified Time: 900940
        Representations:
          Binary labelmap:
            ClassName: vtkOrientedImageData
            Origin: 0 0 0
            Spacing: 1 1 1
            Extent: 0 1998 0 1998 5 5
            Scalar type: short
            Number of components: 1
            IJKToRASDirections:
              1 0 0 
              0 1 0 
              0 0 1 
        Tags:
            TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^
      Label_2:
        Name: Label_2
        Color: (0.435294, 0.721569, 0.823529)
        NameAutoGenerated: true
        ColorAutoGenerated: true
        Debug: Off
        Modified Time: 901289
        Representations:
          Binary labelmap:
            ClassName: vtkOrientedImageData
            Origin: 0 0 0
            Spacing: 1 1 1
            Extent: 0 1998 0 1998 5 5
            Scalar type: short
            Number of components: 1
            IJKToRASDirections:
              1 0 0 
              0 1 0 
              0 0 1 
        Tags:
            TerminologyEntry: Segmentation category and type - 3D Slicer General Anatomy list~SCT^85756007^Tissue~SCT^85756007^Tissue~^^~Anatomic codes - DICOM master list~^^~^^
    Segment converter:
      Debug: Off
      Modified Time: 281959
      Reference Count: 1
      Registered Events: (none)
      Rules:
        Rule[0]:
          Name: Binary labelmap to closed surface
          SourceRepresentationName: Binary labelmap
          TargetRepresentationName: Closed surface
          ConversionParameters:
            Decimation factor: 0.0 [Desired reduction in the total number of polygons. Range: 0.0 (no decimation) to 1.0 (as much simplification as possible). Value of 0.8 typically reduces data set size by 80% without losing too much details.]
            Smoothing factor: 0.5 [Smoothing factor. Range: 0.0 (no smoothing) to 1.0 (strong smoothing).]
            Compute surface normals: 1 [Compute surface normals. 1 (default) = surface normals are computed. 0 = surface normals are not computed (slightly faster but produces less smooth surface display, not used if vtkSurfaceNets3D is used).]
            Conversion method: 0 [Conversion method. 0 (default) = vtkDiscreteFlyingEdges3D is used to generate closed surface.1 = vtkSurfaceNets3D (more performant than flying edges).]
            SurfaceNets smoothing: 0 [SurfaceNets smoothing. 0 (default) = Smoothing done by vtkWindowedSincPolyDataFilter1 = Smoothing done in surface nets filter.]
            Joint smoothing: 0 [Perform joint smoothing.]
          Debug: Off
          Modified Time: 281960
          Reference Count: 2
          Registered Events: (none)
        Rule[1]:
          Name: Closed surface to binary labelmap (simple image stencil)
          SourceRepresentationName: Closed surface
          TargetRepresentationName: Binary labelmap
          ConversionParameters:
            Reference image geometry: -0.7055559999999998;0;0;0;0;-0.7055559999999998;0;0;0;0;0.7055559999999998;0;0;0;0;1;0;1998;0;1998;0;9; [Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.]
            Oversampling factor: 1 [Determines the oversampling of the reference image geometry. If it's a number, then all segments are oversampled with the same value (value of 1 means no oversampling). If it has the value "A", then automatic oversampling is calculated.]
            Crop to reference image geometry: 0 [Crop the model to the extent of reference geometry. 0 (default) = created labelmap will contain the entire model. 1 = created labelmap extent will be within reference image extent.]
            Collapse labelmaps: 1 [Merge the labelmaps into as few shared labelmaps as possible 1 = created labelmaps will be shared if possible without overwriting each other.]
          Debug: Off
          Modified Time: 281962
          Reference Count: 2
          Registered Events: (none)
        Rule[2]:
          Name: Closed surface to fractional labelmap (simple image stencil)
          SourceRepresentationName: Closed surface
          TargetRepresentationName: Fractional labelmap
          ConversionParameters:
            Reference image geometry: -0.7055559999999998;0;0;0;0;-0.7055559999999998;0;0;0;0;0.7055559999999998;0;0;0;0;1;0;1998;0;1998;0;9; [Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.]
            Oversampling factor: 1 [Determines the oversampling of the reference image geometry. If it's a number, then all segments are oversampled with the same value (value of 1 means no oversampling). If it has the value "A", then automatic oversampling is calculated.]
            Crop to reference image geometry: 0 [Crop the model to the extent of reference geometry. 0 (default) = created labelmap will contain the entire model. 1 = created labelmap extent will be within reference image extent.]
            Collapse labelmaps: 1 [Merge the labelmaps into as few shared labelmaps as possible 1 = created labelmaps will be shared if possible without overwriting each other.]
          Debug: Off
          Modified Time: 281964
          Reference Count: 2
          Registered Events: (none)
        Rule[3]:
          Name: Fractional labelmap to closed surface
          SourceRepresentationName: Fractional labelmap
          TargetRepresentationName: Closed surface
          ConversionParameters:
            Decimation factor: 0.0 [Desired reduction in the total number of polygons. Range: 0.0 (no decimation) to 1.0 (as much simplification as possible). Value of 0.8 typically reduces data set size by 80% without losing too much details.]
            Smoothing factor: 0.5 [Smoothing factor. Range: 0.0 (no smoothing) to 1.0 (strong smoothing).]
            Compute surface normals: 1 [Compute surface normals. 1 (default) = surface normals are computed. 0 = surface normals are not computed (slightly faster but produces less smooth surface display, not used if vtkSurfaceNets3D is used).]
            Conversion method: 0 [Conversion method. 0 (default) = vtkDiscreteFlyingEdges3D is used to generate closed surface.1 = vtkSurfaceNets3D (more performant than flying edges).]
            SurfaceNets smoothing: 0 [SurfaceNets smoothing. 0 (default) = Smoothing done by vtkWindowedSincPolyDataFilter1 = Smoothing done in surface nets filter.]
            Joint smoothing: 0 [Perform joint smoothing.]
            Fractional labelmap oversampling factor: 1 [Determines the oversampling of the reference image geometry. All segments are oversampled with the same value (value of 1 means no oversampling).]
            Threshold fraction: 0.5 [Determines the threshold that the closed surface is created at as a fractional value between 0 and 1.]
          Debug: Off
          Modified Time: 281966
          Reference Count: 2
          Registered Events: (none)
  SegmentListFilterEnabled: false
  SegmentListFilterOptions:
</code></pre>
<p>Notably I can see that the new segmentations which have the name Label_1, Label_2 as opposed to the old ones which are named segment_1, segment_2. The spacing, extent, scalar type, and IJKtoRASDirections, are all different between the new and old segments.<br>
How can I ensure that this information is also preserved on the new segments?</p>

---

## Post #3 by @pieper (2024-02-04 14:54 UTC)

<p><a class="mention" href="/u/tueboesen">@tueboesen</a> Yes, exporting the Segmentations to Labelmap volume nodes is a good way to work with them from numpy, but keeping track of the mapping between label numbers and segment IDs requires some care.</p>
<p>A good way to address this is to always use a color node to specify the mapping when going back and forth.  You’ve probably been looking already, but the script repository has a lot of good examples, and if you search for color you’ll see how they are used for this purpose.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations</a></p>
<p>Also for this operation you can say to just mrml, vtk, numpy, and the segmentation logic.  Mixing in sitk and qt may just make it harder to tell what’s going on.</p>
<p>hope that helps,<br>
Steve</p>

---

## Post #4 by @tueboesen (2024-02-05 09:01 UTC)

<p>I was only mixing in sitk and qt because it was the first methods I found for extracting the numpy array from slicer, but after your suggestion I ended up removing those and I ended up with the following, which seems to work!</p>
<pre><code class="lang-auto">
    def onApply(self):
        # Make sure the user wants to do the operation, even if the segment is not visible
        print(self.scriptedEffect.confirmCurrentSegmentVisible())
        if not self.scriptedEffect.confirmCurrentSegmentVisible():
            return
        #
        # Get list of visible segment IDs, as the effect ignores hidden segments.
        segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
        visibleSegmentIds = vtk.vtkStringArray()
        segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(visibleSegmentIds)
        if visibleSegmentIds.GetNumberOfValues() == 0:
            logging.info("Smoothing operation skipped: there are no visible segments")
            return

        # This can be a long operation - indicate it to the user
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

        # Allow users revert to this state by clicking Undo
        self.scriptedEffect.saveStateForUndo()


        # Export source image data to temporary new volume node.
        # Note: Although the original source volume node is already in the scene, we do not use it here,
        # because the source volume may have been resampled to match segmentation geometry.
        sourceVolumeNode = slicer.vtkMRMLScalarVolumeNode()
        slicer.mrmlScene.AddNode(sourceVolumeNode)
        sourceVolumeNode.SetAndObserveTransformNodeID(segmentationNode.GetTransformNodeID())
        slicer.vtkSlicerSegmentationsModuleLogic.CopyOrientedImageDataToVolumeNode(self.scriptedEffect.sourceVolumeImageData(), sourceVolumeNode)

        # Generate merged labelmap of all visible segments, as the filter expects a single labelmap with all the labels.
        mergedLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
        slicer.mrmlScene.AddNode(mergedLabelmapNode)
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(segmentationNode, visibleSegmentIds, mergedLabelmapNode, sourceVolumeNode)
        # slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, mergedLabelmapNode, slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)


        # Run segmentation algorithm

        # Read input data from Slicer into SimpleITK
        labelImage_np = slicer.util.arrayFromVolume(mergedLabelmapNode)
        backgroundImage_np = slicer.util.arrayFromVolume(mergedLabelmapNode)

        m = labelImage_np != 0
        m2 = np.sum(m,axis=(1,2))
        idx = np.argmax(m2)
        print(labelImage_np.shape)


        # Do the segmentation 
        labelImage_np[idx] = dummy(backgroundImage_np[idx], labelImage_np[idx])

        # Set the labelmap volume nodes voxels to the numpy array
        slicer.util.updateVolumeFromArray(mergedLabelmapNode, labelImage_np)

        # Convert labelmap to segmentation node
        slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(mergedLabelmapNode, segmentationNode)


        slicer.mrmlScene.RemoveNode(sourceVolumeNode)
        slicer.mrmlScene.RemoveNode(mergedLabelmapNode)

        qt.QApplication.restoreOverrideCursor()
        return
</code></pre>
<p>Thank  you very much for your help</p>

---
