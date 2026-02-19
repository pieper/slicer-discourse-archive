---
topic_id: 30887
title: "I Am Trying To Copy All The Metadata Header Information From"
date: 2023-07-31
url: https://discourse.slicer.org/t/30887
---

# I am trying to copy all the metadata/header information from one image to another.

**Topic ID**: 30887
**Date**: 2023-07-31
**URL**: https://discourse.slicer.org/t/i-am-trying-to-copy-all-the-metadata-header-information-from-one-image-to-another/30887

---

## Post #1 by @Cristobal_Rodero (2023-07-31 14:11 UTC)

<p>I have a segmentation (original_image) that when I overlap it with the MRI image it comes from it overlaps as expected (comparing it in 3D Slicer, for instance). I perform some operations on Seg3D (or any other software that saves just the image array) and when I save the image (new_image) the overlap doesn’t occur anymore, it’s moved and rotated. I have the function below using SimpleITK (sitk) to try to copy all the possible metadata/header/information from the original_image but it still doesn’t align. The center seems to be fine, but that’s it. I understand that there are probably redundancies in the script, I was trying all possible options.</p>
<pre data-code-wrap="code"><code class="lang-plaintext">def save_itk_keeping_header(new_image, original_image, filename):

  image_bad_header_itk=sitk.ReadImage(new_image)
  image_good_header=sitk.ReadImage(original_image)

  image_bad_header_itk.CopyInformation(image_good_header)

  image_bad_header_itk.SetDirection(image_good_header.GetDirection())
  image_bad_header_itk.SetOrigin(image_good_header.GetOrigin())
  [image_bad_header_itk.SetMetaData(key,image_good_header.GetMetaData(key)) for key in image_good_header.GetMetaDataKeys()]

  sitk.WriteImage(image_bad_header_itk, filename, True)
</code></pre>
<p>I’m not bound to SimpleITK at all, if there’s a solution using Slicer, happy to use it. The output I get is below - it seems that it should be rotated 90 degrees. Any idea what am I missing? In case it helps, the grey image is an MRI, so they are usually rotated in contrast with CT images that are align with the XYZ coordinate system.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/561382234da30df85b25a613974123798b7d25a2.png" alt="TjWuC" data-base62-sha1="chsRfDTbpqIYbcxhaTLbm8HRppE" width="486" height="406"></p>

---

## Post #2 by @lassoan (2023-07-31 14:24 UTC)

<p>What you do looks correct, except I don’t see explicitly copying the image spacing (in ITK, spacing is not included in direction). If copying the spacing does not help then I would recommend to report these issues to their developers. Using the image geometry (origin, spacing, axis direction) when an image is loaded and saving the image geometry properly in output image is not optional.</p>
<p>If these issues are not fixed in those software then I would recommend not to use them. If they make such basic mistakes, what other mistakes can be in those software anyway? How many people use and test them if such issues may go unnoticed? If the issues are noticed but not fixed then what support you can expect and for how long these software will be still around?</p>
<p>What features of these other software you find useful? Most likely similar or same features may be avaialable in Slicer, too, and we can help you to find them.</p>

---
