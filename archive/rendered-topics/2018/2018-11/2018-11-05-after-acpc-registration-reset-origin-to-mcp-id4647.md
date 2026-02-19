---
topic_id: 4647
title: "After Acpc Registration Reset Origin To Mcp"
date: 2018-11-05
url: https://discourse.slicer.org/t/4647
---

# After ACPC registration - reset origin to MCP?

**Topic ID**: 4647
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/after-acpc-registration-reset-origin-to-mcp/4647

---

## Post #1 by @cboulay (2018-11-05 22:11 UTC)

<p>Hello.<br>
What is the recommended way to reset the origin to MCP after doing ACPC transform? So far I’ve been calculating the average coordinates of AC and PC, then creating a Linear Transform that is simply a negative translation of that. I guess there might be a way to do this automatically that I am missing.<br>
Thank you,<br>
Chad</p>

---

## Post #2 by @pieper (2018-11-06 16:47 UTC)

<p>I don’t think there’s any automatic way to do that now, but it sounds like something that could be added to the module:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/CLI/ACPCTransform/ACPCTransform.cxx" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/CLI/ACPCTransform/ACPCTransform.cxx" target="_blank">Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/CLI/ACPCTransform/ACPCTransform.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================

  Program:   Realign Volumes
  Module:    $HeadURL$
  Language:  C++
  Date:      $Date$
  Version:   $Revision$

  Copyright (c) Brigham and Women's Hospital (BWH) All Rights Reserved.

  See License.txt or http://www.slicer.org/copyright/copyright.txt for details.

==========================================================================*/
#include "ACPCTransformCLP.h"
#include "vtkPluginFilterWatcher.h"
#include "vtkPrincipalAxesAlign.h"

// MRML includes
#include &lt;vtkMRMLLinearTransformNode.h&gt;
#include &lt;vtkMRMLScene.h&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/CLI/ACPCTransform/ACPCTransform.cxx" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
