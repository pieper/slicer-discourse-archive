---
topic_id: 39525
title: "Curve Will Not Confine To Model Surfaces"
date: 2024-10-03
url: https://discourse.slicer.org/t/39525
---

# Curve will not confine to model surfaces

**Topic ID**: 39525
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/curve-will-not-confine-to-model-surfaces/39525

---

## Post #1 by @Jones (2024-10-03 14:41 UTC)

<p>I am trying to take semilandmarks on 3D mandible models through taking several open curves on each mandible. For the first 20 models I sampled I didn’t have any problems, but now when I press ‘confine curve to model surface’ the curve instead floats in random places above the surface, in areas unconnected to the initial points of the curve. I have tried uninstalling and restarting the app, as well as uninstalling and updating the SlicerMorph package, but the problem hasn’t resolved. I have tried on many different models and the same problem occurs. This happens whether or not I resample the curve before constraining to surface. The ‘constrain to surface’ function has also become very slow, and sometimes placing the initial points of the curve is also now very slow. I have also tried messing with the ‘advanced’ curve settings, changing the maximum projection distance, and this hasn’t helped. This problem came out of nowhere, and I haven’t been able to fix it for a week- I was wondering what I could do to try and fix it?<br>
Thank you very much for your help.</p>

---

## Post #2 by @lassoan (2024-10-03 14:42 UTC)

<p>Could you please share an example scene that has this unexpected behavior (save the scene as .mrb, upload to dropbox/onedrive/etc., and post the link here)?</p>

---

## Post #3 by @zifangx (2024-12-14 13:26 UTC)

<p>Hi Jones,</p>
<p>I’m experiencing issues with the ‘constrain to model’ functionality. In my case, the open curve that’s constrained to a model causes crashes almost every time I try to adjust the position of a control point, add a control point, or do any sort of edit to the curve. I’ve also tried all the steps you took and have not found a fix…<br>
Please share your experiences if you have successfully resolved this issue.<br>
Thank you in advance.</p>

---

## Post #4 by @lassoan (2024-12-15 05:00 UTC)

<p><a class="mention" href="/u/zifangx">@zifangx</a> Could you please share an example scene that has this unexpected behavior (save the scene as .mrb, upload to dropbox/onedrive/etc., and post the link here)?</p>

---

## Post #5 by @zifangx (2024-12-15 16:06 UTC)

<p>Thank you; I think I have figured out the trigger. The unexpected behaiour (crashing upon hitting undo on an open curve) started after I added the Undo/Redo button following <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/" rel="noopener nofollow ugc">this</a> link, and later I tried the code snippet suggested by <a href="https://discourse.slicer.org/t/is-it-possible-to-add-a-global-undo-button/16859/8">this</a> post, which I suspect further broked the open curve function somehow, crashing every time I try to adjust a control point on the curve, even when I reverse back the first version of the Undo/Redo code snippet.<br>
I have since then removed all code snippets in ‘.slicerrc’, and no more unexpected crashing so far.</p>

---
