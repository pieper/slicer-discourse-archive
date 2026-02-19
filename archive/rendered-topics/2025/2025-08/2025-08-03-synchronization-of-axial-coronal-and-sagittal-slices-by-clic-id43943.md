---
topic_id: 43943
title: "Synchronization Of Axial Coronal And Sagittal Slices By Clic"
date: 2025-08-03
url: https://discourse.slicer.org/t/43943
---

# Synchronization of Axial, Coronal, and Sagittal slices by clicking on a pixel from one of the views

**Topic ID**: 43943
**Date**: 2025-08-03
**URL**: https://discourse.slicer.org/t/synchronization-of-axial-coronal-and-sagittal-slices-by-clicking-on-a-pixel-from-one-of-the-views/43943

---

## Post #1 by @shahrokh (2025-08-03 13:00 UTC)

<p>Hello Dear Developers and Users</p>
<p>To draw ROI, it is needed that three views axial, coronal, and sagittal be synchronize together. This means, for example, by clicking on one certain pixel in sagittal slice, the slices shown in axial and coronal display windows also pass through that pixel in orthogonal way.</p>
<p>To activate this synchronization, the commands below must be copy and paste in Python Interactor.</p>
<blockquote>
<p>import slicer</p>
<p>from slicer.util import VTKObservationMixin</p>
<p>import vtk</p>
<p>import numpy as np</p>
<p>class SliceClickUpdater(VTKObservationMixin):</p>
<p>def _<em>init</em>_(self):</p>
<p>VTKObservationMixin._<em>init</em>_(self)</p>
<p># Define slice nodes with their expected orientations</p>
<p>self.sliceNodes = {</p>
<p>“Red”: {“node”: slicer.mrmlScene.GetNodeByID(“vtkMRMLSliceNodeRed”), “orientation”: “Axial”},</p>
<p>“Yellow”: {“node”: slicer.mrmlScene.GetNodeByID(“vtkMRMLSliceNodeYellow”), “orientation”: “Coronal”},</p>
<p>“Green”: {“node”: slicer.mrmlScene.GetNodeByID(“vtkMRMLSliceNodeGreen”), “orientation”: “Sagittal”}</p>
<p>}</p>
<p># Validate slice nodes</p>
<p>for color, info in self.sliceNodes.items():</p>
<p>if info[“node”] is None:</p>
<p>print(f"Error: Slice node for {color} not found in the scene.")</p>
<p>continue</p>
<p># Ensure correct orientation</p>
<p>current_orientation = info[“node”].GetOrientation()</p>
<p>expected_orientation = info[“orientation”]</p>
<p>if current_orientation != expected_orientation:</p>
<p>print(f"Setting {color} slice node orientation to {expected_orientation} (was {current_orientation})")</p>
<p>info[“node”].SetOrientation(expected_orientation)</p>
<p># Ensure slice is visible</p>
<p>info[“node”].SetSliceVisible(1)</p>
<p>info[“node”].SetWidgetVisible(1)</p>
<p># Validate and link volume to slice nodes via composite nodes</p>
<p>self.volumeNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)</p>
<p>if self.volumeNode is None:</p>
<p>print(“Error: No volume node found in the scene. Please load a volume.”)</p>
<p>return</p>
<p>if self.volumeNode.GetImageData() is None:</p>
<p>print(f"Error: Volume node {self.volumeNode.GetName()} has no image data.")</p>
<p>return</p>
<p># Get volume bounds in RAS coordinates</p>
<p>self.volumeBounds = self.getVolumeBounds()</p>
<p># Find composite nodes for each slice view</p>
<p>compositeNodes = slicer.mrmlScene.GetNodesByClass(“vtkMRMLSliceCompositeNode”)</p>
<p>self.compositeNodeMap = {}</p>
<p>for color, info in self.sliceNodes.items():</p>
<p>if info[“node”] is None:</p>
<p>continue</p>
<p>sliceNodeID = info[“node”].GetID()</p>
<p>compositeNode = None</p>
<p>for i in range(compositeNodes.GetNumberOfItems()):</p>
<p>node = compositeNodes.GetItemAsObject(i)</p>
<p>if node.GetLayoutName() == color:</p>
<p>compositeNode = node</p>
<p>break</p>
<p>if compositeNode is None:</p>
<p>print(f"Error: Composite node for {color} slice view not found.")</p>
<p>continue</p>
<p># Link volume to the slice view</p>
<p>print(f"Linking {color} slice node to volume {self.volumeNode.GetName()} via composite node")</p>
<p>compositeNode.SetBackgroundVolumeID(self.volumeNode.GetID())</p>
<p>compositeNode.SetForegroundVolumeID(None) # Ensure no foreground volume interferes</p>
<p>compositeNode.SetLinkedControl(0) # Disable linked control to prevent automatic updates</p>
<p>self.compositeNodeMap[color] = compositeNode</p>
<p># Reset field of view for all slice views</p>
<p>slicer.util.resetSliceViews()</p>
<p># Get the crosshair node</p>
<p>self.crosshairNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLCrosshairNode”)</p>
<p>if self.crosshairNode is None:</p>
<p>print(“Error: Crosshair node not found in the scene.”)</p>
<p>return</p>
<p># Add observers for interaction events on each slice view</p>
<p>for color, info in self.sliceNodes.items():</p>
<p>if info[“node”] is None or color not in self.compositeNodeMap:</p>
<p>continue</p>
<p># Access the render window via the layout manager</p>
<p>layoutManager = slicer.app.layoutManager()</p>
<p>sliceWidget = layoutManager.sliceWidget(color)</p>
<p>if sliceWidget is None:</p>
<p>print(f"Error: Slice widget for {color} not found.")</p>
<p>continue</p>
<p>renderWindow = sliceWidget.sliceView().renderWindow()</p>
<p>interactor = renderWindow.GetInteractor()</p>
<p>if interactor:</p>
<p>self.addObserver(interactor, vtk.vtkCommand.LeftButtonPressEvent, lambda caller, event, c=color: self.onSliceViewClicked(caller, event, c))</p>
<p>print(f"Added click observer for {color} slice view")</p>
<p>print(“SliceClickUpdater initialized successfully.”)</p>
<p>def getVolumeBounds(self):</p>
<p>“”“Get the RAS bounds of the volume.”“”</p>
<p>imageData = self.volumeNode.GetImageData()</p>
<p>if not imageData:</p>
<p>return None</p>
<p># Get volume dimensions and spacing</p>
<p>dimensions = imageData.GetDimensions()</p>
<p>spacing = imageData.GetSpacing()</p>
<p># Get IJK-to-RAS transformation matrix</p>
<p>ijkToRas = vtk.vtkMatrix4x4()</p>
<p>self.volumeNode.GetIJKToRASMatrix(ijkToRas)</p>
<p># Compute bounds in RAS coordinates</p>
<p>rasBounds = [0, 0, 0, 0, 0, 0]</p>
<p>corners = [</p>
<p>[0, 0, 0], [dimensions[0] - 1, 0, 0], [0, dimensions[1] - 1, 0], [dimensions[0] - 1, dimensions[1] - 1, 0],</p>
<p>[0, 0, dimensions[2] - 1], [dimensions[0] - 1, 0, dimensions[2] - 1], [0, dimensions[1] - 1, dimensions[2] - 1], [dimensions[0] - 1, dimensions[1] - 1, dimensions[2] - 1]</p>
<p>]</p>
<p>for corner in corners:</p>
<p>rasPoint = [0, 0, 0, 1]</p>
<p>ijkToRas.MultiplyPoint([corner[0], corner[1], corner[2], 1], rasPoint)</p>
<p>for i in range(3):</p>
<p>rasBounds[2*i] = min(rasBounds[2*i], rasPoint[i])</p>
<p>rasBounds[2*i+1] = max(rasBounds[2*i+1], rasPoint[i])</p>
<p>print(f"Volume RAS bounds: R=[{rasBounds[0]}, {rasBounds[1]}], A=[{rasBounds[2]}, {rasBounds[3]}], S=[{rasBounds[4]}, {rasBounds[5]}]")</p>
<p>return rasBounds</p>
<p>def clampOffset(self, offset, orientation):</p>
<p>“”“Clamp the slice offset to the volume’s bounds.”“”</p>
<p>if not self.volumeBounds:</p>
<p>return offset</p>
<p>rMin, rMax, aMin, aMax, sMin, sMax = self.volumeBounds</p>
<p>if orientation == “Axial”:</p>
<p>return max(sMin, min(sMax, offset)) # S axis for Axial</p>
<p>elif orientation == “Coronal”:</p>
<p>return max(aMin, min(aMax, offset)) # A axis for Coronal</p>
<p>elif orientation == “Sagittal”:</p>
<p># Use -offset to convert R to L (Left = -R in RAS)</p>
<p>lOffset = -offset</p>
<p># Clamp to the negative of R bounds (L = -R)</p>
<p>clamped_offset = max(-rMax, min(-rMin, lOffset))</p>
<p>if lOffset &lt; -rMax or lOffset &gt; -rMin:</p>
<p>center = (-rMax - rMin) / 2</p>
<p>print(f"Invalid L offset {lOffset} (R={offset}) for Sagittal, using center {center}")</p>
<p>return center</p>
<p>return clamped_offset</p>
<p>return offset</p>
<p>def onSliceViewClicked(self, caller, event, color):</p>
<p># Handle left-button click in the specified slice view</p>
<p>print(f"Left-button click detected in {color} slice view")</p>
<p># Get the coordinates of the clicked point in the RAS system</p>
<p>ras = [0, 0, 0]</p>
<p>self.crosshairNode.GetCursorPositionRAS(ras)</p>
<p>r, a, s = ras</p>
<p>print(f"Click at RAS: R={r}, A={a}, S={s}")</p>
<p># Update the other two slice views</p>
<p>for other_color, info in self.sliceNodes.items():</p>
<p>if other_color == color or info[“node”] is None:</p>
<p>continue # Skip the clicked view and any missing nodes</p>
<p>sliceNode = info[“node”]</p>
<p>sliceToRas = sliceNode.GetSliceToRAS()</p>
<p>orientation = sliceNode.GetOrientation()</p>
<p># Set the slice based on RAS coordinates, clamped to volume bounds</p>
<p>if orientation == “Axial”:</p>
<p>clamped_offset = self.clampOffset(s, orientation)</p>
<p>sliceNode.SetSliceOffset(clamped_offset) # S axis for Axial view</p>
<p>print(f"Updated {other_color} (Axial) slice offset to {clamped_offset}")</p>
<p>elif orientation == “Coronal”:</p>
<p>clamped_offset = self.clampOffset(a, orientation)</p>
<p>sliceNode.SetSliceOffset(clamped_offset) # A axis for Coronal view</p>
<p>print(f"Updated {other_color} (Coronal) slice offset to {clamped_offset}")</p>
<p>elif orientation == “Sagittal”:</p>
<p>clamped_offset = self.clampOffset(r, orientation) # Use -R for Sagittal (L = -R)</p>
<p>sliceNode.SetSliceOffset(clamped_offset) # R axis for Sagittal view</p>
<p>print(f"Updated {other_color} (Sagittal) slice offset to {clamped_offset} (L={clamped_offset})")</p>
<p>else:</p>
<p>print(f"Unknown orientation {orientation} for {other_color} slice node")</p>
<p>sliceNode.UpdateMatrices()</p>
<p>sliceNode.SetSliceVisible(1)</p>
<p>sliceNode.SetWidgetVisible(1)</p>
<p>def removeObservers(self):</p>
<p># Remove observers to deactivate the script</p>
<p>for color, info in self.sliceNodes.items():</p>
<p>if info[“node”] is None or color not in self.compositeNodeMap:</p>
<p>continue</p>
<p>layoutManager = slicer.app.layoutManager()</p>
<p>sliceWidget = layoutManager.sliceWidget(color)</p>
<p>if sliceWidget is None:</p>
<p>continue</p>
<p>renderWindow = sliceWidget.sliceView().renderWindow()</p>
<p>interactor = renderWindow.GetInteractor()</p>
<p>if interactor:</p>
<p>self.removeObserver(interactor, vtk.vtkCommand.LeftButtonPressEvent, lambda caller, event, c=color: self.onSliceViewClicked(caller, event, c))</p>
<p>print(“Observers removed.”)</p>
<p># Activate the script</p>
<p>updater = SliceClickUpdater()</p>
<p># To deactivate the script (if needed):</p>
<p># updater.removeObservers()</p>
</blockquote>
<p>After executing these commands, this synchronization of slices will occur.</p>
<p>Also, a clip has been prepared for showing this feature.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1B55jKzVH7my0RiSgLSaC_UrpYqFtcc50/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1B55jKzVH7my0RiSgLSaC_UrpYqFtcc50/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1B55jKzVH7my0RiSgLSaC_UrpYqFtcc50/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1B55jKzVH7my0RiSgLSaC_UrpYqFtcc50/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">ClipSynchronizationAxialCoronalSagittalSlices.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>‌Best regards.</p>
<p>Shahrokh</p>

---

## Post #2 by @mikebind (2025-08-04 18:24 UTC)

<p>If you hold down the Shift key while moving the mouse over a slice view, the other slice views will change to follow the point in such a way that each view contains the point under the mouse.  <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html</a></p>
<p>You can control whether the other slice views center on this point or simply scroll to contain that point without centering in the dropdown menu next to the crosshair icon in the toolbar (choose “Jump slices - centered” or “Jump slices -offset”).</p>

---
