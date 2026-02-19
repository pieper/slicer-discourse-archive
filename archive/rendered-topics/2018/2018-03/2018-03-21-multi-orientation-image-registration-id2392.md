---
topic_id: 2392
title: "Multi Orientation Image Registration"
date: 2018-03-21
url: https://discourse.slicer.org/t/2392
---

# Multi Orientation Image Registration

**Topic ID**: 2392
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/multi-orientation-image-registration/2392

---

## Post #1 by @Mustafa (2018-03-21 20:08 UTC)

<p>Hi All,</p>
<p>I have two volumes. One is axial (fixed), the other one is sagittal(moving). I am wondering the behavior of ‘General Registration’, if I give these two volumes as they are.</p>
<p>Does General Registration (BRAINS) extract axial orientation from sagittal and register it into the original axial?<br>
Or, does it perform registration as they are given.</p>
<p>Thanks.<br>
Best,<br>
Mustafa</p>

---

## Post #2 by @lassoan (2018-03-21 21:27 UTC)

<p>Volumes are registered to each other based on the image content, regardless of how the slices are oriented.</p>
<p>“General registration (BAINS)” module usually requires some parameter tuning. I would recommend “General registration (Elastix)” module instead, which usually works well with the default parameter set. It is available in SlicerElastix extension.</p>

---

## Post #3 by @Mustafa (2018-03-22 16:41 UTC)

<p>Hi Andras,</p>
<p>Thank you so much!</p>
<p>We will be working on that.</p>
<p>Best, -Mustafa</p>

---

## Post #4 by @Mustafa (2018-03-22 18:59 UTC)

<pre><code class="lang-nohighlight">**Description: itk::ERROR: RandomCoordinateSampler(000000000303E580): ERROR: in your parameter file you selected**
 **SampleRegionSize[ 2 ] = 50 mm,**

 **while the fixed image size at dim = 2 is 10 voxels or 10 mm.**

 **Please select a smaller SampleRegionSize!**

 **It is recommended to be not larger than 1/3 of the image size in mm.**
</code></pre>
<p>Hi All,</p>
<p>It is a registration problem using Elastix, Monomodel MRI. Error message is copied above in bold.</p>
<p>Where can I modify SampleRegionSize to tackle this error? Well, more significantly can any of us share a manual link that reviews parameter adjusting for registration?</p>
<p>Thanks!</p>
<p>Best,</p>
<p>Mustafa</p>

---

## Post #5 by @lassoan (2018-03-22 20:21 UTC)

<p>I would recommend to use “generic (all)” or “generic rigid (all)” preset for <em>all</em> kind of registration. These worked well for me for any registration problems.</p>
<p>If you choose any other preset then you may need to tune those.</p>

---

## Post #6 by @Mustafa (2018-03-26 13:20 UTC)

<p>Thank you Andras. We are working on that.</p>
<p>Best,</p>
<p>-Mustafa</p>

---

## Post #7 by @Mustafa (2018-03-27 17:43 UTC)

<p>Hi All,</p>
<p>I recall my question that solicits what to do if we have  two stacks that are orthogonal to each other. As Andras mentioned, Slicer does not predict their geometric relation(here orthogonality) and takes them as input as they are. I would like to emphasize that orthogonal slices are severely varied  from each other. If one does not know they are two different orientations of same anatomy in advance, he/she will term sagittal  ‘camel’ and the other  ‘thorn’. Therefore, this is a challenging registration problem.</p>
<p>Essentially I wish to know what I should theoretically do. I afraid this forum may not be the place to ask this question. But if any suggests a work done before in line with my question, I will be glad.</p>
<p>Andras, we are exploring Slicer. Again many thanks for your replies!</p>
<p>Note: <strong>[(1)</strong> Extracting the fixed orientation from the moving orientation, <strong>(2)</strong> let us name it ‘pseudo fixed’, **(3) and  perform registration with the fixed and the pseudo fixed  ] ** comes to my mind, but not sure whether it is a null cheating.</p>
<p>Thanks,</p>
<p>Best,</p>
<p>Mustafa</p>

---

## Post #9 by @lassoan (2018-03-27 19:20 UTC)

<p>Slice orientation is irrelevant. The registration algorithm does not care how the voxels are organized in memory. However, it helps the image registration algorithm if the <em>content</em> of the images are already somewhat aligned when you start the registration process. Initial translation can be often computed automatically (for example aligning center of gravity). However, for a successful registration, initial orientation difference of image <em>content</em> (again, slice orientation does not matter) often needs to be under a few ten degrees.</p>

---
