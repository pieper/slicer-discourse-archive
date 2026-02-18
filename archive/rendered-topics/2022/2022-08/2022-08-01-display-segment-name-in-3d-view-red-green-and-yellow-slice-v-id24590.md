# Display segment name in 3d View, Red, Green and Yellow Slice views

**Topic ID**: 24590
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/display-segment-name-in-3d-view-red-green-and-yellow-slice-views/24590

---

## Post #1 by @Karthik (2022-08-01 13:00 UTC)

<p>I have segmentation node with multiple segments. When I click on Show3D, they show up in 3D view and also in Red, Yellow and Green slices.</p>
<p>However, when I have many segments, I find it confusing to differentiate them purely based on colour. I want the segment names to be displayed next to the segments in 3D, Red, Yellow and Green slice views. That way, I can relate what the segment is based on its name.</p>
<p>How is it possible to achieve this?<br>
Thanks</p>

---

## Post #2 by @pieper (2022-08-01 18:02 UTC)

<p>The segment name is already displayed in the DataProbe window (lower left).  It could be displayed elsewhere with some programming but usually the DataProbe is enough.</p>

---

## Post #3 by @Karthik (2022-08-02 03:42 UTC)

<p>In order to display the name on the Slice Views and 3D views next to the segmentation, which parts of the code do I have to modify? Do I have to make changes to the Segment Editor module itself?<br>
Do does it have to do with the rendering?</p>

---

## Post #4 by @pieper (2022-08-02 15:17 UTC)

<p>A good place to start would be to look at the <code>DataProbe</code> code and how corner annotations in the Slice Views</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Scripted/DataProbe">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Scripted/DataProbe" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Scripted/DataProbe" target="_blank" rel="noopener">Slicer/Modules/Scripted/DataProbe at a5f75351073ef62fd6198d9480d86c0009d70f9b ·...</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Scripted/DataProbe" target="_blank" rel="noopener">a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Scripted/DataProbe</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing. - Slicer/Modules/Scripted/DataProbe at a5f75351073ef62fd6198d9480d86c0009d70f9b · Slicer/Slicer</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For the 3D view look, for example, at how the orientation marker is handled.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/DisplayableManager/vtkMRMLOrientationMarkerDisplayableManager.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/DisplayableManager/vtkMRMLOrientationMarkerDisplayableManager.cxx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/DisplayableManager/vtkMRMLOrientationMarkerDisplayableManager.cxx" target="_blank" rel="noopener">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/DisplayableManager/vtkMRMLOrientationMarkerDisplayableManager.cxx</a></h4>


      <pre><code class="lang-cxx">/*==============================================================================

  Program: 3D Slicer

  Copyright (c) Kitware Inc.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Andras Lasso, PerkLab, Queen's University.

==============================================================================*/

// MRMLDisplayableManager includes
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/DisplayableManager/vtkMRMLOrientationMarkerDisplayableManager.cxx" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @muratmaga (2022-08-03 04:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="24590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It could be displayed elsewhere with some programming but usually the DataProbe is enough.</p>
</blockquote>
</aside>
<p>İ would second a request to display segment name inside segmentation view, eg when someone hovers over and waits a few seconds.<br>
On remote sessions (eg zoom) data probe is next to impossible to use effectively.</p>

---
