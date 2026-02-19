---
topic_id: 44409
title: "Create A Scripted Segment Editor Effect By Extension Wizard"
date: 2025-09-09
url: https://discourse.slicer.org/t/44409
---

# create a scripted segment editor effect by extension wizard  

**Topic ID**: 44409
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/create-a-scripted-segment-editor-effect-by-extension-wizard/44409

---

## Post #1 by @LeonHaoWI (2025-09-09 13:15 UTC)

<p>I’m new to slicer development, try to create a scripted module base on segment editor effect,</p>
<p>I’m using 5.9 version, and try to create a skeleton by using extension wizard, no information is shown in error log window, but the created module can’t be found in module finder,</p>
<p>I have tried restart the application, the module path have been added to additional module paths. And the created module can be find in setings-modules.</p>
<p>could any one tell me what have I missed. I suppose such a module don’t need to build slicer from source…</p>

---

## Post #2 by @cpinter (2025-09-09 13:17 UTC)

<p>Segment editor effects do not appear as modules, but as new tools (“effects”) in the Segment Editor module</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" target="_blank" rel="noopener">Segment editor — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>What are you trying to achieve? What does your module do?</p>

---

## Post #3 by @LeonHaoWI (2025-09-09 13:57 UTC)

<p>Thanks for reply.</p>
<p>I’m trying to add a tinny function(push button) to segment editor, to allow auto save current segment and load next data, then add segment node and couple of segment.(for improve efficiency of annotation process).</p>
<p>When create a scripted module by extension wizard, I found there is a module template type called scriptedsegmenteditoreffect, suppose it is the easiest way to customize segment editor module.</p>
<p>But after creation, the module can’t be found in module finder, but can be found in edit- application setings-modules.</p>
<p>So, did I misunderstand this template?</p>

---

## Post #4 by @LeonHaoWI (2025-09-15 01:50 UTC)

<p>I figured out a way: <a href="https://discourse.slicer.org/t/creating-a-basic-paint-foreground-and-paint-background-tool/17050/6">Creating a basic Paint Foreground and Paint Background Tool - Support - 3D Slicer Community</a></p>
<p>Instance segment editor widget. Thank Pinter for your remind.</p>
<p>But I still don’t understand why the template don’t work.</p>

---

## Post #5 by @cpinter (2025-09-15 14:18 UTC)

<aside class="quote no-group" data-username="LeonHaoWI" data-post="3" data-topic="44409">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/leonhaowi/48/81000_2.png" class="avatar"> LeonHaoWI:</div>
<blockquote>
<p>I’m trying to add a tinny function(push button) to segment editor</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="LeonHaoWI" data-post="3" data-topic="44409">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/leonhaowi/48/81000_2.png" class="avatar"> LeonHaoWI:</div>
<blockquote>
<p>scriptedsegmenteditoreffect, suppose it is the easiest way to customize segment editor module.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="LeonHaoWI" data-post="4" data-topic="44409">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/leonhaowi/48/81000_2.png" class="avatar"> LeonHaoWI:</div>
<blockquote>
<p>But I still don’t understand why the template don’t work.</p>
</blockquote>
</aside>
<p>Segment Editor has its own little ecosystem, and it is very complex. What you can do with segment editor effect modules is to <em>add a new editing tool (effect)</em>, nothing else. If you want to change the module, it is not possible. You can get the Segment Editor module from your own module, and insert some widget in a layout you choose, but it’s a hack, and the only way I can currently imagine.</p>
<p>Most of the Segment Editor module is just the segment editor widget, so you could just create your own “batch segment editor” module based on the original, where you add that button. Sorry for the late answer.</p>

---
