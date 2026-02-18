# Load Dicom Image and a mesh

**Topic ID**: 4468
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/load-dicom-image-and-a-mesh/4468

---

## Post #1 by @Abdelkhalek (2018-10-19 15:56 UTC)

<p>Hi, how can I create a .py script in order to create a button for loading a .mha, .hdr files and a button for .stl and .vtk files, please?</p>

---

## Post #2 by @pieper (2018-10-20 01:58 UTC)

<p>Start by looking through the programming tutorials:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a></p>
<p>The script repository also has lots of examples to learn from:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #3 by @Abdelkhalek (2018-10-20 10:06 UTC)

<p>Thank you for your answer. I checked both references but I did not find how can I import an .stl and .vtk files using a button and Python programming language. Could you please send me an exemple of the code?</p>

---

## Post #4 by @pieper (2018-10-20 13:30 UTC)

<p>I don’t think there’s an existing example that does exactly that - but it doesn’t sound like a very difficult task if you learn how to do it.  The best is to start with examples that do something similar and then experiment.</p>
<p>Why do you need this program?  What do you intend to do with it?</p>

---

## Post #5 by @lassoan (2018-10-21 02:46 UTC)

<p>You can load a model from stl or vtk file using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util"><code>slicer.util.loadModel()</code></a>. You may also use <code>slicer.util.openAddModelDialog()</code> to show a model file selector dialog and load the selected file:</p>
<pre><code>button = qt.QPushButton("Load!")
button.connect("clicked()", slicer.util.openAddModelDialog)
button.show()</code></pre>

---

## Post #6 by @Abdelkhalek (2018-10-22 08:52 UTC)

<p>Thank you Andras for your help,<br>
After using the code which you suggested :</p>
<pre><code class="lang-auto"># button for importing mesh files
    button = qt.QPushButton("Load Mesh")
    self.formFrame.layout().addWidget(button)
    button.connect("clicked()", slicer.util.openAddModelDialog)
    button.show()
</code></pre>
<p>I have got the mesh in the 3D Widget and out of the original image (dicom). The mesh is not visuliazed in 2D widgets.<br>
Could I have any solution to get the mesh inside of the original image for the 4 slicer widgets?<br>
Thank you in advance.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f4680d581f1e6bb1bad8dd44ac8fc30ae706658.png" data-download-href="/uploads/short-url/mJ0Y9XW3ncOLA0eGChCU57h23Vu.png?dl=1" title="mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f4680d581f1e6bb1bad8dd44ac8fc30ae706658_2_690x420.png" alt="mesh" data-base62-sha1="mJ0Y9XW3ncOLA0eGChCU57h23Vu" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f4680d581f1e6bb1bad8dd44ac8fc30ae706658_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f4680d581f1e6bb1bad8dd44ac8fc30ae706658_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f4680d581f1e6bb1bad8dd44ac8fc30ae706658.png 2x" data-dominant-color="727287"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mesh</span><span class="informations">1056×643 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-10-22 19:19 UTC)

<aside class="quote no-group" data-username="Abdelkhalek" data-post="6" data-topic="4468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a6a055/48.png" class="avatar"> Abdelkhalek:</div>
<blockquote>
<p>Could I have any solution to get the mesh inside of the original image for the 4 slicer widgets?</p>
</blockquote>
</aside>
<p>Yes. Enable slice intersections in the model node’s <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#aa73e1a73218ddeb1cd40bfbae4e17e58">display node</a> - see SetSliceIntersectionVisibility, SetSliceIntersectionOpacity, SetSliceIntersectionThickness.</p>
<p>Mulitple display modes are available: intersection and various projections - see details <a href="http://apidocs.slicer.org/master/classvtkMRMLModelDisplayNode.html#a7bf7b91a4a4db25759bed9965d8c40e8">here</a>.</p>

---

## Post #8 by @Abdelkhalek (2018-10-25 08:25 UTC)

<p>Thank you Andras.<br>
For now I have two issues:<br>
1- The mesh needs a linear transformation in order to be in the perfect location (correct and incorrect example is attached).<br>
2- How can I use the slicer fill feature from the Segmentations module as a python code in order to transform the region into a contour?</p>
<p>Thank you in advance<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca5e9f7416bda89c246eaceea6b90264e6482cad.png" alt="correct" data-base62-sha1="sSfb0DiLxkkYcwVyoXxoTyrKzP7" width="575" height="390"></p>

---

## Post #9 by @pieper (2018-10-25 14:02 UTC)

<p>At a first glance that looks like an RAS/LPS issue - see this for background: <a href="https://www.slicer.org/wiki/Coordinate_systems">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>Adding a transform diag(-1,-1,1,1) would fix that.</p>

---

## Post #10 by @Abdelkhalek (2018-10-25 18:17 UTC)

<p>Thank you Steve. However, I could not have an access to the node in order to apply the example of the linear transformation below:</p>
<pre><code># Linear Transformation
transformNode=slicer.util.getNode('LinearTransform_3')
referenceVolumeNode=slicer.util.getNode('MRHead')
slicer.modules.transforms.logic().CreateDisplacementVolumeFromTransform(transformNode, referenceVolumeNode, True)
</code></pre>
<p>My actual script looks like:</p>
<pre><code>button1 = qt.QPushButton("Load Segmentation")
self.formFrame1.layout().addWidget(button1)
button1.connect("clicked()", slicer.util.openAddSegmentationDialog)
button1.show()
</code></pre>
<p>Could you please assist me in this matter?<br>
Thank you in advance.</p>

---

## Post #11 by @pieper (2018-10-27 17:24 UTC)

<p>Yes, you’ll need to get the model node, maybe by using a node combo box.</p>
<p>Then you can add a linear transform, like the last block of code in this example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Add_a_texture_mapped_plane_to_the_scene_as_a_model</a></p>
<p>Except that you need to use the diag(-1,-1, 1,1).  Probably you want to do it manually with the GUI and then map that onto the script.</p>

---

## Post #12 by @Abdelkhalek (2018-10-27 20:28 UTC)

<p>Thank you Steve. I solved it finally <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
