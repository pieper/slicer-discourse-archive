---
topic_id: 19457
title: "Extension Manager Doen Not Show Any Extension"
date: 2021-09-01
url: https://discourse.slicer.org/t/19457
---

# Extension Manager doen not show any extension

**Topic ID**: 19457
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/extension-manager-doen-not-show-any-extension/19457

---

## Post #1 by @ylcnkzy (2021-09-01 10:55 UTC)

<p>It seems like there is a problem with the extension manager. There is no extension seen at the extension manager. I thought it might be specific to me, but then I realized that there is an update on the software. For the one who has such issue and benefits from the link below (<a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256?layout=empty&amp;os=win&amp;arch=amd64&amp;revision=29738">how to install extensions manually</a>);</p>
<p>Best,</p>

---

## Post #2 by @John_Agapito (2021-09-01 13:50 UTC)

<p>I am having the same problem - and even when I try to install the extension (SlicerRT) manually, it installs but then does not activate in the menus…running version 4.11.20210226.</p>

---

## Post #3 by @ylcnkzy (2021-09-01 14:05 UTC)

<p>Hi John,<br>
After you install the extension (such as SlicerRT), you need to restart the 3D slicer. In general, it asks you to restart the software with an notification (located right bottom of the extension manager).</p>
<p>Best,</p>

---

## Post #4 by @John_Agapito (2021-09-01 14:18 UTC)

<p>Yes, I know that is what is supposed to happen, but it does not: the restart button stays greyed-out. The error log shows: Uncaught ReferenceError: midas is not defined</p>
<p>Even if I restart the application anyway, the situation persists: SlicerRT appears in the “manage extensions” tab, but does not function - does not appear in the menus…</p>

---

## Post #5 by @mikebind (2021-09-01 22:07 UTC)

<p>This is due to a temporary issue related to the extension manager server being upgraded.  The workaround process is described here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19256">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256">Downloading extensions for older releases</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Due to the recent transition to the updated Extension Manager and Data Store infrastructure, when using Slicer-4.11 (or older) version, users will need to manually download and install extensions from the new extension server, and download data sets from an alternative server instead of using the Data Store module. Rationale for the transition can be found <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444">here</a>.  We anticipate that this will be a temporary measure will the transition is finalized. 
Thank you for your patience!  Please do not hes…
  </blockquote>
</aside>


---

## Post #6 by @lassoan (2021-09-03 01:26 UTC)

<p>The simplest solution is to use the Slicer Preview Release. The Extensions manager has no issues in this version and it should generally work better than the latest Slicer Stable Release.</p>

---
