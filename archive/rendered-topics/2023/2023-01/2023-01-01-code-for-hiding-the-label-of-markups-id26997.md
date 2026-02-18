# Code for hiding the label of markups

**Topic ID**: 26997
**Date**: 2023-01-01
**URL**: https://discourse.slicer.org/t/code-for-hiding-the-label-of-markups/26997

---

## Post #1 by @WilliamLambert1205 (2023-01-01 05:15 UTC)

<p>Hi,every one,happy new year!<br>
I have a question about how to hide the label of markups.<br>
When I create a bunch of markuplines, it comes out very crowded, so is there any code to only hide the labels and keep the markups exist?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d7d0184edbc32405d2116c074906b8f60f2cc16.png" alt="image" data-base62-sha1="fCzRPAkIGzTlKLYgISaBHM3sHIO" width="273" height="193"></p>

---

## Post #2 by @jamesobutler (2023-01-01 13:50 UTC)

<p>In the Markups module Display section there is an advanced option to toggle control point labels on/off. The Markups module also has a Display option for label size you could utilize.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#display-section" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#display-section</a></p>
<p>To make this change programmatically instead of through the GUI, you can access the point list display node (see below) to access all of the various display options such as label visibility.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties</a></p>

---

## Post #3 by @WilliamLambert1205 (2023-01-01 16:24 UTC)

<p>thank you!<br>
I still wonder how to set Text size to 0 programmatically instead of through the GUI<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8442985b06fd6168c357f82dbc173647c855f47.png" alt="image" data-base62-sha1="szDwURuibPO3jHwtAp0eKEZB00v" width="638" height="69"></p>
<p>But these code below<br>
pointListNode = getNode(“F”)<br>
pointListDisplayNode = pointListNode.GetDisplayNode()<br>
pointListDisplayNode.SetVisibility(False) # Hide all points<br>
pointListDisplayNode.SetVisibility(True) # Show all points<br>
pointListDisplayNode.SetSelectedColor(1,1,0) # Set color to yellow<br>
pointListDisplayNode.SetViewNodeIDs([“vtkMRMLSliceNodeRed”, “vtkMRMLViewNode1”]) # Only show in red slice view and first 3D view<br>
sets both “F” point and label invisible</p>

---

## Post #4 by @jamesobutler (2023-01-01 16:43 UTC)

<p>Text scale information can be retrieved and modified using TextScale and TextProperty of the display node. See the below link to the vtkMRMLMarkupsDisplayNode API information.</p>
<p><a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsDisplayNode.html#ae2d3e600b3cd90e325a4a353e3fb9c2a" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/main/classvtkMRMLMarkupsDisplayNode.html#ae2d3e600b3cd90e325a4a353e3fb9c2a</a></p>

---

## Post #5 by @WilliamLambert1205 (2023-01-02 11:01 UTC)

<p>thank you!<br>
Problem solved, code below.<br>
pointListNode = getNode(“F”)<br>
pointListDisplayNode = pointListNode.GetDisplayNode()<br>
pointListDisplayNode.SetTextScale(0)</p>

---
