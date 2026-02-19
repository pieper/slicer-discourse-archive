---
topic_id: 33807
title: "Parameternodewrapper With Dynamic Minimum Maximum"
date: 2024-01-16
url: https://discourse.slicer.org/t/33807
---

# ParameterNodeWrapper with dynamic Minimum/Maximum

**Topic ID**: 33807
**Date**: 2024-01-16
**URL**: https://discourse.slicer.org/t/parameternodewrapper-with-dynamic-minimum-maximum/33807

---

## Post #1 by @che85 (2024-01-16 22:22 UTC)

<p>Hi,</p>
<p>I am working on adapting some code to use the <code>parameterNodeWrapper</code> and was wondering if there is any way to set the validator’s Minimum and Maximum values of ctkSliderWidget dynamically at runtime.</p>
<h2><a name="p-105566-use-case-1" class="anchor" href="#p-105566-use-case-1" aria-label="Heading link"></a>Use case</h2>
<p>I have a volume sequence selector in the UI which upon selection should set the maximum value of the slider to the <code>number of data nodes -1</code>.</p>
<p>I can directly set the maximum of the slider, but I will receive a ValueError when exceeding the initially set Minimum/Maximum.</p>
<p>Similarly, it would be interesting to validate the value of one parameter to be smaller/larger than another parameter.</p>

---

## Post #2 by @che85 (2024-01-16 23:11 UTC)

<p>Since there is already a binding between the UI and the parameter node, could we simply update the UI component’s minimum/maximum values and adjust the validation parameters accordingly?</p>
<p>Is there a way to access the validator directly through the parameterNodeWrapper?</p>

---
