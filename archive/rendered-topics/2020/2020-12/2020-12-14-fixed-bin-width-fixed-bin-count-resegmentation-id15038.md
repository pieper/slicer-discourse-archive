# Fixed Bin Width / Fixed Bin Count + Resegmentation

**Topic ID**: 15038
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/fixed-bin-width-fixed-bin-count-resegmentation/15038

---

## Post #1 by @mcastro (2020-12-14 01:00 UTC)

<p>I am running 3D Slicer + Radiomics using Parameter Files.</p>
<p>In my application, I need to compare a set of CT images that have the same minimum HU but varying maximum HU. Using resegmentation, I thought that I would be able to set the same maximum HU for all images so, with a fixed bin width, all features would be comparable.</p>
<p>However, I noticed that resegmentation only affects the first order features. All other features remain the same, which means that the range is taken from the original segmentation, not the resegmentation.</p>
<p>Is there any way to achieve what I need,  that is to have the same bin width, with the same bin count by using the modified range from the resegmentation?</p>
<p>I found this, which I think suggests it is not possible (???):</p>
<p>“In PyRadiomics, gray value discretization using a fixed bin width always utilizes bin edges which are equally spaced from 0 and where the lowest gray level is ensured to be discretized to the first bin. Regardless of any resegmentation, etc.”</p>

---
