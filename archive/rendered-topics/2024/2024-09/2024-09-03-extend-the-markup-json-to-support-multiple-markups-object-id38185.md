---
topic_id: 38185
title: "Extend The Markup Json To Support Multiple Markups Object"
date: 2024-09-03
url: https://discourse.slicer.org/t/38185
---

# Extend the markup json to support multiple markups object

**Topic ID**: 38185
**Date**: 2024-09-03
**URL**: https://discourse.slicer.org/t/extend-the-markup-json-to-support-multiple-markups-object/38185

---

## Post #1 by @muratmaga (2024-09-03 16:43 UTC)

<p>In SlicerMorph, we often create different types of markup objects on the same volume/module (e.g., anatomical landmarks, geometrically sampled landmarks, resampled curves etc.).</p>
<p>Due to analytical requirements, we have to merge these objects into a single pointList node. There are couple problems with that:</p>
<ol>
<li>We loose visual properties that might have been set to distinguish these object (red for anatomical, blue for semiLM, yellow for curves type of things).</li>
<li>We have to use the description field to tell what these points were previously (because certain analyses distinguish between these points)</li>
<li>Not a good practice for data management as it increases data redundancy (user needs to preserve the individual files, if they have to redo/alter things)</li>
</ol>
<p>Instead more elegant solution would be to save these into a single JSON file. The decision to save the markups objects  individually versus by as a single file can be made actively by the user by nesting these markups objects under a hierarchy, from which the filename of the combined JSON file can be derived from.</p>
<p>We can implement this feature inside the SlicerMorph, but I think can have a broad appeal outside of SlicerMorph, so wanted to discuss.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dd3f1a79d6770c23677e75903a80f1e9125db77.jpeg" data-download-href="/uploads/short-url/6xpzAwGANVpKgSfH5b7nD8SSk51.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dd3f1a79d6770c23677e75903a80f1e9125db77_2_690x384.jpeg" alt="image" data-base62-sha1="6xpzAwGANVpKgSfH5b7nD8SSk51" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dd3f1a79d6770c23677e75903a80f1e9125db77_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dd3f1a79d6770c23677e75903a80f1e9125db77_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dd3f1a79d6770c23677e75903a80f1e9125db77_2_1380x768.jpeg 2x" data-dominant-color="C7C8C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1070 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-09-03 17:16 UTC)

<p>Reading multiple markups from a single markup json file is already supported. There is currently no GUI for creating such combined file, but can be easily done using a text editor for testing. A right-click menu item could be added to <code>Folder</code> item type in the subject hierarchy tree (no Slicer core change is needed, a Python scripted Subject Hierarchy Plugin would work) to export all markups in that folder into a single file.</p>
<p>The markups reader could be updated to put markups that were loaded from a single file into a subject hierarchy subfolder.</p>
<p>One limitation is that we cannot <em>save</em> multiple nodes into a single file. We can save one node into multiple files. We can also <em>import/export</em> multiple nodes from/to a single file. If we wanted to change this, it would require changing the 1-to-1 association between data node and storage node, and it would make the saving logic much more complex.</p>

---

## Post #3 by @muratmaga (2024-09-03 17:21 UTC)

<p>Can you clarify these two statements?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="38185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A right-click menu item could be added to <code>Folder</code> item type in the subject hierarchy tree (no Slicer core change is needed, a Python scripted Subject Hierarchy Plugin would work) to export all markups in that folder into a single file.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="38185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>One limitation is that we cannot <em>save</em> multiple nodes into a single file.</p>
</blockquote>
</aside>
<p>Using the visual I provided above, what would happen if I try to read the combined JSON file into Slicer? I would not get three separate nodes?</p>

---

## Post #4 by @lassoan (2024-09-03 17:24 UTC)

<p>Reading (importing) and exporting multiple nodes to/from file is fine.</p>
<p>Import is already implemented in the markups reader, so if you drag-and-drop a json file containing several markups to the Slicer application window, each markup will appear as a separate node.</p>

---

## Post #5 by @muratmaga (2024-09-03 17:40 UTC)

<p>ok. Thanks for the clarification.</p>
<p>This doesn’t seem to resolve the issue <span class="hashtag-raw">#3</span> (data redundancy), as I understand there will continue to be two sets of markups (one individual files saved with the scene, and one combined that’s exported).</p>

---

## Post #6 by @pieper (2024-09-03 17:55 UTC)

<p>One option could be to create a custom node type that has a dedicated storage node type that saves multiple referenced markups into a single file of the type you want.  Then it would be able to re-use the existing save and load mechanisms.  You could set the <code>SaveWithScene</code> flag to <code>False</code> for the referenced markup nodes so that you’d only have the one copy saved.  This custom compound-markup type could also have logic and gui to make it easier to manage the naming and display properties.</p>

---

## Post #7 by @jamesobutler (2024-09-03 18:47 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="38185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Due to analytical requirements, we have to merge these objects into a single pointList node.</p>
</blockquote>
</aside>
<p>Could describe more about this? Which analysis are you referring to? Is this outside of 3D Slicer? You are not able to select multiple markup objects to use as inputs?</p>

---

## Post #8 by @muratmaga (2024-09-03 19:14 UTC)

<p>In generalized procrustes analysis, you need to have the same number of landmarks for every sample. And more importantly, when the superimposition is generated non-anatomical landmarks (semiLMs, or resampled points on curves) are slid into new positions by minimizing the bending energy (or alternatively procrustes distances), but anatomical landmarks are treated as rigid. So you need to able to distinguish anatomical (fixed) landmarks from other types of landmarks.</p>
<p>Our GPA module (as well many other packages) have a one file per specimen/sample paradigm, so we if you are using semiLMs and anatomical LMs together, you need to concatenate them into a single file.</p>

---
