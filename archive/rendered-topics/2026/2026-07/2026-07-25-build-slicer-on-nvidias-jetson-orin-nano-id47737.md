---
topic_id: 47737
title: "Build Slicer on Nvidia's Jetson Orin Nano"
date: 2026-07-25
url: https://discourse.slicer.org/t/47737
last_bumped: 2026-07-28T01:36:52.826Z
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

## Post #4 by @Mik (2026-07-26 04:48 UTC)

<p>Good to know! Ampere GPU is much better in that case than Mali and VisualCore.</p>

---

## Post #5 by @lassoan (2026-07-27 11:11 UTC)

<p>Great! Do you find the processing and interaction speed comparable to a laptop? How is volume rendering speed? How long does it take to run TotalSegmentator?</p>

---

## Post #6 by @mau_igna_06 (2026-07-28 01:36 UTC)

<p>This is on my laptop:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b0d333c7b054abb019daabc0f353d228dcc398f.jpeg" data-download-href="/uploads/short-url/1zLx4bJSXyBbyBdtfNN0azvHw9F.jpeg?dl=1" title="Screenshot from 2026-07-27 13-57-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b0d333c7b054abb019daabc0f353d228dcc398f_2_690x387.jpeg" alt="Screenshot from 2026-07-27 13-57-21" data-base62-sha1="1zLx4bJSXyBbyBdtfNN0azvHw9F" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b0d333c7b054abb019daabc0f353d228dcc398f_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b0d333c7b054abb019daabc0f353d228dcc398f_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b0d333c7b054abb019daabc0f353d228dcc398f_2_1380x774.jpeg 2x" data-dominant-color="9B91A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2026-07-27 13-57-21</span><span class="informations">1920×1077 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/557e1723849588220066a7b3b47474f997402af1.jpeg" data-download-href="/uploads/short-url/cciJpjUCaYOPbqmjTILK0QVR2qR.jpeg?dl=1" title="Screenshot from 2026-07-27 14-35-45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/557e1723849588220066a7b3b47474f997402af1_2_690x388.jpeg" alt="Screenshot from 2026-07-27 14-35-45" data-base62-sha1="cciJpjUCaYOPbqmjTILK0QVR2qR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/557e1723849588220066a7b3b47474f997402af1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/557e1723849588220066a7b3b47474f997402af1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/557e1723849588220066a7b3b47474f997402af1_2_1380x776.jpeg 2x" data-dominant-color="9A979B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2026-07-27 14-35-45</span><span class="informations">1920×1080 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is on the Jetson<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8d81edb8cd07244267a554b2eb52d8ee23dc8e2.jpeg" data-download-href="/uploads/short-url/o5FfzqtCrSlyRb4lMrm3apIjv9M.jpeg?dl=1" title="Screenshot from 2026-07-27 15-59-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d81edb8cd07244267a554b2eb52d8ee23dc8e2_2_690x388.jpeg" alt="Screenshot from 2026-07-27 15-59-09" data-base62-sha1="o5FfzqtCrSlyRb4lMrm3apIjv9M" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d81edb8cd07244267a554b2eb52d8ee23dc8e2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d81edb8cd07244267a554b2eb52d8ee23dc8e2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8d81edb8cd07244267a554b2eb52d8ee23dc8e2_2_1380x776.jpeg 2x" data-dominant-color="9990A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2026-07-27 15-59-09</span><span class="informations">1920×1080 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I could not run totalsegmentator on the jetson either by building the SlicerTotalSegmentator extension, by using docker or by using the python module. It could be that the unified RAM is too small to fit the segmentation model</p>

---
