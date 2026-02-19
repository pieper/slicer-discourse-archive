---
topic_id: 16256
title: "The Python Source Code Of The Transform Module"
date: 2021-02-27
url: https://discourse.slicer.org/t/16256
---

# The Python source code of the Transform module

**Topic ID**: 16256
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/the-python-source-code-of-the-transform-module/16256

---

## Post #1 by @Carl098 (2021-02-27 07:36 UTC)

<p>I would like to ask where the Python source code of the Transform module is, and I want to learn it.</p>

---

## Post #2 by @mau_igna_06 (2021-02-27 12:42 UTC)

<p>I think this is the code of the transforms module:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/f04a007820f29918810c8a668e8ff79bb963b138/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f04a007820f29918810c8a668e8ff79bb963b138/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/f04a007820f29918810c8a668e8ff79bb963b138/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx</a></h4>
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

  This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.
  and was partially funded by NIH grant 3P41RR013218-12S1

==============================================================================*/

</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/f04a007820f29918810c8a668e8ff79bb963b138/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Here you have two links that may be useful for you:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/MRML/Core/vtkMRMLTransformNode.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/MRML/Core/vtkMRMLTransformNode.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/MRML/Core/vtkMRMLTransformNode.cxx</a></h4>
<pre><code class="lang-cxx">/*=auto=========================================================================

Portions (c) Copyright 2005 Brigham and Women's Hospital (BWH) All Rights Reserved.

See COPYRIGHT.txt
or http://www.slicer.org/copyright/copyright.txt for details.

Program:   3D Slicer
Module:    $RCSfile: vtkMRMLTransformNode.cxx,v $
Date:      $Date: 2006/03/17 17:01:53 $
Version:   $Revision: 1.14 $

=========================================================================auto=*/

#include "vtkMRMLTransformNode.h"

// MRML includes
#include "vtkMRMLBSplineTransformNode.h"
#include "vtkMRMLGridTransformNode.h"
#include "vtkMRMLLinearTransformNode.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/08789e8f2224f89206b2d6a49d1d452d4e677994/Libs/MRML/Core/vtkMRMLTransformNode.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLinearTransform.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLinearTransform.cxx" target="_blank" rel="noopener nofollow ugc">Kitware/VTK/blob/master/Common/Transforms/vtkLinearTransform.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkLinearTransform.cxx

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
#include "vtkLinearTransform.h"

#include "vtkDataArray.h"
#include "vtkMath.h"
#include "vtkMatrix4x4.h"
#include "vtkPoints.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/Kitware/VTK/blob/master/Common/Transforms/vtkLinearTransform.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-02-27 13:30 UTC)

<p>Just to clarify, Transforms module is implemented in C++ and Python-wrapped to make it available in Python. Most core modules and low-level features, processing, and GUI widgets are implemented in C++.</p>

---
