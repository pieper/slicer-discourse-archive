---
topic_id: 36191
title: "New Version Of The Prism Extension Dont Want To Update On 3D"
date: 2024-05-16
url: https://discourse.slicer.org/t/36191
---

# New version of the PRISM Extension don't want to update on 3D Slicer

**Topic ID**: 36191
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/new-version-of-the-prism-extension-dont-want-to-update-on-3d-slicer/36191

---

## Post #1 by @Kiroky (2024-05-16 05:24 UTC)

<p>Hello !<br>
I’ve found a problem with the PRISM Module from 3D slicer that i’ve fixed and merged with the master branch on Git. 1 day after it’s supposed to be online if I understood well.<br>
My problem is, on the mac and linux version of PRISM you can download the last version of the extension but on windows we have a version old of 3 commits.<br>
My question is, what problem could exist to block the new version on windows?</p>
<p>Thanks a lot in advance and have a good day.</p>

---

## Post #2 by @Kiroky (2024-06-12 17:56 UTC)

<p>up, the problem is still there, if someone could guide me on why it happen<br>
Thanks in advance.</p>

---

## Post #3 by @jamesobutler (2024-06-12 18:21 UTC)

<p>It appears the latest version of the PRISM extension is built on Windows with the latest Slicer Preview.</p>
<p>For the current Slicer Stable (5.6.2), extensions for the Windows platform haven’t been updated due to an issue with the factory build machine. See the following post about the situation (cc <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> ):</p>
<aside class="quote" data-post="14" data-topic="35688">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/windows-dashboard-extension-builds-interrupted-due-to-hardware-issue/35688/14">Windows dashboard: Extension builds interrupted due to hardware issue</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Kitware (<a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, <a class="mention" href="/u/jcfr">@jcfr</a>) will have to follow up here since it is their Windows machine building things. 
The corresponding open issue about rebuilding Slicer stable on bluestreak and building the Windows based extensions:
  </blockquote>
</aside>


---
