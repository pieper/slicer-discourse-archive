---
topic_id: 2226
title: "Loading Transformation From Matlab Mat File"
date: 2018-03-02
url: https://discourse.slicer.org/t/2226
---

# Loading transformation from Matlab .mat file

**Topic ID**: 2226
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/loading-transformation-from-matlab-mat-file/2226

---

## Post #1 by @Vinny (2018-03-02 11:37 UTC)

<p>Hi,</p>
<p>I tried to load a FSL generated .mat transformation matrix as a transform but the system crashed.  The simple goal is to use the .mat matrix to transform vtk objects into a different imaging space; using 3d Slicer, I envision dragging the vtk objects onto the transform node and hardening the transformation and saving the transformed vtk objects.</p>
<p>Thanks for your help.</p>

---

## Post #2 by @lassoan (2018-03-02 12:32 UTC)

<p>Instead of saving transform in proprietary Matlab <code>mat</code> file format, could you save the transform into ITK transform file format? Slicer can directly read/write ITK transform files.</p>
<p>You can use Slicer’s MatlabBridge extension to run Matlab functions directly from Slicer. See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>
<p>You can also use this Matlab function that writes a linear transformation matrix to an ITK transformation file: <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m">https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m</a></p>

---

## Post #3 by @Vinny (2018-03-02 17:55 UTC)

<p>Thanks Andras.  I believe ITK stores the matrix in LPS format but from what I see in the cli_lineartransformationwrite.m function, there is the option to save transformation matrix in RAS. My images are in RAS so I’m guessing that I’d have to set the transformType to ‘slicer’?</p>

---

## Post #4 by @lassoan (2018-03-02 18:15 UTC)

<p>ITK transform is always stored as LPS. The flag controls if you work in RAS or LPS, so that it converts to/from LPS transforms files accordingly.</p>

---

## Post #5 by @Vinny (2018-03-03 17:01 UTC)

<p>Hi,</p>
<p>I tried to load the FSL generated .mat transformation matrix into Matlab and got the following error message:</p>
<pre><code>&gt;&gt; a = load('affine_ct_mr.mat')
Error using load
Unable to read MAT-file C:\Users\Vinit\Documents\MATLAB\affine_ct_mr.mat. Not a binary MAT-file. Try load -ASCII to read as text.
</code></pre>
<p>So, I had converted the .mat array into a .txt file using FSL and was able to read this into Matlab as a 4x4 array:</p>
<pre><code>&gt;&gt; b = load('affine_ct_mr.txt')

b =

    0.9892    0.0481    0.1165  -13.8786
   -0.0145    0.9642   -0.2878   13.6338
   -0.1213    0.2732    0.9450   12.4001
         0         0         0    1.0000
</code></pre>
<p>When I attempt to run the cli_lineartransformwrite.m function, I get the following error message:</p>
<pre><code>&gt;&gt; cli_lineartransformwrite('affine_ct_mr_slicer', b, 'slicer')
Undefined function or variable 'cli_transformwrite'.

Error in cli_lineartransformwrite (line 31)
cli_transformwrite(outputfilename, allTransforms);</code></pre>

---

## Post #6 by @lassoan (2018-03-03 19:10 UTC)

<aside class="quote no-group quote-modified" data-username="Vinny" data-post="5" data-topic="2226">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vinny/48/7052_2.png" class="avatar"> Vinny:</div>
<blockquote>
<p>Undefined function or variable ‘cli_transformwrite’.</p>
</blockquote>
</aside>
<p>Matlab requires all necessary .m files to be in the current working directory or in the path. Either change the working directory to <code>.../MatlabCommander/commandserver</code> or add this folder to the path in Matlab.</p>
<p>As it seems that you are very new to Matlab, I would advise to spend minimum necessary time with it, and instead focus your efforts on learning Python, which is a much more versatile language, with many more libraries, much larger community, and it is completely open-source and free.</p>

---

## Post #7 by @Vinny (2018-03-03 23:40 UTC)

<p>Actually, I’m modifying my workflow to include doing intermodality registrations directly in 3d Slicer based on our convos.  This way transformations can be directly calculated without requiring an intermediary Matlab step.  I fully agree with what you are saying about Python and open-source.  I’ve been doing my neuroimaging work in Nipy precisely for the reasons of versatility and support; the very same reasons why I’m using 3d Slicer.  Appreciate all your help.</p>

---
