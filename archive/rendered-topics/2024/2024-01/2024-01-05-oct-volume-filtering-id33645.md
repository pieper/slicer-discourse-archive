# OCT volume filtering

**Topic ID**: 33645
**Date**: 2024-01-05
**URL**: https://discourse.slicer.org/t/oct-volume-filtering/33645

---

## Post #1 by @boiler (2024-01-05 18:01 UTC)

<p>Hello Everyone,<br>
I’ve an OCT image which is grainy and noisy in DICOM format, which I can load successfully in 3D Slicer. The same data viewed in the software of the device looks smoothly and more details are visible. I’m pretty sure the software of the OCT scanner is doing some 3D filtering, maybe with 3D shearlet transformations. Is there any similar stuff I can do in 3D Slicer?<br>
Thanks a lot!</p>

---

## Post #2 by @pieper (2024-01-05 19:55 UTC)

<p>If you want to try a range of filter options the SimpleFilters module exposes a lot of what’s in <a href="https://itk.org/">ITK</a>.</p>

---

## Post #3 by @boiler (2024-01-06 09:29 UTC)

<p>Thanks for  response. For some reason, I cannot select the volume to apply a 3D filter with the data I have. I can choose the volume for rendering</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7672f9e8c4b4d26b49ae23eb53ec3501a679e3c.png" alt="grafik" data-base62-sha1="x15mYV5DK080mBuNMFzK81SgFMU" width="535" height="286"></p>
<p>but not in the ITK simple filters dialog:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bebdc6cfa99d14a9af94d5ee19a14bed43ee48a.png" alt="grafik" data-base62-sha1="3Z0dK0gwq9AMLfnCb1x5175lxHk" width="521" height="227"><br>
The drop down will not just open to let me choose a volume.</p>

---

## Post #4 by @boiler (2024-01-06 16:13 UTC)

<p>Got it! I’ve to convert it to a scaler volume. Has somebody a tip for filtering an OCT image…? I’m quite new into this topic.</p>

---

## Post #5 by @pieper (2024-01-06 17:16 UTC)

<p>Maybe you can share some screenshots of what the data looks like before filtering and what other systems produce post-filtering so people can see what you’re after and make suggestions.  Sometimes a median filter and/or a gradient anisotropic filter can remove noise and preserve features.</p>

---
