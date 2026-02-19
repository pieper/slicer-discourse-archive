---
topic_id: 6075
title: "How To Replicate The Behavior Of Remove All Markups From The"
date: 2019-03-08
url: https://discourse.slicer.org/t/6075
---

# How to replicate the behavior of "remove all markups from the active list" from the module "markups"

**Topic ID**: 6075
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/how-to-replicate-the-behavior-of-remove-all-markups-from-the-active-list-from-the-module-markups/6075

---

## Post #1 by @ZiyunLiang (2019-03-08 13:38 UTC)

<p>Hi, everyone!<br>
I’m writing a scripted module and I want to replicate the behavior of “<em>remove all markups from the active list</em>” from the module “<em>markups</em>” to my module. I have already replicated the behaviors like adding fiducials and get the coordinates of the fiducials but I just cannot replicate the one to delete fiducials.<br>
Does anyone know how to proceed?</p>
<p>Thank you!<br>
Andrea</p>

---

## Post #2 by @gleman (2019-03-08 17:57 UTC)

<p>GetActiveListID() in the markups logic has the current id, then just RemoveAllMarkups()</p>
<pre><code>markupsNode  = slicer.util.getNode( slicer.modules.markups.logic().GetActiveListID() )
markupsNode.RemoveAllMarkups()
</code></pre>
<p>Or just remove a single markup with:</p>
<p><code>markupsNode.RemoveMarkup(0)</code></p>
<p>which will remove the Nth Markup</p>

---

## Post #3 by @ZiyunLiang (2019-03-09 02:02 UTC)

<p>Fantastic! It worked. Thank you so much!<img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=6" title=":grin:" class="emoji" alt=":grin:"></p>

---
