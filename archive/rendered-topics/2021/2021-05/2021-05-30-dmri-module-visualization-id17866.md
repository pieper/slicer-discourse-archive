---
topic_id: 17866
title: "Dmri Module Visualization"
date: 2021-05-30
url: https://discourse.slicer.org/t/17866
---

# DMRI module: visualization

**Topic ID**: 17866
**Date**: 2021-05-30
**URL**: https://discourse.slicer.org/t/dmri-module-visualization/17866

---

## Post #1 by @Nadya_Shusharina (2021-05-30 19:14 UTC)

<p>Is it possible to visualize specific individual components of the diffusion tensor?<br>
Could you please point me to the code?</p>

---

## Post #2 by @lassoan (2021-05-31 23:32 UTC)

<p>Yes. In Volumes module, select your DWI volume as “Active Volume” and then adjust the “DWI component” slider.</p>

---

## Post #3 by @Nadya_Shusharina (2021-06-01 02:03 UTC)

<p>Thank you. I meant that after the diffusion tensor is calculated from DWI, how to visualize each of the six individual elements of the tensor.</p>

---

## Post #4 by @pieper (2021-06-08 17:27 UTC)

<p>With SlicerDMRI you can get a variety of derived scalars from tensors:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DiffusionTensorScalarMeasurements" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DiffusionTensorScalarMeasurements</a></p>
<p>But to access individual elements of the tensor you would need to do some python scripting (e.g. assign tensor components to a new scalar volume node’s array).</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-values-in-a-dti-tensor-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-values-in-a-dti-tensor-volume</a></p>

---
