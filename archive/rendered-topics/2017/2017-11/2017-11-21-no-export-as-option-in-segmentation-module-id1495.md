---
topic_id: 1495
title: "No Export As Option In Segmentation Module"
date: 2017-11-21
url: https://discourse.slicer.org/t/1495
---

# No 'export as' option in Segmentation module

**Topic ID**: 1495
**Date**: 2017-11-21
**URL**: https://discourse.slicer.org/t/no-export-as-option-in-segmentation-module/1495

---

## Post #1 by @Remco (2017-11-21 14:00 UTC)

<p>In the segmentations models, there is no option to ‘export model as’ only ‘export new’ Thus the name has to be changed afterwards for new exports. This seems like a bug to me or is it intentional? At any rate it is inconsistent with the other modules. Please forgive me if this the wrong place for bug reports.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec4f6db3f662a541653be8a1bce9a347b4a39138.png" alt="image" data-base62-sha1="xIuRbCfhNqeBaJDO9XW4ApVTOfm" width="500" height="225"></p>

---

## Post #2 by @lassoan (2017-11-21 14:09 UTC)

<p>When you export to model nodes, you create multiple nodes (one for each segment), so it is not possible to select a single <em>model</em> node, but you have to create/select a <em>model hierarchy</em> node. If you select a model hierarchy node and export into that, then existing models that have a matching name will be updated.</p>

---

## Post #3 by @lassoan (2017-11-21 14:13 UTC)

<p>Maybe you miss “Create new…” option? “Export new…” is a somewhat more convenient option that does the same, except it saves you two clicks, but I have a look if it’s easy to enable “Create new…” option as well.</p>

---

## Post #4 by @Remco (2017-11-21 14:33 UTC)

<p>The “Create new…” option is exactly what I am looking for. It is present in the other modules, so it would make sense to have it here as well. If find that I have to be meticulous in naming files otherwise it easy to lose track of what all the files are for, especially since I am new to Slicer.</p>

---

## Post #5 by @lassoan (2017-11-21 14:42 UTC)

<p>Correct name is automatically created for new nodes : [SegmentationName]-label or [SegmentationName]-models). Do you find behavior of node selectors are better (where you must create a new node manually by 2 clicks; and must type node name if you don’t want to use a generic node name); or you just don’t like that the behavior is different here? If the behavior segmentations export node selector is better then we can gradually change all other node selectors to work the same way.</p>

---

## Post #6 by @cpinter (2017-11-21 15:48 UTC)

<p>This case is different than the regular output node selectors in two ways</p>
<ol>
<li>The output contains the very same data as the input, just a different format (i.e. export). So changing its name would actually cause confusion, and is undesirable. One of the main reasons for using Segmentation nodes instead Labelmap or Model nodes is to keep data together that belongs together without relying on manual naming conventions, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a>
</li>
<li>The output is not one node, but a hierarchy of nodes (and this is a shortcoming of Models, that disconnedted nodes contain information about the same anatomy), so choosing individual nodes is impossible</li>
</ol>
<p>For these reasons, we cannot use the same node selection as with simple processing modules that have an input, do something on it, and put the result in another simple node.</p>

---
