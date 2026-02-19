---
topic_id: 33287
title: "Textured Model Question"
date: 2023-12-07
url: https://discourse.slicer.org/t/33287
---

# Textured model question

**Topic ID**: 33287
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/textured-model-question/33287

---

## Post #1 by @agporto (2023-12-07 16:08 UTC)

<p>Let’s suppose I have a textured model and that I want to segment the model using color information to calculate area measurements (for simplicity, let’s say I want to calculate the area of a model that is the color red). Is there any way to do so that doesn’t involve using the UV mapping of the Texture Model module (which is quite slow for high resolution models)? For example, I can easily perform segmentation in the image itself and generate an image that makes certain regions of the object transparent. Is there a way to calculate the visible area of a 3d model on Slicer? Any alternative suggestions ?<br>
Thanks</p>

---

## Post #2 by @tsehrhardt (2023-12-07 19:48 UTC)

<p>In Meshlab with per vertex and per face color, you can select by specific colors and even set a range and preview the selection, move the selection to another layer, then run stats on the new layer like area, volume, etc. I have not tried it with textured models.</p>

---

## Post #3 by @agporto (2023-12-07 20:42 UTC)

<p>Yeah, that makes sense. I am actually trying to avoid the UV mapping step because the meshes in question have a few million vertices and the process seems really slow (at least when I try the Texture Model extension option of outputting RGB values). If I can get away with not having to map, that would be ideal. Also, I was interested as having this work within Slicer, if I can.</p>

---

## Post #4 by @pieper (2023-12-07 20:48 UTC)

<p>I think the best way to address what you describe would be to implement something in a GPU shader if you’re up for that sort of thing.</p>

---

## Post #5 by @agporto (2023-12-07 22:15 UTC)

<p>That is an interesting suggestion, Steve. Though it would come with the downside of relying on GPUs. Need to explore GPU shaders a bit. Thanks!</p>

---

## Post #6 by @pieper (2023-12-07 22:21 UTC)

<p>Yes, relying on a GPU solution can be problematic, but if you need large models with complex texture access, that is exactly what they are made for.  But of course they come with lots of complexity.  I’ve been interested in <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerWGPU/">this approach</a> for a while and I think it’s a nice tradeoff between complexity and power (although it comes with a fair amount of both, I think power can win out).</p>

---

## Post #7 by @tsehrhardt (2023-12-08 18:22 UTC)

<p>I would not uv map a mesh with millions of vertices. Even with photogrammetry, the texture map would be made directly from the photos not the mesh. Since Slicer shows the vertex color as a scalar, I would think it should be accessible to filter/separate.</p>

---

## Post #8 by @agporto (2023-12-08 18:34 UTC)

<p>Hi Terrie. Thanks for continuing engaging on this. Could you point me towards the filter/separate functionality?</p>

---

## Post #9 by @tsehrhardt (2023-12-08 18:38 UTC)

<p>The function in Meshlab?</p>

---

## Post #10 by @agporto (2023-12-08 18:40 UTC)

<p>I thought you meant Slicer. Got it, thanks!</p>

---

## Post #11 by @agporto (2023-12-09 05:46 UTC)

<p>For future reference, I ended up solving my issue by modifying the source code of the Texture Model extension (Slicer IGT) to do a much faster UV mapping using vectorized operations in numpy (rather than the vtk for loops). <a class="mention" href="/u/lassoan">@lassoan</a> Is there a reason to keep the Texture Model operations in pure vtk instead of numpy?  If not, would you be interested in a pull request?</p>
<pre><code class="lang-auto">  def convertTextureToPointAttribute(self, modelNode, textureImageNode, saveAsPointData):
    """
    Map texture image colors to vertex points of a mesh.

    :param modelNode: VTK model node containing the mesh.
    :param textureImageNode: VTK image node containing the texture.
    :param saveAsPointData: How to save the point data ('uchar-vector', 'float-vector', 'float-components').
    """
    import vtk.util.numpy_support as vtk_np
    import numpy as np

    # Retrieve polydata from the model node
    polyData = modelNode.GetPolyData()
    
    # Retrieve texture coordinates from the polydata
    tcoords_vtk = polyData.GetPointData().GetTCoords()
    tcoords_np = vtk_np.vtk_to_numpy(tcoords_vtk)

    # Flip texture image vertically
    textureImageFlipVert = vtk.vtkImageFlip()
    textureImageFlipVert.SetFilteredAxis(1)
    textureImageFlipVert.SetInputConnection(textureImageNode.GetImageDataConnection())
    textureImageFlipVert.Update()
    textureImageData = textureImageFlipVert.GetOutput()
    
    # Convert texture image to NumPy array
    textureImage_np = vtk_np.vtk_to_numpy(textureImageData.GetPointData().GetScalars()).reshape(
        textureImageData.GetDimensions()[1], textureImageData.GetDimensions()[0], -1)

    # Normalize and scale texture coordinates
    print("Original Texture Coordinates: ", tcoords_np)

    # Scale the texture coordinates
    # Ensure that you're using the correct image dimensions
    width, height = textureImage_np.shape[1], textureImage_np.shape[0]
    uv_scaled = np.clip(tcoords_np, 0, 1) * [width - 1, height - 1]

    print("Scaled UV Coordinates: ", uv_scaled)

    # Map texture coordinates to texture colors (vectorized operation)
    colors = textureImage_np[uv_scaled[:, 1].astype(int), uv_scaled[:, 0].astype(int)]

    # Convert results back to VTK and save as point data
    if saveAsPointData == 'uchar-vector':
        colorArray_vtk = vtk_np.numpy_to_vtk(colors, deep=True, array_type=vtk.VTK_UNSIGNED_CHAR)
        colorArray_vtk.SetName('RGB')
        polyData.GetPointData().SetScalars(colorArray_vtk)
    elif saveAsPointData == 'float-vector':
        colorArray_vtk = vtk_np.numpy_to_vtk(colors.astype(float) / 255.0, deep=True, array_type=vtk.VTK_FLOAT)
        colorArray_vtk.SetName('Color')
        polyData.GetPointData().SetScalars(colorArray_vtk)
    elif saveAsPointData == 'float-components':
        for i, name in enumerate(['ColorRed', 'ColorGreen', 'ColorBlue']):
            componentArray_vtk = vtk_np.numpy_to_vtk(colors[:, i].astype(float), deep=True, array_type=vtk.VTK_FLOAT)
            componentArray_vtk.SetName(name)
            polyData.GetPointData().AddArray(componentArray_vtk)
    else:
        raise ValueError(f"Invalid saveAsPointData: {saveAsPointData}")

    # Mark the polydata as modified
    polyData.Modified()```</code></pre>

---

## Post #12 by @lassoan (2023-12-10 04:12 UTC)

<p>The extension was created by a student with not a lot of experience with VTK or Slicer and it worked well enough, so we added to the extension, but of course it makes more sense to use numpy to perform these vector operations. It would be great if you could submit a pull request!</p>

---

## Post #13 by @agporto (2023-12-10 04:30 UTC)

<p>Makes sense. I’ve submitted the pull request. Thanks, Andras.</p>

---
