---
topic_id: 48643
title: "Workflow Advice: Preclinical rat brain CT hemispheric volumetry"
date: 2026-10-29
url: https://discourse.slicer.org/t/48643
last_bumped: 2026-10-29T19:56:25.585Z
---

# Workflow Advice: Preclinical rat brain CT hemispheric volumetry

**Topic ID**: 48643
**Date**: 2026-10-29
**URL**: https://discourse.slicer.org/t/workflow-advice-preclinical-rat-brain-ct-hemispheric-volumetry/48643

---

## Post #1 by @kbroeren (2026-10-29 19:56 UTC)

<p>Hello,</p>
<p>I am working with micro-CT scans of rat brains to quantify hemispheric tissue loss following Controlled Cortical Impact using the method: % Tissue loss = (Vcontra-V ipsi)/(V contra). There are three specific steps that I am looking for recommendations on.</p>
<ol>
<li>Our scans are frequently off-center, which makes it hard to accurately split the brain into two hemispheres.</li>
</ol>
<ul>
<li>What approach should I take to rotate/re-slice the volume before dividing it into the left and right hemispheres?</li>
<li>Once it is aligned, is there an established way to define a cutting plane to partition the brain down the midsagittal plane?</li>
</ul>
<ol start="2">
<li>Standardizing anatomical boundaries. The olfactory bulbs, and cerebellum were dissected prior to scanning, but some remnants remain.</li>
</ol>
<ul>
<li>What tools are recommended to establish anterior/posterior cutoffs so that remnant tissue is excluded uniformly across all subjects?</li>
<li>How do I do this without sacrificing some of the cortical area?</li>
</ul>
<ol start="3">
<li>Suppressing Surface Spikes/Noise. Due to noise at the tissue boundary, intensity thresholding results in a jagged dorsal cortical surface rather than smooth contour.</li>
</ol>
<ul>
<li>Which tool can I use to preserve the true cortex without distorting the lesion area?</li>
</ul>
<p>Any advice helps!</p>
<p>Thank you</p>

---
