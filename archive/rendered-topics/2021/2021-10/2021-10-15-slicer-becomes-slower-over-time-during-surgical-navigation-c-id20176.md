# Slicer becomes slower over time during surgical navigation cases

**Topic ID**: 20176
**Date**: 2021-10-15
**URL**: https://discourse.slicer.org/t/slicer-becomes-slower-over-time-during-surgical-navigation-cases/20176

---

## Post #1 by @Prashant_Pandey (2021-10-15 19:12 UTC)

<p>We’re using Windows 10, Slicer 4.11, SlicerIGT and PLUS to do navigated surgery. We’re streaming data from an NDI optical tracker and an ultrasound probe using OpenIGTLink.</p>
<p>We are running into problems with Slicer slowing down significantly over time. Usually by the time the surgeon is interacting with the instruments, Slicer and the other software has been running on our system for 1-2 hours. When interacting with Slicer, the GUI is slow to respond and all simple or complex processing (i.e. scrolling through slices or volume rendering) is very slow. Segmenting (via MatlabBridge) and registering volumes (SlicerElastix) takes 30 - 60 minutes when previously it would take 3-5 minutes for the same volumes in the same version of Slicer. There is significant lag in updating the surgical tool position on screen making it difficult for the surgeon to interpret the scene.</p>
<p>Any ideas what causes the slowdown over  time? Is there a memory leak associated with Slicer or PLUS? In Slicer we typically have 3-4 cropped CT scans loaded (~ 400 x 400 x 400 voxels), and this has not been a problem before. Our machine is also relatively powerful with 32GB RAM and a dedicated NVIDIA GPU.</p>

---

## Post #2 by @rbumm (2021-10-17 13:24 UTC)

<p>First thing I would try is to upgrade Slicer to the Preview version.</p>

---

## Post #3 by @pieper (2021-10-17 14:25 UTC)

<p>I’d guess there’s either a memory leak or that there are data or observers being added to the scene each frame and not cleared up.</p>
<p>I agree with <a class="mention" href="/u/rbumm">@rbumm</a> that the easiest thing to try is checking if it’s already fixed in the preview.</p>
<p>Second suggestion would be to attach a profiler to see where Slicer is spending time and how that changes over time.  I’d suggest Activity Monitor on mac, perf for linux, or Very Sleepy for windows.  Sometimes it helps to try different platforms for profiling even if you are deploying on only one (you may learn different things on different platforms).</p>
<p>Finally I’d strongly recommend you develop a SelfTest that emulates your real-world use case as closely as possible, e.g. by generating synthetic tracker data or replaying recorded data.  You can run the test over night or with various options turned on or off to home in on what leads to the slowdown.</p>
<p>Fortunately with your software components (Slicer, PLUS, etc) you have total visibility and control of the software so there’s no reason you shouldn’t be able to identify and fix whatever is happening.  If it’s something in one of the Slicer or PLUS execution paths please do let the relevant maintainers know so it can be fixed for others.</p>

---

## Post #4 by @pll_llq (2021-10-19 06:07 UTC)

<p><a class="mention" href="/u/prashant_pandey">@Prashant_Pandey</a> can you please update this thread once you find what’s causing the slow down? This info could be very valuable for other community members</p>

---

## Post #5 by @Prashant_Pandey (2021-10-19 15:15 UTC)

<p>Thanks for all the advice. I will check each of these to see what the issue is.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="20176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>there are data or observers being added to the scene each frame and not cleared up.</p>
</blockquote>
</aside>
<p>How do I check if this is what is happening? I do add observers during navigation and I have written code to clean them up too, but I am not sure if the clean up is being done correctly.</p>

---

## Post #6 by @lassoan (2021-10-19 17:00 UTC)

<p><a class="mention" href="/u/pll_llq">@pll_llq</a> it could be useful if you could do independent testing - run your navigation system for a few hours and see if you see any performance degradation.</p>

---

## Post #7 by @pieper (2021-10-19 18:17 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="5" data-topic="20176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>How do I check if this is what is happening? I do add observers during navigation and I have written code to clean them up too, but I am not sure if the clean up is being done correctly.</p>
</blockquote>
</aside>
<p>One fairly easy way to get a sense of what’s going on is to pause the debugger repeatedly and look at the stack traces to see where the code is spending its time.  This is a manual version of statistical sampling that is actually very powerful to see where the application is spending time.  If you see a lot of time spent in callback code then probably you have too many observers.</p>
<p>If you are adding observers you can just use <code>getNode</code> and <code>print(node)</code>  to see if the list of observers is getting longer over time.</p>

---

## Post #8 by @Prashant_Pandey (2022-04-20 04:04 UTC)

<p>Just an update after a few months - I narrowed this issue down to the PLUS servers (one for acquisition and one for processing as suggested <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmVolumeReconstruction.html#:~:text=Use%20a%2064%2Dbit%20release.%20If%20some%20devices%20are%20only%20supported%20in%2032%2Dbit%20releases%20then%20run%20two%20instances%20of%20PlusServer." rel="noopener nofollow ugc">here</a> I found stopping the servers helped speed computational intense steps in Slicer such as for registration.</p>

---
