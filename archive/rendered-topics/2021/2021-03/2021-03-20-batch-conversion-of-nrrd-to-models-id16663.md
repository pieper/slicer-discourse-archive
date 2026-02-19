---
topic_id: 16663
title: "Batch Conversion Of Nrrd To Models"
date: 2021-03-20
url: https://discourse.slicer.org/t/16663
---

# Batch conversion of .nrrd to models

**Topic ID**: 16663
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/batch-conversion-of-nrrd-to-models/16663

---

## Post #1 by @Selva (2021-03-20 23:53 UTC)

<p>Hi,</p>
<p>I have a batch of segments-.nrrd files. (100s)<br>
I would like to load them (Add data- files) as .nrrd. (The default in add data dialog box is volume, so I manually change them to segmentations, one by one. (So they load as segmentations)</p>
<p>Then I have to convert them to models. Here also I either do it one by one in the data module by right click, convert to models or in segmentations module by exporting to models.</p>
<p>Is there an efficient way to do this, without going one by one.</p>
<ol>
<li>Load as segmentations (When default is volume)</li>
<li>Export to models</li>
</ol>
<p>Thanks</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-03-21 12:33 UTC)

<aside class="quote no-group" data-username="Selva" data-post="1" data-topic="16663" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/13edae/48.png" class="avatar"> Selva:</div>
<blockquote>
<ol>
<li>Load as segmentations (When default is volume)</li>
<li>Export to models</li>
</ol>
</blockquote>
</aside>
<p>You can write a short python script to do the above</p>
<pre><code class="lang-auto">segmentationNode = slicer.util.loadSegmentation(YOUR_FILE_NAME)  # load the data as a 

# Export segmentation to model
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)

</code></pre>
<p>There are more examples you can take a look at in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">python Script Repository.</a></p>
<p>-Andinet</p>

---

## Post #3 by @Selva (2021-03-21 13:08 UTC)

<p>Thanks  <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a></p>
<p>Tried , but does not load as a batch, does it?<br>
I ve got 100s of.nrrd  files in one folder, wanting them to load/ change at once.</p>
<p>Thanks</p>

---

## Post #4 by @cpinter (2021-03-21 15:24 UTC)

<p>If you combine the code provided by <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> with a <a href="https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory">for loop that traverses all files in a directory</a> then you’ll end up with a script that does just what you want.</p>

---

## Post #5 by @Selva (2021-03-22 03:27 UTC)

<p>Thank you very much, <a class="mention" href="/u/cpinter">@cpinter</a>  and <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a></p>
<p>I tried learning that, doing a loop</p>
<p>Sorry I am a medical person, couldn’t get to doing a loop.</p>
<p>Thanks</p>

---
