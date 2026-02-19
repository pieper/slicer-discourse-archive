---
topic_id: 36496
title: "Reload Option For Data"
date: 2024-05-30
url: https://discourse.slicer.org/t/36496
---

# Reload option for data

**Topic ID**: 36496
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/reload-option-for-data/36496

---

## Post #1 by @dyollb (2024-05-30 12:00 UTC)

<p>I see <a href="https://discourse.slicer.org/t/reload-data-via-ui/26204/5">this has been requested before</a> but was dismissed because there is some python API which could be used to achieve the same thing.</p>
<p>Nevertheless, I really miss the reload option in the Data module context menu. In ParaView I use this all the time to reload data, e.g. when I am debugging an algorithm where I write to the same file name and then need to reload the data to inspect if the result has improved.</p>

---

## Post #2 by @lassoan (2024-05-30 13:23 UTC)

<p>Would you want to add it as a right-click menu action to data module? It would further complicate the already complex GUI, so I would only do it if at least a handful of people confirm they would use this feature.</p>
<p>My reluctance for adding a GUI for this is that a manual update would not be an inconvenient solution if the goal is to automatically reload data after some processing. It is just way faster, easier, and more robust, if you trigger a reload in Slicer by adding a single line of code at the end of your processing in your external software.</p>
<p>If other users are not interested in having GUI for manual reload, you can still easily add it without any Slicer core changes. For example, you can observe all storage nodes and add a QFileSystemWatcher to monitor file changes; and if any file changes then you can reload the data. Or instead of automatically loading the data, it could display a button on the status bar when a change detected that you could click to reload all changed data. These would be all better options than having to locate a node in the Data module, right-click, and choose “Reload”, but if you want to implement exactly that, then that is perfectly doable, too: you can add a subject hierarchy plugin that provides a “Reload” right-click menu action for storable nodes (maybe 30 lines of Python code).</p>

---

## Post #3 by @jamesobutler (2024-05-30 15:21 UTC)

<p>I could see reload being useful as a workaround for there not being an undo function in some areas. For example, many of the CLI based modules doing various types of image manipulation have an option for the output volume node to be the same as the input volume node. Sometimes I accidentally overwrite my input and realize I need to clear and reload the volume to apply a different set of parameters to the original volume.</p>

---

## Post #4 by @dyollb (2024-05-30 15:45 UTC)

<p>I don’t know if you currently store the file path in the node (ParaView, storing the pipeline I guess naturally can re-evaluate the whole pipeline, including readers). If not, I guess it is a bit more complicated to implement.</p>
<ul>
<li>In terms of where in the GUI, I would find the context menu in the Data module the most intuitive. If I need to switch modules I find it less convenient.</li>
<li>I don’t want an auto-reload, but user-controlled on demand. The data is often large or re-extracting surfaces would be slow.</li>
<li>If I could add the functionality via some plugin, adding a button in the status bar might be ok, but then I guess this would globally reload ALL datasets.</li>
</ul>

---

## Post #5 by @lassoan (2024-05-30 15:56 UTC)

<aside class="quote no-group" data-username="dyollb" data-post="4" data-topic="36496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dyollb/48/16686_2.png" class="avatar"> dyollb:</div>
<blockquote>
<p>I don’t know if you currently store the file path in the node</p>
</blockquote>
</aside>
<p>Yes, we store the input file(s) path in the storage node associated with the data node. This makes reload trivial to implement - see for example <a href="https://github.com/Slicer/Slicer/blob/fcba379c077f5a6c3d1d7a0ec91e4a659b32fce4/Modules/Scripted/WebServer/WebServerLib/SlicerRequestHandler.py#L759-L766">here</a>.</p>
<aside class="quote no-group" data-username="dyollb" data-post="4" data-topic="36496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dyollb/48/16686_2.png" class="avatar"> dyollb:</div>
<blockquote>
<p>If I could add the functionality via some plugin, adding a button in the status bar might be ok, but then I guess this would globally reload ALL datasets.</p>
</blockquote>
</aside>
<p>You can add the functionality via plugins anywhere (no need to change anything in Slicer core). It can be a context menu in Data module, a button in the status bar, etc. A button in the status bar would be much easier to use (one click) than context menu in data module (2 clicks to switch to data module, scroll and click to find your data node, 2 click to select reload function in context menu, 2 clicks to switch to the module where you were before). You don’t need to always show that button, only when an input file is changed. You can get a callback when one of the input files changed for example by using QFileSystemWatcher.</p>
<p>How do you generate the updated files? Most people generate updated files by using some custom processing code (without a GUI), and wants to visualize the updated results in Slicer. Is this not the case for you? Note that you can reload data in Slicer from your own Python scripts, running outside Slicer, in any Python environment, even on a different computer, by a single function call. Isn’t this much better then asking the user to manually click some buttons?</p>

---
