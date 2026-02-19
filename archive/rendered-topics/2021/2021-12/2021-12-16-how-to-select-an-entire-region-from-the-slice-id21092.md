---
topic_id: 21092
title: "How To Select An Entire Region From The Slice"
date: 2021-12-16
url: https://discourse.slicer.org/t/21092
---

# How to select an entire region from the slice

**Topic ID**: 21092
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/how-to-select-an-entire-region-from-the-slice/21092

---

## Post #1 by @YihangZhao (2021-12-16 13:53 UTC)

<p>I tried to reconstruct endocast of species but I don’t know how can I select the region that is correspond to the endocast. I know I can select the endocast region for each slice by manually paint it, but that is time-consuming. Is there any ways I can select the whole endocast region with only one click.  (Just like what the level tracing function does, but better than that function because in many cases level tracing can’t select the entire region).</p>

---

## Post #2 by @lassoan (2021-12-16 18:21 UTC)

<p>Is this what you are looking for?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/">
  <header class="source">

      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" target="_blank" rel="noopener">3D Slicer segmentation recipes</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" target="_blank" rel="noopener">Overview</a></h3>

  <p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>          <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/image-003.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/image-003.png" width="561" height="500">
          </a>
</p>

---

## Post #3 by @YihangZhao (2021-12-18 04:55 UTC)

<p>I tried to use the method mentioned above but I got an error at the wrap solidify stage every time I tried. It shows “Wrap solidify failed: Mesh has become empty during shrink-wrap iterations”. I have tried different version but none of them worked.(4.13/4.11.20210226/4.11.20200930)</p>

---

## Post #4 by @lassoan (2021-12-18 14:22 UTC)

<p>Please try to follow the recipe using the latest Slicer Preview Release, on the sample data set, starting from scratch and see if that works. That would help determine if you have something wrong in your data set, segmentation settings, or the software.</p>

---

## Post #5 by @YihangZhao (2021-12-21 21:18 UTC)

<p>I tried again and it turns out that I failed to complete the wrap solidify stage because I miss one earlier step.</p>
<p>Another question I have is after I save the file, how can I open it again and continue my previous work? I exported my segmentation into different file formats. Then, next time when I open 3D Slicer and open these files, I can see the 3D structure I have reconstructed shown in the screen but I don’t know how can I modify the structure so that I can finally finish it. Besides exporting my work, I also saved my work using the “save” function and I wonder if I cannot continue my work with exported files, can I continue my work with the saved file? If so, how can I find the file that I already saved?</p>

---

## Post #6 by @lassoan (2021-12-21 21:22 UTC)

<p>Storage in some file formats are lossy, but in general you can load the exported file and continue editing it. When you use File/Save then the default file formats are all lossless and the scene file (.mrml) contain all minor parameters that were set on the GUI.</p>

---

## Post #7 by @YihangZhao (2021-12-23 20:49 UTC)

<p>But how can I find the saved files?</p>

---

## Post #8 by @lassoan (2021-12-23 21:25 UTC)

<p>When you export a segmentation to a labelmap volume no file is created yet. The file gets created when you use File / Save (or in recent Slicer Preview Releases right-click on the volume and choose “Export to file…”).</p>

---
