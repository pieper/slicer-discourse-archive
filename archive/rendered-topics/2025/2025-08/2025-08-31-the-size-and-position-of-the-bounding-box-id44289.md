# The size and position of the bounding box

**Topic ID**: 44289
**Date**: 2025-08-31
**URL**: https://discourse.slicer.org/t/the-size-and-position-of-the-bounding-box/44289

---

## Post #1 by @Konstantin (2025-08-31 11:22 UTC)

<p>Hello. How can I make the position and dimensions of the bounding box like the 3D model?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee3e0df38656e6ff02d977c47fb3e40e1aa85d04.png" data-download-href="/uploads/short-url/xZAAwyk20zxdk7jyyr0fsQ3usOU.png?dl=1" title="bounding box" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3e0df38656e6ff02d977c47fb3e40e1aa85d04_2_690x363.png" alt="bounding box" data-base62-sha1="xZAAwyk20zxdk7jyyr0fsQ3usOU" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3e0df38656e6ff02d977c47fb3e40e1aa85d04_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3e0df38656e6ff02d977c47fb3e40e1aa85d04_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee3e0df38656e6ff02d977c47fb3e40e1aa85d04_2_1380x726.png 2x" data-dominant-color="C4C2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bounding box</span><span class="informations">1911×1008 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-09-01 09:14 UTC)

<p>I asked the AI to write me such a script, and it works (I tried it):</p>
<pre><code class="lang-auto">import vtk
import slicer

def createBoundingBoxModel(inputModelNode, boundingBoxModelName="BoundingBox"):
    """
    Create a model node that represents the bounding box of the input model.
    
    Args:
        inputModelNode: The model node whose bounding box to visualize
        boundingBoxModelName: Name for the new bounding box model node
        
    Returns:
        The created bounding box model node
    """
    if not inputModelNode or not inputModelNode.GetPolyData():
        raise ValueError("Invalid input model node")
    
    # Get bounding box of the input model
    bounds = inputModelNode.GetPolyData().GetBounds()
    # bounds = [xmin, xmax, ymin, ymax, zmin, zmax]
    
    # Create a cube source with the bounding box dimensions
    cubeSource = vtk.vtkCubeSource()
    cubeSource.SetBounds(bounds)
    cubeSource.Update()
    
    # Alternative approach: Create cube and transform it
    # center = [(bounds[0] + bounds[1])/2, (bounds[2] + bounds[3])/2, (bounds[4] + bounds[5])/2]
    # size = [bounds[1] - bounds[0], bounds[3] - bounds[2], bounds[5] - bounds[4]]
    # cubeSource.SetCenter(center)
    # cubeSource.SetXLength(size[0])
    # cubeSource.SetYLength(size[1])
    # cubeSource.SetZLength(size[2])
    
    # Create a new model node for the bounding box
    boundingBoxModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", boundingBoxModelName)
    boundingBoxModelNode.SetAndObservePolyData(cubeSource.GetOutput())
    
    # Create display node to make it visible
    boundingBoxModelNode.CreateDefaultDisplayNodes()
    displayNode = boundingBoxModelNode.GetDisplayNode()
    
    # Configure display properties for wireframe representation
    displayNode.SetRepresentation(displayNode.WireframeRepresentation)
    displayNode.SetColor(1.0, 1.0, 0.0)  # Yellow color
    displayNode.SetLineWidth(2)
    displayNode.SetOpacity(0.8)
    
    return boundingBoxModelNode
</code></pre>

---
