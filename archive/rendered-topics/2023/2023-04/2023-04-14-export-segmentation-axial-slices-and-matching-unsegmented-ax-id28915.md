# Export segmentation axial slices and matching unsegmented axial slices as .png in different folders

**Topic ID**: 28915
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/export-segmentation-axial-slices-and-matching-unsegmented-axial-slices-as-png-in-different-folders/28915

---

## Post #1 by @Ba_Sar (2023-04-14 12:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7017d3e961ef768a410f1f531af32a8abc56df4.jpeg" data-download-href="/uploads/short-url/zf77NRv5NNJDgvWpKFgCe8xU9Ba.jpeg?dl=1" title="slicer_screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7017d3e961ef768a410f1f531af32a8abc56df4_2_690x249.jpeg" alt="slicer_screenshot" data-base62-sha1="zf77NRv5NNJDgvWpKFgCe8xU9Ba" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7017d3e961ef768a410f1f531af32a8abc56df4_2_690x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7017d3e961ef768a410f1f531af32a8abc56df4_2_1035x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7017d3e961ef768a410f1f531af32a8abc56df4_2_1380x498.jpeg 2x" data-dominant-color="1E1D1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_screenshot</span><span class="informations">1912×691 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Dear community,<br>
i hope you are doing well. I have a T2 TSE TRA MRI dicom of the spine. I used the axial plane to segment the dural sack in 3 different slices. now i want to accomplish the following task:<br>
1)export the segmented axial slices in the folder “segmented” as .png image<br>
2)export the unsegmented corresponding axial slices (same name as segmented slices) to the folder “unsegmented” as .png image</p>
<p>I was able to build the following Python code which was supposed to do this task, however, when accessing the folders they show only black images. Maybe you have a better automated solution for me. I thought such automated way would be faster then manually exporting the slices. I am confident that you as experts will have a better solution for me. I also attached the image of my subject hierarchy. Thank you very much in advance.</p>
<p>Code:</p>
<pre><code class="lang-python">import os
import vtk

# Set the export directories
non_segmented_export_directory = "C:\\Users\\Babak\\Desktop\\Automated_Dural_sack_measurement\\own_study\\non_segmented"
segmented_export_directory = "C:\\Users\\Babak\\Desktop\\Automated_Dural_sack_measurement\\own_study\\segmented"

# Get the original MRI volume node and the segmentation node
volume_node = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')
segmentation_node = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')

def capture_slice_screenshot(slice_widget, filename):
    # Capture the screenshot using vtkWindowToImageFilter
    window_to_image_filter = vtk.vtkWindowToImageFilter()
    window_to_image_filter.SetInput(slice_widget.sliceView().renderWindow())
    window_to_image_filter.Update()

    # Save the screenshot as a PNG file
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(filename)
    writer.SetInputConnection(window_to_image_filter.GetOutputPort())
    writer.Write()

if volume_node is None or segmentation_node is None:
    print("Error: MRI volume or segmentation node not found. Please check the names and try again.")
else:
    # Create a labelmap from the segmentation
    labelmap_volume_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
    slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentation_node, labelmap_volume_node, volume_node)

    # Get the slice widget and slice node for the red slice view
    slice_widget = slicer.app.layoutManager().sliceWidget("Red")
    slice_logic = slice_widget.sliceLogic()
    slice_node = slice_logic.GetSliceNode()
    slice_composite_node = slice_logic.GetSliceCompositeNode()

    # Get the RAS to IJK matrix
    ras_to_ijk = vtk.vtkMatrix4x4()
    volume_node.GetRASToIJKMatrix(ras_to_ijk)

    # Loop through the axial slices
    for slice_index in range(volume_node.GetImageData().GetDimensions()[2]):

        # Get the RAS coordinates for the current slice
        ijk_coordinates = [0, 0, slice_index, 1]
        ras_coordinates = ras_to_ijk.MultiplyPoint(ijk_coordinates)

        # Set the current slice index
        slice_node.SetSliceOffset(ras_coordinates[2])

        # Save the non-segmented slice
        non_segmented_filename = os.path.join(non_segmented_export_directory, f"slice_{slice_index:03d}_non_segmented.png")
        slice_composite_node.SetBackgroundVolumeID(volume_node.GetID())
        slice_composite_node.SetLabelVolumeID(None)
        slice_widget.sliceView().forceRender()
        capture_slice_screenshot(slice_widget, non_segmented_filename)

        # Save the segmented slice
        segmented_filename = os.path.join(segmented_export_directory, f"slice_{slice_index:03d}_segmented.png")
        slice_composite_node.SetLabelVolumeID(labelmap_volume_node.GetID())
        slice_widget.sliceView().forceRender()
        capture_slice_screenshot(slice_widget, segmented_filename)
</code></pre>

---

## Post #2 by @pieper (2023-04-14 12:43 UTC)

<p>Maybe you can just use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html">ScreenCapture</a> module.  If you need to script the behavior you can look at how it’s done in the <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py">Animator</a> module.</p>

---
