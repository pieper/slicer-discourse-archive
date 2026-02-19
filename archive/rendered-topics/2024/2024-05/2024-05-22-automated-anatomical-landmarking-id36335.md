---
topic_id: 36335
title: "Automated Anatomical Landmarking"
date: 2024-05-22
url: https://discourse.slicer.org/t/36335
---

# Automated Anatomical Landmarking

**Topic ID**: 36335
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/automated-anatomical-landmarking/36335

---

## Post #1 by @LindenRB (2024-05-22 23:55 UTC)

<p>Hi,</p>
<p>Is anyone aware of any extensions or tools that would allow a user to perform an automated anatomical landmarking workflow? Looking at options to train a model for 3D landmark registration of bony anatomical landmarks from lower limb CT’s, such as the epicondylar axis of the knee joint, center of rotation of the femoral head etc. Ideal goal would be to open a CT of a new patient, run the landmarker model and have it automatically generate point landmarks (markup points) for all the required anatomical points of interest in the trained model.</p>
<p>Wondering if someone has already done all the hard work here and there is an extension or tool already created for a similar purpose to this. I’ve tried searching the forums but not found much so far.<br>
I understand that to train a model and get anywhere near decent results, we would need likely thousands of patients worth of data.</p>
<p>Open to any and all ideas and suggestions here</p>
<p>Cheers,<br>
Linden</p>

---

## Post #2 by @muratmaga (2024-05-23 00:03 UTC)

<p>Have you tried the ALPACA/MALPACA module in SlicerMorph extension?</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/ALPACA" target="_blank" rel="noopener">Tutorials/ALPACA at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/chz31/Tutorials/blob/main/MALPACA/MALPACA.md">
  <header class="source">

      <a href="https://github.com/chz31/Tutorials/blob/main/MALPACA/MALPACA.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/chz31/Tutorials/blob/main/MALPACA/MALPACA.md" target="_blank" rel="noopener">chz31/Tutorials/blob/main/MALPACA/MALPACA.md</a></h4>


      <pre><code class="lang-md"># Executing Multi-Template ALPACA (MALPACA) 
This tutorial contains instructions for executing the multi-template ALPACA (MALPACA) pipeline for automated landmarking that can accomodate large morphological disparity within a sample. The MALPACA pipeline is essentially performing multiple independent ALPACA runs, each of which based on a single template. It then calculate the median from the results of all these ALPACA runs as the final output of landmark estimates. The same parameter setting of ALPACA applies to MALPACA. For the publication of MALPACA, please see https://doi.org/10.1371/journal.pone.0278035. For tutorials of how to run ALPACA and , please refer to: https://github.com/SlicerMorph/Tutorials/blob/main/ALPACA/README.md. 

Download sample data here: https://github.com/SlicerMorph/mouse_models. Extract the files.

### Step 1. Switch to the ALPCA module in 3D Slicer and choose the Batch Processing tab (red). 
In the `Method` entry (dark blue box in the picture below), select the `Multi-Template (MALPACA)` option from the dropdown menu.

&lt;p align="center"&gt;
&lt;img src="./kmeans_MALPACA_images/MALPACA_019.png", width = 700&gt;
&lt;p/&gt;

### Step 2. Select required input and output directories (see the picture above).
* In the `Source model(s)` entry (yellow), select the folder that contains the templates (ply format). 
  * **If you are uncertain about which specimens to be used as templates, you may use the accompanied k-means multi-template selection method (see [kmeans templates selection tutorial](https://github.com/SlicerMorph/Tutorials/blob/main/MALPACA/K-means_templates_selection.md)).**
  * If you have used the K-means method to select templates, you can select the dirctory that contains the output templates. 
* In the `Source landmarks` entry (green), select the folder that contains the manual landmark files for the selected templates. The file names of the template model and landmark files must be identical. **The format of the landmark files should be either 'mrk.json' or 'fcsv'. The 'mrk.json' format is recommended.**
* In the `Target model directory` entry (dark grey), select the folder that contains the target models (ply format). These are the specimens that will be landmarked by the MALPACA pipeline.
* In the `Target output landmark directory` (light blue), select the folder for storing the MALPACA output landmark files (mrk.json format) of the target specimens.
* Optional settings
</code></pre>



  This file has been truncated. <a href="https://github.com/chz31/Tutorials/blob/main/MALPACA/MALPACA.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @LindenRB (2024-05-27 01:00 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a>, I’m not sure why but I had completely overlooked ALPACA when looking at options. I think this will be adequate for my needs</p>

---
