---
topic_id: 33457
title: "What The Loading Order Of Scripted Modules"
date: 2023-12-19
url: https://discourse.slicer.org/t/33457
---

# What the loading order of scripted modules

**Topic ID**: 33457
**Date**: 2023-12-19
**URL**: https://discourse.slicer.org/t/what-the-loading-order-of-scripted-modules/33457

---

## Post #1 by @Fokatu (2023-12-19 10:14 UTC)

<p>One of my module (“AAA”) need functions of another module (“BBB”), so I want the BBB module be loaded before AAA module.<br>
I add “BBB” in the AAA’s dependencies list as follows, but it seems not working.</p>
<pre><code class="lang-auto">class AAA(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("AAA")  
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Examples")]
        self.parent.dependencies = ["BBB"]  # TODO: add here list of module names that this module requires
</code></pre>
<p>To verify this, I print a line at the end of the two modules init function. It appears that module AAA still loads first.</p>
<p>the output of python console is as follows</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Nov 26 2023, 05:23:59) [MSC v.1935 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
AAA: init
BBB: init
Loading Slicer RC file [D:/3DSlicer/slicer.org/Slicer 5.6.0/bin/../.slicerrc.py]
</code></pre>
<p>How to load “BBB” first before “AAA” is loaded</p>

---
