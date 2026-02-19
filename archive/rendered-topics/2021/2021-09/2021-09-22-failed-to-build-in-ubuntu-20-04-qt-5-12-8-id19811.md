---
topic_id: 19811
title: "Failed To Build In Ubuntu 20 04 Qt 5 12 8"
date: 2021-09-22
url: https://discourse.slicer.org/t/19811
---

# Failed to build in Ubuntu 20.04 (Qt-5.12.8)

**Topic ID**: 19811
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/failed-to-build-in-ubuntu-20-04-qt-5-12-8/19811

---

## Post #1 by @ZakiaKhatun (2021-09-22 16:53 UTC)

<p>Dear concern,</p>
<p>While trying to build Slicer in Ubuntu 20.04 following the instructions mentioned, (13 hours later) I got the following error message (make: Target ‘default_target’ not remade because of errors. Please find attached the error.<br>
Note: I am using Qt 5.12.8 not 5.15.1.<br>
Can anyone kindly assist me solving this issue?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdc626f3f305a2cc10029300b2772acec5eca555.png" data-download-href="/uploads/short-url/r4OMq0v6PlDR1gCbA9OpmvnSqNL.png?dl=1" title="terminal_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdc626f3f305a2cc10029300b2772acec5eca555_2_690x391.png" alt="terminal_error" data-base62-sha1="r4OMq0v6PlDR1gCbA9OpmvnSqNL" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdc626f3f305a2cc10029300b2772acec5eca555_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdc626f3f305a2cc10029300b2772acec5eca555_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdc626f3f305a2cc10029300b2772acec5eca555.png 2x" data-dominant-color="3E1E32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">terminal_error</span><span class="informations">1302×738 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2021-09-22 21:20 UTC)

<p>Did you make any code changes or changes to the cmake options or did you build with the defaults? I have built with 20.04 from scratch many times, most recently about a month ago with no problems.</p>

---

## Post #3 by @ZakiaKhatun (2021-09-23 07:34 UTC)

<p>I didn’t make any changes in the code. I was just following the instructions to build for the first time.</p>

---

## Post #4 by @RafaelPalomar (2021-09-23 14:52 UTC)

<p>I have just built Slicer (master branch) successfully on a fresh Ubuntu 20.04 (VirtualBox). The only issue I experienced was the one mentioned <a href="https://github.com/Slicer/Slicer/issues/5498#issuecomment-795860350" rel="noopener nofollow ugc">here</a>, which can be solved installing <code>python3-dev</code>; but this does not look to be the problem here.</p>
<p>Sometimes I have experienced unexplainable linking errors in two situations: (1) hardware is very (very) old; and (2) if I try to continue building Slicer <strong>after a previous abnormal and abrupt interruption of the building process</strong> (e.g., losing power, hard resetting the machine, etc). In case (2) you can clean with <code>make clean</code> or even delete your build directory and re-build again from scratch.</p>
<p>I hope this helps.</p>

---

## Post #5 by @ZakiaKhatun (2021-09-24 15:47 UTC)

<p>Dear Rafael Palomar,<br>
Thank you very much for responding. Yes, you’re right. Previously there was an interruption while building it and later it threw the mentioned error.<br>
Now, I have rebuilt it from scratch and everything is fine.<br>
(Although it took a long time to build even after using ‘make -j5 -k’ (about 26 hours). I once wished If I could pause the process for a while. :-))</p>

---

## Post #6 by @lassoan (2021-09-26 04:32 UTC)

<aside class="quote no-group" data-username="ZakiaKhatun" data-post="5" data-topic="19811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/df705f/48.png" class="avatar"> ZakiaKhatun:</div>
<blockquote>
<p>it took a long time to build even after using ‘make -j5 -k’ (about 26 hours)</p>
</blockquote>
</aside>
<p>For reference, we recently got a new desktop computer with an above average but not extreme configuration (Intel Core i9-10900X CPU, 64GB RAM, NVMe SSD; running Ubuntu 20.04) and the <strong>entire Slicer build is completed in 30 minutes</strong> (completely from scratch, including building VTK and all its dependencies, using <code>make -j20</code>).</p>
<p>Windows builds take longer. On a 3-year old desktop the build takes about 3-4 hours, on a laptop it takes about a half day to a day.</p>

---

## Post #7 by @RafaelPalomar (2021-09-27 06:24 UTC)

<p><a class="mention" href="/u/zakiakhatun">@ZakiaKhatun</a>, as <a class="mention" href="/u/lassoan">@lassoan</a> points out 3D Slicer does not take that long to build. Your elevated build times indicate that you may be getting out of RAM memory (how much do you have?). The more jobs you spawn to build Slicer (e.g, -j5) the more RAM you need to keep the build process; after using all your RAM your OS will try to use swap memory which is allocated in your SDD/HDD. In that case, just the memory transfers will contribute to such long building times. This behaviour is easy to observe because it makes your computer looking completely unresponsive.</p>
<p>If that is your case, lower your -j parameter to 1 or 2, which should bring your building times down to the  range <a class="mention" href="/u/lassoan">@lassoan</a> points out.</p>

---

## Post #8 by @ZakiaKhatun (2021-09-28 10:01 UTC)

<p>My laptop’s configuration is Intel Core i5-4200M (4th Gen), 2.5GHz, 12GB RAM (8 years old). I am using Ubuntu 20.04 in dual boot with windows.</p>

---

## Post #9 by @ZakiaKhatun (2021-09-28 10:12 UTC)

<p>Also, even though the build was successful, some of the tests fail (ctest -j4). Any idea why they fail?</p>
<p>Please find attached a screenshot of the failure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd2722c358cb4b890900abd9c7496d9fca6d7687.png" data-download-href="/uploads/short-url/vypmSvHrzC4KzSoiPYvARlfaCnt.png?dl=1" title="Test_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd2722c358cb4b890900abd9c7496d9fca6d7687_2_690x233.png" alt="Test_error" data-base62-sha1="vypmSvHrzC4KzSoiPYvARlfaCnt" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd2722c358cb4b890900abd9c7496d9fca6d7687_2_690x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd2722c358cb4b890900abd9c7496d9fca6d7687_2_1035x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd2722c358cb4b890900abd9c7496d9fca6d7687.png 2x" data-dominant-color="380C25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Test_error</span><span class="informations">1294×438 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After running --rerun-failed --output-on-failure command, it didn’t solve the problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b630e716ee2858dcac2e8c9af4c1276a65f10ae1.png" data-download-href="/uploads/short-url/pZJFJCMZCmgAV5VVQogJTQ0lkuR.png?dl=1" title="rerun_fails" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b630e716ee2858dcac2e8c9af4c1276a65f10ae1_2_689x29.png" alt="rerun_fails" data-base62-sha1="pZJFJCMZCmgAV5VVQogJTQ0lkuR" width="689" height="29" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b630e716ee2858dcac2e8c9af4c1276a65f10ae1_2_689x29.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b630e716ee2858dcac2e8c9af4c1276a65f10ae1_2_1033x43.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b630e716ee2858dcac2e8c9af4c1276a65f10ae1.png 2x" data-dominant-color="35162D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rerun_fails</span><span class="informations">1290×56 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2021-09-28 13:31 UTC)

<aside class="quote no-group" data-username="ZakiaKhatun" data-post="8" data-topic="19811" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/df705f/48.png" class="avatar"> ZakiaKhatun:</div>
<blockquote>
<p>My laptop’s configuration is Intel Core i5-4200M (4th Gen), 2.5GHz, 12GB RAM (8 years old). I am using Ubuntu 20.04 in dual boot with windows.</p>
</blockquote>
</aside>
<p>It is a wonder that Slicer can be built and runs on this computer at all. We only aim for compatibility with hardware that was released in the past 5 years.</p>
<aside class="quote no-group" data-username="ZakiaKhatun" data-post="9" data-topic="19811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/df705f/48.png" class="avatar"> ZakiaKhatun:</div>
<blockquote>
<p>even though the build was successful, some of the tests fail (ctest -j4). Any idea why they fail?</p>
</blockquote>
</aside>
<p>You can find the status of tests on official builds on the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a>. If you don’t have any additional test failures than the tests listed there then you don’t need to do anything about it. Those tests did not reveal any critical errors and we are already working on making them pass again.</p>

---
