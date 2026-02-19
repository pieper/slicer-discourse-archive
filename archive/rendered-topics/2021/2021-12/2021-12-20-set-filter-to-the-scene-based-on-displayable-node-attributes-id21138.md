---
topic_id: 21138
title: "Set Filter To The Scene Based On Displayable Node Attributes"
date: 2021-12-20
url: https://discourse.slicer.org/t/21138
---

# Set filter to the scene based on displayable node attributes

**Topic ID**: 21138
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/set-filter-to-the-scene-based-on-displayable-node-attributes/21138

---

## Post #1 by @keri (2021-12-20 00:18 UTC)

<p>Hi,</p>
<p>I’m looking for a way to hide/show displayable nodes based on their attribute value.</p>
<p>I can see an option: to filter the scene at once and after that user can display recently hided nodes (if he wants) by clicking on eye icon in data module for example.<br>
Or add such functionality to the scene so that all nodes that dont fit the criteria must not be displayed no matter what <code>DisplayVisibility</code> they have.</p>
<p>I think I would prefer the second way but does Slicer community need such functionality?</p>

---

## Post #2 by @pieper (2021-12-20 15:15 UTC)

<p>I typically just use a small python loop to selectively show only the desired nodes.</p>

---

## Post #3 by @keri (2021-12-20 15:26 UTC)

<p>This is useful for those who is pretty familiar with python <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2021-12-22 14:44 UTC)

<p>An easy way to show/hide a group of nodes is to put them into a folder in the Data module and click the eye icon of the folder.</p>

---

## Post #5 by @keri (2021-12-23 02:06 UTC)

<p>Thank you, haven’t thought about that</p>

---
