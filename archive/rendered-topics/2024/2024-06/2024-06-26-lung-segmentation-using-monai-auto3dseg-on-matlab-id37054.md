# Lung segmentation using monai auto3dseg on matlab

**Topic ID**: 37054
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/lung-segmentation-using-monai-auto3dseg-on-matlab/37054

---

## Post #1 by @sasurgan (2024-06-26 20:36 UTC)

<p>I want to use the monai auto3dseg lung model on matlab, I could not find the pre-trained model on the internet. I can access it as model.pt from the Slicer 3D cache folder but I am not sure how to use it. Can anyone help me?</p>

---

## Post #2 by @curtislisle (2024-06-27 00:10 UTC)

<p>Hi Sasurgan,<br>
The model file you found corresponds with the inference source code available here:<br>
<a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py" rel="noopener nofollow ugc">https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py</a></p>
<p>This is a PyTorch model. I am not aware of any way to run it from matlab, but you should be able to set up a python environment and run this script with the weight file you mentioned. I hope that helps. Good luck.</p>

---

## Post #3 by @lassoan (2024-06-27 03:11 UTC)

<p>I would suggest reevaluating the use of Matlab. While it is readily available in academic settings, many companies, regardless of size and funding, hesitate to rely on Matlab due to its high cost and proprietary nature. Companies prefer technologies they can control and afford. In the job market, skills in programming languages such as Python, JavaScript, and C++ and knowledge of open-source libraries are highly valued. On the other hand, only very few companies are interested in your Matlab experience.</p>

---
