---
topic_id: 31132
title: "Error Vtktransformpolydatafilter Cxx 82 No Input Data"
date: 2023-08-14
url: https://discourse.slicer.org/t/31132
---

# Error: vtkTransformPolyDataFilter.cxx:82 - No input data

**Topic ID**: 31132
**Date**: 2023-08-14
**URL**: https://discourse.slicer.org/t/error-vtktransformpolydatafilter-cxx-82-no-input-data/31132

---

## Post #1 by @RadmirGareev (2023-08-14 05:44 UTC)

<p>Hello!<br>
I often get an error:<br>
[ERROR][VTK] 14.08.2023 00:41:48 [vtkTransformPolyDataFilter (0000016FB7796AE0)] (vtkTransformPolyDataFilter.cxx:82) - No input data<br>
[ERROR][VTK] 14.08.2023 00:41:48 [vtkTransformPolyDataFilter (0000016FB7795370)] (vtkTransformPolyDataFilter.cxx:82) - No input data</p>
<p>It occurs when I try to use  Segment Editor: I did not notice any relation with use of any specific tool in segment editor. Computer just freezes, stops responding to commands and spontaneously reboots. No error message appears in this case.<br>
I tried to perform similar segmentation on a working PC (much weaker) on the same dataset - there was no error.<br>
Here are the characteristics of the computer on which the error occurs: Intel Core i5-12400 2.5 GHz, 64 GB of RAM, NVIDIA GeForce RTX 3060 12 Gb, 574 GB free on the hard drive.<br>
The video card driver is fresh - updated yesterday.<br>
I have installed CUDA Toolkit (<a href="https://developer.nvidia.com/cuda-downloads?target_os=Windows&amp;target_arch=x86_64&amp;target_version=11" class="inline-onebox" rel="noopener nofollow ugc">CUDA Toolkit 12.2 Update 1 Downloads | NVIDIA Developer</a>), PyTorch (used this tutorial - <a href="https://pytorch.org/get-started/locally/" class="inline-onebox" rel="noopener nofollow ugc">Start Locally | PyTorch</a>), Numpy (<a href="https://numpy.org/install/" class="inline-onebox" rel="noopener nofollow ugc">NumPy - Installing NumPy</a>) - for MONAIlabel use.<br>
It seems that during the installation of PyTorch or Numpy, the drivers for CUDA were reinstalled, but I’m not completely sure about this.<br>
I work with MRI - T1 3D of the brain: matrix 256 * 256, 192 slices - voxel size ~ 1 * 1 * 1 mm, weighs about 40 mb. The error also occurs on images in T2 sequence - 350 * 448, 5 mm, 25 slices each, weighs about 10 mb.<br>
I tried to increase the virtual memory from the default value to 15000-30000 MB - such advice came across on the Slicer forum. Tried older version of Slicer (5.0.2), stable version (5.2.2), preview (5.3.0) - error repeats.<br>
I tried to open the same study in the Radiant viewer and perform multiplanar reconstruction, 3D reconstruction - there were no errors or slowdowns.<br>
Here is last error logs (error logs were not saved on the older version of Slicer) - <a href="https://drive.google.com/drive/folders/1jqQTaJ-I_R1ZFMSsiDV4WtkPLuvpV849?usp=drive_link" class="inline-onebox" rel="noopener nofollow ugc">error logs slicer - Google Drive</a>.<br>
If this information is important, then the event codes in the windows log after the error occurs are: 360, 63, 1, 7023, 7009, 6155, 15, 1101, 41, 56, 6008.<br>
Thank you</p>

---

## Post #2 by @lassoan (2023-08-14 06:19 UTC)

<aside class="quote no-group" data-username="RadmirGareev" data-post="1" data-topic="31132">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/radmirgareev/48/67166_2.png" class="avatar"> RadmirGareev:</div>
<blockquote>
<p>Computer just freezes, stops responding to commands and spontaneously reboots</p>
</blockquote>
</aside>
<p>It should be impossible for any application to make your computer freeze and restart. It may be overheating, but can be other hardware, driver, or configuration issue.</p>
<p>Can you provide more details about the errors in the Windows event log? They may give hints about what goes wrong.</p>

---

## Post #3 by @RadmirGareev (2023-08-14 21:19 UTC)

<p>Thank you for reply!<br>
I check Windows event logs and find suspicious one (in my subjective opinion) - WHEA-Logger 1 (0x8000000000000002). I tried to perform /Restorehealth and /SCANNOW from cmd - it didn’t help.<br>
There is another errors and warnings in windows erroe log - but they were repeated when forced to restart the PC without use of 3D Slicer (I tried to separate errors and warnings caused directly by the restart button).<br>
I attach suspicious event log and another logs after crash here: <a href="https://drive.google.com/drive/folders/1dFK5YI4aAnIjazPUjHuSvhlFNX73srsZ?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">windows error logs - Google Drive</a>.<br>
Judging by the time in the 3D Slicer and Windows logs, the Windows error logs appeared only after the PC was rebooted, but not during the occurrence of an error in the 3D Slicer. There is a small time gap between them - probably the time of a PC restart.<br>
Thank you</p>

---

## Post #4 by @lassoan (2023-08-14 23:21 UTC)

<p>The <code>A fatal hardware error has occurred.</code> error logged by WHEA may indicate an actual hardware error. Have you built this PC or have you added any extra hardware yourself? You may try to remove the GPU, remove memory modules one-by-one and see if that makes a difference. You can also have a look at the <code>Application</code> log in the Windows Event Viewer.</p>

---

## Post #5 by @RadmirGareev (2023-08-15 06:11 UTC)

<p>Thanks for the answer!  This PC was built in the store, I didn’t add any of the hardware myself.  I will try to do as you said with GPU and memory and check the Application log in the Windows Event Viewer again.<br>
Thank you</p>

---

## Post #6 by @RadmirGareev (2023-08-26 16:13 UTC)

<p>Hello!  You were right about the hardware.  I took the computer to the service: they said that the problem was in the compatibility between the RAM and the motherboard.  Replacing the RAM solved the problem.  Thanks for giving me the right idea.</p>

---
