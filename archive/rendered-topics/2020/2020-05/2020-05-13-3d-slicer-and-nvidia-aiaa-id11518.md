# 3D Slicer and Nvidia AIAA

**Topic ID**: 11518
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/3d-slicer-and-nvidia-aiaa/11518

---

## Post #1 by @Ricardo (2020-05-13 11:26 UTC)

<p>Hi all.</p>
<p>I’m really interested in trying the Nvidia extension in title. Is it possible to know if a GPU like this <a href="https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/documents/75509_DS_NV_Quadro_K2200_US_NV_HR.pdf" rel="nofollow noopener">https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/documents/75509_DS_NV_Quadro_K2200_US_NV_HR.pdf</a> would be good enough for that?</p>
<p>Thank you so much.</p>

---

## Post #2 by @pieper (2020-05-13 11:49 UTC)

<p>I don’t think anyone has a lot of experience with th AIAA tools yet, but generally speaking recent nvidia cards all work pretty well with their software.  Probably need to check with nvidia if you really need to know for sure.</p>

---

## Post #3 by @lassoan (2020-05-13 13:41 UTC)

<p>4GB may not be enough if you want to train your own network but probably it can run pre-trained models.</p>
<p>Note that you can use it with the default server, as long as you don’t mind the data is uploaded to a remote server (data is deleted immediately after segmentation is complete, but there is no guarantee that the server cannot be hacked or your communications intercepted).</p>

---

## Post #4 by @Ricardo (2020-05-13 15:20 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>, thank you both.</p>
<p>Most of times I don’t think there’s any issue in sending data to remote servers, but at least 8GB VRAM might be necessary for other uses.</p>
<p>Once again, thank you.</p>
<p>Regards,<br>
Ricardo</p>

---
