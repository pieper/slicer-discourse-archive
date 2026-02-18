# MonaiLabel on 8GB GPU

**Topic ID**: 27239
**Date**: 2023-01-14
**URL**: https://discourse.slicer.org/t/monailabel-on-8gb-gpu/27239

---

## Post #1 by @mau_igna_06 (2023-01-14 16:28 UTC)

<p>Hi</p>
<p>I was trying the vertebrae segmentation pipeline sample-app and I runned out of memory on a small CT</p>
<p>Does it make sense to spend time trying to reconfigure it to get it working? Will the quality of the modified algorithm be too low?</p>
<p>Could you give pointers/recommendations on cloud options?</p>
<p>Thanks a lot</p>

---

## Post #2 by @pieper (2023-01-14 16:36 UTC)

<p>I was having a similar problem running out of GPU memory.  I created a new conda environment and explicitly installed the CPU version of pytorch (using their install wizard: <a href="https://pytorch.org/get-started/locally/" class="inline-onebox">Start Locally | PyTorch</a>).  Running monailabel server in this environment bypassed the GPU.  Inference runs multithreaded is still pretty quick.</p>

---

## Post #3 by @mau_igna_06 (2023-01-14 17:33 UTC)

<p>I was trying to keep it very simple by using the Docker monai-label server because I just want to test one CT currently.<br>
I guess I’ll have to take more time than I initially planned to deploy anaconda, pytorch and monai-label</p>

---

## Post #4 by @pieper (2023-01-14 17:48 UTC)

<p>It’s really pretty straightforward to install miniconda and then install torch and monai label.  It really shouldn’t take more than a few minutes.  Let us know how it goes.</p>

---
