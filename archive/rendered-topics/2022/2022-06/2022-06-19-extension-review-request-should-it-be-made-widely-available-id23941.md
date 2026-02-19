---
topic_id: 23941
title: "Extension Review Request Should It Be Made Widely Available"
date: 2022-06-19
url: https://discourse.slicer.org/t/23941
---

# Extension review request : should it be made widely available?

**Topic ID**: 23941
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/extension-review-request-should-it-be-made-widely-available/23941

---

## Post #1 by @chir.set (2022-06-19 11:25 UTC)

<p>Hi,</p>
<p>I tinkered these <a href="https://github.com/chir-set/ExtraMarkups" rel="noopener nofollow ugc">custom markups</a> that draw primitive shapes, and intend to add a few more shapes.</p>
<p>Apart from <a href="https://discourse.slicer.org/t/draw-specific-dimension/22934">this</a> practical use, I don’t find any useful application yet, at least in the surgical field of my concern.</p>
<p>I’m wondering if core developers would find value in these and if yes, whether any should be made available to others.</p>
<p>They can of course be updated following your advice, slowly though.</p>
<p>Thank you for any input and regards.</p>

---

## Post #2 by @mau_igna_06 (2022-06-19 14:17 UTC)

<p>I like it.</p>
<p>You may combine your efforts with <a class="mention" href="/u/rbumm">@rbumm</a> about the labels</p>

---

## Post #3 by @lassoan (2022-06-19 14:43 UTC)

<p>Thank you for considering contributing this, I think it would be useful.</p>
<p>The only thing I’m not sure about if it is better to provide it in Markups module or Dynamic modeller module. If it is mainly for quantification (measuring diameters, areas, distances, etc.) then Markups make more sense; if it is for modelling (cutting out regions, building new shapes, etc.) then Dynamics modeller would be more appropriate. Maybe we could have both, but the redundancy could confuse users and increase maintenance workload.</p>
<p>I would also consider implementing a single “Basic shape” markup instead of having a 4 separate markup type. It would mean less code to maintain and would allow users to switch between different shapes.</p>

---

## Post #4 by @chir.set (2022-06-19 15:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Markups module or Dynamic modeller module. If it is mainly for quantification</p>
</blockquote>
</aside>
<p>Well it does not have any goal yet ! All this sprung from the <a href="https://discourse.slicer.org/t/draw-specific-dimension/22934">post</a> I mentioned above. I thought about inclusion in the SandBox extension, and honestly, don’t know how useful it can be.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would mean less code to maintain</p>
</blockquote>
</aside>
<p>Here, I find it much easier to maintain in separate objects. Once an object is being edited, reasoning is focused and constrained. A single markup managing multiple shapes implies a lot of conditionals and it’s easy to get lost in the mind this way. Moreover, reading the code becomes more complex, at least to me.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>You may combine your efforts with <a class="mention" href="/u/rbumm">@rbumm</a> about the labels</p>
</blockquote>
</aside>
<p>Please refer me to prior work about labels in this case. <a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #5 by @rbumm (2022-06-19 19:44 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Please refer me to prior work about labels in this case. <a class="mention" href="/u/rbumm">@rbumm</a></p>
</blockquote>
</aside>
<p>I am working on ENH: Add connector line for fiducial markup label texts (<a href="https://github.com/Slicer/Slicer/pull/6188#" class="inline-onebox">ENH: Add connector line for fiducial markup label texts by rbumm · Pull Request #6188 · Slicer/Slicer · GitHub</a>)</p>
<p>but the PR needs to be activated somehow (fell behind perhaps because of Slicer 5 release). I am ready to restart this any time but need input from the core developers <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #6 by @lassoan (2022-06-20 01:45 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I am ready to restart this any time but need input from the core developers <a class="mention" href="/u/lassoan">@lassoan</a></p>
</blockquote>
</aside>
<p>If you have any remaining questions then post them in the pull request. If you have time we can work on this as a project at the upcoming project week. Maybe we can finalize everything and get it integrated by the end of the week.</p>

---

## Post #7 by @lassoan (2022-06-20 02:33 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Here, I find it much easier to maintain in separate objects. Once an object is being edited, reasoning is focused and constrained. A single markup managing multiple shapes implies a lot of conditionals and it’s easy to get lost in the mind this way. Moreover, reading the code becomes more complex, at least to me.</p>
</blockquote>
</aside>
<p>Ring, disk, ellipse, sphere, and ellipsoid are all just special cases of a “hollow ellipsoid”. Ring and disk are special case of ellipsoid (size along the third axis = 0). Disk is a special case of ring (hole size is 0). Disk is a special case of ellipse (both axes have the same size). etc.</p>
<p>If we add one module for each markup then we end up with 5 * 25 = 125 files. This is a very large number. In contrast, if we add a single module then probably we only need to have separate classes for the VTK widget and representation, which would mean 19 + 5 * 6 = 49 files. Still a large number, but somewhat more manageable. It is also nice that you can switch between a sphere and ellipsoid without deleting and recreating a markup.</p>
<p>The manual label markup is indeed somewhat overlaps with <a class="mention" href="/u/rbumm">@rbumm</a>’s automatic label display work. I’m not sure if both are needed. Some kind of arrow markup could be useful, but maybe improving the line markup to allow oriented line ending would be sufficient.</p>
<p>There are a number of things to improve, but these markups might be already usable for some things, so it could make sense to make it available for users for experimenting.</p>

---

## Post #8 by @chir.set (2022-07-01 19:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but these markups might be already usable for some things, so it could make sense to make it available for users for experimenting.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>switch between a sphere and ellipsoid</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="23941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we end up with 5 * 25 = 125 files</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I merged the three primitives in one single <a href="https://github.com/chir-set/ExtraMarkups/tree/Shapes" rel="noopener nofollow ugc">Shape</a> markups. Please comment.</p>
<p>If you still think that wide availability is of interest, a Slicer related repository (Sandbox?) should be found. I still don’t wish to propose it as an extension, because in a few months, I won’t have my mind deep in it. Someone else may find useful work to do with it. It would then be easier for him to extend from a Slicer controlled repository.</p>
<p>Regards.</p>

---

## Post #9 by @chir.set (2022-09-02 13:37 UTC)

<p>Hi,</p>
<p>Sorry to request your attention one last time.</p>
<p>This <a href="https://github.com/chir-set/ExtraMarkups" rel="noopener nofollow ugc">project</a> has been much improved since its inception, with more shapes and a module. I still think it might be useful to others, that’s why it’s open source on github.</p>
<p>I suggest that core devs have a look when they find spare time(!), and say whether built binaries should be made available to Slicer users.</p>
<p>I know only 2 ways to that end :</p>
<ul>
<li>share the project as a Slicer extension (with some kind of bureaucracy, sorry)</li>
<li>integrate the project in an existing extension.</li>
</ul>
<p>Looking forward for your comments.</p>
<p>Regards.</p>

---
