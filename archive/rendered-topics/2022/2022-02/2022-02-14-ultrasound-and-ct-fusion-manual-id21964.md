# Ultrasound and CT Fusion(manual)

**Topic ID**: 21964
**Date**: 2022-02-14
**URL**: https://discourse.slicer.org/t/ultrasound-and-ct-fusion-manual/21964

---

## Post #1 by @Young_Wang (2022-02-14 19:32 UTC)

<p>Hi there, I recently started a project focusing on multimodal imaging modality co-registration using 3Dslicer, specifically ultrasound and CT. From the initial literature review I conducted, the exact procedure seems to be straightforward. However, most papers seemed to ignore the fact that ultrasound has this fan pattern in the Cartesian space whereas the CT does not, which means that the registration thought fiducial points registration are technically the projection from the ultrasound slice to the CT slice due to the curvilinear nature of the ultrasound spacing in the Cartesian space. I wonder what is the best way to address this issue or it is okay to omit this problem based on your experience? I found this plugin <a href="https://www.kitware.com/3d-slicer-resamples-ultrasound-images/" rel="noopener nofollow ugc">https://www.kitware.com/3d-slicer-resamples-ultrasound-images/</a>, but I’m not sure what is the best practice in manual registration of CT and ultrasound. Any suggestion is welcome and greatly appreciated</p>

---
