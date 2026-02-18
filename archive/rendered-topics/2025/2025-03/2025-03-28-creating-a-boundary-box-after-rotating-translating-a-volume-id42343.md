# Creating a boundary box after rotating/translating a volume

**Topic ID**: 42343
**Date**: 2025-03-28
**URL**: https://discourse.slicer.org/t/creating-a-boundary-box-after-rotating-translating-a-volume/42343

---

## Post #1 by @coco (2025-03-28 10:14 UTC)

<p>Dear all,<br>
I’m having some issues creating a bounding box arround my segment after registering a volume and segments.<br>
As you can see on the picture, the calculated bounding box “sticks” to the original volume geometry before rotation whilst I want a bounding box taking into consideration the rotation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e9c3420906f3af50a0fb2219f8b3375a115fc9.jpeg" data-download-href="/uploads/short-url/5H5sfD31Y0oaVIp6TcKLbXLriiJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e9c3420906f3af50a0fb2219f8b3375a115fc9_2_690x367.jpeg" alt="image" data-base62-sha1="5H5sfD31Y0oaVIp6TcKLbXLriiJ" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e9c3420906f3af50a0fb2219f8b3375a115fc9_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e9c3420906f3af50a0fb2219f8b3375a115fc9_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27e9c3420906f3af50a0fb2219f8b3375a115fc9_2_1380x734.jpeg 2x" data-dominant-color="514A55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×1019 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> so that the size of my volume is optimized.</p>
<p>I have two scripts, first one does a centering and unit conversion and allows the user to make small adjustments to the segementation of a brain and allows the user to edit/place fiducials before running the registration in the second script. The bounding box is created during the second script.<br>
(Apologies but it looks like copy pasting my script in this window does not work properly, let me know how to edit this and i’ll fix it):</p>
<p>Script1</p>
<pre><code class="lang-auto">import slicer
import json
import os


#  exec(open("/work/shared/ngmm/scripts/Python/preprocessing_creating_RC_1_test.py", encoding='utf-8').read())

def pause_and_check(message):
    """Pauses execution using a message box to check progress and allows quitting."""
    user_input = qt.QMessageBox.question(None, "Pause", message + "\n\nContinue?", qt.QMessageBox.Yes | qt.QMessageBox.No)
    if user_input == qt.QMessageBox.No:
        print("Exiting script.")
        sys.exit()

def apply_centering_transform(volumeNode):
    """Applies a centering transform with a scale of 0.001."""
    transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", "CenteringTransform")
    matrix = vtk.vtkMatrix4x4()
    matrix.SetElement(0, 0, 0.001)
    matrix.SetElement(1, 1, 0.001)
    matrix.SetElement(2, 2, 0.001)
    transformNode.SetMatrixTransformToParent(matrix)
    volumeNode.SetAndObserveTransformNodeID(transformNode.GetID())
    return transformNode

def get_single_volume_node():
    """Retrieves the only volume node in the scene or raises an exception if multiple are found."""
    volumeNodes = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")
    if len(volumeNodes) != 1:
        raise Exception(f"Expected exactly one volume node, but found {len(volumeNodes)}.")
    return volumeNodes[0]

def segment_volume(volumeNode):
    """Segments the volume to create 'background' and 'brain' segments."""

    # Create segmentation
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("background")

    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setSourceVolumeNode(volumeNode)

    # Thresholding
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold","175")
    effect.setParameter("MaximumThreshold","255")
    effect.self().onApply()
    segmentationNode.CreateClosedSurfaceRepresentation()


    # Keep largest island
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "KEEP_LARGEST_ISLAND")
    effect.setParameter("MinimumSize", "1000")
    effect.self().onApply()
    segmentationNode.CreateClosedSurfaceRepresentation()


    # Invert selection for 'brain'
    segmentEditorWidget.setActiveEffectByName("Logical operators")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "INVERT")
    effect.self().onApply()
    segmentationNode.CreateClosedSurfaceRepresentation()


    # Keep largest island for 'brain'
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "KEEP_LARGEST_ISLAND")
    effect.setParameter("MinimumSize", "1000")
    effect.self().onApply()
    segmentationNode.CreateClosedSurfaceRepresentation()


    # Make segmentation results visible in 3D
    segmentationNode.CreateClosedSurfaceRepresentation()

    return segmentationNode

def load_segmentation_and_landmarks(seg_path, landmark_path):
    """Loads segmentation and landmarking files."""
    slicer.util.loadSegmentation(seg_path)
    slicer.util.loadMarkups(landmark_path)
    slicer.util.selectModule("Markups")

def create_empty_landmark_file(input_json, output_json):
    """Creates an empty landmark file with the same control points but no coordinates."""
    
    with open(input_json, 'r') as f:
        data = json.load(f)

    for markup in data["markups"]:  # Ensure correct hierarchy
        for point in markup["controlPoints"]:  # Modify actual control points
            point["position"] = [0, 0, 0]  # Or use None if required

    with open(output_json, 'w') as f:
        json.dump(data, f, indent=4)

    # Load the new landmark file into Slicer3D
    new_landmark_node = slicer.util.loadMarkups(output_json)

    # Optionally, rename the node for clarity
    if new_landmark_node:
        new_landmark_node.SetName("target_landmarks")
    
    slicer.util.selectModule("Markups")  # Switch to Markups module


def crop_volume(roiNode, volumeNode, outputVolumeName, spacingScaling=1.0):
    """
    Crops the volume using the provided ROI node.
    The spacingScaling constant controls output resolution:
      spacingScaling=1.0 --&gt; same resolution as input (1×)
      spacingScaling&gt;1.0  --&gt; downsampled output (e.g. 5×)
      
    Isotropic resampling is enforced and the B-spline interpolator is used.
    """
    cropParametersNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLCropVolumeParametersNode')
    cropParametersNode.SetInputVolumeNodeID(volumeNode.GetID())
    cropParametersNode.SetROINodeID(roiNode.GetID())
    cropParametersNode.SetIsotropicResampling(True)
    cropParametersNode.SetSpacingScalingConst(spacingScaling)
    cropParametersNode.SetInterpolationMode(2)
    
    croppedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", outputVolumeName)
    cropParametersNode.SetOutputVolumeNodeID(croppedVolumeNode.GetID())
    
    slicer.modules.cropvolume.logic().Apply(cropParametersNode)
    return croppedVolumeNode





def main():
    volumeNode = get_single_volume_node()
    seg_path = "/work/shared/ngmm/3Dimage/ATLAS/registration_atlas_hrem/fullbrain.seg.nrrd"
    landmark_path = "/work/shared/ngmm/3Dimage/ATLAS/registration_atlas_hrem/alignement_landmarks_all.mrk.json"
    empty_landmark_path = "/work/shared/ngmm/3Dimage/ATLAS/registration_atlas_hrem/target_landmarks.mrk.json"
    
 
    # Step 1: Apply centering transform
    centeringTransform = apply_centering_transform(volumeNode)

    volumeNode = get_single_volume_node()
    if not volumeNode or not volumeNode.GetImageData():
        raise RuntimeError("No valid volume loaded. Check input data.")

    # pause_and_check("iseverything ok ?")
    transformLogic = slicer.vtkSlicerTransformLogic()
    transformLogic.hardenTransform(volumeNode)

    # Step 1.1 Create a new ROI that will be fit to volumeNode
    roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
    cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
    cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
    cropVolumeParameters.SetROINodeID(roi.GetID())
    slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
    slicer.mrmlScene.RemoveNode(cropVolumeParameters)

    # Step 1.2: Crop the volume with downscaling (5X resolution).
    croppedVolume_5x = crop_volume(roi, volumeNode, volumeNode.GetName() + "_L5", spacingScaling=10.0)
    # pause_and_check("Segmentation completed successfully?")
    slicer.mrmlScene.RemoveNode(roi)

    # Step 2: Segment L5 volume
    croppedVolumeNode = slicer.util.getNode(volumeNode.GetName() + "_L5")
    segmentationNode = segment_volume(croppedVolumeNode)

    # pause_and_check("Segmentation completed successfully?")

    # Step 3: Load segmentation and landmarks
    load_segmentation_and_landmarks(seg_path, landmark_path)
    # pause_and_check("Segmentation and landmarks loaded correctly?")

    # Step 4: Create empty landmark file for user input
    create_empty_landmark_file(landmark_path, empty_landmark_path)
    
    # Ensure layout manager is available
    layoutManager = slicer.app.layoutManager()

    # Show first 3D view
    threeDWidget1 = layoutManager.threeDWidget(0)
    threeDView1 = threeDWidget1.threeDView()
    threeDView1.resetFocalPoint()

    # Create a second 3D view (if not already present)
    if layoutManager.threeDViewCount &lt; 2:
        layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDual3DView)

    # Get segmentation nodes
    segmentationNode1 = slicer.util.getNode("Segmentation")  # First segmentation
    segmentationNode2 = slicer.util.getNode("fullbrain")     # Second segmentation

    displayNode1 = segmentationNode1.GetDisplayNode()
    displayNode2 = segmentationNode2.GetDisplayNode()

    # Get 3D view nodes
    viewNodes = slicer.util.getNodesByClass("vtkMRMLViewNode")

    if len(viewNodes) &gt;= 2:
        view1 = viewNodes[0]  # First 3D view
        view2 = viewNodes[1]  # Second 3D view

        # RESET all view assignments before setting new ones
        displayNode1.RemoveAllViewNodeIDs()
        displayNode2.RemoveAllViewNodeIDs()

        # Show "segmentation" only in the first 3D view
        displayNode1.AddViewNodeID(view1.GetID())

        # Show "brain" only in the second 3D view
        displayNode2.AddViewNodeID(view2.GetID())

        displayNode1.SetVisibility3D(True)
        displayNode2.SetVisibility3D(True)

    # =============================================
    # 🔹 ADDING LANDMARK NODES TO SPECIFIC 3D VIEWS
    # =============================================

    # Get landmark nodes
    landmarkNode1 = slicer.util.getNode("alignement_landmarks_all")  # Goes in new 3D view
    landmarkNode2 = slicer.util.getNode("target_landmarks")      # Goes in old 3D view

    landmarkDisplay1 = landmarkNode1.GetDisplayNode()
    landmarkDisplay2 = landmarkNode2.GetDisplayNode()

    # Reset all views before assigning
    landmarkDisplay1.RemoveAllViewNodeIDs()
    landmarkDisplay2.RemoveAllViewNodeIDs()

    # Assign landmark nodes to the correct views
    landmarkDisplay1.AddViewNodeID(view2.GetID())  # New 3D view
    landmarkDisplay2.AddViewNodeID(view1.GetID())  # Old 3D view
    landmarkDisplay1.SetSelectedColor(100,100,0)
    landmarkDisplay2.SetSelectedColor(1,1,0)


    # Explicitly force visibility update
    landmarkDisplay1.SetVisibility3D(True)
    landmarkDisplay2.SetVisibility3D(True)

    # Ensure UI refreshes
    slicer.app.processEvents()

    layoutManager = slicer.app.layoutManager()
    threeDWidget = layoutManager.threeDWidget(0)
    threeDView = threeDWidget.threeDView()
    threeDView.rotateToViewAxis(3)  # Look from anterior direction
    threeDView.resetFocalPoint()  # Reset the 3D view cube size and center it
    threeDView.resetCamera()  # Reset camera zoom

    # Let user place landmarks manually...
    slicer.util.delayDisplay("Place landmarks manually, then press OK in the toolbar when done.", autoClose=False)

    # Retrieve the volume node (assuming there's only one)
    volumeNode = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")[0]
    volumeName = volumeNode.GetName()  # e.g. "NG4309"

    # Retrieve the centering transform node (make sure it exists in the scene)
    centeringTransformNode = slicer.util.getNode("CenteringTransform")

    # Define the save folder and build the file name using the volume name as a prefix
    save_folder = "/work/shared/ngmm/3Dimage/iso_processed_files/"
    file_name = f"{volumeName}_CenteringTransform.h5"
    file_path = os.path.join(save_folder, file_name)

    # Save the transform node to file
    slicer.util.saveNode(centeringTransformNode, file_path)

    print("Saved CenteringTransform to", file_path)

    # Delete the croppedVolumeNode
    slicer.mrmlScene.RemoveNode(croppedVolumeNode)

main()
</code></pre>
<p>Script2:</p>
<pre><code class="lang-auto">import os
import vtk
import numpy as np
import slicer
import re

#exec(open("/work/shared/ngmm/scripts/Python/preprocessing_creating_RC_2_test.py", encoding='utf-8').read())


def perform_fiducial_registration(fixedFiducialNode, movingFiducialNode, nodesToTransform):
    """
    Performs rigid fiducial registration and hardens the resulting transform on each node in nodesToTransform.
    """
    params = {
        "fixedLandmarks": fixedFiducialNode.GetID(),
        "movingLandmarks": movingFiducialNode.GetID(),
        "transformType": "Rigid"
    }
    # Create a new transform node to store the registration result.
    transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "FiducialRegistrationTransform")
    params["saveTransform"] = transformNode.GetID()
    
    # Run the registration synchronously.
    slicer.cli.runSync(slicer.modules.fiducialregistration, None, params)
    
    # Apply and harden the registration transform on all provided nodes.
    transformLogic = slicer.vtkSlicerTransformLogic()
    for node in nodesToTransform:
        node.SetAndObserveTransformNodeID(transformNode.GetID())
        transformLogic.hardenTransform(node)
    
    slicer.app.processEvents()
    print("✅ Fiducial registration transform computed and hardened on all target nodes.")
    return transformNode

def crop_volume(roiNode, volumeNode, outputVolumeName, spacingScaling=1.0):
    """
    Crops the volume using the provided ROI node.
    The spacingScaling constant controls output resolution:
      spacingScaling=1.0 --&gt; same resolution as input (1×)
      spacingScaling&gt;1.0  --&gt; downsampled output (e.g. 5×)
      
    Isotropic resampling is enforced and the B-spline interpolator is used.
    """
    cropParametersNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLCropVolumeParametersNode')
    cropParametersNode.SetInputVolumeNodeID(volumeNode.GetID())
    cropParametersNode.SetROINodeID(roiNode.GetID())
    cropParametersNode.SetIsotropicResampling(True)
    cropParametersNode.SetSpacingScalingConst(spacingScaling)
    cropParametersNode.SetInterpolationMode(4)
    
    croppedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", outputVolumeName)
    cropParametersNode.SetOutputVolumeNodeID(croppedVolumeNode.GetID())
    
    slicer.modules.cropvolume.logic().Apply(cropParametersNode)
    return croppedVolumeNode

# === Step 1: Harden any existing CenteringTransform (if available) ===
try:
    centeringTransformNode = slicer.util.getNode("CenteringTransform")
    volumeNode = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")[0]
    transformLogic = slicer.vtkSlicerTransformLogic()
    transformLogic.hardenTransform(volumeNode)
    slicer.app.processEvents()
    print("✅ CenteringTransform hardened onto volume.")
except Exception as e:
    print("CenteringTransform node not found or could not be hardened. Skipping this step.")

# === Step 2: Perform Fiducial Registration ===

# Get fixed and moving fiducial nodes.
fixedFiducialNode = slicer.util.getNode("alignement_landmarks_all")
movingFiducialNode = slicer.util.getNode("target_landmarks")

# Get the volume and segmentation nodes.
volumeNode = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode")[0]
segmentationNode = slicer.util.getNode("Segmentation")

# Create a new label map volume node to hold the segmentation
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "SegmentationLabelmap")
# Export the segmentation into the label map volume.
# The export function uses the geometry of the reference volume (here, volumeNode) for spatial parameters.
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
# Now you can convert the label map volume to a NumPy array.
label = slicer.util.arrayFromVolume(labelmapVolumeNode)


# Apply registration transform to volume, segmentation, and the moving fiducials.
nodesToApplyTransform = [volumeNode, segmentationNode, movingFiducialNode]
registrationTransform = perform_fiducial_registration(fixedFiducialNode, movingFiducialNode, nodesToApplyTransform)

# === Step 3: Compute an Axis-Aligned Bounding Box for "Segment_1" ===

# --- Updated Bounding Box Computation (Step 3) ---

# Find indices of voxels equal to 1.
points = np.array(np.where(label == 1))  # shape: (3, N) where order is (z, y, x)
if points.shape[1] == 0:
    raise ValueError("No voxels with label 1 found. Check your segmentation export.")

# Compute the min and max indices along each axis (in IJK order, but note that numpy gives [z,y,x]).
min_ijk = np.array([np.min(points[0]), np.min(points[1]), np.min(points[2])])
max_ijk = np.array([np.max(points[0]), np.max(points[1]), np.max(points[2])])

# Add margin (in voxels)
margin = 1
margin_half = margin / 2.0
min_ijk = min_ijk - margin_half
max_ijk = max_ijk + margin_half

# Define the 8 corners of the bounding box in IJK space.
# Note: our "points" are in (z,y,x) order; we want IJK order as (x, y, z).
# So we need to reorder: I = third component, J = second, K = first.
corners_ijk = np.array([
    [min_ijk[2], min_ijk[1], min_ijk[0]],
    [min_ijk[2], min_ijk[1], max_ijk[0]],
    [min_ijk[2], max_ijk[1], min_ijk[0]],
    [min_ijk[2], max_ijk[1], max_ijk[0]],
    [max_ijk[2], min_ijk[1], min_ijk[0]],
    [max_ijk[2], min_ijk[1], max_ijk[0]],
    [max_ijk[2], max_ijk[1], min_ijk[0]],
    [max_ijk[2], max_ijk[1], max_ijk[0]],
])

# Transform each corner from IJK to RAS using the volume's IJK-to-RAS matrix.
ijkToRasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrix)
corners_ras = []
for corner in corners_ijk:
    pt_ijk = list(corner) + [1]  # homogeneous coordinate
    pt_ras = ijkToRasMatrix.MultiplyDoublePoint(pt_ijk)
    corners_ras.append(pt_ras[:3])
corners_ras = np.array(corners_ras)

# Compute the axis-aligned bounding box in RAS from the transformed corners.
min_ras = np.min(corners_ras, axis=0)
max_ras = np.max(corners_ras, axis=0)
center_ras = (min_ras + max_ras) / 2.0
radius_ras = (max_ras - min_ras) / 2.0

print("Computed RAS bounding box:")
print("  min:", min_ras)
print("  max:", max_ras)
print("  center:", center_ras)
print("  radius:", radius_ras)

# Create an ROI (bounding box) node for "Segment_1" using the computed RAS values.
roi = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roi.SetXYZ(center_ras[0], center_ras[1], center_ras[2])
roi.SetRadiusXYZ(radius_ras[0], radius_ras[1], radius_ras[2])
print("✅ ROI (bounding box in RAS) created for Segment_1.")

# === Step 4: Crop the Volume using the ROI and Save 1X and 5X Copies ===

# Crop the volume at full (1X) resolution.
croppedVolume_1x = crop_volume(roi, volumeNode, volumeNode.GetName() + "_RC", spacingScaling=1.0)
# Crop the volume with downscaling (5X resolution).
croppedVolume_5x = crop_volume(roi, volumeNode, volumeNode.GetName() + "_RCL5", spacingScaling=5.0)
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(croppedVolume_5x)

# Define your save folder and base filename.
save_folder = "/work/shared/ngmm/3Dimage/iso_processed_files/"  # Replace with your actual save folder path
base_filename = volumeNode.GetName()

# === Step 4.1: setting geometry of segmentation and creating a margin around brain

segmentEditorNodes = slicer.util.getNodesByClass("vtkMRMLSegmentEditorNode")
if segmentEditorNodes:
    segmentEditorNode = segmentEditorNodes[0]
else:
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")

# Set the segmentation and master volume nodes on the Segment Editor node
# segmentEditorNode.SetSegmentationNode(segmentationNode)
# segmentEditorNode.SetMasterVolumeNode(croppedVolume_5x)

# --- Set up the Segment Editor widget ---
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(croppedVolume_5x)

# --- Select the segment to modify ---
selectedSegmentID = "background"
segmentEditorWidget.setCurrentSegmentID(selectedSegmentID)
segmentEditorNode.SetSelectedSegmentID(selectedSegmentID)

# --- Activate the Margin effect ---
segmentEditorWidget.setActiveEffectByName("Margin")
effect1 = segmentEditorWidget.activeEffect()

# --- Set effect parameters and apply ---
# Here we set MarginSizeMm to 0.15; adjust this value as needed.
effect1.setParameter("MarginSizeMm", 0.15)
effect1.self().onApply()

print("Margin effect applied to segment:", selectedSegmentID)

# --- Activate the mask effect ---
# --- Node preparation
maskedVolume_5X = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", base_filename + "_RCL5_masked")
maskedVolume_1X = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", base_filename + "_RC_masked")
masked5X = slicer.util.getNode(base_filename + "_RCL5_masked")
masked1X = slicer.util.getNode(base_filename + "_RC_masked")
RCL5Node = slicer.util.getNode(base_filename + "_RCL5")
RCNode = slicer.util.getNode(base_filename + "_RC")
segmentation = segmentationNode.GetSegmentation()

# --- applying mask on RCL5
backgroundSegment = segmentation.GetSegment('background')
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(masked5X)
segmentEditorWidget.setActiveEffectByName("Mask volume")
effect2 = segmentEditorWidget.activeEffect()
effect2.setParameter("FillValue", 0)
effect2.setParameter("Operation", "FILL_OUTSIDE")
effect2.self().outputVolumeSelector.setCurrentNode(maskedVolume_5X)
effect2.self().inputVolumeSelector.setCurrentNode(RCL5Node)
effect2.self().onApply()

segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(masked1X)
segmentEditorWidget.setActiveEffectByName("Mask volume")
effect3 = segmentEditorWidget.activeEffect()
effect3.setParameter("FillValue", 0)
effect3.setParameter("Operation", "FILL_OUTSIDE")
effect3.self().outputVolumeSelector.setCurrentNode(maskedVolume_1X)
effect3.self().inputVolumeSelector.setCurrentNode(RCNode)
effect3.self().onApply()


# === Step 5: Save Additional Nodes with Generic Volume Prefix ===

# Extract the volume prefix from the volume node name.
# For example, if volumeNode.GetName() returns "NG4309_...", the prefix will be "NG4309".
volumeName = volumeNode.GetName()  # volumeNode should already be defined
match = re.search(r'^(NG\d+)', volumeName)
if match:
    volumePrefix = match.group(1)
else:
    volumePrefix = volumeName  # fallback if pattern not found

# Define the output folder.
outputFolder = "/work/shared/ngmm/3Dimage/iso_processed_files/"

# Construct the file paths using the extracted volume prefix.
roi_save_path = os.path.join(outputFolder, volumePrefix + "_boundingbox.mrk.json")
registration_transform_save_path = os.path.join(outputFolder, volumePrefix + "_reg.h5")
target_landmarks_save_path = os.path.join(outputFolder, volumePrefix + "_reg_lm.mrk.json")
segmentation_save_path = os.path.join(outputFolder, volumePrefix + "_wholebrain_seg.seg.nrrd")

# Save the nodes:
# 'roi' should be your MarkupsROI node,
# 'registrationTransform' is the transform node from fiducial registration,
# 'movingFiducialNode' is your target landmarks node,
# and 'segmentationNode' is your segmentation node.
slicer.util.saveNode(roi, roi_save_path)
slicer.util.saveNode(registrationTransform, registration_transform_save_path)
slicer.util.saveNode(movingFiducialNode, target_landmarks_save_path)
slicer.util.saveNode(segmentationNode, segmentation_save_path)

print("✅ Nodes saved with volume prefix:", volumePrefix)
print("    ROI saved as:", roi_save_path)
print("    Registration transform saved as:", registration_transform_save_path)
print("    Target landmarks saved as:", target_landmarks_save_path)
print("    Segmentation saved as:", segmentation_save_path)

output_path_1X = os.path.join(save_folder, base_filename + "_RC_masked.nrrd")
slicer.util.saveNode(maskedVolume_1X, output_path_1X)
output_path_5X = os.path.join(save_folder, base_filename + "_RCL5_masked.nrrd")
slicer.util.saveNode(maskedVolume_5X, output_path_5X)

print(" Cropped volumes saved:")
print("    1X resolution:", output_path_1X)
print("    5X resolution:", output_path_5X)

</code></pre>
<p>I know that when we do this manually, we have the same issue and we have to create a roi from scratch and adjust it manually to the size of the brain, then select it in crop volume. If we create a roi from cropvolume it will do the same thing as on the picture.</p>
<p>Can someone guide me please ?</p>
<p>ps: again, thanks to the community and developpers for a great freeware !</p>

---

## Post #2 by @mikebind (2025-03-28 16:04 UTC)

<p>This script from the script repository might be helpful:  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi" rel="noopener nofollow ugc">script_repository.html#markups-roi</a></p>
<p>It shows how to construct a new oriented bounding box ROI around a segment. If it is important to you that the axes of the new bounding box are exactly aligned with the rotation you applied, this will not achieve that, but you could perhaps adapt it.</p>

---

## Post #3 by @coco (2025-03-28 17:11 UTC)

<p>Thank! yes, I think the issue is that the segmentation “remembers” the original orientation of the segment. There’s something missing to change that, I’m a bit stuck right now.</p>

---

## Post #4 by @mikebind (2025-03-28 18:57 UTC)

<p>I have not dived into the particulars of your scripts, but a few things you can try which might help:</p>
<ul>
<li>If try hardening your applied transforms if they are only soft applied. If you do that, then any automatically fit ROI should be in the rotated reference frame rather than the original.</li>
<li>The grid geometry of the segmentation can be controlled within the segmentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#editing-a-segmentation-imported-from-model-surface-mesh-file" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation – Specify geometry</a>) or on export to a labelmap <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation – Export to labelmap</a>. If you have an image with the geometry you need, you can use it to specify the geometry of the segmentation or exported labelmap of a segment</li>
</ul>
<p>My guess is that hardening the applied transforms (usually <code>node.HardenTransform()</code> )  before creating the ROI will solve your issue.</p>

---

## Post #5 by @coco (2025-04-02 09:30 UTC)

<p>To cut a long story short, I found that I needed to resample my volume after rotation and use this new “aligned” volume to calculate a roi (I used/adapted the script “Extracting volume patches around segments” from the script repository). New script works but I am not certain it is very helpful to others.</p>

---
