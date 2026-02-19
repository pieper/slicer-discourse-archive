---
topic_id: 34079
title: "Converting Segmentation To Numpy Array And Back Does Not Con"
date: 2024-02-01
url: https://discourse.slicer.org/t/34079
---

# Converting segmentation to numpy array and back does not conserve layer ordering

**Topic ID**: 34079
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/converting-segmentation-to-numpy-array-and-back-does-not-conserve-layer-ordering/34079

---

## Post #1 by @tueboesen (2024-02-01 10:03 UTC)

<p>I have the following function in my custom built segment editor module, built upon the standard extension script. The problem is that the segments I manually put in gets moved to a different layer when I run this code, and I don’t understand how this can happen.</p>
<p>Here is what it might look like before<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9125025b805c00c17adca6d34510284989076086.jpeg" data-download-href="/uploads/short-url/kI0wyp2FyeCtvSznUBw8zck19ga.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9125025b805c00c17adca6d34510284989076086_2_690x470.jpeg" alt="image" data-base62-sha1="kI0wyp2FyeCtvSznUBw8zck19ga" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9125025b805c00c17adca6d34510284989076086_2_690x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9125025b805c00c17adca6d34510284989076086_2_1035x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9125025b805c00c17adca6d34510284989076086_2_1380x940.jpeg 2x" data-dominant-color="3B3939"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1391×948 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here is where the segmentation shows up after applying it. As you can see the slider is in a completely different layer, and there now no longer any segmentation in the layer it was originally applied in<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ac4aef4d5d004d019f5238439753b0d9223f64e.png" data-download-href="/uploads/short-url/66lrECd7pA1yanlC38VQ85hxGhw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac4aef4d5d004d019f5238439753b0d9223f64e_2_690x470.png" alt="image" data-base62-sha1="66lrECd7pA1yanlC38VQ85hxGhw" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac4aef4d5d004d019f5238439753b0d9223f64e_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac4aef4d5d004d019f5238439753b0d9223f64e_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ac4aef4d5d004d019f5238439753b0d9223f64e_2_1380x940.png 2x" data-dominant-color="302E29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1391×948 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The full function is given below. But I think the interesting part is this:</p>
<p><code>labelImage = sitk.GetImageFromArray(labelImage_np)</code><br>
which is how I get the numpy array back into a format that slicer can interact with, but maybe this is not the correct way to do that?</p>
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


        # Run segmentation algorithm

        # Read input data from Slicer into SimpleITK
        labelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))
        backgroundImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(sourceVolumeNode.GetName()))

        Image_np = sitk.GetArrayFromImage(backgroundImage)
        labelImage_np = sitk.GetArrayFromImage(labelImage)
        m = labelImage_np != 0
        m2 = np.sum(m,axis=(1,2))
        idx = np.argmax(m2)
       
        labelImage_np[idx] = dummy(Image_np[idx], labelImage_np[idx])
        labelImage = sitk.GetImageFromArray(labelImage_np)

        sitk.WriteImage(labelImage, sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))

        slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(mergedLabelmapNode, segmentationNode, visibleSegmentIds)

        mergedLabelmapNode.GetImageData().Modified()
        mergedLabelmapNode.Modified()
        
        # Update segmentation from labelmap node and remove temporary nodes
        slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(mergedLabelmapNode, segmentationNode, visibleSegmentIds)
        slicer.mrmlScene.RemoveNode(sourceVolumeNode)
        slicer.mrmlScene.RemoveNode(mergedLabelmapNode)
        
        qt.QApplication.restoreOverrideCursor()
</code></pre>

---
