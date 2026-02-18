# Terminology labels and file location

**Topic ID**: 35240
**Date**: 2024-04-02
**URL**: https://discourse.slicer.org/t/terminology-labels-and-file-location/35240

---

## Post #1 by @muratmaga (2024-04-02 18:26 UTC)

<p>We are creating a custom terminology for vertebrate musculoskeletal system by extracting the relevant terms from the Uberon ontology. I have encountered a few things that I can’t find the answers to.</p>
<ol>
<li>When I custom terminology is successfully imported to Slicer, where is it saved? I removed the original JSON file that was imported, but the terminology is still there. I searched for files modified under Slicer install tree, but wasn’t able to find. As I am testing more and more files are being added, and I would like clear them.</li>
<li>Is there field that controls the value of the displayed value? AFAIT the label comes from “CodeMeaning” field. There is a field called “3dSlicerLabel” but that does’t seem to affect the displayed value.</li>
</ol>
<p>The issue is some of the terms from Uberon is too long to use as the actual name.<br>
E.g., <strong><a href="https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0018588">upper first primary molar tooth</a></strong></p>
<p>Instead we would like this to be displayed something like <strong>UM1</strong>.</p>
<p>Here is the section of terminology we are using…</p>
<pre><code class="lang-auto">"SegmentationCategoryTypeContextName": "Murat",
    "@schema": "https://raw.githubusercontent.com/qiicr/dcmqi/master/doc/schemas/segment-context-schema.json#",
    "SegmentationCodes": {
        "Category": [
            {
                "CodeMeaning": "Dentition",
                "CodingSchemeDesignator": "UBERON",
                "showAnatomy": true,
                "cid": "7150",
                "CodeValue": "0018588",
                "contextGroupName": "SegmentationPropertyCategories",
                "Type": [
                    {
                        "recommendedDisplayRGBValue": [
                            0,
                            179,
                            92
                        ],
                        "CodeMeaning": "upper first primary molar tooth",
                        "CodingSchemeDesignator": "UBERON",
                        "3dSlicerLabel": "UM1",
                        "3dSlicerIntegerLabel": 1,
                        "CodeValue": "0018588",
                        "contextGroupName": "CommonTissueSegmentationTypes",
                        "paired": "Y",
                        "Modifier": [
                            {
                                "recommendedDisplayRGBValue": [
                                    0,
                                    179,
                                    92
                                ],
                                "CodeMeaning": "Right",
                                "CodingSchemeDesignator": "SCT",
                                "3dSlicerLabel": "right UM1",
                                "3dSlicerIntegerLabel": 2,
                                "cid": "244",
                                "UMLSConceptUID": "C0205090",
                                "CodeValue": "24028007",
                                "contextGroupName": "Laterality",
                                "SNOMEDCTConceptID": "24028007"
                            },
                            {
                                "recommendedDisplayRGBValue": [
                                    0,
                                    179,
                                    92
                                ],
                                "CodeMeaning": "Left",
                                "CodingSchemeDesignator": "SCT",
                                "3dSlicerLabel": "left UM1",
                                "3dSlicerIntegerLabel": 3,
                                "cid": "244",
                                "UMLSConceptUID": "C0205091",
                                "CodeValue": "7771000",
                                "contextGroupName": "Laterality",
                                "SNOMEDCTConceptID": "7771000"
                            }
                        ]
                    },
                    {
                        "recommendedDisplayRGBValue": [
                            144,
                            16,
                            49
                        ],
                        
</code></pre>

---

## Post #2 by @cpinter (2024-04-04 11:34 UTC)

<ol>
<li>When you import the terminology, currently it is not even saved in the scene, but the Terminology module logic stores and handles the new terminology data. So you need to load the json after every restart (from script or manually) if you want to use it. No need to delete it (I am not even sure the current API supports it), all you need to do is restart Slicer and you won’t have any custom terminology loaded.</li>
<li>3dSlicerLabal as I understand is just a way to connect any entry to the current GeneralAnatomyColors color table, just establishing correspondence. It is not needed for a custom terminology. The <code>CodeMeaning</code> field is what the displayed terminology type will be.</li>
</ol>
<p>Why do you say it is too long? I work with terminology type names of similar length and did not have problems.</p>

---

## Post #3 by @muratmaga (2024-04-04 14:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>u want to use it. No need to delete it (I am not even sure the current API supports it), all you need to do is restart Slicer and you won’t have any custom terminology loaded.</p>
</blockquote>
</aside>
<p>That’s not the behavior I am observing. The imported terminology is persistent after multiple restarts.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="35240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Why do you say it is too long? I work with terminology type names of similar length and did not have problems.</p>
</blockquote>
</aside>
<p>It makes it harder to distinguish between consecutive segments:<br>
e.g.</p>
<p>upper first primary molar tooth<br>
upper second primary molar tooth<br>
upper third primary molar tooth<br>
upper fourth primary molar tooth<br>
upper first secondary molar tooth<br>
upper second seconday molar tooth<br>
upper third secondary molar tooth<br>
upper fourth  secondary molar tooth<br>
vs<br>
UdM1<br>
UdM2<br>
UdM3<br>
UdM4<br>
UM1<br>
UM2<br>
UM3<br>
UM4</p>
<p>(UdM1 stands for upper deciduous molar <span class="hashtag-raw">#1</span>)</p>

---

## Post #4 by @lassoan (2024-04-04 16:06 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="35240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>There is a field called “3dSlicerLabel” but that does’t seem to affect the displayed value.</p>
</blockquote>
</aside>
<p>“3sSlicerLabel” field specifies the default segment name (see orange arrow):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f2d4d63db67db4b90f18881ca5a625ad7f3db2e.png" data-download-href="/uploads/short-url/2agdKAxFq8jlRc84Ys61cxx8APk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2d4d63db67db4b90f18881ca5a625ad7f3db2e_2_690x492.png" alt="image" data-base62-sha1="2agdKAxFq8jlRc84Ys61cxx8APk" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2d4d63db67db4b90f18881ca5a625ad7f3db2e_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2d4d63db67db4b90f18881ca5a625ad7f3db2e_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f2d4d63db67db4b90f18881ca5a625ad7f3db2e.png 2x" data-dominant-color="353C42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×797 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This label gives more flexibility in how a name appears, which can be particularly useful if there are modifiers, because then automatically generated names are not always the best.</p>
<pre><code class="lang-auto">          {
            "CodingSchemeDesignator": "SCT",
            "CodeValue": "46027005",
            "CodeMeaning": "Common iliac vein",
            "Modifier": [
              {
                "3dSlicerLabel": "right common iliac vein",
                "recommendedDisplayRGBValue": [ 0, 151, 206 ],
                "CodingSchemeDesignator": "SCT",
                "CodeValue": "24028007",
                "CodeMeaning": "Right"
              },
              {
                "3dSlicerLabel": "left common iliac vein",
                "recommendedDisplayRGBValue": [ 0, 151, 206 ],
                "CodingSchemeDesignator": "SCT",
                "CodeValue": "7771000",
                "CodeMeaning": "Left"
              },
              {
                "CodingSchemeDesignator": "SCT",
                "CodeValue": "51440002",
                "CodeMeaning": "Right and left"
              }
            ]
          }, 
</code></pre>
<p>However, you don’t have to use <code>3dSlicerLabel</code>. You can change <code>CodeMeaning</code> value instead. A term is specified only by coding scheme designator and code value; code meaning is for convenience only (for example to provide some user-friendly displayable string).</p>

---

## Post #5 by @cpinter (2024-04-05 09:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="35240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>That’s not the behavior I am observing. The imported terminology is persistent after multiple restarts.</p>
</blockquote>
</aside>
<p>I’m surprised, I need to import the terminology every time. <a class="mention" href="/u/lassoan">@lassoan</a> do you know what is the expected behavior?</p>
<p>About the long code meanings, we also have a terminology for teeth, this is how we created it:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65143e5dcb7423a51e6cb2cd8384873a9db62b19.png" alt="image" data-base62-sha1="eqbAY3rTXKejECpK8iuXekirFjj" width="431" height="342"><br>
I guess the teeth do not have numbering for animals…<br>
Anyway you can edit the code meaning as you wish.</p>

---

## Post #6 by @muratmaga (2024-04-05 09:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="35240">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I guess the teeth do not have numbering for animals…<br>
Anyway you can edit the code meaning as you wish.</p>
</blockquote>
</aside>
<p>Yes, that’s human specific. Varying number of teeth and dental formula in different organisms makes it impossible to use such a numbering scheme.</p>

---
