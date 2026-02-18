# Handling Missing Slice Data in RT Structures: How Does SlicerRT Interpolate Missing RT Data?

**Topic ID**: 40431
**Date**: 2024-11-28
**URL**: https://discourse.slicer.org/t/handling-missing-slice-data-in-rt-structures-how-does-slicerrt-interpolate-missing-rt-data/40431

---

## Post #1 by @tamerWagih (2024-11-28 16:57 UTC)

<p>Hello Slicer Community,</p>
<p>I’m currently working with <strong>RT structure sets (RTSS)</strong>, and I’ve encountered an interesting issue when using <strong>Plastimatch</strong>’s <code>convert</code> command to extract RT structures as label images. The issue is that <strong>Plastimatch</strong> outputs label images where certain slices are missing, particularly when there’s an <strong>unequal slice spacing</strong>. Here’s the warning I received from <strong>Plastimatch</strong>:</p>
<pre><code class="lang-auto">Warning: Slice spacing of RTSS may be unequal
-2.012 - -17.012 = 15 vs. 2.5
</code></pre>
<p>This suggests that there’s a <strong>15mm gap</strong> between certain slices, where <strong>Plastimatch</strong> reports the usual <strong>2.5mm spacing</strong> between slices. <strong>Matlab</strong> confirmed this, as shown below:</p>
<pre><code class="lang-auto">Z-coordinates and slice spacing (in mm):
From -37.012 mm to -34.512 mm: Spacing = 2.500 mm
From -34.512 mm to -32.012 mm: Spacing = 2.500 mm
From -32.012 mm to -29.512 mm: Spacing = 2.500 mm
...
From -17.012 mm to -2.012 mm: Spacing = 15.000 mm
</code></pre>
<p>This gap (15mm) between <code>-17.012 mm</code> and <code>-2.012 mm</code> results in missing RT structure data for some slices. However, when I load the <strong>same RT structure set in Slicer</strong> using <strong>SlicerRT</strong>, the visualization displays <strong>the full RT structure data</strong> with <strong>no missing slices or gaps</strong>, which is quite puzzling.</p>
<h3><a name="p-119999-my-questions-1" class="anchor" href="#p-119999-my-questions-1" aria-label="Heading link"></a>My Questions:</h3>
<ol>
<li><strong>How does SlicerRT handle this missing slice data or unequal slice spacing when visualizing RT structure sets?</strong></li>
</ol>
<ul>
<li>Does <strong>SlicerRT</strong> apply any interpolation to the RT structure data in order to fill the gaps caused by unequal slice spacing?</li>
<li>If so, what part of the <strong>SlicerRT code</strong> is responsible for this interpolation or handling of unequal slice spacing? Is there a specific function or algorithm that addresses this issue?</li>
</ul>
<ol start="2">
<li><strong>Is there a specific process in Slicer that allows it to visualize the missing slices properly, even when <strong>Plastimatch</strong> reports unequal spacing?</strong></li>
<li><strong>Could you point me to any documentation or relevant code sections in <strong>SlicerRT</strong> that explain how the system handles or interpolates RT structure sets with unequal slice spacing or missing slices?</strong></li>
</ol>

---

## Post #2 by @cpinter (2024-11-29 09:29 UTC)

<p>RTSS contains a series of 2D contours. These contours are triangulated to a closed surface, and then that surface is converted into a labelmap. Here is the paper about the actual triangulation:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9415/94151R/Reconstruction-of-surfaces-from-planar-contours-through-contour-interpolation/10.1117/12.2081436.short">
  <header class="source">
      <img src="https://www.spiedigitallibrary.org/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9415/94151R/Reconstruction-of-surfaces-from-planar-contours-through-contour-interpolation/10.1117/12.2081436.short" target="_blank" rel="noopener">SPIE Digital Library</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://www.spiedigitallibrary.org/images/Social/Proceedings-ShareImage.jpg" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/9415/94151R/Reconstruction-of-surfaces-from-planar-contours-through-contour-interpolation/10.1117/12.2081436.short" target="_blank" rel="noopener">Reconstruction of surfaces from planar contours through contour interpolation</a></h3>

  <p>Segmented structures such as targets or organs at risk are typically stored as 2D contours contained on evenly spaced cross sectional images (slices). Contour interpolation algorithms are implemented in radiation oncology treatment planning software...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If contours are missing, it simply means that the adjacent contours to triangulate will be farther from each other there than in the rest of the structure.</p>
<p>About the rest of the conversions and the conversion mechanism itself please see these links<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p><aside class="onebox pdf" data-onebox-src="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">
  <header class="source">

      <a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf" target="_blank" rel="noopener">labs.cs.queensu.ca</a>
  </header>

  <article class="onebox-body">
    <a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf" target="_blank" rel="noopener">Pinter2019_Manuscript.pdf</a></h3>

  <p class="filesize">707.26 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://qspace.library.queensu.ca/handle/1974/26422">
  <header class="source">
      <img src="https://qspace.library.queensu.ca/handle/1974/assets/atmire/images/favicon.png" class="site-icon" width="" height="">

      <a href="https://qspace.library.queensu.ca/handle/1974/26422" target="_blank" rel="noopener">qspace.library.queensu.ca</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://qspace.library.queensu.ca/handle/1974/26422" target="_blank" rel="noopener">Dynamic Representation of Anatomical Structures in Radiation Therapy...</a></h3>

  <p>Segmentation is a ubiquitous operation in radiation therapy (RT) and in medical image computing (MIC) in general. Various data representations can describe segmentation results, such as binary volumes or surface models. Conversions between them are...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @tamerWagih (2024-11-29 12:38 UTC)

<p>Thank you so much for the detailed explanation and the helpful links! I’ll take a look at the resources you’ve shared and dive deeper into the code. Appreciate your help,</p>

---
