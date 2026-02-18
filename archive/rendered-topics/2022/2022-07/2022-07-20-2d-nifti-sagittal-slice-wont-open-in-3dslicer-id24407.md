# 2D nifti sagittal slice won't open in 3DSlicer

**Topic ID**: 24407
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/2d-nifti-sagittal-slice-wont-open-in-3dslicer/24407

---

## Post #1 by @BayesMonk (2022-07-20 11:28 UTC)

<p>Hi,<br>
I have a 2D sagittal slice stored in Nifti. It won’t open in slicer and I get the following error:</p>
<blockquote>
<p>Exception thrown in event: D:\D\S\Slicer-1-build\ITK\Modules\Core\Common\include\itkImageBase.hxx:184:<br>
itk::ERROR: itk::ERROR: Image(0000026509941440): Bad direction, determinant is 0. Direction is -0 0 0 0<br>
1 -0 0 0<br>
0 0 1 0<br>
0 0 0 1</p>
</blockquote>
<p>I can perfectly open the nifti using nibabel, and I could check that the header are not corrupted.</p>
<p>I get this same error in coronal, but not when I use axial slices.</p>
<p>My guess is that slicer is cropping the affine matrix because the data are 2D. The crop is probably fine for axial orientation, but wrong in sagittal or coronal.</p>
<p>FYI, the sagittal affine matrix in my example is like:</p>
<pre><code class="lang-auto">[[   0.       ,    0.        ,    2.5999    , -135.7749939 ],
[  -0.7813    ,    0.        ,    0.        ,  100.54699707],
[   0.        ,   -0.7813    ,    0.        ,  110.85900116],
[   0.        ,    0.        ,    0.        ,    1.        ]]
</code></pre>
<p>Thanks for the help!</p>

---

## Post #2 by @lassoan (2022-07-20 12:54 UTC)

<p>Even 2D slices need a non-singular 3D direction matrix, because even if you have a single slice in your image, the orientation, position, and spacing (thickness) must be specified in the 3D space.</p>
<p>You can fix this invalid file by setting the directions for all 3 axes. You can compute the direction of the third axis of the image slice as the cross product of the direction of the first two axes.</p>

---

## Post #3 by @BayesMonk (2022-07-20 13:46 UTC)

<p>Hi Andras,<br>
I agree with you, the affine matrix should not be singular. However, as I show in my example, it is absolutely not singular if I look at it with Nibabel in Python. However, 3DSlicer reads a different affine matrix which is singular. Any clues about what cause this behavior?<br>
Thanks!</p>

---

## Post #4 by @lassoan (2022-07-20 14:24 UTC)

<p>Probably nibabel adds the missing axis, but ITK just uses what is in the file. You can ask the opinion of ITK folks on <a href="https://discourse.itk.org/">the ITK forum</a>, if they think that automatically fixing up the direction matrix is a good idea or not. But in the meantime, it is probably simpler to write the file correctly (or fix it, maybe by reading it using nibabel and writing it to a file).</p>
<p>What software created this nifti file?</p>
<p>Do you work with neuroimaging data? (if not, then I would recommend to stay away from nifti format, and use a better-behaving file format, such as nrrd)</p>

---

## Post #5 by @BayesMonk (2022-07-20 15:15 UTC)

<p>Hi,<br>
We work with breast MRI data, I agree that nifti is not optimal. However, we checked that the affine in the nifti is correct, so we cannot understand that 3DSlicer is seeing a completely different affine. Also, we tried ITK SNAP, and get the same error, so you’re right, it’s probably a good idea to ask ITK’s people.<br>
Also, in order to allow the opening of this file in Slicer, we forced the affine to be the identity matrix, hence mimicking an axial acquisition, which worked. However, this does not orient the 2D slice correctly in the 3D physical reference system, so this is not a perfect solution.</p>

---

## Post #6 by @lassoan (2022-07-20 15:17 UTC)

<aside class="quote no-group" data-username="BayesMonk" data-post="5" data-topic="24407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/ed655f/48.png" class="avatar"> BayesMonk:</div>
<blockquote>
<p>However, we checked that the affine in the nifti is correct</p>
</blockquote>
</aside>
<p>Could you copy here a text dump of the nifti header?<br>
What software created this nifti file?</p>

---

## Post #7 by @BayesMonk (2022-07-20 15:45 UTC)

<p>Here are the header:</p>
<pre><code class="lang-auto">&lt;class 'nibabel.nifti1.Nifti1Header'&gt; object, endian='&lt;'
sizeof_hdr      : 348
data_type       : b''
db_name         : b''
extents         : 0
session_error   : 0
regular         : b''
dim_info        : 0
dim             : [  2 256 256   1   1   1   1   1]
intent_p1       : 0.0
intent_p2       : 0.0
intent_p3       : 0.0
intent_code     : none
datatype        : float32
bitpix          : 32
slice_start     : 0
pixdim          : [1.        0.7813    0.7813    2.5999904 1.        1.        1.
 1.       ]
vox_offset      : 0.0
scl_slope       : nan
scl_inter       : nan
slice_end       : 0
slice_code      : unknown
xyzt_units      : 0
cal_max         : 0.0
cal_min         : 0.0
slice_duration  : 0.0
toffset         : 0.0
glmax           : 0
glmin           : 0
descrip         : b''
aux_file        : b''
qform_code      : unknown
sform_code      : aligned
quatern_b       : -0.5
quatern_c       : 0.5
quatern_d       : -0.5
qoffset_x       : -135.775
qoffset_y       : 100.547
qoffset_z       : 110.859
srow_x          : [   0.           0.           2.5999904 -135.775    ]
srow_y          : [ -0.7813   0.       0.     100.547 ]
srow_z          : [  0.      -0.7813   0.     110.859 ]
intent_name     : b''
magic           : b'n+1'
</code></pre>
<p>I could not spot anything strange when comparing to an axial 2D nifti.<br>
The nifti was generated with nibabel and an in-house custom python routine. It works well for 3D volume in any orientation, well in 2D axial, but seems to be problematic for Slicer with 2D sagittal and coronal.</p>

---

## Post #8 by @lassoan (2022-07-20 15:59 UTC)

<p>Thank you, this shows what the problem is. The first value of <code>dim</code> field is <code>2</code> and so only the first two components of the <code>srow</code> matrix are used. Therefore the image axis directions are <code>[0., 0.]</code> and <code>[-0.7813, 0.]</code>. The <code>[0., 0.]</code> axis direction is invalid.</p>
<p>If your image lives in the 3D space then it does not matter how many slices your image has, you must set dimension to 3.</p>
<p>Probably nibabel just ignores the image dimension. This may or may not be correct. Probably nobody really knows what is the correct behavior. This kind of issues are very typical for nifti: the format is poorly defined, ambiguous, and therefore developers who implement it make arbitrary decisions that lead to incompatibilities and misinterpretations. Stay away from nifti. This kind of issues very rarely if ever happen if you use other file formats, such as nrrd. It is really just nifti that has all these problems.</p>

---

## Post #9 by @BayesMonk (2022-07-21 08:16 UTC)

<p>Hi Andras,<br>
Thanks a lot for pointing out the problem. This explanation makes perfect sense for me!<br>
I also agree with your comment about nifti format. It is really a mess and we try to get rid of it as much as possible. I didn’t know nrrd format but I’ll have a look at it, it seems interesting.<br>
Best regards</p>

---
