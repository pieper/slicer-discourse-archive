---
topic_id: 3014
title: "Embedding Specimen Metadata Into The 3D Volume"
date: 2018-05-30
url: https://discourse.slicer.org/t/3014
---

# Embedding specimen metadata into the 3D volume

**Topic ID**: 3014
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/embedding-specimen-metadata-into-the-3d-volume/3014

---

## Post #1 by @muratmaga (2018-05-30 05:58 UTC)

<p>Dear all,</p>
<p>As part of a project we will be converting large number of 3D high-resolution scans of biological specimens into volumetric format. Currently most of them are in DICOM or some sort of a image sequence, and we want to use something like NRRD to facilitate easier data exchange and increase usability of these data with 3D Slicer.</p>
<p>However, we also need to make sure we can trace the provenance of the dataset (museum specimen/accession number is the absolute minimum, and possibly few other tags, for example species designation or sex). I am hoping to have a better and more robust method than simply naming the volume with this number and keeping the metadata external. One idea was to use NRRD with a detached text header and keep some of this information as comments. But I am not sure what would happen to them if the user accidentally checkmarks the save option. Would this be retained? Are there other formats more suitable for our use case?</p>
<p>I appreciate any feedback.</p>
<pre><code>NRRD0004
content: Skull CT
# Specimen No: 627546 
# Institution: USNM
# Genus: Homo
# Species: sapiens
# Specimen DOI/URL: where data is stored
dimension: 3
type: short
space: RAS
space directions: (0.5, 0, 0) (0, 0.5, 0) (0, 0, 1)
sizes: 512 512 256
data file: ./USNM627546_Skull_CT.raw.gz
encoding: gzip</code></pre>

---

## Post #2 by @lassoan (2018-05-30 13:02 UTC)

<p>Currently, you can only save custom metadata for a segment and not for the entire segmentation:</p>
<pre><code>segmentationNode=slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
segmentationNode.GetSegmentation().GetNthSegment(0).SetTag("SomeCustomAttribute","This is a value")
</code></pre>
<p>It would be useful and should be quite easy to add custom tags/attributes in the segmentation object itself. <a class="mention" href="/u/cpinter">@cpinter</a> what do you think? Was there any particular reason why we did not implement this?</p>

---

## Post #3 by @muratmaga (2018-05-30 16:47 UTC)

<p>Thank Andras,<br>
So would this this work only with Segment editor? Just to be clear, I am looking into something that I can embed in the volume file, and that these tags are read into Slicer when they are loaded into scene.</p>

---

## Post #4 by @lassoan (2018-05-30 17:13 UTC)

<p>You can embed custom metadata in nrrd files, but you would need to write custom importer and exporter for that. We could implement reading/writing of all or some custom metadata fields into volume nodes, but in general metadata is not saved into volume files. Instead, these two approaches are often used:</p>
<ul>
<li>Use MRB files: Save volume, all kinds of metadata, segmentations, computed results, etc. in mrb file.</li>
<li>Use image file name/path to identify the subject and use external files to store metadata. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator</a> for an example for how you can use this approach for interactive batch processing.</li>
</ul>

---

## Post #5 by @phcerdan (2023-03-31 16:41 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>, can I ask what you ended up doing?</p>
<p>I am getting tired of working with 3 zillions dcm files from DICOM, but I don’t want to lose any metadata. The dream, I know.</p>
<p>I have explored, just a bit, storing the dicom metadata into nrrd files, with custom metadata fields, and it’s ok’eish. But I am curious about your experience after all this time. Thanks for any time you can spare!</p>

---

## Post #6 by @muratmaga (2023-03-31 16:49 UTC)

<p>I agree this is an issue for research imaging format. There is really no one-size fits all solution.</p>
<p>As explained by <a class="mention" href="/u/lassoan">@lassoan</a> custom NRRD headers, works only if you have custom reader/writers (e.g., if you open the NRRD with custom headers in other software and resave it for any reason, those fields are likely to disappear).</p>
<p>There are emerging formats there are more metadata rich, such aS ome-zarr, that will probably fill the gap between NRRD and DICOM, but their support is somewhat sketchy.</p>
<p>If this is for your own data archiving needs, and if you are using Slicer, probably a NRRD + CSV type of metadata of solution might be simplest for the time being. That way you won’t have the risk of loosing embded custom metadata, and csv’s are readily imported into Slicer as tables (you can even turn them into MRB as <a class="mention" href="/u/lassoan">@lassoan</a> suggested).</p>
<p>But it would be good to hear from others too.</p>

---

## Post #7 by @lassoan (2023-04-03 15:22 UTC)

<aside class="quote no-group" data-username="phcerdan" data-post="5" data-topic="3014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/phcerdan/48/1559_2.png" class="avatar"> phcerdan:</div>
<blockquote>
<p>I don’t want to lose any metadata</p>
</blockquote>
</aside>
<p>If you really don’t want to lose <em>any</em> DICOM metadata then the only option I can think of is to store the DICOM instance UIDs in the NRRD file and look up the required metadata from the original DICOM files as needed. DICOM files store a database of complex, hierarchical, interlinked data objects. Even if you save some attributes of some objects somewhere, there is no way you can preserve all data stored in this complex database. Even ome-zarr will not preserve all DICOM metadata. There is an emerging DICOM standard for lossless storage of instances in JSON format, but that is an extremely complex and unfriendly data structure that would be almost as hard to use as binary DICOM (e.g., you cannot simply use json objects to store attributes, because order of attributes matters in DICOM and json objects don’t support attribute ordering).</p>
<p>If you just want to store <em>some</em> custom metadata fields in your files for convenience (which you know you need for a specific analysis), you could store them as custom metadata fields in the NRRD file. However, as <a class="mention" href="/u/muratmaga">@muratmaga</a> warned you, you’ll have to be careful with what tools you use to process these NRRD files, as custom fields may not preserved when you load, modify, and save an image. I’m not sure if we preserve all custom metadata fields for NRRD files in Slicer now. It would not be hard to implement, if it is not implemented already.</p>

---
