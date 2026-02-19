---
topic_id: 2309
title: "Volume Rendering Vtk 9 And Qt5 Crop Doesnt Work Correctly In"
date: 2018-03-14
url: https://discourse.slicer.org/t/2309
---

# Volume rendering, VTK 9 and Qt5 - Crop doesn't work correctly in master

**Topic ID**: 2309
**Date**: 2018-03-14
**URL**: https://discourse.slicer.org/t/volume-rendering-vtk-9-and-qt5-crop-doesnt-work-correctly-in-master/2309

---

## Post #1 by @hherhold (2018-03-14 01:30 UTC)

<p>MacOS 10.12.6, AMD Radeon R9 M370X - crop doesn’t work properly - it appears to clip the view rather than cropping the volume. This is master, updated through <a class="mention" href="/u/jcfr">@jcfr</a>’s DriverScript pull of a couple hours ago.</p>

---

## Post #2 by @jcfr (2018-03-14 03:27 UTC)

<p>I think that <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a> is working on fixes related to cropping and volume rendering that should land in VTK master anytime. We will then update the version used in Slicer.</p>
<p>That said, we would need more details to know for sure. Could you give more details about the data, the volume rendering setting and may be include a screenshot ?</p>

---

## Post #3 by @hherhold (2018-03-14 11:11 UTC)

<p>Yeah, sorry about that - I’ve been trying to get some representative images. It’s a lot easier to see in motion…</p>
<p>These are from CTACardio using the chest vessels preset. First is 4.8.1:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ad5cb7d015a1eff2031659abc6e4c85da41a248.jpeg" data-download-href="/uploads/short-url/aG1nWDJHmBaZemIqAZ8OvQl3U3S.jpg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad5cb7d015a1eff2031659abc6e4c85da41a248_2_653x500.jpg" alt="1" data-base62-sha1="aG1nWDJHmBaZemIqAZ8OvQl3U3S" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad5cb7d015a1eff2031659abc6e4c85da41a248_2_653x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad5cb7d015a1eff2031659abc6e4c85da41a248_2_979x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ad5cb7d015a1eff2031659abc6e4c85da41a248_2_1306x1000.jpg 2x" data-dominant-color="5B5450"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2826×2162 1.19 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can see at the edges of the ROI, it crops the volume and you see internals.</p>
<p>This is master, built March 13:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5661d4ff58e4432f19ebddc071a70d81ea908c08.jpeg" data-download-href="/uploads/short-url/ckaFkoRl1fqmzBGSiiKD6IDmQB2.jpg?dl=1" title="0%203-13-2018%20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5661d4ff58e4432f19ebddc071a70d81ea908c08_2_652x500.jpg" alt="0%203-13-2018%20" data-base62-sha1="ckaFkoRl1fqmzBGSiiKD6IDmQB2" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5661d4ff58e4432f19ebddc071a70d81ea908c08_2_652x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5661d4ff58e4432f19ebddc071a70d81ea908c08_2_978x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5661d4ff58e4432f19ebddc071a70d81ea908c08_2_1304x1000.jpg 2x" data-dominant-color="524B46"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0%203-13-2018%20</span><span class="informations">2832×2170 1.15 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you look carefully, you can see the top of the crop volume at the top of the chest volume. The crop ROI doesn’t crop any volume data - it just seems to clip the view.</p>
<p>I put a quick video in:  <a href="https://drive.google.com/open?id=1__al9fj6B17e1xDKWW7zvunC3Ks1qOkB" class="inline-onebox" rel="noopener nofollow ugc">Slicer - Google Drive</a></p>
<p>Hopefully that will give you an idea.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #4 by @hherhold (2018-03-14 12:35 UTC)

<p>I also get these on the console:</p>
<pre><code>Switch to module:  "VolumeRendering"
QPainter::begin: Paint device returned engine == 0, type: 2
QPainter::setPen: Painter not active
QPainter::setBrush: Painter not active
QPainter::setRenderHint: Painter must be active to set rendering hints
QPainter::begin: Paint device returned engine == 0, type: 2
QPainter::setPen: Painter not active
QPainter::setBrush: Painter not active
QPainter::setRenderHint: Painter must be active to set rendering hints
QPainter::begin: Paint device returned engine == 0, type: 2
QPainter::setPen: Painter not active
QPainter::setBrush: Painter not active
QPainter::setRenderHint: Painter must be active to set rendering hints</code></pre>

---

## Post #5 by @cpinter (2018-03-14 13:39 UTC)

<p>Hi Hollister! I tried it with the latest version and it seems to be working OK on Windows. I started 4.8.1 to see if there is any difference, and they look the same. Maybe this is an issue only on Mac?</p>
<p>That said the volume rendering cropping is not supposed to crop the actial volume data, only restrict the region volume rendering considers.</p>

---

## Post #6 by @cpinter (2018-03-14 13:54 UTC)

<p>And I don’t get any errors either. I’m building a Slicer on Mac now.</p>

---

## Post #7 by @lassoan (2018-03-14 14:08 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> You seem to have the same issue as everybody else (<a href="https://issues.slicer.org/view.php?id=4510">https://issues.slicer.org/view.php?id=4510</a>). A fix was promised to be integrated into VTK by tomorrow. From there Slicer should be able to get it quickly.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> The error only occurs if you enable depth peeling and use GPU volume rendering.</p>

---

## Post #8 by @hherhold (2018-03-14 14:50 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hey Andras - ! I should have checked Mantis before posting - sorry about that!</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #9 by @cpinter (2018-03-14 15:10 UTC)

<p>It just occurred to me that depth peeling makes rendering slower. As you had issues with performance, and it now turns out that you use depth peeling, maybe you can further improve performance by disabling that feature. Of course if you want to render surfaces inside the rendered volume, then you’ll need it, but otherwise it’s not essential.</p>

---
