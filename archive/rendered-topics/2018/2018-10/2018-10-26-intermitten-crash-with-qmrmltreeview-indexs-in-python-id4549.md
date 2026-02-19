---
topic_id: 4549
title: "Intermitten Crash With Qmrmltreeview Indexs In Python"
date: 2018-10-26
url: https://discourse.slicer.org/t/4549
---

# Intermitten crash with qMRMLTreeView index's in python

**Topic ID**: 4549
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/intermitten-crash-with-qmrmltreeview-indexs-in-python/4549

---

## Post #1 by @jamesjcook (2018-10-26 20:07 UTC)

<p>I’m working on a custom application that has a qMRMLTreeView in a scripted python module. I’m using this to view models and hierarchies and fibers.</p>
<p>I want to see when users enable/disable a model/hierarchy/fiber, and maybe do something with the mrmlnode.<br>
So I’ve connected the decorationClicked(QModelIndex) signal to a signal handler.</p>
<p>When my signal handler fires, sometimes it generates a crash.</p>
<p>Most frustratingly try/except didn’t catch the exception. It appears that if I could catch the exception that would be close enough for my purposes.<br>
Alternatively any hints on avoiding it would be great.</p>
<p>Here are my more specific details.<br>
I found this crash when getting the mrml node and have now traced it back.<br>
I can replicate the problem when the QModelIndex.data, or the QModelIndex.flags accessors are used. The exact crash is difficult for me to find due to it being buried in qt.<br>
I can mostly reliably replicate the problem using a few models, and a few model hierarchy nodes in the core “Models” module, with slicer nightly 2018-07-12(which my project is derived from).</p>
<p>I don’t know how to create models/model hierarchies programmatically right now, so that part of my testing is manual.<br>
I load up slicer, switch to the models module, and add at least three hierarchy nodes, with at least one nested in the other.<br>
I then load up any two models into the scene, attaching at least one to the deepest hierarchy node.<br>
The crash is most reliable when moving hierarchies around, but simply clicking on the show/hide eye will cause it also. My first thought was some sort of race condition, but adding an arbitrary pause(up to seconds) didn’t resolve the issue in my signal handler.</p>
<p>Models set which should crash</p>
<pre><code>scene
    \HierarchyA
        \HierarchyB
           ModelA
    \HierarchyC
           ModelB
</code></pre>
<p>I run the following code in the slicer python terminal<br>
to find the tree view, and add the signal handler.</p>
<pre><code>import re
import time
def findWidget( widget, objectRegex ):
  name_reg=re.compile(objectRegex)
  if name_reg.match(widget.objectName):
    return widget
  else:
    children = []
    for w in widget.children():
      resulting_widget = findWidget(w, objectRegex)
      if resulting_widget:
        return resulting_widget
  return None

# consider slicer.util.findChild of findChildren instead.

def indexDumper(index):
  treeView.disconnect('decorationClicked(QModelIndex)');
  try:
    # printing index always works... and never crashes.
    # when we crash, none of the prints make it through, have to switch to logging to see them.
    print(index)
    # index is both not none, and marked valid yet it still crashes on accessing data or flags
    if ( index is None ):
        print("error, Index is none!")
    if ( index.IsValid()):
       print("index is valid")
    print("row"+str(index.row()))
    print("col"+str(index.column()))
    print("sizof"+str(index.__sizeof__()))
    # Both index.data, and index.flags can generate a crash here.
    # it is intermittent.
    #print("flags"+str(index.flags()))
    #time.sleep(0.1)
    print("data"+str(index.data()))
  except:
    print("Exception on index access!!!")
    return
  print("full dump complete")
  treeView.connect('decorationClicked(QModelIndex)',indexDumper)
  return

mW=slicer.modules.models.widgetRepresentation()
treeView=findWidget(mW,".*[Mm]odel.*[Tt]ree.*")
t=treeView.connect('decorationClicked(QModelIndex)',indexDumper)

# now click wildly on hierarchy nodes</code></pre>

---

## Post #2 by @lassoan (2018-10-26 21:21 UTC)

<p>I would suggest to use <a href="https://apidocs.slicer.org/v4.8/classqMRMLSubjectHierarchyTreeView.html">subject hierarchy tree widget</a> instead. You can create groups of arbitrary nodes, drag-and-drop is very robust (does not crash), and highly customizable (you can define custom icons, custom context menu items, etc. with plug-ins written in Python or C++).</p>

---

## Post #3 by @jamesjcook (2018-10-26 21:23 UTC)

<p>Thanks for the hint, that looks like it could be a drop in replacement, am I reading that right?</p>

---

## Post #4 by @lassoan (2018-10-26 21:31 UTC)

<p>Yes. You can see it in action in Data module’s subject hierarchy tab.</p>

---

## Post #5 by @jamesjcook (2018-10-31 15:35 UTC)

<p>Thank you for this. I’ve gotten over most of the hurdles of integrating qMRMLSubjectHierarchyView now.</p>
<p>I’ve gotten stuck detecting when the visibility is toggled and cant seem to get past it.</p>
<p>I’ve settled on using the clicked(QModelIndex) signal, and only performing actions when the QModelIndex is the visibilityColumn.<br>
It seems that the QModelIndex returned is for the scene instead of the the expected position in the tree as expected.<br>
This is okay because subjecthierarchy.currentItem() gets the item, and can be used to get the data node.<br>
This works if the object clicked is a leaf node but it doesnt work for branches.</p>
<p>Can you offer any advice on how to tell when branch visibility is toggled?</p>

---

## Post #6 by @cpinter (2018-10-31 15:52 UTC)

<p>Using QModelIndex is quite fragile and I’d advise against it - these indices are not persistent and may change.</p>
<p>If I had to observe visibility changes then I’d observe the Modified event of display node(s). That said I don’t know exactly what changes visibility, so this may not be a good solution.</p>

---

## Post #7 by @jamesjcook (2018-11-02 14:02 UTC)

<p>Thank you both for all the hints. I believe I now have a functional solution. I’ll share it in case anyone tries this in the future.</p>
<p>A simplified overview, when my scripted module sets up, it finds all vtkMRMLModelHierarchyNodes’s,<br>
For any node which has a valid vtkMRMLModelNode, it gets the vtkMRMLModelDisplayNode and adds my custom observer, to watch that displaynode’s modified event. It also adds an attribute to the displaynode so I can find my modelnode. I didn’t see a way to get the modelnode given the displaynode, so there may be room for improvement on that.</p>
<p>Here is my test code which should work when pasted into slicer python terminal.</p>
<pre><code>def modelDisplayModified(mrmlNode,event):
  # hacky event handler for mrmlscene that is fired any time a modeldisplaynode is modified.
  # finds the modelnode using an attribute which was added in setup
  model=slicer.mrmlScene.GetNodeByID(mrmlNode.GetAttribute("vtkMRMLModelNodeID"))
  print(mrmlNode.GetName(),mrmlNode.GetClassName(), model.GetName(),model.GetClassName())
  return

setConnections=True
if setConnections:
  #set connections,
  mrmlNodes=slicer.mrmlScene.GetNodesByClass('vtkMRMLModelHierarchyNode')
  for mn in range(mrmlNodes.GetNumberOfItems()):
    model=mrmlNodes.GetItemAsObject(mn).GetModelNode()
    if model is not None:
      obsNum=model.GetDisplayNode().AddObserver(vtk.vtkCommand.ModifiedEvent, modelDisplayModified )
      model.SetAttribute('mdObserver',str(obsNum))
      model.GetDisplayNode().SetAttribute("vtkMRMLModelNodeID",model.GetID())
else:
  #remove connections,
  mrmlNodes=slicer.mrmlScene.GetNodesByClass('vtkMRMLModelHierarchyNode')
  for mn in range(mrmlNodes.GetNumberOfItems()):
    model=mrmlNodes.GetItemAsObject(mn).GetModelNode()
    if model is not None:
      model.GetDisplayNode().RemoveAttribute("vtkMRMLModelNodeID")
      model.GetDisplayNode().RemoveObserver(int(model.GetAttribute('mdObserver')))
      model.RemoveAttribute('mdObserver')</code></pre>

---

## Post #8 by @lassoan (2018-11-02 15:13 UTC)

<aside class="quote no-group" data-username="jamesjcook" data-post="7" data-topic="4549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesjcook/48/1177_2.png" class="avatar"> jamesjcook:</div>
<blockquote>
<p>I didn’t see a way to get the modelnode given the displaynode</p>
</blockquote>
</aside>
<p>You can use <code>modelNode = modelDisplayNode.GetDisplayableNode()</code>.</p>

---

## Post #9 by @jamesjcook (2018-11-02 17:13 UTC)

<p>That is much cleaner, thank you.</p>

---
