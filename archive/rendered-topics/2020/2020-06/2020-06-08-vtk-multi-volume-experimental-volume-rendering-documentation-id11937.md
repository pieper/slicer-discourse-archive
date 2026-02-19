---
topic_id: 11937
title: "Vtk Multi Volume Experimental Volume Rendering Documentation"
date: 2020-06-08
url: https://discourse.slicer.org/t/11937
---

# VTK Multi-Volume (experimental) volume rendering documentation and explanation

**Topic ID**: 11937
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/vtk-multi-volume-experimental-volume-rendering-documentation-and-explanation/11937

---

## Post #1 by @tkuraku (2020-06-08 23:55 UTC)

<p>I like how the rendering option “VTK Multi-Volume (experimental)”. I am having a hard time finding documentation on this option. Can someone point me to the relevant documentation and or explain how one might reproduce this effect using VTK?</p>

---

## Post #2 by @lassoan (2020-06-09 00:06 UTC)

<p>This volume renderer allows volume rendering of any number of overlapping volumes. Since shading is not implemented for this option yet in VTK, it is not usable yet in practice (except the very rare case you don’t need shading).</p>
<p>A few potential funding sources have been already identified and so probably this missing feature will be implemented in less than a year. If you can contribute with funds or volunteer work then you can help make this happen faster.</p>

---

## Post #3 by @tkuraku (2020-06-09 14:35 UTC)

<p>Thanks for the reply. For my specific use case I actually like having shading turned off. Can you point me to the source code or maybe explain how I could turn shading off for volume rendering in VTK?</p>

---

## Post #4 by @cpinter (2020-06-09 14:49 UTC)

<p>The related VTK code is in the displayable manager class:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx</a></h4>
<pre><code class="lang-cxx">/*==============================================================================

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
  and CANARIE.

==============================================================================*/
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you’re only interested in the VTK aspect then I suggest writing on the VTK discourse forum.</p>

---

## Post #5 by @tkuraku (2020-06-09 14:52 UTC)

<p>Great. Thanks. I will take a look.</p>

---

## Post #6 by @lassoan (2020-06-09 16:31 UTC)

<aside class="quote no-group" data-username="tkuraku" data-post="3" data-topic="11937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47774/48.png" class="avatar"> tkuraku:</div>
<blockquote>
<p>how I could turn shading off for volume rendering in VTK</p>
</blockquote>
</aside>
<p>Shading is always turned off for multi-volume rendering (no matter if you enable it on the GUI or not).</p>
<p>Can you tell a bit more about your use case and your needs?</p>

---
