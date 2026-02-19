---
topic_id: 12383
title: "Update Slice Views From Qmrmlnodecombobox"
date: 2020-07-05
url: https://discourse.slicer.org/t/12383
---

# Update slice views from qMRMLNodeComboBox

**Topic ID**: 12383
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/update-slice-views-from-qmrmlnodecombobox/12383

---

## Post #1 by @sogo (2020-07-05 15:20 UTC)

<p>Hi,<br>
My question is, is there a way to display slice views from currently selected Volume in qMRMLNodeComboBox. I have a small loadable module c++ script in which I’m using qMRMLNodeComboBox copied from “volumes” module. The combobox does get populated when adding volumes from “add data” script. I would like the slice views display to get updated with currently selected Volume in combo box. Right now I have to go to “Data” module and click on “show/hide branch node”. Thanks</p>

---

## Post #2 by @lassoan (2020-07-06 05:20 UTC)

<p>See several solutions in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images</a></p>

---

## Post #3 by @sogo (2020-07-07 07:07 UTC)

<p>Hi Lassoan,<br>
Thanks for pointing out, at first I wasn’t if sure if there is c++ based alternative for these scripts but I have figured it out. So I’m using push button to get the volumeNode and displaying it in this way. This is called after we select the volume from qMRMLComboBox and click on push button</p>
<pre><code>qSlicerLayoutManager* layoutManager = getLayout();
  if (layoutManager != NULL) {   
  vtkMRMLVolumeNode* currentVolume = vtkMRMLVolumeNode::SafeDownCast(d-&gt;ActiveVolumeNodeSelector-&gt;currentNode());
  std::array&lt;std::string, 3&gt; color = {"Red", "Yellow", "Green"};
  for(const auto&amp; color : color) {  
  QString Color=QString::fromStdString(color);
  vtkMRMLSliceCompositeNode* compositeNode = layoutManager-&gt;sliceWidget(Color)-&gt;sliceLogic()-&gt;GetSliceCompositeNode();
  compositeNode-&gt;SetBackgroundVolumeID(currentVolume-&gt;GetID());
  compositeNode-&gt;SetForegroundVolumeID(currentVolume-&gt;GetID());
  
  }
  layoutManager-&gt;resetSliceViews();
</code></pre>
<p>Thanks for your help, appreciate it. Closing this thread</p>

---
