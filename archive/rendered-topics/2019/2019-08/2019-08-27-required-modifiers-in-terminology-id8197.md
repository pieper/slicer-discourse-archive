---
topic_id: 8197
title: "Required Modifiers In Terminology"
date: 2019-08-27
url: https://discourse.slicer.org/t/8197
---

# Required modifiers in terminology

**Topic ID**: 8197
**Date**: 2019-08-27
**URL**: https://discourse.slicer.org/t/required-modifiers-in-terminology/8197

---

## Post #1 by @lassoan (2019-08-27 15:30 UTC)

<p>We would like to use terminologies correctly in NVidia’s AI segmentation plugin. However, the terminology json or logic does not seem to make sense. For example, I cannot create a segment for “spleen”. When I choose “Segmentation category and type – DICOM master list” and search for spleen, a property is found, but I’m forced to select laterality! I can choose “Left”, “Right”, or “Right and left” - but there is no way I can simply choose “Spleen”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a69758b8d01c07251e8639fe944599364ef7507.png" data-download-href="/uploads/short-url/cTOUT3RdR1du9wB622ckiHvblVJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a69758b8d01c07251e8639fe944599364ef7507.png" alt="image" data-base62-sha1="cTOUT3RdR1du9wB622ckiHvblVJ" width="409" height="500" data-dominant-color="C0D8E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×725 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this an error in the terminology json (there should be an option for not specifying laterality)? Or is this an error in the terminology implementation (it should not <em>require</em> selection of a modifier)?</p>
<p><a href="https://github.com/Slicer/Slicer/blob/ef1891672d53b8dba745673f1ca6eafd1fbfc473/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-DICOM-Master.json#L12281-L12307" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/ef1891672d53b8dba745673f1ca6eafd1fbfc473/Modules/Loadable/Terminologies/Resources/SegmentationCategoryTypeModifier-DICOM-Master.json#L12281-L12307</a></p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @cpinter (2019-08-27 17:14 UTC)

<p>The behaviour is expected, this is how I implemented it back then, based on the specification and later clarifications of <a class="mention" href="/u/fedorov">@fedorov</a>.</p>
<p>If it needs to be changed, then it is not an implementation question but one related to the standards.</p>

---

## Post #3 by @lassoan (2019-08-27 17:17 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>, can you explain the rationale for requiring selection of  “Left”, “Right”, or “Right and left” for organs such as the spleen?</p>

---

## Post #4 by @fedorov (2019-08-28 01:33 UTC)

<p>Spleen is defined in the dcmqi segmentation JSON file, which (at least, a version of it) I believe was used to populate segment editor, here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/dcmqi/blob/master/doc/segContexts/SegmentationCategoryTypeModifier-DICOM-Master.json#L12984-L13000" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/dcmqi/blob/master/doc/segContexts/SegmentationCategoryTypeModifier-DICOM-Master.json#L12984-L13000" target="_blank" rel="nofollow noopener">QIICR/dcmqi/blob/master/doc/segContexts/SegmentationCategoryTypeModifier-DICOM-Master.json#L12984-L13000</a></h4>
<pre class="onebox"><code class="lang-json"><ol class="start lines" start="12984" style="counter-reset: li-counter 12983 ;">
<li>{</li>
<li>  "recommendedDisplayRGBValue": [</li>
<li>    157,</li>
<li>    108,</li>
<li>    162</li>
<li>  ],</li>
<li>  "CodeMeaning": "Spleen",</li>
<li>  "CodingSchemeDesignator": "SRT",</li>
<li>  "3dSlicerLabel": "spleen",</li>
<li>  "3dSlicerIntegerLabel": 220,</li>
<li>  "cid": "4030,7154",</li>
<li>  "UMLSConceptUID": "C0037993",</li>
<li>  "CodeValue": "T-C3000",</li>
<li>  "contextGroupName": "CT,MRandPETAnatomyImaged,AbdominalSegmentationTypes",</li>
<li>  "SNOMEDCTConceptID": "78961009",</li>
<li>  "paired": "U"</li>
<li>},</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It is marked as unpaired, so I do not know why laterality is forced in Segment editor.</p>

---

## Post #5 by @cpinter (2019-08-28 01:58 UTC)

<p>I think the “paired” attribute was not included in the specifications when implementing Terminologies, thus it is not considered.</p>

---

## Post #6 by @lassoan (2019-08-28 02:04 UTC)

<p>Spleen has laterality in this file in the dmqi repository:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/dcmqi/blob/c3b40ac82ebcf760325884c6558e1aacbe622133/doc/segContexts/resources/SegmentationCategoryTypeModifier.json#L11160-L11197" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/dcmqi/blob/c3b40ac82ebcf760325884c6558e1aacbe622133/doc/segContexts/resources/SegmentationCategoryTypeModifier.json#L11160-L11197" target="_blank" rel="nofollow noopener">QIICR/dcmqi/blob/c3b40ac82ebcf760325884c6558e1aacbe622133/doc/segContexts/resources/SegmentationCategoryTypeModifier.json#L11160-L11197</a></h4>
<pre class="onebox"><code class="lang-json"><ol class="start lines" start="11160" style="counter-reset: li-counter 11159 ;">
<li>{</li>
<li>  "codeValue": "T-C3000", </li>
<li>  "cid": "7154", </li>
<li>  "UMLSConceptUID": "C0037993", </li>
<li>  "codeMeaning": "Spleen", </li>
<li>  "contextGroupName": "Abdominal Organ Segmentation Types", </li>
<li>  "codingScheme": "SRT", </li>
<li>  "SNOMEDCTConceptID": "78961009", </li>
<li>  "Modifier": [</li>
<li>    {</li>
<li>      "codeValue": "G-A100", </li>
<li>      "cid": "244", </li>
<li>      "UMLSConceptUID": "C0205090", </li>
<li>      "codeMeaning": "Right", </li>
<li>      "contextGroupName": "Laterality", </li>
<li>      "codingScheme": "SRT", </li>
<li>      "SNOMEDCTConceptID": "24028007"</li>
<li>    }, </li>
<li>    {</li>
<li>      "codeValue": "G-A101", </li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/QIICR/dcmqi/blob/c3b40ac82ebcf760325884c6558e1aacbe622133/doc/segContexts/resources/SegmentationCategoryTypeModifier.json#L11160-L11197" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Which file Slicer should use?</p>

---

## Post #7 by @fedorov (2019-08-28 02:51 UTC)

<p>I think this discussion from March 2017 should help: <a href="https://github.com/QIICR/QuantitativeReporting/issues/150#issuecomment-288408153" rel="nofollow noopener">https://github.com/QIICR/QuantitativeReporting/issues/150#issuecomment-288408153</a></p>

---

## Post #8 by @fedorov (2019-08-28 02:54 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="8197" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I think the “paired” attribute was not included in the specifications when implementing Terminologies, thus it is not considered.</p>
</blockquote>
</aside>
<p>It might well be that this was not considered at the time. The reality is I don’t know how frequently this feature in Slicer was used, so chances are things went un-noticed.</p>

---
