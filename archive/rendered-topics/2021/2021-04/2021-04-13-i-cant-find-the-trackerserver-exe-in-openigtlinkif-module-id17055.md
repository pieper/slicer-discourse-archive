---
topic_id: 17055
title: "I Cant Find The Trackerserver Exe In Openigtlinkif Module"
date: 2021-04-13
url: https://discourse.slicer.org/t/17055
---

# I can't find the TrackerServer.exe in OpenIGTLinkIF module

**Topic ID**: 17055
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/i-cant-find-the-trackerserver-exe-in-openigtlinkif-module/17055

---

## Post #1 by @wujie (2021-04-13 08:49 UTC)

<p>I can’t find the TrackerServer.exe in OpenIGTLinkIF module</p>

---

## Post #2 by @lassoan (2021-04-14 04:55 UTC)

<p>TrackerServer is a test application. You need to enable testing in CMake when you configure your OpenIGTLink build.</p>

---

## Post #3 by @wujie (2021-04-14 07:33 UTC)

<p>Thank you for your reply,but I can’t find the test application.And I want to know where to find the test application.</p>

---

## Post #4 by @lassoan (2021-04-14 14:06 UTC)

<p>You need to build OpenIGTLink to get this test executable. If you don’t want to build then you can use the OpenIGTLink server in Slicer or PlusServer (in Plus Toolkit).</p>

---

## Post #5 by @wujie (2021-04-15 11:29 UTC)

<p>Thank you Lasso,I find the PlusServer,but I don’t know how to use OpenIGTLink  server in Plus ToolKit.And  build the OpenIGTLink need to build the slicer?</p>

---

## Post #6 by @wujie (2021-04-15 11:46 UTC)

<p>Excuse me,and I want to use OpenIGTLinkIF module to  acquire the coordinates from tracker.This is my destination.</p>

---

## Post #7 by @wujie (2021-04-15 11:49 UTC)

<p>Could I realize the function of the image.![1618487250(1)|409x500](upload://gFOdYcodPZi7aHNB<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26ac1c1763169d2cb30b7fa6eab2ceaffd101bfd.png" data-download-href="/uploads/short-url/5w6T0GWfwiyntytUeDHSZHtbrOt.png?dl=1" title="1618487250(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ac1c1763169d2cb30b7fa6eab2ceaffd101bfd_2_409x500.png" alt="1618487250(1)" data-base62-sha1="5w6T0GWfwiyntytUeDHSZHtbrOt" width="409" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ac1c1763169d2cb30b7fa6eab2ceaffd101bfd_2_409x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26ac1c1763169d2cb30b7fa6eab2ceaffd101bfd_2_613x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26ac1c1763169d2cb30b7fa6eab2ceaffd101bfd.png 2x" data-dominant-color="ACABAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1618487250(1)</span><span class="informations">621×758 96.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> 84kLEbu52QI.png)</p>

---

## Post #8 by @wujie (2021-04-15 11:49 UTC)

<p>I want to realize the function of image.</p>

---

## Post #9 by @lassoan (2021-04-15 12:37 UTC)

<p><a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> should help you getting started.</p>
<p>You may find this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_2_PLUS.pptx">Plus Toolkit tutorial</a> and the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/index.html?_ga=2.97452249.792242584.1618490237-473036458.1609520395">Plus Toolkit documentation</a> useful, too.</p>

---
