# Sandbox related extensions installing and running. Could not find Stitcher and could not run total segmentator

**Topic ID**: 27768
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/sandbox-related-extensions-installing-and-running-could-not-find-stitcher-and-could-not-run-total-segmentator/27768

---

## Post #1 by @Elmahdy (2023-02-11 13:56 UTC)

<p>Salamo alekom (hello everybody) I am trying to use sandbox extension; I installed SANDBOX on (ver5.2.1). I searched (CTRL+F) for stitcher. I did not find it. Also, when trying to run Total segmentator. it prompts me to install PYtorch( I instilled and updated it).</p>

---

## Post #2 by @lassoan (2023-02-11 20:02 UTC)

<p>I can confirm that after installing the Sandbox extension in Slicer-5.2.1, the Stitch Volumes module is available:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d06f13efbfcbde3d4185e8c1c0a65a113da20cf9.png" data-download-href="/uploads/short-url/tJTiq50rOOhCHERo2hDCL3w85rX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d06f13efbfcbde3d4185e8c1c0a65a113da20cf9_2_690x459.png" alt="image" data-base62-sha1="tJTiq50rOOhCHERo2hDCL3w85rX" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d06f13efbfcbde3d4185e8c1c0a65a113da20cf9_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d06f13efbfcbde3d4185e8c1c0a65a113da20cf9_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d06f13efbfcbde3d4185e8c1c0a65a113da20cf9_2_1380x918.png 2x" data-dominant-color="3D3E40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1841×1225 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can try reinstalling Slicer from scratch and if you still have problems then upload the application log somewhere and post the link here.</p>
<aside class="quote no-group" data-username="Elmahdy" data-post="1" data-topic="27768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/b2d939/48.png" class="avatar"> Elmahdy:</div>
<blockquote>
<p>when trying to run Total segmentator. it prompts me to install PYtorch( I instilled and updated it)</p>
</blockquote>
</aside>
<p>Please delete your entire Slicer installation folder and follow the <a href="https://github.com/lassoan/SlicerTotalSegmentator#setup">TotalSegmentator setup instructions</a> word-by-word. If you find any difference in what you see and what you expect, stop immediately, take a screenshot and copy the logs and create a new topic on this forum to ask for help.</p>

---

## Post #3 by @Elmahdy (2023-02-13 15:05 UTC)

<p>Thanks a lot for your reply, it WORKED!!. In total segementator i understand there is a fast mode, What the difference? would it affect the statistics(quantification as volume, area, and size) driven from the segment ?</p>
<p>Thanks in advance</p>

---

## Post #4 by @lassoan (2023-02-13 15:09 UTC)

<p>Fast mode uses 3mm cubes for segmenting objects (instead of 1.5mm of the full-resolution segmentation). Probably size differences are negligible for most use cases, but you need to test if it makes a difference for you. You can run the full-resolution segmentation on CPU, you just need to wait more for the result (about 40 minutes).</p>

---

## Post #5 by @Elmahdy (2023-02-13 15:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0f13825bb3355bd8488c841cfddaadbb65dbdf1.png" data-download-href="/uploads/short-url/yntoYRpWT3oS1tFEyG3KSJU7fzj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0f13825bb3355bd8488c841cfddaadbb65dbdf1.png" alt="image" data-base62-sha1="yntoYRpWT3oS1tFEyG3KSJU7fzj" width="690" height="36" data-dominant-color="EDEDDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1109×59 4.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have CUDA 11.7 but i do not think it is running<br>
I enabled it through NEVDA control panel, but still</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2ab281561c0cc3a44f375018053eae95364ed4f.png" data-download-href="/uploads/short-url/nd23bUB3WeLWEMBvGcaCFC72HQH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2ab281561c0cc3a44f375018053eae95364ed4f.png" alt="image" data-base62-sha1="nd23bUB3WeLWEMBvGcaCFC72HQH" width="612" height="500" data-dominant-color="EBEEF2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">671×548 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am not sure if running on GPU</p>

---

## Post #6 by @rbumm (2023-02-13 15:30 UTC)

<p>You can paste</p>
<pre><code class="lang-auto">import torch
print(torch.cuda.is_available())
</code></pre>
<p>into 3D Slicers Python console to check this.</p>

---

## Post #7 by @Elmahdy (2023-02-13 16:25 UTC)

<p>I was trying it again it comes back with this error msg<br>
Traceback (most recent call last):<br>
File “C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 749, in process<br>
self.logProcessOutput(proc)<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/ProgramData/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/M2/AppData/Local/Temp/Slicer/__SlicerTemp__2023-02-13_11+22+31.867/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/M278837/AppData/Local/Temp/Slicer/__SlicerTemp__2023-02-13_11+22+31.867/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #8 by @Elmahdy (2023-02-13 16:37 UTC)

<p>came back true. Still slow</p>

---

## Post #9 by @lassoan (2023-02-13 18:02 UTC)

<p>If you don’t have a powerful GPU or CUDA version is not supported by pytorch then you have to force using the CPU as described <a href="https://github.com/lassoan/SlicerTotalSegmentator#segmentation-fails-while-predicting">here</a>.</p>
<p>If you have Intel Integrated Graphics + discrete NVIDIA GPU in your system then make sure that in NVIDIA settings you set <code>SlicerApp-real.exe</code> to use the NVIDIA GPU.</p>

---

## Post #10 by @Elmahdy (2023-02-13 18:52 UTC)

<p>I checked the box with fast option and I had this previous mentioned error message</p>

---
