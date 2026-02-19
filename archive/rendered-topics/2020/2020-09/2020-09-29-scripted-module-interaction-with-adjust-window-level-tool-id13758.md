---
topic_id: 13758
title: "Scripted Module Interaction With Adjust Window Level Tool"
date: 2020-09-29
url: https://discourse.slicer.org/t/13758
---

# Scripted module interaction with "Adjust window level" tool

**Topic ID**: 13758
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/scripted-module-interaction-with-adjust-window-level-tool/13758

---

## Post #1 by @rohan_n (2020-09-29 19:45 UTC)

<p>Hello,<br>
I would like to know the syntax of the lines of Python code that would allow me to read the window, level values that the user set with the “Adjust Window Level Tool”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6794ceb1aca6446a460be18d8c286ea4e0d58be5.png" alt="adjustwindowlevel" data-base62-sha1="eMjZRGAgbHucRKookxAaqdA6aMJ" width="89" height="75"><br>
into variables in my scripted module.<br>
Thanks,<br>
Rohan</p>

---

## Post #2 by @jamesobutler (2020-09-29 19:53 UTC)

<p>This <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume" rel="noopener nofollow ugc">link</a> from the Slicer Script Repository details how to use python to set window/level.  There are similar methods to get current window level.</p>
<p>Using the python interactor typically located at the bottom of the Slicer main window, you can check out options available by doing the following</p>
<pre><code class="lang-python">volumeNode = getNode('MRHead')
volumeNode.GetDisplayNode().GetWindow # press [Tab] at this point to bring up auto-complete options that begin with GetWindow...
</code></pre>

---

## Post #3 by @rohan_n (2020-09-29 21:05 UTC)

<p>Thanks, I understood how to use the relevant set and get functionalities.<br>
If I have any more issues with this, I’ll reply again on this thread.</p>

---

## Post #4 by @rohan_n (2020-09-29 22:39 UTC)

<p>I actually do have a follow up question.<br>
What is the recommended way to check if the window level has been changed so that I can update variables containing windowlevelmin and windowlevel max? I want to do something like this:</p>
<p><code>(#user drags adjust window level tool in any direction).connect(self.updateWindowMinMax)</code></p>
<pre><code>def updateWindowMinMax(self):
      self.windowmin = self.inputSelector.currentNode().GetDisplayNode().GetWindowLevelMin()

      self.windowmax = self.inputSelector.currentNode().GetDisplayNode().GetWindowLevelMax()</code></pre>

---
