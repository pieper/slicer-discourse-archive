---
topic_id: 5178
title: "Place Fiducials"
date: 2018-12-23
url: https://discourse.slicer.org/t/5178
---

# Place fiducials

**Topic ID**: 5178
**Date**: 2018-12-23
**URL**: https://discourse.slicer.org/t/place-fiducials/5178

---

## Post #1 by @esurechao (2018-12-23 18:23 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.0</p>
<p>I have to place 40 fiducials in my model. (20 in the first stage, 20 in the second stage)</p>
<p>I placed 20 fiducials in the first stage, locked the fiducial positions, and saved.<br>
When I was placing 20 fiducials in the second stage, one or two fiducials placed in the first stage might move on its own.<br>
(I was sure that I locked these fiducials, but the coordinates still changed.)</p>
<p>Did anyone have similar experience? Did I miss something?<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2018-12-23 18:54 UTC)

<p>I don’t remember anyone experiencing this issue, but since updating to latest version of VTK, there are some problems with fiducial picking (see <a href="https://issues.slicer.org/view.php?id=4634" rel="nofollow noopener">bug report</a>).</p>
<p>We are reworking markups infrastructure completely to fix these bugs, improve performance, and add more widgets (curves, angles, etc.). We expect to have the new version integrated in about 1-2 months.</p>
<p>Until then you may try to experiment with this and if you can report exact steps that reproduce the issue then let us know and we might be able to deliver a quick fix or recommend workarounds.</p>

---

## Post #3 by @jamesobutler (2018-12-23 21:27 UTC)

<p>I have experience dealing with fiducials where hovering over them with the cursor will “nudge” them slightly to a new position. It was clearly visible in the slice window when this happened. Not sure if this is exactly what you mean by sometimes “might move on its own”. It was weird behavior that I never really understood and appeared more common after saving fiducials and then loading in again. I know this behavior existed in Slicer 4.8.1 though might still be present in the current code.</p>

---

## Post #4 by @MMMPPPMMM (2018-12-27 11:29 UTC)

<p>I have the same problem sometimes.<br>
I load a scene with two fiducial lists. All fiducials were/are locked.<br>
One fiducial is not on its previous position anymore.<br>
I delete the fiducial.<br>
One fidicual from the 2nd list moves to a wrong postion.</p>

---

## Post #5 by @lassoan (2018-12-27 14:09 UTC)

<p>Could you share the scene and provide exact step-by-step instructions to reproduce the issue?</p>

---

## Post #6 by @esurechao (2018-12-27 15:09 UTC)

<p>Thank you for your responses.</p>
<p>This phenomenon does not always occur. So far, I find this phenomenon seems to occur only when there are more than 40 or 50 fiducials.</p>
<p>In order to describe precisely the main steps and the phenomenon, I am also trying to simplify my procedures now.</p>

---

## Post #7 by @jamesobutler (2019-01-02 20:18 UTC)

<p>I created an issue with steps to reproduce and other details. It can be found as <a href="https://issues.slicer.org/view.php?id=4669" rel="noopener nofollow ugc">4669</a> in the Slicer mantis issue tracker.</p>
<p><strong>Original:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e460bcb5c1c971a0724058b3883d936b9f1b5c1.png" data-download-href="/uploads/short-url/22gKYdZvDT4xNB2HSXQywmEZ5At.png?dl=1" title="fiducial-position" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e460bcb5c1c971a0724058b3883d936b9f1b5c1.png" alt="fiducial-position" data-base62-sha1="22gKYdZvDT4xNB2HSXQywmEZ5At" width="513" height="500" data-dominant-color="EDF0F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fiducial-position</span><span class="informations">534×520 34 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Moved Positions after mouse hover:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff42067c2f2b6118ef2135b46ea8434867b95d1e.png" data-download-href="/uploads/short-url/Aq7df1I01gwP6SAFFQz8SzxCgEK.png?dl=1" title="fiducial-position-moved" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff42067c2f2b6118ef2135b46ea8434867b95d1e.png" alt="fiducial-position-moved" data-base62-sha1="Aq7df1I01gwP6SAFFQz8SzxCgEK" width="515" height="500" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fiducial-position-moved</span><span class="informations">534×518 33.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
