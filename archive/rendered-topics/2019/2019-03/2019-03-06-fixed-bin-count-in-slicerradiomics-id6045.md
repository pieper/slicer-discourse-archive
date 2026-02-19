---
topic_id: 6045
title: "Fixed Bin Count In Slicerradiomics"
date: 2019-03-06
url: https://discourse.slicer.org/t/6045
---

# Fixed bin count in SlicerRadiomics

**Topic ID**: 6045
**Date**: 2019-03-06
**URL**: https://discourse.slicer.org/t/fixed-bin-count-in-slicerradiomics/6045

---

## Post #1 by @Karin_Meijer (2019-03-06 17:19 UTC)

<p>Hello,</p>
<p>Currently I am using the SlicerRadiomics extension and I noticed that features can only be calculated with a fixed bin width, which can be manually set. However, for my analysis I would prefer a fixed bin count. Is it for this extension in any way possible to change this setting to a fixed bin count of 64?</p>
<p>Thank you in advance.</p>
<p>Kind regards,<br>
Karin Meijer</p>

---

## Post #2 by @fedorov (2019-03-06 17:24 UTC)

<p>You can use fixed bin count, but you will need to customize extraction using a “parameter file customization” instead of “manual customization”.</p>
<p>Please consult pyradiomics manual for how to prepare the parameter file: <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file" class="inline-onebox">Customizing the Extraction — pyradiomics v3.1.0rc2.post5+g6a761c4 documentation</a>, also see this relevant FAQ entry: <a href="https://pyradiomics.readthedocs.io/en/latest/faq.html#what-about-gray-value-discretization-fixed-bin-width-fixed-bin-count" class="inline-onebox">Frequently Asked Questions — pyradiomics v3.1.0rc2.post5+g6a761c4 documentation</a>.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb71b86a03d0f5c6ee6512a36684f99003766494.png" alt="image" data-base62-sha1="zSnumYc56XrfU1c1gXA7BaZDTzC" width="657" height="488"></p>

---

## Post #3 by @Karin_Meijer (2019-03-11 09:40 UTC)

<p>Hi Andrey,</p>
<p>Thank you for your fast response.<br>
I will try to prepare a parameter file with the right settings.</p>
<p>Kind regards,<br>
Karin Meijer</p>

---
