---
topic_id: 29785
title: "Toggling Visibility Of Several Curves Within A Specific Fold"
date: 2023-06-01
url: https://discourse.slicer.org/t/29785
---

# Toggling visibility of several curves within a specific folder

**Topic ID**: 29785
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/toggling-visibility-of-several-curves-within-a-specific-folder/29785

---

## Post #1 by @Patrick_Li (2023-06-01 22:36 UTC)

<p>I’m working on a custom module that toggles the visibility of the markups within a specific folder. For example, a user can select the option “Nodule 1”, which causes only the markups within the Nodule 1 folder to be visible. Is there a way to accomplish this? Attached is a screenshot illustrating the problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7b22f9527e70cb38908629ead349656c280c913.jpeg" data-download-href="/uploads/short-url/x3G3xDNbdN6f1Z4OaaVjfWDnTz5.jpeg?dl=1" title="Screenshot (847)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7b22f9527e70cb38908629ead349656c280c913_2_690x388.jpeg" alt="Screenshot (847)" data-base62-sha1="x3G3xDNbdN6f1Z4OaaVjfWDnTz5" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7b22f9527e70cb38908629ead349656c280c913_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7b22f9527e70cb38908629ead349656c280c913_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7b22f9527e70cb38908629ead349656c280c913_2_1380x776.jpeg 2x" data-dominant-color="999CA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (847)</span><span class="informations">1920×1080 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Patrick_Li (2023-06-01 22:43 UTC)

<p>For reference, this is what my UI looks like.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff4de198aa391fd42079ca5b02a928ac4ad44bf8.jpeg" data-download-href="/uploads/short-url/AqwC74lXv8uenECfHwKBrZ4WWoM.jpeg?dl=1" title="Screenshot (849)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff4de198aa391fd42079ca5b02a928ac4ad44bf8_2_690x388.jpeg" alt="Screenshot (849)" data-base62-sha1="AqwC74lXv8uenECfHwKBrZ4WWoM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff4de198aa391fd42079ca5b02a928ac4ad44bf8_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff4de198aa391fd42079ca5b02a928ac4ad44bf8_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff4de198aa391fd42079ca5b02a928ac4ad44bf8_2_1380x776.jpeg 2x" data-dominant-color="999CA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (849)</span><span class="informations">1920×1080 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @mikebind (2023-06-02 00:19 UTC)

<p>Check out the Slicer script repository, which should have most of the pieces for what you need.  For example, this section has how to control the visibility of a MarkupsCurve: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties</a></p>
<p>You can identify and manipulate the items in a folder using the subject hierarchy, see the various parts of this section: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy</a></p>
<p>Controlling visibility at the folder level is slightly more complicated in that the first time you want to do it you need to explicitly create a display node for that folder as described here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item</a></p>
<p>That should help you get started.  If you have further questions or run into problems please feel free to continue the conversation here.</p>

---

## Post #4 by @mikebind (2023-06-02 19:53 UTC)

<p>Patrick followed up with a message with this question (adding it here so the response stays visible and can help other people searching the discourse):</p>
<blockquote>
<p>Hello, thanks for you help! I had one more question on this topic. How do you save all of your data into a specific folder? I’m aware of the saveNode() function, but I’m not sure which node I need to save in order for everything to be saved properly.</p>
</blockquote>
<p>The answer depends on what you mean by saving properly.</p>
<ul>
<li>If you mean saving all the created curves and all imported imaging data as well as the subject hierarchy organization so that you can reload it later, then what you want to do is save the “scene”.  You can specify where everything gets saved in an interactive dialog window by clicking the “Save data” toolbar button (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#save-data">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#save-data</a>). The hierarchy organization is preserved in the MRML scene file (.mrml), which is semi-readable XML.  The rest of the saved nodes will hold all the data, but will not themselves know anything about how they were organized into the subject hierarchy.</li>
<li>If you mean saving individual nodes to a directory structure matching the subject hierarchy structure (like saving the curve1, curve2, comment, and table relating to Nodule 1 into a directory folder named Nodule1 and saving the corresponding nodes for Nodule2 into a directory folder named Nodule2), I’m not aware of an existing automated way to do that, but it would be straightforward to write python code to do. Using the subject hierarchy node, you could traverse the children of a hierarchy folder and use <code>saveNode()</code> to save the node to a directory folder with a matching name.  If you then want to load from that directory structure and recreate the subject hierarchy organization, you would need to write the code to do that as well (it would basically just be the reverse process: add a subject hierarchy folder for each directory folder, traverse the saved files in the directory folder, loading each node and then setting its subject hierarchy parent to the correct subject hierarchy folder).</li>
</ul>

---
