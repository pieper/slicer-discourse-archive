---
topic_id: 17456
title: "Issue With Breachwarning In Slicer 4 11"
date: 2021-05-04
url: https://discourse.slicer.org/t/17456
---

# Issue with BreachWarning in Slicer 4.11

**Topic ID**: 17456
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/issue-with-breachwarning-in-slicer-4-11/17456

---

## Post #1 by @Serg (2021-05-04 20:39 UTC)

<p>I’m using the latest stable Slicer 4.11.20210226 with NDI electromagnetic tracking system on Win10. Once models created, calibrated, and a tracking system successfully connected to the phantom coordinates with all transformations, I’m trying to use a BreachWarning to measure the distance between a needle tip and object. At the first attempt, the models in the Inputs’ “Model to watch:” and “Tool tip (to RAS) transform:” can be chosen. But, after that, if I’m trying to chose the other model in drop-down menus, the mouse cursor just jumping itself, which prevents choosing any other model. However, if the scene saved and reopen, the drop-down menus are working fine, allow changing the models accordingly. But, the real-time distance measurement doesn’t work and the measurement is showing only when the “Display line to closest point” check box is marked or unmarked. Or, when the slider in the “Line to closest point text size” is moved to any position.<br>
Two short videos, related to these issues, uploaded.<br>
I’ve had the same problem when rolled back to Slicer 4.10.2.<br>
But, there is no similar issue in 4.10.1.<br>
Any suggestions or workaround on dealing with these problems would be greatly appreciated because we need to use a new ver. 4.11.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fa5bbc6f5bc1c1b805e91ece2e207dcfe1fe87.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fa5bbc6f5bc1c1b805e91ece2e207dcfe1fe87.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44fa5bbc6f5bc1c1b805e91ece2e207dcfe1fe87.mp4</a>
    </source></video>
  </div><br>
<div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bca9b87a7508d8a088fd3eab93422bd600f3e80.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bca9b87a7508d8a088fd3eab93422bd600f3e80.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bca9b87a7508d8a088fd3eab93422bd600f3e80.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @lassoan (2021-05-05 17:07 UTC)

<p>I could not reproduce this issue. Could you save the scene as a .mrb file, upload it somewhere, and post the link here?</p>

---

## Post #3 by @Serg (2021-05-05 17:47 UTC)

<p>Andras,<br>
please find the link here:</p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1aqHmY_9Snod2Uw-hSF3ksyPpjqKq494O/view" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1aqHmY_9Snod2Uw-hSF3ksyPpjqKq494O/view" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1aqHmY_9Snod2Uw-hSF3ksyPpjqKq494O/view" target="_blank" rel="noopener nofollow ugc">2021-05-04-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks!</p>

---

## Post #4 by @lassoan (2021-05-07 20:20 UTC)

<p>I could reproduce the issue and the problem seem to be due to some problems how annotation ruler node is loaded from a saved scene.</p>
<p>I’ve updated BreachWarning module to use markups line node instead, which should fix the problem.</p>

---

## Post #5 by @Serg (2021-05-07 20:32 UTC)

<p>That would be great.<br>
Will you push a fix, meaning to build a new revision for ver.4.11?<br>
Thanks a lot for the tremendous support!</p>

---

## Post #6 by @lassoan (2021-05-08 00:47 UTC)

<p>It is already available in the latest Slicer Preview Release.</p>

---

## Post #7 by @Serg (2021-05-10 01:13 UTC)

<p>Thank you very much!<br>
The distance measurement in BreachWarning is working now in real time.</p>
<p>Sorry to tell about another issue in the latest release - Slicer doesn’t start after the PortPlacement extension installed. Should be opened a new topic?</p>

---

## Post #8 by @lassoan (2021-05-10 01:27 UTC)

<p>Thanks for the update. Please create a new topic to ask about PortPlacement extension.</p>

---

## Post #9 by @Serg (2021-05-11 03:13 UTC)

<p>Just an update - in the latest release 4.13 rev.29889 deployed today Slicer reboots fine after the PortPlacement installed. No issue with that.</p>
<p>Can’t find Matlab extension. Is it deprecated in 4.13 and in further versions?</p>

---

## Post #10 by @lassoan (2021-05-11 05:11 UTC)

<p>I’ve pushed a fix to make MatlabBridge compatible with Slicer-4.13 (it may take a few days for the extension to show up, as the extensions server is being replaced).</p>
<p>That said, you may consider MatlabBridge deprecated. The MatlabBridge made a lot of sense 10+ years ago when we developed it, but now you are probably much better off using Python instead. Python is a general-purpose programming language with magnitudes larger community and more packages. Moreover, since Slicer has an embedded Python interpreter, you can use Python (and any Python packages) in Slicer very conveniently - without the need for installing any additional runtime or dealing with licensing hassles of Matlab.</p>

---

## Post #11 by @Serg (2021-05-11 19:59 UTC)

<p>Thanks a lot for the MatlabBridge fix!<br>
In today’s release it works like a charm.</p>
<p>Totally agree about the Python and this is what I’m trying to work on. And, using MatlabBridge is very helpful for now.</p>
<p>Actually, we want to use EM tracking system to quickly record location of each catheter inserted into the tumor model in reference to each other catheter, and generate a map similar to shown here.<br>
Could you suggest a simple solution to achieve this goal with the Slicer? Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb7441ffcb2a2d0b900fe135ca735ca4504d18d5.jpeg" data-download-href="/uploads/short-url/t1Q0tDfUsLKRDUJ4BRbIhOIBIY5.jpeg?dl=1" title="pre-planning_map" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb7441ffcb2a2d0b900fe135ca735ca4504d18d5_2_690x275.jpeg" alt="pre-planning_map" data-base62-sha1="t1Q0tDfUsLKRDUJ4BRbIhOIBIY5" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cb7441ffcb2a2d0b900fe135ca735ca4504d18d5_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb7441ffcb2a2d0b900fe135ca735ca4504d18d5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb7441ffcb2a2d0b900fe135ca735ca4504d18d5.jpeg 2x" data-dominant-color="D2D3E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pre-planning_map</span><span class="informations">904×361 53.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Serg (2021-05-12 18:08 UTC)

<p>Seems the solution for my previous request is described here:<br>
<a href="http://perk.cs.queensu.ca/contents/needle-navigation-and-catheter-reconstruction-breast-brachytherapy-using-open-source" rel="noopener nofollow ugc">http://perk.cs.queensu.ca/contents/needle-navigation-and-catheter-reconstruction-breast-brachytherapy-using-open-source</a></p>
<p>There is no MarkupsToModel extension in 4.13.0-2021-05-11.<br>
Are you planning to deploy it?</p>
<p>Thank you so much for keeping the Slicer project up and running!</p>

---

## Post #13 by @lassoan (2021-05-13 04:40 UTC)

<p>This is a temporary issue due to server upgrades - see details <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444">here</a>.</p>

---

## Post #14 by @Serg (2021-05-14 02:15 UTC)

<p>Thanks for the update.<br>
MarkupsToModel is available now and just installed within today’s 4.13 release.</p>

---

## Post #15 by @Serg (2021-06-02 21:47 UTC)

<p>To calculate the distance from the other EM sensor, I added the second BreachWarning set (like BreachWarning_1). Unfortunately, the same issue appeared as it was described in the original post (May 4th).<br>
Adding even more than 2 additional Breachwarmings in Slicer 4.10.1 works fine.<br>
Can you please fix the issue in the recent Slicer 4.13?<br>
Thank you in advance!</p>

---

## Post #16 by @lassoan (2021-06-03 12:12 UTC)

<p>I’ve tested this and I could add multiple BrachWarning nodes and all the line updates worked well in a recent Slicer-4.13 release. You need to create the scene with this recent Slicer version (you cannot use a scene that was created in Slicer-4.10 because I’ve updated the module to use markups line node instead of annotation ruler). If you have any scene that does not work well then save it as an .mrb file and send it and I’ll investigate.</p>

---

## Post #17 by @Serg (2021-06-03 20:18 UTC)

<p>I created a new scene from the scratch in today’s release 4.13.0-2021-06-02 r29939 / 4d13db4, and was able to add more BreachWarnings to the scene.<br>
Unfortunately, when trying to change the model in the drop-down menu, the same behavior of the BreachWarning appears as it was in the original post<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e420aa8c679b74a0b855f246df73a5d983c48060.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e420aa8c679b74a0b855f246df73a5d983c48060.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e420aa8c679b74a0b855f246df73a5d983c48060.mp4</a>
    </source></video>
  </div><br>
.<br>
Looks like that just one small fix should be applied <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><p></p>

---

## Post #18 by @lassoan (2021-06-04 03:34 UTC)

<p>The glitch that you saw was due to the incoming transforms keep triggering update of the GUI from the scene (so it always reverted the selection to the current selection stored in the scene). An easy workaround is to stop the OpenIGTLink connection while setting up the scene.</p>
<p>I have now added some extra checks to the module to prevent these continuous updates, so latest Slicer Stable Release and latest Slicer Preview Release will not have this issue starting from tomorrow.</p>

---

## Post #19 by @Serg (2021-06-05 01:03 UTC)

<p>Works fine now. Thank you!</p>

---
