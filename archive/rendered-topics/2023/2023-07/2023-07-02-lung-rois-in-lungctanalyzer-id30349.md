# Lung ROIs in LungCTAnalyzer

**Topic ID**: 30349
**Date**: 2023-07-02
**URL**: https://discourse.slicer.org/t/lung-rois-in-lungctanalyzer/30349

---

## Post #1 by @Marco_Leali (2023-07-02 11:22 UTC)

<p>Hello everybody. I am using LungCTAnalyzer for a research project: wonderful extension! However, I was wondering about which method LungCTAnalyzer uses to divide lungs into a ventral and a dorsal ROI: is it 50% of the lung maximum height? How would you describe it in section “methods”? I would be grateful if the creator <a class="mention" href="/u/rbumm">@rbumm</a> could provide support.</p>

---

## Post #2 by @rbumm (2023-07-02 12:18 UTC)

<p>Hello Marco,</p>
<p>fantastic that you appreciate the extension.</p>
<p>Using the segment statistics module of 3D Slicers, the extension determines the centroid ras coordinate for each lung.</p>
<p>The “ventral” part of the lung is built as follows:</p>
<p>(1) All examined lung segments of that side are duplicated.<br>
(2) After creating a matching cube with markups and using “Erase inside” to the cube’s content, 3D Slicer’s Segment Editor “Surface Cut” effect is used to remove the dorsal half taking into account the centroid location. In this manner, the ventral lung’s volumes of interest are the only ones left.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9b3f786824e4090a6852bc8b2ff10ffe2b5484b.jpeg" data-download-href="/uploads/short-url/zCYsYPIw0lwG9sFGHzcLAgJ7q3h.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9b3f786824e4090a6852bc8b2ff10ffe2b5484b_2_394x500.jpeg" alt="image" data-base62-sha1="zCYsYPIw0lwG9sFGHzcLAgJ7q3h" width="394" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9b3f786824e4090a6852bc8b2ff10ffe2b5484b_2_394x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9b3f786824e4090a6852bc8b2ff10ffe2b5484b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9b3f786824e4090a6852bc8b2ff10ffe2b5484b.jpeg 2x" data-dominant-color="9091A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">517×656 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The function is realized <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/e72868c1911c96a91e2b37a3b76955c8a70bd8bd/LungCTAnalyzer/LungCTAnalyzer.py#L2576">in the Python script</a> but below is shown how to do it manually.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50e1bb8444feeb706faff4db5edcfa81b277d058.png" data-download-href="/uploads/short-url/bxvPhYXnEhLVhxEHsLjYjtEHATK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50e1bb8444feeb706faff4db5edcfa81b277d058_2_406x500.png" alt="image" data-base62-sha1="bxvPhYXnEhLVhxEHsLjYjtEHATK" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50e1bb8444feeb706faff4db5edcfa81b277d058_2_406x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50e1bb8444feeb706faff4db5edcfa81b277d058.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50e1bb8444feeb706faff4db5edcfa81b277d058.png 2x" data-dominant-color="EEEDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×709 55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best<br>
r</p>

---

## Post #3 by @Marco_Leali (2023-07-02 13:18 UTC)

<p>Thank you very much for your prompt response. The centroid is determined as if the whole lung segment had homogeneous density, isn’t it? So that, by definition, 50% of the lung <em>volume</em> will be kept in the ventral ROI and 50% of the lung <em>volume</em> will be cut by “surface cut” tool. Is my understanding correct?</p>

---

## Post #4 by @rbumm (2023-07-02 13:43 UTC)

<p>Not exactly.</p>
<p>See here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://chat.openai.com/share/0a7eabf5-e46d-4978-894c-d3e98f5368b4">
  <header class="source">
      <img src="https://chat.openai.com/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://chat.openai.com/share/0a7eabf5-e46d-4978-894c-d3e98f5368b4" target="_blank" rel="noopener">ChatGPT</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://chat.openai.com/share/0a7eabf5-e46d-4978-894c-d3e98f5368b4" target="_blank" rel="noopener">ChatGPT</a></h3>

  <p>A conversational AI system that listens, learns, and challenges</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and here:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Segment</th>
<th>Number of voxels [voxels] (1)</th>
<th>Volume [mm3] (1)</th>
<th>Volume [cm3] (1)</th>
<th>Centroid</th>
<th>OBB origin</th>
<th>OBB diameter [mm]</th>
<th>OBB X direction</th>
<th>OBB Y direction</th>
<th>OBB Z direction</th>
<th>Number of voxels [voxels] (2)</th>
<th>Volume [mm3] (2)</th>
<th>Volume [cm3] (2)</th>
<th>Minimum</th>
<th>Maximum</th>
<th>Mean</th>
<th>Median</th>
<th>Standard Deviation</th>
<th>Surface area [mm2]</th>
<th>Volume [mm3] (3)</th>
<th>Volume [cm3] (3)</th>
</tr>
</thead>
<tbody>
<tr>
<td>right lung anterior</td>
<td>3264838</td>
<td>1.37309e+06</td>
<td>1373.09</td>
<td>54.7007 65.8004 -117.272</td>
<td>114.187 -30.2649 -255.738</td>
<td>137.078 199.452 239.165</td>
<td>0.467616 0.829749 0.304718</td>
<td>-0.876122 0.480797 0.0352707</td>
<td>-0.117242 -0.283463 0.951789</td>
<td>3264838</td>
<td>1.37309e+06</td>
<td>1373.09</td>
<td>-1024</td>
<td>762</td>
<td>-831.541</td>
<td>-870.035</td>
<td>140.353</td>
<td>89553.4</td>
<td>1.38085e+06</td>
<td>1380.85</td>
</tr>
<tr>
<td>right lung posterior</td>
<td>3788027</td>
<td>1.59313e+06</td>
<td>1593.13</td>
<td>61.1447 -21.1237 -110.671</td>
<td>-29.5151 -65.0638 12.2558</td>
<td>106.661 146.044 246.468</td>
<td>0.0218395 0.995805 -0.0888537</td>
<td>0.992706 -0.0110596 0.120052</td>
<td>0.118566 -0.0908275 -0.988783</td>
<td>3788027</td>
<td>1.59313e+06</td>
<td>1593.13</td>
<td>-1024</td>
<td>1121</td>
<td>-774.699</td>
<td>-823.046</td>
<td>171.703</td>
<td>90095.9</td>
<td>1.60216e+06</td>
<td>1602.16</td>
</tr>
</tbody>
</table>
</div>

---

## Post #5 by @Marco_Leali (2023-07-02 14:42 UTC)

<p>Thank you very much for you support. However, I am dubious about the AI interpretation: I tried to reformulate the question and it gave a different answer. To my knowledge, centroid calculation should yield the center of mass of an object with homogeneous density, by definition. This is why I wonder whether the volume discrepancies you have pointed out are due to discrete sampling. Should I start a thread asking for support from the segment statistics module authors?</p>

---

## Post #6 by @rbumm (2023-07-02 16:12 UTC)

<p>To my understanding, the center of mass of a lung lobe will not guarantee that cutting the organ axially, sagitally, or coronary in that position will always result in two identical volumes of the divided organ as shape and size of the organ, as well as the location of the division plane, can affect the resulting volumes.<br>
Maybe <a class="mention" href="/u/lassoan">@lassoan</a> or <a class="mention" href="/u/pieper">@pieper</a> can comment?</p>

---

## Post #7 by @pieper (2023-07-02 17:38 UTC)

<p>If i’m following correctly it sounds like <a class="mention" href="/u/marco_leali">@Marco_Leali</a> may be asking for a different calculation that takes into account the density of the lung tissue and maybe calculates a cutting plane that allocates 50% of the density to the dorsal and ventral portions (or apportions 50% of the volume to each?).  In any case I believe the technique based on the centroid will be an approximation of that based purely on geometric calculations.</p>

---

## Post #8 by @lassoan (2023-07-02 19:17 UTC)

<p>Is there a definition of this cutting plane that is widely used in clinical practice? If yes, then we must use that. If not, then we can freely choose a definition - something simple and reproducible.</p>

---

## Post #9 by @Marco_Leali (2023-07-02 19:58 UTC)

<p>Thank you for your response. I beg your pardon: I realized that I was completely wrong about centroid definition. I greatly appreciated your patience. The need for precision about ventral/dorsal separation is for research applications in ARDS, where the point in separating dorsal from ventral areas is that the former have superimposed hydrostatic pressure (and other gravity-dependent phenomena going on). In that case the focus would be more on geometric height than on the centroid. See this (doi: 10.1097/00000542-199101000-00004) as a well-known reference in our field.</p>

---

## Post #10 by @rbumm (2023-07-03 09:52 UTC)

<p>As far as I see there is no clear definition of this cutting plane available, so using the centroid level makes sense for now.<br>
Today masks for “upper half” and “lower half” of the lungs were added for convenience.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c8dbcfc8486ac844f4461e1209a65489f964578.jpeg" alt="image" data-base62-sha1="6m8Gfvk2gqR0hXm7vqUaAL3eaLe" width="588" height="372"></p>

---
