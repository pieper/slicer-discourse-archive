---
topic_id: 39592
title: "How Can Jupyter Control All The Slicer"
date: 2024-10-09
url: https://discourse.slicer.org/t/39592
---

# How can jupyter control all the slicer

**Topic ID**: 39592
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/how-can-jupyter-control-all-the-slicer/39592

---

## Post #1 by @VirOrange (2024-10-09 00:43 UTC)

<p>Hi everyone,</p>
<p>I am new to Slicer and would like to understand how Jupyter can be used to control Slicer. Specifically:</p>
<ol>
<li>Does using Jupyter mean that I can debug and trace the execution of different modules within Slicer, such as following specific processes step by step?</li>
<li>Additionally, if I want to create my own module and run it through Jupyter, is that possible?</li>
</ol>
<p>I am particularly interested in the first question, as I currently have no idea how to effectively use Jupyter for my research. For context, I have already gone through the tutorials and run some example scripts, but I would appreciate more detailed guidance.</p>
<p>Thank you in advance for your help!</p>
<p>Best wishes.</p>

---

## Post #2 by @lassoan (2024-10-10 04:49 UTC)

<aside class="quote no-group" data-username="VirOrange" data-post="1" data-topic="39592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virorange/48/77989_2.png" class="avatar"> VirOrange:</div>
<blockquote>
<p>Does using Jupyter mean that I can debug and trace the execution of different modules within Slicer, such as following specific processes step by step?</p>
</blockquote>
</aside>
<p>You still debug and trace execution of different modules within Slicer using a debugger. For Python scripted modules, you can use the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">DebuggingTools extension</a>.</p>
<aside class="quote no-group" data-username="VirOrange" data-post="1" data-topic="39592">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virorange/48/77989_2.png" class="avatar"> VirOrange:</div>
<blockquote>
<p>Additionally, if I want to create my own module and run it through Jupyter, is that possible?</p>
</blockquote>
</aside>
<p>You can run your code either in Jupyter or by <a href="https://github.com/Slicer/SlicerProgrammingTutorial">creating a new Slicer module</a>.</p>
<p>I find Jupyter most useful for prototyping algorithms. If I get something that is useful and I want to share it with users then I put the algorithm into a new Python scripted Slicer module.</p>

---

## Post #3 by @VirOrange (2024-10-12 13:34 UTC)

<p>Thanks for your reply! it’s really a comfort for me. <img src="https://emoji.discourse-cdn.com/twitter/smiling_face.png?v=12" title=":smiling_face:" class="emoji" alt=":smiling_face:" loading="lazy" width="20" height="20"></p>

---
