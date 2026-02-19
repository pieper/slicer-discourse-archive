---
topic_id: 35798
title: "Create Standard Terminology For New Segmentation Project"
date: 2024-04-25
url: https://discourse.slicer.org/t/35798
---

# Create standard terminology for new segmentation project

**Topic ID**: 35798
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/create-standard-terminology-for-new-segmentation-project/35798

---

## Post #1 by @lassoan (2024-04-25 19:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="35719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/exporting-a-segmentation-paired-to-a-custom-colortable/35719/8">Exporting a segmentation paired to a custom colortable</a></div>
<blockquote>
<p>am not sure how this will fix the conversion to the labelmap though. Labelmaps are what goes into the ML training, and they need to have indices. So we will always need some sort of lookup between segment labels and labelmap indices, regardless if the segment labels comes from a standardized terminology. Or am I overlooking something?</p>
</blockquote>
</aside>
<p>The key is to use a project-independent, universal, archival quality segmentation file format. For example, .seg.nrrd file with terminology or DICOM Segmentation Object can both fulfill this role.</p>
<p>You can perform a very simple fully-automatic normalization step (e.g., that is <a href="https://github.com/lassoan/slicerio?tab=readme-ov-file#extract-selected-segments-with-chosen-label-values">implemented in slicerio Python package</a>) to convert the universal segmentation files to project-specific nrrd files (where you use the same label values for the same structure in all labelmap images). This allows compilation of data from many collections, it does not matter what label values are used in each collection, or if different internal names are used, or some collections have extra segments, etc. These automatically-derived normalized segmentation files are considered temporary files, only used for training, and should not be shared or archived (to avoid redundant storage, backup, complex administration of licenses of combined collections, etc).</p>
<p>I’ve provided a bit more details <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/UsingStandardTerminology.md#use-standard-terminology-during-model-training">here</a>.</p>

---

## Post #2 by @muratmaga (2024-04-25 19:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The key is to use a project-independent, universal, archival quality segmentation file format.</p>
</blockquote>
</aside>
<p>Exactly. We are starting a new project that will involve segmenting a lot of different organisms using a consistent terminology. But we have to build our own terminology from scratch. So any pointers on how to go about it correctly is much appreciated.</p>
<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, .seg.nrrd file with terminology</p>
</blockquote>
</aside>
<p>Will it be possible to embed custom terminology in seg.nrrd? How is this different than current practice.</p>
<p><a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/UsingStandardTerminology.md#use-standard-terminology-during-model-training">From here</a></p>
<p>I did not understand this sentence:</p>
<pre><code class="lang-auto">The segmentation (.seg.nrrd) files may have the segments in different order, therefore different label values may be used for the same segment in each file.
</code></pre>
<p>Is this meant to be a warning about the ordering?</p>
<p>Also, for the labels.csv that needs to be created for slicerio conversion, it is not clear to me whether the header file is fixed or we create our own custom header? Most of these do not fit our terminology</p>
<pre><code class="lang-auto">LabelValue,Name,SegmentedPropertyCategoryCodeSequence.CodingSchemeDesignator,SegmentedPropertyCategoryCodeSequence.CodeValue,SegmentedPropertyCategoryCodeSequence.CodeMeaning,SegmentedPropertyTypeCodeSequence.CodingSchemeDesignator,SegmentedPropertyTypeCodeSequence.CodeValue,SegmentedPropertyTypeCodeSequence.CodeMeaning,SegmentedPropertyTypeModifierCodeSequence.CodingSchemeDesignator,SegmentedPropertyTypeModifierCodeSequence.CodeValue,SegmentedPropertyTypeModifierCodeSequence.CodeMeaning,AnatomicRegionSequence.CodingSchemeDesignator,AnatomicRegionSequence.CodeValue,AnatomicRegionSequence.CodeMeaning,AnatomicRegionModifierSequence.CodingSchemeDesignator,AnatomicRegionModifierSequence.CodeValue,AnatomicRegionModifierSequence.CodeMeaning
</code></pre>

---

## Post #3 by @lassoan (2024-04-25 20:04 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Will it be possible to embed custom terminology in seg.nrrd?</p>
</blockquote>
</aside>
<p>The codes are embedded in the seg.nrrd file. The terminology must be an external file (you don’t want to redefine the entire terminology in each segmentation file).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>How is this different than current practice.</p>
</blockquote>
</aside>
<p>The current practice unfortunately is that people leave the terminology code at the general “tissue” default, and use the segment name to identify segments.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also, for the labels.csv that needs to be created for slicerio conversion, it is not clear to me whether the header file is fixed or we create our own custom header? Most of these do not fit our terminology</p>
</blockquote>
</aside>
<p>There are 2 main hierarchy levels: category and type (with an optional modifier). In addition to this, you can specify anatomical region (with an optional modifier). This is universal terminology, so it should be applicable to anything in biomedical computing. We’ll simplify the column names to the ones described <a href="https://github.com/Slicer/Slicer/issues/7593">here</a>, because I agree that the current column names are too long and confusing.</p>
<p>You don’t have to use SNOMED CT, the scheme is compatible with any terminology, such as TA2, FMA, etc.</p>
<blockquote>
<p>Is this meant to be a warning about the ordering?</p>
</blockquote>
<p>It is just an example of why you may end up having segment ending up with different label values. Maybe not the best example. I need to clarify it more.</p>

---

## Post #4 by @muratmaga (2024-04-25 20:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You don’t have to use SNOMED CT, the scheme is compatible with any terminology, such as TA2, FMA, etc.</p>
</blockquote>
</aside>
<p>We are using UBERON which provides the largest consolidated terminology for vertebrates. Here are some terms we are likely to include (all of them are bones). How would you go about building a terminology from these?</p>
<p><a href="https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0011639">UBERON:0011639 (ebi.ac.uk)</a></p>
<p><a href="https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0004743">UBERON:0004743 (ebi.ac.uk)</a></p>
<p><a href="https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0001688">UBERON:0001688 (ebi.ac.uk)</a></p>
<p><a href="https://www.ebi.ac.uk/ols4/ontologies/uberon/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FUBERON_0008194">UBERON:0008194 (ebi.ac.uk)</a></p>

---

## Post #5 by @lassoan (2024-04-25 22:03 UTC)

<p>UBERON is a great choice. It has a wide scope and it is freely usable, including the ontology.</p>
<p>The coding scheme designator is <a href="https://dicom.nema.org/medical/dicom/current/output/html/part16.html#table_8-1">UBERON</a>, code value is for example <code>0011639</code>, and code meaning is <code>frontoparietal bone</code>.</p>
<p>You can put all the codes you want to use in a .term.json file, drag-and-drop it to the Slicer window, and they will be automatically be imported and will be available in the terminology popup.</p>
<p>Since UBERON is open, we could try to format entire terminology (all the anatomical structures) as a .term.json file and see how well Slicer’s terminology selector can cope with it.</p>

---

## Post #6 by @muratmaga (2024-04-26 02:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since UBERON is open, we could try to format entire terminology (all the anatomical structures) as a .term.json file and see how well Slicer’s terminology selector can cope with it.</p>
</blockquote>
</aside>
<p>Uberon has thousands of terms. If we fully incorporate it, I am worried that it might be too big to manage and navigate (having to search for terms for a segment wouldn’t be conducive to using terminology).</p>
<p>I have an abbreviated version of some common <a href="https://github.com/SlicerMorph/MD_E15/blob/main/SlicerMorph_segmentation_category_type.json">skeletal terms here</a></p>
<p>Can you take a look and comment on it? It seems to work with terminology (i.e, valid JSON file), but I am not sure if we correctly organized it. (BTW, assigned UBERON numbers are fake. I didn’t try to query and pull from it).</p>

---

## Post #7 by @lassoan (2024-04-26 05:00 UTC)

<p>I did a quick test, downloaded <a href="https://obophenotype.github.io/uberon/current_release/"><code>uberon-full.json</code></a> and wrote this little script to convert all anatomical structures into a Slicer terminology json file.</p>
<pre data-code-wrap="python"><code class="lang-python">uberonFile = "path/to/uberon-full.json"
terminologyFile = "path/to/uberon.term.json"

import json
import random

with open(uberonFile, 'r', encoding='utf-8') as file_object:
    uberon = json.load(file_object)

types = []
for node in uberon["graphs"][0]["nodes"]:
    if not node["id"].startswith("http://purl.obolibrary.org/obo/UBERON_"):
        continue
    if not node.get("lbl"):
        # deprecated
        continue
    types.append({
        "CodingSchemeDesignator": "UBERON",
        "CodeValue": node["id"].split("_")[-1],
        "CodeMeaning": node["lbl"],
        "recommendedDisplayRGBValue": [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        })

terminology = {
  "SegmentationCategoryTypeContextName": "Segmentation category and type - Uberon anatomical structures",
  "@schema": "https://raw.githubusercontent.com/qiicr/dcmqi/master/doc/segment-context-schema.json#",
  "SegmentationCodes": {
    "Category": [
      {
        "CodingSchemeDesignator": "SCT", "CodeValue": "123037004", "CodeMeaning": "Anatomical Structure",
        "showAnatomy": False,
        "Type": types
      }
    ]
  }
}

with open(terminologyFile, "w") as f:
    json.dump(terminology, f, indent=4)
</code></pre>
<p>The result is a small file containing 15574 structures. You can download it from <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/uberon.term.json">here</a>. You can drag-and-drop it into Slicer and you have all UBERON terms readily selectable - no chance for typos, no need to manually copy codes, etc.</p>
<p>Slicer terminology selector was a bit slow (filtering by name took a few seconds), but after some optimization it is now very fluid. I’ve submit a <a href="https://github.com/Slicer/Slicer/pull/7714">pull request</a> with the changes, it should be available in the Slicer Preview Release within a few days.</p>
<p>There are a few limitations of this approach:</p>
<ul>
<li>The terminology browser in Slicer currently does not use an ontology (shows just a flat list, not possible to jump to parent or get a list of children), so it may be difficult to find the right term. However, you can use the online UBERON browser to explore the various ontologies and find the right term, which you can then very easily find by name in Slicer.</li>
<li>I’m not sure if you need modifiers. If yes, then you need to find an automated way to figure out what modifiers are relevant for what structures. Maybe something simple like adding <code>left</code> and <code>right</code> modifier to every type that does not have left or right in the name already could cover what is needed.</li>
<li>Color is now generated randomly. It could make sense to get generic color from the ontologies (e.g., bones are white/yellow, muscles red, arteries deep red, veins blue, etc. maybe with some randomization)</li>
</ul>
<p>To make the selection easier, it may make sense to also create smaller terminology files for specific projects that contains a subset of this full list. This subset file would have a unique <code>SegmentationCategoryTypeContextName</code>, for example <code>SlicerMorph Dentition</code>. I would keep the <code>Anatomical Structure</code> category for <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_7150.html">DICOM compatibility</a>. <code>showAnatomy</code> has to be set to false for anatomical structures (it only makes sense to specify anatomical region selector if the type is not an anatomical structure, e.g., if the type is a <code>needle</code> then you can specify the anatomical region it is in). I don’t think you need to use modifiers (the UBERON codes seem to usually include it). I would drop all the attributes that you don’t use (context group name, cid, etc.).</p>
<p>It would look something like this:</p>
<pre data-code-wrap="json"><code class="lang-json">{
    "SegmentationCategoryTypeContextName": "SlicerMorph Dentition",
    "@schema": "https://raw.githubusercontent.com/qiicr/dcmqi/master/doc/schemas/segment-context-schema.json#",
    "SegmentationCodes": {
        "Category": [
            {
                "CodingSchemeDesignator": "SCT",
                "CodeValue": "123037004",
                "CodeMeaning": "Anatomical Structure",
                "showAnatomy": false,
                "Type": [
                    {
                        "recommendedDisplayRGBValue": [ 0, 179, 92 ],
                        "CodeValue": "100022",
                        "CodingSchemeDesignator": "UBERON",
                        "CodeMeaning": "Maxillary Molar 1",
                        "3dSlicerLabel": "maxillary molar 1",
                        "Modifier": [
                            {
                                "recommendedDisplayRGBValue": [0, 179, 92 ],
                                "CodingSchemeDesignator": "SCT",
                                "CodeValue": "24028007",
                                "CodeMeaning": "Right",
                                "3dSlicerLabel": "right maxillary molar 1",
                            },
...
                      ]
                    }
                ]
            }
        ]
    }
}
...
</code></pre>

---

## Post #8 by @pieper (2024-04-26 12:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Color is now generated randomly. It could make sense to get generic color from the ontologies (e.g., bones are white/yellow, muscles red, arteries deep red, veins blue, etc. maybe with some randomization)</p>
</blockquote>
</aside>
<p>It would be great if we could pull in community contributed standards like the one Jiami has done:<br>
<a href="http://www.graysvertebrateanatomy.com/work/colorsofskullanatomy/" class="onebox" target="_blank" rel="noopener">http://www.graysvertebrateanatomy.com/work/colorsofskullanatomy/</a></p>
<p>But these should be selectable - sometimes you’ll want all the bones to be the same and sometimes you’ll want to subdivide them.</p>

---

## Post #9 by @muratmaga (2024-04-26 15:43 UTC)

<p>Dear Andras, thank you so much for doing this. I downloaded the file you generated.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The terminology browser in Slicer currently does not use an ontology (shows just a flat list, not possible to jump to parent or get a list of children), so it may be difficult to find the right term. However, you can use the online UBERON browser to explore the various ontologies and find the right term, which you can then very easily find by name in Slicer.</p>
</blockquote>
</aside>
<p>This is important to optimize, because if search takes longer than manually renaming a segment, it is unlikely that people will bother to use the terminologies.</p>
<p>At this point, everything seems to be listed under the “anatomical structure”. We should divide this into other contexts, such as skeletal system, muscles, organs etc. To make navigating the list easier and faster.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7b7dbec25bb2c0d0efd2cab9a1d08593943f6b3.png" data-download-href="/uploads/short-url/suMVPVK7C9zFnB9TnN0thqYetCX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b7dbec25bb2c0d0efd2cab9a1d08593943f6b3_2_690x387.png" alt="image" data-base62-sha1="suMVPVK7C9zFnB9TnN0thqYetCX" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b7dbec25bb2c0d0efd2cab9a1d08593943f6b3_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7b7dbec25bb2c0d0efd2cab9a1d08593943f6b3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7b7dbec25bb2c0d0efd2cab9a1d08593943f6b3.png 2x" data-dominant-color="E6E9EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×489 56.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure if you need modifiers.</p>
</blockquote>
</aside>
<p>The only modifier we need is the L/R, and for some of the skeletal terms Uberon seem to provide left and right as separate structures. So at this point I can’t think of other usage, but I will check with my colleagues.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="35798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Color is now generated randomly.</p>
</blockquote>
</aside>
<p>We have about 20 visually distinct colors. I think the idea is to use these colors in regions that are closeby or in articulation (e.g., cranial bones), and then recycle them for different anatomical regions. Assigning same color to patella and scapula wouldn’t hurt the visual representation, as they are not near by. Most of our segmentations are bones, so having a fixed color for bone types will not really work for us.</p>

---

## Post #10 by @rkikinis (2024-04-26 15:52 UTC)

<p>For human anatomy you can look at</p>
<p>[</p>
<p><a href="https://ta2viewer.openanatomy.org/?id=3932" rel="noopener nofollow ugc">TA2 Viewer</a><br>
<a href="https://ta2viewer.openanatomy.org/?id=3932" rel="noopener nofollow ugc">ta2viewer.openanatomy.org</a></p>
<p><a href="https://ta2viewer.openanatomy.org/?id=3932" rel="noopener nofollow ugc"><img width="36" height="36" alt="apple-touch-icon.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49377266fff8fa85038a7f62817a2cdec07fe8fa.png" data-base62-sha1="arHEhCeHDvUP3tPmJeaBtZRxV2O"></a></p>
<p>](<a href="https://ta2viewer.openanatomy.org/?id=3932" class="inline-onebox" rel="noopener nofollow ugc">TA2 Viewer</a>)</p>
<p>Best<br>
Ron</p>
<p>This email is intended for non-work related messages</p>

---
