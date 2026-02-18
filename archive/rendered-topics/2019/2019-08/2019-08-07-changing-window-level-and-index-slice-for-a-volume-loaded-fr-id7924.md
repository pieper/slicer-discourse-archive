# Changing window/level and index slice for a volume loaded from the command line

**Topic ID**: 7924
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/changing-window-level-and-index-slice-for-a-volume-loaded-from-the-command-line/7924

---

## Post #1 by @matt-warkentin (2019-08-07 17:24 UTC)

<p>Hi,</p>
<p>I am trying to write a piece of code that will open the Slicer GUI from the command-line, and load a particular volume, with a chosen window/level, and some fiducials pre-loaded into the scene. The code below partially works, in that it loads the volume and fiducials, but I can’t get the window/level change to work.</p>
<pre><code class="lang-auto">/Applications/Slicer\ 2.app/Contents/MacOS/Slicer \
--python-code "volumeNode = slicer.util.loadVolume('200056.nrrd', returnNode=True); displayNode = volumeNode.GetDisplayNode(); displayNode.AutoWindowLevelOff(); displayNode.SetWindow(1400); displayNode.SetLevel(-500)" \
--point F.fcsv
</code></pre>
<p>Any idea what I need to change to get things working?</p>
<p>Also, I would eventually like to extend this code to also open the volume (DICOM series) to a specific index slice. I found the following code at this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer" rel="nofollow noopener">link</a>:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
red = layoutManager.sliceWidget('Red')
redLogic = red.sliceLogic()
# Print current slice offset position
print(redLogic.GetSliceOffset())
# Change slice position
redLogic.SetSliceOffset(20)
</code></pre>
<p>Is this the correct code to modify to specify a slice for the Slicer GUI to open at?</p>

---

## Post #2 by @matt-warkentin (2019-08-07 23:20 UTC)

<p>I ended up figuring things out, here is what I did, in case it is of use for others…</p>
<p>Basically I was not “getting” the node correctly. Once I did, things worked properly. The code below will open the NRRD volume (200056.nrrd), change to lung windows (1400, -500), navigate to the index slice based on physical space, and add the fiducials.</p>
<p>To convert from slice number to physical space (offset), I took the RAS origin for inferior/superior axis which was -303.15, and “added” the distance to the index slice (index slice number (108) multiplied by the slice thickness (2.0 mm)). The fiducial file was previously saved from a Slicer session whereby I added two fiducials to arbitrary locations for testing purposes.</p>
<pre><code class="lang-auto">/Applications/Slicer\ 2.app/Contents/MacOS/Slicer --python-code "volumeNode = slicer.util.loadVolume('200056.nrrd', returnNode=True); volumeNode = getNode('200056'); displayNode = volumeNode.GetDisplayNode(); displayNode.AutoWindowLevelOff(); displayNode.SetWindow(1400); displayNode.SetLevel(-500); layoutManager = slicer.app.layoutManager(); red = layoutManager.sliceWidget('Red'); redLogic = red.sliceLogic(); redLogic.SetSliceOffset(-87.150)" --pointfile F.fcsv
</code></pre>
<p>The above code was ran in a bash shell on Mac OS.</p>

---

## Post #3 by @lassoan (2019-08-08 01:13 UTC)

<p>You can jump all slice views to a specific physical location using this code snippet:</p>
<pre><code>slicer.modules.markups.logic().JumpSlicesToLocation(mean_Ras[0], mean_Ras[1], mean_Ras[2], True)
</code></pre>
<p>See complete example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates</a></p>
<p>See examples of conversion between volume voxel and physical coordinates here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates</a></p>

---

## Post #4 by @matt-warkentin (2019-08-10 01:28 UTC)

<p>Thanks for the response, <a class="mention" href="/u/lassoan">@lassoan</a>. Is it also possible to open a CT axial view (red) to a location based on the slice number/index, rather than the physical location? For example, open the CT to slice 108, rather than -85.150mm.</p>
<p>Something like this code:</p>
<pre><code class="lang-auto">redLogic.SetSliceOffset(-87.150)
</code></pre>
<p>But for slice number, rather than offset from the origin.</p>

---

## Post #5 by @lassoan (2019-08-10 04:33 UTC)

<p>For most images that are read from DICOM, slices are stacked along the third (K) axis, so “slice number” (more accurately, <em>InstanceNumber (0020,0013)</em>) is often (K + 1) but it can be also (number of slices - K) or something else, because when DICOM readers reconstruct a volume, they don’t keep track of slice numbers and they may flip and interpolate slices (if they are not equally spaced) as needed.</p>
<p>If you need a robust mechanism to find closest slice index corresponding to a position, then you need to read <em>ImagePositionPatient</em> and <em>ImageOrientationPatient</em> tags for all the slices of the image, find the closest slice, and then get <em>InstanceNumber</em> of that slice.</p>
<p>Show DICOM slice number comes up time-to-time as a feature request, so if you implement this mechanism then it would be great if you could contribute it.</p>

---

## Post #6 by @pieper (2019-08-10 16:58 UTC)

<p>Also, FYI, if you load your images via the DICOM module as scalar volumes the <code>DICOM.instanceUIDs</code> attribute of the MRML node will have a list of <code>SOPInstanceUID</code>s in slice order (the <code>k</code> dimension of IJK) so you can use that to look up the <code>InstanceNumber</code>.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/2b25e080bce23609710ad87a82030d3fe01c4286/Modules/Scripted/DataProbe/DataProbeLib/SliceViewAnnotations.py#L572" rel="nofollow noopener">Here’s some code</a> that uses the dicom information for display (this could be extended to show the instance number in the case where the slice orientation corresponds to the acquisition plane)</p>

---
