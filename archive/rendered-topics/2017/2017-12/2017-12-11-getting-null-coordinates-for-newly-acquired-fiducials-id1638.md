---
topic_id: 1638
title: "Getting Null Coordinates For Newly Acquired Fiducials"
date: 2017-12-11
url: https://discourse.slicer.org/t/1638
---

# Getting null coordinates for newly acquired Fiducials

**Topic ID**: 1638
**Date**: 2017-12-11
**URL**: https://discourse.slicer.org/t/getting-null-coordinates-for-newly-acquired-fiducials/1638

---

## Post #1 by @MichelODU (2017-12-11 18:08 UTC)

<p>Hello,</p>
<p>I am returning to Slicer after several years, and I’m finding that the Fiducials interface does not properly acquire the coordinates the selected point. Everything that I acquire shows RAS coordinates set to 0.0, 0.0, 0.0. Is there something that I need to be doing to acquire proper Landmark coordinates?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3428c4a11f9755a2cb15d322200026c1abc80538.png" data-download-href="/uploads/short-url/7rqaLCGX2a3Lep4HpKTTCVNgyGk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3428c4a11f9755a2cb15d322200026c1abc80538_2_690x408.png" alt="image" data-base62-sha1="7rqaLCGX2a3Lep4HpKTTCVNgyGk" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3428c4a11f9755a2cb15d322200026c1abc80538_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3428c4a11f9755a2cb15d322200026c1abc80538_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3428c4a11f9755a2cb15d322200026c1abc80538_2_1380x816.png 2x" data-dominant-color="7E7F94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×1127 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best wishes</p>
<p>Michel Audette</p>

---

## Post #2 by @lassoan (2017-12-11 18:29 UTC)

<p>“New fiducial” button in the advanced section of Markups module creates a markup in the (0,0,0) position. To create a point in a specific position, click on the “Place fiducial” button on the toolbar then click in a viewer to place it.</p>

---

## Post #3 by @MichelODU (2017-12-11 18:33 UTC)

<p>Hi. I cannot find the Place Fiducial button. Which toolbar do you mean?</p>

---

## Post #4 by @MichelODU (2017-12-11 18:46 UTC)

<p>Never mind. I found it. Thanks for your support.</p>

---

## Post #5 by @jcfr (2017-12-11 18:46 UTC)

<p>This should help illustrate: <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Mouse_Modes">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Mouse_Modes</a></p>

---

## Post #6 by @MichelODU (2017-12-11 20:40 UTC)

<p>Hi again,</p>
<p>I am using the Fiducials to initialize a deformable surface model, and the code for this model seems to operate in voxel coordinates rather than world coordinates. Can you tell me if I can save in the Fiducials in voxel coordinates?</p>
<p>Best wishes,</p>
<p>Michel</p>

---

## Post #7 by @lassoan (2017-12-11 20:56 UTC)

<p>Fiducial positions are displayed and saved in physical coordinates (in mm).</p>

---

## Post #8 by @MichelODU (2017-12-11 21:02 UTC)

<p>Yes, I know. Hence the question. Is there a flag that I can use to save in IJK, or must I get the IJK-RAS transformation from the mrml file?</p>
<p>I was under the impression that saving in IJK format was feasible with a resource flag set somehow.</p>

---

## Post #9 by @lassoan (2017-12-11 21:06 UTC)

<p>Fiducials are not linked to a particular volume, so you cannot save them relative to a particular volume’s IJK coordinate system. I don’t remember this having come up as a need ever, since volumes are defined in physical coordinate system, too.</p>

---

## Post #10 by @MichelODU (2017-12-11 21:12 UTC)

<p>It did come up. I googled " fiducials slicer voxel coordinates". In fact, it came up with my former student Rabia Haq, but she is not providing much in terms of support, so I’m having to redo the same legwork now.</p>

---

## Post #11 by @lassoan (2017-12-11 21:20 UTC)

<p>I guess you’ve found how to get IJK positions from the saved fiducial positions, but if not then let us know.</p>

---

## Post #12 by @MichelODU (2017-12-11 21:23 UTC)

<p>I cannot follow what they did. I need to have a simple solution in just a few lines, not several threads with the keywords I am looking for. I merely pointed them out to show you that the issue has come up before.</p>

---

## Post #13 by @Nicole_Aucoin (2017-12-11 22:03 UTC)

<p>Fiducial points are linked to the volume for which the slice on which<br>
they’ve placed, via<br>
GetNthFiducialAssociatedNodeID</p>
<p>I’d started to work on the Get method for IJK but didn’t finish it - the<br>
use case was for sending it to CLI modules via the storage node.</p>
<p>If you get the RAS to IJK transform of the volume you’re working with and<br>
create a new transform node with that transform, you can place your world/<br>
RAS coordinates fiducial list under it and then harden it to get the IJK<br>
coordinates (or just display them in the Markups module by clicking the<br>
Transformed checkbox).</p>

---

## Post #14 by @lassoan (2017-12-11 22:03 UTC)

<p>What would you like to achieve? Run a Matlab function using inputs provided by Slicer?</p>

---

## Post #15 by @jcfr (2017-12-11 22:13 UTC)

<p>This post is a follow up of <a href="http://slicer-users-archive.65878.n3.nabble.com/convert-fiducials-in-slicer-to-world-coordinates-td4026776.html">http://slicer-users-archive.65878.n3.nabble.com/convert-fiducials-in-slicer-to-world-coordinates-td4026776.html</a></p>
<p><strong>WARNING: This snippets posted below are not production ready and will most likely break in the future</strong></p>
<h3>Fiducial and coordinate system</h3>
<p>It is indeed possible to choose the coordinate system when using the python console (there is not yet a UI to select the output coordinate system). The default is LPS.</p>
<p>Here is a code snipped allowing to save fiducials from the python console.</p>
<pre><code class="lang-python">node = slicer.util.getNode("vtkMRMLMarkupsFiducialNode1")

fileName = "/tmp/markups.fcsv"

io = slicer.app.ioManager()
snode = io.createAndAddDefaultStorageNode(node)
snode.SetFileName(fileName)

fileFormat = io.completeSlicerWritableFileNameSuffix(node)
snode.SetWriteFileFormat(fileFormat)

snode.SetCoordinateSystem(slicer.vtkMRMLMarkupsStorageNode.RAS)

snode.WriteData(node)
</code></pre>
<p><code>IJK</code> is already a valid format, the only “issue” is that the writer doesn’t implement it yet:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/47e5662bf321acb87f15e83d7f3415faeb44f72f/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsFiducialStorageNode.cxx#L517-L530" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/47e5662bf321acb87f15e83d7f3415faeb44f72f/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsFiducialStorageNode.cxx#L517-L530" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/47e5662bf321acb87f15e83d7f3415faeb44f72f/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsFiducialStorageNode.cxx#L517-L530</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="517" style="counter-reset: li-counter 516 ;">
<li>if (this-&gt;GetCoordinateSystem() == vtkMRMLMarkupsFiducialStorageNode::RAS)</li>
<li>  {</li>
<li>  markupsNode-&gt;GetMarkupPoint(i,p,xyz);</li>
<li>  }</li>
<li>else if (this-&gt;GetCoordinateSystem() == vtkMRMLMarkupsFiducialStorageNode::LPS)</li>
<li>  {</li>
<li>  markupsNode-&gt;GetMarkupPointLPS(i,p,xyz);</li>
<li>  }</li>
<li>else if (this-&gt;GetCoordinateSystem() == vtkMRMLMarkupsFiducialStorageNode::IJK)</li>
<li>  {</li>
<li>  // not implemented yet, use RAS</li>
<li>//      markupsNode-&gt;GetMarkupPointIJK(i,p,xyz);</li>
<li>  markupsNode-&gt;GetMarkupPoint(i,p,xyz);</li>
<li>  }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<h3>Exporting fiducial to IJK (aka voxel coordinates): A draft implementation</h3>
<p>If I recall properly, the reason why this is not yet implemented is because the IJKToRAS matrix is associated with the volume and there is no obvious linkage between the volume and the fiducial.</p>
<p>That said, you could do the following:</p>
<pre><code class="lang-python">def exportFiducials(markupNode, outputFileName, outputCoordinates, associatedVolumeNode=None):
  """Export fiducials to `outputFileName` considering the `outputCoordinates`.

  Supported outputCoordinates are `LPS`, `RAS` and `IJK`.

  Specifying `IJK` requires `associatedVolumeNode` to be specified.
  """
  
  # Create temporary node
  savedMarkupNode = slicer.vtkMRMLMarkupsFiducialNode()
  savedMarkupNode.Copy(markupNode)
  
  snode = slicer.vtkMRMLMarkupsFiducialStorageNode()
  snode.SetFileName(outputFileName)
  savedMarkupNode.SetAndObserveStorageNodeID(snode.GetID())
  
  io = slicer.app.ioManager()
  fileFormat = io.completeSlicerWritableFileNameSuffix(markupNode)
  snode.SetWriteFileFormat(fileFormat)
  
  snode.SetCoordinateSystem(outputCoordinates)
  
  if outputCoordinates == slicer.vtkMRMLMarkupsStorageNode.IJK:
  
    if associatedVolumeNode is None: 
      print("Can not save markup node with IJK coordinate system without a valid volume node")
      return
    
    # Get RAStoIJK matrix associated with the volume
    rasToIJK = vtk.vtkMatrix4x4()
    associatedVolumeNode.GetRASToIJKMatrix(rasToIJK)
    
    # Convert from RAS to IJK
    for idx in range(savedMarkupNode.GetNumberOfFiducials()):
      rasCoord = [0.] * 4
      savedMarkupNode.GetNthFiducialWorldCoordinates(idx, rasCoord)
      ijkCoord = [0.] * 4
      rasToIJK.MultiplyPoint(rasCoord, ijkCoord)
      savedMarkupNode.SetNthFiducialWorldCoordinates(idx, ijkCoord)
  
  snode.WriteData(node)


# Prerequisites
# (1) Download MRHead
# (2) Place a fiducial


# Download sampledata
volume = slicer.util.getNode("MRHead")

# Get Markup (aka fiducial)
node = slicer.util.getNode("vtkMRMLMarkupsFiducialNode1")

# Output filename
fileName = "/tmp/markups.fcsv"

exportFiducials(node, fileName, slicer.vtkMRMLMarkupsStorageNode.IJK, volume)
</code></pre>
<p>The file will then indicate <code>CoordinateSystem = 2</code> which correspond to <code>IJK</code></p>
<pre><code class="lang-auto"># Markups fiducial file version = 4.8
# CoordinateSystem = 2
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
vtkMRMLMarkupsFiducialNode_0,-2.1452,-27.7047,-48.6402,0,0,0,1,1,1,0,F-1,,vtkMRMLScalarVolumeNode1
</code></pre>

---

## Post #16 by @MichelODU (2017-12-12 16:16 UTC)

<p>Thanks for your support, gents. Warm wishes, Michel</p>

---

## Post #17 by @Saima (2019-10-29 03:39 UTC)

<p>Hi andras,<br>
Is there a way to convert ijk points to ras world coordinates.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #18 by @lassoan (2019-10-29 12:08 UTC)

<p>See here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates</a></p>

---
