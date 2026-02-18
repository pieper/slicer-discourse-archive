# IBSI & pyRadiomic

**Topic ID**: 18137
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/ibsi-pyradiomic/18137

---

## Post #1 by @Chenglin_Zhu (2021-06-15 08:59 UTC)

<p>Dear community,</p>
<p>Are there any tutorials on setting the pyRadiomic to adhere to the IBSI? I wish to follow the IBSI standardization yet I am not willing to give up the convenience of pyRadiomic. If not, is there any recommendation on python packages for feature extraction that follow the IBSI?</p>
<p>Appreciate</p>

---

## Post #2 by @JonasB (2022-03-04 15:39 UTC)

<p>Hi,<br>
I know that MITK Phenotyping extracts IBSI defined Radiomics features:<br>
<a href="https://www.mitk.org/wiki/Phenotyping" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.mitk.org/wiki/Phenotyping</a></p>
<p>Best,<br>
Jonas</p>

---

## Post #3 by @JoostJM (2022-03-11 08:57 UTC)

<p>Replacement functions are available in <a href="https://github.com/AIM-Harvard/pyradiomics_ibsi-benchmark.git">PyRadiomics_IBSI-benchmark</a>, though this repo is setup to conduct tests to assess IBSI conformity.</p>
<p>I’m currently working on creating functionality in PyRadiomics that would allow users to perform fully-IBSI compliant extractions using PyRadiomics, it will be available in the next release.</p>
<p>The issue is that some IBSI functions contain functionality that breaks the code. Best example is the IBSI definition of bin edges for discretization when a resegmentation range is defined. This works fine when just extracting on the original image, but really messes up the extraction when filters are enabled (which were not part of the first IBSI publication).</p>

---

## Post #4 by @JonasB (2022-03-23 14:16 UTC)

<p>Thank you for your answer. Do you mean you extend the feature extraction to get the entire IBSI features in Pyradiomics? (<a href="https://discourse.slicer.org/t/missing-ibsi-fetaures-in-pyradiomics/22325" class="inline-onebox">Missing IBSI fetaures in Pyradiomics.</a>)</p>

---
