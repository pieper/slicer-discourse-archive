---
topic_id: 28733
title: "3D Mri Histology Optical Image Registration Of Cardiac Image"
date: 2023-04-03
url: https://discourse.slicer.org/t/28733
---

# 3D MRI / histology / optical image registration of cardiac images for tissue thickness analysis

**Topic ID**: 28733
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/3d-mri-histology-optical-image-registration-of-cardiac-images-for-tissue-thickness-analysis/28733

---

## Post #1 by @MichaelF (2023-04-03 20:19 UTC)

<p>Dear Slicer Community,</p>
<p>I am looking for help with the co-registration and analysis of 3 different types of data. I have started to develop a pipeline for analysis, but my approach so far has been limited by my experience at managing 3d datasets and I feel there is a lot of potential within 3d Slicer that I am yet to utilise. If anyone can help advise, I would be very appreciative.</p>
<p>I have pre-clinical data for hearts following myocardial infarction, with the following high-resolution data:</p>
<p>A)    Ex vivo 3D MRI (T1w/ T2w) (voxel resolution 125- 175 microns)<br>
B)    Limited histological sections (masson’s staining) -3-4 per axial sections per heart<br>
C)    2D optical mapping (OM) data (electrophysiology recordings from the front of the heart) from 100x100 pixel array, resolution 320 microns.</p>
<p>I am now looking at ways to improve the co-registration of these three data sets. The histological samples are limited and primarily intended to validate the MRI segmentations. Perhaps, by chance, there will also be some interesting electrophysiology where the histology was sampled.</p>
<p>My primary aim is to correlate structural features (such as scar thickness measured in the axial stack) with the overlying surface electrophysiology data (OM), recorded as a 2d data set from the front of the heart.</p>
<p>The following is my intended analysis pipeline:</p>
<ol>
<li>Histopathological validation of MRI to inform segmentation (i.e. SI characteristics of scar, fat, normal myocardium &amp; perhaps heterogeneous tissue)</li>
</ol>
<ul>
<li>
<pre><code>  registration of axial slices MRI to corresponding histology
</code></pre>
</li>
<li>
<pre><code>  note imperfect slice alignment may therefore require 3d data transformation / manual alignment
</code></pre>
</li>
</ul>
<ol start="2">
<li>Segmentation of scar &amp; normal myocardium</li>
</ol>
<ul>
<li>
<pre><code>   seems to work well already with 3d slicer 
</code></pre>
</li>
</ul>
<ol start="3">
<li>Thickness measurement of (i) scar and (ii) myocardium (iii) mixed tissue from axial stack</li>
</ol>
<ul>
<li>
<pre><code>  Need to develop methodology to measure thickness of scar/ myocardium &amp; mixed at each radial position in the axial stack (i.e. is this possible using the mesh segmentation) 
</code></pre>
</li>
</ul>
<ol start="4">
<li>3d volume render to generate epicardial surface with fiducials (i.e. scar and vascular markings)</li>
</ol>
<ul>
<li>
<pre><code>  Working reasonably well in 3d slicer
</code></pre>
</li>
<li>
<pre><code>  I am currently getting better results with Horos, but I suspect the same is possible with 3d slicer with more experience
</code></pre>
</li>
</ul>
<ol start="5">
<li>Mapping of thickness measurement values to surface</li>
</ol>
<ul>
<li>
<pre><code>  Is this possible? Ideally to display this as a heat map on the 3d render
</code></pre>
</li>
<li>
<pre><code>  Ideally, in a separate projection I would also display some measure of the change in thickness (i.e. high values corresponding to sudden changes in thickness)
</code></pre>
</li>
</ul>
<ol start="6">
<li>Identification of fiducial markers using a black &amp; white photo taken in the same field of view &amp; resolution as the OM data</li>
</ol>
<ul>
<li>
<pre><code>  using the same vascular and scar features from the anterior heart as above
</code></pre>
</li>
</ul>
<ol start="7">
<li>Co-registration of fiducials from the 2D OM photo (above) with the fiducials on the 3D volume render from MRI</li>
</ol>
<ul>
<li>
<pre><code>  ideally to achieve the best possible approximate location of the same fiducials as there will be limitations. Manually if necessary! 
</code></pre>
</li>
<li>
<pre><code>  thereafter, using OM data in the same field of view (&amp;resolution) project these results as a heat map onto the 3D volume (MRI) 
</code></pre>
</li>
</ul>
<ol start="8">
<li>Correlation of summative structural data (i.e. thickness) and relevant OM data</li>
</ol>
<p>From this list I am primarily interested in advice regarding 3) 5) 7) &amp; 8), nevertheless all advice is very welcome!</p>
<p>Many thanks for your time and consideration</p>

---

## Post #2 by @MichaelF (2023-04-08 14:27 UTC)

<p>Does anyone have any suggestions? All help would be really appreciated!</p>

---

## Post #3 by @muratmaga (2023-04-08 15:43 UTC)

<p>At one point DRAMMS package was developed specifically with that in mind. I do not know if it is maintained still.<br>
<a href="https://www.nitrc.org/projects/dramms/" class="onebox" target="_blank" rel="noopener">https://www.nitrc.org/projects/dramms/</a></p>

---

## Post #4 by @MichaelF (2023-04-12 09:35 UTC)

<p>Hi thanks very much for the suggestion. There does seem to be some issues with that software unfortunately. I note that several other people have had the same issue.</p>
<p>Do you think any of my objectives above would be achievable using 3D slicer?</p>

---
