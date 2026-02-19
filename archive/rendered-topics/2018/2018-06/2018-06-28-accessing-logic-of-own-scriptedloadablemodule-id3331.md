---
topic_id: 3331
title: "Accessing Logic Of Own Scriptedloadablemodule"
date: 2018-06-28
url: https://discourse.slicer.org/t/3331
---

# Accessing logic() of own ScriptedLoadableModule

**Topic ID**: 3331
**Date**: 2018-06-28
**URL**: https://discourse.slicer.org/t/accessing-logic-of-own-scriptedloadablemodule/3331

---

## Post #1 by @basti (2018-06-28 20:28 UTC)

<p>I’m trying to access a method in the logic class of a ScriptedLoadableModule I created and loaded into slicer.<br>
The custom module is listed in slicer.modules, but in slicer.modules.CUSTOMMODULE.logic() I can’t access the specific methods of the module.</p>
<p>Is there a way to solve this?<br>
Thanks a lot, Sebastian</p>

---

## Post #2 by @pieper (2018-06-29 15:20 UTC)

<p>Hi Sebastien -</p>
<p>You can do something like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import BitmapGenerator
&gt;&gt;&gt; l = BitmapGenerator.BitmapGeneratorLogic()
&gt;&gt;&gt; l.generate()
</code></pre>
<p>FYI slicer.modules./module/.logic() is a lower level internal module that hooks your scripted code into the rest of Slicer.</p>
<p>-Steve</p>

---
