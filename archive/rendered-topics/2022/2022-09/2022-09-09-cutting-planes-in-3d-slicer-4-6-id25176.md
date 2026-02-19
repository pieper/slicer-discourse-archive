---
topic_id: 25176
title: "Cutting Planes In 3D Slicer 4 6"
date: 2022-09-09
url: https://discourse.slicer.org/t/25176
---

# Cutting planes in 3D Slicer 4.6

**Topic ID**: 25176
**Date**: 2022-09-09
**URL**: https://discourse.slicer.org/t/cutting-planes-in-3d-slicer-4-6/25176

---

## Post #1 by @Mohammad (2022-09-09 12:54 UTC)

<p>Operating system: 10<br>
Slicer version: 4.6</p>
<p>Dear All,<br>
Currently, I’ve used a version of 4.6 3D Slicer because of a module that only runs in this version. According to this paper (<a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Schumacher2015-manuscript.pdf" rel="noopener nofollow ugc">http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Schumacher2015-manuscript.pdf</a>) I have to specify some cutting planes. Can you please help me with how to do that?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0183964396f85d6bd017b15f6f3c60706828d6f.png" alt="image" data-base62-sha1="rplzC0EsPPBmuS1JaSzg2GL1l83" width="147" height="166"></p>
<p>Thanks.</p>

---

## Post #2 by @cpinter (2022-09-12 08:16 UTC)

<p>Hi Mohammad,</p>
<p>Unfortunately, due to the community-based nature of the platform, we do not have the resources to support past versions, but it would be great to make useful components compatible with the latest version. Could you please try the module in Slicer 5.0.3 and start to get past the errors? Most of them will probably be trivial, and with the rest we are happy to help you. This would be a great contribution!</p>

---

## Post #3 by @jamesobutler (2022-09-12 14:19 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Would you be able to provide usage help for the module? Or only development help for updating the module to work with Slicer 5.0.3?</p>
<aside class="quote" data-post="3" data-topic="25004">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e274bd/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-extension-installation/25004/3">Slicer extension installation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Dear lassoan 
Right now I installed the 3D slicer 4.5. I could install the mentioned extension ( brachytherapy module) but I don’t have any idea how to use this. Have you tried to install and use this module? 
Best regards
  </blockquote>
</aside>

<p>There was some previous request for help on how to install and run the module, but there was not a response at <a href="https://github.com/PerkLab/SlicerSkinMouldGenerator/issues/1" class="inline-onebox" rel="noopener nofollow ugc">How to run · Issue #1 · PerkLab/SlicerSkinMouldGenerator · GitHub</a>.</p>

---

## Post #4 by @jamesobutler (2022-09-12 14:52 UTC)

<p>Xref same discussion at</p>
<aside class="quote quote-modified" data-post="4" data-topic="25046">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e274bd/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/fiducial-marker/25046/4">Fiducial Marker</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi. 
Because of some modules, I had to use this version. After trial and error, I could find how to insert these fiducials, now I need to know how can I insert some “Planes”. Please see the below images. 
[image]
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2022-09-16 01:20 UTC)

<p>I’ve updated the extension for Slicer-5.0.3, added a short step-by-step tutorial, and submitted the extension to the Extensions Index so that from tomorrow it can be installed by a few clicks from the Extensions Manager (extension name: <code>SkinMouldGenerator</code>).</p>

---

## Post #6 by @Mohammad (2022-10-09 14:41 UTC)

<p>Dear Lassoan,</p>
<p>I must apologize for late reply.  I didn’t know you added this module to version 5.0.3. Today I’ve tried to use this module. After running the module, it say mold generated for path 1, but noting is shown on skin.<br>
How can I access to your tutorial?<br>
Is it possible for you to make an video tutorial for this module?</p>
<p>Many Thanks</p>

---

## Post #7 by @lassoan (2022-10-09 15:34 UTC)

<p>Video tutorials take long time to produce and hard to maintain. I might find some time to do it, but I would prefer to make the <a href="https://github.com/PerkLab/SlicerSkinMouldGenerator#tutorial">step by step tutorial</a> good enough so that users can follow it.</p>
<p>Please take a video or explain in detail what exact steps you did, what you expected to happen, and what happened instead. If you encounter any error then take a screenshot and open the Python console to see if there are any error messages and copy them here.</p>

---

## Post #8 by @Mohammad (2022-10-10 19:07 UTC)

<p>Dear Lassoan,</p>
<p>I followed your step-by-step tutorial, and finally, I could create my first mold. thank you so much.<br>
As you mentioned in this tutorial, " * A fake CT volume is created that contains the original CT and the needle channels so that a plan can be created in the treatment planning system. If the plan is not good enough then it is possible to change the channel positions (before it gets printed)." How can I export this fake CT with created mold?</p>
<p>Thanks a lot</p>

---

## Post #9 by @lassoan (2022-11-10 14:42 UTC)

<aside class="quote no-group" data-username="Mohammad" data-post="8" data-topic="25176">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e274bd/48.png" class="avatar"> Mohammad:</div>
<blockquote>
<p>How can I export this fake CT with created mold?</p>
</blockquote>
</aside>
<p>In the Data module you can right-click on any data set and choose “Export to file…” (or save everything using menu: File / Save data).</p>

---
