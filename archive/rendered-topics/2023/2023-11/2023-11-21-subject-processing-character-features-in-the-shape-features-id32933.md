# Subject: Processing Character Features in the shape features 

**Topic ID**: 32933
**Date**: 2023-11-21
**URL**: https://discourse.slicer.org/t/subject-processing-character-features-in-the-shape-features/32933

---

## Post #1 by @curtis_sohn (2023-11-21 19:40 UTC)

<p>Dear Community,</p>
<p>I am working on a project to predict the IDH status in glioma using features extracted via Pyradiomics. I’ve encountered a challenge with certain shape features that are extracted as character strings or tuples rather than single numeric values.</p>
<p>The documentation (<a href="https://pyradiomics.readthedocs.io/en/latest/features.html#module-radiomics.shape" class="inline-onebox" rel="noopener nofollow ugc">Radiomic Features — pyradiomics v3.1.0rc2.post5+g6a761c4 documentation</a>) describes these features as single scalar values, but the output I’m getting includes tuples and even hash strings. For example, the ‘original_shape_Elongation’ feature should represent the relationship between the two largest principal components, but I am seeing values like “(192, 256, 256)”.</p>
<p>Here are some examples of the features and their current formats:</p>
<ul>
<li><code>original_shape_Elongation</code>: “(192, 256, 256)”</li>
<li><code>original_shape_Maximum2DDiameterRow</code>: “(0.9000000357627869, 0.8984375, 0.8984375)”</li>
<li><code>original_shape_Maximum3DDiameter</code>: “(27, 103, 91, 57, 60, 47)”</li>
<li><code>original_shape_Sphericity</code>: “(56.54839034712076, 136.01947201370345, 114.27520278099652)”</li>
<li>And others with similar issues.</li>
</ul>
<p>My goal is to reformat these character feature outputs into a consistent numeric format that I can use for predictive modeling. My initial thought is to extract meaningful single values from these tuples, possibly considering the maximum value, mean, or even recalculating the feature where possible.</p>
<p>How to interpret these tuples and character strings correctly for each feature.</p>
<p>For your reference, here are the settings I used for feature extraction (see attached settings image).</p>
<p>I appreciate any guidance or references to similar cases you might have encountered.</p>
<p>Best regards,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec9e3f16be1308f1e7c49cbf1ea08c724e426f8f.png" data-download-href="/uploads/short-url/xLdIUPvlniKpJTgEpz14tLHk10r.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec9e3f16be1308f1e7c49cbf1ea08c724e426f8f_2_472x499.png" alt="image" data-base62-sha1="xLdIUPvlniKpJTgEpz14tLHk10r" width="472" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec9e3f16be1308f1e7c49cbf1ea08c724e426f8f_2_472x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec9e3f16be1308f1e7c49cbf1ea08c724e426f8f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec9e3f16be1308f1e7c49cbf1ea08c724e426f8f.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">585×619 55.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @curtis_sohn (2023-11-22 20:04 UTC)

<p>I fixed by extracting features separately for each image modality works instead of extracting for multiple modalities together</p>

---
