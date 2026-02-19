---
topic_id: 35259
title: "Totalsegmentor Python Package For Slicer Plugin Showing Erro"
date: 2024-04-03
url: https://discourse.slicer.org/t/35259
---

# TotalSegmentor python package for Slicer plugin showing error

**Topic ID**: 35259
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/totalsegmentor-python-package-for-slicer-plugin-showing-error/35259

---

## Post #1 by @imruljubair (2024-04-03 15:45 UTC)

<p>I am getting following error message to work with TotalSegmentor python package on Slicer plugin showing.</p>
<p>Can anyone help me?</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2961, in tryWithErrorDisplay
    yield
  File "/Applications/Slicer.app/Contents/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 255, in onApplyButton
    self.logic.setupPythonRequirements()
  File "/Applications/Slicer.app/Contents/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 624, in setupPythonRequirements
    slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3571, in pip_install
    _executePythonModule('pip', args)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3533, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3502, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @jamesobutler (2024-04-03 17:18 UTC)

<p>It appears you are using Slicer 5.2. Please download the latest Slicer stable (5.6.1) and try again. Let us know here if switching to the new version fixes things for you.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/">
  <header class="source">
      <img src="https://slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" width="" height="">

      <a href="https://download.slicer.org/" target="_blank" rel="noopener nofollow ugc">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail">

<h3><a href="https://download.slicer.org/" target="_blank" rel="noopener nofollow ugc">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @imruljubair (2024-04-05 10:25 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks. I installed the latest one and it worked. Only thing is that I do not see any segmentation after applying TotalSegmentor with heartchambers_highres with license. I took a sample from Medical Segmentation Decathlon task 02 Heart (<a href="https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2" class="inline-onebox" rel="noopener nofollow ugc">MSD - Google Drive</a>), but it did not segment anything. Am I missing something?</p>
<p>Thanks.</p>

---

## Post #4 by @jamesobutler (2024-04-05 11:24 UTC)

<p>I looked up about MSD and it seems that heart data is MRI while TotalSegmentator works only on CT images. The developer of TotalSegmentator has mentioned about creating an MRI version, but there is no timeline about when it would be available to use.</p>
<p>Other groups are also aiming to build an MRI based segmentator, but again nothing publicly available at this moment.</p><aside class="quote quote-modified" data-post="3" data-topic="35080">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-for-mri-dataset/35080/3">TotalSegmentator for MRI dataset</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have a project underway to try training an MR segmenter based on TotalSegmentator using the SynthSeg approach (not muscles yet though).  The preprint paper actually just went up on arxiv: 


Would be great to generalize to other segmentation tasks.
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2024-04-05 14:44 UTC)

<p>MONAI Auto3DSeg extension has some MRI models already and more are coming.</p>
<p>If there is a training data set for heart chambers and you have a good GPU then you can train an Auto3DSeg model yourself by following the <a href="https://github.com/Project-MONAI/tutorials/blob/main/auto3dseg/README.md">this tutorial</a>.</p>

---

## Post #6 by @imruljubair (2024-04-06 04:22 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks a lot. Is there any way I can convert MRI data to fit into TotalSegmentor model?</p>

---

## Post #7 by @imruljubair (2024-04-06 04:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the suggestions. I already applied Auto3dSeg and nnU-Net on my dataset. I was looking for to observe how pretrained models performs on my dataset. But my dataset is MRI, not CT.</p>

---

## Post #8 by @lassoan (2024-04-06 04:34 UTC)

<p>TotalSegmentator offers a set of pre-trained models for CT. These will not be useful for you for your MRI images.</p>
<p>Since both nn-UNet and MONAI Auto3DSeg can train the AI models fully automatically, all you need to do is to get some training data (the Decathlon task 02 should be good) and run the training. I would recommend to follow the tutorial that I linked above to train the model using MONAI Auto3DSeg; and then you can use the result in MONAIAuto3DSeg extension in Slicer. Alternatively,  you can follow some nn-UNet tutorials to train your model and then use the resulting model in Slicer via the NNUnet extension.</p>

---

## Post #9 by @jamesobutler (2024-05-31 03:06 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="35259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The developer of TotalSegmentator has mentioned about creating an MRI version</p>
</blockquote>
</aside>
<p>Following up here, TotalSegmentator v2.2 now has support for MR tasks. SlicerTotalSegmentator will have to be updated to specify to use this new version.</p>

---
