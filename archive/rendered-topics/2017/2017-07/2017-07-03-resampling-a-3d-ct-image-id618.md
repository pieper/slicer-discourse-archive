---
topic_id: 618
title: "Resampling A 3D Ct Image"
date: 2017-07-03
url: https://discourse.slicer.org/t/618
---

# Resampling a 3D CT Image

**Topic ID**: 618
**Date**: 2017-07-03
**URL**: https://discourse.slicer.org/t/resampling-a-3d-ct-image/618

---

## Post #1 by @Ivan_Hidrovo (2017-07-03 17:10 UTC)

<p>Hello,</p>
<p>Can someone please inform me what module I need to use if I want to downsample a 3D CT image of dimensions 592X 592X 560 to be of dimensions 236X 236X 224 ?</p>
<p>Thank you,<br>
Ivan</p>

---

## Post #2 by @pieper (2017-07-03 19:06 UTC)

<p>Hi Ivan -</p>
<p>Probably the easiest is to figure out what spacing you need and then use the Resample Scalar Volume module.  You need to multiply the current sizes by the spacing in each dimension and then divide by the desired size in each dimension to get the resampling spacing needed.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Ivan_Hidrovo (2017-07-03 19:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thank you for your response.However, I used  the resample image (BRAINS) module and it worked pretty nicely. All you need is a reference image to define the new resolution, and it also let me choose the interpolation method.</p>

---

## Post #4 by @Lorensen (2017-07-03 20:39 UTC)

<p>I wrote this a long time ago…<br>
<a href="https://itk.org/Wiki/ITK/Examples/DICOM/ResampleDICOM" class="onebox" target="_blank" rel="nofollow noopener">https://itk.org/Wiki/ITK/Examples/DICOM/ResampleDICOM</a></p>

---

## Post #5 by @arumiat (2018-04-09 15:46 UTC)

<p>I can’t figure out how to do this from the written description. Could I trouble you to run through a calculation with me.</p>
<p>My images are 720 x 720px and 1871 images ‘long’ (with a slice thickness of 2mm).</p>
<p>If I wanted to <em>halve</em> the number of images in the length (z-axis) which I think is equivalent to doubling the slice thickness, what is current size I need to multiply (for the z-axis?)</p>

---

## Post #6 by @pieper (2018-04-09 16:01 UTC)

<p>Yes, if you double the spacing you’ll get half the number of slices.</p>
<p>If you want N slices, then the spacing needs to be <code>1871 * 2mm / N</code></p>

---

## Post #7 by @arumiat (2018-04-09 16:11 UTC)

<p>Thanks Steve, so</p>
<p>1871*2 = 3742<br>
I want half the number of z-slices (rounds up to 936)<br>
So 3742/936 = 4</p>
<p>So in the resample scalar volume module I use (0,0,4)?</p>

---

## Post #8 by @pieper (2018-04-09 16:57 UTC)

<p>Yes, except you want to use the current spacing for the first two numbers so the number of rows and columns stays the same.</p>

---

## Post #9 by @lassoan (2018-04-09 18:26 UTC)

<p>I would recommend <code>Crop volume</code> module. It allows cropping and adds many convenience features around resampling. For example, you can preview the output image size in <code>Volume information</code> section.</p>
<p>By the way, why do you need exactly 236 x 236 x 224 size? Do you need to match your volume’s geometry (size, origin, spacing, axis directions) to another volume’s geometry?</p>

---

## Post #10 by @arumiat (2018-04-10 10:20 UTC)

<p>By current spacing 720x720px so (720, 720, 4) ?</p>
<hr>
<p>Hi Andras, I don’t need an exact output size, I’m just trying to work on getting my volume down to a smaller size so I can serve it across the internet. (<a href="https://discourse.slicer.org/t/working-with-large-datasets/2469/11">Working with large datasets</a>)</p>
<p>One method I haven’t tried yet which would I imagine help a lot is reducing the number of images in the z-plane, hence the above discussion.</p>
<p>So in summary my overall pipeline is to</p>
<ol>
<li>reduce number of images in the z-plane using above method</li>
<li>crop the volume to just the region of interest</li>
<li>rescale images to a more reasonable size (around 256x256 or 300x300 px)</li>
<li>save as nrrd or mrda</li>
</ol>
<p>and see where that gets me =)<br>
PS I didn’t realise crop volume could also resize, any tutorials on using?</p>

---

## Post #11 by @pieper (2018-04-10 11:40 UTC)

<aside class="quote no-group" data-username="arumiat" data-post="10" data-topic="618">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar"> arumiat:</div>
<blockquote>
<p>By current spacing 720x720px so (720, 720, 4) ?</p>
</blockquote>
</aside>
<p>No, 720 is the dimension (number of voxels) but the spacing is the distance between the voxels.  You can see these in the Volumes module information tab for your volume.  So desired spacing would be something like (2,2,4).  You can experiment with different options to trade off resolution for file size.</p>

---

## Post #12 by @arumiat (2018-04-10 11:49 UTC)

<p>So spacing of <strong>0.375</strong>mm.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2283abb4175b29a920f4b85060cc18ef252325d9.png" alt="spacing" data-base62-sha1="4VkkUdltoeFL4tt5yflM8UKiYYh" width="454" height="449"></p>
<p>I need to multiply current size by spacing (720*0.375 = 270) and then divide by desired size = 270/256 for instance = 1.05</p>
<p>So (1,1,4)?</p>
<p>Or if I wanted to only reduce to 512x512 xy then I could use (0.5, 0.5, 4)?</p>

---

## Post #13 by @pieper (2018-04-10 12:08 UTC)

<p>Yes, that looks right.  You could start with the Resample Scalar Volume module to reduce the number of slices (increase Z spacing) and then use CropVolume to explore the size/resolution tradeoffs.  Look in the Volume Information tab as you adjust the parameters.</p>
<p>(unless I’ve forgotten or missed something Crop Volume doesn’t support per-axis scaling which is why you need Resample Scalar Volume).</p>

---
