# Question about calibration

**Topic ID**: 23035
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/question-about-calibration/23035

---

## Post #1 by @user5 (2022-04-20 04:52 UTC)

<p>Hello everyone.</p>
<p>I am trying yo use ArUco Marker to be the tracker to perform a <a href="https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!29379&amp;ithint=file%2cpptx&amp;authkey=!AL2fpr9tHQTEWNA" rel="noopener nofollow ugc">Brain surgery navigation</a> test. I have followed every step in tutorial , the needle still go to wrong location. I already retry it for many times, the result still is similar.</p>
<p>I think that the problem is the reference point cannot move correctly, I have no idea why my reference point cannot move like tutorial.</p>
<p>I have recorded my setup process. Do someone having idea of why my failure output came out? Do I have performed any wrong process to occur this problem?<br>
Thanks you.<br>
This is the link of <a href="https://mycuhk-my.sharepoint.com/:v:/g/personal/1155129202_link_cuhk_edu_hk/EbXA4vySf8NHnBaQWGSOIVABb3vfupbBZE078MKe_OSWBg?e=0yYXoa" rel="noopener nofollow ugc">setup process video</a></p>

---

## Post #2 by @lassoan (2022-04-20 16:17 UTC)

<p>The mistake was made at 12:43. You have set the <code>registration result</code> transform to <code>StylusTipToStylus</code>. Since auto-update was on, it immediately overwrote your stylus calibration result and everything else that you did after that was corrupted. You need to restart from scratch, calibrate the stylus again and repeat all the steps afterwards.</p>
<p>The aruco marker is not properly attached to the stick. It moves a lot. You must attach it rigidly (e.g., with lots of hot glue).</p>
<p>Spin calibration failed. Probably the angle range of spinning was too large. You can try to spin only +/-20 degree or less. Of course, Aruco tracking is very inaccurate in measuring any out-of plane rotation, so it may be hard to get a usable spin calibration.</p>
<p>You need more than 3 points for fiducial registration. 3 is the absolute minimum, but it does not give you any chance to reduce effect of random errors. I would recommend using at least 6 points.</p>

---
