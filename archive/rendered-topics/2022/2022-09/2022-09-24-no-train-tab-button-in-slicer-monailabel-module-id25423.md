---
topic_id: 25423
title: "No Train Tab Button In Slicer Monailabel Module"
date: 2022-09-24
url: https://discourse.slicer.org/t/25423
---

# No Train Tab/button in Slicer monailabel module

**Topic ID**: 25423
**Date**: 2022-09-24
**URL**: https://discourse.slicer.org/t/no-train-tab-button-in-slicer-monailabel-module/25423

---

## Post #1 by @amitjc (2022-09-24 19:30 UTC)

<p>Dear Experts,</p>
<p>Thank you for the Automated segmentation modules including monailabel.</p>
<p>I am working with Slicer 5.0.3 on Ubuntu 22.04 and look forward to train/refine models for use on local datasets, however the slicer monailabel module lacks the “Train” and “Stop” tabs/buttons under the “Active Learning” field.</p>
<p>I do encounter some “Traceback…” error, but slicer application launches seemlessly.<br>
Please find the error messages below:</p>
<pre><code class="lang-auto">'/home/ac/ApPz/Slicer-5.0.3-linux-amd64/Slicer' 
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/ac/ApPz/Slicer-5.0.3-linux-amd64/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/home/ac/ApPz/Slicer-5.0.3-linux-amd64/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelReviewer.py", line 23, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageData import ImageData
  File "/home/ac/ApPz/Slicer-5.0.3-linux-amd64/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelReviewerLib/__init__.py", line 14, in &lt;module&gt;
    from .ImageDataController import ImageDataController
  File "/home/ac/ApPz/Slicer-5.0.3-linux-amd64/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelReviewerLib/ImageDataController.py", line 19, in &lt;module&gt;
    from MONAILabelReviewerLib.ImageDataStatistics import ImageDataStatistics
ModuleNotFoundError: No module named 'MONAILabelReviewerLib.ImageDataStatistics'
loadSourceAsModule - Failed to load file "/home/ac/ApPz/Slicer-5.0.3-linux-amd64/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabelReviewer.py"  as module "MONAILabelReviewer" !
Fail to instantiate module  "MONAILabelReviewer"
The following modules failed to be instantiated:
   MONAILabelReviewer
Switch to module:  "Welcome"
</code></pre>
<p>I also tried launching Slicer nightly release to address this, however, this fails with following error:</p>
<pre><code class="lang-auto">/home/ac/ApPz/Slicer-5.1.0-2022-09-22-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libitkhdf5_hl-shared-5.3.so.1: cannot open shared object file: No such file or directory
</code></pre>
<p>Look forward to guidance to resolve these issues.</p>
<p>Thanks Again.</p>
<p>Best Regards,<br>
Amit.</p>

---

## Post #2 by @pieper (2022-09-24 20:26 UTC)

<p>Hi - thanks for reporting.</p>
<p>The first issue about MONAILabelReviewer occurs for me too on linux, but it doesn’t have any impact on the MONAI Label module itself, so you can ignore that for now (although the packaging of that module should be fixed at some point).  Could you <a href="https://github.com/Project-MONAI/MONAILabel/issues">file an issue</a> to be sure the MONAI developers are aware of this?</p>
<p>Also the issue with the nightly <a href="https://discourse.slicer.org/t/slicer-latest-preview-release-not-working-on-ubuntu-20/25361/4">was reported here</a> and there’s a patch so I expect the preview will be fixed soon.</p>
<p>The source of your issue not having the Train and Stop buttons is that they only show up after you connect to a server.  So you need to install and run MONAI Label server using the <a href="https://docs.monai.io/projects/label/en/latest/quickstart.html">instructions here</a>.</p>
<p>HTH</p>

---

## Post #3 by @amitjc (2022-09-25 04:11 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for your prompt response.</p>
<p>The Train and Stop tabs/buttons are absent, even while monailabel server (installed as per instructions at <a href="https://docs.monai.io/projects/label/en/latest/installation.html" rel="noopener nofollow ugc">https://docs.monai.io/projects/label/en/latest/installation.html</a>) is running.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> and monai team, seek your inputs on the same.</p>
<p>Best Regards,<br>
Amit.</p>

---

## Post #4 by @pieper (2022-09-25 15:07 UTC)

<p>And you clicked the button to fetch models?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bbcd2514b8d2e00588512d41b33f59a19bc157b.png" data-download-href="/uploads/short-url/1FPND4kajj7ChzWUcAQaqAck9C3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bbcd2514b8d2e00588512d41b33f59a19bc157b_2_690x87.png" alt="image" data-base62-sha1="1FPND4kajj7ChzWUcAQaqAck9C3" width="690" height="87" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bbcd2514b8d2e00588512d41b33f59a19bc157b_2_690x87.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bbcd2514b8d2e00588512d41b33f59a19bc157b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bbcd2514b8d2e00588512d41b33f59a19bc157b.png 2x" data-dominant-color="C6C6C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">742×94 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @amitjc (2022-09-25 16:36 UTC)

<p>Yes, had fetched the models.</p>

---

## Post #6 by @diazandr3s (2022-09-26 22:44 UTC)

<p>Dear <a class="mention" href="/u/amitjc">@amitjc</a>,</p>
<p>This is a bit strange. How did you install the module? Have you tried another Slicer version?</p>
<p>Please try with the preview release and let us know.</p>
<p>Also, can you please post a print screen of the MONAI Label module with the missing buttons?</p>

---
