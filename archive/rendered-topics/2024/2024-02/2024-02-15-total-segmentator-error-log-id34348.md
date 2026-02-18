# Total segmentator error log

**Topic ID**: 34348
**Date**: 2024-02-15
**URL**: https://discourse.slicer.org/t/total-segmentator-error-log/34348

---

## Post #1 by @AsliBeriL (2024-02-15 20:26 UTC)

<p>Hello Dear Community,</p>
<p>OS: Windows 10<br>
Slicer version: 5.2.2</p>
<p>I’m getting warnings when trying to run Total Segmentator.</p>
<p>The code for the first warning is as follows:<br>
Traceback (most recent call last):<br>
File “D:\3D Slicer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “D:/3D Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 279, in onPackageInfoUpdate<br>
self.ui.packageInfoTextBrowser.plainText = self.logic.installedTotalSegmentatorPythonPackageInfo().rstrip()<br>
File “D:/3D Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 568, in installedTotalSegmentatorPythonPackageInfo<br>
versionInfo = subprocess.check_output([shutil.which(‘PythonSlicer’), “-m”, “pip”, “show”, “TotalSegmentator”]).decode()<br>
File “D:\3D Slicer\Slicer 5.2.2\lib\Python\Lib\subprocess.py”, line 424, in check_output<br>
return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,<br>
File “D:\3D Slicer\Slicer 5.2.2\lib\Python\Lib\subprocess.py”, line 528, in run<br>
raise CalledProcessError(retcode, process.args,<br>
subprocess.CalledProcessError: Command ‘[‘D:/3D Slicer/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘show’, ‘TotalSegmentator’]’ returned non-zero exit status 1.</p>
<p>The other issue is that the GPU cannot be found error. I downloaded CUDA. However, the same error persists.</p>
<p>Lastly, is Total Segmentator currently paid?</p>

---

## Post #2 by @jamesobutler (2024-02-15 20:48 UTC)

<p><a href="https://discourse.slicer.org/t/totalsegmentator-v2/32470">TotalSegmentator v2</a> is available as of the Slicer 5.6.0 release. Please download the latest Slicer stable (<a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>) and install the Total Segmentator extension to receive support related to Total Segmentator.</p>
<aside class="quote no-group" data-username="AsliBeriL" data-post="1" data-topic="34348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/asliberil/48/438_2.png" class="avatar"> AsliBeriL:</div>
<blockquote>
<p>Lastly, is Total Segmentator currently paid?</p>
</blockquote>
</aside>
<p>Please consult <a href="https://github.com/wasserth/TotalSegmentator?tab=readme-ov-file#subtasks" rel="noopener nofollow ugc">here</a> in the Total Segmentator readme regarding information about the licenses associated with the various sub tasks.</p>

---

## Post #3 by @AsliBeriL (2024-02-16 11:21 UTC)

<p>Thank you very much for your fast answer!</p>
<p>I downloaded and installed Slicer 5.6.1. But total segmentator cannot detect my GPU again. I have two graphic cards: Intel and Nvidia. I tried this solution of problem like this topic (<a href="https://discourse.slicer.org/t/total-segmenter-cannot-detect-my-gpu-1080ti-x-2/26728" class="inline-onebox">Total Segmenter cannot detect my GPU (1080ti x 2)</a>). But it’s not working.</p>

---

## Post #4 by @AsliBeriL (2024-02-16 19:39 UTC)

<p>Is there anyone who can help?</p>

---

## Post #5 by @jamesobutler (2024-02-16 20:01 UTC)

<p>Try to follow the instructions linked below regarding using the PyTorch Util module to check the installed pytorch version and to install/uninstall versions as part of debugging.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#gpu-is-not-found">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#gpu-is-not-found" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/7bc8d3c835c312787e486e4770ca02c49b9f2a476e9388190853e228c35387c3/lassoan/SlicerTotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#gpu-is-not-found" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body...</a></h3>

  <p>Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model - lassoan/SlicerTotalSegmentator</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also can you provide details about which Nvidia GPU your system has installed?</p>

---

## Post #6 by @AsliBeriL (2024-02-16 20:26 UTC)

<p>I have GeForce GT 720M</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8687303d3ef6f097f2bdad86a8cfea5841592b09.jpeg" alt="Ekran Alıntısı" data-base62-sha1="jc5CuPTS8TzYR8x6qXfQO7115q1" width="410" height="291"></p>

---

## Post #7 by @AsliBeriL (2024-02-16 20:30 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1db9dea57e7a7e4c8afdfda527031d35a3e38c7.jpeg" alt="Ekran Alıntısı" data-base62-sha1="we1XnLTpImcrgLsfOo4tUz8mPVZ" width="414" height="377"></p>
<p>NVidia driver not found?</p>

---

## Post #8 by @muratmaga (2024-02-16 21:12 UTC)

<aside class="quote no-group" data-username="AsliBeriL" data-post="6" data-topic="34348">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/asliberil/48/438_2.png" class="avatar"> AsliBeriL:</div>
<blockquote>
<p>GT</p>
</blockquote>
</aside>
<p>That gpu is over a decade old. I dont think it is supported</p>

---

## Post #9 by @jamesobutler (2024-02-16 21:45 UTC)

<p>Yes you’re going to have to remain on the CPU version of pytorch as the GeForce GT 720M “Fermi” based microarchitecture is not supported by the CUDA compute capability of latest pytorch. However, based on the age of your mobile GPU, I would expect that your CPU and memory are also going to struggle running inference. All these new ML tools generally require fairly recent hardware to run well.</p>
<aside class="onebox wikipedia" data-onebox-src="https://en.wikipedia.org/wiki/CUDA#GPUs_supported">
  <header class="source">

      <a href="https://en.wikipedia.org/wiki/CUDA#GPUs_supported" target="_blank" rel="noopener nofollow ugc">en.wikipedia.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://en.wikipedia.org/wiki/CUDA#GPUs_supported" target="_blank" rel="noopener nofollow ugc">CUDA | GPUs supported</a></h3>

<p>Supported CUDA Compute Capability versions for CUDA SDK version and Microarchitecture (by code name):
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2024-02-17 02:58 UTC)

<p>You can probably run the segmentation on the CPU, just make sure you force using the CPU. Low-resolution segmentation may be completed in a couple of minutes, but full-resolution segmentation on CPU will take tens of minutes.</p>

---

## Post #11 by @AsliBeriL (2024-02-17 20:36 UTC)

<p>Thank you very much for your detailed answer. Yes, my computer is 11 years old. However, I can easily run graphics-based software in terms of CPU, RAM and SSD. I have no problems with manual segmentation either. However, I encountered such a problem in automatic segmentation. All segmentations are completed in approximately 30 minutes (long version). Thank you again!</p>

---

## Post #12 by @AsliBeriL (2024-02-17 20:38 UTC)

<p>Full resolution segmentation via CPU takes approximately 30 minutes. Low-resolution segmentation is completed in a few minutes, but it is not of much use to me.<br>
Father of Total Segmentator, thank you very much for your efforts!</p>

---

## Post #13 by @lassoan (2024-02-20 19:45 UTC)

<p>Thanks for the update, I’m happy that things work for you.</p>
<p>Note that I developed and I am supporting the Slicer module for TotalSegmentator, but the main person who developed the TotalSegmentator model is Jakob Wasserthal.</p>

---
