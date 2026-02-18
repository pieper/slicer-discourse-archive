# Show displacement matrix and log file during image registration

**Topic ID**: 28675
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/show-displacement-matrix-and-log-file-during-image-registration/28675

---

## Post #1 by @Laura.K (2023-03-30 08:58 UTC)

<p>Hi everyone,</p>
<p>I created a BSpline-transformation with the module General Registration (BRAINS) with a CT-image as fixed volume and an MR-image as moving volume. Visualization of the BSpline coefficients and conversion to a displacement field is possible with transforms module.</p>
<p>For further investigation on the occurring displacements I would like to get the 3D distortion matrix with displacement vectors for every voxel in mm. Is there an access to the matrix in 3D-Slicer (e.g. to localize and to get the value and direction of the maximum distortion-vector in every layer)? I already tried to export the data to Matlab and OriginPro, but I only get a table with one column.</p>
<p>Furthermore I would like to take a look at the algorithm. In Elastix module there is a way to display the log files during registration. Is it possible to get a detailed log in General Registration (BRAINS) module? I tried to generate a log file report under debugging parameters, but there wasn’t any data in my CSV-file.</p>

---

## Post #2 by @pieper (2023-03-30 14:30 UTC)

<p>It sounds like you are almost there.  In the Transforms module there’s a Convert section where you can create a grid transform within a selected reference grid (defined by a volume).  The grid transform is the displacement vectors in mm and you can use <code>arrayFromGridTransform</code> to access them for analysis.</p>
<p>For the BRAINSFit logging information you can add <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/brainsfit.html#debugging-parameters">some command line arguments to get extra debug info</a>.  You can get the starting command line from the Slicer log and then run it extra debug parameters.  Best to look at the BRAINSFit source code for to interpret this.</p>

---

## Post #3 by @Laura.K (2023-04-05 12:35 UTC)

<p>Thank you for your help.</p>
<p>I managed to get the array from the output displacement field (stored as transform node) with “arrayFromGridTransform”. But I have difficulties in interpreting the matrix. I guess the 3 columns stand for the x-, y-, and z-component of each displacement-vector in LPS coordinate system. Which of the values represent the location of the base of each arrow? Aside from that I don’t know how to get the complete Matrix without “…,” as replacement.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d966e12a8ba05a18871d0251c8c0926278cd8c8.png" data-download-href="/uploads/short-url/kcxCjPzov61TneBNidH1nDDxGys.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d966e12a8ba05a18871d0251c8c0926278cd8c8.png" alt="image" data-base62-sha1="kcxCjPzov61TneBNidH1nDDxGys" width="300" height="499" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">578×961 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is an image section of the output matrix. The part in blue brackets is repeated six times with other values.</p>

---

## Post #4 by @pieper (2023-04-05 14:05 UTC)

<p>Yes, these are the displacement vectors, but they are in RAS not LPS.  The “…” is just to shorten the string for printing; all the values are there in the array.  The start point of each arrow is defined by the position of the vector in the 3D volumetric grid.  The locations of these start points are calculated based on the origin, spacing, and directions like in an image volume, but the API is a little different.  The tip of the arrow would be the base plus the displacement vector.</p>
<p>For another project I created these helper functions that I plan to add to <code>slicer.util</code> at some point.  You may find them useful for reference to see the relationship between grid transforms and volumes.  I believe they are correct but maybe you can test them and let me know if they work for you.  <code>addVolumeFromGridTransform</code> is helpful for debugging because you can get a color image (VectorVolume) that shows the space covered by the grid transform and you can mouse over the image to see the displacement values in the DataProbe.</p>
<pre><code class="lang-auto">def addGridTransformFromArray(narray, referenceVolume=None, name=None):
    """Create a new grid transform node from content of a numpy array and add it to the scene.
    Displacement values are deep-copied, therefore if the numpy array
    is modified after calling this method, voxel values in the volume node will not change.
    :param narray: numpy array containing grid transform vectors (shape should be [Nk, Nj, Ni, 3], i.e. one displacement vector for slice, row, column location).
    :param referenceVolume: a vtkMRMLVolumeNode or subclass to define the directions, origin, and spacing
    :param name: grid transform node name
    :return: created new grid transform node
    Example::
      # create an identity grid transform
      import numpy
      gridTransformNode = slicer.util.addGridTransformFromArray(numpy.zeros((30, 40, 50, 3)))
    """
    import slicer
    from vtk import vtkMatrix4x4
    from vtk.util import numpy_support

    gridTransformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLGridTransformNode")
    if name is not None:
        gridTransformNode.SetName(name)
    gridTransform = gridTransformNode.GetTransformFromParent()
    gridImage = vtk.vtkImageData()
    gridImage.SetDimensions(tuple(reversed(narray.shape[:3])))
    gridType = numpy_support.get_vtk_array_type(narray.dtype)
    gridImage.AllocateScalars(gridType, 3)
    if referenceVolume is not None:
        gridDirectionMatrix = vtk.vtkMatrix4x4()
        referenceVolume.GetIJKToRASDirectionMatrix(gridDirectionMatrix)
        gridTransform.SetGridDirectionMatrix(gridDirectionMatrix)
        gridImage.SetOrigin(referenceVolume.GetOrigin())
        gridImage.SetSpacing(referenceVolume.GetSpacing())
    gridTransform.SetDisplacementGridData(gridImage)
    transformArray = slicer.util.arrayFromGridTransform(gridTransformNode)
    transformArray[:] = narray
    slicer.util.arrayFromGridTransformModified(gridTransformNode)

    return gridTransformNode

def addVolumeFromGridTransform(gridTransformNode, name=None):
    """Create a new vector volume from grid transform node from content.
    :param gridTransformNode: source transform
    :param name: created volume node name
    :return: created new volume
    """
    displacements = arrayFromGridTransform(gridTransformNode)
    gridTransform = gridTransformNode.GetTransformFromParent()
    gridDirectionMatrix = gridTransform.GetGridDirectionMatrix()
    displacementGrid = gridTransform.GetDisplacementGrid()
    scratchVolume = slicer.vtkMRMLScalarVolumeNode()
    scratchVolume.SetIJKToRASDirectionMatrix(gridDirectionMatrix)
    scratchVolume.SetSpacing(displacementGrid.GetSpacing())
    scratchVolume.SetOrigin(displacementGrid.GetOrigin())
    ijkToRAS = vtk.vtkMatrix4x4()
    scratchVolume.GetIJKToRASMatrix(ijkToRAS)
    return addVolumeFromArray(displacements, ijkToRAS=ijkToRAS, name=name, nodeClassName="vtkMRMLVectorVolumeNode")
</code></pre>

---
