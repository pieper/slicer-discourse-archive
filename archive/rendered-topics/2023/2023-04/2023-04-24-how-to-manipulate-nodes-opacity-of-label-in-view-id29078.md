---
topic_id: 29078
title: "How To Manipulate Nodes Opacity Of Label In View"
date: 2023-04-24
url: https://discourse.slicer.org/t/29078
---

# How to manipulate node's opacity of label in view?

**Topic ID**: 29078
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/how-to-manipulate-nodes-opacity-of-label-in-view/29078

---

## Post #1 by @dsa934 (2023-04-24 05:16 UTC)

<p>Operating system: window 10<br>
Slicer version: 5. 2.1</p>
<p>I want the opacity control to apply only to the label and not to the glyph.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c425c6663bd6f107761f8cfd74bbb17683984bc.png" alt="image" data-base62-sha1="frHK9HUoJLZkVvtsfCtVPYGnV0M" width="485" height="36"></p>
<p>I guess I need to adjust font style a in rgba, how to approach it?</p>
<pre><code class="lang-auto"># example 
temp.GetDisplayNode().SetPointLabelsVisibility(False)
</code></pre>
<p>instead Visibility =&gt; Opacity</p>

---
