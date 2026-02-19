---
topic_id: 26493
title: "Convert Avi To Mha"
date: 2022-11-29
url: https://discourse.slicer.org/t/26493
---

# convert .avi to .mha

**Topic ID**: 26493
**Date**: 2022-11-29
**URL**: https://discourse.slicer.org/t/convert-avi-to-mha/26493

---

## Post #1 by @mattusa90 (2022-11-29 15:06 UTC)

<p>For a research project I collected .avi video files of the vasculature under the tongue of patients with a microscope. I need to convert these .avi files to .mha files for analysis in new software. Would this be something that is possible with 3dslicer.</p>
<p>I have tried to convert the images to .png and then load the images in 3dslicer. How would I create a single .mha file out of this. Is there a more efficient way to do this?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @muratmaga (2022-11-29 20:07 UTC)

<p>I mean if you already read the PNGs as a volume then you are prtty much done. Right-click on the objects name and choose <code>export to file</code> and save as MHA.</p>

---

## Post #3 by @mattusa90 (2022-12-02 12:18 UTC)

<p>Thank you for the quick response!  I am a real novice at this. Just to check:</p>
<p>As a result of the conversion from .avi video to .png I have 100 seperate .png images.</p>
<p>Can these be loaded as 1 volume? Or is there an intermediate step I need to take?</p>

---

## Post #4 by @muratmaga (2022-12-02 15:25 UTC)

<p>To import pngs, the easiest is to use the imagestack module from Slicermorph extension.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Tutorials/blob/main/ImageStacks/README.md</a></h4>


      <pre><code class="lang-md">## ImageStacks
This is a SlicerMorph specific utility to import non-DICOM image sequences (TIF/PNG/JPG/BMP) into 3D Slicer. It provides additional features such as only loading a subset of the data using ROI, downsampling, skipping slice(s) along the Z plane, and reverse the stack order. You can also specify the voxel spacing for your dataset at the import time. `ImageStacks` always produces a ScalarVolume (single channel), so that volumes can be immediately visualized or can be processed with `Segment Editor`.

To use the `ImageStacks` module in SlicerMorph, first go to the `Sample Data` module and download the **Bruker/Skyscan mCT Recon Sample.** If you are not familiar with the `Sample Data` module or how to find where Slicer downloads files, please review the tutorials for [`Sample Data`](https://github.com/SlicerMorph/Tutorials/tree/main/SampleData) and [`SlicerMorph Preferences`](https://github.com/SlicerMorph/Tutorials/tree/main/MorphPrefs). 

Then find the `ImageStacks` under **SlicerMorph-&gt;Input and Output** module menu folder and:

1. Click the **Browse...** button and select a *PNG* file in the folder you just unzipped.

&lt;img src="ImageStacks1.png"&gt;

2. Image spacing in this dataset is provided in the accompanying left_side_damaged__rec.log file as 35.28 micron. Enter this value in millimeters as 0.03528 for all three axes. Millimeters is the default unit in Slicer. 
3. You leave the **Output Volume** blank, which will use the filename prefix. Or you can choose to create a new volume name. 
4. To preview a low resolution version of your file make sure the **preview** quality option is selected and click **Load Files** and see that all three slices viewers contain a low resolution version of our data.
5. To visualize what the specimen looks like, go to `Data` module and drag and drop  **left_side_damaged__rec** into the 3D viewer (Note: We will cover `Volume Rendering` module in great detail tomorrow. For the time being, this is all you need). You may need to hit the cross hairs and push pin directions (red boxes) to center your rendered image in the 3D widow.

&lt;img src="Data_Volume_Rendering.png"&gt;

Notice that the resultant rendering show the damage to the zygomatic arch in the **right side** of the specimen. Curiously, the specimen is named **Left side damaged**. 

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
