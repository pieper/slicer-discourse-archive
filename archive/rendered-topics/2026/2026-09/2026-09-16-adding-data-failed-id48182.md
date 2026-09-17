---
topic_id: 48182
title: "Adding data failed"
date: 2026-09-16
url: https://discourse.slicer.org/t/48182
last_bumped: 2026-09-16T20:05:28.225Z
---

# Adding data failed

**Topic ID**: 48182
**Date**: 2026-09-16
**URL**: https://discourse.slicer.org/t/adding-data-failed/48182

---

## Post #1 by @FabricioFO (2026-09-16 16:34 UTC)

<p>Hello, everyone, I’m trying to load a tiff data of 4,6 GB size and this message appears:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f45a2683f2012c66b830cb5acc0df22cbd97ae.png" data-download-href="/uploads/short-url/77UUVfxWEw02SR3TIFBKsGwUtWK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f45a2683f2012c66b830cb5acc0df22cbd97ae.png" alt="image" data-base62-sha1="77UUVfxWEw02SR3TIFBKsGwUtWK" width="419" height="201"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">419×201 7.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any advices?</p>

---

## Post #2 by @muratmaga (2026-09-16 16:42 UTC)

<p>hit Ctrl+0 and look at the full log and see if there are any more information about this error? Are you certain file is not corrupt? Can you open with some other software e.g., FiJi</p>

---

## Post #3 by @FabricioFO (2026-09-16 16:52 UTC)

<p>Yes!! It’s not corrupt, I was able to open with Fiji.</p>
<p>The full error is this:</p>
<p>Problem reading the row: 648</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader (0000010D2CA011E0) returned failure for request: vtkInformation (0000010D842E6960)</p>
<p>Debug: Off</p>
<p>Modified Time: 6736291</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_DATA</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>FROM_OUTPUT_PORT: 0</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLMultiVolumeNode1) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>
<p>ReadData: This is not a nrrd file</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLDiffusionWeightedVolumeNode1) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ (first filename: ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’)</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ (first filename: ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’)</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ file as a volume of type ‘DiffusionTensorVolume’. Details: FileFormatError.</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLDiffusionTensorVolumeNode1) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>
<p>ReadData: This is not a nrrd file</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLVectorVolumeNode1) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Failed to instantiate a file reader</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLVectorVolumeNode2) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ (first filename: ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’)</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Reading of file ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ failed: FileFormatError Number of files listed in the node is 0. File reader says it was able to read 1 files. File reader used the archetype file name of ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ (first filename: ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’)</p>
<p>vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read ‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’ file as a volume of type ‘Volume’. Details: FileFormatError.</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node raw-hd_1 (vtkMRMLScalarVolumeNode1) from filename=‘C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif’</p>

---

## Post #4 by @muratmaga (2026-09-16 17:01 UTC)

<aside class="quote no-group" data-username="FabricioFO" data-post="3" data-topic="48182">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fabriciofo/48/82005_2.png" class="avatar"> FabricioFO:</div>
<blockquote>
<p>C:/Users/Rafaela/Desktop/Fabricio/Scapteromys_tumidus_NHMUK_671657/Scapteromys_tumidus_NHMUK_671657/raw-hd.tif</p>
</blockquote>
</aside>
<p>This is with regular add data, right? Did you try with the ImageStacks from the SlicerMorph extension?</p>

---

## Post #5 by @FabricioFO (2026-09-16 17:08 UTC)

<p>Yes, it’s with the regular add data! I can’t use ImageStacks because the file I’m trying to open is just one large file; I don’t have the individual micro-CT scans needed to use ImageStacks.</p>

---

## Post #6 by @muratmaga (2026-09-16 17:22 UTC)

<p>Doesn’t matter, imagestacks support the multi-frame tiffs like yours, and it will display the ordering of the dimensions, which I suspect the issue with this specific file.</p>

---

## Post #7 by @FabricioFO (2026-09-16 17:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18178e68a9e5c4bb50410a29a2aa69c86de43826.png" data-download-href="/uploads/short-url/3r7VyL9xxLdEonzYq2vvlm0kKNM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18178e68a9e5c4bb50410a29a2aa69c86de43826_2_445x499.png" alt="image" data-base62-sha1="3r7VyL9xxLdEonzYq2vvlm0kKNM" width="445" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18178e68a9e5c4bb50410a29a2aa69c86de43826_2_445x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18178e68a9e5c4bb50410a29a2aa69c86de43826_2_667x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18178e68a9e5c4bb50410a29a2aa69c86de43826.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">746×838 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But the button is grey. For this file specifically the image stacks is not working</p>

---

## Post #8 by @muratmaga (2026-09-16 17:29 UTC)

<p>If you can share the file, I can take a look. Meanwhile, if you can try exporting as NRRD from Fiji and try loading that way.</p>

---

## Post #9 by @FabricioFO (2026-09-16 17:52 UTC)

<p>Can I send you an email with the files?</p>

---

## Post #10 by @muratmaga (2026-09-16 18:24 UTC)

<p>you can upload here: <a href="https://faculty.washington.edu/maga/data_dropbox" rel="noopener nofollow ugc">https://faculty.washington.edu/maga/data_dropbox</a></p>

---

## Post #11 by @muratmaga (2026-09-16 20:05 UTC)

<p>I am trying to diagnose why fiji opens the file, but slicer doesn;t. Stll your file contents are indeed corrupted. The first 197 slices are variations of this, even if you were to load this into Slicer, you won’t be able to properly use them (these screenshots are from Fiji)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80.jpeg" data-download-href="/uploads/short-url/fJSsNbGiVD5Ewr1NJTxAGOihWIo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg" alt="image" data-base62-sha1="fJSsNbGiVD5Ewr1NJTxAGOihWIo" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_816x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_1088x1000.jpeg 2x" data-dominant-color="8A8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×1043 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80.jpeg" data-download-href="/uploads/short-url/fJSsNbGiVD5Ewr1NJTxAGOihWIo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg" alt="image" data-base62-sha1="fJSsNbGiVD5Ewr1NJTxAGOihWIo" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_816x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_1088x1000.jpeg 2x" data-dominant-color="8A8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×1043 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80.jpeg" data-download-href="/uploads/short-url/fJSsNbGiVD5Ewr1NJTxAGOihWIo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg" alt="image" data-base62-sha1="fJSsNbGiVD5Ewr1NJTxAGOihWIo" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_544x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_816x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e5040ef6fcd32ad8e74e61bd95e4a41696ebe80_2_1088x1000.jpeg 2x" data-dominant-color="8A8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1136×1043 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the diagnosis from claude, and I agree you should go back to the source and ask an uncorrupt version of the file, possibly as a proper image sequence as opposed to multiframe tiff.</p>
<h2><a name="p-135869-there-are-two-separate-defects-not-one-1" class="anchor" href="#p-135869-there-are-two-separate-defects-not-one-1" aria-label="Heading link"></a>There are two separate defects, not one</h2>
<p>I walked the file’s directory structure directly (no libtiff) and then decoded strips with my own LZW decoder to see where each one breaks.</p>
<p><strong>The file:</strong> <code>/tmp/raw-hd.tif</code>, 4,756,310,985 bytes (4.43 GiB). Header is <code>II*\0</code> — magic 42, <strong>classic TIFF, not BigTIFF</strong>. 1999 pages, 1124 × 978, 16-bit, LZW, one strip per page, no predictor. Page 0 carries <code>ImageDescription = "BoundingBox 0 26.267 0 22.852 0 46.7332"</code>, which against 1124 × 978 × 1999 gives <strong>23.37 µm isotropic voxels</strong> — worth keeping, he’ll need it.</p>
<h3><a name="p-135869-defect-a-the-compressed-data-in-the-first-197-slices-is-corrupt-2" class="anchor" href="#p-135869-defect-a-the-compressed-data-in-the-first-197-slices-is-corrupt-2" aria-label="Heading link"></a>Defect A — the compressed data in the first 197 slices is corrupt</h3>
<p>188 of the first 197 slices (Fiji slices 1–197) fail to LZW-decode. Each one decodes correctly for a while and then the code stream desyncs into noise — which is precisely what your screenshots show: clean anatomy on top, static below. Slice 161 is the variant where the stream hits an end-of-information code instead, so the remainder fills with black.</p>
<p>The smoking gun: <strong>slice 1 decodes 1,458,895 bytes before desyncing. At 2248 bytes per row, that is row 648.97.</strong> That is his <code>Problem reading the row: 648</code>. The error he reported is thrown on the very first slice.</p>
<p>This is real byte-level damage to the compressed streams. It is not recoverable — the information is gone. Nine of those 197 slices happen to be intact (7, 8, 178 among them), which is just luck about where the damage fell.</p>
<h3><a name="p-135869-defect-b-the-file-blows-past-the-4-gib-ceiling-of-classic-tiff-3" class="anchor" href="#p-135869-defect-b-the-file-blows-past-the-4-gib-ceiling-of-classic-tiff-3" aria-label="Heading link"></a>Defect B — the file blows past the 4 GiB ceiling of classic TIFF</h3>
<p>Classic TIFF stores every internal offset in 32 bits, so it can only address 4 GiB. This file is 440 MiB beyond that. From slice 1797 on, the stored <code>StripOffsets</code> have wrapped around and point back into the first few MB of the file — slice 1797’s offset is 1,443,814, which lands in the middle of slice 1’s pixel data. libtiff dutifully seeks there and decodes garbage.</p>
<p><strong>This half is repairable.</strong> The data is all physically present and laid out sequentially — I verified the true extent runs 8 .. 4,756,310,985, exactly the file size, so nothing is missing. Adding 2³² to the wrapped offsets recovers those slices cleanly; I decoded 1797, 1798, 1901 and 1999 that way and they come back as sane CT data with statistics continuous with their neighbours.</p>
<p>Your “data ends at 1801” reading is this defect — structurally the last slice with a valid offset is 1796, and the few after it decode into recognizable-looking wreckage before it becomes obviously noise.</p>
<h2><a name="p-135869-what-this-means-4" class="anchor" href="#p-135869-what-this-means-4" aria-label="Heading link"></a>What this means</h2>
<div class="md-table">
<table>
<thead>
<tr>
<th>Fiji slices</th>
<th>Count</th>
<th>State</th>
</tr>
</thead>
<tbody>
<tr>
<td>1–197</td>
<td>197</td>
<td>Corrupt, unrecoverable (9 intact by chance)</td>
</tr>
<tr>
<td>198–1796</td>
<td>1599</td>
<td>Fine as-is</td>
</tr>
<tr>
<td>1797–1999</td>
<td>203</td>
<td>Recoverable by unwrapping the offsets</td>
</tr>
</tbody>
</table>
</div><p>So <strong>1,802 of 1,999 slices are salvageable</strong>, contiguous, and the loss is at the leading end of the specimen — from your screenshots, mostly air plus the first appearance of that small bone ring around 161–183.</p>
<p>The file is damaged and he should get a fresh copy from whoever produced the scan. Whoever exports it must not write a &gt;4 GiB classic TIFF — the options are BigTIFF, an image sequence of single-page TIFFs, or best, NRRD directly, which also carries the voxel size.</p>
<h2><a name="p-135869-imagejs-lzw-decoder-has-no-error-branch-5" class="anchor" href="#p-135869-imagejs-lzw-decoder-has-no-error-branch-5" aria-label="Heading link"></a>ImageJ’s LZW decoder has no error branch</h2>
<p>Because Fiji isn’t reading it correctly either. It’s showing him fabricated pixels, not recovering anything — those noise and black bands in your screenshots <em>are</em> the failure. The difference is entirely in what each reader does when a decode goes wrong.</p>

---
