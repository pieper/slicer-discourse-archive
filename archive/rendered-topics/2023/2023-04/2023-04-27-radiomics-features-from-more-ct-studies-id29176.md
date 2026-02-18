# Radiomics features from more CT studies

**Topic ID**: 29176
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/radiomics-features-from-more-ct-studies/29176

---

## Post #1 by @Tomas_Korinek (2023-04-27 15:12 UTC)

<p>Please,</p>
<p>is there any way extract radiomics features from Slicer 3D application in “one step”?<br>
I mean. I have 200 patient studies (CTs, RT Structure Sets).<br>
I can load them in Slicer 3D. I would like to extract radiomics features for rectum, PTV and bladder for all patients in “one click”.<br>
Is there any way, how to do it?</p>
<p>I am able to make segmentation for one patient including rectum, bladder, PTV in Segmentation module, than go to Radiomics and extract features for these structures into one Table. Or do I have to do in step by step for each patient?</p>
<p>Do you have any idea how to do it? I would really appreciate it.<br>
Thank you very much for your help!</p>
<p>Thomas, Czech Republic.</p>

---

## Post #2 by @pieper (2023-04-27 17:43 UTC)

<p>We recommend writing python scripts for this, something like what’s <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing">described here</a>.</p>

---
