---
topic_id: 16956
title: "Different Values Of Radiomics Features Between Slicer Radiom"
date: 2021-04-06
url: https://discourse.slicer.org/t/16956
---

# Different values of radiomics features between slicer radiomics and pyradiomics

**Topic ID**: 16956
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/different-values-of-radiomics-features-between-slicer-radiomics-and-pyradiomics/16956

---

## Post #1 by @Yasuhiro_TAKEDA (2021-04-06 01:37 UTC)

<p>Hi</p>
<p>I got different values of radiomics features between slicer radiomics (GUI) and pyradiomics (CUI).<br>
How could that happen?</p>
<p>I read 5 MR images of brain, created 5 masks of tumor in 3d slicer, and performed radiomics using slicer radiomics (GUI).<br>
However, these values of radiomics in 2 out of 5 cases were slightly different from those that I got using pyradiomics (CUI), on the other hand, other values in 3 out of 5 were exactly the same as those of pyradiomics.<br>
I always used the same parameter file.</p>
<p>I would really appreciate your doing this for me.<br>
Thank you,</p>
<p>TAKEDA</p>

---

## Post #2 by @JoostJM (2021-04-12 07:49 UTC)

<p>There are several possibilities for those small differences. Did you compare the version of PyRadiomics used by SlicerRadiomics and PyRadiomics (CUI)? Are the differences small enough to be considered machine precision errors?</p>
<p>In the back end,SlicerRadiomics also uses PyRadiomics, which is installed in the slicer environment as part of the SlicerRadiomics setup.</p>

---

## Post #3 by @Yasuhiro_TAKEDA (2021-04-15 01:03 UTC)

<p>Thank you for your reply!</p>

---
