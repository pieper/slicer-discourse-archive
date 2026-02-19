---
topic_id: 10624
title: "Mrb File Format Structure And Naming"
date: 2020-03-10
url: https://discourse.slicer.org/t/10624
---

# MRB File Format - Structure and Naming

**Topic ID**: 10624
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/mrb-file-format-structure-and-naming/10624

---

## Post #1 by @ArneGroskurth (2020-03-10 20:08 UTC)

<p>Hi there,</p>
<p>is there any documentation for the *.mrb file format?</p>
<p>I would like to implement an interface to this format for another application but would ideally not have to reverse-engineer the format.</p>
<p>And if there is no such documentation:</p>
<ul>
<li>Is the mrb-fiel always a zip-archive?</li>
<li>How is the general structure and naming within the archive?</li>
<li>Is there always a directory called “input” in the root of the archive and nothing else? (And why is that so?)</li>
<li>How is the naming within the “Data” directory?</li>
</ul>
<p>I am primarily interested in extracting segmentations from the file.</p>
<p>Thank you very much,<br>
Arne</p>

---

## Post #2 by @pieper (2020-03-10 20:30 UTC)

<p>Hi Arne -</p>
<p>First the standard disclaimer: mrb files are meant to be a application-specific format not an interchange format, so they are subject to change without notice as Slicer’s implementation changes.  You have been warned <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_winking_eye.png?v=9" title=":stuck_out_tongue_winking_eye:" class="emoji" alt=":stuck_out_tongue_winking_eye:"></p>
<p>For interchange we suggest using DICOM, particularly SEG objects if you are interested in segmentation (see <a href="https://dicom4qi.readthedocs.io/en/latest/results/seg/3dslicer/">dicom4qi</a> for example).</p>
<p>That said, certain things are likely to persist.  Basically yes, .mrb is likely to always be a .zip file containing a top level mrml scene file.  All of the storable nodes are redirected into the Data directory and the result is zipped up.  Everything else about it is basically an implementation detail byproduct of <a href="https://github.com/Slicer/Slicer/blob/b849223cb547bab4dbca641185c83a2fa2b8b3be/Libs/MRML/Logic/vtkMRMLApplicationLogic.cxx#L627">this code</a>.</p>
<p>If you are determined to parse the structure it should be pretty easy to do - just read the mrml xml and all the names, datatypes, filenames, etc will be there.  It’s essentially just a serialization of the application state.</p>

---

## Post #3 by @ArneGroskurth (2020-03-10 21:19 UTC)

<p>Thanks for the quick response!</p>
<p>Using DICOM SEG objects would be fine. How can I export them from slicer?</p>
<p>Thank you very much!</p>

---

## Post #4 by @pieper (2020-03-10 21:43 UTC)

<p><a href="https://qiicr.gitbooks.io/quantitativereporting-guide/" class="onebox" target="_blank">https://qiicr.gitbooks.io/quantitativereporting-guide/</a></p>
<p>Good luck with your research - let us know how it goes!</p>

---

## Post #5 by @ArneGroskurth (2020-03-24 10:36 UTC)

<p>Unfortunately, the plugin is not ideal for the workflow in our lab. So I do have some more questions regarding the mrb format - or perhaps, slicer in general.</p>
<ul>
<li><strong>What is the data-model for segmentations?</strong></li>
<li>As documented <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" rel="nofollow noopener">here</a>, I understand that one <em>segmentation</em> consists of multiple <em>segments</em>. But what is a <em>segmentation</em>/<br>
<em>segment</em> then really? Intuitively, I would expect just multiple <em>segmentations</em> being associated with an image, each being defined by a single mask with the same shape as the image volume.</li>
<li>Why are there both Segmentation- and LabelMapVolume-Nodes within the mrml-document? Aren’t label-maps just a different representation for a set of multiple segmentations? Or in what way are they distinct from one another?</li>
</ul>
<p>(Some questions might arise from my lack of usage-experience with slicer.)</p>
<p>Thank you very much!</p>

---

## Post #6 by @lassoan (2020-03-24 12:08 UTC)

<aside class="quote no-group" data-username="ArneGroskurth" data-post="5" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>Unfortunately, the plugin is not ideal for the workflow</p>
</blockquote>
</aside>
<p>Could you write about your workflow? It would help in understanding what you would like to do and what would be the best potential solutions.</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="5" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>what is a <em>segmentation</em></p>
</blockquote>
</aside>
<p>Segmentation defines multiple, potentially overlapping regions. Internally, it can use various representations (binary labelmap, closed surface, fractional labelmap, set of parallel contours, ribbons, etc.) and keep them all in sync. See an overview of how it is related to other nodes <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">here</a>.</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="5" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>Why are there both Segmentation- and LabelMapVolume-Nodes within the mrml-document?</p>
</blockquote>
</aside>
<p>Normally you only have segmentation in the scene because segmentation can do everything that a labelmap, but much more (it can store overlapping segments, can be displayed directly in 3D, can be edited in Segment Editor, etc.). If some external software creates a labelmap volume then you can load it directly as segmentation.</p>

---

## Post #7 by @ArneGroskurth (2020-03-24 16:28 UTC)

<p>Thank you for the background!</p>
<p>Together with the input from a colleague I conclude the following:</p>
<ul>
<li>What I intuitively named a <em>segmentation</em> is a <em>segment</em> is slicer-terms</li>
<li>A <em>segmentation</em> in slicer terms is just a set of multiple <em>segments</em> and every <em>segment</em> has to be part of a <em>segmentation</em>. (Presumably, <em>segmentations</em> have been introduced to slicer to help organize a large number of <em>segments</em>)</li>
<li>A mrb record can have an arbitrary number of <em>segmentations</em>, each containing an arbitrary number of <em>segments</em>.</li>
<li>A <em>label-map</em> can be actively derived from a set of <em>segmentations</em> (or <em>segments</em>?) and saved within the slicer data-model.</li>
<li>As label-maps are derived from segmentations (in some point in time of their edit-history), they are potentially outdated w.r.t. the segmentations</li>
</ul>
<p>Is that about right?</p>
<p>(Side-Note: Having all this information about the data-model as e.g. an UML-diagram would be really helpful)</p>
<p>About our workflow: We currently need to re-visit and slightly correct the segmentations within a large number of scans (thousands). Just loading and saving those segmentations into/from slicer using the plugin takes just too long as the number of required steps/clicks is quite high.</p>

---

## Post #8 by @pieper (2020-03-24 17:36 UTC)

<aside class="quote no-group" data-username="ArneGroskurth" data-post="7" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>A <em>label-map</em> can be actively derived from a set of <em>segmentations</em> (or <em>segments</em> ?) and saved within the slicer data-model.</p>
</blockquote>
</aside>
<p>A labelmap is a lossy representation of a segmentation (no overlap information).</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="7" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>As label-maps are derived from segmentations (in some point in time of their edit-history), they are potentially outdated w.r.t. the segmentations</p>
</blockquote>
</aside>
<p>Labelmaps or other data can also be imported back into segmentations.  So which one is up to date depends on what modules you need to use to process data.</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="7" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>(Side-Note: Having all this information about the data-model as e.g. an UML-diagram would be really helpful)</p>
</blockquote>
</aside>
<p>Yes please do! (haha)</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="7" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>About our workflow: We currently need to re-visit and slightly correct the segmentations within a large number of scans (thousands). Just loading and saving those segmentations into/from slicer using the plugin takes just too long as the number of required steps/clicks is quite high.</p>
</blockquote>
</aside>
<p>Sounds like a good opportunity to make a custom scripted module to simplify things.</p>

---

## Post #9 by @lassoan (2020-03-24 20:11 UTC)

<aside class="quote no-group" data-username="ArneGroskurth" data-post="7" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>About our workflow: We currently need to re-visit and slightly correct the segmentations within a large number of scans (thousands). Just loading and saving those segmentations into/from slicer using the plugin takes just too long as the number of required steps/clicks is quite high.</p>
</blockquote>
</aside>
<p><a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a> was developed for exactly this. You can probably use it as is, but since it is a Python scripted module you can also easily customize and/or extend it to do exactly what you need.</p>

---

## Post #10 by @ArneGroskurth (2020-03-26 18:05 UTC)

<p>That extensions seems promising but when I try to install the extension via the slicer extension manager I just get these error messages:</p>
<p>“Retrieving extension metadata [ extensionId: 293501]”<br>
“{6835d4d9-c3bb-4f34-8d9e-615305101b29}: 5: Operation canceled”</p>

---

## Post #11 by @lassoan (2020-03-26 19:00 UTC)

<p>The extension manager website can be overwhelmed with requests sometimes. If you have trouble installing an extension then click on Install button again, until download and installation succeeds. We plan to migrate to a new server backend soon, which should not have these inconveniences anymore.</p>

---

## Post #12 by @ArneGroskurth (2020-03-26 19:42 UTC)

<p>Okay I will try that - thanks!</p>
<p>One more question: What is the <em>extent</em> being associated with a <em>segment</em>? It gets written into the nrrd header for each segment and is a space-separated list for six integer numbers. (E.g.: <code>Segment5_Extent: '23 333 14 237 0 0'</code>)</p>

---

## Post #13 by @lassoan (2020-03-26 19:49 UTC)

<p><em>SegmentN_Extent</em> defines where within the volume the segment has non-zero voxels according usual VTK extent conventions (xmin, xmax, ymin, ymax, zmin, zmax). It is a hint used for optimizing segmentation reading performance.</p>

---

## Post #14 by @ArneGroskurth (2020-03-28 01:31 UTC)

<p>Great!</p>
<p>I hope, this will be the last (for now…):</p>
<p>What is the relationship between all of these values?:</p>
<ul>
<li>“space origin” and “space directions” from image volume nrrd header</li>
<li>“space origin”, “space directions” and “Segmentation_ReferenceImageExtentOffset” from segmentation volume nrrd header</li>
<li>the attributes “dimensions”, “xyzOrigin”, “uvwExtents”, “uvwDimensions”, “uvwOrigin” and “sliceToRAS” of a  node within the mrml file</li>
<li>voxel coordinates within the image- and segmentation-volumes</li>
</ul>
<p>I assume, most of those values can be derived from basic information about the image volume and a segmentation volume but I struggle to get the complete picture of that.</p>
<p>Thank you very much for your input!</p>

---

## Post #15 by @lassoan (2020-03-28 01:43 UTC)

<aside class="quote no-group" data-username="ArneGroskurth" data-post="14" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<ul>
<li>“space origin” and “space directions” from image volume nrrd header</li>
<li>“space origin”, “space directions” and “Segmentation_ReferenceImageExtentOffset” from segmentation volume nrrd header</li>
</ul>
</blockquote>
</aside>
<p>These are all standard nrrd fields that describe image geometry, except Segmentation_ReferenceImageExtentOffset (which is added to allow extent to start at any voxel position; this is needed, since VTK allows non-zero extent start values, but nrrd format always assumes extents start from 0).</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="14" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>the attributes “dimensions”, “xyzOrigin”, “uvwExtents”, “uvwDimensions”, “uvwOrigin” and “sliceToRAS” of a node within the mrml file</p>
</blockquote>
</aside>
<p>These are slice view properties, define the size and origin of slice display (XYZ) and texture image (UVW) coordinate systems.</p>
<aside class="quote no-group" data-username="ArneGroskurth" data-post="14" data-topic="10624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/0ea827/48.png" class="avatar"> ArneGroskurth:</div>
<blockquote>
<p>voxel coordinates within the image- and segmentation-volumes</p>
</blockquote>
</aside>
<p>IJK to RAS (or IJK to LPS) transform specifies mapping between voxel and physical coordinate system. You can compute these transforms from origin, spacing, and axis directions (e.g., defined by space origin, space directions values in a NRRD file).</p>

---

## Post #16 by @ArneGroskurth (2020-04-07 16:03 UTC)

<p>I’ve still another question <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:">:</p>
<p>When trying to read the image-volume nrrd and overlay it with a segmentation volume nrrd, I’m currently getting a slight mismatch of 22 voxels in the anterior-posterior axis. My assumption was, that I must only care about the <em>Segmentation_ReferenceImageExtentOffset</em> nrrd header field within the segmentation volume to rebuild the <em>full</em> segmentation volume - is that correct?</p>
<p>My python code for that looks roughly like this:</p>
<pre><code># read 3D image volume
image_nrrd_data, image_nrrd_header = nrrd.read(...)

# Read 4D segmentation mask
segmentations_nrrd_data, segmentations_nrrd_header = nrrd.read(...)

# Read segmentation volume offset w.r.t. image volume origin
offset = [
    int(s)
    for s in segmentations_nrrd_data["Segmentation_ReferenceImageExtentOffset"].split()
]

# iterate over all segments
for segment_index in range(...):

    segment_mask = segmentations_nrrd_data[segment_index]

    # Build 3D mask with full size
    mask = np.zeros(image_nrrd_data.shape, dtype=np.bool)
    mask[
        offset[0] : offset[0] + segment_mask.shape[0],
        offset[1] : offset[1] + segment_mask.shape[1],
        offset[2] : offset[2] + segment_mask.shape[2],
    ] = segment_mask

    # save mask for that segment...
</code></pre>
<p>Note, that I’m not taking into consideration information from the nrrd headers <em>SegmentX_Extent</em>, <em>space_direction</em> or <em>space origin</em>.</p>

---

## Post #17 by @ArneGroskurth (2020-04-07 17:11 UTC)

<p>Edit: Nevermind - I find a bug in the surrounding code. Thank you for all the input!</p>

---
