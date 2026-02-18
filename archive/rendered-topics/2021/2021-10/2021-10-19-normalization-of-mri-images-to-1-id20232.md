# Normalization of MRI images to 1

**Topic ID**: 20232
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/normalization-of-mri-images-to-1/20232

---

## Post #1 by @Hadi (2021-10-19 11:49 UTC)

<p>Hi,<br>
I am working on MRI images of BraTs2020 image dataset. I want to normalized them to 1. I use the NormalizedImageFilter, But this does not happen and it is often seen in numbers greater than 1 (rage 2-3).<br>
Please guide me to this.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2021-10-20 02:51 UTC)

<p>You can change the intensity range of an image easily. For example, you can cast the image to float or double using Cast Scalar Volume module (an integer valued volume normalized to 0-1 would end up all black), and then you can use Simple Filters module → RescaleIntensityImageFilter).</p>
<p>However, this kind of image normalization and augmentation is typically done as part of your neural network training and not as a preprocessing step - see TorchIO and MONAI examples.</p>

---

## Post #3 by @Hadi (2021-10-20 18:07 UTC)

<p>Thank you for your answer.<br>
It is works very well.</p>

---
