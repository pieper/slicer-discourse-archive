---
topic_id: 10642
title: "Compute Gradient"
date: 2020-03-11
url: https://discourse.slicer.org/t/10642
---

# Compute Gradient

**Topic ID**: 10642
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/compute-gradient/10642

---

## Post #1 by @loubna (2020-03-11 13:37 UTC)

<p>Hi;</p>
<p>I want to implement a new 3d reconstrcution method, in which I need to know gradient vector of each (i,j,k) voxel. The idea is to convert the binary label map to closed surface. The idea is similar to marching cube.</p>
<p>I know that I must apply vtkImageGradiant followed by VTKProbeFilter to get the gradint vector on each (i,j,k) voxel. But, It is wrong if I apply the vtkGradiantFilter on the LabelMap ( represented by 0 and 1 values). My question how can I recover the really scalar value  of each voxel ( gray value for exemple of the segmented region) in order to apply the gradient filter on it .</p>
<p>I need some ideas, I implement the method in c++</p>

---

## Post #2 by @lassoan (2020-03-11 13:44 UTC)

<p>If you need the gradient to estimate surface normal and you have a binary image then you need to first apply Gaussian smoothing filter on the labelmap.</p>
<p>Make sure that the smoothed results can be represented using the current scalar type and range of label values. For example, if you use int value as scalar type and labelmap values are 0 = background and 1 = foreground then you will get unusable results. You need to have label values of 0 and at least 100 (or use a float scalar type).</p>

---

## Post #3 by @loubna (2020-03-11 13:49 UTC)

<p>I have applied gaussian smoothing filter on the labelMap. Then I have applied the gradient filter on the smoothed image, but the majority of normal vectors are null (0,0,0). I know that is wrong. But I don’t understand how can I make sure that the smoothed results can be represented using the current scalar type and range of labelMap? and how can I get the label values between 0 and 100 for exemple. are there some tests or expressions that i must use</p>

---

## Post #4 by @lassoan (2020-03-11 13:52 UTC)

<p>You can use VTK filters for either rescaling intensity values or casting the image to a different scalar type.</p>

---

## Post #5 by @loubna (2020-03-11 13:55 UTC)

<p>Thank you very much for your help, I can understand now why I have got wrong results</p>

---

## Post #6 by @loubna (2020-03-13 10:20 UTC)

<p>Hi Mr;<br>
I have got good results when I applied vtkImageCast on the labelMap but with SetInputConnection but with SetInputData , I had wrong model . However, SetInputConnection(labelMap) causes an error because in the argument I must add Something like data-&gt;GetOutPourPort() which I can not do with vtkimagedata (labelMap)</p>
<p>the probleme is that setInputdata(labelmap) does not work.<br>
with setInputConnection (labelMap) this is what is displayed (good results)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62feb3256231a8dfb1006f92a99f2ca71a7c074b.jpeg" data-download-href="/uploads/short-url/e7Ku03utcvUttxn4Q2crnAh7Q3F.jpeg?dl=1" title="imgg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62feb3256231a8dfb1006f92a99f2ca71a7c074b_2_690x388.jpeg" alt="imgg" data-base62-sha1="e7Ku03utcvUttxn4Q2crnAh7Q3F" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62feb3256231a8dfb1006f92a99f2ca71a7c074b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62feb3256231a8dfb1006f92a99f2ca71a7c074b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62feb3256231a8dfb1006f92a99f2ca71a7c074b_2_1380x776.jpeg 2x" data-dominant-color="8D909F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imgg</span><span class="informations">1920×1080 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but with setInputdata I have wrong model.</p>

---

## Post #7 by @lassoan (2020-03-14 15:57 UTC)

<p>You have two options for setting input for a VTK filter:</p>
<ul>
<li>use <code>SetInputData</code> with a <code>vtkImageData</code> object as input (may be obtained by calling <code>Update</code> then <code>GetOutput</code> on a filter)</li>
<li>use <code>SetInputConnection</code> with an algorithm output (typically obtained by calling <code>GetOutputPort</code> on a filter)</li>
</ul>

---

## Post #8 by @loubna (2020-03-14 16:11 UTC)

<p>Is exactly what i am doing, I have used SetInputData with vtkImageData but I have not got not good results. however when I have used SetInputConnection with vtkImage Data, I have got like in the Screenshot result. with an error because setInputconnection must not be used with vtkImageData. Is there a solution to convert vtkImageData to an algorithm output without affect data? for exemple I found vtkTrivialProducer, or vtkPassThroughFilter?</p>

---
