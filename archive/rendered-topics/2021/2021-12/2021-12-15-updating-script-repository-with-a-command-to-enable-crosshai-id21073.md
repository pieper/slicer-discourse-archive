---
topic_id: 21073
title: "Updating Script Repository With A Command To Enable Crosshai"
date: 2021-12-15
url: https://discourse.slicer.org/t/21073
---

# Updating script repository with a command to enable crosshair visibility

**Topic ID**: 21073
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/updating-script-repository-with-a-command-to-enable-crosshair-visibility/21073

---

## Post #1 by @koeglfryderyk (2021-12-15 10:13 UTC)

<p>I’m not sure if this is the correct place for such a request, however:</p>
<p>There are a lot of examples with the Crosshair in the script repository, however, none of them actually says that you have to make the crosshair visible (and how to do that). It took me quite some time to figure out why the crosshair was not showing.</p>
<p>Maybe it’s obvious for some, but I think adding a line of code that explains that would be helpful for beginners.</p>
<p>In the end, that’s what I used (but maybe there’s a better way):</p>
<pre><code class="lang-auto">crosshairNode = slicer.util.getNode("Crosshair")
crosshairNode.SetCrosshairMode(1)
</code></pre>

---

## Post #2 by @pieper (2021-12-16 17:01 UTC)

<p>This is a great suggestion.  Would you mind trying to edit the script repository your self and make a pull request?  You will find the ‘Edit on GitHub’ link in the upper right of the read the docs page.  If we all get in the habit of doing this it will help make sure contributions are reviewed and acted on and that credit for the contributions is recorded.</p>
<p>Small suggestion: instead of hard-coding the number <code>1</code> you could use <code>slicer.vtkMRMLCrosshairNode.ShowBasic</code>.</p>

---

## Post #3 by @koeglfryderyk (2024-04-24 13:35 UTC)

<p>is there a way to only show the crosshair in some views?</p>

---

## Post #4 by @lassoan (2024-04-24 20:51 UTC)

<p>There is only one global crosshair and they are shown in all views. However, the cursor only makes the crosshair jump in all the views that are in the same view group. If you set up view groups for your views appropriately then it might be sufficient for your use case.</p>
<p>It would not be too hard to make the <code>vtkMRMLCrosshairNode</code> a displayable node and use an associated display node to specify where the crosshair should be displayed, but I’m not aware that anyone is planning to work on this. If you are willing to spend some time with implementing this (it needs to be in C++) then let us know and we can help you getting started. Otherwise you can enter a feature request in this forum and if significant number of people vote on it then we’ll put it on the roadmap. You can also hire people from one of the Slicer Commercial Partner companies to implement this.</p>

---

## Post #5 by @koeglfryderyk (2024-04-25 13:37 UTC)

<p>I’ll have to get back to this in summer, but then I’d like to implement it myself</p>

---
