# Surgical tool tracking using NDI polaris and 3D Slicer

**Topic ID**: 4157
**Date**: 2018-09-20
**URL**: https://discourse.slicer.org/t/surgical-tool-tracking-using-ndi-polaris-and-3d-slicer/4157

---

## Post #1 by @kamrul079 (2018-09-20 14:55 UTC)

<p>How to do this type of work in 3d slicer using PLUS toolkit? Is there any step by step procedures?<br>
</p><div class="lazyYT" data-youtube-id="d_vHpBRZJco" data-youtube-title="Surgical tool tracking using OptiTrack Duo and 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #2 by @lassoan (2018-09-20 15:05 UTC)

<p>Step-by-step instructions, sample data sets, etc. are all provided at <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT training page</a>. Let us know here if you have trouble following any of the tutorials.</p>

---

## Post #3 by @kamrul079 (2018-09-20 15:09 UTC)

<p>I have gone through all the tutorials. Tutorials has explanation for pre-recorded video. But specifically not for a real phantom or model as like in the above video link.</p>

---

## Post #4 by @lassoan (2018-09-20 16:29 UTC)

<p>In case of real hardware you use OpenIGTLinkIF module to receive transforms and images from Plus toolkit, instead of replaying them using Sequences module. Everything else (calibration, visualization, etc.) are done exactly the same.</p>
<p><a href="http://www.slicerigt.org/wp/user-tutorial/">U-03 tutorial</a> gives a short introduction to how to set up your hardware connections. <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/index.html">Plus toolkit’s user manual</a> gives you all the details.</p>
<p>If you have problems with setting up configuration file for data collection then post questions on Plus toolkit website. If you need help with tool calibration, registration, visualization then post your questions on this forum.</p>

---

## Post #5 by @kamrul079 (2018-09-20 16:46 UTC)

<p>Thank you for your reply. I know actually how to connect through the hardware device like a webcam or NDI tracker. But, I need to know the next steps. Let’s say I am using a LEGO phantom. I have my real LEGO model. Now how can I do the navigation using my webcam, AR tags and my LEGO phantom. I would appreciate if you give me an insight</p>

---

## Post #6 by @kamrul079 (2018-09-20 16:49 UTC)

<p>I had gone through the IGSTK tutorial. Actually, I was trying to do the same stuffs but using the PLUStoolkit not IGSTK.</p>

---

## Post #7 by @lassoan (2018-09-20 17:15 UTC)

<p>You can do everything by using Slicer/SlicerIGT/Plus as you can do with IGSTK. An equivalent to IGSTK’s Lego navigation tutorial is available in <a href="https://github.com/PerkLab/PerkLabBootcamp/tree/master/Doc">PerkLab bootcamp Plus tutorial</a> that explains how to set up tracking of 2D barcodes, followed by pivot calibration and landmark registration explained in SlicerIGT tutorials.</p>

---
