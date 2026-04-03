---
topic_id: 46636
title: "Multi Class Segmentation With Ct Aligned Stl Dental Dataset"
date: 2026-04-02
url: https://discourse.slicer.org/t/46636
---

# Multi-Class Segmentation with CT + Aligned STL (Dental Dataset)

**Topic ID**: 46636
**Date**: 2026-04-02
**URL**: https://discourse.slicer.org/t/multi-class-segmentation-with-ct-aligned-stl-dental-dataset/46636

---

## Post #1 by @abhijeet2410 (2026-04-02 06:37 UTC)

<p>Operating system: Window<br>
Slicer version: 3 D Slicer 5. 10.0</p>
<hr>
<h2><a name="p-132962-question-multi-class-segmentation-with-ct-aligned-stl-dental-dataset-1" class="anchor" href="#p-132962-question-multi-class-segmentation-with-ct-aligned-stl-dental-dataset-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/brain.png?v=15" title=":brain:" class="emoji" alt=":brain:" loading="lazy" width="20" height="20"> Question: Multi-Class Segmentation with CT + Aligned STL (Dental Dataset)</h2>
<p>I am working on a <strong>dental AI dataset pipeline</strong> where I have:</p>
<ul>
<li>
<p><strong>CT scan (DICOM volume)</strong></p>
</li>
<li>
<p><strong>Aligned STL models</strong> (upper jaw, lower jaw, bite scans)</p>
</li>
</ul>
<p>I am able to visualize everything correctly using VTK:</p>
<pre><code class="lang-auto">import vtk

def load_stl(path, color):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(path)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(color)

    return actor

renderer = vtk.vtkRenderer()

upper = load_stl("UpperJawScan.stl", (1,1,1))
lower = load_stl("LowerJawScan.stl", (0.9,0.9,0.9))

renderer.AddActor(upper)
renderer.AddActor(lower)

</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/516d457327ffed3a21e00d009430ab5b2fd30580.png" alt="image" data-base62-sha1="bCkMQ9KDL7eMzt7iNLYC4SetIzu" width="239" height="35"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a512656a8fbb43644285524c7721bb2b3ed3482.png" alt="image" data-base62-sha1="fawtpH2J3qnGQhIVGtwqm28kbSy" width="199" height="39"></p>
<p>So currently:</p>
<ul>
<li>
<p>CT volume and STL teeth are <strong>spatially aligned</strong></p>
</li>
<li>
<p>STL provides <strong>clear tooth geometry</strong></p>
</li>
<li>
<p>CT provides <strong>voxel grid (needed for training)</strong></p>
</li>
</ul>
<hr>
<h2><a name="p-132962-goal-i-want-to-create-a-multi-class-segmentation-dataset-such-as-2" class="anchor" href="#p-132962-goal-i-want-to-create-a-multi-class-segmentation-dataset-such-as-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/bullseye.png?v=15" title=":bullseye:" class="emoji" alt=":bullseye:" loading="lazy" width="20" height="20"> Goal : I want to create a <strong>multi-class segmentation dataset</strong> such as:</h2>
<div class="md-table">
<table>
<thead>
<tr>
<th>Class ID</th>
<th>Structure</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>Background</td>
</tr>
<tr>
<td>1</td>
<td>Teeth</td>
</tr>
<tr>
<td>2</td>
<td>Gum</td>
</tr>
<tr>
<td>3</td>
<td>Impacted Teeth</td>
</tr>
</tbody>
</table>
</div><hr>
<h2><a name="p-132962-problem-3" class="anchor" href="#p-132962-problem-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/red_question_mark.png?v=15" title=":red_question_mark:" class="emoji" alt=":red_question_mark:" loading="lazy" width="20" height="20"> Problem</h2>
<ul>
<li>
<p>Teeth are <strong>not clearly visible in CT slices</strong>, but are <strong>very clear in STL</strong></p>
</li>
<li>
<p>STL is <strong>surface mesh</strong>, not voxel labels</p>
</li>
<li>
<p>Exporting via <code>vtkOBJExporter</code> only gives geometry, not labels</p>
</li>
</ul>
<hr>
<h2><a name="p-132962-core-question-4" class="anchor" href="#p-132962-core-question-4" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/red_question_mark.png?v=15" title=":red_question_mark:" class="emoji" alt=":red_question_mark:" loading="lazy" width="20" height="20"> Core Question</h2>
<p><strong>How can I generate a voxel-wise multi-class segmentation mask from aligned STL + CT data using tools like 3D Slicer or ITK-SNAP?</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd3deab46d2976934e65f20a854e8abae6d388d9.jpeg" data-download-href="/uploads/short-url/thExkyXhyQWo6VXP0JuthsUD5y1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd3deab46d2976934e65f20a854e8abae6d388d9_2_685x499.jpeg" alt="image" data-base62-sha1="thExkyXhyQWo6VXP0JuthsUD5y1" width="685" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd3deab46d2976934e65f20a854e8abae6d388d9_2_685x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd3deab46d2976934e65f20a854e8abae6d388d9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd3deab46d2976934e65f20a854e8abae6d388d9.jpeg 2x" data-dominant-color="1E1E1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">834×608 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>  This is <strong>aligned STL + CT data. How to annotate it  using 3D slicer ?   White part show STL and transparent part show the CT</strong></p>
<hr>
<h2><a name="p-132962-constraints-5" class="anchor" href="#p-132962-constraints-5" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> Constraints</h2>
<ul>
<li>
<p>Dataset is for <strong>deep learning (3D segmentation / PointNet / UNet)</strong></p>
</li>
<li>
<p>Prefer <strong>semi-automatic or automated pipeline</strong></p>
</li>
</ul>
<hr>
<h2><a name="p-132962-what-ive-tried-6" class="anchor" href="#p-132962-what-ive-tried-6" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/light_bulb.png?v=15" title=":light_bulb:" class="emoji" alt=":light_bulb:" loading="lazy" width="20" height="20"> What I’ve Tried</h2>
<ul>
<li>
<p>Rendering CT + STL together → works</p>
</li>
<li>
<p>Exporting meshes → no label info</p>
</li>
<li>
<p>Manual annotation → difficult because CT does not clearly show teeth</p>
</li>
</ul>

---
