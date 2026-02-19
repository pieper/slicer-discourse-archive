---
topic_id: 26780
title: "Orienting Views With Respect To A Selected Markup"
date: 2022-12-17
url: https://discourse.slicer.org/t/26780
---

# Orienting views with respect to a selected markup

**Topic ID**: 26780
**Date**: 2022-12-17
**URL**: https://discourse.slicer.org/t/orienting-views-with-respect-to-a-selected-markup/26780

---

## Post #1 by @Karl_Hahn (2022-12-17 00:04 UTC)

<p>Hello,</p>
<p>For sake of reference, are there any particular Slicer modules that implement functionality to orient views with respect to a markup selected in the Markups module? For example, selecting a Plane reformats the views such that one is coplanar with the Plane and the others are mutually orthogonal.</p>
<p>I did notice that basic centering functionality is available, e.g. when clicking a point in a Point List or the origin of a Plane. The use cases of interest here are somewhat beyond this and perhaps more application-specific.</p>
<p>Thanks for the guidance!</p>
<p>Karl</p>

---

## Post #2 by @lassoan (2022-12-19 16:31 UTC)

<p>You can use <code>Volume reslice driver</code> module in SlicerIGT extension to “drive” (position and orient) a slice view by plan eor line markup. You can also use Path Explorer for reslicing along and around markup line nodes.</p>
<p>You can also create any customized behavior using a few lines of Python script (add an observer to a markup node and modify slice position and orientation whenever the markup is changed. You can find examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups">script repository</a>.</p>

---

## Post #3 by @Karl_Hahn (2022-12-21 20:27 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, a follow-up question: the relevant examples in the script repository observe markup modification, but I would like to trigger view reformatting when a markup is selected. What is the proper way to observe changes in markup selection, specifically in the list shown in the markups module? Do I assume correctly that selection is different from modification?</p>
<p>Thanks!</p>

---

## Post #4 by @Karl_Hahn (2022-12-21 22:21 UTC)

<p>Observing the <code>vtkMRMLSelectionNode</code> might accomplish the desired end. Unsure if this is an intended use case, though.</p>
<p>Crudely:</p>
<pre><code class="lang-auto">last_id = None

def reformat_if_selection_changed(active_id):
    if active_id!= last_id:
        ...reformat views...
        last_id = active_id

sn = slicer.app.applicationLogic().GetSelectionNode()
sn.AddObserver(
    slicer.vtkMRMLSelectionNode.ActivePlaceNodeIDChangedEvent, 
    lambda c, e: reformat_if_selection_changed(c.GetActivePlaceNodeID())
)
</code></pre>

---
