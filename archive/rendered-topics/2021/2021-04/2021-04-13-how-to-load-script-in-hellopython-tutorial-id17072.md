---
topic_id: 17072
title: "How To Load Script In Hellopython Tutorial"
date: 2021-04-13
url: https://discourse.slicer.org/t/17072
---

# How to load script in HelloPython tutorial?

**Topic ID**: 17072
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/how-to-load-script-in-hellopython-tutorial/17072

---

## Post #1 by @spycolyf (2021-04-13 18:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>The HelloPython tutorial say to load HelloPython.py. Do I load it into Python Interactor? Or do I use a text editor? Which tool shall I use to make changes to the python code on a Windows system? Shall I use a Python editor, or is that a good tool integrated with Slicer?</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2021-04-13 19:01 UTC)

<blockquote>
<p>The HelloPython tutorial</p>
</blockquote>
<p>To help us understand the context, which tutorial are you referring to ?</p>
<p>For reference, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></p>

---

## Post #3 by @spycolyf (2021-04-13 21:15 UTC)

<p>OK, I realize my question was totally confusing after re-reading it. I have since finished the tutorial and now know how to load the script. However, I’m using NotePad++ to edit the HelloPython code, save it and then restart Slicer. Are there better tools for editing Python module code that integrates into Slicer and allows debugging and break points for example? Thanks.</p>

---

## Post #4 by @pieper (2021-04-13 21:40 UTC)

<p>I don’t use it myself, but yes, there are debuggers integrated with better editors.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools</a></p>

---

## Post #5 by @jcfr (2021-04-13 21:51 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="3" data-topic="17072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I’m using NotePad++ to edit the HelloPython code, save it and then restart Slicer.</p>
</blockquote>
</aside>
<p>Note that in the context of Slicer modules/extension/customapp, they are usually two copies of each script:</p>
<ol>
<li>the ones available in  the source tree</li>
<li>the ones copied in the build tree after building the project</li>
</ol>
<p>Since we do not yet support a “develop” mode where we have a single copy, this means that after you modified the files in the build directory, you have to make sure to integrate your changes back in the source tree.</p>

---

## Post #6 by @lassoan (2021-04-14 03:40 UTC)

<p>As an IDE for Windows for Slicer Python module development, I would recommend PyCharm because it is a bit easier to set up and use. If you need a completely free version, you can use Visual Studio Code or Visual Studio. See detailed instructions <a href="https://github.com/SlicerRt/SlicerDebuggingTools">here</a>.</p>

---
