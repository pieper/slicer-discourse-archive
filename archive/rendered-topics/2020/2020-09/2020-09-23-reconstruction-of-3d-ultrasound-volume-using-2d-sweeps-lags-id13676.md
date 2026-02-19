---
topic_id: 13676
title: "Reconstruction Of 3D Ultrasound Volume Using 2D Sweeps Lags"
date: 2020-09-23
url: https://discourse.slicer.org/t/13676
---

# Reconstruction of 3D ultrasound volume using 2D sweeps lags and low quality

**Topic ID**: 13676
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/reconstruction-of-3d-ultrasound-volume-using-2d-sweeps-lags-and-low-quality/13676

---

## Post #1 by @AurelieS (2020-09-23 15:55 UTC)

<p>Hi,</p>
<p>I am doing volume reconstruction using 2D ultrasound like in your video :</p><div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>

<ol>
<li>
<p>However, my computer does not seem powerful enough (16Go RAM &amp; Nvidia graphics card) to do live reconstruction, the system is completely lagging (about 1 update of the ultrasound video and tracking every 4-5seconds). What characteristics are needed to do a live reconstruction ?</p>
</li>
<li>
<p>I do not need especially ‘live’ recording, so I take the second option to record a sequence and reconstruct my volume from my recorded sequence.<br>
But, despite a quite high recording frequency acquisition (60fps) and no lagging during acquisition (the ultrasound video is very fluid), and very slow sweeps of my object, my reconstructed volume seems to be missing parts :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de8c78fa923bfed8b3c29f2546358752b8a4f131.jpeg" data-download-href="/uploads/short-url/vKKXutiyrUW4ZS0VFfEef16SkU1.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de8c78fa923bfed8b3c29f2546358752b8a4f131_2_690x388.jpeg" alt="Capture2" data-base62-sha1="vKKXutiyrUW4ZS0VFfEef16SkU1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de8c78fa923bfed8b3c29f2546358752b8a4f131_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de8c78fa923bfed8b3c29f2546358752b8a4f131_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de8c78fa923bfed8b3c29f2546358752b8a4f131_2_1380x776.jpeg 2x" data-dominant-color="626166"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">2560×1440 541 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>or has very low quality :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4323407b68ba642c49a34a0c65d44e98ff69ddc6.png" data-download-href="/uploads/short-url/9zVw4CwiN25C9hJo3H7XjsiDZhc.png?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4323407b68ba642c49a34a0c65d44e98ff69ddc6_2_690x395.png" alt="Capture3" data-base62-sha1="9zVw4CwiN25C9hJo3H7XjsiDZhc" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4323407b68ba642c49a34a0c65d44e98ff69ddc6_2_690x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4323407b68ba642c49a34a0c65d44e98ff69ddc6_2_1035x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4323407b68ba642c49a34a0c65d44e98ff69ddc6_2_1380x790.png 2x" data-dominant-color="8F9094"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">1811×1037 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does the problem come from my computer not powerful enough, or from my volume reconstruction parameters ? I tried changing a lot of parameters, but did not succeed in having a good quality volume …</p>
<p>My long-term objective is to obtain a reconstructed volume of my ultrasound sweeps with a high quality to be able to segment and calculate muscle volumes.</p>
<p>Thanks,<br>
Cheers,<br>
Aurélie</p>

---

## Post #2 by @Sunderlandkyl (2020-09-23 19:11 UTC)

<p>Can you upload your scene with the recorded sequence somewhere?</p>

---

## Post #3 by @AurelieS (2020-09-24 09:47 UTC)

<p>Here you can find my last acquisition, in the folder ‘volumereconstruction’ :<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="16" height="16">
      <a href="https://wetransfer.com/downloads/10a95817a7c96280bdf5b0573798a4a920200924092819/e4a75d" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://wetransfer.com/downloads/10a95817a7c96280bdf5b0573798a4a920200924092819/e4a75d" target="_blank" rel="noopener nofollow ugc">Session 2020-09-24.zip</a></h3>

<p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I also added in the main folder the config files I am using : ‘CALIBRATION’ is for pivot calibration and spatial calibration, and ‘ACQUISITION’ is for my volume acquisition.</p>
<p>The computer I am using is Intel Core i5-3570 CPU @ 3.40GHz, with 16Go RAM, Win10, and NVIDIA Quadro K600 graphics card.</p>
<p>Cheers,<br>
Aurélie</p>

---

## Post #4 by @Sunderlandkyl (2020-09-28 16:36 UTC)

<p>Thanks for the data! It looks like you are reconstructing your volume with a 0.1mm voxel size, which is too small for your ultrasound size (1.0mm).</p>
<p>Based on the size of the voxels in your ultrasound you would get much better results (faster and less artifacts) if you use a similar voxel size to your ultrasound (1.0mm).</p>

---

## Post #5 by @AurelieS (2020-09-29 10:04 UTC)

<p>Thank you for your response.</p>
<p>Yes I reconstructed my volume using a 0.1mm voxel size (this time, because I tried a lot of different settings, including the 1.0mm default one) …</p>
<p>However even by changing the voxel size to 1mm the reconstructed volume is still very blurry and incomplete. Did you succeed in reconstructing a good quality volume with the data I sent you ? can you show me if yes ?</p>
<p>I tried to load ‘ElbowUltrasoundSweep.mha’ (from the tutorials data), and after reconstruction, the volume looks much nicer than for my acquisitions. The ultrasound video seems to be more fluid than mine …</p>
<p>Thanks,<br>
Aurélie</p>

---

## Post #6 by @AurelieS (2020-09-29 11:59 UTC)

<p>UPDATE !<br>
Thanks to the ‘Node Modified Statistics’ in Slicer, I found out that my update time is only around 6-7 frames per second, whereas my video feed can go up to 60Hz and my Optitrack tracker stream up to 120Hz.<br>
And looking at the logs (for a small acquisition it is a 400Mo log), I see that there must be a problem in my tracker stream :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aa09f361ade02c24f366e8484bb1c0a2e32b2de.jpeg" data-download-href="/uploads/short-url/m3TF084wacbXycwaKwj4GVEnl1A.jpeg?dl=1" title="IMG_0107" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa09f361ade02c24f366e8484bb1c0a2e32b2de_2_666x500.jpeg" alt="IMG_0107" data-base62-sha1="m3TF084wacbXycwaKwj4GVEnl1A" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa09f361ade02c24f366e8484bb1c0a2e32b2de_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa09f361ade02c24f366e8484bb1c0a2e32b2de_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9aa09f361ade02c24f366e8484bb1c0a2e32b2de_2_1332x1000.jpeg 2x" data-dominant-color="C2BDB8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0107</span><span class="informations">2016×1512 1.81 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you prefer I go back to the Github of PlusToolkit since the issue must come from my config file ? (you have my config files in the folder I sent you).</p>

---

## Post #7 by @Sunderlandkyl (2020-09-29 13:58 UTC)

<p>It would be great if you could make a post on GitHub. We can continue this discussion there.</p>

---
