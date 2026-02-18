# Problem in render a volume on import

**Topic ID**: 34428
**Date**: 2024-02-20
**URL**: https://discourse.slicer.org/t/problem-in-render-a-volume-on-import/34428

---

## Post #1 by @calvinsuzuki (2024-02-20 16:03 UTC)

<p>Hey guys, I’ve been trying to do a very simple task on Slicer.</p>
<p>Just to display the rendered model on drag n drop import.</p>
<p>It rarely works, but in most cases I got the error:</p>
<p>Warning: In /work/Stable/Slicer-0/Modules/Loadable/VolumeRendering/Logic/vtkSlicerVolumeRenderingLogic.cxx, line 674<br>
vtkSlicerVolumeRenderingLogic (0x7825480): CopyDisplayToVolumeRenderingDisplayNode: No display node to copy.</p>
<p>I used this on start of my module: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>[ image deleted per request ]</p>

---

## Post #2 by @lassoan (2024-02-20 16:07 UTC)

<p>There have been some recent improvements in volume rendering initilization. Please try with the latest Slicer Preview Release and let us know it the issue persists.</p>

---

## Post #3 by @calvinsuzuki (2024-02-23 16:00 UTC)

<p>Hello Andras! Thanks for reaching out!<br>
I’m currently using the 5.2.2 version, I’ve managed to solve this issue by raising the time value of <code>qt.QTimer.singleShot</code> then dinamically checking if it was loaded and increasing the load time using <code>volRenLogic.SetRecommendedVolumeRenderingProperties(displayNode)</code></p>
<pre><code class="lang-auto">    def showVolumeRendering(self, volumeNode):
        volRenLogic = slicer.modules.volumerendering.logic()

        # Check if node exists, if not create a new one
        displayNode = slicer.mrmlScene.GetFirstNodeByName('VolumeRendering')
        if displayNode is None:
            displayNode = volRenLogic.CreateVolumeRenderingDisplayNode()
            slicer.mrmlScene.AddNode(displayNode)

        # Set recommended volume rendering properties will return False if the
        if not volRenLogic.SetRecommendedVolumeRenderingProperties(displayNode):
            # If already using the largest loading time, print error message and return
            if len(self.loading_time) == 1:
                print('Failed to load volume! Please, drag it manually from Data.')
                return
            # If not, increase the loading time and try again 
            else:
                self.loading_time.pop(0)
                print('Failed to load volume! Increasing loading to ' + str(self.loading_time[0]) + 'ms.')
                qt.QTimer.singleShot(self.loading_time[0], lambda: self.showVolumeRendering(volumeNode))

        # ensure the display node is visible
        displayNode.SetVisibility(True)

        # add the volume to the display node
        volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
        volRenLogic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)

        # update the preset based on the volume scalar range
        scalarRange = volumeNode.GetImageData().GetScalarRange()
        if scalarRange[1]-scalarRange[0] &lt; 1500:
            # Small dynamic range, probably MRI
            displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("MR-Default"))
        else:
            # Larger dynamic range, probably CT
            displayNode.GetVolumePropertyNode().Copy(volRenLogic.GetPresetByName("CT-Chest-Contrast-Enhanced"))
</code></pre>

---
