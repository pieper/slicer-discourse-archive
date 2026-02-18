# How to quantitatively compare SPM fMRI data and BIP maps

**Topic ID**: 7140
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/how-to-quantitatively-compare-spm-fmri-data-and-bip-maps/7140

---

## Post #1 by @carba86 (2019-06-12 15:00 UTC)

<p>I am currently working with fMRI, trying to compare performance between SPM and the software provided by GE, BrainWave PA. Besides comparing the two sets of post-processed images with two senior radiologists, I would like to do a quantitative  analysis. I’ve considered a DICE Coefficient obtained for example with 3DSlicer.</p>
<p>However, I am having trouble with the formats. GE provides a stack of images for axial, coronal and sagittal views and a BIP (burn in pixel) volume. I haven’t been able to use neither of these to study a correlation with the data obtained with SPM.</p>
<p>I would like to ask if you are aware of any method available to achieve this task.</p>

---

## Post #2 by @pieper (2019-06-12 19:36 UTC)

<p>I’m not sure anyone has experience with exactly that data, but if you share an example (e.g. phantom or anonymized/volunteer) someone might have suggestions.</p>

---

## Post #3 by @carba86 (2019-06-12 20:09 UTC)

<p>Thanks Steve. I am attaching two images that belong to nii files. These belong to two different patients but I am trying to obtain a coefficient to quantify overlap between the areas painted in white in one file (BIP maps obtained with GE BrainWave) and the colored ones in the other file (SPM obtained files).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86ee1ed83023112b373b9de0139e96950bf29b7a.jpeg" data-download-href="/uploads/short-url/jfE9pD84O6jM9pD5p9ZUq6NfvDQ.jpeg?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86ee1ed83023112b373b9de0139e96950bf29b7a_2_428x500.jpeg" alt="12" data-base62-sha1="jfE9pD84O6jM9pD5p9ZUq6NfvDQ" width="428" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86ee1ed83023112b373b9de0139e96950bf29b7a_2_428x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86ee1ed83023112b373b9de0139e96950bf29b7a_2_642x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86ee1ed83023112b373b9de0139e96950bf29b7a.jpeg 2x" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">674×786 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dce846f55e974b60d851a883ba75042cf5fbbfdb.png" data-download-href="/uploads/short-url/vweH5PtsaidkM6PRM2URK9W3ktt.png?dl=1" title="55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dce846f55e974b60d851a883ba75042cf5fbbfdb.png" alt="55" data-base62-sha1="vweH5PtsaidkM6PRM2URK9W3ktt" width="409" height="500" data-dominant-color="262324"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">55</span><span class="informations">554×676 60.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2019-06-13 14:35 UTC)

<p>Did you try loading the files in Slicer?  It’s hard to guess (not clear to me where the screenshots came from) but if they were both, say, nifti files from the same patient they should line up in Slicer and you should be able to extract the regions for comparison.</p>

---
