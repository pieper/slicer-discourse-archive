---
topic_id: 22625
title: "Scripted Extension Inheretance"
date: 2022-03-21
url: https://discourse.slicer.org/t/22625
---

# Scripted Extension inheretance

**Topic ID**: 22625
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/scripted-extension-inheretance/22625

---

## Post #1 by @tsims (2022-03-21 19:35 UTC)

<p>Hi everyone!</p>
<p>I was wondering if it was possible to set up an extension that defines a base module type that other modules can then inherit.</p>
<p>Basically what  I would like is to have a set of classes that extend the SlicerLoadableModule, then another set extending those classes, e.g.:</p>
<p>foo.py</p>
<pre><code class="lang-auto">class foo(ScriptedLoadableModule):
...

class fooWidget(ScriptedLoadableModuleWidget):
...

class fooLogic(ScriptedLoadableModuleLogic):
...
</code></pre>
<p>bar.py</p>
<pre><code class="lang-auto">class bar(foo):
...

class barWidget(fooWidget):
...

class barLogic(fooLogic):
...
</code></pre>
<p>Is it possible to have a set up like this in slicer? Right now I can’t seem to get slicer to detect and load the module when I have it scan the extension directory.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-03-21 19:50 UTC)

<p>Yes, that should work in theory.  You’ll need to be careful about the directories because the module discover process expects to have a working set of module classes that match the filename of the .py file, so you may need to put the abstract classes into a lib folder.</p>

---
