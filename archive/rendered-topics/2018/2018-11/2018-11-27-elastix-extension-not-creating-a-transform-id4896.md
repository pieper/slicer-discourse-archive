---
topic_id: 4896
title: "Elastix Extension Not Creating A Transform"
date: 2018-11-27
url: https://discourse.slicer.org/t/4896
---

# Elastix extension not creating a transform

**Topic ID**: 4896
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/elastix-extension-not-creating-a-transform/4896

---

## Post #1 by @stephan (2018-11-27 21:09 UTC)

<p>System: Win 7 64 bit, Slicer 4.10.0, SlicerElastix extension<br>
Expected behavior: Save Elastix results in transformation<br>
Actual behavior: Transformation is still identity (Linear transform, diag (1,1,1,1)) after running Elastix.</p>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and everybody,</p>
<p>I tried out the Elastix registration extension today but it does not return a registration.<br>
I selected my <strong>moving and fixed volume</strong> (both contrast-enhanced cardiac CTs of a pig at different time-points, differing in size but otherwise similar) and an <strong>output transform</strong> (which I created using Create New Transform as… from the output transform drop-down menu).<br>
The <strong>parameter set</strong> I selected is “3D CT monomodal (lung)”.<br>
I then run Elastix by clicking “Apply”. Elastix runs for almost 1 hour and gives the following output:</p>
<pre><code>Volume registration is started in working directory: C:/Users/M171189/AppData/Local/Temp/Slicer/Elastix/20181127_135854_439
Register volumes...
Generate output...
Error:
</code></pre>
<p>The working directory contains the following files:</p>
<pre><code>\input
    fixed.mha
    moving.mha

\result-transform
    elastix.log

    IterationInfo.0.R0.txt 
    ...
    IterationInfo.2.R4.txt

    TransformParameters.0.R0.txt
    ...
    TransformParameters.2.R4.txt

    result.0.mhd 
    result.0.raw
</code></pre>
<p>However, the transformation newer shows up in Slicer (the output transformation is empty and the “Information” panel in the Transform module states “Transform to parent: Not specified”)</p>
<p>The log file is huge and contains a couple of warnings, but no errors as far as I can see.</p>
<p>As this is my first attempt to use Elastix, I unfortunately have no clue what else I could try.<br>
Any hints and suggestions are appreciated.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #2 by @cpinter (2018-11-27 23:00 UTC)

<p>Is it possible that you did not specify an output volume? Unfortunately computation fails if only an output transform is given but no volume.</p>
<p>I fell into that trap a while ago and reported it as a bug: <a href="https://github.com/lassoan/SlicerElastix/issues/9" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/issues/9</a></p>

---

## Post #3 by @brhoom (2018-11-27 23:14 UTC)

<blockquote>
<p>I unfortunately have no clue what else I could try.<br>
Any hints and suggestions are appreciated.</p>
</blockquote>
<p>what about sharing the huge log file?</p>

---

## Post #4 by @stephan (2018-11-28 00:19 UTC)

<p>You are right, I did not specify an output volume, only a transform. I’ll retry with specifying both tomorrow when I’m back in the office, but it looks like that might have been the problem.<br>
Thank you very much.</p>

---

## Post #5 by @lassoan (2018-11-28 05:20 UTC)

<p>I’ve fixed the <a href="https://github.com/lassoan/SlicerElastix/issues/9" rel="nofollow noopener">issue</a>. If you update SlicerElastix tomorrow or later then you can run the registration without selecting an output volume.</p>

---
