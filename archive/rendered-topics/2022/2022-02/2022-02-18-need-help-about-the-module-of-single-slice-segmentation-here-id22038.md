---
topic_id: 22038
title: "Need Help About The Module Of Single Slice Segmentation Here"
date: 2022-02-18
url: https://discourse.slicer.org/t/22038
---

# Need help about the module of "Single Slice Segmentation" here

**Topic ID**: 22038
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/need-help-about-the-module-of-single-slice-segmentation-here/22038

---

## Post #1 by @BARNEY (2022-02-18 08:32 UTC)

<p>Hello community,<br>
We are now working about building a new trained models in Segmentation UNet, that requires manuall ultrasound  images segmentation for generating AI training data. The module “Single Slice Segmentation” from “SlicerIGT” seems very helpful cause it generates .npy files. But the npy files I exported only contained the ultrasound  images but no segmentation information, file sizes of “_ultrasound.npy” and “_segmentation.npy”  are same. Did something go wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ce22c5fa4808799ae8efc43bf70729207d6abd7.png" data-download-href="/uploads/short-url/6p3A8pCU4zfL9j1DcuqAKGIEWBV.png?dl=1" title="截屏2022-02-18 下午4.29.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce22c5fa4808799ae8efc43bf70729207d6abd7_2_522x500.png" alt="截屏2022-02-18 下午4.29.54" data-base62-sha1="6p3A8pCU4zfL9j1DcuqAKGIEWBV" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce22c5fa4808799ae8efc43bf70729207d6abd7_2_522x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce22c5fa4808799ae8efc43bf70729207d6abd7_2_783x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2ce22c5fa4808799ae8efc43bf70729207d6abd7_2_1044x1000.png 2x" data-dominant-color="3E3F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-02-18 下午4.29.54</span><span class="informations">1084×1038 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbfd4438bb0a5cf4df6105c05e1f7603010c282.png" data-download-href="/uploads/short-url/8wza5UeVo0Xjm0cW393HqcGKLBw.png?dl=1" title="截屏2022-02-18 下午4.30.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbfd4438bb0a5cf4df6105c05e1f7603010c282_2_690x359.png" alt="截屏2022-02-18 下午4.30.58" data-base62-sha1="8wza5UeVo0Xjm0cW393HqcGKLBw" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbfd4438bb0a5cf4df6105c05e1f7603010c282_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbfd4438bb0a5cf4df6105c05e1f7603010c282_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bbfd4438bb0a5cf4df6105c05e1f7603010c282_2_1380x718.png 2x" data-dominant-color="242A33"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-02-18 下午4.30.58</span><span class="informations">1488×776 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc1672f3c2923a1541eaab4b9e61cc7d2cac2bcf.png" data-download-href="/uploads/short-url/t7rv34R2EUS7VYZuTLXdlJSNM0n.png?dl=1" title="截屏2022-02-18 下午4.33.53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc1672f3c2923a1541eaab4b9e61cc7d2cac2bcf_2_690x350.png" alt="截屏2022-02-18 下午4.33.53" data-base62-sha1="t7rv34R2EUS7VYZuTLXdlJSNM0n" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc1672f3c2923a1541eaab4b9e61cc7d2cac2bcf_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc1672f3c2923a1541eaab4b9e61cc7d2cac2bcf_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc1672f3c2923a1541eaab4b9e61cc7d2cac2bcf.png 2x" data-dominant-color="414140"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-02-18 下午4.33.53</span><span class="informations">1088×552 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-02-18 16:36 UTC)

<p><a class="mention" href="/u/ungi">@ungi</a> can you help with this?</p>

---

## Post #3 by @ungi (2022-02-18 17:22 UTC)

<p>Hi Barney,<br>
I use this module regularly, and I have not run into the issue you describe.<br>
The error message in your second screenshot is from a function that saves your segmentation. That code is not executed during data export, so the problem might be during saving your segmentations. I don’t see anything wrong on your first screenshot, so I need more information to figure out the problem. Could you post here your full Slicer log?<br>
Help / Report a bug / Copy log message to clipboard<br>
It would be best if you put a Slicer scene with a short recorded ultrasound sequence in a shared folder and share that too. I would use that to segment and export the data on my computer to see if I can reproduce the problem.</p>

---

## Post #5 by @BARNEY (2022-02-19 09:07 UTC)

<p>Hello professor Ungi,<br>
I am very glad to get your help. The steps were as follows: set the input selections as shown in the first screenshot, then add a new segmentation item, use the paint tool to determine the segmentation area, click “capture”. Sometimes click “skip” to skip improper image.<br>
The files I uploaded, one is initially recorded ultrasound sequence, the other one is completed segmentation scene, but this time I clicked export, there was no file exported.<br>
I’d appreciate it if you could help me see what went wrong, thank you!<br>
Slicerlog and scene fires in OneDrive: <a href="https://1drv.ms/u/s!AseGPHvl8ngAaqiyLKoc-iG8jiU?e=GizdWz" class="inline-onebox" rel="noopener nofollow ugc">Microsoft OneDrive - Access files anywhere. Create docs with free Office Online.</a></p>

---

## Post #6 by @ungi (2022-02-19 15:25 UTC)

<p>Most likely the problem was that your ultrasound image and your segmentation were in different positions. Segmentations use something called a “master volume”. It is an image that provides pixel/voxel locations for the segmentation to paint on. If you segmentation object is not perfectly overlapping with your master volume, then your segmentations will not work. It’s like trying to paint but your paintbrush is not touching the canvas.</p>
<p>You master volume is an ultrasound image that is on a moving transform. When you create the segmentation node, it copies the current location of the ultrasound image. But when you go to the next frame, the ultrasound image moves, so you paintbrush moves off of your canvas (segmentation node). The solution is to always keep the master volume and the segmentation in the same place in the transform hierarchy. Since segmentations are created at the root of the transform hierarchy, you must put your ultrasound image in the root of the transform hierarchy when you first open the Segment Editor module. I know this is not user friendly, but there is no other way to do it, because Segment Editor automatically creates the segmentation there when you first open that module.</p>
<p>Just to make sure you see every detail, I’ve recorded my screen while using your data. You will notice that in the beginning, I painted on untransformed images. But after a few frames I moved the image and the segmentation to the tracker transform and continue to paint there. The only important thing is always keep these two together. Here is the video:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://onedrive.live.com/redir?resid=7230D4DEC6058018%2172226&amp;authkey=%21AIhN-OAe6cODvtI&amp;ithint=video%2cmp4&amp;e=Fvz3aT">
  <header class="source">

      <a href="https://onedrive.live.com/redir?resid=7230D4DEC6058018%2172226&amp;authkey=%21AIhN-OAe6cODvtI&amp;ithint=video%2cmp4&amp;e=Fvz3aT" target="_blank" rel="noopener nofollow ugc">onedrive.live.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://storage.live.com/Items/7230D4DEC6058018%2172226%3ACustomThumbnailSource%2CHighRes%2CDefault?width=1600&amp;height=900&amp;authKey=%21AIhN-OAe6cODvtI" class="thumbnail" width="690" height="388"></div>

<h3><a href="https://onedrive.live.com/redir?resid=7230D4DEC6058018%2172226&amp;authkey=%21AIhN-OAe6cODvtI&amp;ithint=video%2cmp4&amp;e=Fvz3aT" target="_blank" rel="noopener nofollow ugc">2022-02-19_SingleSliceSegm.mp4</a></h3>

  <p>MP4 File</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let me know if this solves your problem.</p>

---

## Post #7 by @BARNEY (2022-02-21 07:11 UTC)

<p>Thank you very much, that is the perfect solution to my problem and I exported the segmentation sequence successfully. Thank you again!<br>
There is one small problem, the images I exported seemed to be distorted than the original ones, like covered with mist. Is this a problem with my source file? Because I didn’t make any adjustments.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04a5444486c9eb1e3785163c0e3d5d0ff7a3bef5.png" data-download-href="/uploads/short-url/F5ZvAYgI0YKKjtQ2r3rPRPlBxX.png?dl=1" title="2022-02-21 3.14.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04a5444486c9eb1e3785163c0e3d5d0ff7a3bef5_2_689x375.png" alt="2022-02-21 3.14.17" data-base62-sha1="F5ZvAYgI0YKKjtQ2r3rPRPlBxX" width="689" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04a5444486c9eb1e3785163c0e3d5d0ff7a3bef5_2_689x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04a5444486c9eb1e3785163c0e3d5d0ff7a3bef5_2_1033x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04a5444486c9eb1e3785163c0e3d5d0ff7a3bef5.png 2x" data-dominant-color="585858"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-02-21 3.14.17</span><span class="informations">1106×602 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @ungi (2022-02-21 14:41 UTC)

<p>I’m glad it worked.<br>
It’s not mist, the two images are identical. You just use different viewer software with different brightness and contrast settings for the left and right side images. Note that medical image viewers call brightness and contrast “level” and “window”. Higher level means lower brightness, and higher window means lower contrast.</p>

---

## Post #9 by @BARNEY (2022-02-22 04:41 UTC)

<p>I see, thank you for your help and guidance!！</p>

---

## Post #10 by @ElkeC (2022-03-16 13:56 UTC)

<p>Hi Ungi!</p>
<p>I am trying to use the Single Slice Segmentation extension too and I think I have the same problem. I wanted to watch your video but it isn’t available anymore, is it possible to download the video again for me?<br>
Thanks!</p>

---

## Post #11 by @ungi (2022-03-16 14:22 UTC)

<p>Hi <a class="mention" href="/u/elkec">@ElkeC</a>, interesting that the video link doesn’t work… I’ve created another link for the same file. Please try this: <a href="https://1drv.ms/v/s!AhiABcbe1DByhLQiDStPw257kYAr3A?e=HmWFhv" class="inline-onebox" rel="noopener nofollow ugc">Microsoft OneDrive - Access files anywhere. Create docs with free Office Online.</a></p>

---

## Post #12 by @ElkeC (2022-03-16 14:30 UTC)

<p>That works!<br>
Thank you!!</p>

---

## Post #13 by @BARNEY (2022-04-10 07:52 UTC)

<p>Hello Ungi!<br>
I had a problem that was bothering me lately. The manual segmentation result exported by the 3D Slicer has two file forms .npy and .png, but our binary diagram is different from the PerkLab open data.The gray value in our segmentation images is 0 to 255 rather than 0 to 1, and somehow the gray value in our ultrasound images is 0 to 1. After many attempts, we found that it will affect the outcome of learning. So, is something that can be changed in Single Slice Segmentation module?<br>
Thanks! Wish you best!<br>
<a>Uploading: 2022-04-10 下午3.50.44.png…</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8810da5cf472e131e8569a58861db8a93e4557d8.png" alt="_0129_ultrasound" data-base62-sha1="jpH2GxOHlRGhgrQWLIOxR9Wdq6A" width="256" height="256"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84eeeef2ed299aa3e2385e46dc8ca4167d852e1d.png" data-download-href="/uploads/short-url/iXYWbJiUjf8OlfBAodEaK2gHAjb.png?dl=1" title="WechatIMG3629" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84eeeef2ed299aa3e2385e46dc8ca4167d852e1d_2_690x294.png" alt="WechatIMG3629" data-base62-sha1="iXYWbJiUjf8OlfBAodEaK2gHAjb" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84eeeef2ed299aa3e2385e46dc8ca4167d852e1d_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84eeeef2ed299aa3e2385e46dc8ca4167d852e1d_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84eeeef2ed299aa3e2385e46dc8ca4167d852e1d_2_1380x588.png 2x" data-dominant-color="5C5C5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG3629</span><span class="informations">1584×676 30 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @ungi (2022-04-10 15:31 UTC)

<p>Hi, the intensity range is typically managed in your AI training script. If you load the segmentation data in a numpy array (let’s call it S), and its values range between 0 and 255, then you can scale it between 0 and 1 by one line of code: <code>S = S / 255.0</code><br>
I hope this helps.</p>

---

## Post #15 by @BARNEY (2022-04-11 03:07 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">OK I will try, thank you!</p>

---
