# Load three PET/CTs in a separate window

**Topic ID**: 35551
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/load-three-pet-cts-in-a-separate-window/35551

---

## Post #1 by @rkraaijveld (2024-04-17 08:30 UTC)

<p>Hi!</p>
<p>I am making an extension where I load three CT images into the separate windows (Green, Red and Yellow). If available, I would also like to load the PET scan as foreground. Loading the three CT images is successful, but adding the PET scan does not work yet. Can someone help?</p>
<pre><code class="lang-auto">self.volume0_node = slicer.util.loadVolume(file_path[0]["image"])
        self.volume1_node = slicer.util.loadVolume(file_path[1]["image"])
        self.volume2_node = slicer.util.loadVolume(file_path[2]["image"])

        layoutManager = slicer.app.layoutManager()
        sliceWidget0 = layoutManager.sliceWidget('Red')
        sliceNode0 = sliceWidget0.mrmlSliceNode()
        sliceNode0.SetOrientation('Axial')
        compositeNode0 = sliceWidget0.mrmlSliceCompositeNode()
        compositeNode0.SetBackgroundVolumeID(self.volume0_node.GetID())
        if file_path[0]["PET"]:
            self.pet0_node = slicer.util.loadVolume(file_path[0]["PET"])
            compositeNode0.SetForegroundVolumeID(self.pet0_node.GetID())
            
        

        sliceWidget1 = layoutManager.sliceWidget('Green')
        sliceNode1 = sliceWidget1.mrmlSliceNode()
        sliceNode1.SetOrientation('Axial')
        compositeNode1 = sliceWidget1.mrmlSliceCompositeNode()
        compositeNode1.SetBackgroundVolumeID(self.volume1_node.GetID())
        if file_path[1]["PET"]:
            self.pet1_node = slicer.util.loadVolume(file_path[1]["PET"])
            compositeNode1.SetForegroundVolumeID(self.pet1_node.GetID())
            

        sliceWidget2 = layoutManager.sliceWidget('Yellow')
        sliceNode2 = sliceWidget2.mrmlSliceNode()
        sliceNode2.SetOrientation('Axial')
        compositeNode2 = sliceWidget2.mrmlSliceCompositeNode()
        compositeNode2.SetBackgroundVolumeID(self.volume2_node.GetID())
        if file_path[2]["PET"]:
            self.pet2_node = slicer.util.loadVolume(file_path[2]["PET"])
            compositeNode2.SetForegroundVolumeID(self.pet2_node.GetID())
</code></pre>
<p>I have also tried this:<br>
<code>slicer.util.setSliceViewerLayers(background=self.volume2_node, foreground=self.pet2_node)</code><br>
But then I get the same CT/PET scan for each window.</p>

---

## Post #2 by @pieper (2024-04-17 17:54 UTC)

<p>If you haven’t already you also will need to set the foreground opacity.</p>
<p>(As a side note, to get better debugging advice it’s good to narrow down to a small example that replicates what you are trying to solve and that is easy for anyone to test themselves.  Here for example, if you set up your script to use the SampleData module and you only included the code for one slice view and made it so that anyone could paste the code into their own python console then you may get more helpful responses).</p>

---
