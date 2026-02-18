# AI segmentation extension with GPU

**Topic ID**: 14681
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/ai-segmentation-extension-with-gpu/14681

---

## Post #1 by @Legendsevl (2020-11-19 02:33 UTC)

<p>Operating system:Win10<br>
Slicer version:4.11<br>
Expected behavior:local GPU accelerate<br>
Actual behavior:I know that volume rendering can accelerate GPU, but in other extensions, such as NVIDIA’s segmentation model, data is transmitted to the server for processing. Would you like to ask whether NVIDIA’s cloud is accelerated by GPU, or whether it can be accelerated by using local GPU</p>

---

## Post #2 by @lassoan (2020-11-19 02:36 UTC)

<p>You can speed up the AI segmentation by running NVidia AIAA server on your computer, using your GPU. Then transfer to the server will be almost immediate and since the processing itself usually takes just a couple of seconds, you will have segmentation in within about 10 seconds.</p>

---

## Post #3 by @Legendsevl (2020-11-19 03:06 UTC)

<p>Thank you for your timely reply, but could you describe in more detail how to use GPU to accelerate the AIAA model of NVIDIA on 3D slicer? If you can provide reference materials such as documents or videos, it would be very grateful</p>

---

## Post #4 by @lassoan (2020-11-19 04:16 UTC)

<p>You set up your server on your computer (there is a link to instructions in the <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#setup">extension’s documentation</a>) and then you specify your computer’s IP address in AIAA segment editor effect.</p>

---

## Post #5 by @Legendsevl (2020-11-19 07:05 UTC)

<p>Great, thanks for your reply</p>

---
