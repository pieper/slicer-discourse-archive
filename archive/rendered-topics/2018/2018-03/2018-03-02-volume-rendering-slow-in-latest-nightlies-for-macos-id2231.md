---
topic_id: 2231
title: "Volume Rendering Slow In Latest Nightlies For Macos"
date: 2018-03-02
url: https://discourse.slicer.org/t/2231
---

# Volume rendering slow in latest nightlies for MacOS

**Topic ID**: 2231
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/volume-rendering-slow-in-latest-nightlies-for-macos/2231

---

## Post #1 by @hherhold (2018-03-02 21:03 UTC)

<p>Hey guys,</p>
<p>I’m pretty sure I saw something about this come across on the Development list in the last week or so but a quick search didn’t come up with anything…</p>
<p>Volume rendering is significantly slower with the latest 4.9 nightlies. I have one from January 3 that I’ve been using and it’s fine. I’m assuming this probably has to do with the transition to VTK9?</p>
<p>(My main reason for asking is I’d really like to use vtkMRMLPlotSeriesNode and it doesn’t appear to be available in the Jan 3 nightly, but the more recent nightlies are unusable.)</p>
<p>This is on MacOS 10.12.6.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @jcfr (2018-03-02 21:13 UTC)

<p>Thanks for the report.</p>
<p><a class="mention" href="/u/hherhold">@hherhold</a> Could you provide more details about the settings select in the volume rendering module, and the details of your GPU.</p>
<p>We really need to pinpoint what is happening here. There are already two issues related to slower rendering:</p>
<ul>
<li><a href="https://issues.slicer.org/view.php?id=4423">4423: OpenGL2: Slow slice scrolling if volume rendering is enabled</a></li>
<li><a href="https://issues.slicer.org/view.php?id=4496">4496: OpenGL2: Reslicing speed can be very slow on Windows</a></li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a> It would be great  to work together to that can clearly understand the bottle neck:</p>
<ul>
<li>Video driver issue</li>
<li>Problem integrating the vtk GPU volume rendering mapper in Slicer following the transition to VTK9</li>
<li>Problem within the  vtk GPU volume rendering mapper</li>
</ul>

---

## Post #3 by @hherhold (2018-03-02 21:34 UTC)

<p>This is on a Mid 2015 MacBook Pro with AMD Radeon R9 M370X graphics (2G).</p>
<p>I’m rebuilding the latest master from scratch right now to see if I can help debug.</p>
<p>Basically, I just turn on volume rendering and rotate around. It’s significantly slower, and changing the transfer function is <em>really</em> slow.</p>
<p>I’ll update when my build finishes and give you more specifics.</p>
<p>Thanks!!!</p>

---

## Post #4 by @lassoan (2018-03-02 22:00 UTC)

<p>What is the GPU memory size setting? Is quality setting at maximum or adaptive? Any warnings or errors in the log? What is the volume size and scalar type? Is it slower with Slicer sample data sets? How the speed compares to CPU-based rendering?</p>

---

## Post #5 by @hherhold (2018-03-02 22:34 UTC)

<p>Oops, all excellent questions that I should have added in previous post.</p>
<p>Memory size = 2G<br>
Quality = Adaptive</p>
<p>My data set:<br>
Volume dimensions = 385 x 413 x 996<br>
Volume type = 16 bit scalar<br>
No errors on console, but a couple of what look like unrelated warnings:</p>
<pre><code>Switch to module:  "VolumeRendering"
Warning: In /Volumes/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkObserverManager.cxx, line 131
vtkObserverManager (0x7f97c1bae510): The same object is already observed with the same priority. The observation is kept as is.

Warning: In /Volumes/Dashboards/Nightly/Slicer-0/Libs/MRML/Core/vtkObserverManager.cxx, line 131
vtkObserverManager (0x7f97c1bae510): The same object is already observed with the same priority. The observation is kept as is.

ctkDoubleSlider::setSingleStep( 200 ) is outside of valid bounds.

Slicer sample data set is better (smaller) but it's still a bit slow.
</code></pre>
<p>My dataset actually crashed the OS at one point. Sounds like a driver/video card problem. Any idea where I should look in system logs?</p>

---

## Post #6 by @hherhold (2018-03-02 23:02 UTC)

<p>CPU rendering worked with sample set (MRBrainTumor1). Will try with my dataset shortly - I expect it will be slow.</p>

---

## Post #7 by @hherhold (2018-03-03 13:05 UTC)

<p>Build completed on my machine with no problems. I do get these, however, on a number of libraries, but I expect they’re unrelated to performance issues:</p>
<pre><code>dlopen(/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so, 2): no suitable image found.  Did find:
/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/./vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32888) &gt; 32768
/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32888) &gt; 32768
/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32888) &gt; 32768
/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-loadable-modules/vtkSlicerVolumeRenderingModuleMRMLDisplayableManagerPython.so: malformed mach-o: load commands size (32888) &gt; 32768
</code></pre>
<p>CPU rendering is functional but very slow with this dataset.</p>
<p>I’m trying to run Slicer using Instruments in MacOS while changing the opacity mapping transfer function to see what’s eating up time. No conclusions yet - I haven’t used Instruments in a long time so there’s a little learning curve.</p>

---

## Post #8 by @hherhold (2018-03-04 12:50 UTC)

<p>I’m not sure if this is a clue or not, but click-dragging in a slice view to change the window level is noticeably slower than a January 3 nightly build - performance issues do not appear to be just volume rendering.</p>

---

## Post #9 by @lassoan (2018-03-04 13:41 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="8" data-topic="2231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>dragging in a slice view to change the window level is noticeably slower</p>
</blockquote>
</aside>
<p>Probably unrelated, but we have noticed this, too. See <a href="https://issues.slicer.org/view.php?id=4496" class="inline-onebox">VTK OpenGL2 Backend: Reslicing speed can be very slow on Windows · Issue #4496 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #10 by @hherhold (2018-03-05 18:10 UTC)

<p>I’m not sure if this helps or not, but some observations:</p>
<ul>
<li>OpenGL performance with viewing models is fast - to my eye, faster than my “benchmark” January 3 nightly. In fact, nearly everything seems faster except volume rendering.</li>
<li>When turning on volume rendering, the volume appears in a reasonable amount of time, and when it is relatively small in the view, rotating around is tolerably quick.</li>
<li>Zooming in slows everything down, but it’s still useable.</li>
<li>Changing the opacity mapping is extremely slow to respond.</li>
<li>Once the opacity map is changed, rotating the volume is extremely slow, almost to the point of hanging the program.</li>
<li>Changing the interactive frame rate slider in volume rendering has no effect.</li>
</ul>
<p>I get the same results on 16 or 8 bit data.</p>
<p>I’m happy to help debug.</p>
<p>-Hollister</p>

---

## Post #11 by @hherhold (2018-03-06 12:05 UTC)

<p>Andras - I tried volume rendering in the latest nightly of ParaView, but I think it does not support GPU volume rendering - does this sound correct?</p>

---

## Post #12 by @cpinter (2018-03-06 16:23 UTC)

<p>I noticed that even on Windows, volume rendering is much slower with OpenGL2. The frame rate is 2-5 times faster (apparently depending on the image) in 4.8.1 using the same image and default settings than in the nightly.</p>
<p>Is it possible that the defaults of the new vtkGPUVolumeRayCastMapper are set to an unnecessarily high<br>
setting? For example the fixed sampling distance of of minSpacing/10 may be too small, and enabling LockSampleDistanceToInputSpacing would help?</p>

---

## Post #13 by @cpinter (2018-03-06 17:36 UTC)

<p>I tried it and there is a huge improvement in performance using LockSampleDistanceToInputSpacing, while I cannot notice any degradation in quality. I’ll send a PR shortly with other minor changes (such as the option to use jittering to reduce the wood-grain effect).</p>

---

## Post #14 by @hherhold (2018-03-06 17:55 UTC)

<p>This is great news - thank you very much!</p>

---

## Post #15 by @cpinter (2018-03-08 17:14 UTC)

<p>I tried a few options and although the results are promising they are not conclusive. I issued a <a href="https://github.com/Slicer/Slicer/pull/911">pull request</a>, the fate of which will be decided by the core developers. Please stand by</p>

---

## Post #16 by @hherhold (2018-03-08 20:53 UTC)

<p>OK, I took a look at the comments in the pull request. Is there a git command for me to incorporate those changes into my fork to test before they’re merged into master? I’m forked off master, and then I have a local repository of that fork, and I do the usual “git fetch upstream”, “git merge upstream/master”, and “git push” to keep it up to date.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #17 by @cpinter (2018-03-08 20:55 UTC)

<p>You need to add my Slicer fork as a remote, then you can cherry-pick that commit from the branch to your local repository.</p>

---

## Post #18 by @hherhold (2018-03-08 22:05 UTC)

<p>OK, thanks.</p>
<p>I’m not very savvy in git - I did an add remote of your fork, then a fetch, then a merge of your volume-rendering-performance-options branch. I couldn’t find the right incantation for cherry-pick - hopefully this will do the right thing.</p>
<p>I don’t have any changes in my fork, so if I’ve completely screwed it up and have to blow it away and start over, that’s fine.</p>
<p>It’s building now - I will let you know.</p>
<p>Thanks!</p>

---

## Post #19 by @jcfr (2018-03-08 22:21 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="18" data-topic="2231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’m not very savvy in git</p>
</blockquote>
</aside>
<p>I suggest you install <a href="http://hub.github.com/">http://hub.github.com/</a> ,  you will then have an alias from <code>git</code> to <code>hub</code> executable and will streamline your process</p>
<p>You would then simply do:</p>
<pre><code class="lang-auto">git remote add cpinter
git fetch cpinter
git checkout -b name-of-topic cpinter/name-of-topic
</code></pre>
<p>It also simplify creating pull request and forking repo. Reading the associated doc is worth it.</p>

---

## Post #20 by @hherhold (2018-03-08 22:26 UTC)

<p>Will do. Thanks!!</p>
<p>-Hollister</p>

---

## Post #21 by @cpinter (2018-03-13 21:10 UTC)

<p>I integrated the changes in Slicer core, tomorrow’s nightly should include these. Basically the LockSampleDistanceToInputSpacing option is now on by default in Adaptive mode, but Maximum quality mode is the same. The jittering option is exposed on the UI, in advanced rendering properties (when using GPU).</p>

---

## Post #22 by @chir.set (2018-03-16 17:02 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="2231">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>huge improvement in performance using LockSampleDistanceToInputSpacing</p>
</blockquote>
</aside>
<p>Built commit 12806744f on Arch Linux (VTK9). I just want to confirm the huge visual performance gain in Volume Rendering, when moving around the model. Even my low powered AMD Kaveri iGPU renders quite nicely via HDMI on a Full HD wide TV screen. It has never been that good !</p>

---
