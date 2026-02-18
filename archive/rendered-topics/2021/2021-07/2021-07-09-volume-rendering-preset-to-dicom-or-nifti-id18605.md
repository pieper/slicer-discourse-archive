# Volume rendering preset to dicom or NIFTI

**Topic ID**: 18605
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/volume-rendering-preset-to-dicom-or-nifti/18605

---

## Post #1 by @tpereira (2021-07-09 16:22 UTC)

<p>I have a CT scan and I am using the volume rendering preset CT-Bones. I want to save that into a dicom or a nifti or some other format. It could also be helpful if could segment based on the rendering preset or create a model from it. Let me know if any of this is possible. Thanks!</p>

---

## Post #2 by @lassoan (2021-07-12 04:13 UTC)

<p>Volume rendering is just a visualization technique, so you can just save the image as nifti and you can volume render that image the same way anywhere else.</p>
<p>CT-Bones preset has a ramp up from 0 opacity to 0.19 opacity in about 120HU, so you won’t be able to reproduce the exact same visual appearance with a solid surface, but you can go to Segment Editor module and try the Threshold effect to see what you get. For spine segmentation we worked out a very good protocol at the last project week. See more information <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW35_2021_Virtual/Projects/SpineSegmentation/README.md#spine-segmentation-protocol-for-training-data-generation">here</a>.</p>

---
