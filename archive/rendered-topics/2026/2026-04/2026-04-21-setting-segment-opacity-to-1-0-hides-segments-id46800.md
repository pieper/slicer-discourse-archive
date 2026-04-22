---
topic_id: 46800
title: "Setting Segment Opacity To 1 0 Hides Segments"
date: 2026-04-21
url: https://discourse.slicer.org/t/46800
---

# Setting segment opacity to < 1.0 hides segments

**Topic ID**: 46800
**Date**: 2026-04-21
**URL**: https://discourse.slicer.org/t/setting-segment-opacity-to-1-0-hides-segments/46800

---

## Post #1 by @chir.set (2026-04-21 17:23 UTC)

<p>If the opacity of a segment is reduced from the default 1.0, either for the whole segmentation or for the selected segment, the 3D representation does not persist. It appears again if set to 1.0.</p>
<p>This is seen in Linux builds on 2 machines (5.10, today’s preview, self-built), all of them using Qt5.</p>
<p>It does not seem to have been reported yet, though it is observed in 5.10 stable.</p>
<p>May be some users might report if it’s a systemic issue.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2026-04-21 17:47 UTC)

<p>Can you provide an example?  I’m not seeing what you describe.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9693432063596c519ce2699e992be060d3488b9a.jpeg" data-download-href="/uploads/short-url/lu37XA9iTugIWpQGWyqqcTmivG2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9693432063596c519ce2699e992be060d3488b9a_2_690x324.jpeg" alt="image" data-base62-sha1="lu37XA9iTugIWpQGWyqqcTmivG2" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9693432063596c519ce2699e992be060d3488b9a_2_690x324.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9693432063596c519ce2699e992be060d3488b9a_2_1035x486.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9693432063596c519ce2699e992be060d3488b9a_2_1380x648.jpeg 2x" data-dominant-color="A2A19D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×902 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @chir.set (2026-04-21 18:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="46800">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Can you provide an example?</p>
</blockquote>
</aside>
<p>This video in 5.10 is demonstrative.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd52b11204bbad23b23a4145717cd58527a229cd.mp4">
  </div><p></p>

---

## Post #4 by @jamesobutler (2026-04-21 19:34 UTC)

<p>I’m also unable to replicate using Slicer 5.10.0 on the Windows platform.</p>
<p>Therefore, this may be Linux specific? <a class="mention" href="/u/chir.set">@chir.set</a> Did this suddenly start happening or do you think it has been an issue for awhile? Do you know a version when it did work before? Just wondering if it is a graphics issue specific to your machine, or something more generally observed on the Linux platform you are using.</p>

---

## Post #5 by @chir.set (2026-04-21 20:32 UTC)

<p>I noticed that as from today. I can’t say if it existed a few days ago since I don’t tweak opacity of segments every day.</p>
<p>Both machines run Arch, regularly updated, and have a Ryzen GPU. AFAIU, the 3D representation of segments is not GPU rendered like Volume Rendering, the latter having no malfunction.</p>
<p>I’ll be attentive to this and report if it gets back to normal, magically.</p>

---

## Post #6 by @pieper (2026-04-21 20:49 UTC)

<p>Thanks for the video.  I tried the exact same thing on a Ubuntu machine with an nvidia card and did not see the behavior (all worked as I expected).  Maybe you can try on a different machine or boot a different OS, since it may be GPU or driver related.</p>

---

## Post #7 by @lassoan (2026-04-21 23:21 UTC)

<p>5.10 is widely used and nobody has reported this so far, so most likely this is something specific to your system, such as a recent regression in a video card driver.</p>
<ul>
<li>Do you have the same issue with the official Kitware-build Slicer packages, too?</li>
<li>Does disabling depth peeling make the problem go away?</li>
<li>Does it occur if you change <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables"><code>SLICER_OPENGL_PROFILE</code> environment variable</a> to <code>no</code>, <code>core</code>, or <code>compatibility</code>?</li>
<li>Does it occur with both wayland and x11?</li>
<li>Does ParaView have the same issue?</li>
</ul>

---
