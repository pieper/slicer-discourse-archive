# LungCTAnalyzer extension for lung CT segmentation and analysis for COVID-19 assessment

**Topic ID**: 15006
**Date**: 2020-12-11
**URL**: https://discourse.slicer.org/t/lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006

---

## Post #1 by @lassoan (2020-12-11 17:33 UTC)

<p>New extension is added for lung CT segmentation and analysis for COVID-19 assessment. It is developed by Prof. Rudolf Bumm (<a class="mention" href="/u/rbumm">@rbumm</a>), a clinician in KSGR (Chur, Switzerland; with some help from Slicer core developers to polish things up), which is a nice demonstration of how Python scripting in Slicer allows users to quickly develop clinically deployable tools from their ideas.</p>
<p>The extension offers a quick (1-minute) lung segmentation wizard and quantitative volumetric analysis of the lungs with quick slice and volume rendering visualization and PDF report generation.</p>
<p>Extension webpage: <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" class="inline-onebox">GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in lung CT.</a></p>
<p>Demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="fpLxm7uAvZQ" data-video-title="Automated lung CT segmentation and analysis for COVID-19 assessment" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fpLxm7uAvZQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fpLxm7uAvZQ/maxresdefault.jpg" title="Automated lung CT segmentation and analysis for COVID-19 assessment" width="" height="">
  </a>
</div>


---

## Post #2 by @TMrt (2020-12-11 19:03 UTC)

<p>I just tried this out-amazing! Thank you</p>

---

## Post #3 by @rbumm (2020-12-12 17:03 UTC)

<p>Thanks for the mention, <a class="mention" href="/u/lassoan">@lassoan</a>, and thanks for the great cooperation. I pushed several small improvements to Github.</p>

---

## Post #4 by @Khaldoun (2020-12-13 18:15 UTC)

<p>Hi, I am very new and naive to 3D slicer. I just installed the last stable version on Mac OS<br>
and installed the Chest Imaging Platform but i could not find the Lung CT analyser extension for lung CT segmentation and analysis. I checked the extension webpage on GitHub but I don’t know how to install the extensions in 3D Slicer from the files after dowonloading the zip files. By the way I also hardly see the modules in Module finder as they look as ghost icons. Is it a matter of OS ? I am using a Mac Book Pro with 16 Go ram under Mac OS High sierra 10.13.6<br>
Sorry for being at a starter point and thank you for your help<br>
The demo video looks amazing and I am impatient to try it</p>

---

## Post #5 by @lassoan (2020-12-13 18:36 UTC)

<aside class="quote no-group" data-username="Khaldoun" data-post="4" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/3ab097/48.png" class="avatar"> Khaldoun:</div>
<blockquote>
<p>i could not find the Lung CT analyser extension for lung CT segmentation and analysis</p>
</blockquote>
</aside>
<p>Lung CT analyzer is available for latest Slicer Preview Release (extension name: LungCTAnalyzer, in Chest Imaging Platform category).</p>
<aside class="quote no-group" data-username="Khaldoun" data-post="4" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/3ab097/48.png" class="avatar"> Khaldoun:</div>
<blockquote>
<p>By the way I also hardly see the modules in Module finder as they look as ghost icons. Is it a matter of OS ? I</p>
</blockquote>
</aside>
<p>This is a <a href="https://github.com/Slicer/Slicer/issues/5118">known issue</a>, a workaround is to change your system to dark mode.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> This extension may bring in users that are new to Slicer and therefore it would be useful if you could add a few sentences about how to install the extension to the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/edit/master/README.md">extension documentation page</a>. Until now, the extension was only submitted to the Slicer-4.13 extensions index, but I’ve added it not to the Slicer-4.11 extensions index now, so from tomorrow it should show up for the latest stable Slicer version (Slicer-4.11.20200930).</p>

---

## Post #6 by @Khaldoun (2020-12-13 20:12 UTC)

<p>Hi Andras</p>
<p>Thank you very much for you so quick reply<br>
Very clear !</p>
<p>I am a nuclear medicine physician and my aim is to use 3D slicer and CIP for lobar quantification of Lung ventilation/perfusion scans by combining lobar lung segmentation and quantification extensions. If you have suggestions I’ll be glad to follow them</p>
<p>Congratulations for the great job you did and are doing with 3D slicer<br>
Khaldoun</p>

---

## Post #7 by @rbumm (2020-12-13 20:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I added a description on the extension documentation page. I will add a few screenshots later.  Hope I did it right, would we have to comment on <a href="https://slicer.kitware.com/midas3/slicerappstore" rel="noopener nofollow ugc">https://slicer.kitware.com/midas3/slicerappstore</a> too ?</p>

---

## Post #8 by @rbumm (2020-12-13 20:46 UTC)

<p>Oh <a class="mention" href="/u/lassoan">@lassoan</a>  I just see that you added it to the extension index, so it will appear “normally” if you “Install slicer extensions” from 3D slicer  “Welcome”  page ?</p>

---

## Post #9 by @lassoan (2020-12-13 20:47 UTC)

<p>Yes, the extension is already available in the extension manager for 4.13 and will be available for 4.11 from tomorrow. So, there is no need to describe the manual installation steps, only installation via the Extensions Manager in Slicer. Thank you!</p>

---

## Post #10 by @lassoan (2020-12-14 02:06 UTC)

<aside class="quote no-group" data-username="Khaldoun" data-post="6" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/3ab097/48.png" class="avatar"> Khaldoun:</div>
<blockquote>
<p>I am a nuclear medicine physician and my aim is to use 3D slicer and CIP for lobar quantification of Lung ventilation/perfusion scans by combining lobar lung segmentation and quantification extensions. If you have suggestions I’ll be glad to follow them</p>
</blockquote>
</aside>
<p>Thanks for the introduction. Slicer and its extension should be able to help you with these. Post separate topics with specific questions if you need help.</p>

---

## Post #11 by @Javi_Vicente (2021-01-11 13:02 UTC)

<p>What parameters should I look at to know if the patient has covid?</p>

---

## Post #12 by @rbumm (2021-01-11 13:49 UTC)

<p>After running the Lung CT Analyzer, there is an option (button) to display the “COVID-19 Results Table”. In Slicer’s COVID-19 demo dataset you would get:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Results</th>
<th>right (ml)</th>
<th>right (%)</th>
<th>left (ml)</th>
<th>left (%)</th>
<th>total (ml)</th>
<th>total (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lung volume</td>
<td>3857</td>
<td>51</td>
<td>3675</td>
<td>49</td>
<td>7532</td>
<td>100</td>
</tr>
<tr>
<td>Functional volume</td>
<td>2104</td>
<td>55</td>
<td>2874</td>
<td>78</td>
<td>4978</td>
<td>66</td>
</tr>
<tr>
<td>Affected volume</td>
<td>1846</td>
<td>48</td>
<td>854</td>
<td>23</td>
<td>2700</td>
<td>36</td>
</tr>
<tr>
<td>CovidQ (affected / functional)</td>
<td>0.88</td>
<td>-1</td>
<td>0.3</td>
<td>-1</td>
<td>0.54</td>
<td>-1</td>
</tr>
</tbody>
</table>
</div><p>COVID-Q is higher in the right lung compared to the left lung. This corresponds well with the extent of infiltrations on the right side.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dce522a200d6129f7cb7b27c8bd84c7abd46fe87.jpeg" alt="image" data-base62-sha1="vw7XK0uCVAJbnExHCzqfIt0Czyf" width="570" height="482"></p>
<p>Please understand that this computation is for scientific use only, it has been implemented only recently and needs validation in clinical studies.</p>

---

## Post #13 by @yangyang117 (2021-05-25 06:09 UTC)

<p>hi, It is great work. I think the CT is segmented by threshold or other traditional tech,right? I found its still have some cavity in the segmentation.Is there any way to segment the lobes and PA,Aorta?</p>

---

## Post #14 by @rbumm (2021-05-25 08:47 UTC)

<p>Hi,</p>
<p>The “Lung CT Segmenter” currently produces lung masks only by a grow from seeds function. The masks are used in “Lung CT Analyzer” for creating thresholded segments of lung parenchyma.<br>
If the lung masks have dents, missing parts or leaks you can place additional fiducials (right lung, left lung, other = outside)  before you press “Apply” to correct this. You can also change the lung intensity range slider to prevent leaks.</p>
<p>If you need to segment lung lobes you may try “Interactive Lobe Segmentation” from the “Chest Imaging Platform”. This is from different developers and also works quite well.</p>
<p>Best regards<br>
Rudolf</p>

---

## Post #15 by @rbumm (2021-05-25 08:53 UTC)

<p>For PA, Aorta, PV you would need a very good contrast CT and could segment the vessels by producing a vessel mask and then use “Grow from Seeds” like shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="wS6-4dwZCfo" data-video-title="Organ segmentation 3.2 : Lungs vessels" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wS6-4dwZCfo" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wS6-4dwZCfo/maxresdefault.jpg" title="Organ segmentation 3.2 : Lungs vessels" width="" height="">
  </a>
</div>


---

## Post #16 by @franx (2021-05-25 18:41 UTC)

<p>Hi, I was trying to use this extension in order to predict covid, but the “COVID results table” button doesn’t appears in my slicer extension installation. Instead of this appears a button for “extended result table” (<a href="https://gyazo.com/d0be934391961b2497048209faef2979" class="inline-onebox" rel="noopener nofollow ugc">Screenshot - d0be934391961b2497048209faef2979 - Gyazo</a>). It is an error? Or it has been removed?<br>
Thanks.</p>

---

## Post #17 by @rbumm (2021-05-25 21:36 UTC)

<p>Hi Fran,</p>
<p>the COVID results table was renamed because it could also be used in conditions like Pneumonia, measuring infiltrations or ARDS, and be useful in COPD.  The data in the table have not changed much and can be used in COVID.19 disease. Systematic evaluations are under way. A high relative affection rate (infiltrated + collapsed, &gt; 50 %)  in % of total lung tissue indicates advanced cases. High collapse rates (10-20%)  are often seen in fatal cases.</p>
<p>Best regards<br>
rudolf</p>

---

## Post #18 by @franx (2021-05-25 21:46 UTC)

<p>Ok, I get that it is better to look at the percentage of several injuries than in a single parameter of the covid. Thanks for the answer, the work is great!</p>
<p>Fran</p>

---

## Post #19 by @mahmoud (2021-09-06 00:08 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="17" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Systematic evaluations are under way. A high relative affection rate (infiltrated + collapsed, &gt; 50 %) in % of total lung tissue indicates advanced cases. High collapse rates (10-20%) are often seen in fatal cases.</p>
</blockquote>
</aside>
<p>thans prof rbumm<br>
please can you give your email to important disscution in this extention</p>

---

## Post #20 by @lassoan (2021-09-06 00:45 UTC)

<aside class="quote no-group" data-username="mahmoud" data-post="19" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mahmoud/48/12259_2.png" class="avatar"> mahmoud:</div>
<blockquote>
<p>please can you give your email</p>
</blockquote>
</aside>
<p>Please keep the discussion open, to allow others to learn from and contribute to the discussion. Switch to private messages only if you need to talk about personal or confidential matters.</p>

---

## Post #21 by @mahmoud (2021-09-06 01:42 UTC)

<p>This extension is very effective…hands up for this effort</p>
<p>I am about to do a scientific paper on this extension. I want to get the ethical approval for scientific research</p>

---

## Post #22 by @rbumm (2021-09-06 08:36 UTC)

<p>Thank you <a class="mention" href="/u/mahmoud">@mahmoud</a> for the positive feedback. You can always direct mail me here on discourse, but as <a class="mention" href="/u/lassoan">@lassoan</a> said, it would be better to have an open discussion in one of the topics.</p>
<p>If you have questions or feature requests concerning the LungCTAnalyzer, please post them <a href="https://discourse.slicer.org/c/support/11">here</a>. If you find bugs please <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/issues" rel="noopener nofollow ugc">open an issue</a> here.<br>
If you use the LungCTAnalyzer and 3D Slicer in a scientfic paper please cite us as mentioned at the bottom of <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" rel="noopener nofollow ugc">the project page</a>.</p>

---

## Post #23 by @mahmoud (2021-09-06 11:49 UTC)

<p>Thanks all …Of course, and from the ethics of research cited you and your project.</p>
<p>I want to get semi automated quantification yeild from table of Covid … especially  covid Q , functional and affected percentage of lungs</p>
<p>But… I have some questions before I start quantification of the data for my scientific paper</p>
<p>The results are then superimposed to the CT 2D views in standard colors: “Bulla” = black, “Inflated” = blue, “Infiltrated” = yellow, “Collapsed” = pink and “Vessel” = red"</p>
<p>It is known that there are main radiological features in Covid CT images such as (consolidation , ground glass opacity and crazy pazing opacity)<br>
I’m noted, these appearances give the pink color … which is translated is collapse.</p>
<p>Radiologically, the consolidation , ground glass opacity and crazy pazing opacity is considered an infiltration opacities</p>
<ul>
<li>
<p>The concept of collapsed here…?? means that loss of aertion or atlactasis<br>
Moreover, what’s the accurate mean of Infiltrated</p>
</li>
<li>
<p>Another question this extension can be differentiated in consolidation, ground glass opacity and crazy pazing opacity in CT images.</p>
</li>
</ul>
<p>Greetings …</p>

---

## Post #24 by @rbumm (2021-09-06 14:05 UTC)

<p>Great, I am currently analyzing two local CT datasets of the first and second wave as well as the open source submillimetric COVID-19 CT dataset of <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> and the following HU thresholds worked for me:</p>
<pre><code class="lang-auto">Bulla / emphysema:     -1050 &gt; x &lt;= -990
Inflated:             - 990 &gt; x &lt;= -650
Infiltrated:           -650 &gt; x &lt;= -400 
Collapsed:             -400 &gt; x &lt;= 0
Vessel:                  0 &gt;= x &lt; 3000
</code></pre>
<p>“Infiltration” should include “ground glass opacity” and “crazy paving”.<br>
“Infiltrated” includes “consolidation”.</p>
<p>I am not referring to the nonlinear “COVID-Q” any longer, it was suggested to better use “% affected lung” as a severity parameter.</p>

---

## Post #25 by @rbumm (2021-09-06 14:30 UTC)

<aside class="quote no-group" data-username="mahmoud" data-post="23" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mahmoud/48/12259_2.png" class="avatar"> mahmoud:</div>
<blockquote>
<p>ground glass opacity and crazy pazing opacity</p>
</blockquote>
</aside>
<p>GGO and crazy paving are difficult to differentiate yet because they share similar HU ranges. We would need to take their shape and size into account.</p>

---

## Post #26 by @pieper (2021-09-06 16:04 UTC)

<p>You could use SlicerRadiomics for this.  I’d suggest doing a literature search since this has been <a href="https://ccforum.biomedcentral.com/articles/10.1186/s13054-021-03564-y">well studied</a>.</p>

---

## Post #27 by @mahmoud (2021-09-07 20:33 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="24" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<pre><code class="lang-auto">Bulla / emphysema:     -1050 &gt; x &lt;= -990
Inflated:             - 990 &gt; x &lt;= -650
Infiltrated:           -650 &gt; x &lt;= -400 
Collapsed:             -400 &gt; x &lt;= 0
Vessel:                  0 &gt;= x &lt; 3000
</code></pre>
</blockquote>
</aside>
<p>There is modified HU reference … But the default reference is as <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f502bf8b02ad4efcf2c97f3b5a4b810e01ada85a.jpeg" data-download-href="/uploads/short-url/yXsRPGcYTuuokzglqbBR98sKyEi.jpeg?dl=1" title="Screenshot_٢٠٢١-٠٩-٠٧-٢٢-٤٩-٣٧-٥٧٨_com.google.android.apps.docs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f502bf8b02ad4efcf2c97f3b5a4b810e01ada85a_2_230x500.jpeg" alt="Screenshot_٢٠٢١-٠٩-٠٧-٢٢-٤٩-٣٧-٥٧٨_com.google.android.apps.docs" data-base62-sha1="yXsRPGcYTuuokzglqbBR98sKyEi" width="230" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f502bf8b02ad4efcf2c97f3b5a4b810e01ada85a_2_230x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f502bf8b02ad4efcf2c97f3b5a4b810e01ada85a_2_345x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f502bf8b02ad4efcf2c97f3b5a4b810e01ada85a_2_460x1000.jpeg 2x" data-dominant-color="CDCDCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_٢٠٢١-٠٩-٠٧-٢٢-٤٩-٣٧-٥٧٨_com.google.android.apps.docs</span><span class="informations">1080×2340 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After, my investigation I think the default HU is more accurate than the above new modified  referance values because the value as same as non-aeration alveolis ( refer to collapse) represent as consolidation</p>
<p>I wont to use default references  to stars analysis the dataset …</p>
<p>Please, give me your opinions in these issue</p>

---

## Post #28 by @rbumm (2021-09-08 19:09 UTC)

<p>I suggest to analyze a few of your patients with different thresholds, but in the end it may turn out that our predefined LCTA threshold may work well.</p>
<p>In many papers I see the authors using a visual score of the radiologist and comparing that score to the  computed results.</p>

---

## Post #29 by @mahmoud (2021-09-10 01:00 UTC)

<p>We are trying to break the routine and see the achievement of the extension in testing a field other than visual score of the radiologist</p>

---

## Post #30 by @mahmoud (2021-09-11 19:04 UTC)

<p>Hallo I encountered some obstacles, attached to the pictures<br>
It seems to me that the extension is in the process of development…because I noticed that there is a difference in the results, for example:</p>
<p>I downloaded the 3D slicing software using the CT Lung Analyzer on two laptops<br>
The first laptop gave me the COVID results as pictured 1111(image 1)<br>
The second laptop gave me the COVID results as pictured 2222 (image 2)<br>
Which of the results is correct?<br>
whts the best parameter’s … % affected lung as a severity parameter or collapse or infiltrated ???</p>
<p>please  helpe me</p>
<p>Best regards<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3790d2377ed39a5f0e9556add892e5efdf0538d5.png" data-download-href="/uploads/short-url/7Vyxp3LjHa04rjKnbhJPhZkDCcJ.png?dl=1" title="1111---" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3790d2377ed39a5f0e9556add892e5efdf0538d5_2_660x500.png" alt="1111---" data-base62-sha1="7Vyxp3LjHa04rjKnbhJPhZkDCcJ" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3790d2377ed39a5f0e9556add892e5efdf0538d5_2_660x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3790d2377ed39a5f0e9556add892e5efdf0538d5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3790d2377ed39a5f0e9556add892e5efdf0538d5.png 2x" data-dominant-color="F0ECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1111---</span><span class="informations">797×603 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1cb1930713f45003e636b6cd97fcd21b7dc0092.png" data-download-href="/uploads/short-url/tVUVvO0Z5TGG9tbvQiEkfRt27iW.png?dl=1" title="2222---" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1cb1930713f45003e636b6cd97fcd21b7dc0092_2_686x500.png" alt="2222---" data-base62-sha1="tVUVvO0Z5TGG9tbvQiEkfRt27iW" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1cb1930713f45003e636b6cd97fcd21b7dc0092_2_686x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1cb1930713f45003e636b6cd97fcd21b7dc0092.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1cb1930713f45003e636b6cd97fcd21b7dc0092.png 2x" data-dominant-color="F1EDEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2222---</span><span class="informations">790×575 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8c3d7739f536d4a2f47a8295c879a5fbdc7c1a.png" data-download-href="/uploads/short-url/jUuPxZ97J8AqVNFPWnfFzM8vmoG.png?dl=1" title="333" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8c3d7739f536d4a2f47a8295c879a5fbdc7c1a_2_532x500.png" alt="333" data-base62-sha1="jUuPxZ97J8AqVNFPWnfFzM8vmoG" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8c3d7739f536d4a2f47a8295c879a5fbdc7c1a_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8c3d7739f536d4a2f47a8295c879a5fbdc7c1a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8c3d7739f536d4a2f47a8295c879a5fbdc7c1a.png 2x" data-dominant-color="555353"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">333</span><span class="informations">625×587 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #31 by @rbumm (2021-09-11 20:39 UTC)

<p>Hello,</p>
<p>you are obviously using two different versions of the LungCTAnalyzer, probably in two different versions of Slicer.<br>
The first result table you attached is the more recent one (with % affected), the second is from December 2020.</p>
<p>I recommend doing the analysis with the stable version of slicer (4.11). To get the latest distro of the LuncCtAnalyzer (LCTA) extension deinstall it , restart Slicer, install LCTA again, restart. The current program version of LCTA is 2.44. There is a version label at the top of the LCTA GUI.</p>

---

## Post #32 by @Andrew_James_Snyder (2022-04-08 20:22 UTC)

<p>Hi-</p>
<p>I am a graduate student hoping to use the software to analyze mouse tumor volumes. Anyone have any thoughts on if this would be possible? Having a hard time having the program correlate mouse anatomy with human. thoughts?</p>

---

## Post #33 by @rbumm (2022-04-08 22:07 UTC)

<p>Hi,<br>
The Lung CT Analyzer is focused on lung density measurements - what kind of tumors are you analyzing? How many tumors in how many species?</p>
<p>Rudolf</p>

---

## Post #34 by @lassoan (2022-04-08 22:19 UTC)

<p>You can segment tumors using “Grow from seeds” effect as shown in this short tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cybL5A0w3hw" data-video-title="Brain tumor segmentation on MRI in 1 minute" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cybL5A0w3hw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cybL5A0w3hw/maxresdefault.jpg" title="Brain tumor segmentation on MRI in 1 minute" width="" height="">
  </a>
</div>

<p>Or, if the tumor is easily distinguishable from the surrounding tissues then you may can segment using less clicks, using “Local Threshold” effect:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="NmG16cSwUHg" data-video-title='Segmenting a lung nodule with 3D Slicer and "Local Threshold"' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=NmG16cSwUHg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/NmG16cSwUHg/maxresdefault.jpg" title='Segmenting a lung nodule with 3D Slicer and "Local Threshold"' width="" height="">
  </a>
</div>


---

## Post #35 by @oumik (2022-04-29 17:35 UTC)

<p>Hello,<br>
I have been trying to segment a lung CT of a COVID 19 patient and following the steps in your videos I end up with a 3D segment of the lungs that is black and not colored as yours can you please advise?<br>
Thank you in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c485a8cac10475399f3ddcaab47a2a5c40800da.jpeg" data-download-href="/uploads/short-url/hJsdQUxPiIi1PY2DWKfYTQkKbnc.jpeg?dl=1" title="problem with 3d image all black" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c485a8cac10475399f3ddcaab47a2a5c40800da_2_690x312.jpeg" alt="problem with 3d image all black" data-base62-sha1="hJsdQUxPiIi1PY2DWKfYTQkKbnc" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c485a8cac10475399f3ddcaab47a2a5c40800da_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c485a8cac10475399f3ddcaab47a2a5c40800da.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c485a8cac10475399f3ddcaab47a2a5c40800da.jpeg 2x" data-dominant-color="505368"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem with 3d image all black</span><span class="informations">737×334 37.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #36 by @rbumm (2022-04-29 18:47 UTC)

<p>Which version of Slicer are you using?</p>
<p>Could you also check the version number of the Lung CT Analyzer?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a16d177a6f909d2b64c33b4ac9c7c01787df1ec6.png" alt="image" data-base62-sha1="n22BeVrr3cSPUzPBKsk5qv0E3bM" width="501" height="253"></p>

---

## Post #37 by @oumik (2022-04-29 19:39 UTC)

<p>Thank you for your reply.<br>
The 3D slicer version I am using is 4.11.20210226.<br>
The Lung CT Analyzer version is V 2.47.</p>

---

## Post #38 by @rbumm (2022-04-29 19:51 UTC)

<p>And you are using the “Show/hide final segments in 3D” button to create 3D VIEW ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3324345ebeb5c8abfb983a3fb369611ae9e7bf.png" data-download-href="/uploads/short-url/zQdpJyPJWrNUA07KzISXG36yO4f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3324345ebeb5c8abfb983a3fb369611ae9e7bf_2_690x351.png" alt="image" data-base62-sha1="zQdpJyPJWrNUA07KzISXG36yO4f" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3324345ebeb5c8abfb983a3fb369611ae9e7bf_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3324345ebeb5c8abfb983a3fb369611ae9e7bf_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb3324345ebeb5c8abfb983a3fb369611ae9e7bf_2_1380x702.png 2x" data-dominant-color="AFB1B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1812×922 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #39 by @oumik (2022-05-01 16:02 UTC)

<p>Thank you for replying.<br>
Before reaching this step, when I click on show/hide preview in 3D under the Thresholds section, the entire 3D segment is black. I can change the opacity but the 3D model remains mono-colored. When I select the show/hide final segments in 3D under the Statistics section, the output colored regions are displayed but since the model was originally black the combination appears non-homogenous and distorted somehow.</p>

---

## Post #40 by @oumik (2022-05-01 16:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0a280af0e34f2e017aec8a3f50424dd04d9fb0e.jpeg" data-download-href="/uploads/short-url/mV2yrSlorXDIPtAWrCqk7cigcoK.jpeg?dl=1" title="3D slicer LUNG CT COVID output segments shown" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0a280af0e34f2e017aec8a3f50424dd04d9fb0e_2_690x284.jpeg" alt="3D slicer LUNG CT COVID output segments shown" data-base62-sha1="mV2yrSlorXDIPtAWrCqk7cigcoK" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0a280af0e34f2e017aec8a3f50424dd04d9fb0e_2_690x284.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0a280af0e34f2e017aec8a3f50424dd04d9fb0e_2_1035x426.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0a280af0e34f2e017aec8a3f50424dd04d9fb0e.jpeg 2x" data-dominant-color="9D9DAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D slicer LUNG CT COVID output segments shown</span><span class="informations">1284×529 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is what I obtain when I do not click on show preview in 3D and only display show segments in 3D.</p>

---

## Post #41 by @rbumm (2022-05-01 18:20 UTC)

<p>I can not yet reproduce your black preview in 3D, mine (in Slicer 4.13 and LCTA 2.47) is colored.</p>
<p>Anyway, if you <strong>enabled</strong> the 3D <strong>preview</strong>, you should “<strong>Hide preview</strong> in 3D” afterwards to obtain only the final output segmentation in the 3D view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c0aff6f6c53386904b361205612572e2058cafb.png" data-download-href="/uploads/short-url/jYSpknAwoHTDfh1mv1crLUf6DCH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c0aff6f6c53386904b361205612572e2058cafb.png" alt="image" data-base62-sha1="jYSpknAwoHTDfh1mv1crLUf6DCH" width="427" height="500" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">502×587 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #42 by @Aaron_Tsai (2022-10-15 07:25 UTC)

<p>Hi Rudolf,</p>
<p>I would like to test the package on rodents’ lung tissue analysis.<br>
When I move to step 2, that is the step I would need to place a few seeds.<br>
However, the image is kind of resample to very large voxels makes the images blurred.<br>
Dose this package only good for human CT images?<br>
Thank you very much,</p>
<p>Regards,<br>
Aaron</p>

---

## Post #43 by @rbumm (2022-10-15 10:40 UTC)

<p>Hi,<br>
The package has been developed for human CT and the Lung CT Segmenter module does not yet work reliably with Micro CT. However, you could go to “Segment Editor”, and create a “lung segmentation” with “right lung” and “left lung” by using the “Grow From Seeds” effect. As soon as you have good lung masks you could then run the “Lung CT Analyzer” module and use the “lung segmentation” with the lung masks as input segmentation.<br>
Regards<br>
Rudolf</p>

---

## Post #44 by @lassoan (2022-10-15 13:11 UTC)

<p>I think the only value hardcoded for human clinical CT is the preview image resolution of 2mm. This is probably too large for microCT.</p>
<p>You can easily modify this value by editing this line in LungCTSegmenter.py file:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/0ebbfee16245c44c5f2b3e848f93eb3e045ee6dc/LungCTSegmenter/LungCTSegmenter.py#L924">
  <header class="source">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/0ebbfee16245c44c5f2b3e848f93eb3e045ee6dc/LungCTSegmenter/LungCTSegmenter.py#L924" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/0ebbfee16245c44c5f2b3e848f93eb3e045ee6dc/LungCTSegmenter/LungCTSegmenter.py#L924" target="_blank" rel="noopener">rbumm/SlicerLungCTAnalyzer/blob/0ebbfee16245c44c5f2b3e848f93eb3e045ee6dc/LungCTSegmenter/LungCTSegmenter.py#L924</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="914" style="counter-reset: li-counter 913 ;">
          <li>    self.resampledVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "Resampled Volume")
</li>
          <li>
</li>
          <li># Get window / level of inputVolume 
</li>
          <li>displayNode = self.inputVolume.GetDisplayNode()
</li>
          <li>displayNode.AutoWindowLevelOff()
</li>
          <li>displayNode.SetWindowLevel(1400, -500)
</li>
          <li>
</li>
          <li># Create resampled volume with fixed 2.0mm spacing (for faster, standardized workflow)
</li>
          <li>
</li>
          <li>self.showStatusMessage('Resampling volume, please wait...')
</li>
          <li class="selected">parameters = {"outputPixelSpacing": "2.0,2.0,2.0", "InputVolume": self.inputVolume, "interpolationType": "linear", "OutputVolume": self.resampledVolume}
</li>
          <li>cliParameterNode = slicer.cli.runSync(slicer.modules.resamplescalarvolume, None, parameters)
</li>
          <li>slicer.mrmlScene.RemoveNode(cliParameterNode)
</li>
          <li>
</li>
          <li># Set window / level of inputVolume in resampledVolume 
</li>
          <li>displayNode = self.resampledVolume.GetDisplayNode()
</li>
          <li>displayNode.AutoWindowLevelOff()
</li>
          <li>displayNode.SetWindowLevel(1400, -500)
</li>
          <li>
</li>
          <li>if not self.outputSegmentation:
</li>
          <li>    self.outputSegmentation = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", "Lung segmentation")
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Alternatively, you can modify the spacing value of the volume in Volumes module to be 10x larger. This does not change the image in any way, it just makes all length measurements 10x larger.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> we could consider allowing users to edit this value in some advanced parameters section in the GUI.</p>

---

## Post #45 by @rbumm (2022-10-15 14:36 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> never thought you could set volume spacing from the Volumes extension directly.<br>
So now I can confirm that setting a rodent microCT´s spacing from 0.133mm 10 x larger enables the use of Lung CT Segmenter</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae4e1422cf4abb20f0c079c030e5b49ce81fbf4e.jpeg" data-download-href="/uploads/short-url/oRYmtRvsBBlcQoGq7D6LK1EhLQy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae4e1422cf4abb20f0c079c030e5b49ce81fbf4e_2_690x384.jpeg" alt="image" data-base62-sha1="oRYmtRvsBBlcQoGq7D6LK1EhLQy" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae4e1422cf4abb20f0c079c030e5b49ce81fbf4e_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae4e1422cf4abb20f0c079c030e5b49ce81fbf4e_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae4e1422cf4abb20f0c079c030e5b49ce81fbf4e.jpeg 2x" data-dominant-color="6E6E78"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1270×708 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>with the following lung thresholds:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfad1c5a8a395fe89b5c39f278873523cf790617.png" alt="image" data-base62-sha1="rlE5gvQtPb07tDdj2R09f2eaMEn" width="617" height="59"></p>
<p>The other option does not work for me yet. Testing …</p>

---

## Post #46 by @rbumm (2022-10-15 15:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="44" data-topic="15006">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">parameters = {"outputPixelSpacing": "2.0,2.0,2.0", "InputVolume": self.inputVolume, "interpolationType": "linear", "OutputVolume": self.resampledVolume}
</code></pre>
</blockquote>
</aside>
<p>To my understanding setting</p>
<pre><code class="lang-auto">914. parameters = {"outputPixelSpacing": "0.,0.,0.", "InputVolume": self.inputVolume, "interpolationType": "linear", "OutputVolume": self.resampledVolume}
</code></pre>
<p>should leave the spacing untouched in resampling, 2D views are not blurred, but the lung preview looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aa506eee94471873748daeed399cc4bdc6dd9af.jpeg" alt="image" data-base62-sha1="3NHYX8xin4OiIRpUGf0oiyPz7tR" width="636" height="351"></p>
<p>… and “Apply” hangs Slicer.</p>
<p>Any ideas?</p>

---

## Post #47 by @lassoan (2022-10-15 17:10 UTC)

<p>0 spacing is invalid, do not set that value. If you don’t resample then computation time will be too long for interactive use. If you do not want to expose spacing as a parameter to the users (because it is too technical) then we could add a “lung size” (diameter of the lungs along a chosen anatomical axis) and compute the spacing relative to that. It is important that this spacing is not related to the input image resolution but the level of detail that we want for the segmentation preview.</p>

---

## Post #48 by @rbumm (2022-10-15 19:54 UTC)

<p>Setting spacing directly to 1 mm (original 0.188mm)  and then using 2.0, 2.0, 2.0 works well. What would be your suggestion for a corresponding ouputPixelSpacing setting to achieve a similar result by leaving the input spacing at 0.188mm?</p>

---

## Post #49 by @lassoan (2022-10-16 01:55 UTC)

<p>If you had to increase the spacing of the original image by approximately 5x (from 0.188mm to 1mm) then it means that you could instead decrease the spacing of the preview image by approximately 5x to have about the same level of detail. So, instead of 2.0mm spacing, use <strong>0.4mm</strong> spacing for the preview image.</p>

---

## Post #50 by @rbumm (2022-10-16 07:41 UTC)

<p>Yes, but it does not work for some reason. I will open an issue and we can discuss it there.</p>

---

## Post #51 by @lassoan (2022-11-27 20:23 UTC)

<p>2 posts were split to a new topic: <a href="/t/lungctanalyzer-extension-used-for-research-paper/26466">LungCTAnalyzer extension used for research paper</a></p>

---

## Post #52 by @lassoan (2024-09-23 01:38 UTC)

<p>A post was split to a new topic: <a href="/t/lungctanalyzer-for-pneumonia-pleural-effusion-cases/38490">LungCTAnalyzer for pneumonia + pleural effusion cases</a></p>

---

## Post #53 by @lassoan (2024-09-23 01:25 UTC)

<p>A post was split to a new topic: <a href="/t/lung-volume-measurement/38489">Lung volume measurement</a></p>

---

## Post #54 by @lassoan (2024-09-25 19:53 UTC)

<p>2 posts were split to a new topic: <a href="/t/lung-lobe-input-segment-is-missing/38540">Lung lobe input segment is missing</a></p>

---

## Post #55 by @yayale (2025-04-07 14:15 UTC)

<p>Hello,</p>
<p>I am trying to make use of this extension. But the documentation is not enough to understand different values in the results table, and the color legend.<br>
Is there a clear document that explains the details of this extension ?</p>

---

## Post #56 by @Vuk_Vidic (2025-10-27 10:57 UTC)

<p>Hello, i have a problem with Analyzer Results, in report Extended analysis (Table 2) all results are zero (0).</p>

---
