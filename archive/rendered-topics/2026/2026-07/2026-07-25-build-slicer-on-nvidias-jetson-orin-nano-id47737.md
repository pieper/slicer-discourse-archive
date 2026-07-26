---
topic_id: 47737
title: "Build Slicer on Nvidia's Jetson Orin Nano"
date: 2026-07-25
url: https://discourse.slicer.org/t/47737
last_bumped: 2026-07-25T23:02:08.972Z
---

# Build Slicer on Nvidia's Jetson Orin Nano

**Topic ID**: 47737
**Date**: 2026-07-25
**URL**: https://discourse.slicer.org/t/build-slicer-on-nvidias-jetson-orin-nano/47737

---

## Post #1 by @mau_igna_06 (2026-07-25 01:43 UTC)

<p>Hi,</p>
<p>I have this developer kit and I was able to compile Slicer.</p>
<p>My steps where almost the same as provided on <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/#general-notes-building-slicer-in-ubuntu-2204-x86" class="inline-onebox" rel="noopener nofollow ugc">Project Description | NA-MIC Project Weeks</a> and <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" class="inline-onebox" rel="noopener nofollow ugc">Scripts for building Slicer on Ubuntu ARM aarch64 · GitHub</a></p>
<p>1 -</p>
<pre data-code-wrap="bash"><code class="lang-bash">sudo apt update &amp;&amp; sudo apt install git build-essential \
  cmake cmake-curses-gui cmake-qt-gui \
  libqt5x11extras5-dev qtmultimedia5-dev libqt5svg5-dev qtwebengine5-dev libqt5xmlpatterns5-dev qttools5-dev qtbase5-private-dev \
  libxt-dev libssl-dev
</code></pre>
<p>2 - Download this scripts on <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" class="inline-onebox" rel="noopener nofollow ugc">Scripts for building Slicer on Ubuntu ARM aarch64 · GitHub</a></p>
<p>3 - Run in order</p>
<pre data-code-wrap="bash"><code class="lang-bash">./build-CTKAppLauncher.sh
sudo apt-get install hwloc libhwloc-dev
./build-tbb.sh
./build-Slicer.sh
</code></pre>
<p>4 - Then Slicer build on last script fails.<br>
But after <a href="https://github.com/Slicer/Slicer/compare/main...mauigna06:Slicer:patch-8" rel="noopener nofollow ugc">doing this change to the superbuild</a> it finishes successfully.</p>
<p>5 - I can use Slicer</p>

---

## Post #2 by @Mik (2026-07-25 20:17 UTC)

<p>Do you have any visualization bugs? For example the colour bar doesn’t show up on my RockPro64 and Raspberry Pi 5, and I have a lot of console warnings from VTK.</p>

---

## Post #3 by @mau_igna_06 (2026-07-25 23:02 UTC)

<p>Works well for me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/791313f22a818725a6649342d1cc9924307e94b0.jpeg" data-download-href="/uploads/short-url/hh4Ebycc6l4Tf2WNhRemINb5dNS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/791313f22a818725a6649342d1cc9924307e94b0_2_690x389.jpeg" alt="image" data-base62-sha1="hh4Ebycc6l4Tf2WNhRemINb5dNS" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/791313f22a818725a6649342d1cc9924307e94b0_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/791313f22a818725a6649342d1cc9924307e94b0_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/791313f22a818725a6649342d1cc9924307e94b0_2_1380x778.jpeg 2x" data-dominant-color="839BAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
