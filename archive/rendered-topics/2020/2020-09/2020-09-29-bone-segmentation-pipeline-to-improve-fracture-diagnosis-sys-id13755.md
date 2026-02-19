---
topic_id: 13755
title: "Bone Segmentation Pipeline To Improve Fracture Diagnosis Sys"
date: 2020-09-29
url: https://discourse.slicer.org/t/13755
---

# Bone segmentation pipeline to improve fracture diagnosis system

**Topic ID**: 13755
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/bone-segmentation-pipeline-to-improve-fracture-diagnosis-system/13755

---

## Post #1 by @DanielDauner (2020-09-29 18:36 UTC)

<p>Hello everyone,</p>
<p>I’m currently working on my bachelor thesis. My task is to classify acetabular fractures (pelvis) with machine learning. The data is noisy because the CT scans were collected over many decades and in different clinics in Germany. I created a pipeline with a 3D slicer python script to segment bones. It has the following steps:</p>
<ul>
<li>Normalization</li>
<li>Thresholding</li>
<li>Delete small islands</li>
<li>Smoothing</li>
</ul>
<p>The results so far look great but I am sure the segmentations can be improved. My idea is to use filters to reduce noise in the initial step but I don’t know which filter is suitable for this task. Second of all, I want to ask if there are other steps to improve the segmentation. It’s really important that tiny fractures are separated to classify the fractures later.</p>
<p>Thank you so far for all the help provided in the forum and the published example scripts. My results had some major improvements which wouldn’t have been possible without it.</p>
<p>Best regards,<br>
Daniel</p>

---

## Post #2 by @pieper (2020-10-01 21:23 UTC)

<p>If you haven’t already you should look through this book and then also look at the ITK web site for any updates of any topics.  Pretty much all of the features described are available in Slicer one way or other (e.g. through SimpleFilters).</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://dab4rbh62k56j.cloudfront.net/030594a39810cf6b/img/favicon-196x196.png" class="site-icon" width="16" height="16">
      <a href="https://www.semanticscholar.org/paper/Insight-into-Images:-Principles-and-Practice-for-Yoo/6bbf3af2af555509afbe75c72d3fa05a938fe6be" target="_blank" rel="noopener">semanticscholar.org</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:108/56;"><img src="https://www.semanticscholar.org/img/semantic_scholar_og.png" class="thumbnail" width="108" height="56"></div>

<h3><a href="https://www.semanticscholar.org/paper/Insight-into-Images:-Principles-and-Practice-for-Yoo/6bbf3af2af555509afbe75c72d3fa05a938fe6be" target="_blank" rel="noopener">[PDF] Insight into Images: Principles and Practice for Segmentation,...</a></h3>

<p>A companion to the Insight Toolkit An introduction to the theory of modern medical image processing, including the analysis of data from - X-ray computer tomography, - magnetic resonance imaging, - nuclear medicine, - and ultrasound. Using an...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @DanielDauner (2020-10-02 07:37 UTC)

<p>Thank you Steve. That book seems to be exactly what I need. Unfortunately I can’t get it from the university library because it is lent out. When it is available again, I will take a look at it.</p>

---

## Post #4 by @lassoan (2020-10-03 04:20 UTC)

<p>You may also find this Slicer extension useful, which is developed specifically for bone fracture segmentation: <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify</a></p>
<p>If you need help with specific problems then post more details and at least screenshots (but preferably sample data set) that illustrate the issue.</p>

---

## Post #5 by @DanielDauner (2020-10-03 08:33 UTC)

<p>Thanks a lot Andras. I already saw that program and tested it out. The results are impressive on manual segmentations of the pelvis. The problem is that my script and the bone segmentation has to be automatic. Femur and pelvis are close together and I can’t keep the segments separated without editing it manually. With the femur, I get this segmentation as output:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97dfa6c0a5bd19b42f2fd34debe892b3699542cb.png" alt="Screenshot" data-base62-sha1="lFxgFFaUo2W6ocy1kbC8El3zksX" width="665" height="474"></p>

---

## Post #6 by @DanielDauner (2020-10-03 08:44 UTC)

<p>All the scans vary in intensity, contrast and resolution. My attempt now is to combine an edge detection filter (for example canny detector) with my automatic segmentation. I am running out of ideas but I guess that’s part of the process.</p>

---

## Post #7 by @lassoan (2020-10-03 13:16 UTC)

<p>Unless the image is extremely low noise and high resolution you cannot expect to segment structures using basic global methods, such as thresholding and smoothing.</p>
<p>“Grow from seeds” or “Watershed” effects may be able to separate femur and pelvis fully automatically (from seed points approximately placed by some automatic strategy). You can also utilize the special (almost perfectly spherical) shape of the femur head in some way. However, nowadays most people would create a few hundred segmentations using semi-automatic segmentation tools and then train a deep learning network, which could perform the segmentation fully automatically.</p>
<p>We may be able to give more specific advice if you write more details about your needs and constraints.  What is the goal of the segmentation? Visualization, 3D printing, quantitative analysis (shape, volume distance measurements, …)? What kind of results are acceptable? Why the method has to be fully automatic? Are there experts available for at least 1-2 minutes to specify some manual inputs and review/approve results? What are your time constraints? Do you acquire images intraoperatively and need to provide results within minutes? Or you have tens of minutes or several hours?</p>

---

## Post #8 by @DanielDauner (2020-10-03 15:40 UTC)

<p>My task is to create a convolutional neural network that detects acetabular fractures. Additionally, I have to train another neural network that classifies the type of fracture according to the Letournel classification.</p>
<p>The CT scans are cut in half and mirrored to increase the sample size and to collect scans without fractures. The results were not great on the raw pictures, so I decided to do preprocessing and segment the bones. The segmentations can be used to pretrain the network (transfer learning approach) or to feed them directly into the CNN.</p>
<p>I was told that my pipeline has to be automatic so that the results and the segmentations are reproducible. Otherwise my segmentations could be manipulated until the fracture detection works.</p>
<p>I created the script with your provided code and trained the network only on the segmentations. I had an accuracy of 91% which was a 5% improvement. The script works fine in most cases but has troubles with the variety of contrast and intensity. Therefore I am sure there is room for improvement.</p>
<p>My idea is to enhance the script as best as possible before I show the resulting segmentations to the trauma surgeons that help me with the project.</p>
<p>My deadline is the end of January but the complete program should be finished until the end of the year. In the following weeks, I will get a lot more CT scans but first they have to be labeled and classified by the trauma surgeons.</p>
<p>In a nutshell, the segmentations are not the primary goal and will be used as aggressive preprocessing or pre-training which yielded an improvement so far. I plan to implement everything in a simple gui where the segmentation could be useful for visualization.</p>
<p>Thanks for the help so far.</p>

---

## Post #9 by @lassoan (2020-10-03 16:13 UTC)

<p>If the goal is not segmentation then probably it is OK to not do any sophisticated manual pre-processing. It is hard to tell what preprocessing helps and what hinders the CNN, as it depends on many factors that probably nobody really knows. You just need to try many things and see what works.</p>

---
