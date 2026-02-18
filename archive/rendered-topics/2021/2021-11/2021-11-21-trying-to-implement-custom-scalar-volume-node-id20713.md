# Trying to implement custom scalar volume node

**Topic ID**: 20713
**Date**: 2021-11-21
**URL**: https://discourse.slicer.org/t/trying-to-implement-custom-scalar-volume-node/20713

---

## Post #1 by @keri (2021-11-21 16:14 UTC)

<p>Hi,</p>
<p>As I don’t fully understand how custom nodes should be written I describe my progress and probably if someone has an advice I would appreciate.</p>
<p>I’m working on custom node inherited from <code>vtkMRMLScalarVolumeNode</code>.</p>
<p>As an example I use <code>vtkMRMLAstroVolumeNode</code>. I’m able to display my node but it can’t be saved. When I click on <code>Save</code> button I can see my node in the table but in fact the node is not saved (the appropriate file is not created). I guess responsible for that is <code>vtkMRMLCustomStorageNode</code>?</p>
<p>Now I need to add some information to the node (for example the path to the file where the original data resides and the parameters that were applied when data was loaded) that should be seen in <code>Data module -&gt; Node information</code> and also this should be saved when saving the scene (I guess using <code>vtkMRMLDisplayableNode::WriteXML</code>) and read when loading the scene. Is it ok if I add this data to the node <code>Attributes</code>?</p>
<p>To display this information I should reimplement <code>PrintSelf()</code> method (there should not be much problems)</p>
<p>To write/read I should reimplement <code>WriteXML()</code> and <code>ReadXMLAttributes()</code>. Is it the information about my node that should be written to the <code>Scene.mrml</code> file?</p>
<p><a href="https://github.com/tierra-colada/Seismic/tree/main/SeisLoad/MRML" rel="noopener nofollow ugc">My custom node can be found there</a></p>

---

## Post #2 by @keri (2021-11-21 21:42 UTC)

<p>Apparently <code>PrintSelf()</code>, <code>WriteXML()</code> and <code>ReadXMLAttributes()</code> are pretty simple to implement using vtkMRML macros. The task is solved.</p>
<p>The only thins has left to do is to save the binary (scalars) data from node.</p>

---

## Post #3 by @keri (2021-11-22 17:54 UTC)

<p>To fix the issue with saving volume node inherited from <code>vtkMRMLScalarNode</code> I just needed my custom storage node to inherit from <code>vtkMRMLVolumeArchetypeStorageNode</code> instead of more general <code>vtkMRMLStorageNode</code>.</p>
<p>I’m able to save/load custom volumes now</p>

---

## Post #4 by @lassoan (2021-11-22 18:52 UTC)

<p>Volume nodes are quite generic, so most likely you don’t need to create custom variants. If you want to save into a new file format then you need a custom storage node. For storing special display properties you can use custom node attributes in existing volume display node classes, but for some sophisticated features adding a new display node class might be necessary.</p>

---

## Post #5 by @keri (2021-11-22 19:06 UTC)

<p>Yes thank you, for now I just created custom scalar volume and added some information (attributes) that I write to XML file and PrintSelf.</p>
<p>I don’t need to use new file formats and thus I just inherited from VolumeStorage and VolumeDisplay nodes mostly to get experience of registering nodes, get known with read/write functions. I think this will help me to better understand Slicer. My custom storage node and display node works exactly the same way as regular volume storage and volume display nodes</p>

---

## Post #6 by @lassoan (2021-11-22 21:17 UTC)

<p>It can be useful to create this custom node as a learning exercise. If you don’t end up needing anything else than storing custom attributes then you can revert to using a regular scalar volume node and use Get/Set Attribute. All custom attributes are stored in the scene.</p>

---

## Post #7 by @keri (2021-11-22 21:25 UTC)

<p>Have not thought that I can simply add attributes via set attribute, that probably would be enough.</p>

---
