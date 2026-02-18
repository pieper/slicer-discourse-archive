# Volume Rendering Issues

**Topic ID**: 2513
**Date**: 2018-04-04
**URL**: https://discourse.slicer.org/t/volume-rendering-issues/2513

---

## Post #1 by @ckuzi001 (2018-04-04 21:26 UTC)

<p>Hello everyone,</p>
<p>I am trying to programmatically render a volume of a tumor in Python using the VolumeRendering class.  There are four features (labels 1-4) that should each be associated with a unique color.  I used a slightly modified version of the parametricVolumeProperty() function from the ShaderComputation module (ttps://github.com/pieper/CommonGL/blob/master/ShaderComputation/ShaderComputation.py) in order to obtain the color transfer function and apply it to a display node, however, the result is relatively low quality and only two features are colored correctly.  Is there an alternate way to accomplish this?  Or is there an error in my implementation of these classes?  Any assistance would be greatly appreciated.  Thank you!</p>
<p>~ Carrie Kuzio</p>
<hr>
<p>Link to GitHub repository: <a href="https://github.com/visionlabodu/SlicerBrainTumorSegmentation" rel="noopener nofollow ugc">https://github.com/visionlabodu/SlicerBrainTumorSegmentation</a></p>
<hr>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f1ef8b2e52d8d5d3ac51269f42e05493ad04a81.png" alt="Slicer_Screenshot" data-base62-sha1="29Lw7KHBJfaZ74d06ew99twPAGZ" width="654" height="420"></p>
<hr>
<p>The relevant functions are copied below:</p>
<pre><code>def render_volume(self, image_shape, output_array, output_volume=None, ret=False):
    """Render the prediction volume
    """
    # Create output volume
    if output_volume is None:  # Check for existing file
        output_volume = slicer.mrmlScene.AddNewNodeByClass(  # Add new node
            "vtkMRMLScalarVolumeNode")
        output_volume.SetName("outputVolume")  # Set name for output volume
        output_volume.CreateDefaultDisplayNodes()  

    # Update volume from prediction
    image_data = vtk.vtkImageData()  
    image_data.SetDimensions(image_shape)  
    image_data.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, 1)  
    output_volume.SetAndObserveImageData(image_data)
    slicer.util.updateVolumeFromArray(output_volume, output_array)

    # Create a volume property node
    volumePropertyNode = slicer.vtkMRMLVolumePropertyNode()
    volumePropertyNode.SetName(output_volume.GetName() + '-VP')

    # Create functions for gradient and scalar opacity of the volume property node
    scalarOpacity = vtk.vtkPiecewiseFunction()  
    volumePropertyNode.SetScalarOpacity(scalarOpacity)
    gradientOpacity = vtk.vtkPiecewiseFunction()
    volumePropertyNode.SetGradientOpacity(gradientOpacity)
    slicer.mrmlScene.AddNode(volumePropertyNode)  # Add the node to scene

    # Create the display node and give it the volume property
    displayNode = slicer.vtkMRMLGPURayCastVolumeRenderingDisplayNode()
    displayNode.SetName(output_volume.GetName() + '-VR')
    displayNode.SetRaycastTechnique(0)

    displayNode.SetAndObserveVolumePropertyNodeID(volumePropertyNode.GetID())
    displayNode.SetVisibility(1)        
    displayNode.SetAndObserveVolumeNodeID(output_volume.GetID())
    slicer.mrmlScene.AddNode(displayNode)  # Add the display node to scene
    output_volume.AddAndObserveDisplayNodeID(displayNode.GetID())

    # Call function to create the color, gradient, and opacity transfer functions
    self.parametricVolumeProperty(output_volume, displayNode)

    if ret is not False:
        return output_volume


def parametricVolumeProperty(self, volumeNode, displayNode, color_maps=None):
    """Guess the transfer function based on the volume data
    See https://github.com/pieper/CommonGL/blob/master/ShaderComputation/ShaderComputation.py
    """

    # Create default color map
    if color_maps is None:  
        color_maps = {"necrosis": (.847, .749, .847),
                      "edema": (.549, .8784, .8941),
                      "non-enhanced": (0.721, 0.670, 0.929),
                      "enhanced": (0.686, 0.929, 0.670)}

    # Create the volume property node
    volumePropertyNode = slicer.util.getNode(displayNode.GetVolumePropertyNodeID())

    # Create the scalar range for scalar and gradient opacity
    scalarRange = volumeNode.GetImageData().GetScalarRange()
    rangeWidth = scalarRange[1] - scalarRange[0]
    rangeCenter = scalarRange[0] + rangeWidth * 0.5

    # Set the scalar opacity
    scalarOpacityPoints = ((scalarRange[0], 0.),
                           (rangeCenter - 0.1 * rangeWidth, 0.),
                           (rangeCenter + 0.1 * rangeWidth, 1.),
                           (scalarRange[1], 1.))

    scalarOpacity = volumePropertyNode.GetScalarOpacity()

    # Add scalar opacity points to volume property node scalar opacity
    for point in scalarOpacityPoints:
        scalarOpacity.AddPoint(*point)

    # Set the gradient opacity
    gradientOpacityPoints = (
            (0, .2),
            (rangeCenter - 0.1 * rangeWidth, .4),
            (rangeCenter - 0.09 * rangeWidth, 1.),
            (rangeCenter + 0.09 * rangeWidth, 1.),
            (rangeCenter + 0.1 * rangeWidth, 1.),
            (scalarRange[1], .7) )

    gradientOpacity = volumePropertyNode.GetGradientOpacity()

    # Add gradient opacity points to volume property node gradient opacity
    for point in gradientOpacityPoints:
      gradientOpacity.AddPoint(*point)

    # Assign intensity to corresponding color from color map to create color transfer function
    colorPoints = ((1, color_maps["necrosis"]),
                   (2, color_maps["edema"]),
                   (3, color_maps["non-enhanced"]),
                   (4, color_maps["enhanced"]))

    colorTransfer = volumePropertyNode.GetColor()

    # Add color transfer function volume property node 
    for intensity, rgb in colorPoints:
        colorTransfer.AddRGBPoint(intensity, *rgb)

    volumePropertyNode.SetColor(colorTransfer)
</code></pre>

---

## Post #2 by @brhoom (2018-04-04 21:45 UTC)

<p>why not using labelmap or segmentation to visualize the features? I think it is much easier.</p>

---

## Post #3 by @lassoan (2018-04-06 05:40 UTC)

<p>I don’t think you can easily get nice volumetric visualization from binary labelmaps using a single volume renderer.</p>
<p>If you use discrete labelmaps then you will have hard boundaries that look as bad or worse than generating isosurfaces. Segmentations module can already quite nicely visualize segments using isosurfaces, with optional surface smoothing - so most likely it produces nicer visualization.</p>
<p>If you are considering using a range of values for each segment so that you can have smooth edges then you’ll have artifacts at segment boundaries (if you try to use a single volume renderer). Segmentations infrastructure supports storage and some editing operations on fractional labelmaps, so you can have segments with smooth edges, and there are no issues at segment boundaries, since each segment is stored in a separate labelmap.</p>
<p>Volume rendering of multiple overlapping volumes is just being introduced to VTK. If that becomes available, then we’ll expose it in Slicer, too. <a class="mention" href="/u/cpinter">@cpinter</a> has already started implementing this for rendering of scalar volumes. If everything works well then we’ll make it available for segmentations, too.</p>
<p>If you are considering using volume rendering because of faster 3D visualization update, we have good news, too. We are evaluating switching of VTK’s SMP backend to TBB, which allows much faster labelmap-&gt;surface conversion (using flying edges method). In many cases, this will make updates of 3D models from labelmaps almost instantaneous.</p>
<p>Overall, I would recommend to test what you can do with segmentations. If that’s not good enough then wait at least for multi-volume rendering in VTK and implement visualization by using a separate renderer for each segment. You may also choose to just wait until someone else implements volume rendering based visualization for segmentations. If you want to take an active role in the process, then there would be at least two ways you could add a lot of value:</p>
<ol>
<li>Implement volume rendering based visualization of segmentations in segmentation displayable manager classes (instead of waiting for someone else to implement it). Probably you need less code than implementing from scratch; and the result could be made available for all Slicer users.  We can help you to get started.</li>
<li>Add custom shaders to volume renderer to display binary labelmaps as smooth surfaces (to eliminate staircase artifacts). We can achieve this by applying Gaussian smoothing on the image volume, but it would be better to avoid applying filtering on the entire volume and instead send the unmodified image volume to the GPU and perform smoothing or jittering on the fly.</li>
</ol>

---
