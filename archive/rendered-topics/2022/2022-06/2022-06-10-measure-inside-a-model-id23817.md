# Measure Inside a Model

**Topic ID**: 23817
**Date**: 2022-06-10
**URL**: https://discourse.slicer.org/t/measure-inside-a-model/23817

---

## Post #1 by @dbgraf20 (2022-06-10 19:43 UTC)

<p>I am having some problems measuring inside my model. When I use the ruler, the tool I am trying to use locks onto the outside of the model. I need to measure the inside. How can I do this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7354c8d3df6ced94d34706ee313937d395407cb1.png" alt="OG view" data-base62-sha1="gsgyERLMx17jgPDjmhKIlPfrFJL" width="345" height="290"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/996b1209fd5bf53057562b2758b54e3294d73c70.png" alt="Broken View" data-base62-sha1="lTcrViZigk9WJFPmyzzg3qb1Tig" width="557" height="452"></p>

---

## Post #2 by @mau_igna_06 (2022-06-10 22:06 UTC)

<p>You can disable.model snapping in the models module. So when you move the ruler the position is controlled by the camera plane</p>

---

## Post #3 by @lassoan (2022-06-12 00:27 UTC)

<p>There could be many solutions. What would you like to measure on what kind of images?</p>
<p>For example, you could consider translating and rotating a slice view to find a relevant cross-section and then measure in that slice. Or, if you mean that you would like to be inside the model (similarly as using an endoscope) then you can move the camera inside the surface - for example, by placing a point using Markups module inside the surface, right-click on it and choose “Refocus camera on this point” and then get closer to that point (by using the mousewheel) until you find yourself inside the surface.</p>

---
