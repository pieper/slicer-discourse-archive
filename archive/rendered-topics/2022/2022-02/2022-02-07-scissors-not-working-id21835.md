---
topic_id: 21835
title: "Scissors Not Working"
date: 2022-02-07
url: https://discourse.slicer.org/t/21835
---

# Scissors Not Working

**Topic ID**: 21835
**Date**: 2022-02-07
**URL**: https://discourse.slicer.org/t/scissors-not-working/21835

---

## Post #1 by @Sandy1 (2022-02-07 05:50 UTC)

<p>I am in the segment editor, and I am attempting to remove jewelry and bone from my image. I have selected the erase inside option. Nothing happens once I’ve circled the areas with the scissors that I want to remove. Please help.</p>

---

## Post #2 by @DIV (2022-02-07 06:36 UTC)

<p>Hello, Sandra.<br>
Sorry to hear that it didn’t work.<br>
From my experience what commonly happens is that the segment you were tying to erase wasn’t <strong>selected</strong> in the panel on the side.<br>
See below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c6f9e487849e36d6de3b2385af4a592a6f4adf.png" alt="image" data-base62-sha1="7OA5rBdhe7cwqeo1Dm2T1myWup9" width="588" height="225"><br>
In the example, only <code>Segment_2</code> is <em>visible</em>;  <code>Segment_3</code> and <code>Segment_4</code> are <em>hidden</em>.  So the user will often expect to be editing <code>Segment_2</code>*.  (Alternatively, the other segments might be visible, but located outside of the current field of view**, say.)  But none of that matters.  the only thing that matters is that <code>Segment_3</code> is highlighted, so the Scissors effect will be applied to it.  Nothing in <code>Segment_2</code> will be erased.</p>
<p>—DIV</p>
<p>*There’s actually a warning that is displayed in this situation in recent versions of 3D Slicer.<br>
**No warning about this, AFAIK.</p>

---

## Post #3 by @Sandy1 (2022-02-09 18:31 UTC)

<p>This still did NOT work for me. Getting this tool to work is critical for me at the moment as I am working on my dissertation project and am on a strict timeline. Is there anyone willing to virtually meet with me to help figure this out? One thing I did notice in your example is that underneath the flag you have a pencil icon marking the segment you plan to edit and circles for the others. I do not have a pencil icon. I only have a flag and a check mark icon. Could this be another clue to what is causing this issue? I am available any time in the mornings before noon. Please help. Id be so grateful.<br>
Sandy</p>

---

## Post #4 by @muratmaga (2022-02-09 19:00 UTC)

<p>Without screenshots of what you have done so far, it is not possible for us to guide you. Please provide a screen capture of what is not working at the stage you are using the scissor tool.</p>

---

## Post #5 by @Sandy1 (2022-02-09 19:12 UTC)

<p>Understood. Currently at work but will do tomorrow morning. Thank you!!</p>

---

## Post #6 by @Sandy1 (2022-02-10 17:21 UTC)

<p>OK, SO I have set up the image I want to edit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/1/197743d8d5818e15818e3963fb2ccefecfa26aa4.jpeg" data-download-href="/uploads/short-url/3DhszIj3uUeKN6e8HsHeNNDfQjy.jpeg?dl=1" title="Inline image" rel="noopener nofollow ugc"><img title="Inline image" alt="Inline image" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/197743d8d5818e15818e3963fb2ccefecfa26aa4_2_690x431.jpeg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/197743d8d5818e15818e3963fb2ccefecfa26aa4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/197743d8d5818e15818e3963fb2ccefecfa26aa4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/197743d8d5818e15818e3963fb2ccefecfa26aa4_2_1380x862.jpeg 2x" data-dominant-color="C3C3D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inline image</span><span class="informations">3840×2400 831 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My GOAL is to remove everything from this image because all I need to see is the skull. I want to delete the earrings, nose ring, vertebrae, etc… So, I open up the Segment Editor to use the scissors tool…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/9/99d4bac01469b0599fc51a7b2af7e6dfd8a9fb02.jpeg" data-download-href="/uploads/short-url/lWQP4KuUp8I5ud1bJXodvX12aci.jpeg?dl=1" title="Inline image" rel="noopener nofollow ugc"><img title="Inline image" alt="Inline image" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99d4bac01469b0599fc51a7b2af7e6dfd8a9fb02_2_690x431.jpeg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99d4bac01469b0599fc51a7b2af7e6dfd8a9fb02_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99d4bac01469b0599fc51a7b2af7e6dfd8a9fb02_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/99d4bac01469b0599fc51a7b2af7e6dfd8a9fb02_2_1380x862.jpeg 2x" data-dominant-color="C2C3D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inline image</span><span class="informations">3840×2400 909 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I use the scissors as directed and absolutely NOTHING happens. Please Help. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @hherhold (2022-02-10 17:23 UTC)

<p>It looks like you are viewing the volume rendering of the data. Scissors works on the segmentation, not the volume data. You need to create a segment from the volume data, and then cut it with the scissors.</p>

---

## Post #8 by @Sandy1 (2022-02-10 17:30 UTC)

<p>Thank you for your response. Can you explain how to create a segment from the volume data?</p>

---

## Post #9 by @hherhold (2022-02-10 17:35 UTC)

<p>Image segmentation is a <em>vast</em> subject area. If this is a medical CT scan and you’re concentrating on bones, you can probably use the thresholding tool and pick the right Houndsfield unit range for bones (I’m an entomologist, so I’ve no idea what that would be). You can also use the paint tool, or local thresholding tool, etc. There are a LOT of tools for image segmentation.</p>

---

## Post #10 by @muratmaga (2022-02-10 17:55 UTC)

<aside class="quote no-group" data-username="Sandy1" data-post="8" data-topic="21835" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f04885/48.png" class="avatar"> Sandy1:</div>
<blockquote>
<p>Thank you for your response. Can you explain how to create a segment from the volume data?</p>
</blockquote>
</aside>
<p>Please review these tutorials. You will find them helpful:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation.md" target="_blank" rel="noopener">SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation.md</a></h4>


      <pre><code class="lang-md">## IMAGE SEGMENTATION with 3D Slicer

This is the big enchilada. Segmentation is what most people begin learning Slicer for and it is one of the first steps acquiring data towards a morphometric study. Careful extraction of anatomy and constructing an accurate 3D representation will have direct downstream impact on some of the analytical procedures, particularly for various semi-landmarking approaches and other morphometric techniques that require dense-correspondence. 

In Slicer, there two complementary modules that are used hand-in-hand for segmentation tasks.

1. `Segment Editor: ` is the actual module for segmentation of volumes. Segmentation (also known as contouring) delineate structures of interest. Some of the tools in `Segment Editor` mimic a painting interface like photoshop, but work on 3D arrays of voxels rather than on 2D pixels. In addition to the core segmentation tools (such threshold, paint, logical operations etc) provided, **SegmentEditorExtraEffects** extension (already bundled with SlicerMorph) provides additional segmentation tools (such as Mask/Split Volume by segments etc).   
2. `Segmentations:` is the module that allows you to manipulate the segmentations generated by `Segment Editor`. Some of the key functionality is to import/export segmentations into **Label Map** or **3D Model** representation, adjust and edit display properties, copy/move segments across different segmentations, and so forth. 

In addition there are couple supporting modules such as:

3. `Segment Statistics`, which allows you to extract quantitative information (such as volumes, moments of interia, centroid positions, etc) from the segmentations and tabulate them.
4. `Segment Comparison` allows you calculate various similarity indices for two different segmentations (e.g., compare segmentation results from one expert to the other). 
5. `Segment Registration` allows you to linearly and/or deformably register segments from two different datasets using the Elastix registration framework. 
6. `Segment cross-section area` module allows you to calculate, plot and tabulate the cross-sectional area of any segment as a function of slice number. 

If you are new to image segmentation, probably you should read the [official **Image Segmentation** documentation from Slicer.](https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html)

Even if you have previous experience with other 3D segmentation programs, it might be good to take a minute to read the Slicer specific functionalities and how different types of data types relate to each other (see figure below).

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/Segmentation/Segmentation.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Peto (2022-09-08 01:51 UTC)

<p>Step 1.<br>
Go to Segmentation Editor.</p>
<p>Select Threshold and adjust the sliders so that the bones are green.</p>
<p>This usually means adjusting the first slider up the scale (from a negative value to a positive value) to exclude soft tissue structures.</p>
<p>Once you are happy select Apply. You have now segmented the data set. Click on the “Show 3D” button to see the model.</p>
<p>Step 2.<br>
Now you can use the Scissors on the 3D model to remove sections.</p>

---

## Post #12 by @dav (2022-11-01 23:01 UTC)

<p>Yeah is this a bug?  I’m in the segment editor. You can see the green volume (Segment_12) I created that I’m trying to cut. I’m only trying to cut the volume Segment_12 itself so I’ve selected . The settings are set below:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/aba9d5256c0fb221aeccf4c7ae9f5d70f8cddfd0.png" alt="snipping_pic" data-base62-sha1="ouBvKAiFJTWqYCtQLw1FuDv8hvW" width="547" height="475"></p>
<p>(I also tried with and without the “Editable intensity range” on)</p>
<p>Here’s a video of me cutting it in the 3D view:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/870540cd53ec1c4ca3df9ff23c3f7abe6b97d383.gif" alt="gif1_spine" data-base62-sha1="jgrIdUtynTeWaCELyRLWrO6f0pd" width="600" height="338" class="animated"></p>
<p>Same happens if I try in the other views. It doesn’t remove the volumes. The only time I see it remove is if the “Editable area” is set to any of the options above the individual segment line. When I tried the “Outside Visible Segments” or others, it works, but it removes the segments selected (the green section (and maybe the other segments not visible)?</p>
<p>What’s going on?</p>

---

## Post #13 by @muratmaga (2022-11-01 23:27 UTC)

<p>Can you try with the latest stable (5.0.3) and report back?</p>

---

## Post #14 by @dav (2022-11-02 00:46 UTC)

<p>Yes I was using 4.11… It works great with 5.03.  Thanks.</p>

---

## Post #15 by @Unicom (2025-08-05 14:39 UTC)

<p>Solution: go to Segmentation Editor module - add a new empty segmentation - set the threshold to 200-3000 - click apply - click show 3D, and the complete bone model will be displayed on the right side, then you can cut structure.</p>

---
