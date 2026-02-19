---
topic_id: 24640
title: "Funtion Or Equation Of Centreline"
date: 2022-08-04
url: https://discourse.slicer.org/t/24640
---

# Funtion or Equation of centreline

**Topic ID**: 24640
**Date**: 2022-08-04
**URL**: https://discourse.slicer.org/t/funtion-or-equation-of-centreline/24640

---

## Post #1 by @mann (2022-08-04 13:31 UTC)

<p>Hi All,</p>
<p>I am using Extract centreline module for creating vessel centreline.</p>
<ol>
<li>Is their any way that I can get the function or equation that used to connect the control points ?</li>
<li>Is there a way to edit/crop the centreline once it is created and update the properties table ?</li>
</ol>
<p>Thank you for the help<br>
Manjunath</p>

---

## Post #2 by @mau_igna_06 (2022-08-04 20:41 UTC)

<p>Hi</p>
<p>For 1.<br>
Here is the code</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/MRML/vtkCurveGenerator.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/MRML/vtkCurveGenerator.cxx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/MRML/vtkCurveGenerator.cxx" target="_blank" rel="noopener">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/MRML/vtkCurveGenerator.cxx</a></h4>


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

  This file was originally developed by Thomas Vaughan, PerkLab, Queen's University.

==============================================================================*/

// Markups MRML includes
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/MRML/vtkCurveGenerator.cxx" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>For 2.<br>
I think there should be a script for that here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/vmtk/vmtk/tree/master/vmtkScripts">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/vmtk/vmtk/tree/master/vmtkScripts" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/vmtk/vmtk/tree/master/vmtkScripts" target="_blank" rel="noopener">vmtk/vmtkScripts at master · vmtk/vmtk</a></h3>

  <p><a href="https://github.com/vmtk/vmtk/tree/master/vmtkScripts" target="_blank" rel="noopener">master/vmtkScripts</a></p>

  <p><span class="label1">the Vascular Modeling Toolkit. Contribute to vmtk/vmtk development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #3 by @mann (2022-08-09 15:35 UTC)

<p>Hi,</p>
<p>Thanks for the reply.<br>
But I am weak on coding side. Can you please tell me how can I use these codes to get things done.</p>
<p>Thanking you again</p>

---

## Post #4 by @mau_igna_06 (2022-08-09 20:57 UTC)

<p>In the second link I posted there should be one script that let’s you extract part of the centerline. You have to search for it reading each script name.</p>
<p>If you don’t find it let me know and I’ll search on Github myself and try to find it</p>

---
