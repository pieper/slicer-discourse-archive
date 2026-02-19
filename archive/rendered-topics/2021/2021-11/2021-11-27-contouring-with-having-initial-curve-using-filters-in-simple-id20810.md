---
topic_id: 20810
title: "Contouring With Having Initial Curve Using Filters In Simple"
date: 2021-11-27
url: https://discourse.slicer.org/t/20810
---

# Contouring with having initial curve using filters in Simple ITK module?

**Topic ID**: 20810
**Date**: 2021-11-27
**URL**: https://discourse.slicer.org/t/contouring-with-having-initial-curve-using-filters-in-simple-itk-module/20810

---

## Post #1 by @shahrokh (2021-11-27 13:41 UTC)

<p><strong>Hello Dear Developers and Users</strong></p>
<p>I want to segment or contour the pelvis.<br>
Consider the following figure. This screenshot contains a 2D image of EPID, named <em>EPID</em>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e171204995ecc74235b674f60b8a7c227dc6707f.png" data-download-href="/uploads/short-url/walNKCDmauqS5I4EBa5bt5Cc7tZ.png?dl=1" title="EPID" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e171204995ecc74235b674f60b8a7c227dc6707f_2_486x500.png" alt="EPID" data-base62-sha1="walNKCDmauqS5I4EBa5bt5Cc7tZ" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e171204995ecc74235b674f60b8a7c227dc6707f_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e171204995ecc74235b674f60b8a7c227dc6707f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e171204995ecc74235b674f60b8a7c227dc6707f.png 2x" data-dominant-color="6F6F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">EPID</span><span class="informations">715×735 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Consider the following figure. This screenshot contains the contour of the pelvic bone extracted from the DRR image named <em>contourDRR</em>,  using filters such as <strong>ClosingByReconstructionImageFilter</strong>, <strong>OpeningByReconstructionImageFilter</strong> and <strong>ZeroCrossingBasedEdgeDetectionImageFilter</strong> in <strong>Simple ITK</strong> module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f26e2462539c4323887706667ad3e93652c1e10.png" data-download-href="/uploads/short-url/4rA6OwHkovtR2FFMFyxsWk5LgJi.png?dl=1" title="contourDRR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f26e2462539c4323887706667ad3e93652c1e10_2_486x500.png" alt="contourDRR" data-base62-sha1="4rA6OwHkovtR2FFMFyxsWk5LgJi" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f26e2462539c4323887706667ad3e93652c1e10_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f26e2462539c4323887706667ad3e93652c1e10.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f26e2462539c4323887706667ad3e93652c1e10.png 2x" data-dominant-color="060606"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">contourDRR</span><span class="informations">715×735 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/183e2b23d01b31389b6391ac7d39c0130a4dd3de.png" data-download-href="/uploads/short-url/3ssEAKbxVuhRAqfiBesLkurntQq.png?dl=1" title="contourANDEPID" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183e2b23d01b31389b6391ac7d39c0130a4dd3de_2_475x500.png" alt="contourANDEPID" data-base62-sha1="3ssEAKbxVuhRAqfiBesLkurntQq" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183e2b23d01b31389b6391ac7d39c0130a4dd3de_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183e2b23d01b31389b6391ac7d39c0130a4dd3de_2_712x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/183e2b23d01b31389b6391ac7d39c0130a4dd3de.png 2x" data-dominant-color="585757"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">contourANDEPID</span><span class="informations">714×751 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to consider this contour (<em>contourDRR</em>) as a starting point (initial contour) and using, for example, the filter of <strong>geodesicActiveContourLevelSetImageFilter</strong> in <strong>Simple ITK</strong> module, it is deformable to match the edge of the pelvis in the EPID image (<em>EPID</em>).<br>
In other words, I want to use active contour with matching this initial contour (<em>contourDRR</em>) on the edges of pelvis in <em>EPID</em>.<br>
Unfortunately, after using this filter, I took an output image that had all the pixels equal to one.</p>
<p>How can I do this contouring with initial contour?<br>
Please guide me to do it.<br>
Best regards.</p>
<p>Shahrokh</p>

---

## Post #2 by @shahrokh (2021-11-27 14:30 UTC)

<p>Details:</p>
<p>EPID information:<br>
Image Dimension: 611 576 1<br>
Image Spacing: 0.25mm 0.25mm 1.00mm</p>
<p>contourDRR Information:<br>
Image Dimension: 270 256 1<br>
Image Spacing: 0.5859mm 0.5859mm 1.0000mm</p>
<p>With these specifactions, at firstly I made the same type these volumes (EPID and contourDRR) to Double. Then I applied <strong>geodesicActiveContourLevelSetImageFilter.</strong> I get the following error message:</p>
<p><em>Exception thrown in SimpleITK GeodesicActiveContourLevelSetImageFilter_Execute: /work/Preview/Slicer-0-build/SimpleITK/Code/BasicFilters/src/sitkImageFilter.cxx:63:</em></p>
<p><em>sitk::ERROR: Input “featureImage” for “GeodesicActiveContourLevelSetImageFilter” has size of [ 270, 256, 1 ] which does not match the primary input’s size of [ 611, 576, 1 ]!</em></p>
<p>So I use the module of <strong>General Registration (ANTs)</strong> to unify the specifications of these volumes (EPID and contourDRR).</p>
<p><strong>Inputs:</strong><br>
Fixed Image: EPID<br>
Moving Image: contourDRR<br>
Stages (Presets): Rigid<br>
<strong>Setting:</strong><br>
Computation Precision: double<br>
<strong>Outputs:</strong><br>
Transformed Volume: ContourDRRTRansformed</p>
<p>I get the following result:<br>
EPID information:<br>
Image Dimension: 611 576 1<br>
Image Spacing: 0.25mm 0.25mm 1.00mm<br>
ContourDRRTRansformed Information:<br>
Image Dimension: 611 576 1<br>
Image Spacing: 0.25mm 0.25mm 1.0000mm</p>
<p>At now, I run <strong>geodesicActiveContourLevelSetImageFilter</strong> on these volumes: EPID and ContourDRRTRansformed nodes.I get the following error message:</p>
<p><em>Exception thrown in SimpleITK GeodesicActiveContourLevelSetImageFilter_Execute: /work/Preview/Slicer-0-build/ITK/Modules/Filtering/ImageFilterBase/include/itkRecursiveSeparableImageFilter.hxx:227:</em></p>
<p><em>ITK ERROR: RecursiveGaussianImageFilter(0x7f8d78567a40): The number of pixels along direction 2 is less than 4. This filter requires a minimum of four pixels along the dimension to be processed.</em></p>
<p>I do not know to add three slices (exactly one or copy) in the direction of IS in 3DSlicer. For doing it, I save these volumes ( <strong>EPID and ContourDRRTRansformed</strong> ) in nifti format and use <strong>medcon</strong> for example with following commands:</p>
<pre><code class="lang-auto">$ cp ContourDRRTRansformed.nii ContourDRRTRansformed1.nii
$ cp ContourDRRTRansformed.nii ContourDRRTRansformed2.nii
$ cp ContourDRRTRansformed.nii ContourDRRTRansformed3.nii
$ cp ContourDRRTRansformed.nii ContourDRRTRansformed3.nii
$ medcon -f ContourDRRTRansformed1.nii ContourDRRTRansformed2.nii ContourDRRTRansformed3.nii ContourDRRTRansformed4.nii -stack3d -c nii
...
$ cp EPID.nii EPID1.nii
$ cp EPID.nii EPID2.nii
$ cp EPID.nii EPID3.nii
$ cp EPID.nii EPID3.nii
$ medcon -f EPID1.nii EPID2.nii EPID3.nii EPID4.nii -stack3d -c nifti
</code></pre>
<p><strong>Result:</strong><br>
EPID information:<br>
Image Dimension: 611 576 4<br>
Image Spacing: 0.25mm 0.25mm 1.00mm<br>
contourDRR Information:<br>
Image Dimension: 611 576 4<br>
Image Spacing: 0.25mm 0.25mm 1.00mm</p>
<p>After doing it, I again I run <strong>geodesicActiveContourLevelSetImageFilter</strong> on these volumes: EPID and ContourDRRTRansformed. As mentioned in my previous message, unfortunately, after using this filter, I took an output image that had all the pixels equal to one.</p>
<p>Please guide me to solving this problem.<br>
Thanks.<br>
Shahrokh</p>

---

## Post #3 by @lassoan (2021-11-28 05:32 UTC)

<p>You can use “Resample Scalar/Vector/DWI Volume” to resample the contourDRR image to match the geometry of the EPID image, but setting the contourDRR as input image and the EPID as reference image.</p>

---

## Post #4 by @shahrokh (2021-11-28 10:48 UTC)

<p>Thanks a lot for your guidance.</p>
<p>I used the module of <strong>Resample Scalar/Vector/DWI Volume</strong> to match the geometry of <em>contourDRR</em> image with <em>EPID</em> image (as you mentioned, I set <em>contourDRR</em> and <em>EPID</em> as Input Volume and Reference Volume respectively). After running it, I have new volume node with the name of <em>contourDRR2</em> which is geometrically matched with the <em>EPID</em> image.</p>
<p>But I’m sorry, I still have two major and minor problems:</p>
<p><em><strong>Major problem:</strong></em><br>
How can I use a binary image containing the contour of an organ (such as <em>contourDRR2</em>) as the initial curve using <strong>Simple ITK</strong> filter, based on the <strong>active contour</strong> technique, to extract the contour in a gray scale image (<em>EPID</em>)? As mentioned above, I have two images <em>contourDRR2</em> (binary images) and <em>EPID</em> (graycale image) which are geometrically matched with ‌each other. I used the filter of <strong>geodesicActiveContourLevelSetImageFilter</strong> to deform this initial contour so that the result of this deformation (for example using this filter) is a contour that matches the edge of the pelvis in the <em>EPID</em> image.</p>
<p><em><strong>Minor problem:</strong></em><br>
How do I generate four axial slices that are exactly the same as a original slice and are in a row in the IS direction?<br>
For example, I have ContourDRR2 with the following specifications:<br>
Image Dimension: 611 576 1<br>
…<br>
How can I convert this image with the following specifications:<br>
Image Dimension: 611 576 4<br>
…<br>
Best regards.<br>
Shahrokh</p>

---

## Post #5 by @lassoan (2021-11-28 12:53 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="4" data-topic="20810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>How can I use a binary image containing the contour of an organ (such as <em>contourDRR2</em> ) as the initial curve</p>
</blockquote>
</aside>
<p>Probably the best would be to ask this from the developers of these algorithms on the <a href="https://discourse.itk.org">ITK forum</a>.</p>
<aside class="quote no-group" data-username="shahrokh" data-post="4" data-topic="20810">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>How do I generate four axial slices that are exactly the same as a original slice and are in a row in the IS direction?</p>
</blockquote>
</aside>
<p>You can use a resampling module for this, setting the spacing along IS direction to 1/4 of the original and the IS extent of the image to 4.</p>

---

## Post #6 by @shahrokh (2021-11-28 13:27 UTC)

<p>Thank a lot for your guidance and refer to ITK forum. I raise my problem there.<br>
Best regards.<br>
Shahrokh</p>

---
