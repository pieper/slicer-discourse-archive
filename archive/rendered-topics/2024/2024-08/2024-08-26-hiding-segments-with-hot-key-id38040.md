---
topic_id: 38040
title: "Hiding Segments With Hot Key"
date: 2024-08-26
url: https://discourse.slicer.org/t/38040
---

# Hiding segments with hot key

**Topic ID**: 38040
**Date**: 2024-08-26
**URL**: https://discourse.slicer.org/t/hiding-segments-with-hot-key/38040

---

## Post #1 by @gazeofthespark (2024-08-26 21:21 UTC)

<p>I need to “hide” all of my segmentations so that I can see only the volume underneath. I would like to map this to a keyboard shortcut so that I can toggle it on and off swiftly.<br>
So far my attempts have not worked:</p>
<pre><code class="lang-auto">def hide_segment(segmentID):
    segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
    displayNode = segmentationNode.GetDisplayNode()
    displayNode.SetSegmentVisibility(segmentID, False)
</code></pre>

---

## Post #2 by @cpinter (2024-08-27 09:27 UTC)

<p>This hides only one segment. You say you want to hide all your segmentations so this only hides some of that.</p>
<p><code>displayNode.SetVisibility(False)</code> hides a whole segmentation. Or <code>segmentationNode.SetDisplayVisibility(False)</code> the same thing.</p>
<p>To add a shortcut here’s a sample script from the script repository:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts</a></p>
<p>To show/hide you’ll need something like<br>
<code>segmentationNode.SetDisplayVisibility(not segmentationNode.GetDisplayVisibility())</code></p>

---

## Post #3 by @gazeofthespark (2024-10-01 08:46 UTC)

<p>Thank you very much, after some trial and error, I was able to get the desired results: I can now toggle all my segmentations on and off to see the greyscale data underneath, in the 2D viewer using:</p>
<pre><code class="lang-auto">def hide_all_segmentations():
    segmentationNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSegmentationNode')
    segmentationNodes.InitTraversal()
    segmentationNode = segmentationNodes.GetNextItemAsObject()
    while segmentationNode:
        displayNode = segmentationNode.GetDisplayNode()
        if displayNode:
            displayNode.SetVisibility(False)
        segmentationNode = segmentationNodes.GetNextItemAsObject()

def toggle_first_segmentation_visibility():
    segmentationNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSegmentationNode')
    segmentationNodes.InitTraversal()
    segmentationNode = segmentationNodes.GetNextItemAsObject()
    if segmentationNode:
        current_visibility = segmentationNode.GetDisplayVisibility()
        segmentationNode.SetDisplayVisibility(not current_visibility)```
</code></pre>
<p>I now need to figure out how to see multiple “greyscale” volumes at once, in the 2D viewer. The purpose is to load multiple adjacent volumes, view them in the 2D slice viewer, and compare segmentaiton consistencies.<br>
My understanding is that only one volume file can be actively displayed at a time due to the way the software manages rendering. Would using overlays be possible to achieve my goal?</p>
<p>Thank you for your help</p>

---

## Post #4 by @pieper (2024-10-01 12:28 UTC)

<p>One option is to use the CompareVolumes module to see the volumes side by side and linked.  Another option would be to set up the volumes as background in the viewers and set up a hot key to cycle through them with <code>setSliceViewerLayers</code>.</p>

---

## Post #5 by @gazeofthespark (2024-10-02 21:18 UTC)

<p>Thank you for your reply.</p>
<p>When I use the CompareVolumes module the volumes appear side by side, but not spatially congrunet in the way I need.<br>
The volumes and segmentations I am working with  provide a limited, localized perspective of the data. I need to be able to inspect the “greyscale” volume data underneath the coloured segmentations, in the sagittal slice viewer.</p>
<p>Hopefully these images will clarify my goal:</p>
<ol>
<li>
<p>Here I have 7 segmentation mask files, and one “active” volume (the greyscale underneath) in the sagittal slice viewer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f.png" data-download-href="/uploads/short-url/bXrr2AwPdfUsO3d7CUTg8xovbeD.png?dl=1" title="Slicer_help" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_510x500.png" alt="Slicer_help" data-base62-sha1="bXrr2AwPdfUsO3d7CUTg8xovbeD" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_765x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_1020x1000.png 2x" data-dominant-color="24221B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_help</span><span class="informations">1183×1159 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Here I’ve hidden the 5th segmentation mask to inspect the greyscale volume underneath:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932.png" data-download-href="/uploads/short-url/m4aTdeFqjSKYhgf13OBlEUgRJDQ.png?dl=1" title="Slicer_help2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_510x500.png" alt="Slicer_help2" data-base62-sha1="m4aTdeFqjSKYhgf13OBlEUgRJDQ" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_765x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_1020x1000.png 2x" data-dominant-color="24221D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_help2</span><span class="informations">1183×1159 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>To effectively analyze and visualize the changes in the segmentation masks across a broader spatial context, I need to be able to see all 7 of the corresponding greyscale volumes at the same time as I scrub through the slice.</p>

---

## Post #6 by @JASON (2024-10-09 16:55 UTC)

<p>Are these images acquired in patches like this, or were they broken into smaller volumes from a larger image for segmentation performance?  If so, loading the full-scale image for visualization in the slice view would be the easiest path.</p>
<p>Another idea… you could write a script to get the RAS coordinates of where your mouse overlaps the slice view.  Loop through all volumes and set visibility based on if the RAS coordinates of the mouse in the slice view are contained within the bounds of the volume.</p>

---

## Post #7 by @JASON (2024-10-09 16:58 UTC)

<pre><code class="lang-auto"># Function to check if the given RAS coordinates are within the bounds of a volume
def is_ras_within_volume(ras, volumeNode):
    bounds = [0] * 6
    volumeNode.GetRASBounds(bounds)
    return (bounds[0] &lt;= ras[0] &lt;= bounds[1] and
            bounds[2] &lt;= ras[1] &lt;= bounds[3] and
            bounds[4] &lt;= ras[2] &lt;= bounds[5])

# Function to set slice visibility for a given slice view and volume
def set_slice_visibility(volumeNode, isVisible):
    sliceCompositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
    for sliceCompositeNode in sliceCompositeNodes:
        # Set the background or foreground volume in each slice view based on visibility
        if isVisible:
            # If the volume should be visible, set it as the background volume
            sliceCompositeNode.SetBackgroundVolumeID(volumeNode.GetID())
        else:
            # If it should not be visible, clear the background volume ID
            if sliceCompositeNode.GetBackgroundVolumeID() == volumeNode.GetID():
                sliceCompositeNode.SetBackgroundVolumeID(None)

# Function that is triggered when the crosshair position is modified
def onCrosshairPositionModified(observer, eventid):
    ras = [0, 0, 0]
    crosshairNode.GetCursorPositionRAS(ras)
    print(f"Crosshair RAS coordinates: {ras}")

    # Loop through all volumes and set visibility in the slice views based on RAS location
    volumeNodes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
    for volumeNode in volumeNodes:
        isVisible = is_ras_within_volume(ras, volumeNode)
        set_slice_visibility(volumeNode, isVisible)
        print(f"Volume '{volumeNode.GetName()}' slice view visibility set to {isVisible}")

# Add the observer for crosshair position updates and store the observer ID for future removal
crosshairNode = slicer.util.getNode("Crosshair")
observerTag = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onCrosshairPositionModified)

print("Crosshair position tracking and volume slice view visibility update script initialized.")

# To remove the observer, use the following line:
# crosshairNode.RemoveObserver(observerTag)
</code></pre>

---

## Post #8 by @JASON (2024-10-09 17:01 UTC)

<p>Trying to render a composite of multiple volumes to the slice view is an uncommon but interesting use-case. It kind of reminds me of dealing with geospatial data (like Google Earth), where you can load data in patches on demand for the current field of view, but the full dataset can be potentially infinite.</p>

---

## Post #9 by @pieper (2024-10-09 17:02 UTC)

<p>For that kind of data this extension could be useful: <a href="https://github.com/gaoyi/SlicerBigImage" class="inline-onebox">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image computing using 3D Slicer</a></p>

---

## Post #10 by @lassoan (2024-10-10 22:09 UTC)

<p>You can stitch these blocks into a single image before display using the Stitch Volumes module (in Sandbox extension).</p>
<p>Reading these old scrolls (Vesuvius Challenge) has been discussed in this forum before, have a look at it here: <a href="https://discourse.slicer.org/t/crippling-lag-during-segmentation-on-a-strong-computer/37218/19" class="inline-onebox">CRIPPLING LAG during segmentation on a strong computer - #19 by lassoan</a></p>

---
