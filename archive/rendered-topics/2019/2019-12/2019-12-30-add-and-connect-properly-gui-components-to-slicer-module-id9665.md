---
topic_id: 9665
title: "Add And Connect Properly Gui Components To Slicer Module"
date: 2019-12-30
url: https://discourse.slicer.org/t/9665
---

# Add and connect properly GUI components to Slicer module

**Topic ID**: 9665
**Date**: 2019-12-30
**URL**: https://discourse.slicer.org/t/add-and-connect-properly-gui-components-to-slicer-module/9665

---

## Post #1 by @CreepyTrick (2019-12-30 18:43 UTC)

<p>Hello</p>
<p>I come here again for a basic question … how to add and connects UI components like button and all in a new <strong>Loadable</strong> (so c++) module ?</p>
<p>I found how to add: The UI file that i can open with Qt and add any component i want, but i dont know how to connect them properly …. nether where to do it.</p>
<p>I got the base <code>qSlicerModuleNameFooBarWidget</code> and other file with “Widget” in their name …<br>
But if i want to connect the basic “foo bar” button (created by default), how and where i should do this ?</p>
<p>(I’m working with Visual Studio)</p>

---

## Post #2 by @lassoan (2019-12-30 19:56 UTC)

<p>Usually you create all connections in the widget’s <code>setup</code> method. You can use all of Slicer’s loadable modules as examples. For example, see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Tables/qSlicerTablesModuleWidget.cxx#L109-L164">source code of Tables module widget</a>.</p>

---

## Post #3 by @CreepyTrick (2019-12-31 13:20 UTC)

<p>Alright, thanks for your answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> .</p>

---
