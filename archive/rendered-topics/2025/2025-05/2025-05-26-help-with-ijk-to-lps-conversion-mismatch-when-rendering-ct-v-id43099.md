---
topic_id: 43099
title: "Help With Ijk To Lps Conversion Mismatch When Rendering Ct V"
date: 2025-05-26
url: https://discourse.slicer.org/t/43099
---

# Help with IJK to LPS Conversion Mismatch When Rendering CT Volume Outside Slicer

**Topic ID**: 43099
**Date**: 2025-05-26
**URL**: https://discourse.slicer.org/t/help-with-ijk-to-lps-conversion-mismatch-when-rendering-ct-volume-outside-slicer/43099

---

## Post #1 by @Khaleel_Ur_Rehman (2025-05-26 05:16 UTC)

<p><strong>Hello Slicer Community,</strong></p>
<p>I’m currently working on a custom algorithm that requires rendering a CT volume in 3D using VTK (outside of Slicer). As part of this, I need to convert the CT image from IJK space to LPS (or RAS) physical space to accurately extract surfaces and analyze spatial positions of structures.</p>
<p>To test this pipeline, I’ve tried using different image readers:</p>
<ul>
<li><code>SimpleITK.ReadImage()</code></li>
<li><code>ITK</code> readers</li>
<li><code>vtkDICOMImageReader</code> / <code>vtkMetaImageReader</code></li>
</ul>
<p>In all cases, I convert the image data to <code>vtkImageData</code>, apply the spacing, origin, and direction matrix, and then run my 3D algorithm (e.g., Marching Cubes, surface filtering, etc.). However, <strong>the spatial positions I get are very far off</strong> from what I see in 3D Slicer, even after applying proper transforms (including direction and spacing). I verified this by comparing coordinates of fiducials or surface centers manually with Slicer’s RAS values.</p>
<p>I am aware that:</p>
<ul>
<li>3D Slicer uses <strong>RAS</strong> orientation (as opposed to LPS).</li>
<li>To convert from LPS to RAS, we typically negate the <strong>first two axes (X and Y)</strong>.</li>
</ul>
<p>However, even accounting for this transformation, the coordinates from my processed VTK pipeline don’t align with Slicer’s scene — they are off by <strong>tens of millimeters</strong> or more.</p>
<hr>
<h3><a name="p-125455-what-im-trying-to-achieve-1" class="anchor" href="#p-125455-what-im-trying-to-achieve-1" aria-label="Heading link"></a><strong>What I’m trying to achieve:</strong></h3>
<ul>
<li>Render the CT in 3D and perform surface-based operations <strong>while keeping spatial coordinates consistent with Slicer</strong>.</li>
<li>Ensure that any sphere or point I place in VTK matches exactly with what I see in Slicer (e.g., using Markups).</li>
</ul>
<hr>
<h3><a name="p-125455-questions-2" class="anchor" href="#p-125455-questions-2" aria-label="Heading link"></a><strong>Questions:</strong></h3>
<ol>
<li><strong>Is there a reliable way to convert a CT volume (e.g., <code>.mha</code>, <code>.nrrd</code>, DICOM) into <code>vtkImageData</code></strong> while <strong>preserving the full IJK → LPS → RAS transform</strong>, exactly as Slicer does internally?</li>
<li><strong>Can I use 3D Slicer itself to read and process the volume</strong>, then export it (or a <code>vtkMRMLVolumeNode</code>) into a <code>vtkImageData</code> with all spatial orientation handled correctly?</li>
<li><strong>Is there an example of how Slicer computes world coordinates</strong> from IJK for a volume? I’d like to replicate that logic in my standalone pipeline.</li>
<li>Is there a preferred method to <strong>export a loaded volume from Slicer into <code>.vti</code> or <code>.vtk</code></strong> with all spatial metadata preserved, so that external VTK pipelines will behave identically?</li>
</ol>
<hr>
<h3><a name="p-125455-what-ive-tried-so-far-3" class="anchor" href="#p-125455-what-ive-tried-so-far-3" aria-label="Heading link"></a><strong>What I’ve Tried So Far:</strong></h3>
<ul>
<li>Extracted <code>direction</code>, <code>origin</code>, <code>spacing</code> from SimpleITK and constructed a <code>vtkTransform</code> to apply to surface meshes.</li>
<li>Tried negating X and Y axes to convert LPS to RAS.</li>
<li>Validated center of mass / bounding box coordinates of extracted surfaces against Slicer Markups — and found major mismatches.</li>
</ul>
<hr>
<p>Any suggestions, best practices, or example scripts would be highly appreciated. I’m happy to share code snippets or sample data if needed.</p>
<p>Thanks in advance!</p>
<p><strong>Best regards,</strong><br>
<em>Khaleel Ur Rehman</em></p>

---

## Post #2 by @pieper (2025-05-26 19:06 UTC)

<p>I don’t think there’s any magic that we can suggest other than carefully tracking your assumptions through the entire pipeline of operations.  You should be aware that historically VTK hasn’t supported oriented images or the concepts of LPS/RAS, and so it’s possible for some data to be lost depending on the filters you use.  Although we are careful in Slicer to flag our assumptions about RAS and LPS when reading and writing files, not all software respects these conventions.  Of course you can read the Slicer source code to see how things are managed.</p>
<p>An advantage of building your analysis pipelines within Slicer’s environment is that so much of this work has already been done for you and you can avoid reinventing code that’s already freely available and debugged.</p>

---

## Post #3 by @lassoan (2025-05-26 19:54 UTC)

<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="43099">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p>apply the spacing, origin, and direction matrix, and then run my 3D algorithm (e.g., Marching Cubes, surface filtering, etc.).</p>
</blockquote>
</aside>
<p>It is possible that not all VTK filters take into account the image direction matrix.</p>
<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="43099">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p><strong>Is there a reliable way to convert a CT volume (e.g., <code>.mha</code>, <code>.nrrd</code>, DICOM) into <code>vtkImageData</code></strong> while <strong>preserving the full IJK → LPS → RAS transform</strong>, exactly as Slicer does internally?</p>
</blockquote>
</aside>
<p>Yes. ITK readers provide IJK to LPS mapping, while Slicer volume storage nodes provide the IJK to RAS mapping for most cases. If the volume’s axes are not orthogonal or spacing between slices are varying, or slices are not all parallel then probably the easiest is to reconstruct the volume into a regular grid using Slicer.</p>
<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="43099">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p><strong>Can I use 3D Slicer itself to read and process the volume</strong>, then export it (or a <code>vtkMRMLVolumeNode</code>) into a <code>vtkImageData</code> with all spatial orientation handled correctly?</p>
</blockquote>
</aside>
<p>Sure, you can load the volume, then export it to a NRRD file. If you use <code>slicer.util.exportNode</code> instead of <code>slicer.util.saveNode</code> then you have the convenient option of saving in the <code>world</code> coordinate system, i.e., harden any acquisition transforms (to handle varying slice spacing, non-parallel slices, etc.).</p>
<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="43099">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p><strong>Is there an example of how Slicer computes world coordinates</strong> from IJK for a volume? I’d like to replicate that logic in my standalone pipeline.</p>
</blockquote>
</aside>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-markup-control-point-ras-coordinates-from-volume-voxel-coordinates">example in the script repository</a>.</p>
<p>Why do you want to replicate Slicer’s logic? Have you considered using Slicer instead?</p>
<aside class="quote no-group" data-username="Khaleel_Ur_Rehman" data-post="1" data-topic="43099">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/khaleel_ur_rehman/48/79947_2.png" class="avatar"> Khaleel_Ur_Rehman:</div>
<blockquote>
<p>Is there a preferred method to <strong>export a loaded volume from Slicer into <code>.vti</code> or <code>.vtk</code></strong> with all spatial metadata preserved, so that external VTK pipelines will behave identically?</p>
</blockquote>
</aside>
<p>I don’t think the old <code>.vtk</code> format can store image directions. The XML-based <code>.vtk</code> file format could, but it is a complex file format that only VTK-based applications can read/write, so I would not recommend its use. Instead, you can use <code>.nrrd</code> format.</p>

---
