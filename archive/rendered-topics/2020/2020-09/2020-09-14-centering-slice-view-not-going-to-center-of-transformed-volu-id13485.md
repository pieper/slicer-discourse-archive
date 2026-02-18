# Centering slice view not going to center of transformed volume

**Topic ID**: 13485
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/centering-slice-view-not-going-to-center-of-transformed-volume/13485

---

## Post #1 by @jamesobutler (2020-09-14 22:40 UTC)

<p>I loaded a 2D sequence volume and created a transform to apply to the sequence setting spacing for X, Y, and Z dimensions.  Z was set to 0.2mm from a default of 1.0mm.  However, centering the axial red slice after applying the transform appears to still center to the position of the original bounds in Z which was a default 1.0mm.  However after dragging the axial red slider to the ends and back it then fixes itself in regards to having the center of the slider mean the center of the bounds.  Is there something else I can call to trigger this update? Or is there something else incorrect in this method of applying spacing?</p>
<p>After clicking center button for axial red slice:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64f8a7f0cc7f2f0e53e6dcc9c4f7ff711fd812cb.png" data-download-href="/uploads/short-url/epeunY7Dyr8dXnyVOaXIk2L8Sv1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f8a7f0cc7f2f0e53e6dcc9c4f7ff711fd812cb_2_426x500.png" alt="image" data-base62-sha1="epeunY7Dyr8dXnyVOaXIk2L8Sv1" width="426" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f8a7f0cc7f2f0e53e6dcc9c4f7ff711fd812cb_2_426x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64f8a7f0cc7f2f0e53e6dcc9c4f7ff711fd812cb_2_639x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64f8a7f0cc7f2f0e53e6dcc9c4f7ff711fd812cb.png 2x" data-dominant-color="0D0D0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">664×779 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After dragging the axial red slider to the ends and back:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/089522e7c3b2cdfa4a093b30d7d4deafd809cec2.png" data-download-href="/uploads/short-url/1dVlgaRpgSBXT5NSXkyTr7gLPxg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089522e7c3b2cdfa4a093b30d7d4deafd809cec2_2_431x500.png" alt="image" data-base62-sha1="1dVlgaRpgSBXT5NSXkyTr7gLPxg" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089522e7c3b2cdfa4a093b30d7d4deafd809cec2_2_431x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089522e7c3b2cdfa4a093b30d7d4deafd809cec2_2_646x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/089522e7c3b2cdfa4a093b30d7d4deafd809cec2.png 2x" data-dominant-color="3E3E3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">668×774 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-15 04:08 UTC)

<p>Can you share an example scene?</p>

---

## Post #3 by @jamesobutler (2020-09-15 12:36 UTC)

<p>Here is an <a href="https://sonovolinc-my.sharepoint.com/:u:/g/personal/jbutler_sonovol_com/ESKaVQLYHGNLnHnhb97DB_gBg_d2VMPLobpkIqM10SgL6Q?e=Lcn6kx" rel="noopener nofollow ugc">example scene</a>. When you turn on slice intersection and then click the center button for the red axial slice view, it is not centering to volume bounds.</p>

---

## Post #4 by @jamesobutler (2020-09-15 23:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> have you had a chance to take a look at the scene provided?</p>

---

## Post #5 by @lassoan (2020-09-16 11:35 UTC)

<p>I was able to reproduce the problem and I’m working on it.</p>

---

## Post #6 by @lassoan (2020-09-16 18:52 UTC)

<p>I’ve <a href="https://github.com/Slicer/Slicer/commits/master">fixed the issue</a>, tomorrow’s Preview Release should work well.</p>

---

## Post #7 by @jamesobutler (2020-09-17 13:13 UTC)

<p>Thanks! I tried my scene again and the fix appears to work well.</p>

---
