---
topic_id: 38454
title: "How To Interact With 3D Slicer From An External Python Envir"
date: 2024-09-20
url: https://discourse.slicer.org/t/38454
---

# How to interact with 3D Slicer from an external Python environment?

**Topic ID**: 38454
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/how-to-interact-with-3d-slicer-from-an-external-python-environment/38454

---

## Post #1 by @wenlin_x (2024-09-20 05:44 UTC)

<p>I have attempted to use the pyigtl and slicerio libraries, but neither was successful in displaying the three surfaces of the instrument tip in real-time within 3D Slicer. My requirement is to execute this externally, allowing modifications or displays to 3D Slicer. I can successfully achieve my needs within the Python console of 3D Slicer, but now I need to execute it externally.</p>
<p>I want to interact with the 3D Slicer environment from my Python project but I’m facing issues accessing the interfaces provided by 3D Slicer in an external environment. I would like to post a question on Stack Overflow regarding this issue. Below is the code that outlines my requirements:</p>
<pre><code class="lang-auto">import slicer
import vtk

# Replace with the name of the loaded volume node

volume_node = slicer.util.getNode('verse808_seg')

# Get the volume data extent

image_data = volume_node.GetImageData()
extent = image_data.GetExtent()
print("Volume extent:", extent)

# Replace with the coordinates of the point to use as a reference

point = \[1, 1, 1\]  # Your point coordinates

# Get the RASToIJKMatrix of the volume node

ras_to_ijk_matrix = vtk.vtkMatrix4x4()
volume_node.GetRASToIJKMatrix(ras_to_ijk_matrix)

# Convert the RAS coordinates of the point to IJK coordinates

ras_point = \[point\[0\], point\[1\], point\[2\], 1.0\]  # Add homogeneous coordinate
ijk_point = ras_to_ijk_matrix.MultiplyPoint(ras_point)\[:3\]  # Take the first three coordinates, ignoring the homogeneous coordinate

# Print the converted IJK coordinates for debugging

print("IJK Coordinates:", ijk_point)

# Check if the IJK coordinates are within the extent

if (extent\[0\] \&lt;= ijk_point\[0\] \&lt;= extent\[1\] and
extent\[2\] \&lt;= ijk_point\[1\] \&lt;= extent\[3\] and
extent\[4\] \&lt;= ijk_point\[2\] \&lt;= extent\[5\]):
print("IJK point is within the volume extent.")

    # Create a fiducial node and add control points (using fiducials instead)
    fiducial_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'F')
    fiducial_node.AddControlPoint(ras_point[0], ras_point[1], ras_point[2])
    
    # Update display
    slicer.app.processEvents()
    
    # Get slice nodes
    slice_node_red = slicer.util.getNode('vtkMRMLSliceNodeRed')
    slice_node_yellow = slicer.util.getNode('vtkMRMLSliceNodeYellow')
    slice_node_green = slicer.util.getNode('vtkMRMLSliceNodeGreen')
    
    # Get slice logic
    red_logic = slicer.app.layoutManager().sliceWidget('Red').sliceLogic()
    yellow_logic = slicer.app.layoutManager().sliceWidget('Yellow').sliceLogic()
    green_logic = slicer.app.layoutManager().sliceWidget('Green').sliceLogic()
    
    # Set slice positions and force update the display
    slice_node_red.SetSliceOffset(ras_point[2])      # Z slice
    slice_node_yellow.SetSliceOffset(ras_point[0])   # X slice
    slice_node_green.SetSliceOffset(ras_point[1])    # Y slice
    slicer.app.processEvents()
    
    # Print debugging information
    print("Red slice offset:", slice_node_red.GetSliceOffset())
    print("Yellow slice offset:", slice_node_yellow.GetSliceOffset())
    print("Green slice offset:", slice_node_green.GetSliceOffset())
    
    # Lock slice views to prevent auto-reset
    red_composite_node = red_logic.GetSliceCompositeNode()
    yellow_composite_node = yellow_logic.GetSliceCompositeNode()
    green_composite_node = green_logic.GetSliceCompositeNode()
    
    red_composite_node.SetLinkedControl(False)
    yellow_composite_node.SetLinkedControl(False)
    green_composite_node.SetLinkedControl(False)
    
    # Force refresh the view
    slicer.app.processEvents()
    
    # Add event listeners to ensure slice positions do not reset
    def onSliceNodeModified(caller, event):
        slice_node_red.SetSliceOffset(ras_point[2])      # Z slice
        slice_node_yellow.SetSliceOffset(ras_point[0])   # X slice
        slice_node_green.SetSliceOffset(ras_point[1])    # Y slice
        slicer.app.processEvents()
    
    slice_node_red.AddObserver(vtk.vtkCommand.ModifiedEvent, onSliceNodeModified)
    slice_node_yellow.AddObserver(vtk.vtkCommand.ModifiedEvent, onSliceNodeModified)
    slice_node_green.AddObserver(vtk.vtkCommand.ModifiedEvent, onSliceNodeModified)
    
    # Force refresh the view again
    slicer.app.processEvents()

else:
print("Error: Point is outside the volume extent.")
</code></pre>
<p>I can successfully achieve my needs within the Python console of 3D Slicer, but now I need to execute it externally.</p>

---

## Post #2 by @lassoan (2024-09-20 05:49 UTC)

<p>You probably don’t need to do any programming. Instead, you can drive slices by a transform by configuring <code>Volume Reslice Driver</code> module (in <code>SlicerIGT</code> extension) and set up all other visualization options that you need, then save the scene in a single .mrb file.</p>
<p>To start navigation, you can start Slicer and load the scene (using <code>slicerio</code> python package) and send the reslicing transform via OpenIGTLink (using <code>pyigtl</code> python package).</p>

---

## Post #3 by @wenlin_x (2024-09-20 07:13 UTC)

<p>Thank you very much for your professional response. I have located the Volume Reslice Driver within the IGT framework and have configured it to display the necessary faces, as shown in the figure. However, I am not clear about the phrase “end the reslicing transform via OpenIGTLink (using the pyigtl python package).” What I am trying to achieve is depicted in the figure: I have placed two surgical instruments into 3D Slicer (the real-time position matrix of the instruments is transmitted via OpenIGTLink). My goal is to display the three faces of the spine at the tip of the needle when it is placed on the spine and to continuously display the sections I need throughout the entire surgical procedure.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9c504420edb7e612d6ce90b659e4d13e8591f6.jpeg" data-download-href="/uploads/short-url/flXZlPX2xupENXbZoOaacCLsoOG.jpeg?dl=1" title="20240920150139" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9c504420edb7e612d6ce90b659e4d13e8591f6_2_690x364.jpeg" alt="20240920150139" data-base62-sha1="flXZlPX2xupENXbZoOaacCLsoOG" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9c504420edb7e612d6ce90b659e4d13e8591f6_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9c504420edb7e612d6ce90b659e4d13e8591f6_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9c504420edb7e612d6ce90b659e4d13e8591f6_2_1380x728.jpeg 2x" data-dominant-color="77777D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240920150139</span><span class="informations">1912×1011 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d25c8d4e6fdfc2640f34227a23b610f7fbf73eb.jpeg" data-download-href="/uploads/short-url/b0tIwwLcoajWbFKeEbxbABPZ4E3.jpeg?dl=1" title="20240920150150" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d25c8d4e6fdfc2640f34227a23b610f7fbf73eb_2_690x360.jpeg" alt="20240920150150" data-base62-sha1="b0tIwwLcoajWbFKeEbxbABPZ4E3" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d25c8d4e6fdfc2640f34227a23b610f7fbf73eb_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d25c8d4e6fdfc2640f34227a23b610f7fbf73eb_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d25c8d4e6fdfc2640f34227a23b610f7fbf73eb_2_1380x720.jpeg 2x" data-dominant-color="75757A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240920150150</span><span class="informations">1920×1003 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-09-21 02:51 UTC)

<aside class="quote no-group" data-username="wenlin_x" data-post="3" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>However, I am not clear about the phrase “end the reslicing transform via OpenIGTLink (using the pyigtl python package).”</p>
</blockquote>
</aside>
<p>I was recommending pyigtl only for sending transforms to Slicer from an external Python environment. If you already have a solution streaming your transform into Slicer (e.g., using PLUS) then you are good.</p>
<aside class="quote no-group" data-username="wenlin_x" data-post="3" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>My goal is to display the three faces of the spine at the tip of the needle</p>
</blockquote>
</aside>
<p>Volume Reslice Driver can do this.</p>
<aside class="quote no-group" data-username="wenlin_x" data-post="3" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>continuously display the sections I need throughout the entire surgical procedure</p>
</blockquote>
</aside>
<p>I don’t understand this part yet. How would the software know which slices you need? Would you manually move the slices (e.g., Shift + Mouse move)?</p>

---

## Post #5 by @wenlin_x (2024-09-23 01:24 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="wenlin_x" data-post="3" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>My goal is to display the three faces of the spine at the tip of the needle</p>
</blockquote>
</aside>
<p>Volume Reslice Driver can do this.</p>
</blockquote>
</aside>
<p>Thank you for your guidance.  I have been using pyigtl to transmit the spatial position matrix of the surgical instruments into 3D Slicer.  However, when I place the tip of the surgical instrument on the CT model of the spine, the desired sections are not displayed.  Are there any additional steps I need to perform?</p>
<p>Regarding the continuous display of the sections I need throughout the entire surgical procedure, the slices I need will be saved in the scene, and then imported and confirmed before surgery using slicerio or pyigtl.</p>
<p>Additionally, you previously mentioned that the Volume Reslice Driver module can provide micromotion warnings.  I would like to implement this micromotion warning during surgery.  The original plan was to mark a reference object on the human skin to achieve micromotion warning during the procedure.  I am not clear on how the Volume Reslice Driver module can achieve this.</p>

---

## Post #6 by @lassoan (2024-09-23 01:55 UTC)

<aside class="quote no-group" data-username="wenlin_x" data-post="5" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>However, when I place the tip of the surgical instrument on the CT model of the spine, the desired sections are not displayed. Are there any additional steps I need to perform?</p>
</blockquote>
</aside>
<p>Yes, you need to perform a standard tooltip calibration (typically using pivot calibration) and patient registration (usually by landmark registration). All these are described in step-by-step tutorials in <a href="https://www.slicerigt.org/wp/user-tutorials/">SlicerIGT training page</a>.</p>
<aside class="quote no-group" data-username="wenlin_x" data-post="5" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>Regarding the continuous display of the sections I need throughout the entire surgical procedure, the slices I need will be saved in the scene, and then imported and confirmed before surgery using slicerio or pyigtl.</p>
</blockquote>
</aside>
<p>The whole image volume is saved in the scene, so you don’t need to save specific slices. It is sufficient if you save a surgical plan as a transform (e.g., the ToolTipToReference transform when the tooltip is at the planned position). You can then use this transform with Volume Reslice driver to show the corresponding slices.</p>
<aside class="quote no-group" data-username="wenlin_x" data-post="5" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>Additionally, you previously mentioned that the Volume Reslice Driver module can provide micromotion warnings. I would like to implement this micromotion warning during surgery. The original plan was to mark a reference object on the human skin to achieve micromotion warning during the procedure. I am not clear on how the Volume Reslice Driver module can achieve this.</p>
</blockquote>
</aside>
<p>I’m not sure what you mean exactly by micromotion warnings. If you want to visualize small motion measured by a position tracker then Slicer provides many visualization tools for this (for example, show the original and transformed tool position in 2D and 3D views), but it is not obvious how Volume Reslice Driver would be useful for this.</p>

---

## Post #7 by @wenlin_x (2024-09-23 03:10 UTC)

<p>Thank you for your guidance and responses. I have a question regarding the 3D Slicer Volume Reslice Driver module. When displaying sections, should the ‘Driver’ be selected as ‘Transform’ or does it impact the images in some way? I have not been able to locate the ‘Transform’ option. The ‘Transform’ refers to the matrix of my surgical instrument, and I have created a ‘NeedleModel’.</p>

---

## Post #8 by @lassoan (2024-09-23 04:18 UTC)

<aside class="quote no-group" data-username="wenlin_x" data-post="7" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>When displaying sections, should the ‘Driver’ be selected as ‘Transform’ or does it impact the images in some way?</p>
</blockquote>
</aside>
<p>The driver transform determines the position and orientation of the slice view. It does not impact any other node in any way.</p>
<aside class="quote no-group" data-username="wenlin_x" data-post="7" data-topic="38454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenlin_x/48/77798_2.png" class="avatar"> wenlin_x:</div>
<blockquote>
<p>I have not been able to locate the ‘Transform’ option. The ‘Transform’ refers to the matrix of my surgical instrument, and I have created a ‘NeedleModel’.</p>
</blockquote>
</aside>
<p>This sounds good. Make sure your transform node’s class is <code>vtkMRMLLinearTransformNode</code> and then you can select it in the <code>Driver</code> combobox.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d427b5a56bc68616b1184aeb1a422c029a024f5.jpeg" data-download-href="/uploads/short-url/k9DL7zoyZUmiLVjq9ag0nT33kQl.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d427b5a56bc68616b1184aeb1a422c029a024f5_2_670x500.jpeg" alt="image" data-base62-sha1="k9DL7zoyZUmiLVjq9ag0nT33kQl" width="670" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d427b5a56bc68616b1184aeb1a422c029a024f5_2_670x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d427b5a56bc68616b1184aeb1a422c029a024f5_2_1005x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d427b5a56bc68616b1184aeb1a422c029a024f5_2_1340x1000.jpeg 2x" data-dominant-color="534B40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1496×1116 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @wenlin_x (2024-09-23 04:58 UTC)

<p>Thank you very much for your professional response. I now know what to do.</p>

---
