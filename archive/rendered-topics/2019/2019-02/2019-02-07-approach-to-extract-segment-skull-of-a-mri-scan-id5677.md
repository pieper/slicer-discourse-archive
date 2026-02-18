# Approach to extract/segment skull of a MRI scan

**Topic ID**: 5677
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/approach-to-extract-segment-skull-of-a-mri-scan/5677

---

## Post #1 by @SvK (2019-02-07 12:52 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.10</p>
<p>Hey everybody,<br>
I am looking for an approach to extract the complete skull reliably and accurately from an MRI of the head. My previous attempts with the Segment Editor and various additional extensions have not yet yielded satisfactory results. I have the feeling to overlook something, maybe some special tool or a crucial setting…</p>
<p>The dataset is a T1mprage. The biggest problem I see is that the bone has a rather heterogeneous structure. That’s why thresholding doesn’t work so easily…</p>
<p>I would be very grateful for any new approach or perhaps someone has already had good experience with a certain method.</p>
<p>best</p>
<p>Sven</p>

---

## Post #2 by @Viorel_Mirea (2022-04-08 00:24 UTC)

<p>Hi SvK,</p>
<p>Have you found a solution for this?<br>
I just started using 3D Slicer and I want to see if I can get out the shape of my skull from my MRI</p>
<p>Regards,<br>
Viorel</p>

---

## Post #3 by @slicer365 (2022-04-08 06:34 UTC)

<p>A good way is to use SPM12 based on Matlab,it can extract skull from T1MR .</p>

---

## Post #4 by @lassoan (2022-04-09 10:16 UTC)

<p>No need for Matlab for MRI skull stripping. There are multiple extensions for 3D Slicer that can do it:</p>
<ul>
<li>
<a href="https://github.com/lassoan/SlicerHDBrainExtraction">HDBrainExyraction</a>: uses deep learning, very robust and accurate, takes 10-20 seconds if you have CUDA-capable GPU, several minutes if running on the CPU</li>
<li>SwissSkullStripper: classic registration-based method, not as robust or accurate, but good enough if you use atlas image that is similar to your input image.</li>
</ul>
<p>However, the question was if it was possible to get the skull and remove everything else. This is a much harder task, because MRIs in general and particularly brain MRIs are optimized for imaging of soft tissues. Bone and air both appear as dark regions. You can try to segment these dark regions and your may get a shape that resembles the skull but it will be very noisy. If you want to get a detailed, accurate depiction of your skull then to can get it from a CT.</p>
<p>If you don’t need clinical accuracy (e.g., an art project) then your can warp someone else’s head CT to your MRI using image registration (by SlicerElastix or SlicerANTs extensions).</p>

---

## Post #5 by @jonel (2025-11-11 21:26 UTC)

<p>If you are still searching for a solution to this problem you might be interested in the new ModalityConverter extension: <a href="https://discourse.slicer.org/t/new-extension-modalityconverter-bringing-ai-medical-image-to-image-translation-to-3d-slicer/44405" class="inline-onebox">New extension: ModalityConverter - bringing AI medical image-to-image translation to 3D Slicer</a> You can use it to generate a synthetic CT from your MRI images, from which you can then easily extract the skull with the Segment Editor.</p>

---
