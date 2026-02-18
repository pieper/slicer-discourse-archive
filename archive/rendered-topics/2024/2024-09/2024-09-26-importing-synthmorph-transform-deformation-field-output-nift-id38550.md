# Importing SynthMorph transform/deformation field output (NIFTI) into 3D Slicer

**Topic ID**: 38550
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/importing-synthmorph-transform-deformation-field-output-nifti-into-3d-slicer/38550

---

## Post #1 by @andy97 (2024-09-26 03:01 UTC)

<p>Hi,</p>
<p>I am using SynthMorph via ‘mri_synthmorph’ command from Freesurfer to get the transform (deformation field) from image registration:</p>
<pre><code class="lang-auto">mri_synthmorph -m joint -t def.nii.gz moving.nii.gz fixed.nii.gz
</code></pre>
<p>when I use this ‘def.nii.gz’ file to transform the ‘moving.nii.gz’ using FreeSurfer’s ‘mri_convert’ command, it works as intended. However, when I try importing the file into 3D Slicer as a ‘Transform’, it does not work.</p>
<p>I have tried fixing the intent code and reshaping of the file as per:</p>
<ul>
<li><a href="https://github.com/voxelmorph/voxelmorph/issues/438" class="inline-onebox" rel="noopener nofollow ugc">Aligning warp field output to ANTs SyN registration · Issue #438 · voxelmorph/voxelmorph · GitHub</a></li>
</ul>
<p>This removes the intent error but does not solve the problem. I get a very weird artifact (shown in attachment).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6120ab639207267fb5d7c1ff3449a49804a24626.jpeg" data-download-href="/uploads/short-url/dRej8BdBQwudgHyMvCz6wsMN30y.jpeg?dl=1" title="Screenshot 2024-09-26 at 10.58.28 am" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6120ab639207267fb5d7c1ff3449a49804a24626_2_689x493.jpeg" alt="Screenshot 2024-09-26 at 10.58.28 am" data-base62-sha1="dRej8BdBQwudgHyMvCz6wsMN30y" width="689" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6120ab639207267fb5d7c1ff3449a49804a24626_2_689x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6120ab639207267fb5d7c1ff3449a49804a24626_2_1033x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6120ab639207267fb5d7c1ff3449a49804a24626.jpeg 2x" data-dominant-color="7B6377"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-26 at 10.58.28 am</span><span class="informations">1206×862 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to correctly import the transform output from SynthMorph into 3D Slicer?</p>
<p>Kind regards</p>
<p>Andy</p>
<p>*additional header info ‘def.nii.gz’:</p>
<blockquote>
<p>Shape: (256, 256, 256, 3)<br>
&lt;class ‘nibabel.nifti1.Nifti1Header’&gt; object, endian=‘&lt;’<br>
sizeof_hdr      : 348<br>
data_type       : np.bytes_(b’‘)<br>
db_name         : np.bytes_(b’‘)<br>
extents         : 0<br>
session_error   : 0<br>
regular         : np.bytes_(b’‘)<br>
dim_info        : 0<br>
dim             : [  4 256 256 256   3   1   1   1]<br>
intent_p1       : 0.0<br>
intent_p2       : 0.0<br>
intent_p3       : 0.0<br>
intent_code     : none<br>
datatype        : float32<br>
bitpix          : 32<br>
slice_start     : 0<br>
pixdim          : [-1.  1.  1.  1.  1.  1.  1.  1.]<br>
vox_offset      : 0.0<br>
scl_slope       : nan<br>
scl_inter       : nan<br>
slice_end       : 0<br>
slice_code      : unknown<br>
xyzt_units      : 10<br>
cal_max         : 0.0<br>
cal_min         : 0.0<br>
slice_duration  : 0.0<br>
toffset         : 0.0<br>
glmax           : 0<br>
glmin           : 0<br>
descrip         : np.bytes_(b’‘)<br>
aux_file        : np.bytes_(b’‘)<br>
qform_code      : scanner<br>
sform_code      : scanner<br>
quatern_b       : 0.0<br>
quatern_c       : -0.70710677<br>
quatern_d       : 0.70710677<br>
qoffset_x       : 127.5<br>
qoffset_y       : -127.5<br>
qoffset_z       : 127.5<br>
srow_x          : [ -1.   -0.   -0.  127.5]<br>
srow_y          : [  -0.    -0.     1.  -127.5]<br>
srow_z          : [  0.   -1.    0.  127.5]<br>
intent_name     : np.bytes_(b’‘)<br>
magic           : np.bytes_(b’n+1’)</p>
</blockquote>

---

## Post #2 by @pieper (2024-09-27 13:08 UTC)

<p>I don’t think anyone has worked on this exact transform, but it should be possible to make it work with some coding.  Basically a grid transform in Slicer is just a vector field in space where each vector tells how to map from a source image to a target image.  the sampling grid is defined by the origin, directions, spacing, and dimensions of the grid transform’s image data.  You can easily inspect this by getting the data as numpy arrays and you can use transform visualization options in Slicer to view them.  To address the SynthMorph import you just need to understand the conventions they have used to represent the nifti file and map those into what Slicer expects.</p>
<p>There are several conventions that can be used to represent nonlinear transforms, and you just need to figure out which are used by SynthMorph.  Maybe start by applying a known translation to sample data, run the registration, and inspect the resulting transform file.</p>

---

## Post #3 by @lassoan (2024-09-27 14:41 UTC)

<p>I’ve implemented displacement field storage in 4D NIFTI files in ITK and Slicer and it should work well, as long as the displacement field file is valid.</p>
<aside class="quote no-group" data-username="andy97" data-post="1" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andy97/48/18487_2.png" class="avatar"> andy97:</div>
<blockquote>
<p>when I try importing the file into 3D Slicer as a ‘Transform’, it does not work</p>
</blockquote>
</aside>
<p>What do you mean by “does not work”? What did you do, what did you expect to happen, and what happened instead?</p>
<aside class="quote no-group" data-username="andy97" data-post="1" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andy97/48/18487_2.png" class="avatar"> andy97:</div>
<blockquote>
<p>This removes the intent error but does not solve the problem. I get a very weird artifact (shown in attachment).</p>
</blockquote>
</aside>
<p>I don’t see any artifacts, it is a color image.</p>
<p>A 4D array may be interpreted as an RGB color image, so if you chose “Volume” when you loaded the data then this is the correct behavior (it would be nice to select “Transform” by default when you load a displacement field, but I don’t think it is implemented yet).</p>
<p>If you choose “Transform” in the “Add data” window then the file will be loaded as a displacement field transform.</p>
<p>One suspicious thing in the file header that you shared is that image orientation is specified with both sform and qform. Is that intentional? What are the image origin, spacing, axis directions of this image in RAS space? What does Volumes module / Volume information section show?</p>
<p>It is easy to create an incorrect file (intent field may be wrong, some software might write the vector values in voxel space, etc.), so check all details and report any problems to the developers of the software that created the incorrect field. If you believe that the file is correct then please share a set of data files (upload somewhere and post the link here) and I’ll have a look.</p>
<p>You may also choose to use NRRD format instead, which does not suffer from many of the issues and ambiguities of NIFTI files.</p>

---

## Post #4 by @lassoan (2024-09-27 18:46 UTC)

<aside class="quote no-group" data-username="andy97" data-post="1" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andy97/48/18487_2.png" class="avatar"> andy97:</div>
<blockquote>
<p>dim : [ 4 256 256 256 3 1 1 1]</p>
</blockquote>
</aside>
<p>Most likely the violation of the NIFTI file format in your file header that prevents loading into Slicer is that the dimensions are incorrect. Dimensions are hardcoded in NIFTI. 4th dimension is always time: it is set to 3 in your file (correct value for a 3D displacement field is 1). 5th dimension is the dimensionality of the displacement vector: it is set to 1 in your header (correct value is 3 see<br>
<a href="https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/group__NIFTI1__INTENT__CODES.html">here</a>: <code>dim[5] must be the dimensionality of the displacment vector (e.g., 3 for spatial displacement...</code>)</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it would be nice to select “Transform” by default when you load a displacement field, but I don’t think it is implemented yet</p>
</blockquote>
</aside>
<p>I’ve implemented this now - <a href="https://github.com/Slicer/Slicer/pull/7967">pull request submitted</a>.</p>

---

## Post #5 by @JASON (2024-09-27 19:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it would be nice to select “Transform” by default when you load a displacement field, but I don’t think it is implemented yet</p>
</blockquote>
</aside>
<p>+1 on this comment <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @andy97 (2024-10-07 05:40 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for looking into this. I managed to fix the issue following your suggestions.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>You can easily inspect this by getting the data as numpy arrays and you can use transform visualization options in Slicer to view them. To address the SynthMorph import you just need to understand the conventions they have used to represent the nifti file and map those into what Slicer expects.</p>
</blockquote>
</aside>
<p>I cross-checked the NIFTI header of a deformation field that was produced in 3D Slicer with the one produced by SynthMorph and found that the dimensions were different. I reshaped the SynthMorph NIFTI output to match the one produced by 3D Slicer and this worked.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I don’t see any artifacts, it is a color image.</p>
</blockquote>
</aside>
<p>Sorry, I used the wrong terminology. Usually when I import a displacement field as an image, I see a faint outline of how the image gets deformed. Additionally, when I hover over the voxels, I can read the vector. In this case, it did not look like this and the output when hovering over the voxels is only a scalar. But as you mentioned above, it has to do with the dimensions of the NIFTI file.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38550">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Most likely the violation of the NIFTI file format in your file header that prevents loading into Slicer is that the dimensions are incorrect. Dimensions are hardcoded in NIFTI. 4th dimension is always time: it is set to 3 in your file (correct value for a 3D displacement field is 1). 5th dimension is the dimensionality of the displacement vector: it is set to 1 in your header (correct value is 3 see<br>
<a href="https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/group__NIFTI1__INTENT__CODES.html" rel="noopener nofollow ugc">here</a>: <code>dim[5] must be the dimensionality of the displacment vector (e.g., 3 for spatial displacement...</code>)</p>
</blockquote>
</aside>
<p>I updated the header with the correct dimensions which fixed the problem!</p>

---

## Post #7 by @pieper (2024-10-07 12:25 UTC)

<p>Thanks for working through this <a class="mention" href="/u/andy97">@andy97</a> and letting us know.</p>
<p>If SynthMorph / mri_convert create and support this kind of nifti file maybe it should be considered a “standard” variant and our reader should try to detect that and work with the files the way they are produced.</p>
<p>Or do we think this is a bug in SynthMorph and that it was meant to be producing “standard” deformation files?  If you’re not sure we could contact the SynthMorph/Freesurfer team to clarify.</p>

---

## Post #8 by @lassoan (2024-10-07 15:21 UTC)

<p>Yes, these are bugs in VoxelMorph. We described the exact steps (even provided Python code) to fix the standard violations in this issue: <a href="https://github.com/voxelmorph/voxelmorph/issues/438" class="inline-onebox">Aligning warp field output to ANTs SyN registration · Issue #438 · voxelmorph/voxelmorph · GitHub</a></p>
<p><a class="mention" href="/u/andy97">@andy97</a> please add a comment to this issue that summarizes your findings. If many people will ask for the fix then that might motivate the developers.</p>

---
