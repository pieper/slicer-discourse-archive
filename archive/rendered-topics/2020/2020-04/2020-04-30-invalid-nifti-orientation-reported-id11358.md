# Invalid NIFTI Orientation Reported

**Topic ID**: 11358
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/invalid-nifti-orientation-reported/11358

---

## Post #1 by @Vincent_Magnotta (2020-04-30 01:52 UTC)

<p>Operating system: Mac<br>
Slicer version: Slicer 4.10.0<br>
Expected behavior: 4D NIFTI images load with an expected orientation of [1 0 0][0 1 0] [0 0 1]. If I concatenate multiple 3D datasets together and load the resulting the file the image orientation is reported as [-1 0 0][0 -1 0] [0 0 1]. I have verified the orientation with nifti_tool and found that it reports the same orientation between the two datasets.<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-04-30 01:54 UTC)

<p>Slicer uses RAS coordinate system internally, so if your input IJK to LPS matrix was <code>[1 0 0][0 1 0] [0 0 1]</code> then in Slice the IJK to RAS matrix is expected to be <code>[-1 0 0][0 -1 0] [0 0 1]</code>. Therefore, what you see may not be a problem.</p>
<p>How did you load the 4D Nifti file?<br>
What is the 4th dimension? Time?</p>

---

## Post #3 by @pieper (2020-04-30 12:28 UTC)

<p>There’s been <a href="https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157">a lot of discussion</a> of this topic.</p>
<p>I took a shot at fixing the <a href="https://github.com/fedorov/MultiVolumeImporter/commit/13436f7e663b35e7116363de0ac537d02db79c61">MultiVolume Importer</a> a few years ago and found it impossible to pin down any real standard for 4D nifti, but made things work for the files on the nifti web site.  Beyond that I tend to throw up my hands and consider any other files application-specific and not interoperable.</p>
<p><a class="mention" href="/u/vincent_magnotta">@Vincent_Magnotta</a> if you can make the case that there is a valid definition of 4D nifti that will allow true interoperability then for sure we would want Slicer to read and write those correctly, ideally via ITK.  Things may have changed, but nfortunately last time I looked there was no such definition. Even <a href="https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157">3D nifti has some issues</a>.</p>

---

## Post #4 by @Vincent_Magnotta (2020-04-30 13:07 UTC)

<p>The example that I have is from a project that is using NIFTI for handling fNIRS data. The data I am working with would be more similar to DTI data than fMRI data. A very simple example is that I take a 3D NIFTI image and simply run the<br>
3dTcat command from afni that will concatenate two images together into a 4D image file. If I take the same image and concatenate the image with itself I end up with a NIFTI image that has the same NIFTI sform and qform transforms in the header. However, if<br>
I load the 3D and 4D versions of the file into Slicer, the 3D image loads correctly and the 4D version that is loaded in a different orientation.</p>
<p>I can appreciate that NIFTI does not a great way to specify spatial and other dimensions of the data, but currently Slicer seems to at least interpret which dimensions are spatial relative to other dimensions. I would have expected that<br>
the 3D and 4D versions would have had the same orientation and not be flipped relative to one another.</p>

---

## Post #5 by @pieper (2020-04-30 14:06 UTC)

<p>I agree, it’s frustrating for everyone.</p>
<p>Does it load correctly in ITK?</p>

---

## Post #6 by @Vincent_Magnotta (2020-04-30 14:44 UTC)

<p>I did not try loading directly into an ITK image, but ITKSnap does load both images correctly and the results overlap as I would expected.</p>

---

## Post #7 by @lassoan (2020-04-30 14:48 UTC)

<p>While investigating this orientation issue, you can apply an appropriate transformation matrix to fix the image after loading is completed; or you can use nrrd file format instead.</p>
<p>What is the 4th dimension in your data? Would you like to visualize it as a time sequence, a vector field, or just display a selected component? Would you like to process it? Using Segment Editor, or do some spatial registration, deformation, or process it using your own scripts using ITK/VTK/numpy,… ?</p>

---

## Post #8 by @pieper (2020-04-30 15:00 UTC)

<p><a class="mention" href="/u/vincent_magnotta">@Vincent_Magnotta</a> can you post example data along with screen captures of what you think is the correct interpretation?  Also can you provide links to the various apps you mention that generated the data along with the parameters you used.  Sorry if this sounds super picky, but we’ve chased a lot of nifti orientation issues over the years and as I said earlier there is no clear standard for correctness.</p>

---

## Post #9 by @Vincent_Magnotta (2020-04-30 18:00 UTC)

<p>Steve,</p>
<p>Totally understand the issues here. Happy to post some data. What is the preferred method to share? I am attaching a screenshot showing what I would expect the result to be and where the 4D image results when loaded. I am also attaching<br>
the output of using nifti_tool to show the image headers.</p>
<p>For this I am using matlab and the associated NIFTI library to write the images files using the save_nii function. I then take a 3D image and concatenate it with itself to generate the 4D image,  example command</p>
<p>3dTcat AdotVol_3d.nii AdotVol_3d.nii -prefix AdotVol_4d.nii</p>
<p>Output of <strong>nifti_tool</strong></p>
<p>N-1 header file ‘headvol.nii’, num_fields = 43</p>
<p>all fields:</p>
<p>name<br>
offset<br>
nvals  values</p>
<hr>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e80e6a0f7753408c949a4bded8d2398ce9804355.jpeg" data-download-href="/uploads/short-url/x6REEgtTPY5Gy8CC0ydfUsnemFf.jpeg?dl=1" title="Slicer-3dOverlay.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80e6a0f7753408c949a4bded8d2398ce9804355_2_512x500.jpeg" alt="Slicer-3dOverlay.jpg" data-base62-sha1="x6REEgtTPY5Gy8CC0ydfUsnemFf" width="512" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80e6a0f7753408c949a4bded8d2398ce9804355_2_512x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80e6a0f7753408c949a4bded8d2398ce9804355_2_768x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80e6a0f7753408c949a4bded8d2398ce9804355_2_1024x1000.jpeg 2x" data-dominant-color="3F3E4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-3dOverlay.jpg</span><span class="informations">1656×1616 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66221c332e80086445f381472f06af3d36056bd4.jpeg" data-download-href="/uploads/short-url/ezvMwxisKPPwLwsCOymL3e3lC4Y.jpeg?dl=1" title="Slicer-4dOverlay.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66221c332e80086445f381472f06af3d36056bd4_2_407x500.jpeg" alt="Slicer-4dOverlay.jpg" data-base62-sha1="ezvMwxisKPPwLwsCOymL3e3lC4Y" width="407" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66221c332e80086445f381472f06af3d36056bd4_2_407x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66221c332e80086445f381472f06af3d36056bd4_2_610x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66221c332e80086445f381472f06af3d36056bd4_2_814x1000.jpeg 2x" data-dominant-color="35353E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-4dOverlay.jpg</span><span class="informations">1320×1618 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2020-04-30 18:36 UTC)

<aside class="quote no-group" data-username="Vincent_Magnotta" data-post="9" data-topic="11358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_magnotta/48/6730_2.png" class="avatar"> Vincent_Magnotta:</div>
<blockquote>
<p>What is the preferred method to share?</p>
</blockquote>
</aside>
<p>It could be google drive, onedrive, dropbox or whatever you think is most convenient.</p>
<p>And what method do you use to load them in Slicer?   Which version of Slicer?</p>

---

## Post #11 by @lassoan (2020-04-30 18:38 UTC)

<p>Another option, if you just use nifti to pass images between Matlab and Slicer to write 3D/4D nrrd files using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a>. NRRD files do not suffer from image orientation ambiguities and both 3D and 4D data sets are loaded consistently into Slicer.</p>
<p>What is the 4th dimension in your data? Would you like to visualize it as a time sequence, a vector field, or just display a selected component? Would you like to process it? Using Segment Editor, or do some spatial registration, deformation, or process it using your own scripts using ITK/VTK/numpy,… ? – The answers to these questions are important because you can represent 4D data various ways (vector volume, scalar volume with multiple components, multi-volume, or volume sequence) and different features are available for each.</p>

---

## Post #12 by @Vincent_Magnotta (2020-04-30 19:01 UTC)

<p>Here is a link to the data.</p>
<p><a href="https://www.dropbox.com/sh/g270f3mioz4u9vq/AAAxgfjdlfukGI1CVy65F4-pa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/g270f3mioz4u9vq/AAAxgfjdlfukGI1CVy65F4-pa?dl=0</a></p>

---

## Post #13 by @Vincent_Magnotta (2020-04-30 19:06 UTC)

<p>I need these images to be in NIFTI format right now. We are working on an fNIRS pipeline that glues a lot of components together (HOMER/AtlasViewer, NeuroDot, AFNI, ANTS). I would really like to avoid conversion to another format. We have<br>
worked hard to resolve all of the file format issues between these programs and NRRD just does not have the broad adoption to support this effort.</p>

---

## Post #14 by @lassoan (2020-04-30 19:30 UTC)

<p>I fully agree, for the final solution you should be able to use any file format (and fix nifti specification and implementation wherever needed). I just recommended a workaround so you can proceed while it is being sorted out.</p>
<p>What is the 4th dimension in your data? Would you like to visualize it as a time sequence, a vector field, or just display a selected component? Would you like to process it? Using Segment Editor, or do some spatial registration, deformation, or process it using your own scripts using ITK/VTK/numpy,… ? – The answers to these questions are important because you can represent 4D data various ways (vector volume, scalar volume with multiple components, multi-volume, or volume sequence) and different features are available for each.</p>

---
