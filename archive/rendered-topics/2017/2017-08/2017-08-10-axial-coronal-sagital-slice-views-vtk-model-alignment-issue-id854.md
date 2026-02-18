# AXIAL, CORONAL, SAGITAL, Slice Views - VTK model alignment Issue

**Topic ID**: 854
**Date**: 2017-08-10
**URL**: https://discourse.slicer.org/t/axial-coronal-sagital-slice-views-vtk-model-alignment-issue/854

---

## Post #1 by @kitlu_s (2017-08-10 14:47 UTC)

<p>Hello,</p>
<p>Trying to load test.nrrd which consists of 3 slice views and 3d model test.vtk in 3d view which is developed using threejs. Issue when I am loading nrrd( 3 slices) file bone structure is not matching with vtk model(Extracted Bone part , Threshold is 187) . Both NRRD and VTK model generated from Slicer python script .  I am using the viewer(threejs) from this link Referer link : <a href="https://threejs.org/examples/webgl_loader_nrrd.html" rel="nofollow noopener">https://threejs.org/examples/webgl_loader_nrrd.html</a></p>
<p>Let me know is there I am doing anything wrong while loading or any other parameters I have to capture from slicer to make the both nrrd and vtk alignment perfect. How the nrrd slice bone structure alignment exactly matches with vtk model when we enable slice view in 3d View in Slicer? How to check this what parameters are required?</p>
<p>I am new to this coordinate system and orientation part of the slicer. Please suggest any solution for this I will go through that .</p>
<p>Thanks,<br>
Kitlu</p>

---

## Post #2 by @pieper (2017-08-10 16:31 UTC)

<p>Hi -</p>
<p>Did you read this info:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>Slicer saves vtk files in RAS patient space in mm.  The nrrd header has information about how the voxels are mapped to patient space.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @kitlu_s (2017-08-11 04:37 UTC)

<p>Hi Pieper,</p>
<p>I have gone through that link but I am unable to do that while loading nrrd<br>
and vtk in 3d view. I understood but unable to implement . Can you help on<br>
this topic?</p>

---

## Post #4 by @kitlu_s (2017-08-11 04:39 UTC)

<p>Hi Pieper,</p>
<p>I observed one more thing. Even I create both nrrd and vtk files from<br>
slicer then these 2 files orientations bone structure matches when I save<br>
these files and load in another viewer then it is not matching.</p>

---

## Post #5 by @pieper (2017-08-11 13:47 UTC)

<p>Hi -</p>
<p>Not sure what your other viewer is doing, but probably it ignores the index to physical transform of the nrrd files.</p>
<p>You could have a look at  <a href="http://slicedrop.com/">http://slicedrop.com/</a> which is able to correctly load a nrrd file and an stl file generated from Slicer.</p>
<p>Hope that helps,<br>
Steve</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/279e393471f0ea8e2d1048aa3cde41738eee5b29.jpeg" data-download-href="/uploads/short-url/5EtC2rFXed57kzihMXYSc0eIXMt.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/279e393471f0ea8e2d1048aa3cde41738eee5b29_2_690x404.jpg" alt="image" data-base62-sha1="5EtC2rFXed57kzihMXYSc0eIXMt" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/279e393471f0ea8e2d1048aa3cde41738eee5b29_2_690x404.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/279e393471f0ea8e2d1048aa3cde41738eee5b29_2_1035x606.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/279e393471f0ea8e2d1048aa3cde41738eee5b29_2_1380x808.jpg 2x" data-dominant-color="4B4C55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2258×1323 553 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @kitlu_s (2017-08-17 12:10 UTC)

<p>Hi Pieper,</p>
<p>Thankyou for suggesting the different viewer. Tried this but unable to view<br>
the 3d model , it is loading only nrrd but not vtk file.</p>
<p>Can you please explain me in detail about physical tranform index in nrrd<br>
file?So that I can try out some modifications in current viewer.</p>
<p>I am using teem library to check the nrrd details. Using this command :<br>
unu head nrrdfile. But this command gives basic details like (Space, Size,<br>
type, space directions, space origin, endian, encoding, ).</p>
<p>Is it possible to capture the position of bone structure on nrrd file? If<br>
not let me know is there any other way to get the details while generating<br>
nrrd file from python so that I can use these details to generate VTK file.</p>
<p>Let me know if it is not clear.</p>

---

## Post #7 by @pieper (2017-08-17 13:32 UTC)

<p>Hi Kitlu -</p>
<p>The <a href="http://slicedrop.com">slicedrop.com</a> site accepts stl files, so if you save your model in that format from Slicer 3D along with the nrrd file.  You can look open the stl file in a text editor and see the coordinate values in patient space.</p>
<p>The nrrd documentation explains how to go from pixel coordinates into physical space.</p>
<p><a href="http://teem.sourceforge.net/nrrd/format.html#space" class="onebox" target="_blank">http://teem.sourceforge.net/nrrd/format.html#space</a></p>
<p>This should give you everything you need, together with the Slicer coordinate systems wiki page linked above.  Also using the DataProbe in Slicer to interactively see the pixel (IJK) and physical (RAS) coordinates of various structures in your data can help you understand what is going on.</p>
<p>Hope that helps,<br>
Steve</p>

---
