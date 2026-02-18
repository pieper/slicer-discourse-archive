# Markups : new point ID restart from 1 when loaded from saved scene

**Topic ID**: 21142
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/markups-new-point-id-restart-from-1-when-loaded-from-saved-scene/21142

---

## Post #1 by @chir.set (2021-12-20 13:14 UTC)

<p>I’ve noticed an ID numbering problem with curve and fiducial markups. I have not tested all markups objects. Using home built Slicer on Linux. Found with factory build 4.13.0-2021-11-01 r30345 / 08aeb16 also.</p>
<ul>
<li>Start Slicer</li>
<li>Load any volume (unused)</li>
<li>Place 2 fiducial points</li>
<li>Save the scene</li>
<li>Restart Slicer</li>
<li>Load the scene</li>
</ul>
<p>First, we see that the Fiducial node is selected in the markups toolbar, but ‘Place new point button’ is greyed. To activate it we need to create a new markups. So,</p>
<ul>
<li>Create a markups open curve</li>
<li>Place 3 points</li>
<li>Stop point placement</li>
<li>Save the scene</li>
</ul>
<p>Next,</p>
<ul>
<li>Select the existing fiducial node ‘F’</li>
<li>Place a new point</li>
<li>Stop point placement</li>
<li>Save the scene</li>
</ul>
<p>We see that the third fiducial point is labeled ‘F-1’.</p>
<ul>
<li>Close Slicer</li>
<li>Open F.mrk.json with a text editor</li>
</ul>
<p>The first point has ID == 1, the second has ID == 2 and the third has ID == 1.<br>
We have the same result with GetNthControlPointID().</p>
<ul>
<li>Start Slicer again</li>
<li>Load the scene</li>
<li>Activate point placement, by selecting Fiducial ‘F’</li>
<li>Select curve ‘OC’</li>
<li>Place a fourth point</li>
<li>Stop point placement</li>
<li>Save the scene</li>
<li>Close Slicer</li>
</ul>
<p>If we inspect ‘OC.mrk.json’, we see that the fourth point ID == 1, just like with fiducials.</p>
<p>I hope someone else could confirm it, after which, core devs could have a look.</p>
<p>Regards.</p>

---

## Post #2 by @jamesobutler (2021-12-20 13:18 UTC)

<p>Could you confirm with the latest Slicer preview build? Your factory build is a month and a half old which is quite behind latest development and fixes.</p>

---

## Post #3 by @chir.set (2021-12-20 13:31 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="21142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Using home built Slicer on Linux. Found with factory build 4.13.0-2021-11-01 r30345 / 08aeb16 also.</p>
</blockquote>
</aside>
<p>I confirm, found with :</p>
<ul>
<li>Home built : after ‘git pull’ today</li>
<li>Factory build : 4.13.0-2021-11-01 r30345 / 08aeb16</li>
<li>Factory build : 4.13.0-2021-12-19 r30507 / f779d8e</li>
</ul>

---

## Post #4 by @lassoan (2021-12-22 04:23 UTC)

<p>The last used control point number (that is used for generating the control point names) are not stored persistently, therefore the numbering starts from 0 every time the markup is loaded from disk. I’ve <a href="https://github.com/Slicer/Slicer/commit/b76bcebcaf6bc8705fdb8403655bb2b806de96aa">updated the storage node</a> to save and restore this value.</p>

---
