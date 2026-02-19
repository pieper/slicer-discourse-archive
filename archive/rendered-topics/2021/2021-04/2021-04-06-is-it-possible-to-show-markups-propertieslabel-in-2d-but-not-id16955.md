---
topic_id: 16955
title: "Is It Possible To Show Markups Propertieslabel In 2D But Not"
date: 2021-04-06
url: https://discourse.slicer.org/t/16955
---

# Is it possible to show Markups PropertiesLabel in 2D but not 3D?

**Topic ID**: 16955
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/is-it-possible-to-show-markups-propertieslabel-in-2d-but-not-3d/16955

---

## Post #1 by @mikebind (2021-04-06 00:14 UTC)

<p>Hello, I find the new MarkupsCurve  “PropertiesLabel” handy in 2D, but find that it clutters up my 3D view (where I have other labels) and there’s more overlap. Is it possible to show these labels in slice views but not the 3D view?  I know that it is possible to hide the markups curve in just the 3D view by unchecking “View1” in the “Advanced” section of the Display section of the Markups module, but this makes the curve and control points disappear from the 3D view.  Ideally, I’d like control of just the PropertiesLabel.</p>

---

## Post #2 by @lassoan (2021-04-06 13:36 UTC)

<p>You can remove 3D views from the first display node; and add a second display node with all the slice views removed. This way you can set all display properties separately in the two view types. Only the first display node can be edited in the Markups module GUI.</p>
<p>We plan to allow manual repositoning of the labels repositionable. Would that fix the issue?</p>

---

## Post #3 by @mikebind (2021-04-06 14:56 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, a second display node should work perfectly for me, I didn’t realize that was possible, and might be a good solution for some other use cases too.</p>
<p>An option for manual repositioning would be great in general, but would not solve my problem in this case.  I am generating a standard set of screenshots for stereo EEG electrodes and the whole goal is to automate that process as much as possible, so manually repositioning labels would be too time consuming.  In general, on those shots, the more labels on slice views, the better, but on the 3D views, I already have custom labels which are located more out of the way (at the entry end of the electrodes), so the PropertiesLabels are duplicates and more obscuring.  In addition to standard screenshots, I also often generate more curated shots to illustrate something specific, with more care taken to decide exactly what is shown in each shot.  For those cases, I would definitely use manual label repositioning if it were available.</p>

---

## Post #4 by @Emanuel_Tschopp (2023-08-24 11:15 UTC)

<p>Dear Andras<br>
I have the same issue as Mike, but couldn’t figure out where and how to create these different display nodes you’re talking about. Could you elaborate on that a little?<br>
Alternatively, it would be very useful, if there was a possibility to select all (or at least multiple) markup curves etc. in the “Markups” module and change the display setting for all of them at the same time. If that’s possible, please let me know how (I couldn’t figure that out either…).<br>
I’m using version 5.2.1 on Windows, currently.<br>
Thanks a lot,<br>
Emanuel</p>

---

## Post #5 by @mikebind (2023-08-28 20:25 UTC)

<p>You can create and modify these additional display nodes using python, either in the python interactor (if you just want to experiment a bit) or in a custom scripted module (if you want to have a reusable tool).  It is not possible within the default Slicer build to modify more than one display node using the GUI; if a node has more than one display node, then only the first one can be modified using the GUI.   I tried to find good reference information for using multiple display nodes, either in the documentation, script repository, or on this forum, but was not quickly successful.  Basically, however, using multiple display nodes works the same a using a single display node, with the exception of managing which views a given display node should appear in.  This is handled through <code>dispNode.SetViewNodeIDs()</code></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties</a></p>
<p>If you want to pursue this further and need a little more guidance, let me know and I can put together a small example to demonstrate.</p>

---
