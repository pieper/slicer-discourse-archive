---
topic_id: 12938
title: "Adjusting Window Level With Python Commands"
date: 2020-08-11
url: https://discourse.slicer.org/t/12938
---

# Adjusting window level with Python commands

**Topic ID**: 12938
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/adjusting-window-level-with-python-commands/12938

---

## Post #1 by @rohan_n (2020-08-11 00:00 UTC)

<p>Are there Python commands that do the same things as the various click and drag options of the Adjust Window level button? If so what is the syntax of these Python commands?<br>
Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @mangotee (2020-08-11 09:08 UTC)

<p>Hi there,<br>
if you have your volume node <code>nVol</code>, you can use these two lines:</p>
<pre><code>nVol.GetDisplayNode().SetAutoWindowLevel(False)
nVol.GetDisplayNode().SetWindowLevel(window,level)
</code></pre>
<p>where window and level are float values.</p>

---

## Post #3 by @Alex_Vergara (2020-08-11 13:28 UTC)

<p>you can also do</p>
<pre><code class="lang-auto">def setAndObserveColorNode(nVol, colorMap = "PET-Heat"):
    """
    set observable in color node
    """
    displayNode = nVol.GetScalarVolumeDisplayNode()
    if displayNode is not None:
        colornodeID = slicer.util.getFirstNodeByName(colorMap).GetID()
        displayNode.SetAndObserveColorNodeID(colornodeID)
        # Refresh Window Level
        displayNode.AutoWindowLevelOff()
        displayNode.AutoWindowLevelOn()
</code></pre>
<p>That way you control the color map and refresh window level</p>

---
