---
topic_id: 1544
title: "Cardiac Agatston Scoring Module"
date: 2017-11-28
url: https://discourse.slicer.org/t/1544
---

# Cardiac Agatston Scoring module

**Topic ID**: 1544
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/cardiac-agatston-scoring-module/1544

---

## Post #1 by @Emily_BM (2017-11-28 17:52 UTC)

<p>I require help regarding use of 3d slicer module “CardiacAgatstonScoring”.This module isnt showing in any version except 4.4 but in 4.4 when i click Apply(for calculating calcium score)it doesnt work</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ihnorton (2017-11-28 19:03 UTC)

<p>That module appears to be available in the Extension Manager in both Slicer 4.8 on Windows and a recent nightly that I had open on Mac. So please try either Slicer 4.8 or the most recent nightly.</p>
<ul>
<li>
<p>Before using on your own data, the first step is to try the test data and tutorial here:</p>
<p><a href="https://na-mic.org/wiki/2014_Summer_Prioject_Week:AgatstonScoring" class="inline-onebox">2014 Summer Prioject Week:AgatstonScoring - NAMIC Wiki</a></p>
</li>
<li>
<p>Someone might suggest a quick fix if you post the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog#To_capture_the_entire_error_log_for_a_report">Error Log</a> – click the gray (or probably red) circle with X at the bottom-right part of the window:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19aa5bab8bea8de7a8579f4ce4323125a305fe37.png" alt="image" data-base62-sha1="3F2VushLW0vCgNRzvHrJJQ1RWHZ" width="115" height="93"></p>
</li>
<li>
<p>you could also try <a href="https://github.com/BRAINSia/CardiacAgatstonMeasures/issues">filing an issue</a> with the information above (error log, etc.), however, this extension has not been updated for several years and may no longer be maintained.</p>
</li>
</ul>

---

## Post #3 by @lassoan (2017-11-28 20:40 UTC)

<p>I had a look at the module and it is quite outdated and had some errors when I tried to launch its thresholding function. It would be nice if somebody could fix it up, switch to use Segment Editor, etc.</p>
<p>However, you can compute Agatston score by a few simple steps, without the CardiacAgatstonScoring module:</p>
<ul>
<li>Load your CT</li>
<li>Switch to <code>Segment Editor</code> module</li>
<li>Add a new segment</li>
<li>Use <code>Threshold</code> effect to segment calcifications. Set lower threshold value to 130 (for 120 keV images) or 167 (for 80 keV images). Click <code>Apply</code>.</li>
<li>Add a segment for each vessel segment (LM, LAD, LCX, RCA)</li>
<li>To assign each disconnected segmented structure to one of the vessel segments. Select Select <code>Islands</code> effect and choose <code>Add selected island</code> option. Then, to assign an island to a vessel segment: select the corresponding segment in the list (for example “RCA”) and click the island in the slice viewer that you would like to add to that segment.</li>
<li>Use <code>Segment Statistics</code> module to compute volume, mean an max intensity, etc. for each segment.</li>
<li>Use File / Save to save statistics result to .csv file that you can load into Excel for computing the Agatston score.</li>
</ul>

---

## Post #4 by @Emily_BM (2017-11-29 16:58 UTC)

<p>Thanks for the Response!!<br>
I have to calculate Total Agatston score of RCA only.After performing the<br>
steps you have mentioned above I have Statistics such as volume,total voxel<br>
number,  mean an max intensity(of whole RCA not of single slice).<br>
Do I just have to multily the max intensity number with Area to<br>
calculate Agatston<br>
score?or will calculate (slice by slice) agatston score and add up at end?</p>

---

## Post #5 by @lassoan (2017-11-29 17:47 UTC)

<p>There are several variants of the metric. If you need to compute the metric slice by slice then you can use Mask volume effect (available in Segment Editor module after you install SegmentEditorExtraEffects extension) to create a volume where all voxels are blanked out except the calcifications in the selected vessel and compute the total score using this script:</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02" target="_blank">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02" target="_blank">https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02</a></h4>
<h5>CardiacAgatstonScoring</h5>
<pre><code class=""># There are several variants of the metric. If you need to compute the metric slice by slice then
# you can use Mask volume effect (available in Segment Editor module after you install SegmentEditorExtraEffects
# extension) to create a volume where all voxels are blanked out except the calcifications in the selected vessel
# and compute the total score using this script.

def computeAgatstonScore(volumeNode, verbose=False):
  import numpy as np
  import math
  voxelArray = slicer.util.arrayFromVolume(volumeNode)
  areaOfPixelMm2 = volumeNode.GetSpacing()[0] * volumeNode.GetSpacing()[0]</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02" target="_blank">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Just open the Python console and copy-paste this script (change <code>CTChest masked</code> to the actual name of your masked volume).</p>

---

## Post #7 by @NFQ (2018-08-22 13:33 UTC)

<p>Hi@Andras Lasso,<br>
I am trying to calculate agatston score in a single vessel(RCA).Do I need to segment plaque slice by slice.And write the above script to determine agatston score of a single plaque lession(per slice).And at the end add  agatston scores of all slices manually to calculate the total agatston score of a single vessel. ??</p>

---

## Post #8 by @lassoan (2018-08-22 16:15 UTC)

<p>I’ve updated the post above with a link to the current version of the script.</p>

---

## Post #9 by @lassoan (2018-08-31 18:41 UTC)

<aside class="quote no-group" data-username="NFQ" data-post="7" data-topic="1544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8491ac/48.png" class="avatar"> NFQ:</div>
<blockquote>
<p>I am trying to calculate agatston score in a single vessel(RCA).Do I need to segment plaque slice by slice</p>
</blockquote>
</aside>
<p>You need to segment the plaque in that vessel, using any of the tools in Segment editor. Probably the best is to use <em>Paint</em> effect with a large brush, <em>Sphere</em> option enabled (so that you don’t have to paint on each and every slice), <em>Masking</em> / <em>Editable intensity range</em> option enabled (range set to 100-3000; so that only calcifications are highlighted). After segmentation is completed, export the segmentation to a labelmap (using Segmentations module <em>Export/Import…</em> section).</p>
<aside class="quote no-group" data-username="NFQ" data-post="7" data-topic="1544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8491ac/48.png" class="avatar"> NFQ:</div>
<blockquote>
<p>And write the above script to determine agatston score of a single plaque lession(per slice).And at the end add agatston scores of all slices manually to calculate the total agatston score of a single vessel. ??</p>
</blockquote>
</aside>
<p>The script computes score for each slice and then reports the sum.</p>

---

## Post #10 by @NFQ (2018-10-07 19:19 UTC)

<p>Thanks@ Andras Lasso,<br>
I just have a query related to the updated script by yourself in the above discussion.<br>
In this script highest /maximum intensity factor was set to 100(all pixels above 100 CT density/HU will be consider for calcium scoring.isnt it?).<br>
But according to the literature and (by3D slicer tutorial regarding agatston scoring),it is 130 HU for 120 KvP and 167 HU for 167 kvP.Right?Do we need to correct that.<br>
secondly,area in mm2 should be the area covered by 3 consecuive voxels .is this algo calculating area based on this principle?<br>
Thanks,</p>

---

## Post #11 by @lassoan (2018-10-07 19:59 UTC)

<p>Feel free to modify the threshold as you see fit. If you can give reference to a paper then I’ll update the example script accordingly.</p>
<p>What do you mean by “3 consecutive voxels”? Is there a minimum blob size within a slice? Or the same pixel position must be above the threshold on 3 consecutive slices?</p>
<p>Would you be interested in converting the example script to a Slicer module?</p>

---

## Post #12 by @NFQ (2018-10-10 18:02 UTC)

<p>Thanks for your response!!<br>
“If you can give reference to a paper then I’ll update the example script accordingly.”</p>
<p>sure.Here are the links of the papers.<br>
<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4091626/" rel="nofollow noopener">Paper1</a><br>
<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3075464/" rel="nofollow noopener">Paper2</a><br>
According to these papers"To qualify as a calcified plaque using CAC scoring, the plaque calcium density, measured in Hounsfield units, must be 130 Hu or higher."</p>
<p>"What do you mean by “3 consecutive voxels”?</p>
<p>According to paper2 “Agatston score, requiring 3 contiguous voxels of &gt;=130 Hounsfield units to be classified as calcified plaque”.Means…for example if we have one CT slice with a calcified spot occupying 4 consecutive pixels,if just 2 out of that 5 pixels are &gt;=130 HU than we cant classify it as calcified plaque/agatston score.</p>
<p>“Would you be interested in converting the example script to a Slicer module?”<br>
No.I just want to understand how the algorithm is working.And if I apply this algorithm to calculate calcium score of my dataset than is it calculating the score according to the principles/my conditions.So basically I want to modify it based on the informaion i have mentioned above(&gt;=130HU and 3 consecutive pixels).</p>

---

## Post #13 by @lassoan (2018-10-12 00:18 UTC)

<p>I’ve checked Paper1 referenced above. They wrote the requirement was <em>contiguous</em> voxels (consecutive would require sequence of voxels, which cannot be interpreted on an image slice), so this is clear now. My other concern was defining minimum size as number of voxels, because voxel size depends on the image acquisition protocol. However, they wrote that they used minimum surface area of 1mm^2 (which happened to be 3 voxels for their imaging protocol). We can use the 1mm^2 value.</p>
<p>I’ve updated the score computation to use minimum threshold value for island separation, discard small islands, and compute score per island - see latest revision of the <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02">script</a>.</p>

---

## Post #15 by @Laode_Muhammadin_Mat (2022-08-28 09:32 UTC)

<p>Is there an extension that can be used directly to assess the coronary calcium score/agatsone score?</p>

---

## Post #16 by @lassoan (2022-08-28 11:59 UTC)

<p>We have not put the <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02">Cardiac Agatston Scoring script</a> into an extension yet, so you need to copy-paste the code into Slicer’s Python console. If you can confirm that the script is useful and works well then I can add it as an extension to allow installing and running the analysis by a few clicks.</p>

---

## Post #17 by @Omar_El-Taji (2023-05-01 01:06 UTC)

<p>Hi</p>
<p>I am trying to download this extension from <a href="http://brainsia.github.io/CardiacAgatstonMeasures/" class="inline-onebox" rel="noopener nofollow ugc">Cardiac Agatston Measures by BRAINSia</a><br>
I cannot seem to install it I keep getting error message.<br>
Is this still available?</p>
<p>I am trying to get an agatston score for the abdominal aorta only.</p>
<p>Thanks</p>

---

## Post #18 by @lassoan (2023-05-02 19:14 UTC)

<p>You don’t need to install the script, just copy-paste it into Slicer’s Python console.</p>

---

## Post #19 by @Omar_El-Taji (2023-05-09 17:24 UTC)

<p>Hi Andras,</p>
<p>Thanks for the response.</p>
<p>I have followed instructions as above–&gt; Segment the plaque in aorta, using Paint effect and Masking. I then exported using the segmentation module to a label map.<br>
I then used the script provided. I got a total score of 0 which based on the CT aorta is incorrect. It’s based on the example CTA abdo panoramic provided.</p>
<p>This is what I got:</p>
<pre><code class="lang-python">def computeAgatstonScore(volumeNode, minimumIntensityThreshold=130, minimumIslandSizeInMm2=1.0, verbose=False):
  import numpy as np
  import math
  import SimpleITK as sitk
  voxelArray = slicer.util.arrayFromVolume(volumeNode)
  areaOfPixelMm2 = volumeNode.GetSpacing()[0] * volumeNode.GetSpacing()[1]
  minimumIslandSizeInPixels = int(round(minimumIslandSizeInMm2/areaOfPixelMm2))
  numberOfSlices = voxelArray.shape[0]
  totalScore = 0
  for sliceIndex in range(numberOfSlices):
    voxelArraySlice = voxelArray[sliceIndex]
    maxIntensity = voxelArraySlice.max()
    if maxIntensity &lt; minimumIntensityThreshold:
      continue
    # Get a thresholded image to analyse islands (connected components)
    # If island size less than minimum size then it will be discarded.
    thresholdedVoxelArraySlice = voxelArraySlice&gt;minimumIntensityThreshold
    sliceImage = sitk.GetImageFromArray(voxelArraySlice)
    thresholdedSliceImage = sitk.GetImageFromArray(thresholdedVoxelArraySlice.astype(int))
    labelImage = sitk.ConnectedComponentImageFilter().Execute(thresholdedSliceImage)
    stats = sitk.LabelStatisticsImageFilter()
    stats.Execute(sliceImage, labelImage)
    numberOfNonZeroVoxels = 0
    numberOfIslands = 0
    sliceScore = 0
    for labelIndex in stats.GetLabels():
      if labelIndex == 0:
        continue
      if stats.GetCount(labelIndex) &lt; minimumIslandSizeInPixels:
        continue
      maxIntensity = stats.GetMaximum(labelIndex)
      weightFactor = math.floor(maxIntensity/100)
      if weightFactor &gt; 4:
        weightFactor = 4.0
      numberOfNonZeroVoxelsInIsland = stats.GetCount(labelIndex)
      sliceScore += numberOfNonZeroVoxelsInIsland * areaOfPixelMm2 * weightFactor
      numberOfNonZeroVoxels += numberOfNonZeroVoxelsInIsland
      numberOfIslands += 1
    totalScore += sliceScore
    if (sliceScore &gt; 0) and verbose:
      print("Slice {0} score: {1:.1f} (from {2} islands of size &gt; {3}, {4} voxels)".format(
        sliceIndex, sliceScore, numberOfIslands, minimumIslandSizeInPixels,
        numberOfNonZeroVoxels))
      slicer.app.processEvents()
  return totalScore

print("Total Agatston score: {0}".format(computeAgatstonScore(getNode('Segmentation-Calcification-label'), verbose=True)))
</code></pre>
<pre><code>Total Agatston score: 0
</code></pre>

---

## Post #20 by @lassoan (2023-05-10 04:15 UTC)

<p>The input to the algorithm is a masked volume, not a labelmap. The reason is that the computation requires the original HU values. I’ve uploaded a sample masked data set <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/CardiacAgatstonScore.mrb">here</a>.</p>
<p>It would be great if you could test if the results look good to you. I’ve just implemented the algorithm based on the reference paper and have not compared the results to known implementations. I’ve updated the script with some more detailed logging of computation details so that you can verify the results more easily.</p>

---

## Post #21 by @Omar_El-Taji (2023-05-10 14:22 UTC)

<p>Hi</p>
<p>Thanks for the response. I have tried it on the sample data and it is giving a reasonable reading.</p>
<p>I have now tried it on my own scan using the updated script but it’s giving me errors. I think it’s probably the masking. I tried to mask in segment editor–&gt;masking (I have attached a screenshot of the masking process and masked data set). is this the correct way to mask?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7960dbac5eac142735be1219ed1107e4fd202ea.jpeg" data-download-href="/uploads/short-url/x2HMC3ZIFJPuwdWyWJcc9Vje7ge.jpeg?dl=1" title="Screenshot 2023-05-10 at 15.16.57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7960dbac5eac142735be1219ed1107e4fd202ea_2_690x421.jpeg" alt="Screenshot 2023-05-10 at 15.16.57" data-base62-sha1="x2HMC3ZIFJPuwdWyWJcc9Vje7ge" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7960dbac5eac142735be1219ed1107e4fd202ea_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7960dbac5eac142735be1219ed1107e4fd202ea_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7960dbac5eac142735be1219ed1107e4fd202ea_2_1380x842.jpeg 2x" data-dominant-color="DCD8D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-10 at 15.16.57</span><span class="informations">1920×1173 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/453fbfc23a3dcfe754c2da572b19aa9210326ae7.jpeg" data-download-href="/uploads/short-url/9SBwGvkwCz0AJXm6Ukbzf6lrs23.jpeg?dl=1" title="Screenshot 2023-05-10 at 15.21.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453fbfc23a3dcfe754c2da572b19aa9210326ae7_2_690x397.jpeg" alt="Screenshot 2023-05-10 at 15.21.58" data-base62-sha1="9SBwGvkwCz0AJXm6Ukbzf6lrs23" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453fbfc23a3dcfe754c2da572b19aa9210326ae7_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453fbfc23a3dcfe754c2da572b19aa9210326ae7_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453fbfc23a3dcfe754c2da572b19aa9210326ae7_2_1380x794.jpeg 2x" data-dominant-color="CAC9C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-05-10 at 15.21.58</span><span class="informations">1920×1107 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @lassoan (2023-05-10 16:43 UTC)

<p>It seems it is just a typo in the node name (you typed an extra “S” at the beginning of the name).</p>

---

## Post #23 by @Keefe_Lai (2023-06-02 09:14 UTC)

<p>Hi Andras, many thanks for the code.  Could I ask what the license is for the code?  In the distant future, I may incorporate this as part of a chargeable service in my (public) hospital (in addition to segmenting other structures).</p>

---

## Post #24 by @Keefe_Lai (2023-06-02 09:17 UTC)

<p>Also, how may I cite this script/your work?</p>

---

## Post #25 by @lassoan (2023-06-03 18:58 UTC)

<p>THe best would be if you could add the script as a module to Sandbox extension (use Extension Wizard module to create a skeleton, add GUI for the input parameters, and copy the processing script to the module logic class).</p>
<p>The BSD license of the <a href="https://github.com/PerkLab/SlicerSandbox">Sandbox extension</a> would apply and you could cite the Sandbox extension and the Agatston 1990 paper.</p>

---

## Post #26 by @curtislisle (2023-06-04 08:47 UTC)

<p>. t has been a while since I wrote a Python slicer module, but I’d be willing to work on this during Project Week. It would be nice to have this as a Slicer module again. I’ll discuss this at the preparation call this week</p>

---

## Post #27 by @Keefe_Lai (2023-06-04 12:56 UTC)

<p>Thank you Andras and Curtis!  It would indeed fill an important need to have Agatston scoring in Slicer again.</p>

---

## Post #28 by @SYL (2023-07-10 13:26 UTC)

<p>SO ，have it done?<br>
so,i dont understand above progress, i need to caculate the cadiac agaston scoring . but i feel it is alittle difficult for me .</p>

---

## Post #29 by @curtislisle (2023-07-10 19:45 UTC)

<p>Apologies. I started the module and Andras has offered support. Unfortunately, I didn’t finish during the project week and have been swamped with other projects since returning to my office. I’ll try to get back to the agatston module during this coming week. Thanks for your patience.</p>

---

## Post #31 by @lassoan (2023-07-11 19:33 UTC)

<p><a class="mention" href="/u/syl">@syl</a> Your last message was too harsh and demanding - does not match the friendly tone of this community. This is a problem because people you are trying to pressure here are volunteering to help the community in their free time and if you use unpleasant tone then they will unlikely to help you - and you may even discourage them to help others.</p>
<p>If you urgently need this feature then you can offer your help: Python programming is not a very difficult job, you can learn how to do it while developing this module; or you can ask friends of yours to help you; or you can offer funding to someone who already has the right skills.</p>
<p>If it is not that urgent then you can wait patiently for someone to take on this job for free. Maybe you can come back to this post in every couple of weeks and indicate in a friendly comment that you are still interested in this feature.</p>

---

## Post #32 by @SYL (2023-11-14 14:00 UTC)

<p>so, excuseme i still focus the agatston module. can i try to use this module now?thanks.</p>

---

## Post #33 by @curtislisle (2023-11-15 16:52 UTC)

<p>The effort on an agatston module, which I started over the Summer, is not complete. However, I am planning to resume work on this module before and during the next Slicer Project Week in January.</p>

---

## Post #34 by @Emmanuel_Candus (2024-06-15 17:07 UTC)

<p>Hello</p>
<p>Many thanks for this interesting topic.<br>
I am a new user and I am looking at the posted script.</p>
<p>When I a trying to validate the outputs against what I can see on the net.<br>
I am a little bit puzzled by the output of the GE SmartScore against Slicer and other vendors.</p>
<p>Volume and AJ130 are not in line with the expected range.<br>
Given a 3mm thick slices<br>
ex: SmartScore-2.jpg<br>
If volume = 106 → Area = 106/3 = 35mm²<br>
Max AJ130 = Area * 4 = 141 (far away from 285)</p>
<p>Vitae and other systems (like Slicers) are producing more coherent figures.</p>
<p>Do you think that there exist some kind of new or different methodology ?<br>
Is there a specific pre treatment that must be done ?<br>
slices interpolation, reslicing with 3mm and start the algo ?</p>
<p>Many thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4def2abe04edff47afb1a73a8a4061b839afca55.jpeg" data-download-href="/uploads/short-url/b7rb2wOVGxMv2RnxXg3FkKcWOk5.jpeg?dl=1" title="SmartScore4 - 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4def2abe04edff47afb1a73a8a4061b839afca55_2_690x381.jpeg" alt="SmartScore4 - 2" data-base62-sha1="b7rb2wOVGxMv2RnxXg3FkKcWOk5" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4def2abe04edff47afb1a73a8a4061b839afca55_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4def2abe04edff47afb1a73a8a4061b839afca55.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4def2abe04edff47afb1a73a8a4061b839afca55.jpeg 2x" data-dominant-color="CCBFB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SmartScore4 - 2</span><span class="informations">887×491 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f194e6d2cee6e612e4d4f16625504013b5823a79.jpeg" alt="Vitrae - 1" data-base62-sha1="yt85CEAkR9Wrv5CCFaZ9Enmq01b" width="310" height="182"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dac9970e2422d5f006f30b6e8390b6461a0a11.jpeg" data-download-href="/uploads/short-url/axlBwPRMxBCL54LET6lVjHskBTH.jpeg?dl=1" title="SmartScore4 - 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49dac9970e2422d5f006f30b6e8390b6461a0a11_2_690x135.jpeg" alt="SmartScore4 - 1" data-base62-sha1="axlBwPRMxBCL54LET6lVjHskBTH" width="690" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49dac9970e2422d5f006f30b6e8390b6461a0a11_2_690x135.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dac9970e2422d5f006f30b6e8390b6461a0a11.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49dac9970e2422d5f006f30b6e8390b6461a0a11.jpeg 2x" data-dominant-color="EAE0DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SmartScore4 - 1</span><span class="informations">983×193 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #35 by @lassoan (2024-06-16 17:56 UTC)

<p>All these calcium scoring algorithms are trivial to implement, but there are many small decisions to make, which may significantly affect the final scores. If you can create 10 sample data sets (you can get the images from any public cardiac CT data sets) and get calcium scores for them by using a few commercial packages then I can help you to put together a very nice, robust, and convenient Slicer module in a few days.</p>

---
