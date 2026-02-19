---
topic_id: 35130
title: "How To Save Segmentation Data As It Appears In Slicer Data P"
date: 2024-03-27
url: https://discourse.slicer.org/t/35130
---

# How to save segmentation data as it appears in slicer data probe?

**Topic ID**: 35130
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/how-to-save-segmentation-data-as-it-appears-in-slicer-data-probe/35130

---

## Post #1 by @naveen_27b (2024-03-27 13:27 UTC)

<p>Hello,  3D Slicer community. I’m want your help with a task I’m trying to do. I’m working with 3D Slicer to segment a brain and I’m interested in exporting this voxelized segmentation.</p>
<p>If there are multiple segments within a scene, I’d like to export this information on a voxel-by-voxel basis. Essentially, I want each voxel at a specific coordinate to include the names of the segments present at that coordinate. This is similar to how the DataProbe displays information about segments and coordinates in 3D Slicer.</p>
<p>Is there a way to achieve this? I appreciate any guidance you can provide. Thank you in advance.</p>

---

## Post #2 by @pieper (2024-03-27 14:38 UTC)

<p>You would need to write some code for this, but you could reuse the DataProbe code so it really wouldn’t be a lot.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbe.py#L126">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbe.py#L126" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbe.py#L126" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbe.py#L126</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="116" style="counter-reset: li-counter 115 ;">
          <li>        postSize = preSize - 3</li>
          <li>        name = name[:preSize] + "..." + name[-postSize:]</li>
          <li>    return name</li>
          <li></li>
          <li>def removeObservers(self):</li>
          <li>    # remove observers and reset</li>
          <li>    if self.CrosshairNode and self.CrosshairNodeObserverTag:</li>
          <li>        self.CrosshairNode.RemoveObserver(self.CrosshairNodeObserverTag)</li>
          <li>    self.CrosshairNodeObserverTag = None</li>
          <li></li>
          <li class="selected">def getPixelString(self, volumeNode, ijk):</li>
          <li>    """Given a volume node, create a human readable</li>
          <li>    string describing the contents</li>
          <li>    """</li>
          <li>    # TODO: the volume nodes should have a way to generate</li>
          <li>    # these strings in a generic way</li>
          <li>    if not volumeNode:</li>
          <li>        return _("No volume")</li>
          <li>    imageData = volumeNode.GetImageData()</li>
          <li>    if not imageData:</li>
          <li>        return _("No Image")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @naveen_27b (2024-03-27 15:51 UTC)

<p>Thanks a ton for the reply. I will try this</p>

---
