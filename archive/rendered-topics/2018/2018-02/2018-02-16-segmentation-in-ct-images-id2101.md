# Segmentation in CT images

**Topic ID**: 2101
**Date**: 2018-02-16
**URL**: https://discourse.slicer.org/t/segmentation-in-ct-images/2101

---

## Post #1 by @afsanehlahooti (2018-02-16 17:34 UTC)

<p>Hi guys,<br>
I want to segment the tumor in CT images from head and neck cancers. Do you know what the best module in 3DSlicer 4.8 is? (I am not a radiologist.)<br>
Thanks a lot.</p>

---

## Post #2 by @gcsharp (2018-02-16 17:59 UTC)

<p>Head and neck cancer is a heterogenous group of diseases which vary in location and presentation.  Manual contouring using the segmentation editor will probably be best.</p>
<p>Since you mention you are not a radiologist, do you mean that you are not confident in identifying the tumor?  It may help if you explain your project goal.</p>

---

## Post #3 by @afsanehlahooti (2018-02-16 18:02 UTC)

<p>Yes, I am not confident in identifying the tumor. I want to extract some radiomics features in Head and neck cancer pre and post-treatment.</p>

---

## Post #4 by @gcsharp (2018-02-16 20:24 UTC)

<p>In that case, I suggest you ask an expert to perform the segmentation.  Automatic delineation of H&amp;N tumors in CT is beyond the current state of the art.</p>

---

## Post #5 by @timeanddoctor (2018-02-18 03:31 UTC)

<p>A CTA of neck tumor may be help for you to segment the ROI through the module “segment”.<br>
I caculated the volume of a “cancerous goiter” from CTA, which is interesting to measure the I131 for a patient.</p>

---
