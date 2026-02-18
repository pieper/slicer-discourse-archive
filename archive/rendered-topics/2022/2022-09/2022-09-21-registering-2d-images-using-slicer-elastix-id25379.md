# Registering 2D images using Slicer Elastix

**Topic ID**: 25379
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/registering-2d-images-using-slicer-elastix/25379

---

## Post #1 by @Krishna_Nanda (2022-09-21 16:55 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3<br>
Expected behavior: Completes successfully<br>
Actual behavior: Error during registration</p>
<p>Hello,</p>
<p>I am trying to register 2 X-ray images using the Slicer Elastix module with preset: generic (all). However the registration fails with the message “Error occurred during actual registration”. I also saw the following messages “Stopping Condition: Error in metric.” and “Description: ITK ERROR: Region ImageRegion (00000042EDDFCCD0)<br>
Dimension: 3<br>
Index: [-9223372036854775808, -9223372036854775808, -9223372036854775808]<br>
Size: [4, 4, 4]<br>
is outside of buffered region ImageRegion (0000019CA452D440)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [11, 11, 4]”.</p>
<p>I wanted to check if Slicer Elastix supports registration of 2D images as is, similar to say the original Elastix or Simple Elastix? Any advice on running this registration successfully will be helpful.</p>
<p>Thank you!</p>

---

## Post #2 by @Krishna_Nanda (2022-09-25 02:37 UTC)

<p>Hello, any suggestions will be greatly helpful, thank you!</p>

---

## Post #3 by @Krishna_Nanda (2023-01-10 12:04 UTC)

<p>Any pointers will be helpful, thank you!</p>

---

## Post #4 by @muratmaga (2023-01-10 17:28 UTC)

<p>If you want to do 2D registrations you are probably better of using the Elastix or ANTS directly, and not from Slicer.</p>
<p>Slicer treats every dataset, even if it is a single slice as if it is 3D. You can see from the output that there are three dimensions (4,4,4) reported for your data. Even if the registration concludes successfully, this is probably not going to be an ideal result (because every voxel can now move in 3D space as opposed in 2D as they should).</p>

---
