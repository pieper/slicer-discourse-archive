# Radiomics result validation

**Topic ID**: 15181
**Date**: 2020-12-22
**URL**: https://discourse.slicer.org/t/radiomics-result-validation/15181

---

## Post #1 by @vinartrulz (2020-12-22 05:09 UTC)

<p>Hello everyone.<br>
I am interested to know about the result validation strategy followed by libraries like pyradiomics.<br>
While looking through the unit test cases, I found the results are validated against golden data. How was this golden data created and how was its correctness ensured?</p>

---

## Post #2 by @JoostJM (2021-03-09 12:37 UTC)

<p>The baseline data in PyRadiomics was first created using the same software tool used to extract features in the publication by <a href="https://pubmed.ncbi.nlm.nih.gov/24892406/">Aerts et al (Nat. Com. 2014)</a>. After this, changes were only made to the baseline when this was due to intended changes in the code that were expected to yield different results.</p>
<p>As such, it mainly serves to act as a check that changes in the PyRadiomics code do not cause unintentional changes in the values of extracted features.</p>
<p>Besides this, PyRadiomics adheres to the standard described by IBSI in most cases, with documentation detailing how and why some differences exist.</p>

---
