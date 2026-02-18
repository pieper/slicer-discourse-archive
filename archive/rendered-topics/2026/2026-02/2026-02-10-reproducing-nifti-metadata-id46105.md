# Reproducing Nifti metadata

**Topic ID**: 46105
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/reproducing-nifti-metadata/46105

---

## Post #1 by @Yaroslav_Plutenko (2026-02-10 08:32 UTC)

<p>Greetings!</p>
<p>I have a question regarding Nifti format circulation. I’m developing a plugin that interacts with a remote repository and can upload/download images and whole datasets (viewing and fixing labels on the way if necessary). We prefer the Nifti format for images, since it’s widely used and accepted by many software viewers.<br>
The data is 3D scans of plants without strict reliance on orientation; only the resolution is important. Roughly speaking, I needed only numpy arrays, and I figured out how to bring them in and out of Slicer nodes, both source images and labels. So I used Nifti just as a container, and the required metadata is attached to datasets as a text/json file.<br>
But for the prospect, I think about how to preserve more metadata from the sources (scanner, other editors, automatic segmentation frameworks…). This metadata is stripped from the Nifty header and distributed to other locations during transformation to the Slicer node.<br>
Is there a way to gracefully collect it back when I want to re-export the node to Nifti?<br>
At least I figured out how to recollect the resolution from the spacing property, but it doesn’t exist for label nodes. Where to obtain it? There is a workaround to get the source image for the label and get spacing from the source image, but having a source node for the label node is not guaranteed and/or requires manual actions for the user.<br>
So there are two points in my question -</p>
<ul>
<li>One is specifically for the resolution of label nodes. How to collect it?</li>
<li>and other more general, if there is a way to re-collect more parameters for source and label images to recreate image/label metadata (provided no transformation was applied in-between)?</li>
</ul>

---

## Post #2 by @pieper (2026-02-10 14:10 UTC)

<p>The spacing and dimensions of the volumes are preserved when you load and save in nifti from slicer.  Can you describe what other metadata you are referring to and how it is stored in nifti?</p>
<p>Loading the labels as either a Slicer segmentation or labelmap volume will also preserve the spacing and dimensions so it’s not clear to me what specific issue you are having trouble with.</p>
<p>Perhaps you need some custom <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">python code</a> to track the data you are loading.</p>

---

## Post #3 by @Yaroslav_Plutenko (2026-02-10 15:18 UTC)

<p>Here is the Nifti header content. I guess it’s a Nifti1 format according to the reference</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://nipy.org/nibabel/nifti_images.html">
  <header class="source">

      <a href="https://nipy.org/nibabel/nifti_images.html" target="_blank" rel="noopener nofollow ugc">nipy.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://nipy.org/nibabel/nifti_images.html" target="_blank" rel="noopener nofollow ugc">Neuroimaging in Python — NiBabel 5.4.0.dev1+g3b1c7b37 documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">
sizeof_hdr      : 348
data_type       : b''
db_name         : b''
extents         : 0
session_error   : 0
regular         : b'r'
dim_info        : 0
dim             : [  3 360 360 390   0   0   0   0]
intent_p1       : 0.0
intent_p2       : 0.0
intent_p3       : 0.0
intent_code     : none
datatype        : int16
bitpix          : 16
slice_start     : 0
pixdim          : [1.  0.1 0.1 0.1 0.  0.  0.  0. ]
vox_offset      : 0.0
scl_slope       : nan
scl_inter       : nan
slice_end       : 0
slice_code      : unknown
xyzt_units      : 0
cal_max         : 0.0
cal_min         : 0.0
slice_duration  : 0.0
toffset         : 0.0
glmax           : 0
glmin           : 0
descrip         : b''
aux_file        : b''
qform_code      : scanner
sform_code      : unknown
quatern_b       : 0.0
quatern_c       : 0.0
quatern_d       : 1.0
qoffset_x       : 17.95
qoffset_y       : 17.95
qoffset_z       : -19.45
srow_x          : [0. 0. 0. 0.]
srow_y          : [0. 0. 0. 0.]
srow_z          : [0. 0. 0. 0.]
intent_name     : b''
magic           : b'n+1'

</code></pre>
<p>So far I use only <code>pixdim</code>, potentially <code>xyzt_units</code> and <code>datatype</code>, when unsure, but I want to preserve the maximum number of parameters to avoid inconsistency - I mean, sometimes I see warnings in the Slicer console regarding <code>sform/qform</code>, when I import Nifti images with rigged headers, but didn’t have time to investigate, I’m gonna address it later somehow.</p>
<p>In the code, I don’t see an example to extract spacing from the label node. Volume node has the function GetSpacing(), label node has not. Also in the code snippets, it is assumed that you have a reference (source) volume when you export label into labelMap. (I don’t know what spacing is assigned when you export without it using ExportAllSegmentsToLabelmapNode - perhaps default spacing 1.1.1.).</p>
<p>Anyway, these examples imply access to the image path, I thought about it already - for example, reading the niffi header and storing it somewhere in memory,  associated with the loaded node, to place it back during the export.  But I’d like to use the drag-n-drop feature, when the user just drops Nifti images into Slicer and they become nodes on the scene. And I can’t intercept the metadata after that.</p>

---

## Post #4 by @pieper (2026-02-10 16:30 UTC)

<p>If you really want to preserve all those fields then you can do that with some custom scripts.  You can give a custom file reader to override the default drag-and-drop behavior and track the data as you wish.</p>
<p>But you should probably check if any of your other code or tools really use any of that info.  Nifti is a complex format and many of those fields are disused and/or used differently by different custom use cases (e.g. for fMRI) but there’s a long history of different software using them inconsistently.  Even the qform/sform part, which it sounds like you don’t even need, has not being created consistently in these files, which is why you get the warnings.</p>
<p>Regarding your other questions, Slicer’s label maps do have a GetSpacing method and can be saved as nifti in a way that preserves the input spacing and dimensions.  Segmentations are more sophisticated and you can learn more about them to see if you need them (check the geometry options to decide what sampling grid you want to use, it’s all nicely documented so an LLM can guide you through it).</p>

---

## Post #5 by @Yaroslav_Plutenko (2026-02-12 08:05 UTC)

<p>Label map has the spacing, but Label node - doesn’t. When it’s alone in the scene without a reference source image, the spacing is gone. However, I realize that such cases would be uncommon, and at the end of the day, a label image will land in the dataset near a source image, so the resolution can be taken from somewhere anyway.</p>
<p>I’m also inclined towards custom import of images and tracking metadata in the plugin.  But I liked the option of dropping image(s) to Slicer,  and this way, I cannot control the import.  Or is it still possible with some hooks?  Anyway, I just realized that it’s also possible via custom UI elements in the plugin, which can handle drag-n-drop events according to the QT docs. Users will have to drop files there instead of the scene.</p>

---

## Post #6 by @pieper (2026-02-12 14:55 UTC)

<p>I’m not sure what you are referring to by a “Label node”.</p>
<p>In any case, yes, you can do just about anything you need with a script.  You can use Qt directly or you can provide a custom reader for your data.  Here’s an <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/NIfTIFile/NIfTIFile.py">example of a custom nifti reader</a>.  Custom FileReader and FileWriter classes are a kind of advanced topic that’s not very well documented, but could e an option for you.</p>

---

## Post #7 by @Yaroslav_Plutenko (2026-02-13 09:15 UTC)

<p>I meant the Segmentation node…</p>
<p>The Nifi files I can read/write with nibabel lib, I just need a path to them, then I separate the 3d array for the Slicer nodes and the header and will try to keep them tracked. Not sure what the custom reader is.  Also I’m confused by a multitude of Qt elements in UI editor, including Slicer-specific, and a lack of tutorials/documentation for them. But I guess it’s material for other topics on the forum, when I will start to struggle.</p>
<p>Thank you!</p>

---

## Post #8 by @lassoan (2026-02-14 05:09 UTC)

<p>You can avoid all the suffering by using nrrd format instead of nifti. Nifti is particularly bad for storing segmentations, as you cannot store any metadata in the files (except a very few hardcoded MRI-specific fields). In contrast, you can store segment names, colors, standard DICOM terminology in the nrrd segmentation file, even for overlapping segments - it is a fully self-contained file with all metadata that you need to create valid DICOM segmentation objects. The file format is very simple, mostly self-explaining, but you can see the official description <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html#segmentation-labelmap-file-format-seg-nrrd">here</a>. You can also use the <a href="https://pypi.org/project/slicerio/">slicerio</a> package in any Python environment to conveniently read/write segments and metadata.</p>

---

## Post #9 by @Yaroslav_Plutenko (2026-02-14 13:38 UTC)

<p>I will definitely consider other formats.<br>
It happened so that we build our workflow around nifty.<br>
Most of the software viewers/editors are familiar with Nifty, as well as plugins for viewing on web pages.<br>
Metatada was not crucial at first, and we also considered to use even numpy arrays in datasets, but it’s not suitable for exchange, since people need to drop files in some viewer and see what’s there, without scripting.<br>
I guess the conventions of the nnUnet framework, which I used the most for automatic segmentation,  impacted our decisions to adopt Nifti.<br>
I should have learned more about other formats, but we already passed some milestones in our workflows for on-the-fly changes.<br>
We consider adaptation and conversion to nrrd in the next iterations.</p>
<p>Thank you for the tips!</p>

---
