# Merging volumes - what to do after landmark registration

**Topic ID**: 2580
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/merging-volumes-what-to-do-after-landmark-registration/2580

---

## Post #1 by @katharina_hecker (2018-04-13 09:24 UTC)

<p>I wanted to integrate one volume into another one (at a certain position: That is why I was using Landmark registration to align both volumes. It also worked as far as I know. But now I have the problem that When I want to segment the ‘transformed outcome volume’ I can´t see an integration of the first into the second… Am I using the wrong tool for integration at a certain position?<br>
Thanks for your help!</p>

---

## Post #2 by @lassoan (2018-04-13 13:11 UTC)

<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="2580">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>It also worked as far as I know</p>
</blockquote>
</aside>
<p>What did you see? Can you post a screenshot before and after registration? Have you applied the computed transform to the volume? (you can apply a transform using Transforms module; or in Data module’s Transform hierarchy tab, drag-and-drop volume under the transform)</p>
<p>You can find several registration tutorials that use Fiducial registration wizard module, among <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>

---
