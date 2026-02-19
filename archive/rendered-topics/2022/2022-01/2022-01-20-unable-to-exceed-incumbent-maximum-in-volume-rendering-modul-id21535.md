---
topic_id: 21535
title: "Unable To Exceed Incumbent Maximum In Volume Rendering Modul"
date: 2022-01-20
url: https://discourse.slicer.org/t/21535
---

# Unable to exceed incumbent 'maximum' in Volume Rendering module by text entry

**Topic ID**: 21535
**Date**: 2022-01-20
**URL**: https://discourse.slicer.org/t/unable-to-exceed-incumbent-maximum-in-volume-rendering-module-by-text-entry/21535

---

## Post #1 by @DIV (2022-01-20 00:46 UTC)

<p>In the <strong>Volume Rendering</strong> module under <em>Advanced</em> there are settings for <code>Scalar Opacity Mapping</code> and <code>Scalar Color Mapping</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc33b2543d127cdf58871020097d0fd956d01c4.png" data-download-href="/uploads/short-url/vDNNH6Sxc2EjcFdpXG0IXeitn92.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc33b2543d127cdf58871020097d0fd956d01c4.png" alt="image" data-base62-sha1="vDNNH6Sxc2EjcFdpXG0IXeitn92" width="491" height="500" data-dominant-color="EDD8C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">504×513 33.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If the largest preset <code>X</code> value in the series of points in either set is smaller than the maximum image intensity, and if the user would like to therefore increase the value of <code>X</code> by typing it in, the current GUI prevents it.<br>
I find that inconvenient &amp; unintuitive, and am not sure what benefit (if any) accrues from this constraint on the entry field.</p>
<p>There are some workarounds…</p>
<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="21332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"><a href="https://discourse.slicer.org/t/trouble-with-thresholding/21332/5">Trouble with thresholding</a></div>
<blockquote>
<p>There is a kind of limitation in 3D Slicer that will prevent a user from entering an intensity value in the opacity or colour mapping that’s above some nominal ‘maximum’ by directly typing it in. (Some people might call this a bug.) The workarounds are to either drag the rightmost grey circular knob to the far right, or to manually edit the <code>VP</code> file. It’s not very convenient.</p>
</blockquote>
</aside>
<p>…but if there’s no big advantage to retaining the constraint, it would be good to remove it.</p>
<p>Alternatively, perhaps a softer constraint could be imposed:  <em>e.g.</em> prevent the user from entering a value higher than the <em>actual</em> maximum image intensity (or perhaps double it, say), rather than just whatever the old/existing volume rendering setting happened to be.</p>
<p>—DIV</p>
<p>P.S.  In the first workaround, after dragging the respective grey <em>circular</em> knob to the right, if the mouse reaches the edge of the the user’s screen, then the <em>rectangular</em> grey knob of the scrollbar may also need to be dragged to the right in order to access even higher values.  These are annotated in the screenshot above.</p>

---

## Post #2 by @DIV (2022-01-20 03:34 UTC)

<p>The text entry field for <code>X</code> in the “Gradient Opacity” control doesn’t seem to allow text entry at all.</p>

---

## Post #3 by @pieper (2022-01-21 18:39 UTC)

<p>The Volume Rendering widgets have a lot of usability challenges and could really stand a refresh.  There are many new features we could expose too.  It would be great if someone wants to take this work.</p>

---
