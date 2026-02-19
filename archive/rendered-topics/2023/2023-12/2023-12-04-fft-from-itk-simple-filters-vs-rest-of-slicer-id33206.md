---
topic_id: 33206
title: "Fft From Itk Simple Filters Vs Rest Of Slicer"
date: 2023-12-04
url: https://discourse.slicer.org/t/33206
---

# FFT from ITK Simple Filters (vs rest of Slicer)

**Topic ID**: 33206
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/fft-from-itk-simple-filters-vs-rest-of-slicer/33206

---

## Post #1 by @shai-ikko (2023-12-04 16:26 UTC)

<p>Hi,</p>
<p>I am trying to do some image processing with Slicer, and one of the things I wanted to try was a High Pass filter. I found no such filter ready-made, so I thought I might construct one using parts which are. The first step is FFT, and in “ITK Simple Filters” there is a “ForwardFFTImageFilter”, which looks like it can fit the bill.</p>
<p>Alas, FFT produces an image whose pixels are complex; and AFAICT, Slicer doesn’t really support this. So, I got a volume with these properties:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41a9aa36509267ed52ad4f09d40fb103cd1fce53.png" alt="image" data-base62-sha1="9mSxxlj8nLvllelnUsERCY60NYD" width="333" height="382"></p>
<p>It’s a Scalar volume, so one can’t apply Vector-to-Scalar to extract the real and imaginary parts; and yet its scalar type is “2 doubles”, which nothing in Slicer seems to handle – including ITK Simple filters. E.g. when trying to extract the magnitude using ComplexToModulusImageFilter, we get:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/558e513c5241926ae5949bc502b870f62c741a21.png" alt="image" data-base62-sha1="ccRuU3CKs4uUoH1H2MMWX9Z8Cul" width="498" height="165"></p>
<p>I will manage to do what I want in Python, I suppose, but, unless I’m missing something, this appears to be broken.</p>
<p>Slicer 5.4.0 on Linux, in case that matters.</p>

---

## Post #2 by @mau_igna_06 (2023-12-04 17:24 UTC)

<p>This might be not helpful: But I was able to do a frequency domain filtering using SimpleFilters on Slicer in the past. I don’t have any code though.</p>

---
