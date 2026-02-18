# Mac OS And AI segmentation with CIP:

**Topic ID**: 29232
**Date**: 2023-05-01
**URL**: https://discourse.slicer.org/t/mac-os-and-ai-segmentation-with-cip/29232

---

## Post #1 by @jack_richecoeur (2023-05-01 15:30 UTC)

<p>Operating system:Mac os Ventura 24Giga RAM *radeon Pro 5300 4 giga<br>
Slicer version:5.2.2<br>
Expected behavior: AI lung segmentation.<br>
Actual behavior: does not work, with messages Error Pytorch CUDA not found ( OK because is a mac oS) and failed to compute results :Errno2 : no such file or directory.<br>
torch, torchvision, torchaudio installed as recommended on Pytorch site<br>
-Python3.11.3<br>
Anaconda<br>
Homebrew<br>
Pip3 -all installed with recent versions.<br>
How to do?<br>
second question: With high lung densities corresponding to not aerated areas, the segmentation don’t take into account these areas and lung volumes don’t fit with well so I use segment editor to complete the segmentation but it’s time consuming.<br>
Do you have a other way, best setting (we  dont not set the higher density thresold up to 0).<br>
Thank you for your help.</p>

---

## Post #2 by @rbumm (2023-05-01 17:05 UTC)

<p>Could you also start all over again fresh installation, please?</p>
<p><a href="https://discourse.slicer.org/t/totalsegmentator-error-at-first-run-command-pip-install-git-https-github-com-wasserth-totalsegmentator-git-no-deps-returned-non-zero-exit-status/26715/38">See here</a> for a description.</p>

---

## Post #3 by @rbumm (2023-05-01 17:07 UTC)

<p>We will deal with the second question later.</p>

---
