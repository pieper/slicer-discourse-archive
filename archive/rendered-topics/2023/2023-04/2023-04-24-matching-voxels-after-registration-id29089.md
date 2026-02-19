---
topic_id: 29089
title: "Matching Voxels After Registration"
date: 2023-04-24
url: https://discourse.slicer.org/t/29089
---

# Matching Voxels After Registration

**Topic ID**: 29089
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/matching-voxels-after-registration/29089

---

## Post #1 by @yonnif (2023-04-24 13:44 UTC)

<p>Hi,</p>
<p>I have two registered CT images that I’m trying to register to an MRI image. The CT images have matching matrices but they are different to the MRI image.</p>
<p>After successfully registering one of them with ANTs, the registered image and the MRI image have the same matrix sizes. However, when I apply the transform to the second CT image, the images are well registered but the matrix size is unchanged. It seems like it should be trivial to downsample the second CT image so it matches the matrix of the other two images but I cannot figure out how.</p>
<p>Any advice?</p>
<p>Thanks,<br>
Yonni</p>

---
