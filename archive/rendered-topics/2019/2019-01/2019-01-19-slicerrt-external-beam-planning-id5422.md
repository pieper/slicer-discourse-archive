# SlicerRT external beam planning

**Topic ID**: 5422
**Date**: 2019-01-19
**URL**: https://discourse.slicer.org/t/slicerrt-external-beam-planning/5422

---

## Post #1 by @PaoloZaffino (2019-01-19 15:21 UTC)

<p>Hi all,<br>
I have some questions about external beam planning (that is great!).</p>
<p>Is it just for protons? I didn’t see the photon option.</p>
<p>After setting the isocenter in the center of a structure, is it possible to manually change the beam angle along each direction?</p>
<p>Thanks a lot!</p>
<p>Best.<br>
Paolo</p>

---

## Post #2 by @cpinter (2019-01-20 01:57 UTC)

<p>Thanks Paolo!</p>
<p>There is no photon option unfortunately. We had plans to integrate Matrad engines via Matlab-enabled EBP plugins but that development stalled.</p>
<p>If you click Edit next to beam then you can edit them. I’m supposed to be offline for a few weeks so I’ll ask <a class="mention" href="/u/gcsharp">@gcsharp</a> to answer the follow-up questions.</p>
<p>Please let us know all the comments you have, I’ll catch up with you a bit later!</p>

---

## Post #3 by @PaoloZaffino (2019-01-21 10:20 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> !<br>
Perfect, proton plan is good for my application <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I remember that in the previous releases it was possible to change the beam angle, but now I don’t find this option. It can just rotate the beam, but not tilt it.</p>
<p>I’m running Slicer 4.10.0 r27501 on a Linux box.</p>
<p>Thanks again!<br>
Paolo</p>

---

## Post #4 by @gcsharp (2019-01-23 17:16 UTC)

<p>Hi Paolo,   What do you mean rotate the beam?  Gantry? Collimator? Couch?</p>

---

## Post #5 by @PaoloZaffino (2019-01-24 11:53 UTC)

<p>I would be interested in tilting the beam (I know it is a little bit strange).<br>
Actually, right now, I discovered that a transformation can be applied to beams as well, so basically I found a solution.<br>
Thanks a lot <a class="mention" href="/u/gcsharp">@gcsharp</a> and <a class="mention" href="/u/cpinter">@cpinter</a>!</p>
<p>Paolo</p>

---

## Post #6 by @cpinter (2019-02-07 14:57 UTC)

<p>If you add a custom transform to the beams, then they probably won’t be properly taken into account when you calculate the dose.</p>
<p>There are controls to change beam angles and geometry in the Beams module. In EBP module you can click on Edit for the beam you want to modify, and it takes you to Beams with that beam selected. There will be a Geometry tab, where you can change these parameters.</p>
<p>See the third screenshot (under the first two which are in one row) in this page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ExternalBeamPlanning" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/ExternalBeamPlanning</a></p>

---

## Post #7 by @PaoloZaffino (2019-02-20 21:42 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>!</p>
<p>Paolo</p>

---
