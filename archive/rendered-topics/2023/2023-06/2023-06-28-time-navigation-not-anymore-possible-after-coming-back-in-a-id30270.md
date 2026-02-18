# time navigation not anymore possible after coming back in a saved mitral valve tracing from a 3DE loop

**Topic ID**: 30270
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/time-navigation-not-anymore-possible-after-coming-back-in-a-saved-mitral-valve-tracing-from-a-3de-loop/30270

---

## Post #1 by @mvergnat (2023-06-28 02:48 UTC)

<p>Operating system: windows<br>
Slicer version: 5.2.2</p>
<p>hello to everybody,</p>
<p>sorry for not being perfect, I am Slicer beginner and also Slicer Forum beginner. I try my best:</p>
<p>So,<br>
I did a mitral valve segmentation from a 4DE Volume loop.<br>
everything went very fine.<br>
I saved data.</p>
<p>then I want to come back.</p>
<p>I upload data (or I also directly clicked on the slicer supported file (.mml) where it is saved).<br>
everything comes again (segments traced before, echo loop), no problem.</p>
<p>The echo loop is also there (when I click on play/pause button, loop moves).</p>
<p>Then I open the module segment editor.<br>
it functions ok<br>
BUT then I loose the echo loop: the segments are there, superimposed on the frame 15 of the echo loop (I did tracing of valve on this frame), BUT I cannot anymore navigate in time through the echo loop: the play/pause button does not function anymore.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e89e24bea00dccfe9bb7d207f647f67afaf8dc44.jpeg" data-download-href="/uploads/short-url/xbPAPJgzE6wLwHiXnZLNyLjlBFq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89e24bea00dccfe9bb7d207f647f67afaf8dc44_2_690x388.jpeg" alt="image" data-base62-sha1="xbPAPJgzE6wLwHiXnZLNyLjlBFq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89e24bea00dccfe9bb7d207f647f67afaf8dc44_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89e24bea00dccfe9bb7d207f647f67afaf8dc44_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e89e24bea00dccfe9bb7d207f647f67afaf8dc44_2_1380x776.jpeg 2x" data-dominant-color="79777F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can anything help to better understand the problem??<br>
Many thx for help!</p>
<p>mathieu</p>
<p>3D slicer is a miraculous tool</p>
<p>(I did a lot of research in 2008 in the originating lab for valve tracing in 4Decho on Tomtec derived program (Gorman Lab, HUP), that is apparently where come from the 3D slicer heart segmentation).</p>

---

## Post #2 by @lassoan (2023-06-28 02:57 UTC)

<p>When you open Segment Editor, the module probably automatically shows the leaflet segmentation volume (which is a single 3D volume) as background volume. If you want to see other frames of the time sequence then you can select that volume as foreground volume and adjust the foreground volume opacity.</p>

---
