---
topic_id: 1382
title: "Import Point Cloud Data"
date: 2017-11-05
url: https://discourse.slicer.org/t/1382
---

# Import point cloud data

**Topic ID**: 1382
**Date**: 2017-11-05
**URL**: https://discourse.slicer.org/t/import-point-cloud-data/1382

---

## Post #1 by @Hamburgerfinger (2017-11-05 06:21 UTC)

<p>I have image data in point cloud format (4 columns: x,y,z,intensity).  How can I import this volume, or convert it to a format I can import into Slicer?</p>
<p>Any help would be most appreciated!</p>

---

## Post #2 by @lassoan (2017-11-05 15:32 UTC)

<p>Can you update the software that writes the file to use a standard file format that VTK understands - such as .vtk or .vtp?</p>
<p>For example a .vtk file that contains point coordinates, normals, and a custom scalar (RandomPointScalars) looks like this:</p>
<pre><code># vtk DataFile Version 4.0
vtk output
ASCII
DATASET POLYDATA
POINTS 10 float
15 20 55 15 20 5 36.6506 20 42.5 
36.6506 20 17.5 15 41.6506 42.5 15 41.6506 17.5 
-6.65064 20 42.5 -6.65064 20 17.5 15 -1.65064 42.5 
15 -1.65064 17.5 
POLYGONS 16 64
3 2 4 0 
3 4 6 0 
3 6 8 0 
3 8 2 0 
3 3 1 5 
3 5 1 7 
3 7 1 9 
3 9 1 3 
3 2 3 5 
3 2 5 4 
3 4 5 7 
3 4 7 6 
3 6 7 9 
3 6 9 8 
3 8 9 3 
3 8 3 2 

POINT_DATA 10
SCALARS RandomPointScalars double
LOOKUP_TABLE default
59.2003 48.7194 47.505 35.9199 76.0935 74.2874 67.639 79.0812 38.1966 
40.449 
NORMALS Normals float
0 0 1 0 0 -1 0.866025 0 0.5 
0.866025 0 -0.5 5.30288e-017 0.866025 0.5 5.30288e-017 0.866025 -0.5 
-0.866025 1.06058e-016 0.5 -0.866025 1.06058e-016 -0.5 -1.59086e-016 -0.866025 0.5 
-1.59086e-016 -0.866025 -0.5</code></pre>

---

## Post #3 by @Hamburgerfinger (2017-11-05 15:56 UTC)

<p>Yes; it’s actually data that’s processed in Paraview (voxel data as a rectilinear grid).  I can export it from Paraview as .vtk, .vtu, and so on, but once I import that into Slicer, it becomes a “model” with no signal information, and I would like it to import it as a “volume” so I can use Gaussian blur, segmentation, etc.</p>
<p>Best,<br>
Luke</p>

---

## Post #4 by @lassoan (2017-11-05 17:45 UTC)

<p>If you have a surface mesh then you can load it into Slicer as a model and import as a segment using Segmentations module. To edit in Segment Editor, you need to select a Master volume to define image resolution and axes. If you don’t have any volume then load any of the sample volumes and resize&amp;resample using Crop volume module.</p>

---

## Post #5 by @lassoan (2017-11-05 18:03 UTC)

<p>If you have volumetric mesh in Paraview, then convert it to an image using <code>Resample to image</code> filter and save it as a Meta Image (.mha or .mhd) file.</p>
<p>Note that in general Slicer is much better suited for medical image analysis, processing, and visualization than Paraview, as Slicer is primarily developed for this purpose, while Paraview’s main strength is visualization and processing of large meshes. Let us know if there is any Paraview feature that you would like to use and don’t find in Slicer.</p>

---

## Post #6 by @Hamburgerfinger (2017-11-05 21:17 UTC)

<p>Can I “resample a model to image” in Slicer?  Doing so works in Paraview, but saving the result as a .mhd causes Paraview v5.4 to crash, on both Mac and PC.</p>
<p>The main issue I’m still having with Slicer is that I can’t (or don’t know how to) use the Gaussian blur module in Slicer if my data is imported as a model  (the Gaussian blur module with volume data works perfectly).</p>
<p>Alternatively, I’ve tried the “Gaussian resampling” filter in Paraview, but the blurring parameters aren’t well described in the GUI/documentation, particularly for how the input parameters relate to sigma, as used in Slicer.</p>
<p>I really appreciate all your help with this!</p>

---

## Post #7 by @lassoan (2017-11-05 22:13 UTC)

<p>Can you describe what you would like to do overall? Most likely you can do everything in Slicer and then you don’t have to worry about these conversions (Slicer can probably do all processing that you need while keeping your data as image or segmentation).</p>

---

## Post #8 by @Hamburgerfinger (2017-11-05 23:01 UTC)

<p>Sure; the program I’m using creates voxel data output as cells in a .vtk rectilinear grid.  For example:</p>
<h1>vtk DataFile Version 3.0</h1>
<p>vtk_output<br>
ASCII<br>
DATASET RECTILINEAR_GRID<br>
DIMENSIONS  51 101 41<br>
X_COORDINATES 51 float<br>
-2.0000E+00 -1.9200E+00 -1.8400E+00 …<br>
Y_COORDINATES 101 float<br>
-4.5000E+00 -4.4100E+00 -4.3200E+00 …<br>
Z_COORDINATES 41 float<br>
-1.5000E+00 -1.4250E+00 -1.3500E+00 …</p>
<p>CELL_DATA 200000<br>
FIELD FieldData 3<br>
all 1 200000 float<br>
0.0000E+00  0.0000E+00  0.0000E+00  …</p>
<p>Specifically, I want to apply a Gaussian blur to the volume, to simulate the same data imaged at different resolutions.</p>
<p>You’re absolutely right, I can ideally do everything I need to do in Slicer.  With “normal” image volumes, e.g. DICOM files, I just import as a “volume” and can use the Gaussian blur module to blur the image.  However, the problem here, is that since my present data is generated at the source as a .vtk file, I can’t seem to import it as a “volume”.  Slicer recognizes it only as a “model”.  And the Gaussian blur module in Slicer doesn’t allow one to select a “model” as input.</p>

---

## Post #9 by @lassoan (2017-11-05 23:45 UTC)

<aside class="quote no-group" data-username="Hamburgerfinger" data-post="8" data-topic="1382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar"> Hamburgerfinger:</div>
<blockquote>
<p>the program I’m using creates voxel data output as cells in a .vtk rectilinear grid</p>
</blockquote>
</aside>
<p>Maybe you could fix that program then. A vtk rectilinear grid is not a volume (vtkImageData), as in a rectilinear grid, spacing along each axis may vary arbitrarily, while in a volume, spacing along each axis is constant. If that programs wants to write a volume then it should create a .vtk file that has <code>DATASET STRUCTURED_POINTS</code> inside.</p>
<p>Even better, use .nrrd or .mha file format instead. The problem with .vtk image files is that they cannot store axis orientation (it is assumed that IJK image axes are aligned with XYZ physical axes, which is often not true in medical images).</p>

---

## Post #10 by @Hamburgerfinger (2017-11-06 15:57 UTC)

<p>Unfortunately I’m not a programmer.  But, I can save my file as vtkImageData in Paraview, but it still won’t import as a volume into Slicer.  For example:</p>

  
  
    
      
        0 0 0 0 0 0
        0 0 0 0 0 0
...
<p>Isn’t this the same as “structured points”?</p>

---

## Post #12 by @lassoan (2017-11-06 16:20 UTC)

<p>What software generates that file that contains the volume as.vtk rectilinear grid? Is there a particular reason why that software does not save the volume as an image (.vtk file with DATASET STRUCTURED_POINTS inside; .vti file; .nrrd or .mha file…)?</p>
<p>You should be able to convert volumetric mesh (such as rectilinear grid) of a model node to vtkImageData of a volume node in Slicer, using <a href="https://www.vtk.org/doc/nightly/html/classvtkProbeFilter.html">vtkProbeFilter</a>, but that requires writing 10-15 lines of Python script.</p>

---

## Post #13 by @Hamburgerfinger (2017-11-06 19:44 UTC)

<p>Its a monte carlo code called PHITS.  It’s advantageous sometimes in MC simulations to use a nonuniform grid size, for example in order to optimize counting statistics in a particular direction, or region of the mesh.</p>
<p>I can convert to .vti, but Slicer isn’t importing my .vti files.</p>
<p>Additionally I’ve saved it as a structured point dataset (below is the header info from my file) but it also won’t import my structured point .vtk into Slicer as a volume.  Do you see any errors or incompatibility here?</p>
<h1>vtk DataFile Version 4.1</h1>
<p>vtk output<br>
ASCII<br>
DATASET STRUCTURED_POINTS<br>
DIMENSIONS 52 116 39<br>
SPACING 0.0784314 0.0782609 0.0789474<br>
ORIGIN -2 -4.5 -1.5<br>
CELL_DATA 222870<br>
FIELD FieldData 1<br>
vtkGhostType 1 222870 unsigned_char<br>
0 0 0 0 0 0 0 0 0<br>
…</p>

---

## Post #14 by @lassoan (2017-11-06 20:02 UTC)

<p>To load volume from VTK file, in the “Add data” dialog choose Volume instead of Model.</p>

---

## Post #15 by @Hamburgerfinger (2017-11-06 20:17 UTC)

<p>Could I send you the file?  I’ve tried this on both Mac and PC, and it won’t load.  It loads into Paraview as an image, but not into Slicer.</p>

---

## Post #16 by @lassoan (2017-11-06 23:31 UTC)

<p>Yes, having an example file would help a lot. You can upload it to dropbox, onedrive, gdrive, etc. and post the link here.</p>

---

## Post #17 by @Hamburgerfinger (2017-11-08 17:00 UTC)

<p>Perfect, thanks!</p>
<p>The .vti file is here:</p>
<p><a href="https://drive.google.com/open?id=1sryack8W_0iYvbwzniu_S7tYgYqATIg7" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1sryack8W_0iYvbwzniu_S7tYgYqATIg7</a></p>
<p>The .vtk file is here:</p>
<p><a href="https://drive.google.com/open?id=1qBVl7VNlQcfXOoXsacJCswV9S74iep5Q" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1qBVl7VNlQcfXOoXsacJCswV9S74iep5Q</a></p>
<p>When attempting to load in the GUI, nothing happens, and when doing so with the Python interactor, it returns (False, None).</p>

---

## Post #18 by @lassoan (2017-11-08 18:26 UTC)

<p>Slicer could not load the .vtk file, as no SCALAR data was specified for point data. You can load the data manually using the Python console like this:</p>
<pre><code># Read data set
reader=vtk.vtkStructuredPointsReader()
reader.SetFileName("test14.vtk")
reader.Update()
img=reader.GetOutput()
# Set active point scalar attribute
img.GetPointData().SetActiveAttribute("all",vtk.vtkDataSetAttributes.SCALARS)
# Convert to volume node
volumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
spacing = img.GetSpacing()
origin = img.GetOrigin()
img.SetSpacing(1,1,1)
img.SetOrigin(0,0,0)
volumeNode.SetAndObserveImageData(img)
volumeNode.SetSpacing(spacing)
volumeNode.SetOrigin(origin)
# Show in slice views
volumeNode.CreateDefaultDisplayNodes()
slicer.util.setSliceViewerLayers(background=volumeNode)</code></pre>

---

## Post #19 by @Hamburgerfinger (2017-11-08 22:31 UTC)

<p>This works perfectly!!!</p>
<p>Thanks so much!!<br>
Luke</p>

---

## Post #20 by @lassoan (2021-12-22 03:40 UTC)

<p>A post was split to a new topic: <a href="/t/convert-point-cloud-to-surface-model/21175">Convert point cloud to surface model</a></p>

---

## Post #21 by @lassoan (2023-07-29 14:57 UTC)

<p>A post was split to a new topic: <a href="/t/import-point-cloud/30867">Import point cloud</a></p>

---
