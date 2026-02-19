---
topic_id: 16517
title: "Issue With Mask Exported From Slicer"
date: 2021-03-12
url: https://discourse.slicer.org/t/16517
---

# Issue with mask exported from Slicer 

**Topic ID**: 16517
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/issue-with-mask-exported-from-slicer/16517

---

## Post #1 by @Charlotte (2021-03-12 22:15 UTC)

<p>Hi, I am working on a project which requires me to perform radiomics analysis on ROIs exported from different software, including Slicer. The software I am using to perform the analysis is LifeX and I am also using CERR and MICE to create ROIs. I have however noticed that the ROI exported from Slicer is rotated and of the wrong size and resolution compared to those from other software. I am using the following instructions to export the ROI as both a Nifty and NRRD file: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a></p>
<p>The data I am using is this:</p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/theibsi/data_sets/tree/master/ibsi_1_validation/dicom/STS_001/CT" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:400/400;"><img src="https://avatars.githubusercontent.com/u/38988250?s=400&amp;amp;v=4" class="thumbnail" width="400" height="400"></div>

<h3><a href="https://github.com/theibsi/data_sets/tree/master/ibsi_1_validation/dicom/STS_001/CT" target="_blank" rel="noopener nofollow ugc">theibsi/data_sets</a></h3>

<p><a href="https://github.com/theibsi/data_sets/tree/master/ibsi_1_validation/dicom/STS_001/CT" target="_blank" rel="noopener nofollow ugc">master/ibsi_1_validation/dicom/STS_001/CT</a></p>

  <p><span class="label1">Data sets used by the IBSI for benchmarking and standardisation</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>As you can see, the size of the original CT image is 198x202x59 whereas the mask exported from slicer has the dimensions 239x248x264 which is what is causing the problem.<br>
Are there any settings I could use to create a binary mask with the same size as the CT matrix?</p>

---

## Post #2 by @lassoan (2021-03-13 00:56 UTC)

<p>It seems that the other software that you use do not take into account physical space information correctly. For compatibility with such software, you can choose a reference volume when you export the segmentation (it will make the exported labelmap geometry match the geometry of the reference volume).</p>

---

## Post #3 by @Charlotte (2021-03-13 10:43 UTC)

<p>Thanks for your answer!<br>
Unfortunately I think the problem is with the way the ROI is exported…<br>
See below the LifeX interface<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfe0fc7bfbbdd7d45022eab15214ef3287e2c923.jpeg" data-download-href="/uploads/short-url/vWwvpZZbqSBEdDaeRjq6XfmGeJl.jpeg?dl=1" title="Screenshot (72)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfe0fc7bfbbdd7d45022eab15214ef3287e2c923_2_690x352.jpeg" alt="Screenshot (72)" data-base62-sha1="vWwvpZZbqSBEdDaeRjq6XfmGeJl" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfe0fc7bfbbdd7d45022eab15214ef3287e2c923_2_690x352.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfe0fc7bfbbdd7d45022eab15214ef3287e2c923_2_1035x528.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfe0fc7bfbbdd7d45022eab15214ef3287e2c923_2_1380x704.jpeg 2x" data-dominant-color="61725D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (72)</span><span class="informations">1891×965 481 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It is clear that the ROI exported from the other software I am using (MICE and CERR) all match whereas that exported from Slicer (in green) is clearly wrong.<br>
The exported mask also doesn’t match with that created in Slicer which suggests that the export function is wrong?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86797d3ec6c2e6e2a7de0e80ac6eeddba8c5226e.png" data-download-href="/uploads/short-url/jbCgLVY2t8Gf0mXggJMhQFHRQho.png?dl=1" title="Screenshot (73)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86797d3ec6c2e6e2a7de0e80ac6eeddba8c5226e_2_690x351.png" alt="Screenshot (73)" data-base62-sha1="jbCgLVY2t8Gf0mXggJMhQFHRQho" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86797d3ec6c2e6e2a7de0e80ac6eeddba8c5226e_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86797d3ec6c2e6e2a7de0e80ac6eeddba8c5226e_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86797d3ec6c2e6e2a7de0e80ac6eeddba8c5226e_2_1380x702.png 2x" data-dominant-color="A4A1A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (73)</span><span class="informations">1845×939 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What steps can I take to avoid this?</p>

---

## Post #4 by @lassoan (2021-03-13 13:43 UTC)

<p>What format you export the segmentation to: nrrd, nifti, stl, obj, DICOM Segmentation Object, or DICOM RT structure set?<br>
How do you export from Slicer - export to files feature, export to model/labelmap and save, or using DICOM export data in Data module?</p>

---

## Post #6 by @lassoan (2021-03-14 05:13 UTC)

<p>I’ve downloaded the data and checked where Slicer gets the exported labelmap geometry and I’ve found that the DICOM data sets are not created correctly. RT structure sets must reference image frames that they are created from. The <a href="https://github.com/theibsi/data_sets/tree/master/ibsi_1_validation/dicom/STS_001/CT">STS_001 validation data set’s structure set</a> contains invalid references:</p>
<p>Referenced series instance UID in RT structure set:</p>
<pre><code>[0020,000e]	SeriesInstanceUID   1.3.6.1.4.1.14519.5.2.1.5168.1900.293609116849698550139986038601	UI	64
</code></pre>
<p>Series instance UID of the CT image:</p>
<pre><code>[0020,000e]	SeriesInstanceUID	1.3.6.1.4.1.14519.5.2.1.5168.1900.449841255123215696894565592289	UI	64
</code></pre>
<p>ReferencedSOPInstanceUIDs listed in the RT structure set file do not match any of the UIDs in the CT image either.</p>
<p>Please report this error to the maintainers of this data set.</p>
<p>Consequence of these invalid references that the RT structure set does not get associated with the CT automatically (Slicer can work with many CTs and structure sets simultaneously, so the fact that you only loaded a single CT so far does not make Slicer assume that it should be used as reference geometry).</p>
<p>You can set the CT as the reference geometry for the structure set in Segmentations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca56b38f044f6e34786758de92542ebbe7b2abcb.jpeg" data-download-href="/uploads/short-url/sRYcLzR1vA5zviFep55iHPApE1l.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca56b38f044f6e34786758de92542ebbe7b2abcb_2_690x489.jpeg" alt="image" data-base62-sha1="sRYcLzR1vA5zviFep55iHPApE1l" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca56b38f044f6e34786758de92542ebbe7b2abcb_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca56b38f044f6e34786758de92542ebbe7b2abcb_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca56b38f044f6e34786758de92542ebbe7b2abcb_2_1380x978.jpeg 2x" data-dominant-color="56514C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1598×1133 342 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that the binary labelmap representation that Slicer created without this association were completely valid, too. If they loaded incorrectly in some other software then report this error to their developers. It is OK if a software cannot handle segmentations and and CT images with different geometries (use different origin, spacing, axis direction, or extent), but then the software should detect this and display an error instead of showing incorrect result.</p>

---

## Post #7 by @Charlotte (2021-03-14 10:34 UTC)

<p>Hi, thank you so much for looking into this! I have followed your steps and LifeX is now displaying the correct position and size from the Slicer export! I suspect I will need to do this for every data set?</p>
<p>Regarding the error in LifeX, I did actually get an error message when importing the old ROIs: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c92ca868a867c05da1ed18111338bfc222f03cd9.png" alt="Screenshot (64)" data-base62-sha1="sHFEkJJkpIf763svaZAnRt4AZ6N" width="292" height="369"><br>
This obviously does not show up anymore so thanks again!</p>

---

## Post #8 by @lassoan (2021-03-14 14:13 UTC)

<aside class="quote no-group" data-username="Charlotte" data-post="7" data-topic="16517">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/65b543/48.png" class="avatar"> Charlotte:</div>
<blockquote>
<p>I have followed your steps and LifeX is now displaying the correct position and size from the Slicer export! I suspect I will need to do this for every data set?</p>
</blockquote>
</aside>
<p>You can ask maintainers of these test data sets to fix the DICOM references (maybe only some of them are broken). If they are not willing to do that and you don’t want to do this manually for many data sets then you can write a Python script that does this automatically (along with any other processing steps that to plan to do in Slicer).</p>

---
