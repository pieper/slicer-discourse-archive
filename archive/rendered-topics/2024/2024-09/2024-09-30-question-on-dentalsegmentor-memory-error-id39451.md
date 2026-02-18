# Question on DentalSegmentor memory error

**Topic ID**: 39451
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/question-on-dentalsegmentor-memory-error/39451

---

## Post #1 by @alientex (2024-09-30 09:35 UTC)

<p>Hello,</p>
<p>I’ve selected cuda from the following device option in DentalSegmentor:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4aa752fb4dbf81218e3d6563323ec9222e9df4e.png" alt="image" data-base62-sha1="ulkqwsI3GZ1vqe8lXaFuCRb2cLY" width="488" height="57"></p>
<p>When I click on Apply button, I get the following error:</p>
<code>
####################################################################### Please cite the following paper when using nnU-Net: Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., &amp; Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211. ####################################################################### There are 1 cases in the source folder I am process 0 out of 1 (max process ID is 0, we start counting with 0!) There are 1 cases that I would like to predict Predicting volume: perform_everything_on_device: True Prediction on device was unsuccessful, probably due to a lack of memory. Moving results arrays to CPU
</code>
<p>RAM size: 16 GB<br>
GPU: NVidia Geforce GTX</p>
<p>Please help, Thank you.</p>

---

## Post #2 by @alientex (2024-10-01 03:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Could you help me solve this issue?</p>

---

## Post #3 by @lassoan (2024-10-01 04:37 UTC)

<p>You can try to crop and downsample your input image (using Crop volume module) to reduce memory need or try with a GPU with more memory.</p>
<p>You may also find more information in the application log.</p>

---
