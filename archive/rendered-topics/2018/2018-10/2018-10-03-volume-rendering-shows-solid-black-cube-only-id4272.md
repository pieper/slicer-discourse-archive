---
topic_id: 4272
title: "Volume Rendering Shows Solid Black Cube Only"
date: 2018-10-03
url: https://discourse.slicer.org/t/4272
---

# Volume rendering shows solid black cube only

**Topic ID**: 4272
**Date**: 2018-10-03
**URL**: https://discourse.slicer.org/t/volume-rendering-shows-solid-black-cube-only/4272

---

## Post #1 by @Anthony_Evlambiou (2018-10-03 14:10 UTC)

<p>Hello,</p>
<p>I have a quick question as I am new to slicer and it might just be a simple error.</p>
<p>I have created a stack of tiff files and managed to load them onto slicer and then adjust the image spacing so that there a full picture from each view.</p>
<p>The problem comes in when I want to create a volume rendering to show the bones of the specimens in the scan. When I click on the ‘eye’ button to view the volume rendering all I get is a solid black cube and nothing of what is in the scan.</p>
<p>I have tried adjusting the threshold and the shift but to no avail. It still only shows black. No bones. I also tried different presets to get the bones to show with no luck again.</p>
<p>I first tested myself on one of the samples that I could download (the chest cavity) and I managed to do that just fine. Everything worked perfectly.</p>
<p>Could you please advise on where I could be going wrong.</p>
<p>Thank you an much appreciated. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @cpinter (2018-10-03 14:25 UTC)

<p>I’d try selecting different presets and then play with the shift slider.</p>
<p>What’s the scalar range of your images?</p>

---

## Post #3 by @lassoan (2018-10-03 14:30 UTC)

<p>Tiff files might contain vector (RGB color) images that you need to convert to grayscale (single-component scalar) volume. See details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#Module_Description">https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeRendering#Module_Description</a></p>

---

## Post #4 by @Anthony_Evlambiou (2018-10-03 15:50 UTC)

<p>Thanks. So I tried the different presets and the shift slider. Still no luck.</p>
<p>I am not sure where to check the scalar ranges. Sorry, like I said I am very new to all of this.</p>

---

## Post #5 by @Anthony_Evlambiou (2018-10-03 15:53 UTC)

<p>Thanks. I had a look and it says my files are scalar and grey scale.</p>
<p>The one thing I did notice between the sample and my files when looking at the three different views…for the sample when I move the slider it cuts through the sample like it shows one slice at a time. When I move the slider on my files it rotates the whole image and does not cut through. I hope that makes sense.</p>
<p>Not sure if that means anything but thought I would mention it.</p>

---

## Post #6 by @pieper (2018-10-03 16:22 UTC)

<p>If you can share example images or screenshots it might help.</p>

---

## Post #7 by @cpinter (2018-10-03 17:42 UTC)

<p>You can check volume properties like scalar range and number of components in the Volumes module. When you make the screenshot if you make sure the Volumes module is open and the content of the Volume Information panel is visible, that would be great.</p>

---

## Post #8 by @lassoan (2018-10-03 22:40 UTC)

<p>You can also check in Volumes module that you have loaded a 3D volume and not just a single image slice.</p>

---

## Post #9 by @Anthony_Evlambiou (2018-10-04 07:02 UTC)

<p>Thanks Everyone,</p>
<p>I really appreciate the effort you guys are going through to help.</p>
<p>Below is a screen shot of what I get</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/befa4ed9282ba0d9998a52e297c251afc83fa458.png" data-download-href="/uploads/short-url/rft06W0qsrNUf76G7I1ge27uyNO.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/befa4ed9282ba0d9998a52e297c251afc83fa458_2_690x356.png" alt="screenshot" data-base62-sha1="rft06W0qsrNUf76G7I1ge27uyNO" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/befa4ed9282ba0d9998a52e297c251afc83fa458_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/befa4ed9282ba0d9998a52e297c251afc83fa458_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/befa4ed9282ba0d9998a52e297c251afc83fa458_2_1380x712.png 2x" data-dominant-color="919197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1598×826 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @rkikinis (2018-10-04 07:55 UTC)

<p>Hi,</p>
<p>the picture shows a dark structure embedded in a white structure. You will need to modify the transfer function in the volume rendering module to have low values opaque and high values transparent. The default transfer function has low opacity in low signal intensity and high opacity in high signal intensity. You might also want to assign different colors to low and high signal  intensity as opposed to black and white.</p>
<p>The crop function in the volume renderer might allow you to peek into the current cube where you might be able to see your snakes as dark tunnels.</p>
<p>Best</p>
<p>Ron</p>

---

## Post #11 by @cpinter (2018-10-04 12:53 UTC)

<p>Also what I see in the slice views seems to be off, like when the images are loaded from raw data with the wrong height/width values. Are your original tiff files different from what you get in the axial view?</p>

---

## Post #12 by @Anthony_Evlambiou (2018-10-04 13:25 UTC)

<p>The scans were done with a microCT scanner. The raw data files seem to be the same as the axial view. There were about 2800 files of which I built the stack using every fifth image. As I move the axial slider it rotates the image around and does not show the slices through.</p>
<p>The screenshot below is what I get after I load the data and click on the volume module so you can see the details there.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42ae8a9d116a5bfe33f5907f5a9c36e5fa4523fa.png" data-download-href="/uploads/short-url/9vTsUQtAox3zIKyHa70101l06Ke.png?dl=1" title="Straight%20after%20loading" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42ae8a9d116a5bfe33f5907f5a9c36e5fa4523fa_2_690x355.png" alt="Straight%20after%20loading" data-base62-sha1="9vTsUQtAox3zIKyHa70101l06Ke" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42ae8a9d116a5bfe33f5907f5a9c36e5fa4523fa_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42ae8a9d116a5bfe33f5907f5a9c36e5fa4523fa_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42ae8a9d116a5bfe33f5907f5a9c36e5fa4523fa_2_1380x710.png 2x" data-dominant-color="86868D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Straight%20after%20loading</span><span class="informations">1598×824 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @cpinter (2018-10-04 13:29 UTC)

<p>I really don’t understand the rotation part. Are you sure the projections have been reconstructed into a volume?</p>

---

## Post #14 by @Anthony_Evlambiou (2018-10-04 13:34 UTC)

<p>I tried fiddling with the shift and the scaler opacity mapping with no luck.<br>
I am not actually sure how to change the transfer function as I do not see its heading anywhere.</p>
<p>Is there a link to a step process I could follow perhaps?</p>
<p>Thank you again.</p>

---

## Post #15 by @lassoan (2018-10-04 13:35 UTC)

<p>It looks like the image is not a Cartesian 3D volume but a <a href="https://en.wikipedia.org/wiki/Tomographic_reconstruction">sinogram</a>. You need to run these images through filtered backprojection or similar reconstruction method to get a 3D volume that you can load into Slicer.</p>

---

## Post #16 by @hherhold (2018-10-04 13:53 UTC)

<p>The Z image spacing here is only 1mm - is that correct? Looks like it should be 25mm like X and Y?</p>

---

## Post #17 by @lassoan (2018-10-04 14:02 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="16" data-topic="4272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>The Z image spacing here is only 1mm - is that correct?</p>
</blockquote>
</aside>
<p>The data set is just a series of 560 projection images, from different angles as the gantry rotates around the object. There is no Z image spacing, because it is not a Cartesian volume.</p>
<p>If the scanner is a commercial product then it must have 3D reconstruction feature built in. <a class="mention" href="/u/anthony_evlambiou">@Anthony_Evlambiou</a> should simply load the correct data set - the 3D reconstructed volume - into Slicer instead of loading a series of projections.</p>

---

## Post #18 by @Anthony_Evlambiou (2018-10-04 14:17 UTC)

<p>These were the steps I followed to load my tiff files:</p>
<ol>
<li>Choose from the menu:  <em>File</em>  /  <em>Add Data</em>
</li>
<li>Click  <em>Choose File(s) to Add</em>  button and select any of the files in the sequence in the displayed dialog</li>
<li>Click on  <em>Show Options</em>  and uncheck the  <em>Single File</em>  option</li>
<li>Click  <em>OK</em>  to load the volume</li>
<li>Go to the  <em>Volumes</em>  module</li>
<li>Choose the loaded image as  <em>Active Volume</em>
</li>
<li>In the  <em>Volume Information</em>  section set the correct  <em>Image Spacing</em>  and  <em>Image Origin</em>  values</li>
</ol>
<p>Thanks again to everyone for all the help.<br>
I will keep at it and keep trying the advice you are giving.</p>

---

## Post #19 by @pieper (2018-10-04 14:30 UTC)

<p>Hi <a class="mention" href="/u/anthony_evlambiou">@Anthony_Evlambiou</a>, just to reiterate <a class="mention" href="/u/lassoan">@lassoan</a>’s point, you are doing everything correctly in Slicer but need to reconstruct the volume from the projections before you can proceed.  Probably easiest to do this on the scanner that produced the images.</p>

---

## Post #20 by @hherhold (2018-10-04 14:31 UTC)

<p>I thought it looked pretty characteristic of a sinogram, but I wondered if it just looked strange from having incorrect spacing.</p>
<p>Just out of curiosity, does anyone use itk/vtk-based open-source based reconstruction software?</p>

---

## Post #21 by @Anthony_Evlambiou (2018-10-11 07:51 UTC)

<p>Ok great. Thank you.</p>
<p>The scans were done at a different university so I do not have access to the scanner but will contact the university to find out.</p>
<p>Thanks again Everyone.</p>

---
