---
topic_id: 12502
title: "Segment Ids When Imported From Label Map"
date: 2020-07-13
url: https://discourse.slicer.org/t/12502
---

# Segment ids when imported from label map

**Topic ID**: 12502
**Date**: 2020-07-13
**URL**: https://discourse.slicer.org/t/segment-ids-when-imported-from-label-map/12502

---

## Post #1 by @Niels (2020-07-13 11:40 UTC)

<p>I have a label map with numbers which I would like to keep when I convert it to a segment but I don’t know if this is possible.</p>
<p>For example i have labels 1,3,5,8 but I think I loose them to segment 0 1 2 and 4.</p>
<p>I have looked-up this function but I don’t know if this is what I need or how it works?</p>
<p>/// Update segmentation from segments in a labelmap node.<br>
/// \param updatedSegmentIDs Defines how label values 1…N are mapped to segment IDs (0…N-1).<br>
static bool ImportLabelmapToSegmentationNode(vtkOrientedImageData* labelmapImage,<br>
vtkMRMLSegmentationNode* segmentationNode, vtkStringArray* updatedSegmentIDs,<br>
vtkGeneralTransform* labelmapToSegmentationTransform=nullptr );</p>

---

## Post #2 by @lassoan (2020-07-14 06:33 UTC)

<p>Probably the easiest is to create a color table (.ctbl) file that contains your segment names. The format is a simple text file that you can create in any text editor:</p>
<pre><code class="lang-nohighlight">0 background 0 0 0 0
1 first 128 174 128 255
2 second 241 214 145 255
3 and_the_last_one 177 122 101 255
</code></pre>
<p>You can use this color table like this:</p>
<ul>
<li>Load this color table into Slicer</li>
<li>Load the labelmap volume into Slicer, in Add data dialog check “Show options” and check “LabelMap” checkbox and select your custom color table</li>
<li>Convert the loaded labelmap volume to segmentation volume by right-clicking on it in Data module</li>
</ul>

---

## Post #3 by @Niels (2020-07-14 19:50 UTC)

<p>Thanks lassoan!</p>
<p>But i still need to understand the ImportLabelmapToSegmentationNode function to get the right ids after import.</p>
<p>If found an alternative way by iterating the Label_1 to Label_N segments and i would like to change their id to somthing else but there is only a function to change a segment name. Not the id.</p>
<p>Do you know how this function works or how i change the ids?</p>
<p>I am working with python</p>

---

## Post #4 by @Niels (2020-07-15 16:18 UTC)

<p>found a useful example here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py</a></h4>
<pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
import logging
from slicer.ScriptedLoadableModule import *
from slicer.util import TESTING_DATA_URL
import vtkSegmentationCore


class SegmentationsModuleTest1(unittest.TestCase):

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
