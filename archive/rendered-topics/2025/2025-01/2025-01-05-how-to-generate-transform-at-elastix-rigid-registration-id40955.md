# How to generate transform at Elastix rigid registration

**Topic ID**: 40955
**Date**: 2025-01-05
**URL**: https://discourse.slicer.org/t/how-to-generate-transform-at-elastix-rigid-registration/40955

---

## Post #1 by @Jason_chen (2025-01-05 03:37 UTC)

<p>Hi, I am using 3D slicer to register a CT volume into MR volume and transform node labels on CT into MR coordinates.</p>
<p>Through Elastix in 3D slicer I can do the registration and output the transform to do the job, which is done successfully. However, I want to make that pipeline in Python scripts, with ITK-Elastix to register the volume.</p>
<p>The problem here is that the way to transform the nodes in moving image(CT) into fixed image(MR) with reference to the registration transform parameters is not clear in ITK-Elastix.</p>
<p>So I want to know how this is done in Slicer-Elastix. In another word, how is it done to get a transform matrix from rigid registration result parameters?</p>
<p>If there is any function or algorithm, it is welcomed to introduce.<br>
Thanks a lot!</p>

---

## Post #2 by @muratmaga (2025-01-05 18:09 UTC)

<p>This is more of ITK-Elastix question than Slicer one. Did you look at their repository for documentation: <a href="https://github.com/InsightSoftwareConsortium/ITKElastix" class="inline-onebox" rel="noopener nofollow ugc">GitHub - InsightSoftwareConsortium/ITKElastix: An ITK Python interface to elastix, a toolbox for rigid and nonrigid registration of images</a></p>
<p>Specifically, this example I think shows what you want to do:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITKElastix/blob/main/examples/ITK_Example01_SimpleRegistration.ipynb">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITKElastix/blob/main/examples/ITK_Example01_SimpleRegistration.ipynb" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/ITKElastix/blob/main/examples/ITK_Example01_SimpleRegistration.ipynb" target="_blank" rel="noopener nofollow ugc">InsightSoftwareConsortium/ITKElastix/blob/main/examples/ITK_Example01_SimpleRegistration.ipynb</a></h4>


      <pre><code class="lang-ipynb">{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Simple Elastix"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Registration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
</code></pre>



  This file has been truncated. <a href="https://github.com/InsightSoftwareConsortium/ITKElastix/blob/main/examples/ITK_Example01_SimpleRegistration.ipynb" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Jason_chen (2025-03-05 02:02 UTC)

<p>Thanks for your feedback! Yes, I have reviewed their repository while it did not show how the output parameters of Elastix registration is translated into Slicer transorm which is shown as matrix that can be applied in transforming coordinates. As a result, my problem focused on how to achieve such procedure.</p>

---

## Post #4 by @Elie_Bukuru (2025-03-06 19:18 UTC)

<p>Be kind to your fellow community members.</p>

---

## Post #5 by @muratmaga (2025-03-06 20:07 UTC)

<aside class="quote no-group" data-username="Jason_chen" data-post="3" data-topic="40955">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/71e660/48.png" class="avatar"> Jason_chen:</div>
<blockquote>
<p>Elastix registration is translated into Slicer transorm which is shown as matrix that can be applied in transforming coordinates.</p>
</blockquote>
</aside>
<p>Unfortunately I am not familiar with elastix that much. SlicerElastix is a python module, you can open the source code and review how they are doing it.</p>

---
