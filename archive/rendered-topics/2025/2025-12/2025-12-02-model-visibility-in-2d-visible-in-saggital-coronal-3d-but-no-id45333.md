# Model visibility in 2D - visible in saggital/coronal/3D but not axial

**Topic ID**: 45333
**Date**: 2025-12-02
**URL**: https://discourse.slicer.org/t/model-visibility-in-2d-visible-in-saggital-coronal-3d-but-not-axial/45333

---

## Post #1 by @ckolluru (2025-12-02 17:57 UTC)

<p>I have two image stacks, a raw CT image and a corresponding distance map (same physical space, dimensions and spacing). I want to iteratively run vtkFlyingEdges2D on each slice of the distance map, with an isocontour value of 0 and display the result on the 2D axial slice of the CT.</p>
<p>I’m able to create the model (vtkAppendPolyData output) after processing each slice, and it is what I expect in the 3D view. However, when I switch on Slice Display Visibility for the model, I see it in the saggital/coronal views but not the axial view. Am I missing something in this conversion? Here is the script I’m using.</p>
<pre><code class="lang-auto">import vtk
import slicer

# ================================================================
# 1. Extract a 2D slice from a 3D volume using vtkExtractVOI
# ================================================================
def extract_slice_from_volume(volumeNode, k):
    """
    Extracts axial slice k as a 2D vtkImageData.
    Keeps spacing and origin identical to the parent volume.
    """

    imageData = volumeNode.GetImageData()
    dims = imageData.GetDimensions()
    spacing = imageData.GetSpacing()
    origin = imageData.GetOrigin()

    extractor = vtk.vtkExtractVOI()
    extractor.SetInputData(imageData)

    # (xmin, xmax, ymin, ymax, zmin, zmax)
    extractor.SetVOI(0, dims[0]-1,
                     0, dims[1]-1,
                     k, k)

    extractor.Update()
    slice2d = extractor.GetOutput()

    # Copy metadata back (vtkExtractVOI does not preserve it)
    slice2d.SetSpacing(spacing)
    slice2d.SetOrigin(origin)

    return slice2d


# ================================================================
# 2. Extract contour lines using vtkFlyingEdges2D
# ================================================================
def extract_contours_from_2d_image(image2d_vtk, iso_value=0.0):
    """
    Runs vtkFlyingEdges2D on a 2D vtkImageData.
    Returns vtkPolyData (contour lines).
    """

    fe = vtk.vtkFlyingEdges2D()
    fe.SetInputData(image2d_vtk)
    fe.SetValue(0, iso_value)
    fe.Update()

    poly = fe.GetOutput()
    return poly if poly.GetNumberOfPoints() &gt; 0 else None


# ================================================================
# 3. Transform polydata from slice IJK → RAS world coords
# ================================================================
def transform_polydata_IJK_to_RAS(polydata, volumeNode, sliceIndex):
    """
    Takes contour polydata in slice-IJK space and maps it to RAS space.
    Adds Z = slice index before applying the 4×4 IJK→RAS matrix.
    """

    if polydata is None:
        return None

    # Add correct Z position to each point
    points = polydata.GetPoints()
    for i in range(points.GetNumberOfPoints()):
        x, y, z = points.GetPoint(i)
        points.SetPoint(i, x, y, z)

    # Get full IJK→RAS transform
    ijkToRas = vtk.vtkMatrix4x4()
    volumeNode.GetIJKToRASMatrix(ijkToRas)

    transform = vtk.vtkTransform()
    transform.SetMatrix(ijkToRas)

    tf = vtk.vtkTransformPolyDataFilter()
    tf.SetInputData(polydata)
    tf.SetTransform(transform)
    tf.Update()

    return tf.GetOutput()


# ================================================================
# 4. Main: Build all contours into one model node
# ================================================================
def build_contours_for_volume(volumeNode, iso_value=0.0):
    """
    For each slice:
      · Extract 2D image
      · Compute FlyingEdges2D contour
      · Convert contour → proper 3D RAS space
    Then merges everything and adds as a Slicer model.
    """

    imageData = volumeNode.GetImageData()
    dims = imageData.GetDimensions()

    append = vtk.vtkAppendPolyData()

    for k in range(dims[2]):
        print(f"Processing slice {k+1}/{dims[2]}")

        slice2d = extract_slice_from_volume(volumeNode, k)
        poly2d = extract_contours_from_2d_image(slice2d, iso_value)

        if poly2d:
            print(f"  Extracted {poly2d.GetNumberOfLines()} contour lines")

            polyRAS = transform_polydata_IJK_to_RAS(poly2d, volumeNode, k)
            append.AddInputData(polyRAS)
        else:
            print("  No contours found.")

    append.Update()
    combined = append.GetOutput()

    # Create Slicer model
    modelNode = slicer.modules.models.logic().AddModel(combined)
    modelNode.SetName(f"Contours_iso_{iso_value}")

    display = modelNode.GetDisplayNode()
    display.SetColor(1, 0, 0)
    display.SetLineWidth(2)
    display.SetOpacity(1.0)

    return modelNode


# ================================================================
# 5. Run the pipeline
# ================================================================
# Replace 'YourVolumeName' with the name of your loaded distance map volume
volumeNode = slicer.util.getNode('YourVolumeName')

modelNode = build_contours_for_volume(volumeNode, iso_value=0.0)

print("Done. Contours model:", modelNode.GetName())
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb79639ae714a731857cb0348152974c05ab96f9.png" data-download-href="/uploads/short-url/xB6ho6G4AGiztGUKAAe2ehCoyil.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb79639ae714a731857cb0348152974c05ab96f9_2_690x294.png" alt="image" data-base62-sha1="xB6ho6G4AGiztGUKAAe2ehCoyil" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb79639ae714a731857cb0348152974c05ab96f9_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb79639ae714a731857cb0348152974c05ab96f9_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb79639ae714a731857cb0348152974c05ab96f9_2_1380x588.png 2x" data-dominant-color="8F8EA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×820 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
