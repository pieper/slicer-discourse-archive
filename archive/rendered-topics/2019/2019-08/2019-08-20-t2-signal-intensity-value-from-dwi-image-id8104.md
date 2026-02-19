---
topic_id: 8104
title: "T2 Signal Intensity Value From Dwi Image"
date: 2019-08-20
url: https://discourse.slicer.org/t/8104
---

# T2 Signal intensity value from DWI image

**Topic ID**: 8104
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/t2-signal-intensity-value-from-dwi-image/8104

---

## Post #1 by @fpsiddiqui91 (2019-08-20 11:50 UTC)

<p>Hello Developers,<br>
I am developing an application for Diffusion weighted imaging. For some mathematical modeling I need the signal intensity value from DWI volume data. I just want to make sure<br>
If I load a DWI volume as dwi and use dwi.GetID(). The resulting array is the signal intensity values or do I need to apply some weighting?</p>
<p>Thank you in Advance.</p>

---

## Post #2 by @ljod (2019-08-20 13:17 UTC)

<p>Hi! The DWI volume will contain both baseline images acquired without diffusion weighting, as well as images with diffusion weighting. The “signal” is often defined as the ratio of a diffusion-weighted to a non-diffusion-weighted image (also called baseline or b=0) at each pixel. Or, the denominator can be the average of the baseline images. You need to see how the signal is defined in the particular equation you are interested in.  You can take a look at the code for diffusion brain masking and also for tensor computation in order to see how the different components of the image are handled according to their b-values.</p>

---

## Post #3 by @fpsiddiqui91 (2019-08-20 13:47 UTC)

<p>Thank you for your response, it helped a lot. I just have one confusion in the data. if I use “dwi.GetID()” It returns my diffusion weighted volume node. I can convert it into an array by using (slicer.util.array).<br>
The returned matrix are integer numbers from 0 to 4506</p>
<p>What exactly these values represents?  is it some kind of weighted signal values?</p>
<p>Thank you so much for your help.</p>

---

## Post #4 by @ljod (2019-08-20 14:15 UTC)

<p>Hi. No the numbers are the scan from the scanner. You have to read more of the code I pointed you to. The “signal” in papers usually refers to a ratio as I described before. You have to calculate this ratio (or the natural log of this ratio) from the actual DWI scan, which is the data from the scanner and includes both baseline and diffusion weighted images, in an order determined by the b values. I can’t tell you what any voxel in your array represents. You have to use the b values to figure this out. Reading other code will be the best way to see examples.</p>

---

## Post #5 by @fpsiddiqui91 (2019-08-20 14:39 UTC)

<p>Thank you so much for your response. I am reading your suggested code right now and it cleared most of my confusions. Thank you for all your suggestions.</p>

---

## Post #6 by @fpsiddiqui91 (2019-08-20 15:33 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> just want to clarify one more thing. how can I access the actual data from the scanner for each voxel? I thought if I use “dwi.GetID()” I can get the actual data from the scanner but apparently its something else.<br>
I understand the the sequence of my data. I can extract diffusion weighted and non diffusion weighted images,what I dont know is the value from the scanner for each voxels.</p>
<p>As you have suggested,I have read the code,  I now have an access of the gradient matrix and b values as well. I just want to get an access of the data from the scanner. Can you please guide me in this regard.</p>
<p>Thanks alot</p>

---

## Post #7 by @ljod (2019-08-20 15:50 UTC)

<p>the data from the scanner is in your image array. However it will be safer to access it using vtk operations to get the correct image component according to the b value and gradient direction of interest. Examples of this are in the masking code here for example:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/f0e2ac96268d0fc836a67bd1514b4cb9483cbc3b/Modules/CLI/DiffusionWeightedVolumeMasking/DiffusionWeightedVolumeMasking.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/f0e2ac96268d0fc836a67bd1514b4cb9483cbc3b/Modules/CLI/DiffusionWeightedVolumeMasking/DiffusionWeightedVolumeMasking.cxx" target="_blank" rel="nofollow noopener">SlicerDMRI/SlicerDMRI/blob/f0e2ac96268d0fc836a67bd1514b4cb9483cbc3b/Modules/CLI/DiffusionWeightedVolumeMasking/DiffusionWeightedVolumeMasking.cxx</a></h4>
<pre><code class="lang-cxx">// MRMLCore includes
#include &lt;vtkMRMLNRRDStorageNode.h&gt;

// vtkTeem includes
#include &lt;Libs/vtkTeem/vtkTeemNRRDReader.h&gt;
#include &lt;Libs/vtkTeem/vtkTeemNRRDWriter.h&gt;

// VTK includes
#include &lt;vtkNew.h&gt;
#include &lt;vtkVersion.h&gt;
#include &lt;vtkPoints.h&gt;
#include &lt;vtkImageCast.h&gt;
#include &lt;vtkImageExtractComponents.h&gt;
#include &lt;vtkImageMedian3D.h&gt;
#include &lt;vtkImageSeedConnectivity.h&gt;
#include &lt;vtkImageThresholdConnectivity.h&gt;
#include &lt;vtkImageWeightedSum.h&gt;

// ITK includes
#include &lt;itkFloatingPointExceptions.h&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/f0e2ac96268d0fc836a67bd1514b4cb9483cbc3b/Modules/CLI/DiffusionWeightedVolumeMasking/DiffusionWeightedVolumeMasking.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>or the tensor creation code<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Libs/vtkDMRI/vtkTeemEstimateDiffusionTensor.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Libs/vtkDMRI/vtkTeemEstimateDiffusionTensor.cxx" target="_blank" rel="nofollow noopener">SlicerDMRI/SlicerDMRI/blob/master/Libs/vtkDMRI/vtkTeemEstimateDiffusionTensor.cxx</a></h4>
<pre><code class="lang-cxx">/*=auto=========================================================================

  Portions (c) Copyright 2005 Brigham and Women's Hospital (BWH) All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Program:   3D Slicer
  Module:    $RCSfile: vtkTeemEstimateDiffusionTensor.cxx,v $
  Date:      $Date: 2007/04/09 08:10:15 $
  Version:   $Revision: 1.3.2.1 $

=========================================================================auto=*/
#include "vtkTeemEstimateDiffusionTensor.h"
#include "vtkInformation.h"
#include "vtkInformationVector.h"
#include "vtkObjectFactory.h"
#include "vtkStreamingDemandDrivenPipeline.h"
#include "vtkPointData.h"
#include "vtkImageData.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Libs/vtkDMRI/vtkTeemEstimateDiffusionTensor.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #8 by @fpsiddiqui91 (2019-08-21 13:44 UTC)

<p>Thank you so much for your response</p>

---
