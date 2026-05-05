---
topic_id: 46911
title: "Totalsegmentator Fails To Install Pytorch Dependencies Insta"
date: 2026-05-04
url: https://discourse.slicer.org/t/46911
---

# TotalSegmentator fails to install PyTorch dependencies – installTorch() got unexpected keyword argument 'torchVisionVersionRequirement'

**Topic ID**: 46911
**Date**: 2026-05-04
**URL**: https://discourse.slicer.org/t/totalsegmentator-fails-to-install-pytorch-dependencies-installtorch-got-unexpected-keyword-argument-torchvisionversionrequirement/46911

---

## Post #1 by @Madison_Golledge (2026-05-04 12:46 UTC)

<p>I’m trying to use the <strong>T</strong>otalSegmentator extension in 3D Slicer for segmenting an MRI dataset, but I’m running into a consistent error during the dependency installation step.</p>
<p>When clicking “Apply” in the TotalSegmentator module, I get:</p>
<p>PyTorch Python package is required. Installing… (it may take several minutes)</p>
<p>Failed to install Python dependencies:<br>
PyTorchUtilsLogic.installTorch() got an unexpected keyword argument ‘torchVisionVersionRequirement’</p>
<h3><a name="p-133555-nvironment-1" class="anchor" href="#p-133555-nvironment-1" aria-label="Heading link"></a>nvironment:</h3>
<ul>
<li>
<p>OS: Windows (also tested on macOS with same error)</p>
</li>
<li>
<p>Slicer version: 5.11.0 (Preview)<br>
(Also tested on 5.10 stable with same issue</p>
</li>
<li>
<p>Extensions installed:</p>
<ul>
<li>
<p>TotalSegmentator (latest)</p>
</li>
<li>
<p>PyTorch (latest via Extensions Manager)</p>
</li>
<li>
<p>nnUNet (latest)</p>
</li>
</ul>
</li>
</ul>
<p>Observations: PyTorch appears installed and visible in Extensions Manager. Error occurs during the automatic dependency installation step triggered by TotalSegmentator. Suggests a mismatch between TotalSegmentator and PyTorchUtils API (unexpected argument)</p>
<p>Is this a known compatibility issue between TotalSegmentator and current PyTorchUtils versions? Is there a recommended Slicer version / extension version combination that avoids this? Is there a way to bypass the internal PyTorch installation step and point to an existing PyTorch install?</p>

---

## Post #2 by @Matteboo (2026-05-04 16:18 UTC)

<p>Have you tried MONAIAuto3DSeg<br>
It works for version 5.10</p>

---

## Post #3 by @lassoan (2026-05-04 19:26 UTC)

<p>Sorry, that’s due to a recent regression that I cause when fixing the macOS installation. I’ve fixed the issue now, please retry tomorrow. You can either use the latest Slicer Stable Release (Slicer-5.10) and update the TotalSegmentator extension; or install the latest Slicer Preview Release (Slicer-5.11) tomorrow.</p>

---

## Post #4 by @MGL (2026-05-04 23:31 UTC)

<p>hallo sir，could I try now？</p>

---

## Post #5 by @lassoan (2026-05-04 23:54 UTC)

<p>You can make <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/e5f0f8e6e3f5d857dd99217787fccc7f47418b6d">these changes</a> locally in <code>TotalSegmentator.py‎</code> file on your computer (you can find the location of the file in the error message in the Python console); or wait for the nightly builds to complete at around 10am EST.</p>

---

## Post #6 by @MGL (2026-05-05 00:22 UTC)

<p>thanks a lot sir!Really appreciate it!</p>

---

## Post #7 by @MGL (2026-05-05 00:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e28373ae14793a76d934ccb045bb00d08404f8af.png" data-download-href="/uploads/short-url/wjPxE0dfWFgVoUAvgHiUkc0t6RF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e28373ae14793a76d934ccb045bb00d08404f8af_2_690x186.png" alt="image" data-base62-sha1="wjPxE0dfWFgVoUAvgHiUkc0t6RF" width="690" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e28373ae14793a76d934ccb045bb00d08404f8af_2_690x186.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e28373ae14793a76d934ccb045bb00d08404f8af_2_1035x279.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e28373ae14793a76d934ccb045bb00d08404f8af_2_1380x372.png 2x" data-dominant-color="EDF3F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1973×533 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>Sorry sir,I cant find any changes when I try to modify your code locally.Did I do something wrong?thank for your reply again!</p>

---

## Post #8 by @lassoan (2026-05-05 00:37 UTC)

<p>Please copy here the complete error message. Don’t forget to reload the module or restart Slicer after you make the changes and save the file.</p>

---

## Post #9 by @MGL (2026-05-05 03:03 UTC)

<p>Failed to compute results.</p>
<p>Command ‘[‘D:/software/3D Slicer 5.10.0/bin/../bin\\PythonSlicer.EXE’, ‘D:\\software\\3D Slicer 5.10.0\\lib\\Python\\Scripts\\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/Lenovo/AppData/Local/Temp/Slicer/__SlicerTemp__2026-05-05_11+01+56.029/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Lenovo/AppData/Local/Temp/Slicer/__SlicerTemp__2026-05-05_11+01+56.029/segmentation’, ‘–device’, ‘gpu’, ‘–task’, ‘vertebrae_body’]’ returned non-zero exit status 1.</p>

---
