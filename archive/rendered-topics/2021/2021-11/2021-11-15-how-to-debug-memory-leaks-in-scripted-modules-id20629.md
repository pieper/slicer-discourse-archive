---
topic_id: 20629
title: "How To Debug Memory Leaks In Scripted Modules"
date: 2021-11-15
url: https://discourse.slicer.org/t/20629
---

# How to debug memory leaks in scripted modules

**Topic ID**: 20629
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/how-to-debug-memory-leaks-in-scripted-modules/20629

---

## Post #1 by @tsims (2021-11-15 21:30 UTC)

<p>Hello everyone, I have been writing a Python scripted module for slicer, and recently I have been getting warnings about memory leaks when I go to close slicer, is there a recommended way of diagnosing where those are coming from in my code?</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2021-11-15 23:15 UTC)

<p>It can be a bit of a bear of a task, but generally there seem to be some pretty common method usages that cause the memory leaks.</p>
<p>I would guess it is because you are using some methods like <code>GetNodesByClass</code> rather than something like <code>GetNthNodeByClass</code>.</p>
<pre><code class="lang-python">for i in range(slicer.mrmlScene.GetNumberOfNodesByClass('vtkMRMLSegmentationNode')):
            segmentation_node = slicer.mrmlScene.GetNthNodeByClass(i, 'vtkMRMLSegmentationNode')
</code></pre>
<p>Also things like <code>CreateNodeByClass</code> can cause memory leaks, but can be avoided by using <code>AddNewNodeByClass</code> instead.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Tutorials/MemoryManagement - Slicer Wiki</a> for more details.</p>
<p>Also related is <a href="https://github.com/Slicer/Slicer/issues/2718" class="inline-onebox" rel="noopener nofollow ugc">Memory leaks when returning vtkCollection objects to Python as return value · Issue #2718 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #3 by @tsims (2021-11-16 14:44 UTC)

<p>Thank you so much! That looks like what is probably going on in my code, thank you for the information!</p>

---
