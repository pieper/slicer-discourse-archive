# Export Segmentation as Labeled LabelMap

**Topic ID**: 26468
**Date**: 2022-11-27
**URL**: https://discourse.slicer.org/t/export-segmentation-as-labeled-labelmap/26468

---

## Post #1 by @apparrilla (2022-11-27 23:08 UTC)

<p>Hi everyone!<br>
I´m trying to export a segmentation with some segments labed as:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461.png" data-download-href="/uploads/short-url/3h0VaNRThqq9bZXG6rTVJKjw5tn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461_2_325x375.png" alt="image" data-base62-sha1="3h0VaNRThqq9bZXG6rTVJKjw5tn" width="325" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461_2_325x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461_2_487x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16f2e73b79540b3572ee5eb5fe0ce693be447461.png 2x" data-dominant-color="252625"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×741 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And I exported:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403.png" data-download-href="/uploads/short-url/h3ZXjOSISYuxPirRxW5yCiknf8f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403_2_345x213.png" alt="image" data-base62-sha1="h3ZXjOSISYuxPirRxW5yCiknf8f" width="345" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403_2_345x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403_2_517x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7798b0c17eaf85e5c9dc13e9968bd12bbb3ea403_2_690x426.png 2x" data-dominant-color="3E3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">856×529 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I close scene and try to import again this file as a segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2.png" data-download-href="/uploads/short-url/2GmR8IK1xWx3bPiv0xZ9AH2bo5Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2_2_420x375.png" alt="image" data-base62-sha1="2GmR8IK1xWx3bPiv0xZ9AH2bo5Q" width="420" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2_2_420x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2_2_630x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12ce6cb1c81f5e50350419ab89ea253fdc5a28b2.png 2x" data-dominant-color="282827"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">827×738 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Original label is not preserved…</p>
<p>I have some other NonSlicerMade labelmaps and if I import them:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c1eabb770d4364d22b81b6f75e2b08c003ab4dd.png" data-download-href="/uploads/short-url/hI0UVnuSYztvnMiDVD0JSdyBk4Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c1eabb770d4364d22b81b6f75e2b08c003ab4dd.png" alt="image" data-base62-sha1="hI0UVnuSYztvnMiDVD0JSdyBk4Z" width="517" height="216" data-dominant-color="272726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">806×338 4.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I undertand that:</p>
<ul>
<li>Slicer always add string “Segment_” to labelmap labels</li>
<li>Slicer save labelmaps always without original label (just as a ColorTable second file)</li>
</ul>
<p>Is there any way to change this behaviour, or just the second issue?<br>
Thanks on advance.</p>
<p>Slicer Stable 5.0.3 r30893</p>

---

## Post #2 by @lassoan (2022-11-28 14:39 UTC)

<p>Slice allows round-trip editing and exporting and importing with preserving all the segment names.</p>
<p>I would recommend to save the segmentation file as usual, in a seg.nrrd file, because it contains a regular 3D labelmap that any software can read (if you have overlapping segments, then it will be a 4D volume containing a few non-overlapping 3D volumes) and the segment names, in a single file.  You can edit these files and the segment names are preserved, just make sure all the custom fields in the .nrrd file header are preserved.</p>
<p>If you want to save the segment names in a separate file (because the file you use for segment editing cannot preserve custom fields in the nrrd file header) then you can export the segmentation into a labelmap and save the resulting color table file. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">use this color table file to specify segment names when you load a labemap volume</a>.</p>

---

## Post #3 by @Dolzodmaa_D (2022-11-28 17:41 UTC)

<p>Is there a way to output those label maps as colored masks? By default, Slicer3D outputs them all as binary masks.</p>

---

## Post #4 by @apparrilla (2022-11-28 20:42 UTC)

<p>I agree with you <a class="mention" href="/u/lassoan">@lassoan</a> but I´m working on a dataset to train Monai so I need the labelmap in nii format to work with. That is the reason fot not to work directly with segmentations (much better for almost everthing…).<br>
I´m trying to mix my own cases with others form VerSe Dataset and I need to export as nii.gz labelmaps but it´s been impossible to me to get labelmaps with segments with the right label…</p>
<p>Thanks in advance !!!</p>

---

## Post #5 by @muratmaga (2022-11-28 22:18 UTC)

<p>Labelmaps are not meant to preserve segmentation labels, just the indices. You need to create a color table, and when converting the labelmap to segmentation you need to apply this: this section might be useful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/MEMOS.py#L568-L579">
  <header class="source">

      <a href="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/MEMOS.py#L568-L579" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/MEMOS.py#L568-L579" target="_blank" rel="noopener nofollow ugc">SlicerMorph/MEMOS/blob/main/MEMOS/MEMOS.py#L568-L579</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="568" style="counter-reset: li-counter 567 ;">
          <li>labelNode = slicer.util.loadLabelVolume(outputLabelPath)</li>
          <li>labelNode.GetDisplayNode().SetAndObserveColorNodeID(colorNode.GetID())</li>
          <li>#if originalSpacing != (1,1,1):</li>
          <li>  #labelNode.SetSpacing(originalSpacing)</li>
          <li>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")</li>
          <li>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelNode, segmentationNode)</li>
          <li>slicer.util.saveNode(segmentationNode, outputSegPath)</li>
          <li>slicer.mrmlScene.RemoveNode(labelNode)</li>
          <li>slicer.mrmlScene.RemoveNode(segmentationNode)</li>
          <li>os.remove(outputLabelPath)</li>
          <li>end = time.time()</li>
          <li>print("MEMOS Inference time: ", end - start)    </li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>the associate color table looks like this: First column is the label index, second column is the segment label to be applied, followed by the RGB code (and alpha).</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl">
  <header class="source">

      <a href="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl" target="_blank" rel="noopener nofollow ugc">SlicerMorph/MEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl</a></h4>


      <pre><code class="lang-ctbl">0 background 0 0 0 255
1 left_lung 197 165 145 255
2 cranial_lobe 128 174 128 255
3 middle_lobe 241 214 145 255
4 caudal_lobe 177 122 101 255
5 accessory_lobe 111 184 210 255
6 left_kidney 185 102 83 255
7 right_kidney 185 102 83 255
8 stomach_wall 216 101 79 255
9 stomach_lumen 221 130 101 255
10 medial_lobe_of_liver 144 238 144 255
11 left_lobe_of_liver 192 104 88 255
12 right_lobe_of_liver 220 245 20 255
13 caudate_lobe_of_liver 78 63 0 255
14 left_adrenal 255 250 220 255
15 right_adrenal 230 220 70 255
16 rectum 200 200 235 255
17 bladder 250 250 210 255
18 left_ventricle 244 214 49 255
19 right_ventricle 0 151 206 255
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/MEMOS/blob/main/MEMOS/Resources/Support/KOMP2.ctbl" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @apparrilla (2022-11-28 23:43 UTC)

<p>I think i´m not explain properly…<br>
I want to make labelmaps as they are in VerSe Dataset but my labelmaps exported with Slicer are not the same. Verse ones have labels inside because i you import them in Slicer and you send them to an empty Segmentation, segments are correctly labeled (first vertebra is “8” because it is T1, not “1” because it´s the first indice).<br>
I need to add my cases to VerSe Dataset to retrain a Monai Pipeline with them.<br>
It´s strange that Segmentation Module ask you for a ColorTable during export task and labels are not added to the labelmap and output labelmap have no color as <a class="mention" href="/u/dolzodmaa_d">@Dolzodmaa_D</a> said.</p>
<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> for your explain about labelmap import task into a Segmentation.</p>

---

## Post #7 by @muratmaga (2022-11-29 01:09 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="6" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>It´s strange that Segmentation Module ask you for a ColorTable during export task and labels are not added to the labelmap and output labelmap have no color as <a class="mention" href="/u/dolzodmaa_d">@Dolzodmaa_D</a> said.</p>
</blockquote>
</aside>
<p>Because labelmap format does not have a field to store actual labels, only indices. The labels are preserved in the color table that was saved during the export.</p>
<p>See this thread on how to correctly load the labelmap as a segmentation using the color table from the UI. <a href="https://discourse.slicer.org/t/copying-segment-names-colors-from-one-segmentation-to-another/21204/7" class="inline-onebox">Copying segment names/colors from one segmentation to another - #7 by lassoan</a></p>
<p>The example I sent you is the programmatic approach to the same thing.</p>
<aside class="quote no-group" data-username="apparrilla" data-post="6" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I need to add my cases to VerSe Dataset to retrain a Monai Pipeline with them.</p>
</blockquote>
</aside>
<p>This may or may not be relevant for you, but we encountered an issue when using a labelmaps with non-contiguous numbers, and not starting from 1. We were training a multilabel model, and the source we used had for training had labelmaps that go from 1-50 (with couple gaps) and then 101-103. Monai didn’t like that so we ended having to reorder the labels in a continuous fashion from 1-50. So if your first label has an index of 8, you may or may not encounter the same issue. FYI.</p>

---

## Post #8 by @lassoan (2022-11-29 03:01 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="4" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Monai so I need the labelmap in nii format to work with.</p>
</blockquote>
</aside>
<p>Many MONAI examples use NIFTI format, but you should be able to use NRRD file format just as well. If you have trouble with that then you can post it as a question and <span class="mention">@mention</span> some MONAILabel people.</p>
<aside class="quote no-group" data-username="apparrilla" data-post="4" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I´m trying to mix my own cases with others form VerSe Dataset and I need to export as nii.gz labelmaps but it´s been impossible to me to get labelmaps with segments with the right label…</p>
</blockquote>
</aside>
<p>If some of the data is already in NIFTI format then it may be indeed simpler to add more data to it in the same format.</p>
<p>To make things easier for you, I’ve created a color table for the Verse data set. You can download it from <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/VerseLabels.txt">here</a>. Simply load this color table then select it when you load a labelmap volume or export a segmentation.</p>

---

## Post #9 by @apparrilla (2022-11-30 00:12 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a> for your kind explanations and the Verse ColorTable.<br>
It’s a pity you can’t export slicers segmentations as NIFTI as other software do it because split labels and color in a diferent file is a bit tricky for sharing masks with other users in multilabel AI pipelines.</p>

---

## Post #10 by @lassoan (2022-11-30 00:30 UTC)

<p>You can save segmentation in NIFTI file format, exactly for interoperability with other software. The color table ensures consistent label values &lt;-&gt; segment names mapping when importing or exporting NIFTI files.</p>

---

## Post #11 by @muratmaga (2022-11-30 00:34 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="9" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>It’s a pity you can’t export slicers segmentations as NIFTI</p>
</blockquote>
</aside>
<p>Do you know of a software that actually embeds segments names into NIFTI? Because I don’t think it is possible with that format. I never encountered one.</p>

---

## Post #12 by @apparrilla (2022-11-30 23:24 UTC)

<p>I find the way to do it in Segmentations Module but it works the same as export to labelmap and save it as nifti. Thanks</p>

---

## Post #13 by @apparrilla (2022-11-30 23:37 UTC)

<p>I´ve been looking for a software to review NIFTI files metadata but I can´t find it. I don´t know what software were used to made VerSe masks and review documentation about.<br>
I think I was in a mistake about labels in labelmaps file. Probably these VerSe masks don´t have labels but they are saved with “altered indexes”. I mean that first segment is not index 1 but has a higher index correlated with the vertebra level. They really don´t save label, they change first index in the labelmap.<br>
Other issue is they have color info for each segment, but this is not critical for me.<br>
Is there any way to save labelmap with this kind of “altered index” o edit indexes in labelmaps?</p>

---

## Post #14 by @lassoan (2022-12-01 00:39 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="13" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I´ve been looking for a software to review NIFTI files metadata but I can´t find it</p>
</blockquote>
</aside>
<p>You can use <code>nibabel</code> Python package (you can run <code>pip_install('nibabel')</code> in the Slicer Python console to install it):</p>
<pre data-code-wrap="python"><code class="lang-python">import nibabel
f = nibabel.load(r'path/to/some/segmentation.nii')
print(f)
</code></pre>
<p>It will provide an output like this:</p>
<pre><code class="lang-auto">&lt;class 'nibabel.nifti1.Nifti1Image'&gt;
data shape (256, 256, 130)
affine: 
[[ -0.           0.           1.29999542 -86.64489746]
 [ -1.          -0.          -0.         133.92860413]
 [  0.          -1.           0.         116.78569794]
 [  0.           0.           0.           1.        ]]
metadata:
&lt;class 'nibabel.nifti1.Nifti1Header'&gt; object, endian='&lt;'
sizeof_hdr      : 348
data_type       : b''
db_name         : b''
extents         : 0
session_error   : 0
regular         : b'r'
dim_info        : 0
dim             : [  3 256 256 130   1   1   1   1]
intent_p1       : 0.0
intent_p2       : 0.0
intent_p3       : 0.0
intent_code     : none
datatype        : int16
bitpix          : 16
slice_start     : 0
pixdim          : [1.        1.        1.        1.2999954 0.        0.        0.
 0.       ]
vox_offset      : 0.0
scl_slope       : nan
scl_inter       : nan
slice_end       : 0
slice_code      : unknown
xyzt_units      : 2
cal_max         : 0.0
cal_min         : 0.0
slice_duration  : 0.0
toffset         : 0.0
glmax           : 0
glmin           : 0
descrip         : b''
aux_file        : b''
qform_code      : scanner
sform_code      : scanner
quatern_b       : -0.5
quatern_c       : 0.5
quatern_d       : -0.5
qoffset_x       : -86.6449
qoffset_y       : 133.9286
qoffset_z       : 116.7857
srow_x          : [ -0.          0.          1.2999954 -86.6449   ]
srow_y          : [ -1.      -0.      -0.     133.9286]
srow_z          : [  0.      -1.       0.     116.7857]
intent_name     : b''
magic           : b'n+1'
</code></pre>
<aside class="quote no-group" data-username="apparrilla" data-post="13" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I think I was in a mistake about labels in labelmaps file. Probably these VerSe masks don´t have labels but they are saved with “altered indexes”. I mean that first segment is not index 1 but has a higher index correlated with the vertebra level.</p>
</blockquote>
</aside>
<p>Yes, exactly. NIFTI files have a very limited and rigid header structure. It cannot store label values, but it entirely relies on external label description files to specify which label value correspond to what segment.</p>
<aside class="quote no-group" data-username="apparrilla" data-post="13" data-topic="26468">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>Is there any way to save labelmap with this kind of “altered index” o edit indexes in labelmaps?</p>
</blockquote>
</aside>
<p>I <a href="https://discourse.slicer.org/t/export-segmentation-as-labeled-labelmap/26468/8">provided you the correct label description file for the VerSe data set</a>, which is all you need for importing and exporting with correct segment names / label values, but I give it one more try to explain every click you need to make.</p>
<h1><a name="p-86848-import-1" class="anchor" href="#p-86848-import-1" aria-label="Heading link"></a>Import</h1>
<p>All you need to import a segmentation from NIFTI file with the correct segment names are these two simple steps:</p>
<ol>
<li>Load the label file into Slicer</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d3a3be8746edea315c74e9ef8bed305ba1287b.png" data-download-href="/uploads/short-url/gFuOZe4kGZigEKQIl19Yusw58XV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74d3a3be8746edea315c74e9ef8bed305ba1287b_2_690x131.png" alt="image" data-base62-sha1="gFuOZe4kGZigEKQIl19Yusw58XV" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74d3a3be8746edea315c74e9ef8bed305ba1287b_2_690x131.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d3a3be8746edea315c74e9ef8bed305ba1287b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d3a3be8746edea315c74e9ef8bed305ba1287b.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×185 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Load the NIFTI file, choosing: Description → <code>Segmentation</code>, Color node → <code>VerseLabels</code></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/963407abcd211e701079bcdf1237db42dec7b065.png" data-download-href="/uploads/short-url/lqL5Qjj61gBD2iD1fvDZvWZ9yhT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/963407abcd211e701079bcdf1237db42dec7b065_2_690x120.png" alt="image" data-base62-sha1="lqL5Qjj61gBD2iD1fvDZvWZ9yhT" width="690" height="120" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/963407abcd211e701079bcdf1237db42dec7b065_2_690x120.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/963407abcd211e701079bcdf1237db42dec7b065_2_1035x180.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/963407abcd211e701079bcdf1237db42dec7b065_2_1380x240.png 2x" data-dominant-color="F4F3F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1871×328 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result of the loaded CT volume and vertebra segmentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f827d480f4f8d96809db3e9295788c09b04bc66.jpeg" data-download-href="/uploads/short-url/dCUVMefLv5v0WBicDBSL7yv0xRs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f827d480f4f8d96809db3e9295788c09b04bc66_2_690x397.jpeg" alt="image" data-base62-sha1="dCUVMefLv5v0WBicDBSL7yv0xRs" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f827d480f4f8d96809db3e9295788c09b04bc66_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f827d480f4f8d96809db3e9295788c09b04bc66_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f827d480f4f8d96809db3e9295788c09b04bc66_2_1380x794.jpeg 2x" data-dominant-color="888A8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1105 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1><a name="p-86848-export-2" class="anchor" href="#p-86848-export-2" aria-label="Heading link"></a>Export</h1>
<p>To export a segmentation with the chosen label values in NIFTI format, use “Export to file” section in Segmentations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ab5e97c6f7526ceb8daf0349494e2e34db0f9c.jpeg" data-download-href="/uploads/short-url/lVqd2XihaTaqe4O4I7uJp119E2o.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ab5e97c6f7526ceb8daf0349494e2e34db0f9c_2_526x500.jpeg" alt="image" data-base62-sha1="lVqd2XihaTaqe4O4I7uJp119E2o" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ab5e97c6f7526ceb8daf0349494e2e34db0f9c_2_526x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ab5e97c6f7526ceb8daf0349494e2e34db0f9c_2_789x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99ab5e97c6f7526ceb8daf0349494e2e34db0f9c_2_1052x1000.jpeg 2x" data-dominant-color="B8B8B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1184×1124 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @apparrilla (2022-12-01 14:31 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
Thanks for your export manual… Really clear what to do step by step!</p>
<p>I´ve been talking with <a class="mention" href="/u/diazandr3s">@diazandr3s</a> from MonaiLabel and we have reach another approach to the issue.<br>
I´m going to add empty segments at the begining of segmentation till first vertebra has the same index as label. It´s supposed not to be a problem for MonaiLabel to manage empty segments…</p>
<p>I will give you fedback, maybe be intersting for anyone else because can fix many other problems with multilabel pipelines.</p>
<p>Thank you very much for your support…</p>

---

## Post #16 by @apparrilla (2023-05-11 10:25 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Sorry to be again over this old topic put I´m trying to follow your export method in a script and I´ve found some trouble.</p>
<p>Import color table code:</p>
<blockquote>
<p>labelmapNodePath = ‘path_to_labelmap.nii.gz’ (labelmap is in NIFTI format)<br>
labelmapNode = slicer.util.loadLabelVolume(labelmapNodePath)<br>
importColorTable = slicer.util.loadColorTable(importColorTablePath)<br>
labelmapNode.GetDisplayNode().SetAndObserveColorNodeID(importColorTable.GetID())<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapNode,segmentationNode)</p>
</blockquote>
<p>This is working fine but I don´t know how to make the export task.</p>
<blockquote>
<p>exportLabelmapNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
segmentsIDs = segmentationNode.GetSegmentation().GetSegmentIDs()<br>
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentsIDs, exportLabelmapNode , volumeNode)</p>
</blockquote>
<p>If I try to SetAndObserveColorNodeID to exportLabelmapNodeDisplayNode or segmentationNodeDisplayNode, both sends error of (“vtkSegmentation::SetSegmentIndex failed: index 17 is out of range [0,10]”)</p>
<p>Could you bring me some light about this?<br>
Thanks in advance!!!</p>

---

## Post #17 by @lassoan (2023-05-11 22:49 UTC)

<p>You can use this method: <a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#ace576efb43c16ee0478bf077b3324cff" class="inline-onebox">Slicer: vtkSlicerSegmentationsModuleLogic Class Reference</a></p>
<p>Leave segment list empty to export all the segments. Set the color node as input. If you encounter problems try with latest Slicer Preview Release.</p>

---

## Post #18 by @apparrilla (2023-05-12 22:42 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , thanks for your quick answare!!</p>
<p>It works perfect…</p>

---
