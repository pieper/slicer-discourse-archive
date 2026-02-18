# 103: Processed Images [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.

**Topic ID**: 24739
**Date**: 2022-08-13
**URL**: https://discourse.slicer.org/t/103-processed-images-scalar-volume-reference-image-in-series-does-not-contain-geometry-information-please-use-caution/24739

---

## Post #1 by @usmanqadir91 (2022-08-13 16:55 UTC)

<p>Hi</p>
<p>I have DICOM data and I am attempting to read the data using import DICOM files. The examine feature in the DICOM database presents warning “Reference image in series does not contain geometry information. Please use caution.” Upon clicking on the loading, I get the error “Could not load: Processed image as a scalar volume”.</p>
<p>Any assistance will be highly appreciated.</p>

---

## Post #2 by @pieper (2022-08-13 18:30 UTC)

<p>That basically means that the data doesn’t form a coherent volume.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---
