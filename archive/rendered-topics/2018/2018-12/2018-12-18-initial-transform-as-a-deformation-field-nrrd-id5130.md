---
topic_id: 5130
title: "Initial Transform As A Deformation Field Nrrd"
date: 2018-12-18
url: https://discourse.slicer.org/t/5130
---

# Initial transform as a deformation field (.nrrd)

**Topic ID**: 5130
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/initial-transform-as-a-deformation-field-nrrd/5130

---

## Post #1 by @rayan (2018-12-18 16:36 UTC)

<p>Hello,</p>
<p>I am registering two images using Elastix. I want to define an initial transform which I created outside of Elastix in .nrrd format. However, I see Elastix can only accept a text file transform (.txt) defined using -t0 option. I was wondering is there a way to put the deformation field .nrrd as an initial transform? Or convert the deformation field to a text file parameters that Elastix can read?</p>
<p>Thanks,<br>
Rayan</p>

---

## Post #2 by @stephan (2018-12-18 20:21 UTC)

<p>Have you had a look at<br>
<a href="http://elastix.isi.uu.nl/doxygen/classelastix_1_1DeformationFieldTransform.html" class="onebox" target="_blank" rel="nofollow noopener">http://elastix.isi.uu.nl/doxygen/classelastix_1_1DeformationFieldTransform.html</a></p>
<p>I am not sure about .nrrd files (the example there uses .mhd), but this might be a good starting point at least.</p>
<p>Stephan</p>

---

## Post #3 by @lassoan (2018-12-18 20:26 UTC)

<p>Unfortunately, Elastix does not use standard ITK transform file format. I’ve already <a href="https://github.com/SuperElastix/elastix/issues/18" rel="nofollow noopener">reported this issue</a> and several users supported it but it was not important enough for Elastix developers to work on it and I did not have time to implement it. You may add a comment to the issue to confirm that this is an important need.</p>
<p>Until it gets fixed in Elastix, you can <em>harden</em> the initial transform in Slicer. Hardening a linear transform only changes the image header, does not resample the voxels, so it is fast and does not affect image quality.</p>

---

## Post #4 by @stephan (2018-12-18 20:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I found that at least for affine transforms returned by Elastix one can simply copy/paste the parameters 1:1 into an ITK .tfm file to import the linear transform into Slicer.<br>
So, for example, the Elastix output</p>
<blockquote>
<p>(Transform “AffineTransform”)<br>
(NumberOfParameters 12)<br>
(TransformParameters <strong>0.885096 -0.037625 0.021871 0.053013 0.878547 -0.037054 -0.046384 0.040843 0.821334 0.789846 -6.528138 2.683686</strong>)<br>
(InitialTransformParametersFileName “NoInitialTransform”)<br>
(UseBinaryFormatForTransformationParameters “false”)<br>
(HowToCombineTransforms “Compose”)</p>
<p>// AdvancedAffineTransform specific<br>
(CenterOfRotationPoint <strong>6.2539062500 -240.1992187500 262.1000061035</strong>)</p>
</blockquote>
<p>becomes</p>
<blockquote>
<p><span class="hashtag-raw">#Insight</span> Transform File V1.0<br>
<span class="hashtag-raw">#Transform</span> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: <strong>0.885096 -0.037625 0.021871 0.053013 0.878547 -0.037054 -0.046384 0.040843 0.821334 0.789846 -6.528138 2.683686</strong><br>
FixedParameters: <strong>6.2539062500 -240.1992187500 262.1000061035</strong></p>
</blockquote>
<p>This ITK .tfm file can then be loaded into Slicer to get a linear transform. Something similar might be possible with the Elastix BSplineTransform and the corresponding ITK .tfm “BSplineTransform_double_3_3”, but I have not tested this.<br>
I admit it’s a little bit crude as work-around and direct ITK output would be great, but for the time being this is what I resort to when I have an affine transform from SlicerElastix and do not want to have it represented by gigabytes of deformation data.</p>

---

## Post #5 by @lassoan (2018-12-18 21:50 UTC)

<p>Yes, for basic transforms parameter conversion is trivial. I’ve been considering adding a Elastix transform file parser to SlicerElastix instead of improving transform reader/writer classes in Elastix.</p>

---
