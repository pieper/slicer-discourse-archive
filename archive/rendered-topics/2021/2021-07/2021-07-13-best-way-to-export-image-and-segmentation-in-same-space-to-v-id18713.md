---
topic_id: 18713
title: "Best Way To Export Image And Segmentation In Same Space To V"
date: 2021-07-13
url: https://discourse.slicer.org/t/18713
---

# Best way to export image and segmentation in same space to view in ParaView?

**Topic ID**: 18713
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/best-way-to-export-image-and-segmentation-in-same-space-to-view-in-paraview/18713

---

## Post #1 by @tossin (2021-07-13 23:58 UTC)

<p>I’m sure this type of problem pops up a lot, but I couldn’t find an exact answer to my problem.</p>
<p>I have an image volume imported from a DICOM sequence which I’ve segmented first with the VMTK Extension (produces a node named “LevelSetSegmentationModel”) and then edited that segmentation with the Segment Editor (node “LevelSetSegmentationModel-segmentation”).  I want to export both of these into ParaView aligned for further postprocessing. For now in ParaView, it seems easiest to use IJK coordinates.</p>
<p>Slicer saves the image data in .nrrd format by default, which will be read into ParaView as a rectilinear grid in IJK coordinates.  I read this into ParaView and then removed the origin to have the image volume purely in IJK.  Then I tried to use the Slicer Python Interpreter to transform the segmentation from RAS to IJK coordinates, using the API documentation:</p>
<pre><code class="lang-auto"># get orientation and origin from the master volume
image = getNode('62: CE-MRA')
orientations = [[0]*3 for i in range(3)]
image.GetIJKToRASDirections(orientations)
origin = image.GetOrigin()
origin = np.array(origin)
ijk_to_ras = orientations

transform_np = np.zeros((4,4))
transform_np[:3,:3] = orientations
transform_np[:3, 3] = origin
transform_np[3,3] = 1

transform_vtk = vtk.vtkTransform()
transform_vtk.SetMatrix(ijk_to_lps_transform.flatten())
transform_vtk.Inverse()  

# retrieve the segmentation from Segment Editor node and transform it from RAS to IJK
node = getNode('LevelSetSegmentationModel-segmentation')
orientedImageData = node.GetBinaryLabelmapInternalRepresentation('LevelSetSegmentationModel')

transformF = vtk.vtkTransformFilter()
transformF.SetInputData(orientedImageData)
transformF.SetTransform(transform_vtk)
transformF.Update()
sg = transformF.GetOutput()
# --&gt; save as .vts using vtkXMLStructuredGridWriter
# use Contour Filter to extract surface in ParaView
</code></pre>
<p>This method seems to work, but has some problems:</p>
<ol>
<li>
<p>It’s convoluted.  Is there a better way to retrieve the image orientations?</p>
</li>
<li>
<p>Is there a better way to retrieve the segmentation from Segment Editor (such as in a vtkPolyData format)?  I could only retrieve a vtkOrientedImageData, and it has some issues.  For one, the contour generated from it is of much poorer quality than the surface manually exported as an STL file.  Second, the vtkOrientedImageData seems to capture the bare minimum bounding box, which leads to holes not found in the STL:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74bd1a7c92504bb17eb59c0838131900eea0a3ca.png" data-download-href="/uploads/short-url/gEIxpqGINUPY58rNI0Y5LoeJe3w.png?dl=1" title="orientedImageData vs exported STL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bd1a7c92504bb17eb59c0838131900eea0a3ca_2_690x357.png" alt="orientedImageData vs exported STL" data-base62-sha1="gEIxpqGINUPY58rNI0Y5LoeJe3w" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bd1a7c92504bb17eb59c0838131900eea0a3ca_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bd1a7c92504bb17eb59c0838131900eea0a3ca_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bd1a7c92504bb17eb59c0838131900eea0a3ca_2_1380x714.png 2x" data-dominant-color="58576D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">orientedImageData vs exported STL</span><span class="informations">1538×796 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Left side is contour from exported vtkOrientedImageData (hole outlined in blue), right side is contour from exported STL.<br>
I can get around these issues, I just wonder if I’m making things harder than they have to be.</p>
</li>
<li>
<p>Just in general, is there a better way to export images and segmentations in the coordinate system of my choice?</p>
</li>
</ol>
<p>Also, all the data is aligned in the 3D render window.  Is there some way I could access the data objects used for the visualization and save those instead?</p>

---

## Post #2 by @lassoan (2021-07-14 02:37 UTC)

<p>Paraview is awesome for meshes, but it is barely usable for medical imaging applications. First of all, last time I checked Paraview still did not support oriented images. So, if you load any DICOM image with its I axis direction not the same as the patient L axis or J axis is not the same as patient P axis then the image position and orientation will be incorrect and Paraview will just not be able to display the image in its correct location. Paraview will load meshes correctly but they will not be aligned with the image that they were derived from. Image slice and volume rendering display is also very limited compared to what you need for medical image computing.</p>
<aside class="quote no-group" data-username="tossin" data-post="1" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/258eb7/48.png" class="avatar"> tossin:</div>
<blockquote>
<p>It’s convoluted. Is there a better way to retrieve the image orientations?</p>
</blockquote>
</aside>
<p>The process that you describe is not just convoluted but it leads to incorrect results. You must have your data represented in physical space.</p>
<aside class="quote no-group" data-username="tossin" data-post="1" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/258eb7/48.png" class="avatar"> tossin:</div>
<blockquote>
<p>Is there a better way to retrieve the segmentation from Segment Editor (such as in a vtkPolyData format)?</p>
</blockquote>
</aside>
<p>Since image support in Paraview is very poor, I would recommend to export the segmentation to mesh if you want to visualize it in Paraview. What would you like to do with the segmentation data in Paraview?</p>
<aside class="quote no-group" data-username="tossin" data-post="1" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/258eb7/48.png" class="avatar"> tossin:</div>
<blockquote>
<p>the vtkOrientedImageData seems to capture the bare minimum bounding box</p>
</blockquote>
</aside>
<p>This was the default behavior in older Slicer versions, but current versions keep the original image extents (consumes more memory but we have found that it causes more confusion for users, so disabled cropping to minimum size option by default).</p>
<p>By the way, requiring a padding around image data is one of the thousands of small but annoying issues that have been fixed in Slicer over the past decades, but since Paraview’s use cases are different, these are not fixed in Paraview.</p>
<aside class="quote no-group" data-username="tossin" data-post="1" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/258eb7/48.png" class="avatar"> tossin:</div>
<blockquote>
<p>Just in general, is there a better way to export images and segmentations in the coordinate system of my choice?</p>
</blockquote>
</aside>
<p>I don’t think so. Medical imaging data support is just not a priority for Paraview developers. If you find part of your workflow that only requires meshes then you can switch to Paraview. But the inconvenience of saving, loading, viewing/processing, saving, loading is just not worth it. You can also extend and customize Slicer to make it do exactly what you need, so there is not much that you can do in Paraview that you cannot easily do in Slicer, too.</p>
<p>Is there anything that you would like to do in Paraview but not sure how to do in Slicer?</p>

---

## Post #3 by @tossin (2021-07-14 22:02 UTC)

<p>Hello Andras, thanks for the response.  I probably should have stated that I plan to use the segmentations for CFD simulations.  An example image would be:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3aeb887283d572d37ce2d17b87eaa52e222948f.jpeg" data-download-href="/uploads/short-url/ucD5cqEBZGRfRLwrU8lhwaCkNfF.jpeg?dl=1" title="04 MRA + Streamlines, WSS - Zoom 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3aeb887283d572d37ce2d17b87eaa52e222948f_2_517x267.jpeg" alt="04 MRA + Streamlines, WSS - Zoom 2" data-base62-sha1="ucD5cqEBZGRfRLwrU8lhwaCkNfF" width="517" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3aeb887283d572d37ce2d17b87eaa52e222948f_2_517x267.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3aeb887283d572d37ce2d17b87eaa52e222948f_2_775x400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3aeb887283d572d37ce2d17b87eaa52e222948f_2_1034x534.jpeg 2x" data-dominant-color="131414"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04 MRA + Streamlines, WSS - Zoom 2</span><span class="informations">3076×1592 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The above includes streamlines and WSS distributions from CFD aligned to a volumetric rendering of the imaging data.  Generally, I use standalone VMTK to segment image data, but Slicer has more features and a better interface, so I was hoping to use it for more complex cases.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The process that you describe is not just convoluted but it leads to incorrect results. You must have your data represented in physical space.</p>
</blockquote>
</aside>
<p>For my purposes, I only need the aligned data between mesh and image.  As you say, ParaView/VTK will not load DICOM data correctly, but as long as the mesh is also in the same incorrect orientation, it’s good enough.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since image support in Paraview is very poor, I would recommend to export the segmentation to mesh if you want to visualize it in Paraview. What would you like to do with the segmentation data in Paraview?</p>
</blockquote>
</aside>
<p>To be more specific, the surface mesh itself isn’t important, but it needs to be aligned with the image data so that the CFD mesh generated from it is also aligned.  I only know that you can manually export a segmentation as .stl in LPS or RAS coordinates from the Segment Editor.  The reason I tried the Python Interpreter is to transform it back to IJK in Slicer without needing a second script.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This was the default behavior in older Slicer versions, but current versions keep the original image extents (consumes more memory but we have found that it causes more confusion for users, so disabled cropping to minimum size option by default).</p>
<p>By the way, requiring a padding around image data is one of the thousands of small but annoying issues that have been fixed in Slicer over the past decades, but since Paraview’s use cases are different, these are not fixed in Paraview.</p>
</blockquote>
</aside>
<p>I appreciate the insight.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there anything that you would like to do in Paraview but not sure how to do in Slicer?</p>
</blockquote>
</aside>
<p>Probably a lot since I’m used to ParaView for the visualization of simulation results and I’m not familiar with the intricacies of Slicer at all.  Do you recommend I use Slicer for both CFD and image visualization? To be honest, I would just prefer to use Slicer for segmentations only without spending too much time learning a new postprocessing pipeline, but I am open to suggestions.</p>

---

## Post #4 by @lassoan (2021-07-14 23:22 UTC)

<p>Paraview is better for explorative visualizing of CFD results than Slicer, but only Slicer has all the tools that are required for your complete workflow (DICOM import, segmentation, rich image visualization, etc.). You could either export images in a simplified format (resampled to have image axes aligned with patient axes, etc.) and live with Paraview’s limited image visualization features; or import the CFD simulation results in to Slicer and add the visualization modes that you need in a small Python scripting module. Slicer uses the same visualization toolkit as Paraview (VTK), so most visualization features are already available in Slicer, just not exposed on the user interface.</p>
<p>What are your long term goals? Do you need tools that you use for your research or at some point you would want to have one integrated solution that others can use (potentially even clinicians)? If yes, then go all in on 3D Slicer is a good strategy. If this is only for you and you are already comfortable with using multiple applications and you don’t need to spend too much time viewing images and segmentations while looking at the CFD results then it may be simpler to use Paraview for final visualization.</p>

---
