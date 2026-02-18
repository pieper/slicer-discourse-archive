# Nvidia GeForce setting (and relative 3d Slicer setting)

**Topic ID**: 42559
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/nvidia-geforce-setting-and-relative-3d-slicer-setting/42559

---

## Post #1 by @Nicola_Calcabrini (2025-04-14 15:09 UTC)

<p>Good morning everyone, I am a young researcher and I have recently started to use 3D slicer for fossil vertebrate reconstruction.</p>
<p>I use the following main functions:</p>
<ul>
<li>automatic and manual segmentation</li>
<li>ISLAND extension for model cleaning</li>
<li>WRAP SOLIDIFY extension for volume filling of the brain cavity.</li>
</ul>
<p>regarding the starting CT images, I have been using both low resolution images and microCTs that are extremely heavy to process.<br>
Because of this, I found that the software allows a choice of processing tool: i.e. CPU, GPU, multicore.<br>
I realized that the rendering processing of the 3D model is done through the use of CPU and RAM; instead, I think it is more convenient to use GPU and dedicated card given the following features of the workstation:<br>
Processor → Intel core i9 14900KF 3.2GHz<br>
Ram → 128Gb<br>
video card → Nvidia GeForce 4090 RTX</p>
<p>I am asking if in addition to the setting shown in the image, there are other types of settings to maximize the power of the machine.<br>
also I would like to understand if the video card settings themselves can be maximized for slicer use.<br>
I remain available for any clarification. Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f273845d65cfd019ac13568f481d1a499bfcc4.png" data-download-href="/uploads/short-url/iY6ttKGloWAwVDMct71vldZvfiQ.png?dl=1" title="Screenshot 2025-04-14 alle 16.40.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f273845d65cfd019ac13568f481d1a499bfcc4_2_690x497.png" alt="Screenshot 2025-04-14 alle 16.40.11" data-base62-sha1="iY6ttKGloWAwVDMct71vldZvfiQ" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f273845d65cfd019ac13568f481d1a499bfcc4_2_690x497.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f273845d65cfd019ac13568f481d1a499bfcc4_2_1035x745.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f273845d65cfd019ac13568f481d1a499bfcc4_2_1380x994.png 2x" data-dominant-color="E8E9EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-14 alle 16.40.11</span><span class="informations">1636×1180 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-04-14 15:30 UTC)

<p>This setting only has an effect on <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html">volume rendering</a>. Most algorithms in Slicer run on the CPU, some on the GPU (like some AI-based segmentations), however Slicer does not have a setting that influences it. Slicer is a research platform, so performance has not been a priority. Contributions to parallelise algorithms are, however, always welcome. A few years ago there was an effort to run some Segment Editor effects on teh GPU, but it was never integrated.</p>

---

## Post #3 by @muratmaga (2025-04-14 16:41 UTC)

<aside class="quote no-group" data-username="Nicola_Calcabrini" data-post="1" data-topic="42559">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/nicola_calcabrini/48/79984_2.png" class="avatar"> Nicola_Calcabrini:</div>
<blockquote>
<p>I am asking if in addition to the setting shown in the image, there are other types of settings to maximize the power of the machine.</p>
</blockquote>
</aside>
<p>Make sure you are using GPU Raycasting as default (you have a good video card), and the default quality is set to <strong>Normal</strong> (the setting below default rendering method), not <strong>Adaptive</strong>.</p>
<p>Also if your computer has a integrated GPU, make sure windows is configured to use your Nvidia RTX gpu for Slicer. You can search the forum and internet  for that.</p>
<p>These should take care of your rendering speed issues. Other slowdowns might be related to data size, processing pipeline and some other settings.</p>

---

## Post #4 by @lassoan (2025-12-03 13:36 UTC)

<p>6 posts were split to a new topic: <a href="/t/how-to-make-the-system-use-the-nvidia-gpu-for-slicer-not-the-integrated-intel-graphics/45348">How to make the system use the NVIDIA GPU for Slicer (not the integrated Intel graphics)</a></p>

---
