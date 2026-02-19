---
topic_id: 22644
title: "Wavelet Features With Flat Region"
date: 2022-03-22
url: https://discourse.slicer.org/t/22644
---

# Wavelet features with "flat region"?

**Topic ID**: 22644
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/wavelet-features-with-flat-region/22644

---

## Post #1 by @Helo (2022-03-22 20:35 UTC)

<p>Hi everyone!</p>
<p>I am doing a feature extraction and one of the problems I am having is some “flat regions” in the wavelet features of some events (not all dataset and not always the same features), like:                                                                              wavelet-LHH, “glszm”, “SizeZoneNonUniformity”, “1.0”<br>
wavelet-HLH, “glszm”, “GrayLevelNonUniformity”, “1.0”<br>
wavelet-HLH, “glszm”, “SizeZoneNonUniformity”, “1.0”<br>
wavelet-HHH, “glszm”, “SizeZoneNonUniformity”, “1.0”</p>
<p>My interpolator is ‘sitkBSpline’, with a resampledPixelSpacing of [2, 2, 2], as I have slices from 2.5 to 8 mm.  I selected my binWidth based on the range feature of the whole dataset and found that the best value is 3 (it is within the ideal range 16-128).</p>
<p>For some events, the above problem disappears when I set resampling to  2.5,2.5,2.5  but for others, it does not work. I have also tried changing the binWidth.</p>
<p>Can you tell me if the values of these parameters (binWidth and resampledPixelSpacing) are ok, and if this “flat regions” are normal? Or could this also be a problem with the wavelet (I have not entered any parameters into this filter)?</p>
<p>Thank you for your attention!</p>

---

## Post #2 by @JoostJM (2022-05-03 07:46 UTC)

<p>Wavelet filtering can result in quite different values. You can review the range feature extracted from the filter to be sure. If necessary, you can set a different binWidth for the wavelet-filtered images, though it is not possible to do this for e.g. just the HLH filtered.</p>

---
