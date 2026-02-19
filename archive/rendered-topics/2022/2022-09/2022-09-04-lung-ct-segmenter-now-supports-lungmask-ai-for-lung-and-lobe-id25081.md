---
topic_id: 25081
title: "Lung Ct Segmenter Now Supports Lungmask Ai For Lung And Lobe"
date: 2022-09-04
url: https://discourse.slicer.org/t/25081
---

# Lung CT Segmenter now supports 'lungmask' AI for lung and lobe segmentation

**Topic ID**: 25081
**Date**: 2022-09-04
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter-now-supports-lungmask-ai-for-lung-and-lobe-segmentation/25081

---

## Post #1 by @rbumm (2022-09-04 17:10 UTC)

<p>We have a new “experimental AI” option in Lung CT Segmenter for creating lung and lobe segmentations with minimal effort (one tracheal markup) on the fly.</p>
<p>This feature involves Johannes Hofmanningers <a href="https://github.com/JoHof/lungmask">lungmask</a> with permission.</p>
<p>A short YouTube demo is here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="bw1IaxVkOM4" data-video-title='Lung and lobe segmentation with "lungmask" AI in 3D Slicer' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bw1IaxVkOM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bw1IaxVkOM4/maxresdefault.jpg" title='Lung and lobe segmentation with "lungmask" AI in 3D Slicer' width="" height="">
  </a>
</div>

<p>In this setting, an Nvidia GPU (1060 +), 6 GB GPU memory and “CUDA enabled” are strongly recommended.</p>
<p>Real processing time on a desktop PC with RTX 3070Ti GPU (without the in-video speedup): 97.23 s.<br>
Slicer extension: Lung CT Analyzer<br>
Dataset: From MONAILabel Task06_lung with permission.</p>

---

## Post #2 by @Mehran (2022-09-06 14:05 UTC)

<p>That is great. Is it possible to use cli and save labelmaps?</p>

---

## Post #3 by @rbumm (2022-09-06 15:46 UTC)

<p>Yes, you can.</p>
<p>The Lung CT segmenter <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/dcb9c94ba35fd9398558bedfa066da45094ed989/LungCTSegmenter/LungCTSegmenter.py#L1824">AI test function</a> is a working example.</p>
<p>The only thing to note is the current necessity to define one tracheal markup in this code. If you want just lungs and lobes you could just freely define one, f.e. as in the test example, it is not really needed for AI.</p>

---

## Post #4 by @rbumm (2022-09-06 15:47 UTC)

<aside class="quote no-group" data-username="Mehran" data-post="2" data-topic="25081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mehran/48/11080_2.png" class="avatar"> Mehran:</div>
<blockquote>
<p>and save labelmaps</p>
</blockquote>
</aside>
<p>You would have to convert the output segmentation to a labelmap if you really needed to.</p>

---

## Post #5 by @Mehran (2022-09-07 07:29 UTC)

<p>thanks, i will do that</p>

---

## Post #6 by @yopi.simargi (2022-10-25 03:38 UTC)

<p>Hi Rudolf. Mine is not working. It is said no module name torch. How to get it and use the module torch? Thank you.</p>

---

## Post #7 by @rbumm (2022-10-25 06:11 UTC)

<p>Please install the “Pytorch Utils” extension and restart Slicer.<br>
Then it should typically install torch when you run the lung segmenter extension, but you could also install it from Pytorch Utils directly:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0091e8cf796d3e3baf5f63c653f1aa769360446.png" alt="image" data-base62-sha1="roPdaxlQYPynh7ZXygJnIfbDrMy" width="194" height="194"></p>
<p>Please be patient during installation, it will take several minutes with no reaction or progress bar.</p>
<p>Which version of 3D Slicer and Lung CT Segmenter are you using?</p>

---

## Post #8 by @lassoan (2022-10-27 05:41 UTC)

<p>Also note that you may need 20-30GB of free disk space for installing pytorch. If you run out of disk space then you may need to completely remove all remnants of pytorch and then install it again. I’ve found that in this case it is easier to reinstall Slicer than trying to clean up things manually.</p>

---

## Post #9 by @rbumm (2022-10-27 09:44 UTC)

<p>All dependencies (SegmentEditorExtraEffects, SurfaceWrapSolidify, and PyTorch) are now included in Lung CT Analyzer’s <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/1d852c1bd7d8a7b2098ed95646a13b96e6058f2f/CMakeLists.txt#L13">CMakeList.txt</a> for user convenience.</p>
<p>A fresh 3D Slicer 5.0.3 install on a Windows 11 system occupies 850 MB which grows to 7.4 GB after AI lung segmentations (mainly from Pytorch).</p>

---

## Post #10 by @yopi.simargi (2022-10-28 03:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/296b69ae0296e0ee7d9a598918abc5cd521562cc.png" data-download-href="/uploads/short-url/5UpHQnJClVbpfb7LaADDWK1csqw.png?dl=1" title="Screen Shot 2022-10-28 at 10.06.31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/296b69ae0296e0ee7d9a598918abc5cd521562cc_2_223x500.png" alt="Screen Shot 2022-10-28 at 10.06.31" data-base62-sha1="5UpHQnJClVbpfb7LaADDWK1csqw" width="223" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/296b69ae0296e0ee7d9a598918abc5cd521562cc_2_223x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/296b69ae0296e0ee7d9a598918abc5cd521562cc_2_334x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/296b69ae0296e0ee7d9a598918abc5cd521562cc_2_446x1000.png 2x" data-dominant-color="EEE0DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-28 at 10.06.31</span><span class="informations">542×1214 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fc5fd6c2bbe6a441c0cf320351881d8898e4bb.jpeg" data-download-href="/uploads/short-url/7Qquz5F7sgmWFZyGOPBHM4Y3PSP.jpeg?dl=1" title="Screen Shot 2022-10-28 at 10.08.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fc5fd6c2bbe6a441c0cf320351881d8898e4bb_2_690x316.jpeg" alt="Screen Shot 2022-10-28 at 10.08.08" data-base62-sha1="7Qquz5F7sgmWFZyGOPBHM4Y3PSP" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fc5fd6c2bbe6a441c0cf320351881d8898e4bb_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fc5fd6c2bbe6a441c0cf320351881d8898e4bb_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36fc5fd6c2bbe6a441c0cf320351881d8898e4bb_2_1380x632.jpeg 2x" data-dominant-color="CCCBCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-28 at 10.08.08</span><span class="informations">1848×848 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone, thank you for guiding me. I have installed the Pytorch and still got the same message. Is there any way to fix it? Thank you.</p>

---

## Post #11 by @yopi.simargi (2022-10-28 03:20 UTC)

<p>I am using Macbook Pro, macOS Big Sur, 2.8GHz Dual-Core Intel Core i7, Memory 8 GB. 3D Slicer version 5.03.<br>
I have installed PyTorch as I mentioned and the AI still not working. Thank you for your help Rudolf.</p>

---

## Post #12 by @rbumm (2022-10-28 09:05 UTC)

<p>Unfortunately, I have no experience with using PyTorch in MacOS.</p>
<p>Have you been pressing this button in the PyTorch Utils extension?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250a083cce816b51b6f44c021391c6e65e7c4b04.png" alt="image" data-base62-sha1="5hF9VZHGeVzRSTAPx8B5AGZ09V2" width="229" height="202"></p>
<p>If yes and you still got the error message you may want to refer <a href="https://pytorch.org/get-started/locally/">to this page</a> on how to install PyTorch from Slicer´s Python Interactor. See “Installing on MacOS” section.</p>
<p><code>import torch</code></p>
<p>should not throw an exception and</p>
<pre><code class="lang-auto">import torch
x = torch.rand(5, 3)
print(x)
</code></pre>
<p>should show a result.</p>

---

## Post #13 by @pieper (2022-10-28 13:28 UTC)

<p>Following the steps to install and test pytorch that <a class="mention" href="/u/rbumm">@rbumm</a> suggested works for me on a mac (m2 macbook air) with Slicer 5.0.3.</p>

---

## Post #14 by @mch114 (2023-05-20 08:36 UTC)

<p>Hi,</p>
<p>I am using the Lung CT analyser for a research project involving analysis of chest CTs of severe COVID patients. I would like to be able to automatically segment the lung regions using the lungmask AI feature/dataset, however I consistently get the following error each time I try it;</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9636d339540a779dab4c107735a33dc9621818d7.jpeg" data-download-href="/uploads/short-url/lqR58eOiLArjC9FXxIKSgTPQDDp.jpeg?dl=1" title="Screenshot 2023-05-20 at 5.57.33 pm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9636d339540a779dab4c107735a33dc9621818d7_2_690x376.jpeg" alt="Screenshot 2023-05-20 at 5.57.33 pm" data-base62-sha1="lqR58eOiLArjC9FXxIKSgTPQDDp" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9636d339540a779dab4c107735a33dc9621818d7_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9636d339540a779dab4c107735a33dc9621818d7_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9636d339540a779dab4c107735a33dc9621818d7_2_1380x752.jpeg 2x" data-dominant-color="9F9FB3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-20 at 5.57.33 pm</span><span class="informations">1920×1047 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Details;</p>
<ul>
<li>Machine: MacBook Pro M1</li>
<li>OS: Mac OS Ventura Version 13.2.1 (22D68)</li>
<li>Slicer for Mac version 5.2.2</li>
</ul>
<p>Python code for the error is;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2a20a979dc95785866c5e5ccb8cddcf40de593.png" data-download-href="/uploads/short-url/oqbU8ifbftl4lSeatFIbQkEoZk7.png?dl=1" title="Screenshot 2023-05-20 at 5.58.29 pm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2a20a979dc95785866c5e5ccb8cddcf40de593_2_690x127.png" alt="Screenshot 2023-05-20 at 5.58.29 pm" data-base62-sha1="oqbU8ifbftl4lSeatFIbQkEoZk7" width="690" height="127" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2a20a979dc95785866c5e5ccb8cddcf40de593_2_690x127.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2a20a979dc95785866c5e5ccb8cddcf40de593_2_1035x190.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2a20a979dc95785866c5e5ccb8cddcf40de593_2_1380x254.png 2x" data-dominant-color="FDEBEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-20 at 5.58.29 pm</span><span class="informations">1419×262 82.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m curious to know if this is an issue others have had with lungmask within 3D Slicer, and if so were there any solutions?</p>
<p>Thanks</p>

---

## Post #16 by @rbumm (2023-05-20 11:13 UTC)

<p>I just tested your issue and can confirm it on my systems too. Will try to find a solution.</p>

---

## Post #17 by @rbumm (2023-05-20 12:40 UTC)

<p>Identified the error. The lungmask developers have introduced a different infer mode in their new program version 0.2.14. LungCTAnalyzer has been adopted (2.67) and has just been pushed to the project GitHub, so it will be available for updates tomorrow via the extension manager and no longer display the error message.</p>

---

## Post #18 by @mch114 (2023-05-23 12:43 UTC)

<p>Hi Dr. Bumm,</p>
<p>Thanks very much for looking into this. I can confirm the lungmask AI model is working well within 3D slicer now and producing very nice segmentations.</p>
<p>Thanks again for the solution,</p>
<p>Marcus</p>

---

## Post #19 by @rsalkin (2024-01-17 15:24 UTC)

<p>Hello,</p>
<p>I recently updated slicer and had to re-install the Lung CT Segmenter. I am now getting an error stating the module ‘torch’ has no attribute ‘inference_mode’ (see below). I tried to uninstall and re-install the module as well as pytorch.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/447025586451b64c4931fd7d175238dc4fc192df.jpeg" data-download-href="/uploads/short-url/9LqJQmWSQAUJhZvyVrf8Gie2BtR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447025586451b64c4931fd7d175238dc4fc192df_2_690x315.jpeg" alt="image" data-base62-sha1="9LqJQmWSQAUJhZvyVrf8Gie2BtR" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447025586451b64c4931fd7d175238dc4fc192df_2_690x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/447025586451b64c4931fd7d175238dc4fc192df_2_1035x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/447025586451b64c4931fd7d175238dc4fc192df.jpeg 2x" data-dominant-color="727374"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1274×583 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Currently running windows 10 enterprise on a HP Z1 workstation, so using CUDA is not an option.</p>
<p>Any help would be appreciated, thanks!</p>

---

## Post #20 by @rbumm (2024-01-24 11:25 UTC)

<p>Hello,</p>
<p>sorry for the late response.<br>
I can not reproduce the problem after the last 3 installations that I have done.<br>
What do you see in the Python console when you experience this error?</p>
<p>Best</p>
<p>Rudolf</p>

---

## Post #21 by @rsalkin (2024-01-24 15:22 UTC)

<p>Hello Dr. Bumm,</p>
<p>Thank you for the reply. I attached my python console output below. The problem persist even with a fresh re-install of everything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b579df0c2850fc59e2b5d9835dffeba98ce9db2e.png" data-download-href="/uploads/short-url/pTpwRWEJZgJ2Kl2JS6raaOdqvmu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b579df0c2850fc59e2b5d9835dffeba98ce9db2e.png" alt="image" data-base62-sha1="pTpwRWEJZgJ2Kl2JS6raaOdqvmu" width="690" height="272" data-dominant-color="291D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×277 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @rbumm (2024-01-24 17:25 UTC)

<p>This seems to be a torch problem.<br>
Could you install 3D Slicer 5.6.1 into a new directory and just install Pytorch, LungCTAnalyzer and TotalSegmentator extensions ?<br>
And determine the version of torch as shown here ?</p>
<p><a href="https://www.youtube.com/watch?v=s2lB6MLBVeE" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=s2lB6MLBVeE</a></p>
<p>Best<br>
Rudolf</p>

---

## Post #23 by @jamesobutler (2024-01-24 17:26 UTC)

<p><a class="mention" href="/u/rsalkin">@rsalkin</a> If you switch to the “PyTorch Utils” module in Slicer, what version of Torch does it show that is currently installed?</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> What is the minimum torch version requirement to use your LungCTSegmenter module? I see that <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/a98033d8437f54106592982c9cbc4f331a3580cf/LungCTSegmenter/LungCTSegmenter.py#L2296-L2319" rel="noopener nofollow ugc">your code</a> checks if <code>torch</code> is present and that CUDA support is available, but it doesn’t check a specific <code>torch</code> version requirement?</p>
<p>Below is example usage of SlicerTotalSegmentator enforcing a minimum <code>torch</code> version.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/a716dd36e2afaf20cc5648204823ad1c6a8a0e8b/TotalSegmentator/TotalSegmentator.py#L703-L708">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/a716dd36e2afaf20cc5648204823ad1c6a8a0e8b/TotalSegmentator/TotalSegmentator.py#L703-L708" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/a716dd36e2afaf20cc5648204823ad1c6a8a0e8b/TotalSegmentator/TotalSegmentator.py#L703-L708" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerTotalSegmentator/blob/a716dd36e2afaf20cc5648204823ad1c6a8a0e8b/TotalSegmentator/TotalSegmentator.py#L703-L708</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="703" style="counter-reset: li-counter 702 ;">
          <li># torch is installed, check version</li>
          <li>from packaging import version</li>
          <li>if version.parse(torchLogic.torch.__version__) &lt; version.parse(minimumTorchVersion):</li>
          <li>    raise ValueError(f'PyTorch version {torchLogic.torch.__version__} is not compatible with this module.'</li>
          <li>                     + f' Minimum required version is {minimumTorchVersion}. You can use "PyTorch Util" module to install PyTorch'</li>
          <li>                     + f' with version requirement set to: &gt;={minimumTorchVersion}')</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It appears that <a href="https://github.com/JoHof/lungmask" rel="noopener nofollow ugc"><code>lungmask</code></a> specifies no torch version which can result in incompatibilities of an older torch version not working.</p>

---

## Post #24 by @rsalkin (2024-01-24 17:42 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> I did a fresh install into a new directory with the modules as you suggested and get the same error.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> The current version of Torch is 1.8.1. I don’t know if it matters but TorchVision is 0.9.1.</p>

---

## Post #25 by @rbumm (2024-01-24 18:21 UTC)

<p>Uninstall Pytorch again.<br>
Then install it with cu118.<br>
For that press "show all compatible and select cu118.<br>
Press Install Pytorch.</p>
<p>Any changes?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffb9637e50b55e96802d906d1087f0b473521ffa.png" data-base62-sha1="AueWNi89BWq6M1T69HiR6zWu6HE" alt="image.png" width="519" height="233"></p>

---

## Post #26 by @rsalkin (2024-01-24 19:38 UTC)

<p>The Pytorch Utils module only let me install up to version 1.8.1+cpu but I was able to manually install version 2.1.2+cpu via the python console (<a href="https://discourse.slicer.org/t/pytorch-extension-installation/30929" class="inline-onebox">Pytorch extension installation</a>) and now the segmenter is working.</p>
<p>Thanks Dr. Bumm for answering my question. The module has been extremely helpful.</p>

---

## Post #27 by @rbumm (2024-01-24 20:04 UTC)

<p>Great, but there seems to be a bug in Pytorch …</p>

---

## Post #28 by @rbumm (2024-01-25 10:47 UTC)

<p>Could you describe in detail what you had to do to install the torch version that finally worked?</p>

---

## Post #29 by @rsalkin (2024-01-25 14:45 UTC)

<p>This is just for the CPU version as my computer does not have a capable GPU for PyTorch.</p>
<p>You first have to go to the PyTorch Utils module (see below) in slicer then select uninstall PyTorch (if you uninstall via the python console <code>slicer.util.pip_uninstall("torch")</code> it doesn’t work and crashes when you try to uninstall via the Utils module afterwards, assuming the original PyTorch installation used the Utils module).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9792d31a46785b35774ec93720bb81c2940d733.png" alt="image" data-base62-sha1="v1ReiwesdTMtQLPnrvOceUOcYRJ" width="542" height="238"></p>
<p>Restart Slicer after removing PyTorch then run the line:</p>
<pre><code class="lang-auto">slicer.util.pip_install("torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu")
</code></pre>
<p>Restart the application one more time after PyTorch has been re-downloaded and you should be good to go.</p>

---

## Post #30 by @lassoan (2024-01-26 19:02 UTC)

<p>For some reason, on some computers these ancient PyTorch 1.x versions are installed by default.</p>
<p>We added the “torch version requirement” field to PyTorch Utils module to make it very easy to install a more recent version. For example, you can type <code>&gt;2</code> in that field and click <code>Install PyTorch</code>.</p>
<p><a class="mention" href="/u/rsalkin">@rsalkin</a> Do you have any recommendation of how to make it more clear that the required pytorch version can be specified in Pytorch Utils module? Maybe changing the placeholder text from “default” to something like “specify version requirement here” would help?</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> I would recommend to copy the PyTorch version check that <a class="mention" href="/u/jamesobutler">@jamesobutler</a> highlighted from TotalSegmentator module to the LungCTSegmenter module.</p>

---

## Post #31 by @rbumm (2024-01-27 13:03 UTC)

<p>Now check the Pytorch version in LungCTSegmenter.</p>

---

## Post #32 by @rsalkin (2024-01-29 15:47 UTC)

<p>Hi Andras, I think that could be good, otherwise it might be simpler to have a drop down menu and select either latest stable version, system default version, or a specify system version where you can then type which one you want, i.e. x.x. That way its easy for someone not to have to look up the first two and give the optionality if a module is very specific for the last option.</p>

---
