---
topic_id: 7286
title: "Open Atlas Followup"
date: 2019-06-23
url: https://discourse.slicer.org/t/7286
---

# Open Atlas Followup

**Topic ID**: 7286
**Date**: 2019-06-23
**URL**: https://discourse.slicer.org/t/open-atlas-followup/7286

---

## Post #1 by @Lorensen (2019-06-23 22:00 UTC)

<p>Folks,</p>
<p>At the 2015 Winter Project Week, I presented and improved a project called <a href="https://na-mic.org/wiki/2015_Winter_Project_Week:OpenAtlas" rel="nofollow noopener">Open Atlas</a>. After that meeting, I did further improvements. Jesica Forbes and <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a>  approached me about using the tools on their MRI BRAINS atlases. I made further improvements that made the tools useful for them. Jessica presented a poster called <a href="https://drive.google.com/open?id=1KE3fhz6mALsJUNtJvR0GSjvBIrOVqC2m" rel="nofollow noopener">“Visualization and Utilization of Medical Imaging Atlas Correction Tools”</a>. Susequently Jessica, Hans and others published <a href="https://www.frontiersin.org/articles/10.3389/fninf.2016.00029/full" rel="nofollow noopener">“An Open-Source Label Atlas Correction Tool and Preliminary Results on Huntingtons Disease Whole-Brain MRI Atlases”</a>.</p>
<p>I had put this project on the back burner. I recently rebuild it with newer vtk and itk versions.</p>
<p>Here are some of the features:</p>
<ol>
<li>Creates an <a href="https://github.com/lorensen/SPLBrainAtlas/blob/master/Models/adjacencies.txt" rel="nofollow noopener">adjacency map</a> for each label.</li>
<li>Creates <a href="https://github.com/lorensen/SPLBrainAtlas/blob/master/Statistics/fourth_ventricle-15.txt" rel="nofollow noopener">statistics</a> for each label.</li>
<li>Generates <a href="https://github.com/lorensen/SPLBrainAtlas/blob/master/Models/STL/anterior_part_of_left_middle_frontal_gyrus-1027.stl" rel="nofollow noopener">STL files</a> for each label.</li>
<li>Generates<a href="https://github.com/lorensen/SPLBrainAtlas/blob/master/Models/VTK/anterior_part_of_left_middle_frontal_gyrus-1027.vtk" rel="nofollow noopener">.vtk files</a> showing labeled voxels as cubes for each label.</li>
<li>Generates <a href="https://github.com/lorensen/SPLBrainAtlas/blob/master/Models/Screenshot/anterior_part_of_left_middle_frontal_gyrus.png" rel="nofollow noopener">screenshots</a> with one viewport showing the .stl model and its adjacencies. The other viewport shows the .vtk cube models with its adjacencies. Views are selected automatically based on the left/right/centered label names.</li>
<li>Generates a <a href="https://drive.google.com/open?id=1le5M85oe7PClBiBOY7lfWhGIJ9z7AN2l" rel="nofollow noopener">mrml scene</a> for the atlas. The scene also has markups for labels that have disconnected regions.</li>
<li>Generates “<a href="https://github.com/lorensen/SPLBrainAtlas/blob/695d6552ad0612236d13bcebd2c3e841cf6632a4/Changes/fourth_ventricle_diff.png" rel="nofollow noopener">diff images</a>” for edited labels.</li>
</ol>
<p>Are these useful tools for the Slicer Community? If so, I’d be happy to work with someone to integrate some or all into Slicer.</p>
<p>Bill</p>
<p>BTW I’ve run the tools in the SPLBrainAtlas, SPLKneeAtlas, SPLHeadNeckAtlas, SPLAbdominalAtlas, ICBMBrainAtlas FreeSurferSampleAtlas and 107 <a href="https://mindboggle.info/" rel="nofollow noopener">Mindboggle</a>  segmentations.</p>

---

## Post #2 by @pieper (2019-06-26 00:12 UTC)

<p>Hey Bill -</p>
<p>Thanks for keeping this going, looks great.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> and I will work on an extension for this code tomorrow.</p>
<p>Cheers from project week! (Actually from the post-hacking sushi bar outing).</p>

---

## Post #3 by @Tina_Kapur (2019-06-26 13:53 UTC)

<p>Hi Bill!  Great to hear from you.  Mike is sending you something.</p>

---

## Post #4 by @Lorensen (2019-06-26 21:59 UTC)

<p>Wish I was there to help. I sure miss Project Week.</p>

---

## Post #5 by @Tina_Kapur (2019-06-27 02:31 UTC)

<p>Why not come again? How’re you doing?</p>

---

## Post #6 by @rkikinis (2019-06-27 02:40 UTC)

<p>And we are missing you</p>

---

## Post #7 by @Lorensen (2019-06-27 04:05 UTC)

<p>Tina,</p>
<p>Doing well, but my traveling days are over…</p>
<p>Bill</p>

---

## Post #8 by @Tina_Kapur (2019-06-27 09:30 UTC)

<p>How about joining by video conference? Just to say hello to everyone?</p>

---
