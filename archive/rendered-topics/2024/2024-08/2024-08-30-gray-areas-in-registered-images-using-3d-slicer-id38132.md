---
topic_id: 38132
title: "Gray Areas In Registered Images Using 3D Slicer"
date: 2024-08-30
url: https://discourse.slicer.org/t/38132
---

# Gray areas in registered images using 3D Slicer

**Topic ID**: 38132
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/gray-areas-in-registered-images-using-3d-slicer/38132

---

## Post #1 by @Nastaran (2024-08-30 18:25 UTC)

<p>Hello <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>I used 3D Slicer’s General Registration (BRAINS) to register brain CT images from two different modalities. An example of the resulting registered image with the <strong>background filled value set to 0.0</strong> shows gray areas that appeared after the registration process. However, after setting the <strong>background filled value to -1000</strong>, the gray parts changed to black, while other parts turned white.<br>
Could you please advise on how to address this issue?<br>
Thank you in advance.</p>
<p><img src="https://github.com/user-attachments/assets/7f116db8-a306-48be-96c5-20c662cb3e4a" width="200" height="167"></p>
<p><img src="https://github.com/user-attachments/assets/acb35f98-b455-4fef-a8ac-39a90580ee33" width="200" height="169"></p>

---

## Post #2 by @cpinter (2024-08-30 18:35 UTC)

<p>Please check the actual voxel values in the Data Probe, it might be a window/level issue. If you are not sure what these mean please refer to the documentation. Also I recommend actually using -3000 because that is the typical “background” value for CT as far as I know.</p>

---

## Post #3 by @Nastaran (2024-09-02 09:42 UTC)

<p>Thanks for getting back to me.<br>
I tried using -3000 as you suggested, but the results were the same as with -1000. However, after checking the window/level settings as you recommended, I discovered that the issue was indeed related to them. Thank you for pointing that out!</p>

---
