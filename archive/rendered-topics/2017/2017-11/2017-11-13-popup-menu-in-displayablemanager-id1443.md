---
topic_id: 1443
title: "Popup Menu In Displayablemanager"
date: 2017-11-13
url: https://discourse.slicer.org/t/1443
---

# Popup menu in displayablemanager

**Topic ID**: 1443
**Date**: 2017-11-13
**URL**: https://discourse.slicer.org/t/popup-menu-in-displayablemanager/1443

---

## Post #1 by @PaulMartinMurphy (2017-11-13 14:30 UTC)

<p>Hi all,</p>
<p>I’m trying to develop a Slicer module in which right clicking within a 2d slice view will generate a popup menu.</p>
<p>I’m implementing this functionality in DisplayableManager. I haven’t found a VTK object that implements a popup menu. Instead, I’ve created a  DisplayableManagerMenu QOBJECT that has some slots that can be called from a QMenu object.</p>
<p>To get this to compile required changing the CMakeLists.txt file to build the MRMLDM library using SlicerMacroBuildModuleWidgets instead of SlicerMacroBuildModuleLogic, so that I can specifiy the DisplayableManagerMenu as an MOC source.</p>
<p>This actually worked, UNTIL I rebuilt the extension from scratch (ie, removed the entirety of the build directory and recompiled). Then I started getting the following error:</p>
<p>“vtkMRMLSliceViewDisplayableManagerFactory (0x55e643f3d890): RegisterDisplayableManager - Test1DisplayableManager is not a displayable manager. Failed to register”</p>
<p>Interestingly, it works just fine when I initially switch from SlicerMacroBuildModuleLogic to SlicerMacroBuildModuleWidgets if I don’t rebuild from scratch in between. Looking into how these two SlicerMacroBuildModule* functions work, they  eventually call SlicerMacroBuildVTKLibrary and SlicerMacroBuildQtLibrary respectively. I get the sense that what I’m trying to do runs contrary to some deep limitation or assumption, since what I seem to need would be a function called “SlicerMacroBuildVTKandQtLibrary”.</p>
<p>I have also tried adding the relevant QT5_WRAP_CPP  into a CMakeLists.txt that uses SlicerMacroBuildModuleLogic, but run into problems when Python tries to wrap the moc_DisplayableManagerMenu.h file since that doesn’t exist. Disabling python wrapping generates the same error as above.</p>
<p>Does anyone have any suggestions about:</p>
<ol>
<li>
<p>What SlicerMacroBuildModuleLogic is doing that gets the DisplayableManager registered correctly that isn’t done by SlicerMacroBuildModuleWidgets?</p>
</li>
<li>
<p>Whether there is a VTK-based alternative to QMenu for generating popup menus?</p>
</li>
<li>
<p>Any example extensions that implement something similar to this?</p>
</li>
</ol>
<p>Thanks,<br>
-Paul</p>

---

## Post #2 by @lassoan (2017-11-13 14:48 UTC)

<p>Displayable managers are VTK objects, they do not depend on Qt, so you won’t be able to use any Qt classes there. However, you can invoke VTK events and you can add observers to VTK events from Qt classes. You should not modify any existing displayable managers, just add your own.</p>
<p>If you want to interact with specific nodes that are displayed in a viewer, then you can add observers to events of that node. For example, you can use the code below to show a menu when user left-clicks on a markup:</p>
<pre><code>menu = qt.QMenu()
a1 = qt.QAction("test", slicer.util.mainWindow())
#a1.connect('triggered()', self.select)
menu.addAction(a1)
a2 = qt.QAction("action", slicer.util.mainWindow())
#a2.connect('triggered()', self.select)
menu.addAction(a2)
a3 = qt.QAction("here", slicer.util.mainWindow())
#a3.connect('triggered()', self.select)
menu.addAction(a3)

@vtk.calldata_type(vtk.VTK_INT)
def markupCallback3(caller, eventId, callData):
  menu.move(qt.QCursor.pos())
  menu.show()

markupsNode = getNode('F')
observerTag = markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointClickedEvent, markupCallback3)
</code></pre>
<p>Note: There is a small bug that makes a menu appear after clicking on the slice view after clicking a markup (<a href="https://github.com/Slicer/VTK/pull/13">https://github.com/Slicer/VTK/pull/13</a>). A fix for it should be integrated soon.</p>

---

## Post #3 by @PaulMartinMurphy (2017-12-11 06:17 UTC)

<p>Thanks Andras, that worked great.</p>
<p>I’m developing in C++ so what I did was:</p>
<ul>
<li>invoke an event on the MRMLNode from within the VTKWidget</li>
<li>set up an observer of the MRMLNode at the Module level</li>
<li>create QMenu subclasses at the Widget level</li>
</ul>
<p>Thanks again,<br>
-Paul</p>

---

## Post #4 by @jcfr (2017-12-11 21:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1443">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A fix for it should be integrated soon.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the fix, it has been merged into upstream VTK.</p>
<p>Also starting with <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26697">r26697</a>, Slicer includes the fix.</p>

---
