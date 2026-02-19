---
topic_id: 9154
title: "Openanatomys Reference Dicom Visualisation Of The Whole Proj"
date: 2019-11-15
url: https://discourse.slicer.org/t/9154
---

# OpenAnatomy's reference .dicom. Visualisation of the whole project

**Topic ID**: 9154
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/openanatomys-reference-dicom-visualisation-of-the-whole-project/9154

---

## Post #1 by @Melodicpinpon (2019-11-15 12:42 UTC)

<p>Good afternoon,</p>
<p>I would like to know if the .dicom used to create the meshes of OpenAnatomy was available to the public; and how the collaborative work functions.<br>
Is there a .dicom file containing hundreds of segmentations?<br>
Is there a way to visualise/hide all of the structures and their names?</p>
<p>I read that a common file format was still under development; I was wondering if Blender had been an option or not. Its new collection system would fit the needs of visualisation but as far as I know, the dicom viewing was only experimented on an older version and not much developed.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-11-15 13:59 UTC)

<p>Source images should be available for most atlases. Which atlas are you interested in?</p>
<p>Segmentation storage in DICOM was suboptimal until a few years ago and modern information object types are still not widely supported. Segmentation is most commonly stored as labelmap volume.</p>
<p>You can show/hide groups of structures using Data module.</p>
<p>A glTF based atlas file format is still under development. Mesh export is already implemented in SlicerOpenAnatomy, which can be loaded into and edited in Blender.</p>
<p>Blender’s (or any particular editing software’s) internal storage file format is not considered as an archival format for atlases, as these formats are optimized for storing the application state and therefore they are more complicated than necessary, change frequently, and controlled by the application’s developers.</p>

---

## Post #3 by @mhalle (2019-11-16 03:28 UTC)

<p>Hi Gauthier,</p>
<p>All of the current Open Anatomy datasets have NRRD files as their underlying image format. In almost all cases, the original DICOM files weren’t provided to us. Our goal is to provide DICOM data sets in the future; the open anatomy file format is agnostic to file format (much like HTML is agnostic for the formats of images on a page).</p>
<p>We don’t have large populations in open anatomy. I did a few of the MindBoggle brain data sets in open anatomy format. Let me know if a full conversion would be useful (those data files are NIFTI).</p>
<p>The current interface is limited and growing old in the tooth. We are looking to a cornerstone/OHIF based image viewer with a new 3D viewer, but no time frame at this time.</p>
<p>We are looking to glTF with extensions as an interchange format for annotated geometric models. I’m not familiar with Blender’s file format, but I don’t believe it’s likely to represent the association of images, region descriptions, annotations, and graphical styles for potentially multiple data sets. For that reason, Open Anatomy has a container file format with links to other data files. We have working prototypes of this concept, but it can always use more eyes looking at it, especially for use cases we haven’t yet really explored (like associating multiple atlases together).</p>
<p>I hope this helps a little to understand what the current state of things is. Let me know if you have additional questions or comments!</p>
<p>–Mike Halle</p>

---

## Post #4 by @Melodicpinpon (2019-11-16 08:04 UTC)

<p>Thank you for the answer.<br>
I beg you perdon because I made a terrible mistake: I had downloaded several years ago a huge serie of anatomical .obj files from this website:<br>
<a href="https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html" class="onebox" target="_blank" rel="nofollow noopener">https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html</a></p>
<p>Then I forgot about it and assumed that it had been done through the OpenAnatomy project.<br>
Sorry for the confusion.</p>
<p>Its viewer also lacks a collection system and a simple way to connect the mesh to the name of the structure. It would be great to get the dicom used for this modeling and a community working to turn it more precise.</p>

---

## Post #5 by @robertf (2019-11-16 20:49 UTC)

<p>Although the BodyParts3D modelling started from a whole-body MRI scan,<br>
‘missing details were supplemented and blurred contours were clarified<br>
using a 3D editing program by referring to textbooks, atlases and<br>
mock-up models by medical illustrators’ (Mitsuhashi, 2009,<br>
doi:10.1093/nar/gkn613). It might therefore not be useful to revert to<br>
the original image data at this point. The latest version of the data<br>
is dated 2018 Dec so it seems that development is on-going. It now<br>
contains 1000’s of anatomical structures.</p>
<p>The BodyParts3D project makes use of the Foundational Model of Anatomy<br>
ontology. I don’t know if the FMA is used in the Open Anatomy project.</p>
<ul>
<li>Robert</li>
</ul>

---

## Post #6 by @Melodicpinpon (2019-11-17 17:54 UTC)

<p>I wrote to the Life Science Database Archive (LSDB) institution to ask if they had meshes in higher definition because the downloadable folder mention ‘polygon reduction=99%’.<br>
The post processing work is very appreciable since the final mesh is so much cleaner than most of the segmentation models.</p>
<p>By the way, I just discovered today the ‘MorphoSource’ website:<a href="https://www.morphosource.org" rel="nofollow noopener">https://www.morphosource.org</a><br>
Many dicoms of animals are available directly or on demand.</p>

---

## Post #7 by @pieper (2019-11-18 13:22 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="6" data-topic="9154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>By the way, I just discovered today the ‘MorphoSource’ website:<a href="https://www.morphosource.org">https://www.morphosource.org </a><br>
Many dicoms of animals are available directly or on demand.</p>
</blockquote>
</aside>
<p>If you are interested in biological specimens you may also want to have a look at SlicerMorph:  <a href="https://slicermorph.github.io/">https://slicermorph.github.io/</a></p>

---

## Post #8 by @tsehrhardt (2019-11-18 15:13 UTC)

<p>You can get nrrd files and models from <a href="http://Embodi3d.com" rel="nofollow noopener">Embodi3d.com</a> too. There are a few whole body CTs.</p>

---

## Post #9 by @lassoan (2019-11-18 20:20 UTC)

<aside class="quote no-group" data-username="Melodicpinpon" data-post="6" data-topic="9154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I wrote to the Life Science Database Archive (LSDB) institution to ask if they had meshes in higher definition because the downloadable folder mention ‘polygon reduction=99%’.</p>
</blockquote>
</aside>
<p>If the input is a high-resolution image then 99% mesh reduction is not necessarily too much. Even with a basic method like VTK’s decimation, 90% reduction often does not result in visible difference in the mesh. If a more sophisticated method is used then 99% reduction may be achievable without any significant loss of detail.</p>
<aside class="quote no-group" data-username="Melodicpinpon" data-post="4" data-topic="9154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/melodicpinpon/48/3254_2.png" class="avatar"> Melodicpinpon:</div>
<blockquote>
<p>I had downloaded several years ago a huge serie of anatomical .obj files from this website:<br>
<a href="https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html">https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html </a></p>
</blockquote>
</aside>
<p>This seems like a very nice database. I’ve checked out the “partof” model, containing 1258 structures and wrote a short script to create subject hierarchy folders from the relation list text file.</p>
<details>
<summary>
Script for creating subject hierarchy from relation list</summary>
<pre data-code-wrap="python"><code class="lang-python">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
sceneItemID = shNode.GetSceneItemID()

def getItemParentsFmaIds(shNode, itemShItemId):
    existingParentShItemId = shNode.GetItemParent(itemShItemId)
    existingParentFmaIds = []
    while existingParentShItemId != sceneItemID:
        existingParentFmaIds.append(shNode.GetItemUID(existingParentShItemId, "FMA"))
        existingParentShItemId = shNode.GetItemParent(existingParentShItemId)
    return existingParentFmaIds

# Create partof hierarchy
inclusionListTable = getNode('partof_inclusion_relation_list').GetTable()
parentIdArray = inclusionListTable.GetColumnByName('parent id')
parentNameArray = inclusionListTable.GetColumnByName('parent name')
childIdArray = inclusionListTable.GetColumnByName('child id')
childNameArray = inclusionListTable.GetColumnByName('child name')
for i in range(inclusionListTable.GetNumberOfRows()):
    parentFmaId = parentIdArray.GetValue(i)
    parentShItemId = shNode.GetItemByUID("FMA", parentFmaId)
    if not parentShItemId:
        parentShItemId = shNode.CreateFolderItem(sceneItemID, parentNameArray.GetValue(i))
        shNode.SetItemUID(parentShItemId, "FMA", parentFmaId)
    childFmaId = childIdArray.GetValue(i)
    childShItemId = shNode.GetItemByUID("FMA", childFmaId)
    if not childShItemId:
        childShItemId = shNode.CreateFolderItem(sceneItemID, childNameArray.GetValue(i))
        shNode.SetItemUID(childShItemId, "FMA", childFmaId)
    existingParentFmaIds = getItemParentsFmaIds(shNode, childShItemId)
    if parentFmaId in existingParentFmaIds:
        # this parent is already a parent of the current item
        continue
    shNode.SetItemParent(childShItemId,parentShItemId)

# Update part list with names and FMA IDs
partsListTable = getNode('partof_element_parts').GetTable()
fmaIdArray = partsListTable.GetColumnByName('concept id')
filenameArray = partsListTable.GetColumnByName('element file id')
for i in range(partsListTable.GetNumberOfRows()):
    partNode = slicer.mrmlScene.GetFirstNodeByName(filenameArray.GetValue(i))
    if not partNode:
      continue
    parentFmaId = fmaIdArray.GetValue(i)
    parentShItemId = shNode.GetItemByUID("FMA", parentFmaId)
    if not parentShItemId:
        # this hierarchy is not found in the SH tree
        continue
    itemShItemId = shNode.GetItemByDataNode(partNode)
    existingParentFmaIds = getItemParentsFmaIds(shNode, itemShItemId)
    newParentFmaIds = getItemParentsFmaIds(shNode, parentShItemId)
    if len(newParentFmaIds)&gt;len(existingParentFmaIds):
        # New parent is more specific than the current (parent has more nesting levels)
        shNode.SetItemParent(itemShItemId, parentShItemId)
</code></pre>
</details>
<p>The resulting scene can be downloaded from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHuYk4-foSOXDfyM1gOA?e=GUczrX">here</a> (compatible with Slicer-4.11.x, revision r28625 or later).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e7da6ab42f7177d9c550ed969a23ddfebe92620.png" data-download-href="/uploads/short-url/mC4E50QZiXCoavVP5RihRdFoqbu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7da6ab42f7177d9c550ed969a23ddfebe92620_2_690x373.png" alt="image" data-base62-sha1="mC4E50QZiXCoavVP5RihRdFoqbu" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7da6ab42f7177d9c550ed969a23ddfebe92620_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7da6ab42f7177d9c550ed969a23ddfebe92620_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e7da6ab42f7177d9c550ed969a23ddfebe92620_2_1380x746.png 2x" data-dominant-color="BBB9DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unfortunately, the same model is usually listed in multiple branches of the hierarchy, and in the subject hierarchy tree a node can be only listed once, so structures are often “missing” from where you would expect to find it. For example, skin is listed in both <code>human body/integumentary system</code> and in <code>human body/integument/skin</code>, but in the subject hierarchy tree it can be only listed in one branch, so it appears only in <code>human body/integument/skin</code>. Due to this, probably the scene is not very useful as is, but may serve as an example of how to import hierarchical anatomical atlases into Slicer.</p>

---

## Post #10 by @mhalle (2019-11-18 20:54 UTC)

<blockquote>
<p><a href="https://discourse.slicer.org/u/lassoan">Andras Lasso</a>:<br>
If the input is a high-resolution image then 99% mesh reduction is not necessarily too much. Even with a basic method like VTK’s decimation, 90% reduction often does not result in visible difference in the mesh. If a more sophisticated method is used then 99% reduction may be achievable without any significant loss of detail.</p>
</blockquote>
<p>For these models, 99% is generally too much. Many of the brain structures are effectively useless nondescript lumps. To their credit, the lumps are nice and smooth looking, not strangely decimated.</p>
<p>Gauthier, if you get a response about the models or want us to help make a case for getting them, please let us know. We might be able to help because we clearly are not out to sell the results.</p>
<blockquote>
<p><a href="https://discourse.slicer.org/u/lassoan">Andras Lasso</a>:<br>
Unfortunately, the same model is usually listed in multiple branches of the hierarchy, and in the subject hierarchy tree a node can be only listed once, so structures are often “missing” from where you would expect to find it. For example, skin is listed in both  <code>human body/integumentary system</code>  and in  <code>human body/integument/skin</code> , but in the subject hierarchy tree it can be only listed in one branch, so it appears only in  <code>human body/integument/skin</code> . Due to this, probably the scene is not very useful as is, but may serve as an example of how to import hierarchical anatomical atlases into Slicer.</p>
</blockquote>
<p>We should talk more about how to organize these structures. I’m thinking more and more about faceted search rather than hierarchical trees. Overlapping groups of structures make sense. Imprecise ontologies such as FMA make handling cases like this a necessity, with Andras’s example being a prime case. One model should be able to be in two groups but only rendered once.</p>

---

## Post #11 by @Melodicpinpon (2019-11-19 08:47 UTC)

<p>Wow, I am impressed.<br>
Unfortunately I do not achieve to visualise the models. I will watch it better later.</p>
<p>The links for the references are great; I wish I could dive into all these anatomical treasures soon in the future.</p>
<p>Thank you so much.<br>
I will keep you informed if I get an answer from the japanese ‘Life Science Database Archive’.</p>

---

## Post #12 by @Melodicpinpon (2019-11-27 11:34 UTC)

<p>Goodmorning.</p>
<p>I did not receive any answer from the ‘Life Science Database’.<br>
It would be worth that you try and ask them if they can provide you the high resolution models, if you did not do it yet.</p>

---

## Post #13 by @Melodicpinpon (2020-01-07 14:31 UTC)

<p>Did you get any answer?</p>

---
