# Data format of the probabilistic segmentation map for UKF Tractography module?

**Topic ID**: 40730
**Date**: 2024-12-17
**URL**: https://discourse.slicer.org/t/data-format-of-the-probabilistic-segmentation-map-for-ukf-tractography-module/40730

---

## Post #1 by @Ilya_Pshenichnyy (2024-12-17 17:42 UTC)

<p>I have been trying to use Option 2 in Seeding Options ( <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/UKFTractography" rel="noopener nofollow ugc">Documentation/Nightly/Modules/UKFTractography - Slicer Wiki</a>). I used Tracula generated probability distribution volume, normalized it to have 0 to 1 values as the documentation requires and tried float32 and uint8 +importing it as nii.gz and as .nrrd. Regardless, UKF tractography module outputs “Unsupported data type for seed file!”. Unfortunately, i could not find any requirements for data format in the module’s documentation.</p>

---
