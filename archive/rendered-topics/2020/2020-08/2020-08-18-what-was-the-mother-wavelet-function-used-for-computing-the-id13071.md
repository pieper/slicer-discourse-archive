---
topic_id: 13071
title: "What Was The Mother Wavelet Function Used For Computing The"
date: 2020-08-18
url: https://discourse.slicer.org/t/13071
---

# What was the mother wavelet function used for computing the wavelet features by SlicerRadiomic?

**Topic ID**: 13071
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/what-was-the-mother-wavelet-function-used-for-computing-the-wavelet-features-by-slicerradiomic/13071

---

## Post #1 by @danceward (2020-08-18 13:22 UTC)

<p>Hello, I am doing some work about radiomic feature extraction from chest CT by SlicerRadiomic, and I want to know what was the mother wavelet function used for computing the wavelet features? Thanks!</p>

---

## Post #2 by @fedorov (2020-08-28 02:19 UTC)

<p>SlicerRadiomics is using <a href="https://github.com/Radiomics/pyradiomics">pyradiomics</a> for feature extraction, which in turn is using <a href="https://pywavelets.readthedocs.io/en/latest/ref/wavelets.html">pywavelets</a> for wavelet decomposition (see this <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/imageoperations.py#L831-L883">code</a>). The default type of wavelet decomposition pyradiomics is using is <code>coif1</code>.</p>

---
