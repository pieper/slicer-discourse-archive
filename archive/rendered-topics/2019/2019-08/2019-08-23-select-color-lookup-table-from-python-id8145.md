---
topic_id: 8145
title: "Select Color Lookup Table From Python"
date: 2019-08-23
url: https://discourse.slicer.org/t/8145
---

# Select color lookup table from python

**Topic ID**: 8145
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/select-color-lookup-table-from-python/8145

---

## Post #1 by @rogertrullo (2019-08-23 09:50 UTC)

<p>Hi,<br>
I am displaying a label image in slicer using this two lines of code</p>
<pre><code>volumeNode = sitkUtils.PushVolumeToSlicer(anno_itk, name='Annotations', className='vtkMRMLLabelMapVolumeNode')
slicer.util.setSliceViewerLayers(background=volumeNode)
</code></pre>
<p>Now the problem is that I want to use a color lookuptable that I already defined as a txt file in the  ColorFiles folder. Is there a way to do this?<br>
I tried this:</p>
<pre><code>bgDisplay = volumeNode.GetDisplayNode()
bgDisplay.SetAndObserveColorNodeID('mylookuptable')
</code></pre>
<p>but it only works with some colors like green, red, etc but not with my own ones.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-08-23 16:49 UTC)

<p>“mylookuptable” does not look like a node ID. You should do something like this:</p>
<pre><code>bgDisplay.SetAndObserveColorNodeID(myColorNode.GetID())</code></pre>

---
