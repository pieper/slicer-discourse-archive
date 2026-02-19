---
topic_id: 21815
title: "Subject Hierarchy Throws Error Message When Creating Item In"
date: 2022-02-05
url: https://discourse.slicer.org/t/21815
---

# Subject hierarchy throws error message when creating item in the folder

**Topic ID**: 21815
**Date**: 2022-02-05
**URL**: https://discourse.slicer.org/t/subject-hierarchy-throws-error-message-when-creating-item-in-the-folder/21815

---

## Post #1 by @keri (2022-02-05 21:07 UTC)

<p>Hi,</p>
<p>I noticed that if I try to programmatically create new folder in subject hierarchy and add there a node an error message is sent. Though the node is added to the folder.<br>
The error message:<br>
<strong>GetChildByPositionUnderParent: Failed to find subject hierarchy item under parent Scene at position 2</strong><br>
Here are the steps to reproduce:</p>
<ol>
<li>open the data module (so the subject hierarchy treeview gets initialized);</li>
<li>copy/paste the code below (it creates model node, folder and adds the node to the folder):</li>
</ol>
<pre><code class="lang-python"># Create and set up polydata source
box = vtk.vtkCubeSource()
box.SetXLength(30)
box.SetYLength(20)
box.SetZLength(15)
box.SetCenter(10,20,5)

# Create a model node that displays output of the source
boxNode = slicer.modules.models.logic().AddModel(box.GetOutputPort())

# Adjust display properties
boxNode.GetDisplayNode().SetColor(1,0,0)
boxNode.GetDisplayNode().SetOpacity(0.8)

#-----------------------------------------
# Subject hierarchy part starts
#-----------------------------------------
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
folderID = shNode.CreateFolderItem(shNode.GetSceneItemID(), 'MyFolder')

# On this last step check the log, an error should appear there
shNode.CreateItem(folderID, boxNode)
</code></pre>
<p>By the way there is no such error when I use GUI to create folder and drag/drop the node to the folder.</p>
<p>Tested on Ubuntu 20.04 with Slicer dowloaded from official site 4.13.0-2022-02-02</p>

---

## Post #2 by @cpinter (2022-02-07 14:10 UTC)

<p>Unfortunately subject hierarchy sometimes logs errors that we have been unable to find the root cause for. Since there is no funding for stabilizing infrastructure (and even then, subject hierarchy has become extremely complex by now so it has a low result/effort ratio), we focus on actual bugs that arise during the common use cases. So if your code apparently works well, then I suggest ignoring this specific error.</p>
<p>At the same time, contributions are more than welcome to track down and fix deep infrastructure issues like this one!</p>

---

## Post #3 by @keri (2022-02-07 14:35 UTC)

<p>Thank you, good to know</p>

---
