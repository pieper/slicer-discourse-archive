---
topic_id: 21559
title: "Resample Volume With Unregular Spacing"
date: 2022-01-21
url: https://discourse.slicer.org/t/21559
---

# Resample volume with unregular spacing

**Topic ID**: 21559
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/resample-volume-with-unregular-spacing/21559

---

## Post #1 by @LaurennLam (2022-01-21 13:58 UTC)

<p>Hi everyone,</p>
<p>I’m trying to resampled a volume with an unregular spacing along Z axis.<br>
I followed this <a href="https://C:%5CKitware%5CProjects%5CEDAP%5CCMake%5Cscript%5CdefinePaths.bat" rel="noopener nofollow ugc">post</a> but I encountered issue when resampling.<br>
Here are the steps I followed:</p>
<ul>
<li>Loading dicom volume as <code>dicomVolume</code>
</li>
<li>It also creates an acquisition transform <code>transform</code> (vtkMRMLGridTransform)</li>
<li>I used Resample Scalar Volume by specifying output spacing (I’ll use the output as an input for the other Resample filter) with <code>dicomVolume</code> as an input and create a new volume <code>tempResampledVolume</code>
</li>
<li>I launch the Resample Image (BRAINS) by setting:<br>
– ImageToWrap: <code>dicomVolume</code><br>
– Reference image: <code>tempResampledVolume</code><br>
– Transform file: <code>transform</code><br>
The resampling fails with this error :</li>
</ul>
<pre><code class="lang-auto">[FAILED]
Error while reading the the file C:/blablabla/Slicer/BJAIA_vtkMRMLGridTransformNodeB.h5

itk::ExceptionObject (000000D6A50FDA00)
Location: "unknown" 
File: D:\D\S\Slicer-1-build\ITK\Modules\IO\TransformBase\src\itkTransformIOBase.cxx
Line: 62
Description: itk::ERROR: itk::ERROR: HDF5TransformIOTemplate(0000024174726940): Could not create an instance of "InverseDisplacementFieldTransform_double_3_3"
The usual cause of this error is not registering the transform with TransformFactory
Currently registered Transforms: 
	"AffineTransform_double_2_2"
	"AffineTransform_double_3_3"
	"AffineTransform_double_4_4"
	"AffineTransform_float_2_2"
	"AffineTransform_float_3_3"
	"AffineTransform_float_4_4"
	"AzimuthElevationToCartesianTransform_double_3_3"
	"AzimuthElevationToCartesianTransform_float_3_3"
       .....
</code></pre>
<p>My understanding is that there are some issue with the transform but I don’t understand what exactly.<br>
Thanks for your help.</p>

---

## Post #2 by @pieper (2022-01-23 20:41 UTC)

<aside class="quote no-group" data-username="LaurennLam" data-post="1" data-topic="21559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/laurennlam/48/16833_2.png" class="avatar"> LaurennLam:</div>
<blockquote>
<p>I followed this <a href="https://C:%5CKitware%5CProjects%5CEDAP%5CCMake%5Cscript%5CdefinePaths.bat" rel="noopener nofollow ugc">post</a> but I encountered issue when resampling.</p>
</blockquote>
</aside>
<p>Can you re-send the post you linked to?  It’s not coming through.</p>
<p>As a workaround you can use the “harden transform” option in the transforms module.</p>

---

## Post #3 by @LaurennLam (2022-01-24 11:51 UTC)

<p>Sorry for the fail.<br>
Here is the <a href="https://discourse.itk.org/t/account-for-non-uniform-spacing/2797/4" rel="noopener nofollow ugc">link</a></p>

---

## Post #4 by @pieper (2022-01-24 13:28 UTC)

<aside class="quote no-group" data-username="LaurennLam" data-post="3" data-topic="21559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/laurennlam/48/16833_2.png" class="avatar"> LaurennLam:</div>
<blockquote>
<p>Here is the <a href="https://discourse.itk.org/t/account-for-non-uniform-spacing/2797/4">link</a></p>
</blockquote>
</aside>
<p>Thanks!  Yes, I figured it was that one or something similar.</p>
<p>For now I think hardening the volume through the transforms or data module is best.  Passing the grid transform to the brains resampler really should work and I’m not sure why it doesn’t.</p>

---

## Post #5 by @LaurennLam (2022-01-24 14:16 UTC)

<p>Thanks for your fast answer. Indeed, I was able to apply the harden transform. I didn’t remember how to do this. It seems to work well. Thanks !!</p>

---
