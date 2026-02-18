# Fail to launch FiberTractMeasurements CLI module on Windows

**Topic ID**: 30708
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/fail-to-launch-fibertractmeasurements-cli-module-on-windows/30708

---

## Post #1 by @Kening_Zhang (2023-07-20 16:31 UTC)

<p>Dear developers,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/501506ce385e20737726183397ee96f1c778dec2.jpeg" data-download-href="/uploads/short-url/bqrfj1xVUSbln28PulCosQdQuzw.jpeg?dl=1" title="img_v2_32bf3ef9-97e1-497a-8291-12cfe06d9d1g" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/501506ce385e20737726183397ee96f1c778dec2_2_690x19.jpeg" alt="img_v2_32bf3ef9-97e1-497a-8291-12cfe06d9d1g" data-base62-sha1="bqrfj1xVUSbln28PulCosQdQuzw" width="690" height="19" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/501506ce385e20737726183397ee96f1c778dec2_2_690x19.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/501506ce385e20737726183397ee96f1c778dec2_2_1035x28.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/501506ce385e20737726183397ee96f1c778dec2_2_1380x38.jpeg 2x" data-dominant-color="252525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img_v2_32bf3ef9-97e1-497a-8291-12cfe06d9d1g</span><span class="informations">1502×42 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I type this command to use cli FiberTractMeasurements on my windows computer, some errors jumped, which says, can’t find xxx.dll, and cannot run the code,   reinstalling the program may resolve this issue.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efbba16ee446842e031e5c20850c579684d932c6.jpeg" alt="img_v2_7ad83fed-1d3e-4a71-8e65-c1d96ef175bg" data-base62-sha1="ycM6X49TpFf7rpGvKAnCxHxaDr0" width="542" height="202"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86647a4fe704dcae5ceb4384ae0f172ee9ec329a.jpeg" alt="img_v2_5f8d95e1-726f-456d-9931-fc75e5216bdg" data-base62-sha1="jaTfJcxFonFRYj7lEkXPQRsvzL4" width="542" height="218"><br>
However, this problem only appears on my windows computer, my macbook never go wrong results, how can I sovle it on windows?<br>
Warmest regards,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-07-20 16:54 UTC)

<p>The answer is probably similar to this post:</p>
<aside class="quote quote-modified" data-post="2" data-topic="30657">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dazhangge-666/48/66865_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/i-want-to-perform-the-ukftractography-singlely-on-command-line-in-my-ubuntu-20-04-how-could-i-do/30657/2">How to perform the UKFTractography via command line on ubuntu 20.04?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I want to use the UKFTractography singlely in order to use batch process on my data for tractography. 
when I make the code UKFTractography from github,I met the problem. 
I use the correct command from author. 
fatal: not a git repository (or any of the parent directories): .git 
make[5]: *** [ukf/CMakeFiles/_GEN_GITVER.dir/build.make:60: ukf/CMakeFiles/GEN 
make[4]: *** [CMakeFiles/Makefile2:1043: ukf/CMakeFiles/_GEN_GITVER.dir/all] Err 
make[3]: *** [Makefile:141: all] Error 2 
make[2]: *** […
  </blockquote>
</aside>

<p>On windows you provide the full path to Slicer.exe with the --launch argument to run the CLI executable.</p>

---

## Post #3 by @Kening_Zhang (2023-07-21 06:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0be1b4be941a9c43204aaa6694c6a3f1ae34f821.jpeg" data-download-href="/uploads/short-url/1H6P9LiBmSXLJJ6hVbTb05yRElj.jpeg?dl=1" title="20230721-135924" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be1b4be941a9c43204aaa6694c6a3f1ae34f821_2_690x293.jpeg" alt="20230721-135924" data-base62-sha1="1H6P9LiBmSXLJJ6hVbTb05yRElj" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be1b4be941a9c43204aaa6694c6a3f1ae34f821_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be1b4be941a9c43204aaa6694c6a3f1ae34f821_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0be1b4be941a9c43204aaa6694c6a3f1ae34f821_2_1380x586.jpeg 2x" data-dominant-color="191E1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230721-135924</span><span class="informations">1900×808 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It seems like I use the wrong command.</p>

---

## Post #4 by @pieper (2023-07-21 14:58 UTC)

<p>I believe you need to put the full string with <code>\path\to\Slicer.exe --launch ... FiberTractMeasurements.exe</code> inside a single set of quotes.</p>

---
