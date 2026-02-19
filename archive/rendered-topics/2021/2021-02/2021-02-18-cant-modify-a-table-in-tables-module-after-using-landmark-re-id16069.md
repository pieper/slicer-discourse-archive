---
topic_id: 16069
title: "Cant Modify A Table In Tables Module After Using Landmark Re"
date: 2021-02-18
url: https://discourse.slicer.org/t/16069
---

# Can't modify a table in "Tables" module after using "Landmark Registration" module

**Topic ID**: 16069
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/cant-modify-a-table-in-tables-module-after-using-landmark-registration-module/16069

---

## Post #1 by @giovform (2021-02-18 22:16 UTC)

<p>To reproduce:</p>
<ul>
<li>
<p>Use the “Landmark Registration” module to register any pair of RGB images (I used ThinPlate Registration type);</p>
</li>
<li>
<p>Go to the “Tables” module, create a new table, and try to add columns or rows using the interface. It will be irresponsive;</p>
</li>
</ul>

---

## Post #2 by @lassoan (2021-02-18 23:51 UTC)

<p>Can you share with us a scene with that you can reproduce this? Have you tried with the latest Slicer Preview Release?</p>

---

## Post #3 by @giovform (2021-02-19 10:26 UTC)

<p>I have tried with the latest preview, and had the same problem.</p>
<p>Sending a scene won’t do much since the problem only happens when you acess the Landmark Registration module (you don’t even need to finish a registration, just add and select two plain jpg images to register and click apply to start the registration), and then access the Tables module, create a table and try to add columns and rows.</p>

---

## Post #4 by @pieper (2021-02-19 15:54 UTC)

<p>Yes, I was able to replicate this behavior.  After using LandmarkRegistration the <code>qMRMLTableView</code> gets into a bad state somehow.  I have no idea why at this point.</p>

---

## Post #5 by @lassoan (2021-02-19 15:56 UTC)

<p>I could reproduce the issue, too. I’ll submit a fix today.</p>

---

## Post #6 by @lassoan (2021-02-19 17:10 UTC)

<p>The problem is caused by incorrect handling of batch processing in qMRMLTableView. I’ve pushed a <a href="https://github.com/Slicer/Slicer/pull/5475">fix</a>.</p>
<p>It is related to Landmark Registration module, which uses batch processing mode excessively. Probably the original intent was to speed up things, but switching to batch processing mode is a very expensive operation by itself, because it invalidates contents of widgets, so they need to rebuild themselves from scratch. Doing it for simple operations can cause very significant performance hit, especially when the scene has many nodes. Instead of scene-level batch processing, node-level start/end-modified and pause/resume-render should be used for performance optimization.</p>

---

## Post #7 by @pieper (2021-02-19 18:21 UTC)

<p>Thanks for the fix <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I suppose LandmarkRegistration could change, but I’ve never notice any performance issues related to batch processing mode, even in scenes with dozens of volumes and other things loaded (there are lots of other things that have <em>do</em> need fixing in Landmark Registration though to make it more useful).</p>

---

## Post #8 by @lassoan (2021-02-19 18:53 UTC)

<p>Each node selector, subject hierarchy view, etc. widget contain a scene model, which may take significant amount of time to rebuild from scratch after batch processing. If you load the brain atlas scene (it contains 1200 nodes) then each node selector adds about 5 ms, each subject hierarchy tree view adds about 15 ms to the time to get out of batch processing, which can easily add up to hundreds of ms. It may still be hardly noticeable, but if modules started to use batch processing to try to speed up simple operations then it would actually slow down the application.</p>
<p>I fully agree, though, that there are much more important things to improve in landmark registration.</p>

---

## Post #9 by @giovform (2021-02-19 19:56 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
