---
topic_id: 11022
title: "Brainsfit Registration Gives Error Number Of Objects 70129 G"
date: 2020-04-06
url: https://discourse.slicer.org/t/11022
---

# BRAINSfit Registration gives error "Number of objects (70129) greater than maximum of output pixel type (65535)"?

**Topic ID**: 11022
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/brainsfit-registration-gives-error-number-of-objects-70129-greater-than-maximum-of-output-pixel-type-65535/11022

---

## Post #1 by @mikebind (2020-04-06 23:39 UTC)

<p>Hello, I am using the BRAINS registration module to try to register two CT images together, and am getting the following error:</p>
<pre><code>General Registration (BRAINS) standard error:

Relabel: exception caught !

itk::ExceptionObject (0000005B8E8F2EC8)

Location: "unknown"

File: d:\d\p\slicer-0-build\itk\modules\segmentation\connectedcomponents\include\itkConnectedComponentImageFilter.hxx

Line: 133

Description: itk::ERROR: ConnectedComponentImageFilter(00000240C5DB4600): Number of objects (70129) greater than maximum of output pixel type (65535).
</code></pre>
<p>I’m not sure what will lead to this error or how to resolve it.  I’m not sure why the registration process is concerned with the maximum of the output pixel type.  In this case, both the moving and the fixed CT images are of type “short”.  In my case, I am just trying to get the transform between the two, so I am not actually even asking for an output transformed image.  Even if I were, it wouldn’t require pixel values outside the range of the untransformed image.  It seems odd that an intermediate image would require so many more possible pixel values.</p>
<p>Any suggestions or insight?  Thanks.</p>

---

## Post #2 by @lassoan (2020-04-07 00:30 UTC)

<p>Maybe ConnectedComponentImageFilter is used for automatic ROI generation. What parameters have you changed from the default? Have you tried if the behavior is the same in latest Slicer preview and stable releases?</p>
<p><a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> do you know why ConnectedComponentImageFilter is used in BRAINS registration?</p>

---

## Post #3 by @mikebind (2020-04-07 00:41 UTC)

<p>I wondered if it might have something to do with something like a “number of bins” for mutual information registration.  I use mostly default parameters.  I sometimes increase or more occasionally decrease the percentage of samples, and often increase the “Remove intensity outliers” to .0005 or .001 because I am usually trying to register two images which differ by primarily by the addition of a small amount of metal hardware.  I use the “useCenterOfHeadAlign” for initialization and am doing only rigid registration. I have tried ROIAUTO, but it has never helped in a case where I was getting this error on NOMASK.</p>
<p>On the theory that the error might be caused by too many different pairings between pixel values in the mutual information, I tried increasing the Median Filter Size from 0,0,0 to 3,3,3, and this did not give an error and registered the two volumes.   So, in the future I’ll try that as well.</p>

---

## Post #4 by @lassoan (2020-04-07 01:33 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="11022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I use the “useCenterOfHeadAlign” for initialization and am doing only rigid registration</p>
</blockquote>
</aside>
<p>That explains it. This method performs simple image analysis to detect the head and uses the center of the head object that it found for initial alignment. Most likely itkConnectedComponentImageFilter is used for getting the largest connected component (the head) and you run into issues because the threshold that produces the head also produces 70219 small islands, which are more than the algorithm expects (it cannot store it in its internal 16-bit labelmap image).</p>
<p>Maybe your image is not actually a head MRI image or it is unusual in some way that makes the head detection algorithm fail (in this case, don’t use this initialization option) or it is very noisy (then application of a noise filter, such as median or Gaussian can help).</p>

---

## Post #5 by @hjmjohnson (2020-04-07 02:06 UTC)

<p>YES!  I’m 99% sure I  fixed this a few days ago.  I am working on a few other cleanups.</p>
<p>This also prompted a recent error message change in ITK to better refect the problem.</p>
<p>The problem is caused by incorrectly using an intermediate datatype of unsigned char that is too small to hold the number of objects.</p>
<p>My plan is to update Slicer’s version of BRAINSTools in the middle of this week (Wed or Thursday).</p>
<p>If you have a test data set, I could confirm that this is fixed at the end of the week.</p>
<p>Hans</p>

---

## Post #6 by @mikebind (2020-04-07 23:35 UTC)

<p>The volumes I have are medical, so I can’t share, but I can test next week to verify.   They are not head MRIs, they are head CTs, though I believe I may have gotten this error when trying to register a head MR to head CT.</p>
<p>Should I not use “useCenterOfHeadAlign” for CT volumes?</p>

---
