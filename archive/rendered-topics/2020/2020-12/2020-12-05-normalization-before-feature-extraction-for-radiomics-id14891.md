# Normalization before feature extraction for Radiomics

**Topic ID**: 14891
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/normalization-before-feature-extraction-for-radiomics/14891

---

## Post #1 by @hsotoudeh1 (2020-12-05 05:50 UTC)

<p>Hello;<br>
I have one question about Normalization before feature extraction for Radiomics.<br>
I know that the images from different scanners must be normalized before feature extraction. How can I do it in 3D Slicer? I see filtering (e.g. simple filter) but I don’t see the mean normalization which is the most common normalization in literature.<br>
Does the Pyradiomics perform the normalization itself?<br>
Thank you very much.</p>

---

## Post #2 by @JoostJM (2020-12-17 12:42 UTC)

<p>PyRadiomics performs the normalization if enabled in the settings. By default, no normalization is applied. You can enable it by setting <code>normalize: True</code></p>

---

## Post #4 by @harad (2023-03-28 09:46 UTC)

<p>As I know, the NORMALIZE function that you mention is a z-score which only considers one MRI at a time. Would it be better to normalize pixel intensities by any method which considers ALL MRI in the set? Cheers, Marko</p>

---

## Post #5 by @Josefa_Garcia (2023-03-31 18:43 UTC)

<p>Well, it depends if you need to segment and also from where you want to extract the features, in that case you should normalize before segment, I mean for example if you want to extract features from a brain tumor, you should first do skull stripping to remove the background, then normalize the brain mask and then segment the tumor (literature have shown to increase performance of the segmentation). There is a package to do it in python or in the CLI (I think it’s easier in the command line). here is the link. <a href="https://github.com/jcreinhold/intensity-normalization/tree/master/docs" class="inline-onebox" rel="noopener nofollow ugc">intensity-normalization/docs at master · jcreinhold/intensity-normalization · GitHub</a><br>
And after that you can extract the features. Hope it help you</p>

---
