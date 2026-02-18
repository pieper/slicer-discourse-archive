# Update to Endoscopy flythrough

**Topic ID**: 33055
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/update-to-endoscopy-flythrough/33055

---

## Post #1 by @Lee_Newberg (2023-11-27 13:18 UTC)

<p>We have updated the Endoscopy module – the oldest Python ScriptedModule for 3D Slicer – for functionality, interface, and underneath. You can fly through your path while you watch your progress in the adjacent pane.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>First-person view</th>
<th>Third-person view</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9250d81c867e11aaf637242620f88aa26e97de11.png" alt="First-person view" data-base62-sha1="kSmUWV3whFpC27zz34S5azYJzTX" width="490" height="370"></td>
<td><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d3bf742c004e1546c631665f174b0dc789a2c84.png" alt="Third-person view" data-base62-sha1="hRS9Vk0gBN9iQgI7LY6syKesYjW" width="488" height="369"></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div><p>Now, camera orientations through a flythrough are modifiable, so you can pitch, roll, and yaw the camera to how you want it instead of being stuck with the previous default behavior. At any points in the flythrough, you adjust the camera in the 3d-viewing pane as desired and then hit the “Save keyframe orientation” button in the Flythrough section of the interface; see below. Camera orientations for all remaining frames will automatically be interpolated between the supplied orientations using quaternion slerp to give smooth transitions. Navigation buttons (First, Back, Next, and Last) allow you to quickly find your supplied orientations whenever you want to check, modify, or delete them. The set of supplied camera orientations will be saved to disk with the input curve and can be read and edited at a later time.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Old interface</th>
<th>New Interface</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec671a6c84627dd3efa4235a97cc4bbb87e52dd5.png" alt="Old interface" data-base62-sha1="xJjA01Ks55iDkRs7ipfQhCwyDbv" width="436" height="302"></td>
<td><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7564f5607a14b1917c0947b7d3a1d13de243cc12.png" alt="New interface" data-base62-sha1="gKwakyBtMxokPm0Agvpi0JbZtHc" width="442" height="406"></td>
</tr>
</tbody>
</table>
</div><p>We show a typical example in the video below. We segment an airway, create a path through it, and fly through it. There’s a point where the flythrough isn’t looking where we want, so we first choose good frames before and after that point with the “Save Keyframe Orientation” button. Then we go to the peak frame of the excursion to correct it, and save that with a press of the button. 3D Slicer automatically interpolates the orientations between the supplied keyframes.</p>
<p>Additionally, the interface for the functionality for creating a model to export has been moved to an Advanced section rather than doing it every time a curve is selected for a flythrough.</p>
<p>Behind the scenes, flythroughs now take advantage of the more advanced features of 3D Slicer’s <code>vtkMRMLMarkupsCurveNode</code> and <code>vtkMRMLMarkupsClosedCurveNode</code>, rather than only on the simpler <code>vtkMRMLMarkupsFiducialNode</code>. Furthermore, the 3D Slicer scripted Endoscopy module is upgraded to support multiple display nodes per widget and to replace homegrown mathematical implementations with those from 3D Slicer, VTK, and the Python numpy package.</p>
<p>These changes are now available in the preview build of 3D Slicer.</p>
<p><a href="https://github.com/Slicer/Slicer/issues/6502" rel="noopener nofollow ugc">Issue</a><br>
<a href="https://github.com/Slicer/Slicer/pull/7165" rel="noopener nofollow ugc">Pull Request</a><br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/348998d7ac0e57c926eb04f0ad8c2fd23d18b25a.mp4">
  </div><p></p>

---

## Post #2 by @hherhold (2023-11-27 13:24 UTC)

<p>This looks awesome, I’m super excited to try it out!</p>

---

## Post #3 by @muratmaga (2023-11-27 17:28 UTC)

<aside class="quote no-group" data-username="Lee_Newberg" data-post="1" data-topic="33055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lee_newberg/48/7615_2.png" class="avatar"> Lee_Newberg:</div>
<blockquote>
<p>These changes are now available in the preview build of 3D Slicer.</p>
</blockquote>
</aside>
<p>Just to clarify, we need v5.7 to use the updated module?</p>

---

## Post #4 by @Lee_Newberg (2023-11-27 18:02 UTC)

<p>The new Endoscopy module should be available in this morning’s preview build of 3D Slicer.  It is also slated to be available in 5.6.</p>

---

## Post #5 by @hherhold (2023-11-27 18:06 UTC)

<p>I just downloaded the 5.7 preview and the updated module is in there.</p>

---
