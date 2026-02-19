---
topic_id: 9693
title: "Rotation In Dicom Data"
date: 2020-01-02
url: https://discourse.slicer.org/t/9693
---

# Rotation in DICOM data

**Topic ID**: 9693
**Date**: 2020-01-02
**URL**: https://discourse.slicer.org/t/rotation-in-dicom-data/9693

---

## Post #1 by @OJay (2020-01-02 19:43 UTC)

<p>Hi:)<br>
Is it possible to set in DICOM data two points to get a line and then rotate around this line?<br>
Best Regards,<br>
Ole</p>

---

## Post #2 by @lassoan (2020-01-03 13:30 UTC)

<p>If you need to rotate slice views (for example, to explore structures around a tool trajectory): you can install SlicerIGT extension and use Volume reslice driver or PathExplorer modules. These modules are not trivial to use, so if you need help with then let us know.</p>
<p>If you need to rotate images or structures (change their physical orientation): you can follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line">these instructions</a>. You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">put the code snippet into a scripted module</a> to make it more user-friendly (to not require typing and copy/pasting into the Python console).</p>

---

## Post #3 by @OJay (2020-01-07 13:37 UTC)

<p>Thank you very much for you information… i try a little bit its not so easy <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>again one question… where i found a Surface Registration?<br>
I will merge a STL model on a cbct data set…</p>
<p>Thank you in advance,<br>
Ole</p>

---

## Post #4 by @lassoan (2020-01-07 13:56 UTC)

<aside class="quote no-group" data-username="OJay" data-post="3" data-topic="9693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/c5a1d2/48.png" class="avatar"> OJay:</div>
<blockquote>
<p>Thank you very much for you information… i try a little bit its not so easy</p>
</blockquote>
</aside>
<p>Are you interested in rotating slice views or you need to change physical position/orientation of images?</p>
<aside class="quote no-group" data-username="OJay" data-post="3" data-topic="9693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/c5a1d2/48.png" class="avatar"> OJay:</div>
<blockquote>
<p>again one question… where i found a Surface Registration?<br>
I will merge a STL model on a cbct data set…</p>
</blockquote>
</aside>
<p>Would you mind posting this in a separate topic? (this will be a start of a new discussion, unrelated to image or view rotation)</p>

---

## Post #5 by @OJay (2020-01-07 14:16 UTC)

<p>interested in rotating slice views (rotate around a bone)</p>
<p>thank you</p>

---

## Post #6 by @lassoan (2020-01-07 14:39 UTC)

<p>In recent Slicer Preview Releases, you can easily rotate slice views by showing slice intersections (using dropdown menu of crosshair button in the toolbar), setting slice intersection position using <kbd>Shift</kbd> + mouse-move, then rotate slices using <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + left-click-and-drag.</p>
<p>You can copy-paste this code snippet into the Python interactor for initial alignment based on a markups line:</p>
<pre><code class="lang-python">lineNode = getNode('L')

# Get direction vector of the line
import numpy as np
p1 = np.zeros(3)
p2 = np.zeros(3)
lineNode.GetNthControlPointPositionWorld(0, p1)
lineNode.GetNthControlPointPositionWorld(1, p2)
directionVector = p2-p1

# Position/orient slice views based on line position and direction
for axisIndex, viewName in enumerate(['Red', 'Green', 'Yellow']):
  sliceNode = slicer.app.layoutManager().sliceWidget(viewName).mrmlSliceNode()
  sliceNode.SetSliceToRASByNTP(directionVector[0], directionVector[1], directionVector[2], 1,0,0, p1[0], p1[1], p1[2], axisIndex)
</code></pre>

---

## Post #7 by @OJay (2020-01-08 15:51 UTC)

<p>Sorry its dont work… is a other way available?</p>

---

## Post #8 by @lassoan (2020-01-08 16:02 UTC)

<p>I’ve tested this yesterday with a recent Slicer Preview Release and it worked well. If you have any trouble then please provide step-by-step description (or screen capture) of what you did, what you expected to happen, and what happened instead.</p>

---

## Post #9 by @OJay (2020-01-08 16:47 UTC)

<p>Ohhh yessss with the Preview Release version it is works!!! i had the older version…</p>
<p>Thanks!</p>

---

## Post #10 by @WangZhen1175701153 (2021-04-07 07:25 UTC)

<p>How do I get the node ‘L’?<br>
Sorry, I just started learning how to use 3DSlicer.</p>

---

## Post #11 by @lassoan (2021-04-08 16:06 UTC)

<p>If you draw a line markup (choose to place a Line in the toolbar) then by default its name will be ‘L’. The code snippet uses that line as rotation axis.</p>

---

## Post #13 by @WangZhen1175701153 (2021-04-09 00:42 UTC)

<p>Thank you very much <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:">. I’ve looked at a number of script files that just use getNode () without explaining how Nodes are created.</p>

---

## Post #14 by @lassoan (2021-04-09 00:43 UTC)

<p>You can learn Slicer programming basics from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">these tutorials</a>.</p>

---

## Post #15 by @WangZhen1175701153 (2021-04-09 01:25 UTC)

<p>ok. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"> Thank you for your help!!!</p>

---
