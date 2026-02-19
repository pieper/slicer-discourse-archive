---
topic_id: 22256
title: "Running A Custom Extension On Start"
date: 2022-03-02
url: https://discourse.slicer.org/t/22256
---

# Running a custom extension on start

**Topic ID**: 22256
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/running-a-custom-extension-on-start/22256

---

## Post #1 by @Vincebisca (2022-03-02 09:50 UTC)

<p>Hello,</p>
<p>I am searching for a way to start a custom extension directly when starting 3D Slicer (some kind of modified .exe file, I don’t know).<br>
I am very bad at coding but managed somehow a few months ago to create a custom extension for a personal project using the QuickSegment template that I found. I would like to have a shortcut that starts 3D Slicer directly on this extension.</p>
<p>I have tried the command method first, described at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Slicelets - Slicer Wiki</a> but didn’t work. I don’t understand why it works on ordinary modules like Transforms or Colors, but not on Extensions such as SlicerElastix. And it doesn’t work for my own extension…</p>
<p>Would really appreciate if someone can help me out !</p>
<p>Thank you !</p>

---

## Post #2 by @jamesobutler (2022-03-02 12:07 UTC)

<p>Does setting your module as the “Home” module work for your purposes? For options on how to implement this, see <a href="https://discourse.slicer.org/t/open-a-slicer-module-with-python/21754" class="inline-onebox">Open a slicer module with python</a>.</p>

---

## Post #3 by @Vincebisca (2022-03-02 12:26 UTC)

<p>That is a good suggestion, and it might work, but it would make my 3D Slicer always start on this module, and it’s an internal setting… What I am trying to do is really to have an external shortcut that opens 3D Slicer on my Extension. That way I (and other people I work with) can access this feature when they need to, without internal configuration. Don’t know if I’m clear enough tho… Not a pro at all</p>

---

## Post #4 by @jamesobutler (2022-03-02 12:28 UTC)

<p>You can create a shortcut that includes the flag as suggested in the following post as that doesn’t require going into Slicer first and setting the “Home” module setting.</p>
<aside class="quote" data-post="2" data-topic="21754">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/open-a-slicer-module-with-python/21754/2">Open a slicer module with python</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    As an example I add this to the command line when I start slicer: 
--python-code "selectModule('WebServer')"

But you can put the same in .slicerrc.py, maybe using slicer.util.selectModule for style purposes.
  </blockquote>
</aside>


---

## Post #5 by @Vincebisca (2022-03-02 12:32 UTC)

<p>I tried something similar, but even with the command console, I can’t zuse the --python-code “selectModule(‘MyModule’)” command on my module, it doesn’t work also for SlicerElastix. I don’t know if it’s because they have a different status than internal modules such as Transforms…</p>
<p>Edit: doesn’t work with SegmentEditorExtraEffects, but works with MarkupsToModel. The main difference I see is that MarkupsToModel seems to be a loadable module, as opposed to the others which are scripted modules, but I don’t really know the difference</p>

---

## Post #6 by @Vincebisca (2022-03-02 13:07 UTC)

<p>Okay found it, the problem was that for an unknown reason, my module is still recognized as “QuickSegment”, the template’s name, and not by the name I gave. So it worked to modify the shortcut properties with the command line --python-code “slicer.util.selectModule(‘QuickSegment’)”. Still don’t know for Elastix tho.</p>
<p>Thanks for your help james ! Appreciate !</p>

---
