---
topic_id: 21792
title: "Loaded Models Are Sometimes In Different Coordinate System A"
date: 2022-02-03
url: https://discourse.slicer.org/t/21792
---

# Loaded models are sometimes in different coordinate system, and sometimes not. What exactly is going on?

**Topic ID**: 21792
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/loaded-models-are-sometimes-in-different-coordinate-system-and-sometimes-not-what-exactly-is-going-on/21792

---

## Post #1 by @MJJ (2022-02-03 22:30 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior: A model should be loaded into a consistent coordinate system<br>
Actual behavior: When I load some models, it appears to interpret the vertices as being in the RAS coordinate system. And for other models, it appears to use the world coordinates.</p>
<p>For example,</p>
<p>I have .vtu file. I load it up into 3d slicer. The x and y coordinates of all the vertices are flipped. I assume this is because the application is interpretting the vertex values to be in the RAS coordinates. No problem, I just apply a transformation [[-1,0,0,0, 0,-1,0,0, 0,0,1,0, 0,0,0,1]] and all is fine!</p>
<p>However, i have a .ply model too. When I load this model the application uses the actual coordinates of the vertices and it does not appear to be loaded in the RAS coordinate system, so I dont have to apply the transformation above to this model.</p>
<p>Why is there an inconsistency here?</p>
<p>How can I control which coordinate system a model’s vertices are interpreted to be in?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2022-02-03 22:38 UTC)

<p>If you know the model’s coordinate system, when loading expand the dialog box and specify whether it is LPS or RAS and your model should be imported correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d9c81c0b4fdf15a5e8661a0aecd17e22679714b.png" data-download-href="/uploads/short-url/dm7IAju1ytl1wuWRKzFw854XiKn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d9c81c0b4fdf15a5e8661a0aecd17e22679714b_2_690x162.png" alt="image" data-base62-sha1="dm7IAju1ytl1wuWRKzFw854XiKn" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d9c81c0b4fdf15a5e8661a0aecd17e22679714b_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d9c81c0b4fdf15a5e8661a0aecd17e22679714b_2_1035x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d9c81c0b4fdf15a5e8661a0aecd17e22679714b_2_1380x324.png 2x" data-dominant-color="E1EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1477×348 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Inconsistency comes from the lack of standardization in those formats.</p>

---

## Post #3 by @MJJ (2022-02-03 22:44 UTC)

<p>Thank you for the reply. I noticed this dialogue box, and I tested it by importing the same model twice but with the different options (LPS and RAS) chosen. There was no difference (and my model is definitely not symmetric about the x and y axes!)</p>

---

## Post #4 by @MJJ (2022-02-03 22:47 UTC)

<p>For VTU files, it actually works. I see a difference depending on the LPS / RAS option chosen in that dialogue box.</p>
<p>For my .ply file it does not work. There is no difference between RAS and LPS option</p>

---

## Post #5 by @MJJ (2022-02-03 22:48 UTC)

<p>Ok, update:</p>
<p>It must be something weird with this specific .ply file. I just tried another .ply file and it worked…</p>

---

## Post #6 by @MJJ (2022-02-03 22:52 UTC)

<p>Confirmed. The file must have been corrupted somehow. I loaded it up in paraview, and exported it to a new .ply file, and then tried it in slicer, and it works!</p>
<p>My last question on this topic, is how do I do this programtically in python when i load a model?</p>
<p>i’m using slicer.util.loadModel(…) function</p>

---

## Post #7 by @mikebind (2022-02-04 00:35 UTC)

<p>You will need to use the <code>slicer.util.loadNodeFromFile()</code> function and specify this somehow in the <code>properties</code>.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadNodeFromFile" class="inline-onebox">slicer package — 3D Slicer documentation</a></p>
<p><code>slicer.util.loadModel()</code> is a simplified wrapper for <code>loadNodeFromFile()</code> but lacks the ability to pass in properties.  I couldn’t quickly find an example, but perhaps you can follow the code a bit deeper to find out what the property you want is and how to specify it: <a href="https://github.com/Slicer/Slicer/blob/10fc1df859fa094691e2358d6c0b420bce477700/Base/Python/slicer/util.py#L619">https://github.com/Slicer/Slicer/blob/10fc1df859fa094691e2358d6c0b420bce477700/Base/Python/slicer/util.py#L619</a></p>

---

## Post #8 by @MJJ (2022-02-04 00:51 UTC)

<p>I cannot seem to locate it by following the python code.<br>
I’m wondering if it is even possible.</p>
<p>I noticed this noted in one of the files:</p>
<pre><code class="lang-auto">
  /// Coordinate system options
  /// LPS coordinate system is used the most commonly in medical image computing.
  ///   Slicer is moving towards using this coordinate system in all files by default
  ///   (while keep using RAS coordinate system internally).
  /// RAS coordinate system is used in Slicer internally. For many years, Slicer used
  ///   this coordinate system in files that it created, too.
  enum
  {
    CoordinateSystemRAS = 0,
    RAS = 0, ///&lt; for backward compatibility
    CoordinateSystemLPS = 1,
    LPS = 1, ///&lt; for backward compatibility
    CoordinateSystemType_Last
  };
</code></pre>
<p>from:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Libs/MRML/Core/vtkMRMLStorageNode.h">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Libs/MRML/Core/vtkMRMLStorageNode.h" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Libs/MRML/Core/vtkMRMLStorageNode.h" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Libs/MRML/Core/vtkMRMLStorageNode.h</a></h4>


      <pre><code class="lang-h">/*=auto=========================================================================

  Portions (c) Copyright 2005 Brigham and Women's Hospital (BWH) All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Program:   3D Slicer
  Module:    $RCSfile: vtkMRMLStorageNode.h,v $
  Date:      $Date: 2006/03/19 17:12:29 $
  Version:   $Revision: 1.3 $

=========================================================================auto=*/

#ifndef __vtkMRMLStorageNode_h
#define __vtkMRMLStorageNode_h

// MRML includes
#include "vtkMRMLNode.h"
#include "vtkCommand.h"
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Libs/MRML/Core/vtkMRMLStorageNode.h" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @mikebind (2022-02-04 01:14 UTC)

<p>Found it!  Check out here: <a href="https://github.com/Slicer/Slicer/blob/49320e0294eee6b0a471d97664f32aaaf31e5a17/Modules/Loadable/Models/qSlicerModelsReader.cxx#L118">https://github.com/Slicer/Slicer/blob/49320e0294eee6b0a471d97664f32aaaf31e5a17/Modules/Loadable/Models/qSlicerModelsReader.cxx#L118</a></p>
<p>The property is called “coordinateSystem” and the correct value is the integer 0 (for RAS) or 1 (for LPS). For these you could also use a more descriptively named enum.</p>
<p>An example of using properties for a different kind of node can be found here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-file" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>So, properties are given as python dictionaries, where the key is the property name and the value is the property value.</p>

---
