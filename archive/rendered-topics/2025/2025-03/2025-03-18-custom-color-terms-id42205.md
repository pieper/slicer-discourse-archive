# Custom color terms

**Topic ID**: 42205
**Date**: 2025-03-18
**URL**: https://discourse.slicer.org/t/custom-color-terms/42205

---

## Post #1 by @muratmaga (2025-03-18 17:01 UTC)

<p>With the new custom color table, if I do not want to use a terminology, just want to create custom color/label set to be used during segmentation, what should I enter into these fields:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b1fb196b57031c4c6a230d2b3553fc8d3ec86a5.png" data-download-href="/uploads/short-url/m8hUvjioUh77YXt3jmNaS8sk1Fj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1fb196b57031c4c6a230d2b3553fc8d3ec86a5_2_690x371.png" alt="image" data-base62-sha1="m8hUvjioUh77YXt3jmNaS8sk1Fj" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b1fb196b57031c4c6a230d2b3553fc8d3ec86a5_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b1fb196b57031c4c6a230d2b3553fc8d3ec86a5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b1fb196b57031c4c6a230d2b3553fc8d3ec86a5.png 2x" data-dominant-color="DBDEE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">954×514 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think there was a custom value, but I can’t remember how to enter it.</p>
<p>Because if I leave them blank, this color table does not show up in the terminology module.</p>

---

## Post #2 by @lassoan (2025-03-19 02:28 UTC)

<p>You can use Tissue/Tissue when you do not have any information on what the segment contains. Let us know how it works.</p>
<p>We could tune the behavior to allow color table without any terminology information to be used in terminology selectors. But it would be also good to learn about what prevents people from using terminology. When you want use the segmentation, you need a clear definition of what each segment contains. You could choose to first do the segmentation and then define what is in each segment, but that would not save time and there would be a higher risk that the segmentation is not consistent with the specification (because the specification did not exist when the segmentation was done).</p>
<p>Standard terminology in itself does not solve all problems. For example, most terminologies do not provide exact specification or segmentation instructions fit each term. But without using standard terms (or at least some predefined custom terms), it is hard to do anything robustly.</p>

---

## Post #3 by @jamesobutler (2025-03-19 02:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>But it would be also good to learn about what prevents people from using terminology.</p>
</blockquote>
</aside>
<p>What terminology would I use when segmenting luminescent signal from a given mouse as in <a href="https://github.com/Slicer/Slicer/pull/8210#pullrequestreview-2648387394" class="inline-onebox" rel="noopener nofollow ugc">Add support for managing and blending arbitrary number of layers in Slice viewer by jcfr · Pull Request #8210 · Slicer/Slicer · GitHub</a>? I’m getting image based statistics for a luminescent source being shown in a 2D projection type capture. I’m not segmenting a specific structure from this type of image but selecting a region of intensity.</p>

---

## Post #4 by @lassoan (2025-03-19 03:36 UTC)

<p>If you don’t segment a specific structure then the standard anatomical terminologies would not be useful for you, but you can introduce your own codes and specify what they mean. You can specify your own coding scheme where all your codes are defined in. If you start the coding scheme name with the <code>99</code> prefix then you do not need to register it with any authority. You then define “categories” and in each category a list of “types”. For each type you define a code value, meaning, default color, optionally modifiers. You can optionally also specify region and region modifier (it does not have to be anatomic region).</p>
<p>For example, you could use <code>99REVVITY</code> as coding scheme designator for all your codes. A category could be defined as <code>("99REVVITY", "LUM", "Luminescence")</code>, a type could be <code>("99REVVITY", "LSABC123", "Luminescent source ABC123")</code>, modifiers could be <code>("99REVVITY", "LMENH", "Enhanced luminescence")</code> and <code>("99REVVITY", "LMUS, "Ultra-sensitive luminescence")</code>.</p>
<p>In the documentation you can find more information on how to define custom terminolologies using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv">color tables</a> or <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html#how-to">terminology json files</a>.</p>

---

## Post #5 by @muratmaga (2025-03-19 04:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use Tissue/Tissue when you do not have any information on what the segment contains. Let us know how it works.</p>
</blockquote>
</aside>
<p>I ended up entering Tissue to Value field of Category and Type. Is that what am I supposed to do?</p>
<p>When I try to use this color table in segmentation, it worked and I was able to pull the terms from it, but it the selection in the terminology did not stick like the properly created color tables. Ie., every time I had to choose this specific color table from the drop down menu of the Terminology selector module. Is that because of the other missing fields?</p>
<p>Otherwise, it seemed to work.</p>

---

## Post #6 by @lassoan (2025-03-19 04:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I ended up entering Tissue to Value field of Category and Type. Is that what am I supposed to do?</p>
</blockquote>
</aside>
<p>Yes, exactly.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>When I try to use this color table in segmentation, it worked and I was able to pull the terms from it, but it the selection in the terminology did not stick like the properly created color tables. Ie., every time I had to choose this specific color table from the drop down menu of the Terminology selector module. Is that because of the other missing fields?</p>
</blockquote>
</aside>
<p>I could not reproduce this. For me, after I select a color from that color table, for all newly created segments the same color table is offered. Can you describe the exact steps you make (or take a screen capture video)?</p>

---

## Post #7 by @muratmaga (2025-03-19 04:43 UTC)

<p>Try with this file. It reproduces for me with this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv">
  <header class="source">

      <a href="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/terms-and-colors</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv" target="_blank" rel="noopener nofollow ugc">E15_Mouse_Embryo.csv</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-csv">LabelValue,Name,Color_R,Color_G,Color_B,Color_A,Category_CodingScheme,Category_CodeValue,Category_CodeMeaning,Type_CodingScheme,Type_CodeValue,Type_CodeMeaning,TypeModifier_CodingScheme,TypeModifier_CodeValue,TypeModifier_CodeMeaning,Region_CodingScheme,Region_CodeValue,Region_CodeMeaning,RegionModifier_CodingScheme,RegionModifier_CodeValue,RegionModifier_CodeMeaning
1,left lung,197,165,145,255,,Tissue,,,Tissue,,,,,,,,,,
2,cranial lobe,128,174,128,255,,Tissue,,,Tissue,,,,,,,,,,
3,middle lobe,241,214,145,255,,Tissue,,,Tissue,,,,,,,,,,
4,caudal lobe,177,122,101,255,,Tissue,,,Tissue,,,,,,,,,,
5,accessory lobe,111,184,210,255,,Tissue,,,Tissue,,,,,,,,,,
6,left kidney,185,102,83,255,,Tissue,,,Tissue,,,,,,,,,,
7,right kidney,185,102,83,255,,Tissue,,,Tissue,,,,,,,,,,
8,stomach wall,216,101,79,255,,Tissue,,,Tissue,,,,,,,,,,
9,stomach lumen,221,130,101,255,,Tissue,,,Tissue,,,,,,,,,,
10,medial lobe of liver,144,238,144,255,,Tissue,,,Tissue,,,,,,,,,,
11,left lobe of liver,192,104,88,255,,Tissue,,,Tissue,,,,,,,,,,
12,right lobe of liver,220,245,20,255,,Tissue,,,Tissue,,,,,,,,,,
13,caudate lobe of liver,78,63,0,255,,Tissue,,,Tissue,,,,,,,,,,
14,left adrenal,255,250,220,255,,Tissue,,,Tissue,,,,,,,,,,
15,right adrenal,230,220,70,255,,Tissue,,,Tissue,,,,,,,,,,
16,rectum,200,200,235,255,,Tissue,,,Tissue,,,,,,,,,,
17,bladder,250,250,210,255,,Tissue,,,Tissue,,,,,,,,,,
18,left ventricle,244,214,49,255,,Tissue,,,Tissue,,,,,,,,,,
19,right ventricle,0,151,206,255,,Tissue,,,Tissue,,,,,,,,,,
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @lassoan (2025-03-19 04:59 UTC)

<p>I see. The issue is that a code value cannot be defined without a coding scheme.   Also, a code value is typically not a human-readable name. It is better to use a standard terminology.</p>
<p><strong>Instead of:</strong></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>LabelValue</th>
<th>Name</th>
<th>Color_R</th>
<th>Color_G</th>
<th>Color_B</th>
<th>Color_A</th>
<th>Category_CodingScheme</th>
<th>Category_CodeValue</th>
<th>Category_CodeMeaning</th>
<th>Type_CodingScheme</th>
<th>Type_CodeValue</th>
<th>Type_CodeMeaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>left lung</td>
<td>197</td>
<td>165</td>
<td>145</td>
<td>255</td>
<td></td>
<td>Tissue</td>
<td></td>
<td></td>
<td>Tissue</td>
<td></td>
</tr>
</tbody>
</table>
</div><p><strong>You can use:</strong></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>LabelValue</th>
<th>Name</th>
<th>Color_R</th>
<th>Color_G</th>
<th>Color_B</th>
<th>Color_A</th>
<th>Category_CodingScheme</th>
<th>Category_CodeValue</th>
<th>Category_CodeMeaning</th>
<th>Type_CodingScheme</th>
<th>Type_CodeValue</th>
<th>Type_CodeMeaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>left lung</td>
<td>197</td>
<td>165</td>
<td>145</td>
<td>255</td>
<td>SCT</td>
<td>85756007</td>
<td>Tissue</td>
<td>SCT</td>
<td>85756007</td>
<td>Tissue</td>
</tr>
</tbody>
</table>
</div><p><strong>It is even better to use:</strong></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>LabelValue</th>
<th>Name</th>
<th>Color_R</th>
<th>Color_G</th>
<th>Color_B</th>
<th>Color_A</th>
<th>Category_CodingScheme</th>
<th>Category_CodeValue</th>
<th>Category_CodeMeaning</th>
<th>Type_CodingScheme</th>
<th>Type_CodeValue</th>
<th>Type_CodeMeaning</th>
<th>TypeModifier_CodingScheme</th>
<th>TypeModifier_CodeValue</th>
<th>TypeModifier_CodeMeaning</th>
<th>Region_CodingScheme</th>
<th>Region_CodeValue</th>
<th>Region_CodeMeaning</th>
<th>RegionModifier_CodingScheme</th>
<th>RegionModifier_CodeValue</th>
<th>RegionModifier_CodeMeaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>left lung</td>
<td>197</td>
<td>165</td>
<td>145</td>
<td>255</td>
<td>SCT</td>
<td>123037004</td>
<td>Anatomical Structure</td>
<td>SCT</td>
<td>39607008</td>
<td>Lung</td>
<td>SCT</td>
<td>7771000</td>
<td>Left</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #9 by @muratmaga (2025-03-19 05:08 UTC)

<p>Thats just an example which I converted from an older color map we used to the new one. I really do not want to go into SCT or other things to pull all the fields, since it is a bit tedious.</p>
<p>Going back to what <a class="mention" href="/u/jamesobutler">@jamesobutler</a> asked, what should we enter to those fields when we have to make do without an ontology and or a reference terminology?</p>
<p>I thought we had discussed things like “custom” or something we can enter to distinguish when I have to make do with a term</p>

---

## Post #10 by @lassoan (2025-03-19 05:22 UTC)

<p><code>(SCT,85756007)</code> is a standard way to tell that it is some kind of tissue that you don’t want to describe more specifically. You could use a custom code like <code>(99SLICERMORPH,123)</code> but that would not be much simpler (and you would need to document it somewhere).</p>
<p>To look up the SCT code takes 4 clicks (double-click to open the terminology selector, click “Select from terminology”, double-click “Tissue”, click “Save”). We could add a “use default” terminology button in the “Edit terminology” dialog (that would set the Tissue/Tissue codes), but that would still require 3 clicks from the user, so it would only save a single click. Maybe we could add an advanced section below the color table in Colors module that would allow changing the terminology for all selected items? You could then select all entries and set Tissue / Tissue via the terminology selector only once.</p>

---

## Post #11 by @muratmaga (2025-03-19 05:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>(SCT,85756007)</code> is a standard way to tell that it is some kind of tissue that you don’t want to describe more specifically.</p>
</blockquote>
</aside>
<p>If that’s what it is for, that is good enough for me.</p>

---

## Post #12 by @muratmaga (2025-03-19 05:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="42205">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To look up the SCT code takes 4 clicks (double-click to open the terminology selector, click “Select from terminology”, double-click “Tissue”, click “Save”). We could add a “use default” terminology button in the “Edit terminology” dialog (that would set the Tissue/Tissue codes), but that would still require 3 clicks from the user, so it would only save a single click. Maybe we could add an advanced section below the color table in Colors module that would allow changing the terminology for all selected items? You could then select all entries and set Tissue / Tissue via the terminology selector only once.</p>
</blockquote>
</aside>
<p>For this use case (creating a completely custom set of terms without a terminology), I would create a CSV file with single tissue entry from Slicer’s standard terminology and edit in Excel the rest of the terms by copy and pasting the fields. It took me less than a minute to convert the other csv file with SCT codes. <a href="https://github.com/SlicerMorph/terms-and-colors/blob/main/E15_Mouse_Embryo.csv" class="inline-onebox" rel="noopener nofollow ugc">terms-and-colors/E15_Mouse_Embryo.csv at main · SlicerMorph/terms-and-colors · GitHub</a></p>
<p>It is more of a documentation problem more than anything else.</p>

---
