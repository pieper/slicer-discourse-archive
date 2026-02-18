# Python called qSlicerSubjectHierarchyParseLocalDataPlugin function

**Topic ID**: 18600
**Date**: 2021-07-09
**URL**: https://discourse.slicer.org/t/python-called-qslicersubjecthierarchyparselocaldataplugin-function/18600

---

## Post #1 by @StephenLeePeng (2021-07-09 12:48 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.13.0 - self build.<br>
Expected behavior:<br>
When I load a directory contains subdirectory in the Slicer. The directory contains some .stl files. And after load, these stl models will be displayed in the Node subject hierarchy window by name, but without any hierarchy format.<br>
When I right click the scene option: “Create hierarchy from loaded directory structure”, these stl models will be rearranged by directory structure.<br>
Above description is manually operations. And I want realize this process in Python terminal. So I faced a problem: qSlicerSubjectHierarchyParseLocalDataPlugin is a Loadable module, how I can use Python to called Loadable module qSlicerSubjectHierarchyParseLocalDataPlugin’s slot function: createHierarchyFromLoadedDirectoryStructure.</p>
<p>Actual behavior:</p>

---

## Post #2 by @cpinter (2021-07-09 13:07 UTC)

<p>It is a protected slot, so you cannot currently call it directly from code. We could move this code out to a class and make it public from which you can call it. Unfortunately I don’t see a class that is a natural place for this function (the logic would be it but it is VTK based so we cannot put it there). <a class="mention" href="/u/lassoan">@lassoan</a> how about <code>qMRMLSubjectHierarchyTreeView</code>? <code>qSlicerSubjectHierarchyPluginLogic</code> maybe? Or the model?</p>

---

## Post #3 by @StephenLeePeng (2021-07-12 06:41 UTC)

<p>Thank you for your reply.<br>
As my aim is to create an extension,  combine some features originally belong to different modules, such as Data, Models, Segment Editor and so on.<br>
To achieve python called qSlicerSubjectHierarchyParseLocalDataPlugin’s protected slot function: createHierarchyFromLoadedDirectoryStructure aim, I modify the qSlicerSubjectHierarchyParseLocalDataPlugin.h, change the function type, from “protected slots” to “public slots”, then make the slicer project again.<br>
After make finished, I can called the slot function in the Python Interactor.</p>
<pre><code class="lang-python">plugin = slicer.qSlicerSubjectHierarchyPluginHandler.instance()
p = plugin.pluginByName("ParseLocalData")
p.createHierarchyFromLoadedDirectoryStructure()
</code></pre>
<p>After call the public slot func, the models which sorted by default name, display in the Node tree view window, will be rearranged by local loaded directory structure.</p>
<p>Of course, this is a tempory solution. And I hope there has been a more suitable solution.</p>

---

## Post #4 by @cpinter (2021-07-12 12:08 UTC)

<p>This is an acceptable workaround until we make this function accessible.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you please see my question above? If we decide where to move this function I can do that. Thanks!</p>

---

## Post #5 by @lassoan (2021-07-12 13:52 UTC)

<p>I find organizing of loaded data into folders based on file location a very useful feature, but underused - because it is hard to discover it. What do you think about making it the default behavior somehow?</p>
<p>If this feature would become essential infrastructure (e.g., used in all data loading) then the most appropriate place would be to have it in vtkSlicerSubjectHierarchyModuleLogic. Otherwise exposing it as a public method of the plugin sounds like a completely fine solution to me.</p>

---

## Post #6 by @cpinter (2021-07-12 15:00 UTC)

<p>I agree with your choice of class, but porting it to VTK would be a pain. We could make it default if we could detect if the user is loading a folder structure, but I don’t see how to do it conveniently without showing a popup about this every time the user loads more than one file at a time.</p>

---

## Post #7 by @lassoan (2021-07-12 19:58 UTC)

<p>We could always do this when the user loads multiple files. It could be a feature of the “Add data” dialog and we could add a checkbox to enable/disable it. It would take a lot of effort to implement this, and it would just save two clicks for the user; but it could still make sense to implement this at some point, because users otherwise would probably not know that this feature exists.</p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="18600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I agree with your choice of class, but porting it to VTK would be a pain.</p>
</blockquote>
</aside>
<p>kwSys has a number of file and directory manipulation functions, so nothing major or risky would need to be developed, but I agree that it could take a few hours.</p>

---

## Post #8 by @lassoan (2021-07-18 02:37 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> has made <code>createHierarchyFromLoadedDirectoryStructure</code> method available in current Slicer Preview Release.</p>

---

## Post #9 by @cpinter (2021-07-18 12:58 UTC)

<p>Right, thanks for mentioning it here, I forgot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
