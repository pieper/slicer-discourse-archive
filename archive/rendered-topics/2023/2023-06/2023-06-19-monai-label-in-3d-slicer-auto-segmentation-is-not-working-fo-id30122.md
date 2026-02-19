---
topic_id: 30122
title: "Monai Label In 3D Slicer Auto Segmentation Is Not Working Fo"
date: 2023-06-19
url: https://discourse.slicer.org/t/30122
---

# Monai Label in 3d slicer -auto segmentation is not working for loaded data

**Topic ID**: 30122
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/monai-label-in-3d-slicer-auto-segmentation-is-not-working-for-loaded-data/30122

---

## Post #1 by @linda_varghese (2023-06-19 14:04 UTC)

<p>Hi Team,<br>
I am facing trouble to get the model to run on auto segmentation,I tried with the sample datatsets with segmentation-spleen model and even on deepedit model,in both case autosegmentation is not showing any models.<br>
As of now my aim is to automate the segmentation of liver,hepatic vein and portal vein.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73f0f5d2f51bf4c7bac28b4609f452a8095c900.png" data-download-href="/uploads/short-url/q94tUVN4EzLG3LH92BBzCLxYwda.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b73f0f5d2f51bf4c7bac28b4609f452a8095c900_2_523x500.png" alt="image" data-base62-sha1="q94tUVN4EzLG3LH92BBzCLxYwda" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b73f0f5d2f51bf4c7bac28b4609f452a8095c900_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73f0f5d2f51bf4c7bac28b4609f452a8095c900.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73f0f5d2f51bf4c7bac28b4609f452a8095c900.png 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">645×616 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2023-06-19 14:57 UTC)

<p>The standard MONAILabel radiology app works in 3D Slicer 3.2.2, provided you have a GPU on the server computer and enough VRAM on the NVIDIA GPU.</p>
<p>I used:</p>
<pre><code class="lang-auto">monailabel start_server --app MONAILabel/sample-apps/radiology --studies c:/Data/Task06_Lung/imagesTr --conf models segmentation
</code></pre>
<p>Make sure you install MONAILabel correctly, maybe restart from scratch and <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">follow our recipe</a><br>
Work on small or resampled datasets.</p>
<p>Using the pre-trained “segmentation” model on an AWS server with an A10G GPU (24GB):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd12be24855298f7ba43607b0a62f8809db6fafa.png" data-download-href="/uploads/short-url/vxHFYPohi9pUc3nsARjvKaNBzAe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd12be24855298f7ba43607b0a62f8809db6fafa_2_690x471.png" alt="image" data-base62-sha1="vxHFYPohi9pUc3nsARjvKaNBzAe" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd12be24855298f7ba43607b0a62f8809db6fafa_2_690x471.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd12be24855298f7ba43607b0a62f8809db6fafa_2_1035x706.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd12be24855298f7ba43607b0a62f8809db6fafa.png 2x" data-dominant-color="BBBAB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1261×861 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You would have to invest more training for better results.</p>
<p>MONAILabel version: 0.7.0rc7+2.g943d545<br>
Numpy version: 1.23.5<br>
Pytorch version: 1.13.1+cu117<br>
MONAILabel rev id: 943d545efdc6e3d6a50f959b1d7dd1b19d80e372</p>

---

## Post #3 by @linda_varghese (2023-06-23 12:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ad4d9453d57be0fa090f7a16ceb659676da2ebe.png" data-download-href="/uploads/short-url/jO9URF4VzA9hBeu3QOZtHrrIeGG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad4d9453d57be0fa090f7a16ceb659676da2ebe_2_548x499.png" alt="image" data-base62-sha1="jO9URF4VzA9hBeu3QOZtHrrIeGG" width="548" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ad4d9453d57be0fa090f7a16ceb659676da2ebe_2_548x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ad4d9453d57be0fa090f7a16ceb659676da2ebe.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ad4d9453d57be0fa090f7a16ceb659676da2ebe.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">731×666 63.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I had re installed Monai again with different with different version but again auto segmentation was disable</p>

---

## Post #4 by @rbumm (2023-06-23 12:27 UTC)

<p>What are your system specifications, Linda?</p>

---

## Post #5 by @linda_varghese (2023-06-23 12:35 UTC)

<p>AMD Ryzen 5 PRO 5675U with Radeon Graphics        2.30 GHz<br>
64-bit operating system, x64-based processor</p>

---

## Post #6 by @rbumm (2023-06-23 13:37 UTC)

<p>I have never got MONAILabel running on a non-NVIDIA GPU or an NVIDIA GPU with less than 6 GB of VRAM.<br>
Your non-display of the auto-segmentation model may be connected to that fact. You should be able to get TotalSegmentator (see your other thread) up and running if you install Pytorch (from the Pytorch extension) in <strong>CPU</strong> mode.<br>
But the best thing would be to upgrade your hardware or use a cloud server.</p>

---

## Post #7 by @Ylim (2023-09-01 00:56 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="6" data-topic="30122">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>n-NVIDIA GPU or an NVIDIA GPU with less than 6 GB of VRAM.</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f333a5fff257d061f841046b16db394355f96554.jpeg" data-download-href="/uploads/short-url/yHsGg0DMM6jkrofTK44FYzCKl3S.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f333a5fff257d061f841046b16db394355f96554_2_690x402.jpeg" alt="image" data-base62-sha1="yHsGg0DMM6jkrofTK44FYzCKl3S" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f333a5fff257d061f841046b16db394355f96554_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f333a5fff257d061f841046b16db394355f96554_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f333a5fff257d061f841046b16db394355f96554_2_1380x804.jpeg 2x" data-dominant-color="ADACAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1494×872 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi, using pycharm and slicer 5.2.2, i7 and rts3070 laptop (ram of 8gb?)<br>
I do need that the source volume cannot be chosen/shown, device is CPU and the auto seg cannot be run?</p>
<p>Please advise. Thanks.</p>

---

## Post #8 by @Ylim (2023-09-01 01:02 UTC)

<p>Resolved. Graphics Settings and Slicer.</p>

---

## Post #9 by @Ylim (2023-09-01 01:17 UTC)

<p>On your point on cloud computing, have you been successful in deploring the radiology app/ slicer/ monai label on colab?</p>

---

## Post #10 by @rbumm (2023-09-01 07:10 UTC)

<p>Just for other visitors: Could you please specify exactly how you resolved your problem?</p>

---

## Post #11 by @rbumm (2023-09-01 07:11 UTC)

<p>We were able to implement MonaiLabel on an AWS EC2 Windows server instance but not on a Colab.<br>
Maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> is aware of a Colab implementation?</p>

---

## Post #12 by @Ylim (2023-09-02 13:43 UTC)

<p>Hi Rudolf,<br>
I am using pycharm and slicer 5.2.2.</p>
<p>I have using pycharm and python 3.9 and have run<br>
pip install torch torchvision torchaudio --extra-index-url <a href="https://download.pytorch.org/whl/cu113" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu113</a></p>
<p>In slicer 5.2.2 python intrepretor,<br>
import torch; print(torch.cuda.is_available())<br>
output is TRUE.</p>
<p>I have an i7, 3070 laptop gpu, and was able to run autosegmenation in monailabel.<br>
however, i realise that the infer and within the infer is always cpu and i cannot change this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5771400b9123ee763b966cf0d96a2fef257b026.png" data-download-href="/uploads/short-url/wJWsNoslEGosISXf49VYrjoZ1BQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5771400b9123ee763b966cf0d96a2fef257b026_2_321x500.png" alt="image" data-base62-sha1="wJWsNoslEGosISXf49VYrjoZ1BQ" width="321" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5771400b9123ee763b966cf0d96a2fef257b026_2_321x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5771400b9123ee763b966cf0d96a2fef257b026_2_481x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5771400b9123ee763b966cf0d96a2fef257b026.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">580×902 24.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
task manager sees little to no gpu activity and i have enabled high performance for slicer in the nvida control.</p>
<p>The real issue is when I want to run my own data -<br>
AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\MONAILabel\lib\Slicer-5.2\qt-scripted-modules\MONAILabelLib\client.py", line 344, in infer<br>
raise MONAILabelClientException(<br>
MONAILabelLib.client.MONAILabelClientException: (1, ‘Status: 500; Response: Internal Server Error’)</p>
<p>log reads - [2023-09-02 23:39:53,031] [24088] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:480) - Inferer:: cpu =&gt; SlidingWindowInferer =&gt; {‘roi_size’: (96, 96, 96), ‘sw_batch_size’: 2, ‘overlap’: 0.4, ‘mode’: gaussian, ‘sigma_scale’: 0.125, ‘padding_mode’: ‘replicate’, ‘cval’: 0.0, ‘sw_device’: None, ‘device’: None, ‘progress’: False, ‘cpu_thresh’: None, ‘buffer_steps’: None, ‘buffer_dim’: -1, ‘roi_weight_map’: None}</p>
<p>any advice?</p>

---

## Post #13 by @rbumm (2023-09-03 18:45 UTC)

<ul>
<li>
<p>Uninstall everything.</p>
</li>
<li>
<p>Freshly install:5.4.0</p>
</li>
<li>
<p>Pytorch Utilities and Pytorch</p>
</li>
<li>
<p>Restart Slicer.</p>
</li>
<li>
<p>Install the Monailabel extension.</p>
</li>
<li>
<p>Install the Monailabel server separately on your computer. It must not residue in the Python interactor and within 3D Slicer. Ensure that CUDA support is available there.</p>
</li>
<li>
<p>Download the Monailabel apps and datasets that you need depending on the nature of your project.</p>
</li>
<li>
<p>Start the ML server</p>
</li>
<li>
<p>Start Slicer<br>
Start the ML extension</p>
</li>
<li>
<p>connect the server to the MonaiLabel extension.by just presssing enter in the ML server line.</p>
</li>
</ul>

---

## Post #14 by @diazandr3s (2023-09-04 10:43 UTC)

<p>Thanks for the ping, <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p><a class="mention" href="/u/ylim">@Ylim</a>, Colab is a Jupyter Notebook service. It is not intended for server hosting. Unless you mean using Colab to run shell commands and start the server in the background.</p>
<p>If this is the case, you must ensure permanent access to the same instance or computing resources. Something that’s not common in Colab.</p>
<p>Hope this helps,</p>

---

## Post #15 by @Ylim (2023-09-04 23:27 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> and <a class="mention" href="/u/rbumm">@rbumm</a> , the two of you have been very helpful/</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a>, i did find out the specific problem in my case, both the right version of pytorch must be installed in at both ends.</p>

---

## Post #16 by @zariliusra (2023-10-03 19:45 UTC)

<p>Can you explain how you resolved the “auto segmentation not working” problem? i also got this problem and still not resolved</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afd64738417592ede0c4b5c87473845963d0aa5a.jpeg" data-download-href="/uploads/short-url/p5wE4dHLSZdeE5WcbQaN7EOnh5U.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd64738417592ede0c4b5c87473845963d0aa5a_2_690x318.jpeg" alt="image" data-base62-sha1="p5wE4dHLSZdeE5WcbQaN7EOnh5U" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd64738417592ede0c4b5c87473845963d0aa5a_2_690x318.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd64738417592ede0c4b5c87473845963d0aa5a_2_1035x477.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd64738417592ede0c4b5c87473845963d0aa5a_2_1380x636.jpeg 2x" data-dominant-color="5D5E65"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1852×855 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
