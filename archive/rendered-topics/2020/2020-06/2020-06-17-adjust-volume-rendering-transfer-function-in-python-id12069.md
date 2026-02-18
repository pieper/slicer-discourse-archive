# Adjust volume rendering transfer function in Python

**Topic ID**: 12069
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/adjust-volume-rendering-transfer-function-in-python/12069

---

## Post #1 by @Dootsiie (2020-06-17 12:07 UTC)

<p>Hi,</p>
<p>I tried adjusting the transfer function on a 3D volume by using the lines of code you mentioned here. However, I do not see any difference in the 3D volume. Can you help me out? What I did, is I loaded the volume, visualized it like you did in the example above, and used the following code:</p>
<blockquote>
<p>volRenWidget = slicer.modules.volumerendering.widgetRepresentation()<br>
if volRenWidget is None:<br>
logging.error(‘Failed to access volume rendering module’)<br>
return<br>
# Make sure the proper volume property node is set<br>
volumePropertyNode = displayNode.GetVolumePropertyNode()<br>
if volumePropertyNode is None:<br>
logging.error(‘Failed to access volume properties’)<br>
return<br>
volumePropertyNodeWidget = slicer.util.findChild(volRenWidget, ‘VolumePropertyNodeWidget’)<br>
volumePropertyNodeWidget.setMRMLVolumePropertyNode(volumePropertyNode)<br>
# Adjust the transfer function<br>
volumePropertyNodeWidget.moveAllPoints(x, 0, false)</p>
</blockquote>

---

## Post #2 by @cpinter (2020-06-17 12:27 UTC)

<p>This function works for me, please see it as example:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/cpinter/8a1f71c7eb3ef0ebcaa6c1be6e1c9d4a">
  <header class="source">

      <a href="https://gist.github.com/cpinter/8a1f71c7eb3ef0ebcaa6c1be6e1c9d4a" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/cpinter/8a1f71c7eb3ef0ebcaa6c1be6e1c9d4a" target="_blank" rel="noopener">https://gist.github.com/cpinter/8a1f71c7eb3ef0ebcaa6c1be6e1c9d4a</a></h4>

  <h5>setPresetOffest.py</h5>
  <pre><code class="Python">def setPresetOffset(self, x, y, dontMoveFirstLast, presetsCombobox):
  volRenWidget = slicer.modules.volumerendering.widgetRepresentation()
  if volRenWidget is None:
    logging.error('Failed to access volume rendering module')
    return

  # Make sure the proper volume property node is set
  volumePropertyNode = presetsCombobox.mrmlVolumePropertyNode()
  if volumePropertyNode is None:
    logging.error('Failed to access volume properties')</code></pre>
    This file has been truncated. <a href="https://gist.github.com/cpinter/8a1f71c7eb3ef0ebcaa6c1be6e1c9d4a" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For the record, this is the topic referred to above:</p><aside class="quote quote-modified" data-post="1" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/f1d935/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi developers, 
Using a Python script I am trying to load a volume, set the slice views and also a volume rendering preset. While loading and setting the slice views works out well, the volume rendering always shows up with the default settings and not the targeted preset. Could someone please give me a hint of what’s missing? Is there a way to adjust the preset parameter “shift” in advance? 
Since I am new to Slicer development I would also be happy about any hint of how to  improve the code (i…
  </blockquote>
</aside>


---
