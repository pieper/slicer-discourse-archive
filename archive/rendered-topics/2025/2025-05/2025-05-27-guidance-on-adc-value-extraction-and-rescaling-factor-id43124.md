---
topic_id: 43124
title: "Guidance On Adc Value Extraction And Rescaling Factor"
date: 2025-05-27
url: https://discourse.slicer.org/t/43124
---

# Guidance on ADC Value Extraction and Rescaling Factor

**Topic ID**: 43124
**Date**: 2025-05-27
**URL**: https://discourse.slicer.org/t/guidance-on-adc-value-extraction-and-rescaling-factor/43124

---

## Post #1 by @nima_Taghizadeh (2025-05-27 22:26 UTC)

<p>Hello everyone,</p>
<p>I am currently working with ADC values extracted from inhomogeneity bias-corrected brain MRIs obtained through SAMSEG and have encountered a few issues that I would greatly appreciate your insights on.</p>
<ol>
<li>
<p>Units for ADC Values: When extracting ADC values for my ROIs, including, using 3D Slicer, I noticed that no unit was provided for the ADC values, neither in the software nor in the imaging visualization tools (PACS, VISAGE). I also checked the DICOM metadata for ADC and DWI MRIs but could not find any relevant tags related to ADC values, rescaling, or intersection. As a result, I am uncertain about the unit or scale used for the ADC values.</p>
</li>
<li>
<p>Discrepancy in ADC Value Range: The mean ADC values extracted from the bias-corrected image for my ROIs were in the range of 150-250. These values seem far away than the normal average ADC values for these structures. I suspected that the bias correction might have influenced these values, so I also extracted the values from the original ADC image. In this case, the values ranged from 1200-1500 for ROIs. However, I still could not identify any unit or rescaling factor.</p>
</li>
</ol>
<p>Considering that the average normal ADC values for my ROI is around 1000 to 1500 x 10^-6 mm²/s, I have two questions:</p>
<ol>
<li>
<p>For extracting radiomics features (including ADC values) from the ADC image, would you recommend using the bias-corrected image or the original ADC image as the scalar volume?</p>
</li>
<li>
<p>Based on the values I found, it seems there may be a rescaling factor (e.g., 10^(-6) or 10^(-5)). Would you happen to know where I might find the rescaling factor, or how I could confirm it?</p>
</li>
</ol>
<p>I would greatly appreciate any guidance you could provide on these issues.</p>
<p>Thanks,<br>
Nima</p>

---
