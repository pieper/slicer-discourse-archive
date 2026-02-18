# How to prevent Slicer from "forgetting" slicer.util.loadColorTable after closing a scene

**Topic ID**: 9932
**Date**: 2020-01-24
**URL**: https://discourse.slicer.org/t/how-to-prevent-slicer-from-forgetting-slicer-util-loadcolortable-after-closing-a-scene/9932

---

## Post #1 by @Vincent_C (2020-01-24 01:10 UTC)

<p>Hi all,</p>
<p>I am using <strong>slicer.util.loadColorTable('c:/Users…)</strong> in slicerrc.py to direct Slicer to load a custom color table file in a specified location. This works great, however, when I close the scene and “Add Data into the scene”, the option for my custom colour table no longer shows up in the drop-down menu. How can I prevent the table from disappearing after closing a scene?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-01-24 01:17 UTC)

<p>There is no standard way of storing label and color information in a volume file.</p>
<p>One option is to save the scene (containing the labelmap and color table) as a single .mrb file. Click on the package icon in the Save data dialog to toggle between single/multi-file saving.</p>
<p>Or, you can save the segmentation as a segmentation node (right-click the labelmap volume node to convert it to segmentation). Segmentation files are volume files that contain all segment names and color in custom fields.</p>

---

## Post #3 by @Vincent_C (2020-01-24 01:23 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply. What if I were to use a script similar to that from <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_custom_color_table" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_custom_color_table</a> in slicerrc.py?:</p>
<pre><code class="lang-python">invertedocean = slicer.vtkMRMLColorTableNode()
invertedocean.SetTypeToUser()
invertedocean.SetNumberOfColors(256)
invertedocean.SetName("InvertedOcean")

for i in range(0,255):
    invertedocean.SetColor(i, 0.0, 1 - (i+1e-16)/255.0, 1.0, 1.0)

slicer.mrmlScene.AddNode(invertedocean)
</code></pre>
<p>It also gives the option to choose the InvertedOcean color but disappears after closing a scene. Can the script be modified so that the color is saved?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-01-24 01:28 UTC)

<p>There are many options to keep a node around but probably the simplest is to make it a singleton node (one instance per scene, identified by node type and singleton tag, not deleted when scene is closed) by calling <code>invertedocean.SetSingletonTag("Vincent.InvertedOcean")</code>.</p>

---

## Post #5 by @Vincent_C (2020-01-24 01:38 UTC)

<p>Hi Andras,</p>
<p>This sounds like a possible solution! Say I am using the command: slicer.util.loadColorTable(‘c:/Users/Vince/My_Color_Table.ctbl’) - Can I also use the singleton tag to keep the node corresponding vtkMRMLColorTableNode around?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2020-01-24 01:40 UTC)

<p>Yes, you can make any node singleton by setting its SingletonTag.</p>

---

## Post #7 by @Vincent_C (2020-01-24 01:47 UTC)

<p>Oh that is great! I am a novice user, can you give me an example of how to do that if my node is as so: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dd7c292d292a7e5c0294003ad2089c4c1a328aa.png" data-download-href="/uploads/short-url/mwle3d4Ov2ixaJd7VWt4446qp0S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dd7c292d292a7e5c0294003ad2089c4c1a328aa_2_690x30.png" alt="image" data-base62-sha1="mwle3d4Ov2ixaJd7VWt4446qp0S" width="690" height="30" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9dd7c292d292a7e5c0294003ad2089c4c1a328aa_2_690x30.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dd7c292d292a7e5c0294003ad2089c4c1a328aa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dd7c292d292a7e5c0294003ad2089c4c1a328aa.png 2x" data-dominant-color="A0C8E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×33 8.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-01-24 01:57 UTC)

<p><code>slicer.util.load...</code> methods return the loaded node, so you can call <code>SetSingletonTag</code> on that.</p>

---
