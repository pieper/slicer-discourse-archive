---
topic_id: 7936
title: "How To Assign Default Color Table To A Node"
date: 2019-08-08
url: https://discourse.slicer.org/t/7936
---

# How to assign default color table to a node

**Topic ID**: 7936
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/how-to-assign-default-color-table-to-a-node/7936

---

## Post #1 by @Alex_Vergara (2019-08-08 09:48 UTC)

<p>I wonder if this is too trivial for appearing here but I struggle for weeks before realizing that you can easily assign a color table to a node in python</p>
<pre><code class="lang-python"># First access the color table by name, the name is the one that appears in the combobox
PETnodeColor = slicer.util.getFirstNodeByName('PET-Heat')
# Now you get your node display, the node is any vtkMRMLScalarVolumeNode that you have already loaded
displaynode = node.GetScalarVolumeDisplayNode()
# Finally the assignment
displaynode.SetAndObserveColorNodeID(PETnodeColor.GetID())
</code></pre>
<p>This does not even appear in the documentation nor the wiki and is really hard to find</p>

---

## Post #2 by @jamesobutler (2019-08-08 12:38 UTC)

<p>There was an example for setting colormap of a volume in the Slicer script repository. This page has a lot of examples for python scripting.</p>
<p>It was in an example titled “Change window/level (brightness/contrast) or colormap of a volume”.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume</a></p>

---
