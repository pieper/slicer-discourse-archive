# Not working "DWI Component"

**Topic ID**: 4793
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/not-working-dwi-component/4793

---

## Post #1 by @Ekaterina (2018-11-19 04:07 UTC)

<p>Operating system: MacOS High Sierra 10.13.6<br>
Slicer version: 4.81<br>
Expected behavior: I was hoping everything would be easy:-)<br>
Actual behavior:<br>
Good day!<br>
Please help in my situation:<br>
I have DWI images in DICOM. In the converter (diffusion - import and export - diffusion weighted DICOM import (DWI convert) transformed the images into “nrrd”. Trying to build “Diffusion Tensor Imaging”. I can not change the “DWI Component” parameter (module Volumes, field Scalar Display). Program does not allow me to do this. The value of “DWI Component” is 0. How can I make 10?<br>
On the example of the pictures downloaded from the page <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> - Documentation - Slicer Training - everything works out for me.<br>
Just ask for help in the following.<br>
After creating the “Diffusion Tensor Imaging” how to find the values ​​of the “anisotropy fraction”? I heard that they should be unloaded into a separate file. Could you tell us more about how to do this?</p>

---

## Post #2 by @ihnorton (2018-11-20 18:45 UTC)

<p>Hi <a class="mention" href="/u/ekaterina">@Ekaterina</a>, here are some suggestions to get started from raw DICOM files.</p>
<ol>
<li>
<p>please see this tutorial for loading DWI data from DICOM:</p>
<p><a href="https://www.dropbox.com/sh/qv1mo5lg5bzykps/AAB721QJ1VjZUm4oUSAleHsWa?dl=1">https://www.dropbox.com/sh/qv1mo5lg5bzykps/AAB721QJ1VjZUm4oUSAleHsWa?dl=1</a></p>
<p>If that works correctly then you should be able to change the DWI Component in the resulting file.</p>
</li>
<li>
<p>Next, please see this tutorial (from around page 57) for how to calculate a diffusion tensor volume from a DWI image, and then measure Fractional Anistropy.</p>
</li>
</ol>
<p>It sounds like you may have tried step 1 already, and there was a problem. If that is true, then please run the conversion again and <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report">send a log file</a>. Also please provide more information about the dataset (scanner model, etc. – if you are able to privately share data then that would be most helpful).</p>

---

## Post #3 by @ihnorton (2018-11-20 18:47 UTC)

<p>Also, see below to download a set of DWI DICOM data which is known to work with Slicer/DWIConvert. I would suggest following both tutorials first, using one of these datasets, and then if successful try with your own data.</p>
<ul>
<li><a href="https://www.dropbox.com/sh/qv1mo5lg5bzykps/AAB721QJ1VjZUm4oUSAleHsWa?dl=1">https://www.dropbox.com/sh/qv1mo5lg5bzykps/AAB721QJ1VjZUm4oUSAleHsWa?dl=1</a></li>
</ul>

---

## Post #4 by @Ekaterina (2018-12-05 16:50 UTC)

<p>Good day! Thanks for your reply!</p>
<p>I am using the “RadiAnt” program. In it, the patient’s pictures look right.</p>
<p>When loading the same images in “3D sliser”, the images are displayed incorrectly (as in the screenshot).</p>
<p>The error occurs with snapshots of DWI (several gradients!), the rest of the images load well.</p>
<p>Please tell me how to solve the problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf89d01af32b0384987eade9cd0d3fdec1ef23b6.jpeg" data-download-href="/uploads/short-url/rkqsuUYjuI0dIboJ6yBuHjXOFn0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf89d01af32b0384987eade9cd0d3fdec1ef23b6_2_690x385.jpeg" alt="image" data-base62-sha1="rkqsuUYjuI0dIboJ6yBuHjXOFn0" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf89d01af32b0384987eade9cd0d3fdec1ef23b6_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf89d01af32b0384987eade9cd0d3fdec1ef23b6_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf89d01af32b0384987eade9cd0d3fdec1ef23b6_2_1380x770.jpeg 2x" data-dominant-color="79798E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2546×1424 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ihnorton (2018-12-05 17:47 UTC)

<p>Please be careful not to publicly post images/data that contain personal identifying information (I removed the original image and replaced with identifiers blotted out).</p>
<p>Based on the series/file names in your screenshot, for example <code>801: DTI_medium_iso</code>:</p>
<ul>
<li>I believe you may be trying to load pre-computed tensor maps – tensors computed on the scanner. Slicer does not support these, Slicer only loads original/raw DWI images (gradient volumes).</li>
<li>If the files are indeed DWI, please make sure to use the “Diffusion-weighted DICOM Import (DWIConvert)” module. I mentioned this because usually the output from DWIConvert would not include the series number in the output like your screenshot shows (<code>801: </code>).</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/337c793060316749e93991282ac191fc9120aaf5.png" alt="image" data-base62-sha1="7lt26JEng0mxBfMJleV9qcsXqFT" width="393" height="42"></p>
<ul>
<li>See the tutorial <a href="https://discourse.slicer.org/t/not-working-dwi-component/4793/2">linked above</a> for instructions to use DWIConvert.</li>
</ul>

---

## Post #6 by @Ekaterina (2019-02-19 09:37 UTC)

<p>Hello! Please help with the import of DICOM images from a Toshiba tomograph! The program does not recognize them and does not allow editing. I do not understand how to transpose the matrix (I work with DWI images). Can you write step by step instructions?</p>
<p>I can send you my pictures.</p>

---

## Post #7 by @Ekaterina (2019-02-19 09:47 UTC)

<p>Sorry to write to you from two sides. I just can not start working on a diploma because of this problem.</p>

---

## Post #8 by @ljod (2019-02-19 13:06 UTC)

<p>Hi please write exactly which steps you did, what modules you used in slicer, and what output resulted.</p>
<p>It is impossible to help with so little description.</p>
<p>Did you follow all the steps we previously suggested and what happened then?</p>
<p>I also don’t understand what you mean by transpose the matrix. What matrix?</p>

---

## Post #10 by @Ekaterina (2019-02-19 13:53 UTC)

<p>I can not attach DICOM images. How do you send them?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc37ed91a987d787444b70bbb61a5ff7446464ee.png" data-download-href="/uploads/short-url/qR3AyzKjxob6IFmHsJ0nY54fXT8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc37ed91a987d787444b70bbb61a5ff7446464ee_2_690x404.png" alt="image" data-base62-sha1="qR3AyzKjxob6IFmHsJ0nY54fXT8" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc37ed91a987d787444b70bbb61a5ff7446464ee_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc37ed91a987d787444b70bbb61a5ff7446464ee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc37ed91a987d787444b70bbb61a5ff7446464ee.png 2x" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">983×576 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2019-02-19 14:01 UTC)

<aside class="quote no-group" data-username="Ekaterina" data-post="10" data-topic="4793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/bc79bd/48.png" class="avatar"> Ekaterina:</div>
<blockquote>
<p>I can not attach DICOM images. How do you send them?</p>
</blockquote>
</aside>
<p>Upload anywhere (dropbox, onedrive, gdrive, …) and post the link.</p>

---

## Post #12 by @Ekaterina (2019-02-19 14:24 UTC)

<p><a href="https://1drv.ms/f/s!AibGTREGoRSCgqp513SKt8zDeNVz_w" rel="nofollow noopener">https://1drv.ms/f/s!AibGTREGoRSCgqp513SKt8zDeNVz_w</a></p>

---

## Post #13 by @ljod (2019-02-19 14:47 UTC)

<p>Thanks. Have you tried dcm2niix as suggested previously? That program has the broadest support for DICOM dwi. It will most likely handle your data. It can now output need. Please try it and let us know if it works for you.</p>

---

## Post #14 by @ljod (2019-02-19 14:47 UTC)

<p>Output nrrd is what I meant.</p>

---

## Post #15 by @Ekaterina (2019-02-19 18:13 UTC)

<pre><code class="lang-auto">Transformed in this program, the result has not changed.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33abff9e682bbbbee2bd56b36d9d0c23826282a8.png" data-download-href="/uploads/short-url/7n6R4RhAMM68U7KBpXTk8TxrIDK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abff9e682bbbbee2bd56b36d9d0c23826282a8_2_375x500.png" alt="image" data-base62-sha1="7n6R4RhAMM68U7KBpXTk8TxrIDK" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abff9e682bbbbee2bd56b36d9d0c23826282a8_2_375x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abff9e682bbbbee2bd56b36d9d0c23826282a8_2_562x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33abff9e682bbbbee2bd56b36d9d0c23826282a8_2_750x1000.png 2x" data-dominant-color="C5C5CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×1134 94.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0aa785943572f6ad25a2d5723ef109c0ea7dc6.png" data-download-href="/uploads/short-url/vGgPaDvdaDfPkOWOy22u5szOahw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0aa785943572f6ad25a2d5723ef109c0ea7dc6_2_689x426.png" alt="image" data-base62-sha1="vGgPaDvdaDfPkOWOy22u5szOahw" width="689" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0aa785943572f6ad25a2d5723ef109c0ea7dc6_2_689x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de0aa785943572f6ad25a2d5723ef109c0ea7dc6_2_1033x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0aa785943572f6ad25a2d5723ef109c0ea7dc6.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1299×803 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1692b25466c629d6e1da65cc55bbfc9884d0defd.png" alt="image" data-base62-sha1="3dGNCBMpYb2gqGHMcTXHGY1mbox" width="644" height="267"></p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">
</code></pre>

---

## Post #16 by @ljod (2019-02-19 18:40 UTC)

<p>Hi is this the same data that Isaiah looked at before? Please let us know. That was DTI, not DWI. Slicer can’t read DTI.</p>
<p>The best program to handle various scanner vendor DICOM headers and their transforms is dcm2nii, so if this is actually truly DWI then please run that program to convert to a file format such as nrrd that slicer can read.</p>
<p>If you are loading nii not DICOM files (as shown in the finder window) then please try to load as nii in dwiconvert.</p>

---

## Post #17 by @Ekaterina (2019-02-24 17:01 UTC)

<p>I converted dicom format in nii. Uploaded new images. This format is not set on the panel in the program How to convert now to nrrd? (DiconToNrrd? FSLToNrrd?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a46ad59ec4d168d85aed173c62007f9c44e537f.png" data-download-href="/uploads/short-url/m0MXf8LBJrxAwWTIJvHYm5tZ4Qf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a46ad59ec4d168d85aed173c62007f9c44e537f_2_427x500.png" alt="image" data-base62-sha1="m0MXf8LBJrxAwWTIJvHYm5tZ4Qf" width="427" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a46ad59ec4d168d85aed173c62007f9c44e537f_2_427x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a46ad59ec4d168d85aed173c62007f9c44e537f_2_640x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a46ad59ec4d168d85aed173c62007f9c44e537f_2_854x1000.png 2x" data-dominant-color="B6B5C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×1069 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @Chris_Rorden (2019-02-25 02:48 UTC)

<p>The file you uploaded is a single volume with 74 slices. It looks like a derived from 12-directions. In order to compute tensors (DTI) you will need the raw data: assuming 12-directions and one unweighted B=0 image, this raw dataset should have 962 2D DICOM images (13*74). The derived trace image is useful for identifying pathology but it is isotropic and unable to reveal direction information.</p>
<p>For those who prefer NRRD to NIfTI, the upcoming release of dcm2niix will export to NRRD (just use the ‘-e y’ argument to specify NRRD export). Tashrif Billah deserves the credit for working out the DWI vector conversion. Currently, this is still a developmental release. However, if users want to try this out (and report any issues on the dcm2niix Github page), you simply need to install the developmental branch.</p>
<p>For Mac/Linux users it is usually pretty easy to build the latest developmental commit of dcm2niix yourself with the following commands:</p>
<p><span class="math"> git clone --branch development https://github.com/rordenlab/dcm2niix.git
</span> cd dcm2niix/console<br>
<span class="math"> make
</span> ./dcm2niix</p>
<p>You can also compile on Windows, but I usually just go to the Development branch Github page, click the AppVeyor button and get the most recently compiled ‘Artifact’</p>

---

## Post #19 by @Chris_Rorden (2019-02-25 05:46 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="18" data-topic="4793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>It looks like a derived from 12-directions</p>
</blockquote>
</aside>
<p>This should say “It looks like a Trace image derived from 12-directions.” If you look up “Trace DWI and ADC map” in your favorite search engine you will get more details.</p>

---

## Post #20 by @Ekaterina (2019-02-25 13:32 UTC)

<p>Earlier, I used DICOM images (Philips tomograph) and converted them to DWIConvert. After that, I could build a DTI.</p>
<p>Now the pictures are obtained on a Toshiba tomograph. The 3d slicer does not perceive them (the tomograph inverts the matrix with the numbers of series and image numbers). To solve this problem, I transferred Dicom images to niftii format.</p>
<p>how do i build a dti image from niftii format? Is it even possible? Is there a way to transpose a matrix of DICOM images (to bring to the correct form: a series number of pictures — a picture number)?</p>

---

## Post #21 by @ljod (2019-02-27 15:49 UTC)

<p>Hi it is not possible because the dataset you shared does not have enough information. You need DWI (diffusion weighted images) not a trace image. You should talk to the person who did the scanning.</p>

---

## Post #22 by @Ritu_Karela (2019-11-18 07:03 UTC)

<p>My DICOM to DWI conversion works fine but number of scalars is zero in volume tab. So I am unable to increase DWI component. Can anyone help please?</p>

---

## Post #23 by @pieper (2019-11-18 12:59 UTC)

<p>That probably means that your dicom series wasn’t really a DWI.  If you have more information to debug (like if you can share the data for testing) please start a new thread.</p>

---
