# Annotation of two different volumes at the same time

**Topic ID**: 22292
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/annotation-of-two-different-volumes-at-the-same-time/22292

---

## Post #1 by @Karl-Philippe (2022-03-03 18:10 UTC)

<p>Hi,</p>
<p>I’m new to Slicer and was wondering if it’s possible to annotate two different volumes (in a three-by-three view, for example) at the same time for registration purposes? In other words, is it possible to display two different sets of annotation marks in the same layout that only appear on their respective volumes?</p>
<p>Thank you,</p>

---

## Post #2 by @mikebind (2022-03-03 18:52 UTC)

<p>Yes, this is possible. Here are the steps to accomplish this.</p>
<ul>
<li>
<p>Choose “Three over three” layout and put one volume in the upper row and the other in the lower row<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e227fd71adf968510962d4d610e5d9349484c1b3.png" data-download-href="/uploads/short-url/wgFAmDN5t6ak6BxYXFrp4KwiHAv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e227fd71adf968510962d4d610e5d9349484c1b3_2_220x499.png" alt="image" data-base62-sha1="wgFAmDN5t6ak6BxYXFrp4KwiHAv" width="220" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e227fd71adf968510962d4d610e5d9349484c1b3_2_220x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e227fd71adf968510962d4d610e5d9349484c1b3_2_330x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e227fd71adf968510962d4d610e5d9349484c1b3.png 2x" data-dominant-color="CCCECF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">350×794 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Create two markups fiducial nodes (in the most recent versions of Slicer, these have been renamed “Point List”)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/131dfea70987e85be6bbb47736d641448fdbc853.png" alt="image" data-base62-sha1="2J7kN8MFIpRFuFh94Gf3LYtk59x" width="597" height="252"><br>
I called mine “F” and “G”.</p>
</li>
<li>
<p>In the Markups module, select the first node (“F” for me), then expand the “Display” section, and then the “Advanced” section within the “Display” section.  The top entry is “View:” and the default is “All”, which means that points in this point list will appear on all slice and all 3D views.</p>
</li>
<li>
<p>Click the dropdown, and uncheck the bottom row slice views (these are “Red+”, “Green+”, and “Yellow+”).  This will mean that points in “F” are not visible in the bottom row views.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f22163a64020221f7f34120ccabcc28ad11c8bce.jpeg" data-download-href="/uploads/short-url/yxZ5cTfnVUA0btOCmDgMvzf9hv0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f22163a64020221f7f34120ccabcc28ad11c8bce_2_690x488.jpeg" alt="image" data-base62-sha1="yxZ5cTfnVUA0btOCmDgMvzf9hv0" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f22163a64020221f7f34120ccabcc28ad11c8bce_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f22163a64020221f7f34120ccabcc28ad11c8bce_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f22163a64020221f7f34120ccabcc28ad11c8bce_2_1380x976.jpeg 2x" data-dominant-color="959595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×1058 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Do the same for the other point list (“G”).  First select it on the list of nodes at the top, then click the “View:” dropdown, and this time uncheck “Red”, “Green”, and “Yellow”.  This will make “G” points invisible in the top row of slice views.</li>
</ul>
<p>Following these instructions, both sets would be visible in the 3D view when present; if that is not what you want, then you can hide either or both in the 3D view by unchecking “View1” in the “View:” dropdown list.</p>
<p>If you haven’t already, I would recommend taking a look at the “Fiducial Registration Wizard” module from the “SlicerIGT” extension (installable from the Extension Manager). The “Landmark Registration” module included in core Slicer is supposed to do something similar, but I have always found it very difficult to use and not at all intuitive.</p>

---

## Post #3 by @Karl-Philippe (2022-03-08 14:57 UTC)

<p>Thank you very for this very complete anwser! Actually, I am develloping my own scripted module and I am trying to find a way to display the nodes in only specific view ex: Red/Green/Yellow and Red+/Green+/Yellow+ like you did in the last step. Is there a way do that in a python script (accessing slicer.modules.markups.logic() for example)?</p>

---

## Post #4 by @mikebind (2022-03-08 18:52 UTC)

<p>In Slicer, you control how things appear via display nodes.  A MRML node (markups, model, scalar image volume, etc) typically has one associated display node (but can have multiple in order to have different display properties in different views). To control which views display the MRML node according to the properties in the display node, you provide a list of view node IDs to the display node.</p>
<pre><code class="lang-auto">markupName = 'F'  # change to whatever it's called in the Data module
Fnode = slicer.util.getNode(markupName)
dispNode = Fnode.GetDisplayNode()
listOfSlicesToDisplayIn = ['vtkMRMLSliceNodeRed+', 'vtkMRMLSliceNodeGreen+', 'vtkMRMLSliceNodeYellow+']
dispNode.SetViewNodeIDs( listOfSlicesToDisplayIn )
</code></pre>
<p>The slice and view node ID names are easy to guess once you have seen a few, but you can also get a list of all 2D slice node IDs and all 3D view node IDs like this and inspect them:</p>
<pre><code class="lang-auto">sliceNodeIDs = [node.GetID() for node in slicer.util.getNodesByClass('vtkMRMLSliceNode')] # all 2d slice nodes
threeDViewIDs = [node.GetID() for node in slicer.util.getNodesByClass('vtkMRMLViewNode')] # all 3d view nodes
</code></pre>
<p>Perhaps slightly counter-intuitive, if you pass in an empty list to <code>dispNode.SetViewNodeIDs()</code>, the default behavior is that display is in all slices and views rather than in none.  If you don’t want something displayed anywhere, you control that by <code>dispNode.SetVisible(False)</code> rather than by providing an empty list of places to show.</p>

---

## Post #5 by @Karl-Philippe (2022-03-09 16:00 UTC)

<p>Thanks again for your very helpful reply, it worked fine in the slice views.</p>
<p>However, I am also trying to display two different volumes in two different 3D views. I am able to display the rendering of each volume using the following python command (<code>displayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(getNode('VolumeName))</code>) but each volume appears in both 3D windows.</p>
<p>Is there a way to choose in which 3D window a volume rendering will be displayed (for example using <code>slicer.app.layoutManager().threeDWidget(0)</code>)?</p>

---

## Post #6 by @mikebind (2022-03-09 18:52 UTC)

<p>The method is similar, but a bit more complicated with volume rendering because the display nodes are more complex and there are fewer convenience functions.</p>
<pre><code class="lang-auto">volNode = getNode('volumeNameHere')
vrLogic = slicer.modules.volumerendering.logic()
vrDispNode1 = vrLogic.CreateDefaultVolumeRenderingNodes(volNode)
vrDispNode1.SetViewNodeIDs(('vtkMRMLViewNode1')) # show only in first 3D view
vrDispNode2 = vrLogic.CreateVolumeRenderingNode() # to create a second vr display node
slicer.mrmlScene.AddNode(vrDispNode2) # needs to be explicitly added to the scene
volNode.AddAndObserveDisplayNodeID(vrDispNode2.GetID()) # link it to the volume to display
vrDispNode2.SetViewNodeIDs(['vtkMRMLViewNode2']) # show only in second 3D view
vrLogic.UpdateDisplayNodeFromVolumeNode(vrDispNode2, volNode) # this initializes the VolumeProperty
# You can't modify the display properties for the second display node using the GUI; only 
# the first display node is shown when interacting with the GUI. So, if you want to do any 
# modification, you need to figure out how to do it programmatically
</code></pre>
<p>Alternatively, you can clone the volume you want displayed twice, and display the original in one 3D view and the clone in the second 3D view.  That way you can still interactively modify the display settings for each. In this approach you just need to get the volume rendering display node for each and use <code>SetViewNodeIDs</code> to control which view each is shown in.</p>

---

## Post #7 by @Karl-Philippe (2022-03-10 17:01 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> Thank you for this method, it worked.</p>

---
