---
topic_id: 43285
title: "Red Boundary Border Around Frame In Version 5 8 1"
date: 2025-06-10
url: https://discourse.slicer.org/t/43285
---

# Red Boundary/Border Around Frame in Version 5.8.1

**Topic ID**: 43285
**Date**: 2025-06-10
**URL**: https://discourse.slicer.org/t/red-boundary-border-around-frame-in-version-5-8-1/43285

---

## Post #1 by @rcpr (2025-06-10 14:09 UTC)

<p>I’m using Slicer to acquire and record sequences in real-time via the PLUS server. I’ve recently started using version 5.8.1, and I’ve noticed a red boundary appearing around the acquired sequence.</p>
<p>My issue is that even after I click on “Close Scene” to close the current acquisition and open a new one, this red boundary persists, even though there’s nothing actually inside it</p>
<p>Am I missing something here?</p>
<p>Thank you in advance for your help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b540b56b53e0e045d1c38f3e8ad9956978b36e46.png" data-download-href="/uploads/short-url/pRr3I0nqAdmO0Oz0S5wkqptEWLc.png?dl=1" title="Captura de ecrã 2025-06-10 150535" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b540b56b53e0e045d1c38f3e8ad9956978b36e46_2_537x500.png" alt="Captura de ecrã 2025-06-10 150535" data-base62-sha1="pRr3I0nqAdmO0Oz0S5wkqptEWLc" width="537" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b540b56b53e0e045d1c38f3e8ad9956978b36e46_2_537x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b540b56b53e0e045d1c38f3e8ad9956978b36e46.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b540b56b53e0e045d1c38f3e8ad9956978b36e46.png 2x" data-dominant-color="A2A2D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de ecrã 2025-06-10 150535</span><span class="informations">601×559 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Deep_Learning (2025-06-15 13:28 UTC)

<p>I had this problem a few weeks ago for the first time, when making figures for publication.<br>
Can’t remember how I solved it, but try clicking off show slicer edges.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad407d3ae83daae5826b9ff91ea4fe1787239990.png" data-download-href="/uploads/short-url/oIELJbnKGKfnlNOWznBG48HVdio.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad407d3ae83daae5826b9ff91ea4fe1787239990.png" alt="image" data-base62-sha1="oIELJbnKGKfnlNOWznBG48HVdio" width="690" height="426" data-dominant-color="C3CBC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">896×554 23.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rcpr (2025-06-24 11:22 UTC)

<p>Hi!<br>
First of all, thank you so much for your answer. Unfortunately, I already tried that, but the red boundaries didn’t disappear. By any chance, do you remember anything else you might have done? Thanks again!</p>

---

## Post #4 by @Deep_Learning (2025-06-24 14:42 UTC)

<p>I know your frustration. Trust me…<br>
This box is either new to 5.8 or newly on by default in 5.8.<br>
I had never seen it before.<br>
I removed it using “Show Slice Edges”</p>
<p>I also from time to time have some “leftovers” in the 3d view after a “clear or close all”.</p>
<p>That’s your issue right?</p>
<p>…always worrying that they are going to affect the next case, but I do not think that they are really there.<br>
That’s why you can’t get rid of them.  Sounds crazy and I’m guessing a bit.</p>

---

## Post #5 by @rcpr (2025-06-24 15:29 UTC)

<p>It’s good to know I’m not the only one going crazy with this boundary! I can already remove it from the 3D volumes, but I still see it when playing back the 2D sequence I acquired and even after closing the scene, the boundaries are still there. Really annoying. But yeah, thanks again for taking the time to help!</p>

---

## Post #6 by @Deep_Learning (2025-06-26 14:25 UTC)

<p>I’m a big fan of slicer and use it daily.</p>
<p>Often I have/find a problem and am surprised that no one else has posted in the fourm…</p>
<p>In this situation, I just type restart() to get a complete Clear All.</p>

---
