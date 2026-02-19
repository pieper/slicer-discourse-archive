---
topic_id: 5410
title: "How To Use The Command Code Of Extractskeleton"
date: 2019-01-18
url: https://discourse.slicer.org/t/5410
---

# How to use the command code of ExtractSkeleton

**Topic ID**: 5410
**Date**: 2019-01-18
**URL**: https://discourse.slicer.org/t/how-to-use-the-command-code-of-extractskeleton/5410

---

## Post #1 by @timeanddoctor (2019-01-18 03:54 UTC)

<p>I went calculat a skeleton by input a script for a label, then I read the code of Slicer/Modules/CLI/ExtractSkeleton/.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ExtractSkeleton/SkelGraph.h">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ExtractSkeleton/SkelGraph.h" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ExtractSkeleton/SkelGraph.h" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/CLI/ExtractSkeleton/SkelGraph.h</a></h4>


      <pre><code class="lang-h">/*=========================================================================

  Program:   Extract Skeleton
  Module:    $HeadURL$
  Language:  C++
  Date:      $Date$
  Version:   $Revision$

  Copyright (c) Brigham and Women's Hospital (BWH) All Rights Reserved.

  See License.txt or http://www.slicer.org/copyright/copyright.txt for details.

==========================================================================*/
#ifndef _SKEL_GRAPH_H_
#define _SKEL_GRAPH_H_

#include &lt;deque&gt;
#include &lt;list&gt;
#include "coordTypes.h"

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ExtractSkeleton/SkelGraph.h" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code>void ExtractSkeletalGraph(const unsigned char *image, const int dim[3]);
</code></pre>
<p>// Extract maximal path between 2 points in the m_Graph<br>
void FindMaximalPath();</p>
<p>// Sample points along the maximal path.<br>
// requestedNumberOfPoints is an approximate number of points to be returned.<br>
void SampleAlongMaximalPath(int requestedNumberOfPoints, std::deque &amp;axis_points);</p>
<p>I used <code>slicer.modules.ExtractSkeleton.ExtractSkeletalGraph(label-1,3)</code>,but slicer tell me couldnot found module “ExtractSkeleton”.</p>
<p>If I went run extractskeleton like the follow pictrue, which codes I should write?<br>
Thanks.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5ddff09f26f96015328659074ea9dae012c3f5ea.jpeg" alt="360%E6%88%AA%E5%9B%BE-233030281" data-base62-sha1="dosc16u7l8gstyAsyrDOshooxjI" width="490" height="288"></p>

---

## Post #2 by @lassoan (2019-01-18 04:44 UTC)

<p>Type <code>slicer.modules.extractskeleton</code> in the Python console and you’ll see that object type is <code>qSlicerCLIModule</code>, which means that it is a CLI module. See how to run CLI modules from Python <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">here</a>.</p>

---
