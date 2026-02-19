---
topic_id: 17947
title: "Total Number Of Radiomics Features"
date: 2021-06-04
url: https://discourse.slicer.org/t/17947
---

# Total number of radiomics features

**Topic ID**: 17947
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/total-number-of-radiomics-features/17947

---

## Post #1 by @Chenglin_Zhu (2021-06-04 09:55 UTC)

<p>Hello Slicer Community!</p>
<p>In Radiomics of Slicer, the maximum number of radiomic features is 130, which is mostly consistent with the number of features specified in the documentation of Pyradiomics (<a href="https://pyradiomics.readthedocs.io/en/latest/features.html#" class="inline-onebox" rel="noopener nofollow ugc">Radiomic Features — pyradiomics v3.0.1.post4+gad5b2de documentation</a> ).<br>
However, I read one research saying they extract about 1300 radiomic features using Pyradiomics, and a google search also specifies that " On average, Pyradiomics extracts ≈1500  features per image."</p>
<p>How to interpret these differences? And are there any disadvantages using Radiomic in Slicer than the Pyradiomics?</p>
<p>Appreciate.</p>

---

## Post #2 by @mina (2021-12-10 01:15 UTC)

<p>hello,<br>
that’s my question too.<br>
also, sometimes for unknown reason it extracts 140 features instead of 130 features!</p>

---

## Post #3 by @JoostJM (2022-01-11 11:33 UTC)

<p>The difference is due to the compounding effect of applying filters. This is possible in SlicerRadiomics if you use the parameters file. See the PyRadiomics documentation for more info.</p>

---

## Post #4 by @harad (2022-04-11 07:25 UTC)

<p>I went through all mentioned documentation but would be really helpful to provide a working SlicerRadiomics PARAMETERS FILE (one that instructs ALL possible image types and feature classes) as an example and courtesy to those of us who are not coding experts. I would be enormously grateful. Thanks in advance and best regards, Marko</p>

---

## Post #5 by @JoostJM (2022-05-03 07:42 UTC)

<p>Parameter files can be found in the repository <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings">here</a>. A good place to start would be <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/examples/exampleSettings/Params.yaml">Params.yaml</a>.</p>

---
