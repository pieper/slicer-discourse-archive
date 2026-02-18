# CUDA is not currently available on your system -DentalSegmentator problem

**Topic ID**: 43738
**Date**: 2025-07-16
**URL**: https://discourse.slicer.org/t/cuda-is-not-currently-available-on-your-system-dentalsegmentator-problem/43738

---

## Post #1 by @tarikau (2025-07-16 10:21 UTC)

<p>Hello,<br>
I’ve installed DentalSegmentator extension together with PyTorch extension. When I click on Apply, it says:<br>
“Selected device (CUDA) is not currently available on your system and will default to CPU device.<br>
Running the segmentation may take up to 1 hour.<br>
Would you like to proceed?”</p>
<p>When I check CUDA and PyTorch on Slicer:</p>
<p>print(torch.<strong>version</strong>)<br>
2.7.0+cpu<br>
print(torch.version.cuda)<br>
None<br>
print(torch.cuda.is_available())<br>
False</p>
<p>It gives these infos but I have CUDA installed (CUDA Version: 12.9).<br>
Also I have NVIDIA GeForce RTX 4090.</p>
<p>How can i solve this problem?</p>

---

## Post #2 by @tarikau (2025-07-16 11:41 UTC)

<p>I managed to solve my own problem. Apparently PyTorch is using only CPU as default at least on my case. I changed that form PyTorch Utils extention.</p>

---
