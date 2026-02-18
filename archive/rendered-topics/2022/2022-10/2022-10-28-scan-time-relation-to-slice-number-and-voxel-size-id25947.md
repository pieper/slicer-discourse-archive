# Scan time relation to slice number and voxel size

**Topic ID**: 25947
**Date**: 2022-10-28
**URL**: https://discourse.slicer.org/t/scan-time-relation-to-slice-number-and-voxel-size/25947

---

## Post #1 by @juliangallaun (2022-10-28 08:08 UTC)

<p>Hello everyone,</p>
<p>I have a more logical question to people which are working with CT-Scanners in general.</p>
<p>For example I have a volume which consist of 100 slices (the voxel size is 10 → 10x10x10), to decrease the GPU power, I use half the resolution when I upload my slices. So my new volume consist of 50 slices, the voxel size should now be 20x20x20, is this assumption correct?</p>
<p>And my second question is related to the time consumption of practical work, if my original volume (100 slices, voxel size 10) took 2 hours to scan, but I know the information I get from half the resolution is enough. So I change the CT setting to voxel size 20, the scanning time should than take only 1 hour (or decrease at least) and by using the full resolution now, I should have the same resolution as my original volume if halved.</p>
<p>Thank you all for your help!</p>

---

## Post #2 by @hherhold (2022-10-28 11:09 UTC)

<p>Question 1: That <em>sounds</em> correct but I haven’t finished my coffee this morning.</p>
<p>Question 2: Scan time is a function of a number of parameters, and resolution depends on your scanning setup. For example, in a cone-beam micro-CT scanner, your resolution depends on the size of the detector and the distance between the sample and the beam emitter. If the detector is stationary, the closer you get your sample to the emitter, the smaller your voxel size is.</p>
<p>What kind of scanner are you using? Medical or laboratory micro-CT?</p>

---

## Post #3 by @juliangallaun (2022-10-28 12:45 UTC)

<p>Thank you for your reply, I use the “µCT 40 SCANCO Medical” device.<br>
It should be a cone-beam micro-CT with a fixed detector.</p>
<p>Here are the specs of the device.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fda90642ec9d99728adb7abf879ba1a4de5d2ee.jpeg" data-download-href="/uploads/short-url/2gfqRIjHihktp6qgA19ZOw32FOe.jpeg?dl=1" title="Spec1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fda90642ec9d99728adb7abf879ba1a4de5d2ee_2_375x500.jpeg" alt="Spec1" data-base62-sha1="2gfqRIjHihktp6qgA19ZOw32FOe" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fda90642ec9d99728adb7abf879ba1a4de5d2ee_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fda90642ec9d99728adb7abf879ba1a4de5d2ee_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fda90642ec9d99728adb7abf879ba1a4de5d2ee_2_750x1000.jpeg 2x" data-dominant-color="9F9FA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Spec1</span><span class="informations">1200×1600 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5f159dda455826ff23daa18745cbd9fb0d08768.jpeg" data-download-href="/uploads/short-url/z5I4uAJBlYbihhdt3M0luGtqMNa.jpeg?dl=1" title="Spec2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f159dda455826ff23daa18745cbd9fb0d08768_2_375x500.jpeg" alt="Spec2" data-base62-sha1="z5I4uAJBlYbihhdt3M0luGtqMNa" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f159dda455826ff23daa18745cbd9fb0d08768_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f159dda455826ff23daa18745cbd9fb0d08768_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f159dda455826ff23daa18745cbd9fb0d08768_2_750x1000.jpeg 2x" data-dominant-color="989898"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Spec2</span><span class="informations">1200×1600 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @hherhold (2022-10-28 13:05 UTC)

<p>Changing the resolution of a cone beam micro-CT scanned volume requires downsampling or re-scanning.</p>
<p>Requirements vary, of course, but usually it’s best to scan at the highest resolution you can and then resample it if you need to.</p>
<p>(“Gory” details, if you’re interested - Here is one way to think about resolution with cone beam CT scanners. Take a flashlight and your hand, and shine a shadow of your hand on the wall. Think of the wall as the detector, the flashlight as the beam emitter, and your hand as your sample.</p>
<p>Hold the flashlight in one place and move your hand closer to and and further from the flashlight. If your hand is further away from the flashlight, it projects a smaller shadow on the wall. If you move your hand closer to the light, it projects a bigger shadow. This is basically what is happening when you move your sample closer to the emitter - you’re spreading out the image of your hand on the wall/detector, effectively magnifying it from the detector’s point of view, resulting in smaller voxels for each bit of hand.)</p>
<p>Hope this helps.</p>

---

## Post #5 by @muratmaga (2022-10-28 15:27 UTC)

<aside class="quote no-group" data-username="juliangallaun" data-post="1" data-topic="25947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/juliangallaun/48/9545_2.png" class="avatar"> juliangallaun:</div>
<blockquote>
<p>And my second question is related to the time consumption of practical work, if my original volume (100 slices, voxel size 10) took 2 hours to scan, but I know the information I get from half the resolution is enough. So I change the CT setting to voxel size 20, the scanning time should than take only 1 hour (or decrease at least)</p>
</blockquote>
</aside>
<p>It really doesn’t work that way. Scanning time has only approximate relationship to the resolution (i.e., the higher the resolution, the longer the scan). Other settings such as frame averaging, exposure, how many rotations you are acquiring has significant effect on your acquisition time than the resolution. It is also dependent on the specifics of the system. Usually these small desktop microCT systems (Scanco, Bruker), has a sweet spot that is most optimal for bone imaging, you need to experiment and find those settings (or talk to the technician running the scanner).</p>

---
