# 3D Model of membranous labyrinth from serial histological sections

**Topic ID**: 34088
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/3d-model-of-membranous-labyrinth-from-serial-histological-sections/34088

---

## Post #1 by @Zbynek (2024-02-01 12:03 UTC)

<p>Operating system: Windows 1.2309.12711.0<br>
Slicer version: 3D Slicer 5.6.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Can anyone tell me if 3D Slicer is suitable for building a 3D model of the membranous labyrinth from serial frontal histological sections through the otic capsule of a frog, and if so, how should I do it? The sections are available as JPG images taken under binoculars at the same scale but in different positions. I am a comparative anatomist, not a computer expert.</p>

---

## Post #2 by @muratmaga (2024-02-02 04:30 UTC)

<p>Short answer: You can. However, how good of end result you will get depends on how good you do the preprocessing.</p>
<ol>
<li>you need to register each slide so that random differences in the positioning of the sample are removed. Each slide needs to same XY number of pixels.</li>
<li>you need to know the correct spacing of each slide (XY resolution), and the spacing between each slide (Z resolution).</li>
</ol>
<p>You can try to use the registration tools in Slicer to accomplish step <span class="hashtag-raw">#1</span>. However, if you have too many slides, it can get tedious. A few days ago I stumbled this paper, which implemented a workflow similar to what you want to do in Fiji/ImageJ. If you can get this working, you can export the aligned images as a NRRD file from ImageJ and visualize in Slicer.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.frontiersin.org/articles/10.3389/fcomp.2021.780026/full">
  <header class="source">
      <img src="https://3718aeafc638f96f5bd6-d4a9ca15fc46ba40e71f94dec0aad28c.ssl.cf1.rackcdn.com/favicon_16x16.ico" class="site-icon" width="48" height="48">

      <a href="https://www.frontiersin.org/articles/10.3389/fcomp.2021.780026/full" target="_blank" rel="noopener">Frontiers</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://www.frontiersin.org/files/MyHome%20Article%20Library/780026/780026_Thumb_400.jpg" class="thumbnail">

<h3><a href="https://www.frontiersin.org/articles/10.3389/fcomp.2021.780026/full" target="_blank" rel="noopener">An Open-Source Whole Slide Image Registration Workflow at Cellular Precision...</a></h3>

  <p>Image analysis workflows for Histology increasingly require the correlation and combination of measurements across several whole slide images. Indeed, for multiplexing, as well as multimodal imaging, it is indispensable that the same sample is imaged...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
