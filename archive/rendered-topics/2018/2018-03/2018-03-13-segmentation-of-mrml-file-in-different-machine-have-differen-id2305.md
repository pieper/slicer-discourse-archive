# Segmentation of mrml file in different machine have different resolution

**Topic ID**: 2305
**Date**: 2018-03-13
**URL**: https://discourse.slicer.org/t/segmentation-of-mrml-file-in-different-machine-have-different-resolution/2305

---

## Post #1 by @Masteling (2018-03-13 17:15 UTC)

<p>Hi,</p>
<p>I tried to segment the same mrml file in 2 different computers (created file in machine 1 and copied to machine 2 before segmenting) and the segmentation resolution if different between those machines.<br>
Machine 1: pixel size of 0.4<em>0.4mm (Slicer 4.8.0)<br>
Machine 2: pixel size of 0.9</em>0.9mm (Slicer 4.8.1 and 4.8.0 - tried both versions to see if it was a version issue).</p>
<p>What do you think creates this issue and how do you suggest us to solve it?</p>
<p>Thanks,<br>
Mariana</p>

---

## Post #2 by @cpinter (2018-03-13 17:50 UTC)

<p>Interesting. Can you please give us a few other details?</p>
<ul>
<li>When you say you want to segment a MRML file it means that you loaded a volume on computer 1 and saved the MRML scene (mrb or mrml in a folder) and that’s what you load on computer 2?</li>
<li>Do you use Segment Editor?</li>
<li>How do you check the resolution of the segmentation? Asking because if you use Segment Editor, then the segmentations don’t show up in Volumes module</li>
</ul>
<p>Thanks!</p>

---

## Post #3 by @Masteling (2018-03-13 18:06 UTC)

<p>Thanks for helping, here go some more details:</p>
<ol>
<li>
<p>In machine 1, I imported the dicom into slicer from folder X. Created the mrml file and then copy folder X into machine 2 and open the mrml from that folder.</p>
</li>
<li>
<p>Yes, we use segment editor.</p>
</li>
<li>
<p>I checked the resolution by measuring the size of the “squares”/pixel I get after segmenting using a ruler.<br>
Here’s an example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96a0d9a5246574df63351c8f90505f4e23cda46b.png" data-download-href="/uploads/short-url/luweUpc4pspuRuNyLDExlgT5jgT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a0d9a5246574df63351c8f90505f4e23cda46b_2_306x250.png" alt="image" data-base62-sha1="luweUpc4pspuRuNyLDExlgT5jgT" width="306" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a0d9a5246574df63351c8f90505f4e23cda46b_2_306x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a0d9a5246574df63351c8f90505f4e23cda46b_2_459x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96a0d9a5246574df63351c8f90505f4e23cda46b_2_612x500.png 2x" data-dominant-color="354132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1072×875 16.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>I tried using the crop volume, but in machine 2 it doesn’t change the resolution much/ never gets as good as in machine 1.</p>
</li>
</ol>

---

## Post #4 by @cpinter (2018-03-13 18:09 UTC)

<aside class="quote no-group" data-username="Masteling" data-post="3" data-topic="2305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masteling/48/13587_2.png" class="avatar"> Masteling:</div>
<blockquote>
<p>In machine 1, I imported the dicom into slicer from folder X. Created the mrml file and then copy folder X into machine 2 and open the mrml from that folder.</p>
</blockquote>
</aside>
<p>I don’t understand why this step is even necessary if you copy folder X anyway (which shouldn’t be necessary if you already have a saved MRML scene). Can you please explain it to me how you “created the mrml file”?</p>

---

## Post #5 by @Masteling (2018-03-13 18:13 UTC)

<p>We did that to save the time of loading all dicom, align them and save each scene.<br>
So the person using machine 2 could have a ready to go file. We have different people using the same mri for different things.<br>
I created the mrml file using the save option (manually).</p>

---

## Post #6 by @brhoom (2018-03-13 18:23 UTC)

<p>simply save the files as .nrrd (the original image and the segmentation), you will have to copy 2 files only to the other machine.</p>

---

## Post #7 by @Masteling (2018-03-13 18:26 UTC)

<p>The issue is not that we want to use the same segmentation. We are highlighting different structures, but in the process, we realize that our machines have different resolutions for the same image set.<br>
Is there isn’t a “solution” for this, we might need to just create a mrml in each machine.</p>

---

## Post #8 by @brhoom (2018-03-13 18:30 UTC)

<blockquote>
<p>highlighting different structures</p>
</blockquote>
<p>you can do it using the segmentation (.seg) file by adding new segment for the different structure. Just wondering, do you have the same problem when using the Editor (the old module for segmentation)? if yes,  It is not clear what you are doing, the best way to explain it is to record a short video of what you did and send the links. If no, then try to export the segmentation to a labelmap then import it in a new segmentation in the the new machine.</p>

---

## Post #9 by @cpinter (2018-03-13 18:35 UTC)

<p>You mention that you need to align multiple images (aka. register them together). This means you have multiple volumes to segment. Are you sure you choose the right master volume in Segment Editor?</p>
<p>To verify this, please go to Volumes module after loading the MRML scene, and check the voxel spacing for each volume. If one is 0.4mm and another 0.9mm, then it’s possible that simply the wrong one was used. Segment Editor makes the segmentation the same resolution as the first (!) master volume you selected. So if you select one, then change it to another, it will still have the resolution of the first one.</p>

---

## Post #10 by @Masteling (2018-03-13 20:54 UTC)

<p>Yes, we’re sure we are using the same master volume.<br>
Just opened and measure the pixel size for a couple different mrml files, and machine 2 has always worse quality than machine 1.</p>
<p>We decided to create a new file when the person that uses machine 2 needs to work on the files.<br>
However, this is an “interesting” “bug” and if you find a way to avoid this it will be highly appreciated.</p>
<p>Thanks,<br>
Mariana</p>

---

## Post #11 by @pieper (2018-03-14 20:56 UTC)

<p><a class="mention" href="/u/masteling">@Masteling</a> are you sure the pixel size is different and not just the display?  If the slice display is rotated compared with the segmentation the voxels may appear different sizes.</p>
<p>Do you have a way that we can replicate this with the sample data?</p>

---

## Post #12 by @lassoan (2018-03-14 21:24 UTC)

<p>Segmentation uses the first selected master volume to decide what will be the voxel size of the internal labelmap in the segmentation node. If you go to Segment Editor and a volume was selected by default and you select another one, it is already too late. You need to delete the segmentation node and create a new one, and select the correct volume as master volume.</p>
<p>We know that it is not intuitive, but not yet have the time to add GUI to force changing the internal geometry for an existing segmentation.</p>

---
