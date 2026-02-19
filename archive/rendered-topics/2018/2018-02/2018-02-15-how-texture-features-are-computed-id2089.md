---
topic_id: 2089
title: "How Texture Features Are Computed"
date: 2018-02-15
url: https://discourse.slicer.org/t/2089
---

# How texture features are computed?

**Topic ID**: 2089
**Date**: 2018-02-15
**URL**: https://discourse.slicer.org/t/how-texture-features-are-computed/2089

---

## Post #1 by @afsanehlahooti (2018-02-15 01:53 UTC)

<p>Does 3DSlicer use any filter when gives us some features such as Kurtosis and skewness?<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-02-15 01:57 UTC)

<p>Which Slicer module do you use to compute these features?</p>

---

## Post #3 by @afsanehlahooti (2018-02-15 20:13 UTC)

<p>I use HeterogeneityCAD for those features.<br>
Thanks</p>

---

## Post #4 by @JoostJM (2018-02-16 08:59 UTC)

<p>As far as I know, HeterogeneityCAD doesn’t apply filters. But if you want to calculate kurtosis and skewness on Laplacian of Gaussian or Wavelet filtered images, that is supported in SlicerRadiomics (category Informatics).</p>

---

## Post #5 by @timeanddoctor (2018-02-16 11:36 UTC)

<p>I am still confused by “kurtosis and skewness on Laplacian of Gaussian or Wavelet filtered images”. What’s that and how to use? I would appreciat it if you could give me any suggestions or any examples about it.<br>
Thanks.<br>
Li</p>

---

## Post #6 by @JoostJM (2018-02-16 12:21 UTC)

<p>In short, these features often encode something about the texture.</p>
<p>Skewness and Kurtosis from original images are only dependent on the graylevels present in the image, not their location, so not really texture, as coarse and fine texture can have the same grayvalues present, but in different locations.<br>
When they are extracted from filtered images, such as Laplacian of Gaussian (LoG), the tell you more about the texture, i.e. the relationship between gray value and it’s location in the region of interest (ROI).</p>
<p>Quick example: in LoG,the meaning of the gray value is how quickly the gray value is changing in that area (i.e. second derivative: laplacian). if the value is very high or very low, it means that there is a lot of contrast (i.e. says something about the local texture). First order statistics then say something about the texture of the entire ROI, such as mean tells you something about the average contrast in the image, whereas kurtosis tells you something about how areas of contrast in the image relate to each other (low kurtosis = mainly areas with similar contrast, high = both areas with high and low contrast).<br>
Finally, as we are performing Laplacian of Gaussian, the values depend on the sigma of the gaussian kernel used. Practically, this controls at what level you are looking at your image. Low sigma means looking at fine (i.e. very local) texture, and higher values look at increasingly coarse texture (smooth out the very local differences).</p>

---

## Post #7 by @afsanehlahooti (2018-02-16 16:09 UTC)

<p>Thank you so much for your reply.</p>

---

## Post #8 by @afsanehlahooti (2018-02-16 16:09 UTC)

<p>Too much useful. Thanks.</p>

---

## Post #9 by @timeanddoctor (2018-02-18 03:24 UTC)

<p>Thank you JoostJM.<br>
It is very usefull to me.<br>
Thank you for your detailed introduction. I will print and read it.<br>
Your Sincerely,<br>
Li</p>

---
