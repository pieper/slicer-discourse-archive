# Showing deformation on a reference model

**Topic ID**: 37084
**Date**: 2024-06-28
**URL**: https://discourse.slicer.org/t/showing-deformation-on-a-reference-model/37084

---

## Post #1 by @coco (2024-06-28 11:17 UTC)

<p>Dear all,<br>
I wonder if there’s a way in slicer to produce similar figures as below, where you can see surface deformation as increase or decrease procruste distance relative to reference (control animals)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03748d3691b0660ed0407acdcdde8c07c9423c5a.jpeg" data-download-href="/uploads/short-url/uz8S2WKoyXfRRg8b82uNXijBuq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03748d3691b0660ed0407acdcdde8c07c9423c5a_2_577x499.jpeg" alt="image" data-base62-sha1="uz8S2WKoyXfRRg8b82uNXijBuq" width="577" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03748d3691b0660ed0407acdcdde8c07c9423c5a_2_577x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03748d3691b0660ed0407acdcdde8c07c9423c5a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03748d3691b0660ed0407acdcdde8c07c9423c5a.jpeg 2x" data-dominant-color="D5D8D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">670×580 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
many thanks again to all developpers…</p>

---

## Post #2 by @muratmaga (2024-06-28 13:51 UTC)

<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/heatmaps/Heatmaps.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/heatmaps/Heatmaps.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/heatmaps/Heatmaps.md" target="_blank" rel="noopener">SlicerMorph/Tutorials/blob/main/heatmaps/Heatmaps.md</a></h4>


      <pre><code class="lang-md"># How to visualize heatmaps of surface difference in 3D Slicer
This tutorial steps you through how to create models and heatmaps in Slicer that show the difference between the mean shape and shapes at an extreme of a principal component axis from a PCA. 

Things you will need to be able to do this on your own dataset: 
  - full landmark dataset
  - a reference model - this can be an average image or just a single model from your dataset
    - Depending on your computer and the size of your model, you may need to decimate your model (make it smaller), which you can do in the `Surface Toolbox` module in 3D Slicer.
  - Landmarks for your reference model
  - Install the Model To Model Distance Extension from the extension catalogue
  
If you want to run the tutorial as written, you need to download (or git clone) the https://github.com/SlicerMorph/Mouse_Models repository. Or you can use your own data.

-----
## Creating PCA shape models using from the GPA module
Navigate to the GPA module, select all landmarks in the LM folder of the mouse_models repo you have downloaded. For heatmaps to have physical meaning, you need to execute your analysis with Boas coordinates option enabled. This will make sure that the scale of data is preserved during the PCA decomposition. If you leave the Boas coordinates option unchecked, then the heatmap values will be in the unitless procrustes distances. Set your output folder and other options as usual and execute the GPA + PCA. 

For input if you have selected all LMs as instructed, then GPA module will report as the FVB_NJ specimen as the sample closest to the consensus shape. We will use the 3D model (and its corresponding LM) as our reference model. For your own data, make sure you choose the sample closest reported to be closest to the mean shape.

Go to the `Interactive 3D Visualization` tab of GPA module and choose the 3D model visualization option. Navigate to the `FVB_NJ_.ply` file  and `FVJ_NJ_.fcsv` file as reference model and LM, respectively, and hit Apply. What this step would do is to transform the original FVB_NJ model in the mean shape model of the study. This model will provide the basis of heatmap visualization. Now slide the PC1 axis all the way to the +100 side. This will deform the mean model to the maximum of PC1. This would be the model we will calculate and visualize its difference from the mean model. We need to save these two models. To do that go to the `Data` module and:

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/heatmaps/Heatmaps.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @coco (2024-06-28 13:58 UTC)

<p>Fantastic ! Exactly what I was looking for !<br>
Struggled with the Distance to use in Model to model Distance options. “Corresponding_poitn_to_point” worked like a charm…</p>

---
