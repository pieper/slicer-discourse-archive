---
topic_id: 37149
title: "Selecting Input Nodes In Slicer Rts Segment Comparison"
date: 2024-07-02
url: https://discourse.slicer.org/t/37149
---

# Selecting input nodes in Slicer RT's Segment Comparison

**Topic ID**: 37149
**Date**: 2024-07-02
**URL**: https://discourse.slicer.org/t/selecting-input-nodes-in-slicer-rts-segment-comparison/37149

---

## Post #1 by @zehret (2024-07-02 15:04 UTC)

<p>Hi,</p>
<p>I am trying to use a python script to run the Slicer RT Segment Comparison module. I am able to load the module and create buttons to compute the Hausdorff Distance and DICE metrics. I am struggling to set the structure set and segment for the reference and compare inputs. What is the general form of using python to select these inputs?<br>
Thanks!</p>

---

## Post #2 by @cpinter (2024-07-03 11:53 UTC)

<p>The recommended way is via MRML. The module has a parameter node that you can set up in Python</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h</a></h4>


      <pre><code class="lang-h">/*==============================================================================

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

==============================================================================*/

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It defines all the selections and options. Then you can use this parameter node with the logic functions to do the computation.</p>

---
