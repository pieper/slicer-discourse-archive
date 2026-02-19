---
topic_id: 6078
title: "High Slicer Cpu Usage While Live Streaming"
date: 2019-03-08
url: https://discourse.slicer.org/t/6078
---

# High Slicer CPU usage while live streaming

**Topic ID**: 6078
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/high-slicer-cpu-usage-while-live-streaming/6078

---

## Post #1 by @jamesobutler (2019-03-08 19:34 UTC)

<p>I’ve been seeing high CPU usage by the Slicer process when viewing live stream images from <a href="https://plustoolkit.github.io/" rel="nofollow noopener">PLUS</a>. I’m not sure if the issue is the rendering changes between Slicer 4.8 and 4.10 or an issue with OpenIGTLinkIF.</p>
<p>Environment1: Windows 10, Slicer 4.8.1, with OpenIGTLinkIF core module<br>
Environment2: Windows 10, Slicer 4.10.1 with latest <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">SlicerOpenIGTLink</a> extension to use OpenIGTLinkIF.</p>
<ul>
<li>I streamed two <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html" rel="nofollow noopener">mmf</a> webcam devices and connected to them in Slicer as port 18944 and 18945.</li>
<li>AcqusitionRate was specified as “1” FPS for both mmf devices. Confirmed with Slicer node statistics module that each were streaming as 1 FPS.</li>
<li>Layout: SideBySide, viewing both streams at same time</li>
</ul>
<p>Using Environment1:</p>
<ul>
<li>CPU usage for Slicer process: ~3%</li>
<li>GPU usage for Slicer process: ~3%</li>
<li>If I disconnect one of the nodes, as though only streaming 1 device, CPU usage for the process doesn’t appear to change.</li>
</ul>
<p>Using Environment2:</p>
<ul>
<li>CPU usage for Slicer process: ~30%</li>
<li>GPU usage for Slicer process: ~3%</li>
<li>If I disconnect one of the nodes, as though only streaming 1 device, CPU usage for the process drops to half so about ~15%.</li>
</ul>
<p>Tagging some knowledgeable users on topic:<br>
<a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @lassoan (2019-03-08 20:21 UTC)

<p>Can you do some profiling? You might get some results using VerySleepy tool or VisualStudio’s built-in profiler, even if Slicer is just built in Release mode (you get more reliable info if you build in RelWithDebInfo).</p>
<p>What graphics card do you have in your computer?</p>
<p>I’ve found indications to that on some systems, VTK’s texture update operations take much longer time with the OpenGL2 rendering backend than with the old OpenGL backend. Maybe your testing can confirm this.</p>
<p>There have been many changes, so it is also possible that the additional CPU load comes from the OpenIGTLink or some other layers. Profiling should help in figuring out where to look.</p>

---

## Post #3 by @jamesobutler (2019-03-08 20:29 UTC)

<p>Ok, I’ll try to do some additional profiling. Right now my Slicer build is a simple release mode version.</p>
<p>I have a GTX 960 in my system with nVidia driver 398.36 (I could update this to 419.35).</p>
<p>I was looking into the following PRs that might be related.</p>
<ul>
<li>
<a href="https://github.com/commontk/CTK/pull/827" rel="nofollow noopener">commontk/CTK #827</a> ENH: Add pauseRender function to ctkVTKAbstractView</li>
<li>
<a href="https://github.com/Slicer/Slicer/pull/1011" rel="nofollow noopener">Slicer/Slicer #1011</a> BUG: Change invocation of ImageDataModifiedEvent to a CustomModifiedEvent</li>
</ul>

---

## Post #4 by @Sunderlandkyl (2019-03-08 20:45 UTC)

<p>We did some profiling here.</p>
<p>It looks like the possible culprit may be some extremely fast loops in OpenIGTLinkIO (Possibly in igtlioConnector::ConnectionAcceptThreadFunction()).</p>
<p>I’m going to add some sleep statements to see if that reduces the apparent CPU load.</p>

---

## Post #5 by @jamesobutler (2019-03-08 20:50 UTC)

<p>I’m not super familiar with profiling in visual studio, but here is what was shown after connecting the two streams into Slicer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dafc48a3366669e0ea76f924bba07654b9540ae1.png" alt="profiling" data-base62-sha1="vfeBrH5w4DiRbADWnbMpK3vJKx3" width="653" height="468"></p>

---

## Post #6 by @jamesobutler (2019-03-08 20:52 UTC)

<p>And<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29961c1cab8c948f32d808dbb125c1eaa691efb4.png" data-download-href="/uploads/short-url/5VTbtrmqLjNtuF1VX2T9zjZnyOo.png?dl=1" title="profiling2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29961c1cab8c948f32d808dbb125c1eaa691efb4.png" alt="profiling2" data-base62-sha1="5VTbtrmqLjNtuF1VX2T9zjZnyOo" width="468" height="500" data-dominant-color="3A4043"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">profiling2</span><span class="informations">649×693 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Sunderlandkyl (2019-03-08 20:56 UTC)

<p>I think the issue should be fixed by: <a href="https://github.com/IGSIO/OpenIGTLinkIO/commit/51011693a627cc95db0eec181c450b4b9fa3f416" rel="nofollow noopener">https://github.com/IGSIO/OpenIGTLinkIO/commit/51011693a627cc95db0eec181c450b4b9fa3f416</a></p>
<p>CPU usage for me went from ~15% to ~1%.</p>

---

## Post #8 by @jamesobutler (2019-03-08 23:21 UTC)

<p>Thanks for the quick fix! I built and confirmed the improvement to keep CPU usage lower. <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=6" title=":tada:" class="emoji" alt=":tada:"></p>
<p>For others to use the fix, will the SlicerOpenIGTLink extension get built and updated since the OpenIGTLinkIO dependency was updated?  Should I expect the SlicerOpenIGTLink package in tomorrow’s builds to include the fix even though there was not a new commit to the SlicerOpenIGTLink repo?</p>

---

## Post #9 by @Sunderlandkyl (2019-03-09 05:40 UTC)

<p>It should be. I’ll double check tomorrow to make sure it’s included.</p>

---

## Post #10 by @nayanw775 (2021-02-18 08:47 UTC)

<p>Hi Sunderland,</p>
<p>I have been facing the same issue but I am unable to locate above mentioned code to change it, where can I find it in the PlusApp code(OpenIGTLinkIO). I am using windows 10.<br>
Can you please guide me with instructions, I am totally new to it.</p>
<p>Thanks<br>
Nayan</p>

---

## Post #11 by @Sunderlandkyl (2021-02-18 16:52 UTC)

<p>The mentioned fix was integrated in OpenIGTLinkIO and is included in both Plus and the SlicerOpenIGTLink extension.<br>
What is the issue that you are having?</p>

---

## Post #12 by @nayanw775 (2021-02-19 04:29 UTC)

<p>So I will start from the beginning, We are using PlusApp and slicer for the navigation purpose, As soon as I launch server for the above method my system gets very slow and causes a lapse in the tracking after fiducial registration, before launching the server CPU usage is in between 5-10% and as soon as I launch and start tracking CPU usage goes to 100%<br>
PC configuration - OS -Windows 10, RAM -16GB, Graphic Card-6GB Nvidia</p>
<p>I suppose PC configuration is fine, may be I need to change some settings in the PlusApp or IGTLinkIF, I don’t know exactly where the problem lies.<br>
What should I change in the code to reduce my CPU usage and to minimize the lapse.</p>

---

## Post #13 by @Sunderlandkyl (2021-02-19 15:50 UTC)

<p>That would depend on the device. Could you create a discussion for this on the PlusLib Github page (<a href="https://github.com/PlusToolkit/PlusLib/discussions" class="inline-onebox" rel="noopener nofollow ugc">Discussions · PlusToolkit/PlusLib · GitHub</a>) with more info about your Plus version and config file?</p>

---
