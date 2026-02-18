# Ubuntu 18.04 scaling small issues

**Topic ID**: 2622
**Date**: 2018-04-18
**URL**: https://discourse.slicer.org/t/ubuntu-18-04-scaling-small-issues/2622

---

## Post #1 by @Davide_Punzo (2018-04-18 12:44 UTC)

<p>Hi all,</p>
<p>I personally don’t use 4k monitors, however I  have just tried running Slicer in a 4k monitor on ubuntu 18.04 with the scaling option (recently added in ubuntu, 200%).</p>
<p>This is the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/404706492991cb2cd4568003535cd7d744cc662e.png" data-download-href="/uploads/short-url/9aCJ6yRuNFqJ82mGo6Y0pWncL1A.png?dl=1" title="Screenshot-20180418115402-3966x2107" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/404706492991cb2cd4568003535cd7d744cc662e_2_690x366.png" alt="Screenshot-20180418115402-3966x2107" data-base62-sha1="9aCJ6yRuNFqJ82mGo6Y0pWncL1A" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/404706492991cb2cd4568003535cd7d744cc662e_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/404706492991cb2cd4568003535cd7d744cc662e_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/404706492991cb2cd4568003535cd7d744cc662e_2_1380x732.png 2x" data-dominant-color="9192A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot-20180418115402-3966x2107</span><span class="informations">3966×2107 1.04 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>it kind of works, but many icons are of different sizes and at the end it does not look too good. I was wandering if this is just an issue with ubuntu, how it does the scaling (it looks that it scales only the text and the relative GUI) or do you experience this also in windows? (on mac everything seems working on retina display with scaling).</p>

---

## Post #2 by @lassoan (2018-04-18 15:55 UTC)

<p>Thanks for testing this. If scaling has just been added to Ubuntu then probably it will take some time for Qt developers to take advantage of it and use it to optimize display.</p>

---

## Post #3 by @ihnorton (2018-04-18 16:43 UTC)

<p>I believe 18.04 ships with Wayland as an optional graphics stack, so if you have some time to rebuild, it might be worth enabling QtWayland in your qt build and then see if Slicer runs at all/better:</p>
<p><a href="https://wiki.qt.io/QtWayland#Run_Qt_applications_as_Wayland_clients" class="onebox" target="_blank">https://wiki.qt.io/QtWayland#Run_Qt_applications_as_Wayland_clients</a></p>
<p>(I’ve read somewhere that hidpi support is better in wayland – and X11 isn’t getting much effort there)</p>

---

## Post #4 by @Davide_Punzo (2018-04-19 09:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2622" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Thanks for testing this. If scaling has just been added to Ubuntu then probably it will take some time for Qt developers to take advantage of it and use it to optimize display.</p>
</blockquote>
</aside>
<p>yeah, most likely will take at least another distro release in time for having the scaling sorted out in linux (at least in ubuntu).</p>
<aside class="quote no-group quote-modified" data-username="ihnorton" data-post="3" data-topic="2622" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I believe 18.04 ships with Wayland as an optional graphics stack, so if you have some time to rebuild, it might be worth enabling QtWayland in your qt build and then see if Slicer runs at all/better:</p>
<p><a href="https://wiki.qt.io/QtWayland#Run_Qt_applications_as_Wayland_clients" class="inline-onebox" rel="noopener nofollow ugc">QtWayland - Qt Wiki</a></p>
<p>(I’ve read somewhere that hidpi support is better in wayland – and X11 isn’t getting much effort there)</p>
</blockquote>
</aside>
<p>I tried to use Wayland in ubuntu 17.10. However it was very bugged, specifically there was almost no support in the nvidia driver for wayland. On fresh install of ubuntu 18.04, the default is back to Xorg and I can’t even go back to wayland (maybe it is a bug, there is no gear option at login screen). It seems, unfortunately, we will have to wait at least the next release to have decent wayland support.</p>

---

## Post #5 by @brhoom (2018-10-24 21:59 UTC)

<p>I had the same issue. I changed the font size from Slicer settings.</p>

---

## Post #6 by @brhoom (2018-10-28 14:00 UTC)

<p>I did some testing today using Slicer binaries 8.4.1, 4.10.0 and nightly build 4.11.0  2018-10-23. It seems 4.8.1 adapts better to different monitors. I think the problem is related to Slicer version as I am using the same hardware, system, and settings. Is it possible to have the same behavior in recent versions?</p>

---

## Post #7 by @pieper (2018-10-28 15:05 UTC)

<p>Slicer 4.8 used Qt 4.x and 4.10 uses Qt 5.x and there appears to be some debugging to do related to handling of various ‘retina’ and other multiresolution monitor support (the hardware and OS features are continuing to evolve, I’m sure).  For example <a href="https://discourse.slicer.org/t/building-on-mac-10-14-mojave/4554/2">my recent mac build is completely screwed up</a> with the latest Qt and macOS.</p>
<p>This will require some experimentation on the developer side, but also we’ll need a lot of people to test and provide feedback as we try different settings.</p>

---

## Post #8 by @brhoom (2018-10-28 15:25 UTC)

<blockquote>
<p>Slicer 4.8 used Qt 4.x and 4.10 uses Qt 5.x</p>
</blockquote>
<p>Thanks for the info. I am happy to help with the testing. BTW, I tried building 4.10 with Qt4 and it seems there is no scaling problem.</p>

---

## Post #9 by @lassoan (2018-10-28 16:13 UTC)

<p>Qt4 did not do any scaling, therefore issues with high-DPI screens are completely different on Qt4 and Qt5.</p>

---
