---
topic_id: 4755
title: "Landmark Registration Module"
date: 2018-11-14
url: https://discourse.slicer.org/t/4755
---

# Landmark Registration Module

**Topic ID**: 4755
**Date**: 2018-11-14
**URL**: https://discourse.slicer.org/t/landmark-registration-module/4755

---

## Post #1 by @adelmo (2018-11-14 09:47 UTC)

<p>Good morning developers,</p>
<p>First of all, I wanted to thank you for all the great work you are doing on 3D Slicer and the support you provide.</p>
<p>I recently tried to move all of my team works from Slicer 4.8 to the new stable 4.10. I can see the huge improvements, especially from a development point of view, but unluckily there is a bug that is a dealbreaker for me.</p>
<p>As reported <a href="https://discourse.slicer.org/t/hangout-2018-10-16/4414">here</a> and <a href="https://issues.slicer.org/view.php?id=4634" rel="nofollow noopener">here</a>, neither in the stable and in the nightly version the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/LandmarkRegistration" rel="nofollow noopener">Landmark Registration </a> module works. In particular, it is pretty much impossible to drag the inserted landmarks on the images.</p>
<p>As some of our pipelines involve an extensive use of that module I am stuck on using the ancient 4.8  version until it is fixed.</p>
<p>I understand the problem is a compatibility issue between VTK and Qt and I don’t know if the fix is in your control or in the hand of the VTK team. But since it has been a month since the last communication I wanted to ask:</p>
<p>Do you have any plan for a fix?<br>
Could you estimate how long we will have to wait for it?<br>
Do you any workaround to make it usable?</p>
<p>Thank You,<br>
AD</p>

---

## Post #2 by @jcfr (2018-11-14 14:13 UTC)

<blockquote>
<p>I wanted to thank you for all the great work you are doing on 3D Slicer and the support you provide.</p>
</blockquote>
<p>Thanks for the kind words <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>pretty much impossible to drag the inserted landmarks on the images<br>
[…] compatibility issue between VTK and Qt<br>
[…]  don’t know if the fix is in your control<br>
Do you have any plan for a fix?</p>
</blockquote>
<p>I confirm we want to fix it.</p>
<blockquote>
<p>Could you estimate how long we will have to wait for it?</p>
</blockquote>
<p>Conservatively, I would say January</p>
<blockquote>
<p>Do you any workaround to make it usable?</p>
</blockquote>
<p>Beside of using Slicer 4.8.1, not yet.</p>

---
