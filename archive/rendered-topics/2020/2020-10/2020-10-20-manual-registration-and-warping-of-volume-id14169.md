# Manual registration and warping of volume

**Topic ID**: 14169
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/manual-registration-and-warping-of-volume/14169

---

## Post #1 by @opetne (2020-10-20 19:44 UTC)

<p>Sorry if it has been mentioned before. I’m using Slicer for mainly anatomical 3D modeling. I do many CT and MR scans about the same specimen in the same position. I’d like to make manual “registration” of the volumes. DUring this I simply would like to rotate or “pull-push” one volume to the other. Is there a chance to make an improvement that I could easily pick an anatomicaly easily recognisable structure (point) what I’d like to have as the centre of my rotation? It happens many time that manual transform is not possible since the centre of the 2 volumes are not the same and it is impossible to move the to volumes to the same position.</p>

---

## Post #2 by @muratmaga (2020-10-20 21:17 UTC)

<p>Did you try the Fiducial Registration Wizard in the SlicerIGT extension? You need to specify points in one volume (minimum of four) and then the same set on the volume you try to align (your target). Then it will create a rigid or a warping transform of the target to the source.</p>
<p>Here is a tutorial <a href="https://onedrive.live.com/redir?resid=7230D4DEC6058018!24624&amp;authkey=!AJlO_xg84-IhsVo&amp;ithint=file%2cpptx" rel="noopener nofollow ugc">https://onedrive.live.com/redir?resid=7230D4DEC6058018!24624&amp;authkey=!AJlO_xg84-IhsVo&amp;ithint=file%2Cpptx</a> from Perklab.</p>

---

## Post #3 by @opetne (2020-11-12 09:39 UTC)

<p>Dear Murat,</p>
<p>Thank you for the tutorial, I tried this already but there are some situation where the manual movement could work easier. There would be a nice option where I could simply create a point on an anatomical sturcture and set this point as the centre of rotation or any kind of translation.</p>
<p>Ors</p>

---
