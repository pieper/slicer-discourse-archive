---
topic_id: 12985
title: "Mrml Node Singleton Behaviour"
date: 2020-08-13
url: https://discourse.slicer.org/t/12985
---

# MRML Node Singleton Behaviour

**Topic ID**: 12985
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/mrml-node-singleton-behaviour/12985

---

## Post #1 by @Samuel_Gerber (2020-08-13 18:38 UTC)

<p>I am trying to use the SetSingletonTag of a MRMLNode to enforce a single node in my scene. The singleton is created at startup of the application.<br>
When loading a scene with the singleton saved, the singleton node behaves as expected. The singleton node at startup is “populated” by the saved state. There is two unexpected behaviors:</p>
<ol>
<li>
<p>When looking at the subject hierarchy there appear two nodes with the same id and name and trying to manipulate, e.g. delete, results in errors such as:<br>
void qSlicerSubjectHierarchyPluginLogic::onNodeAboutToBeRemoved(vtkObject *, vtkObject *) : Failed to access subject hierarchy node</p>
</li>
<li>
<p>Creating another node with different id and setting the same SingletonTag name results in two singletons</p>
</li>
</ol>
<p>(An unrelated third unexpected behaviour is that clearing the scene does not reset the fiducial id counter)</p>
<p>Here is a snippet to reproduce both behaviour:</p>
<pre><code class="lang-python">#Create singleton
sNodeName = slicer.modules.markups.logic().AddNewFiducialNode("Test")
sNode = slicer.util.getNode(sNodeName)
sNode.SetSingletonTag("TestSingleton")
sNode.AddFiducial(0,0,0)
slicer.util.saveScene("./Test.mrb")

#For behaviour 1: Restart slicer here
#For behaviour 2: Clear the scene with
#slicer.mrmlScene.Clear()
#Clearing the scene does not reset the fiducial node id counter. 

sNodeName = slicer.modules.markups.logic().AddNewFiducialNode("Test")
sNode = slicer.util.getNode(sNodeName)
sNode.SetSingletonTag("TestSingleton")
def onPointModified(caller, event): print( "Point Modified")
sNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, onPointModified)
slicer.util.loadScene("./Test.mrb")
</code></pre>

---

## Post #2 by @lassoan (2020-08-13 18:45 UTC)

<p>Thanks for reporting this. Singleton nodes are intended for special, configuration nodes, not for visible data nodes. Nevertheless, subject hierarchy should not report an error. How did you create another node with a different ID?</p>
<p>What you would like to achieve? There may be better, cleaner solution than using singleton nodes.</p>

---

## Post #3 by @Samuel_Gerber (2020-08-13 19:00 UTC)

<p>I am writing a module that can be used to place and display orthopedic hardware.<br>
A simple solution would be to just have individual markup node for each configuration of hardware per patient. However, I want to avoid the user having to select which configuration to view. I.e. up on loading a scene I would like to have one designated markup node that will contain the configuration of hardware and populate the UI /display from this node.<br>
This might be not the typical slicer philosophy but it would probably the expected behaviour for an end user when loading a scene.</p>

---

## Post #4 by @lassoan (2020-08-13 19:11 UTC)

<p>Yes, of course it is not necessary for the user to select a node. The usual solution to this is to have a singleton parameter node that stores user selections. See latest scripted loadable module template for an example.</p>

---

## Post #5 by @Samuel_Gerber (2020-08-16 17:17 UTC)

<p>Thank you for your suggestion.</p>
<p>I ended up using the ReferenceNode mechanism to use a volume node as a “master” and add references to the orthopedic model nodes. Up on selecting a volume the widget checks now if it has the reference nodes associated with the orthopedic models and populates the widget from that.<br>
That seems a pretty clean solution to me but I am all ear for better suggestions.</p>
<p>I am still using the singleton mechanism in a different settings but I don’t need to store the associated node. None the less in above example there still seems to be something misbehaving and I am happy to have a look into it if it would be useful to fix that. I’d also argue that one should not be able to create two singleton’s with the same tag.</p>

---

## Post #6 by @lassoan (2020-08-16 17:27 UTC)

<p>You can create a second singleton node with the same tag but when you “add” it to the scene, then thos second singleton node just overwrites the existing node in the scene and does not get added to the scene. It is possible that the subject hierarchy widget or scene model still gets confused somehow, so it would be great if you can investigate this and propose a fix.</p>

---
