---
topic_id: 7567
title: "Two Different Layoutwidget"
date: 2019-07-14
url: https://discourse.slicer.org/t/7567
---

# Two different layoutWidget

**Topic ID**: 7567
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/two-different-layoutwidget/7567

---

## Post #1 by @AndreaRoberti (2019-07-14 16:51 UTC)

<p>Hi,<br>
I’m developing a custom interface with slicer for one of my projects, and i’m facing a “simple” problem.</p>
<p>I want in the same QWidget two different layoutWidget with two different layout manager, but when I create the objects it seems that they are the same layout manager for both widgets. Is it possible to have separate layout manager?</p>
<p>Following a simple example to show you what is the problem !</p>
<code>
   import qt
   import __main__
<p>mainWidget = qt.QWidget()<br>
mainWidget.objectName = “TestWidget”<br>
vBoxLayout = qt.QVBoxLayout()<br>
mainWidget.setLayout(vBoxLayout)</p>
<p>lm = slicer.qSlicerLayoutManager()<br>
lm.setMRMLScene(slicer.mrmlScene)<br>
lm.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpRedSliceView)<br>
lw =  slicer.qMRMLLayoutWidget()<br>
lw.setLayoutManager(lm)</p>
<p>lw2 =  slicer.qMRMLLayoutWidget()<br>
lm2 = slicer.qSlicerLayoutManager()<br>
lm2.setMRMLScene(slicer.mrmlScene)<br>
lm2.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)<br>
lw2.setLayoutManager(lm2)</p>
<p>vBoxLayout.addWidget(lw)<br>
vBoxLayout.addWidget(lw2)<br>
mainWidget.show()<br>
</p></code>
<p>I hope you can help me, any suggestion would be appreciate !</p>

---

## Post #2 by @lassoan (2019-07-14 18:20 UTC)

<p>There can be only one layout manager in the application and it displays all views within a single layout widget. If you want to add more views, detached from the layout widget, then you have to add them outside the layout and manage them yourself, as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout" rel="nofollow noopener">examples in script repository</a>.</p>
<p>We’ve been discussing with <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> about the possibility of improving the layout manager with multi-monitor layouts. The layout manager would be able create additional widgets (maybe in a dockable window), which would be shown on second display (or third, fourth, …). Would this address your needs?</p>

---

## Post #3 by @AndreaRoberti (2019-07-14 18:40 UTC)

<p>Thanks for the quick reply!<br>
Yes, i started to do every single view outside , but I was hoping there was an easier solution with the layout manager. I’ll continue with that !</p>
<p>I’m interested on layout manager improvement, maybe that could help me / us !</p>
<p>Best regards,<br>
Andrea</p>

---

## Post #4 by @lassoan (2019-07-14 18:42 UTC)

<p>You can create your GUI in Qt designer and load the generated .ui file. That way the GUI design is quite effortless, even if you have many widgets.</p>

---

## Post #5 by @AndreaRoberti (2019-07-14 18:55 UTC)

<p>Ye, true!  I’m doing everything with qt designer.</p>
<p>When I saw that there was the possibility of creating everything from the designer, it has speeded me up a lot.<br>
I have experience in qt and pythonqt as well. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I will do a custom widget and a class that handle all the views and i will share it here</p>
<p>Thanks!</p>

---
