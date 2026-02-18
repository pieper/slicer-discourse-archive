# vmtkcenterlinesections doesn't work sometime

**Topic ID**: 18729
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/vmtkcenterlinesections-doesnt-work-sometime/18729

---

## Post #1 by @Dongwei (2021-07-14 12:48 UTC)

<p>Hi,</p>
<p>I am using vmtkcenterlinesections to calculate the cross-sectional area of my vessel. But sometimes the function brokes for certain vessel geometry… It says ‘executing vmtkcenterlinesections’, then directly exit without returning anything. I increase vmtkcenterlineresampling parameter from 1 to, for example, to 3. Then it works. However, this may cause to miss the minimum cross-sectional area due to the too sparse sampling on the centerline. Does anyone has any idea to solve the situation? Like, could it be the roughness of the surface that broke the function? (Cause mine vessel wall is pretty bumpy)<br>
Thank you!</p>

---

## Post #2 by @lassoan (2021-09-03 01:45 UTC)

<aside class="quote no-group" data-username="Dongwei" data-post="1" data-topic="18729">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dongwei/48/11616_2.png" class="avatar"> Dongwei:</div>
<blockquote>
<p>Like, could it be the roughness of the surface that broke the function?</p>
</blockquote>
</aside>
<p>Absolutely. If the vessel polydata quality is bad then anything can happen. All computational geometry algorithms are inherently unstable, so if you provide bad input then anything can happen.</p>
<p>Could you share (upload somewhere and post the link) your problematic mesh files? Or at least post a few screenshots?</p>

---

## Post #3 by @junqiangchen (2021-10-21 07:52 UTC)

<p>i have same the problem,maybe there should modify the centerlinesections source code,and add abnormal process code in order to the program exit directly.</p>

---

## Post #4 by @lassoan (2021-10-22 05:56 UTC)

<p>Please provide an example file and information about your environment (Slicer version, operating system).</p>

---
