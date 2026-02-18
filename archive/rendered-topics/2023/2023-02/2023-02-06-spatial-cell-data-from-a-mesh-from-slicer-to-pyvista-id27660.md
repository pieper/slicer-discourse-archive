# "Spatial Cell Data" from a mesh: from Slicer to Pyvista

**Topic ID**: 27660
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/spatial-cell-data-from-a-mesh-from-slicer-to-pyvista/27660

---

## Post #1 by @luke90 (2023-02-06 13:47 UTC)

<p>I exported a Cartesian 4D echo images by Philips QLAB and I converted them using the module [Philips 4D US DICOM patcher]. Then I exported the US volume in a nrrd file into Pyvista for 3D analysis. Reading the mesh (UniformGrid) I observed it reported the ‘Spatial Point Data’ but not the ‘Spatial Cell Data’ that is basically the intensity of each voxel. I just wondering how 3D Slicer can read and show the pixel/voxel intensity from the nrrd file. Where is the intensity value of each cell of the mesh stored, so that maybe i can retrieve using Pyvista.Thanks in advance for the help</p>
<p>UniformGrid (0x26b6e7bc288)<br>
N Cells:	8078175<br>
N Points:	8200192<br>
X Bounds:	0.000e+00, 2.060e+02<br>
Y Bounds:	0.000e+00, 2.007e+02<br>
Z Bounds:	0.000e+00, 1.610e+02<br>
Dimensions:	224, 176, 208<br>
Spacing:	9.237e-01, 1.147e+00, 7.777e-01<br>
N Arrays:	1</p>
<p>mesh.point_data<br>
Out[118]:<br>
pyvista DataSetAttributes<br>
Association     : POINT<br>
Active Scalars  : ImageFile<br>
Active Vectors  : None<br>
Active Texture  : None<br>
Active Normals  : None<br>
Contains arrays :<br>
ImageFile               uint8      (8200192,)           SCALARS</p>
<p>mesh.cell_data<br>
Out[119]:<br>
pyvista DataSetAttributes<br>
Association     : CELL<br>
Active Scalars  : None<br>
Active Vectors  : None<br>
Active Texture  : None<br>
Active Normals  : None<br>
Contains arrays : None</p>

---

## Post #2 by @lassoan (2023-02-06 14:07 UTC)

<p>NRRD file stores a voxel array, so it is not a mesh, but an image (<a href="https://vtk.org/doc/nightly/html/classvtkImageData.html">vtkImageData</a>). To get a mesh, you need to segment the image.</p>
<p>I don’t know why the image shows up for you as <a href="https://vtk.org/doc/nightly/html/classvtkUniformGrid.html">vtkUniformGrid</a>, which is a specialized, more complex kind of image data. If you load the data using Pyvista then probably that’s the culprit - it may do this to allow some special visualization techniques - but using this special class instead of vtkImageData may lead to problems if you attempt to use this data for any processing.</p>
<p>Pyvista is a convenience layer on top of VTK to make <em>visualization</em> easier. I’m not sure if it makes <em>processing</em> easier, as the convenience layer hides lots of VTK features and may introduce additional complexities. <strong>What kind of 3D analysis would you like to do?</strong></p>
<p>We’ve been working with cardiac ultrasound image processing and visualization for many years, so if you tell us a bit about what you want to achieve then we can give you advice on potential approaches. <strong>What is your overall goal?</strong></p>

---

## Post #3 by @luke90 (2023-02-06 22:20 UTC)

<p>Thanks Andras for the information. Quick and very kind in response. Thanks again.<br>
Given a 3D ultrasound image (a volume), I need to extract one or more slices (2D image as array) along a selected vector. This vector, depending how the volume was acquired, can be in any direction in the space. To define the vector, I need to select two marker (points) in the space. Then, starting from the first selected point, I need to extract a slice along the defined vector at a certain distance from that point (in mm). Example I select 1mm, and 10 slices, so every 1mm from the first point, a slice would be extracted for a total of 10 slices. All these operations should be done in automatic for an AI application. Using 3Dslicer and the Valve View tool in the cardiac package (thanks Andras for this package it’s amazing it looks like a mini version of tomtec) I can set the two long axis and the short axis to visualize the plane that contains the aortic valve. Of course the two long axis are not perpendicular to each other as normally set in 3DSlicer but should be set manually by an operator. Then along the short axis the two marker points can be selected.<br>
Using a deep learning model I would like to extract the coordinate of the two marker, in order to then make what I explained above, thus extrapolating the slices along the vector direction perpendicularly. The slices then will be segmented, but this is a pretty easy for me. I need to resolve the problem of how to extract the slices as array along a vector in the 3D space.<br>
Following the example in pyvista (<a href="https://docs.pyvista.org/examples/01-filter/slicing.html" class="inline-onebox" rel="noopener nofollow ugc">Slicing — PyVista 0.38.1 documentation</a>) and the function (<a href="https://github.com/pyvista/pyvista-support/issues/89" class="inline-onebox" rel="noopener nofollow ugc">Transform slice() output to 2D numpy array · Issue #89 · pyvista/pyvista-support · GitHub</a>) to convert a slice in a 2D numpy array (even if it does not seem to work properly). I should probably fix it. Unfortunately, the nrrd file imported into pyvista that is converted to a mesh (UniformGrid) does not contain cell information. Even if I export the 3D eco image as a vtk file, it is read as UniformGrid in Pyvista. Basically in Pyvista the two files are seen in the same way.  The only difference I found was that the nrrd file is exported and then read by 3DSlicer, while the vtk file is exported but then no longer read by 3DSlicer (- Error: Failed to load model from VTK file F:****. vtk as it does not contain polydata nor unstructured grid. The file might be loadable as a volume.</p>
<ul>
<li>Error: Loading F:/****. vtk - Failed to read node US_2 (vtkMRMLModelNode7) from filename='F:*****. vtk).<br>
I hope I’ve been clear enough. In case I try to be even more detailed.</li>
</ul>

---

## Post #4 by @lassoan (2023-02-07 14:05 UTC)

<p>What would you like to extract using deep learning? The annulus curve, specific landmark points along the annulus, leaflets, papillary muscles, …?</p>

---

## Post #5 by @luke90 (2023-02-07 18:52 UTC)

<p>Just to understand what I have to do by making it automatic: <a href="https://www.youtube.com/watch?v=0dMgpYDWxPw" class="inline-onebox" rel="noopener nofollow ugc">How to assess the Aortic root dimensions by 3D-TEE (Q-lab) - YouTube</a><br>
using deep learning first specific landmark points along defined long axis, and then the area of the annulus in a plane perpendicular to the resulting short axis. The problem is that I cannot simply train a model to segment a surface in the US volume as this might lead to the classic overfitting problem. Of course I can generate a ROI (and this is what I plan to do) but it doesn’t solve the problem.</p>

---
