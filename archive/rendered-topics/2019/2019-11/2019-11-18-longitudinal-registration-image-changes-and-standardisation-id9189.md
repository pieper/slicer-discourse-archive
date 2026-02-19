---
topic_id: 9189
title: "Longitudinal Registration Image Changes And Standardisation"
date: 2019-11-18
url: https://discourse.slicer.org/t/9189
---

# Longitudinal registration image changes and standardisation

**Topic ID**: 9189
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/longitudinal-registration-image-changes-and-standardisation/9189

---

## Post #1 by @RadioQuest (2019-11-18 13:02 UTC)

<p>Hi…</p>
<p>I am working on longitudinal brain images in a pediatric population to analysis change in texture in different parts of the brain.</p>
<p>These scans at later time points are registered with the initial scan to enable the selection of the same ROI. Registration performed is affine followed by BSplien to compensate for several brain changes.</p>
<p>What is the best way to justify the changes in texture features over specific areas of brain are due to radiation ( which I am studying) and not due to resampling done during registration / filtration/ processing etc?</p>
<p>Can have an area as a control in non-irradiated part help? or is there any better way to justify this?</p>
<p>Thanks.</p>
<p>Kind Regards</p>

---

## Post #2 by @lassoan (2019-11-18 14:56 UTC)

<p>Some texture features may be affected by resampling, so it makes sense to study the sensitivity of the features that you use.</p>
<p>For example, you can simulate new image acquisitions (by taking the original image, applying slight translation rotation, adding some random noise, maybe apply some spatially varying intensity modulation to simulate bias, add slight deformation, etc.) then run them through your registration pipeline. You can trust those texture features that give the same output for the simulated images as for the original image.</p>

---
