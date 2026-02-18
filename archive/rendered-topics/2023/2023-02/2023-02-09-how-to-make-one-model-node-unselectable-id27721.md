# How to make one model node unselectable

**Topic ID**: 27721
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/how-to-make-one-model-node-unselectable/27721

---

## Post #1 by @jay1987 (2023-02-09 13:37 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f766c0b870a1cddbc338e8735fec1aa52859c386.png" alt="image" data-base62-sha1="ziC55yq2ImQ84lAz3iAk7z6B3ka" width="217" height="229"><br>
when i move the fiducial point, i want to move the point on the suface of the head ,but when close to the tube,the point attach to the tube , is it possible to make the tube unselectable use code?<br>
i understand move the camera can solve these,this scene is a example , i need help to solve these problem use code to make the tube unattachable</p>

---

## Post #2 by @cpinter (2023-02-09 16:23 UTC)

<p>You almost answered it yourself, as I think what you need to do is<br>
<code>tubeModelNode.SetSelectable(False)</code><br>
to make the tube actor not be picked.</p>

---

## Post #3 by @jay1987 (2023-02-10 01:09 UTC)

<p>thank you pinter<br>
i have written tubeModelNode.SetSelectable(False)<br>
but the when i place the fiducial point in 3D view,the fiducial point still attach the surface of tubeModelNode</p>

---

## Post #4 by @cpinter (2023-02-10 09:53 UTC)

<p>I just tried this in Slicer 5.2.1 and if I call <code>SetSelectable(False)</code> on a model node it is not picked by fiducial placement.</p>

---

## Post #5 by @jay1987 (2023-02-10 10:38 UTC)

<p>i think i need to check my code , than you very much</p>

---
