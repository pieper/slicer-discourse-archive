---
topic_id: 4509
title: "Accessing Modules From Python"
date: 2018-10-23
url: https://discourse.slicer.org/t/4509
---

# Accessing modules from Python

**Topic ID**: 4509
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/accessing-modules-from-python/4509

---

## Post #1 by @smrolfe (2018-10-23 18:06 UTC)

<p>Hello,</p>
<p>I’m new to Slicer and would like to understand better how to access scripted modules using python. I’m interested in using Python scripts to automate tasks by setting properties and executing the modules themselves, rather than the underlying filters. There are some good <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">examples</a> on the wiki using the segmentation editor and I’d like to understand how to generalize this to other modules.</p>
<p>I can access the widgets and logic using:<br>
widget = slicer.modules.myModule.widgetRepresentation()<br>
logic = slicer.modules.myModule.logic()</p>
<p>Any tips on a general approach to identifying and setting the properties from the GUI would be helpful.</p>
<p>Thanks,<br>
Sara</p>

---

## Post #2 by @pieper (2018-10-23 19:02 UTC)

<p>Hi Sara -</p>
<p>As a general rule, scripted modules should divide the work between the Widget class (pure GUI) and the Logic class that does all the actual work.  Following this design makes it easier to reuse the functionality in the way you are looking for, but it’s a little extra effort and not all modules are as clean as we would like.</p>
<p>Generally the easiest way to learn what’s going on is to have a look at the module code.  If you learn how to use the GUI, then you can trace what widget signals are connected slots that implement the behavior and you can tell quickly what is performed in the logic classes.</p>
<p>Also note that the two calls you cited both create new instances of the classes in question.  This can be useful if you want to create a copy of the widget to embed in another layout.</p>
<p>If the module has been entered in the current Slicer session, then a widget is already created and is cached for subsequent access.  So you can get it with something like (substitute the module name for “LabelStatistics” of the example):</p>
<pre><code class="lang-auto">slicer.modules.LabelStatisticsWidget
</code></pre>
<p>so you could use the GUI components and invoke callbacks if needed.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @smrolfe (2018-10-23 22:22 UTC)

<p>Hi Steve,<br>
Thanks for your reply, I appreciate the clarification. My eventual goal is to provide some simplified automation instructions for individuals familiar with the GUIs but with less programming experience.</p>
<p>I’m curious whether there’s been any discussion on providing some documentation or interface to translate module GUI options to Python commands? Thanks again for your input.</p>

---

## Post #4 by @yulaomao (2019-10-13 02:35 UTC)

<p>Hi Sara,<br>
I also have similar requirements, we need to call the module through Python and make it complete certain work or modify some of the default values in the module. Have you solved your problem? Can you give me some relevant information? Thanks very much.</p>

---

## Post #5 by @lassoan (2019-10-13 02:54 UTC)

<p>If there are any specific operations that you cannot figure out how to access from Python then feel free to post it as a new topic on this forum.</p>

---
