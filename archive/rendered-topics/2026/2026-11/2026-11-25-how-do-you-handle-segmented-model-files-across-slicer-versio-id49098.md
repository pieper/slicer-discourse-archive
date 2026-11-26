---
topic_id: 49098
title: "How do you handle segmented model files across Slicer versions?"
date: 2026-11-25
url: https://discourse.slicer.org/t/49098
last_bumped: 2026-11-25T19:26:46.244Z
---

# How do you handle segmented model files across Slicer versions?

**Topic ID**: 49098
**Date**: 2026-11-25
**URL**: https://discourse.slicer.org/t/how-do-you-handle-segmented-model-files-across-slicer-versions/49098

---

## Post #1 by @rimsouthcott16 (2026-11-25 17:50 UTC)

<p>I’m setting up a small workflow for a lab group at the university and trying to decide how to organize our segmentation work so it survives version changes. We have several people producing label maps and surface models from the same scans, and some of them open files in different Slicer releases. I’m not sure whether to standardize on one save format or keep both model and label map outputs, since I’ve read that some formats don’t round-trip cleanly between versions and I’m worried about losing segment names or colors. My main concern is that a colleague’s older files might load without warnings but still be subtly different from what they intended. I haven’t committed to a scheme yet and don’t want to force everyone onto one version if there’s a simpler habit that works. If you’ve dealt with this in a shared project, what has actually held up for your group?</p>

---

## Post #2 by @muratmaga (2026-11-25 17:58 UTC)

<p>This is exactly the problem <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MorphoDepot#readme" rel="noopener nofollow ugc"><code>MorphoDepot</code></a> is created to solve. (Step by step tutorial is in the link).</p>
<p>You can find the overview paper here: <a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210x.70342" rel="noopener nofollow ugc">https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210x.70342</a></p>

---

## Post #3 by @fedorov (2026-11-25 19:26 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=16" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<p><a href="https://portal.imaging.datacommons.cancer.gov/">Imaging Data Commons</a> relies on DICOM for storing segmentation results, and DICOM Segmentation is supported in Slicer.</p>
<p>Connect your AI assistant to the hosted IDC MCP to learn more: <a href="https://learn.canceridc.dev/ai-assistants/agents" class="inline-onebox">Start here | IDC User Guide</a>.</p>
<p>Below is the response from Claude (Opus 5.5), grounded in real experience and data we have in IDC, and checked/re-prompted by me - I have expertise in IDC and the relevant capabilities of DICOM.</p>
<p>Full conversation: <a href="https://claude.ai/share/0c030605-cacb-43c8-829d-d4b96c0338bb">https://claude.ai/share/0c030605-cacb-43c8-829d-d4b96c0338bb</a></p>
<hr>
<p>If your scans are DICOM, I’d suggest <strong>DICOM Segmentation (SEG)</strong> as the format of record. It addresses most of what you’re worried about:</p>
<ul>
<li><strong>Segment names and colors are defined by the DICOM standard, not by a Slicer version.</strong> Each segment carries a label, standard codes for what it represents (e.g. SNOMED “Liver”, “Neoplasm”), and a recommended display color. Pick segment types from Slicer’s terminology selector instead of typing free-text names, and two people’s “liver” will clearly be the same structure.</li>
<li><strong>A segmentation can’t quietly end up on the wrong scan.</strong> Each SEG records the UIDs of the image series it was drawn on, so it’s tied to the exact source images.</li>
<li><strong>Provenance stays with the file.</strong> Creator, method (manual / semi-automatic / automatic) and algorithm name are stored inside it. Fill these in carefully, though: the standard gives them a place but doesn’t check that they’re correct.</li>
<li><strong>Each revision is a new object.</strong> SEGs are write-once, so every edit gets its own series and date, which gives you a record of every version.</li>
</ul>
<p><strong>Evidence that it works at scale:</strong> NCI Imaging Data Commons (IDC) uses SEG as its main format for segmentations. The current release (v25) has about 193,000 SEG series with about 9.7 million segments across 70 collections, combining expert manual work and AI output from many groups and tools.</p>
<p><strong>Size isn’t a real objection.</strong> Most existing SEGs were saved uncompressed, but the standard also supports a LABELMAP type and lossless compression. In IDC, RCC-AID’s compressed labelmap SEGs average about 0.06 MB, versus about 5.8 MB for uncompressed binary SEGs with a similar number of segments on kidney CT. Overlapping segments need the binary type, which can also be compressed.</p>
<p><strong>Surface models:</strong> DICOM also defines a Surface Segmentation object. IDC doesn’t contain any yet and software support is limited, so for now I’d keep the masks as the primary record and regenerate surfaces from them in Slicer.</p>
<p><strong>A habit that should hold up:</strong></p>
<ol>
<li>Edit in <code>.seg.nrrd</code>, using coded terminology for segment names.</li>
<li>Export a DICOM SEG at each checkpoint and treat that as the official copy.</li>
<li>Test a round trip once: export from the newest Slicer release your group uses, open it in the oldest, and compare names, colors and masks. Also check that your setup supports labelmap and compressed SEGs. (Tools: the QuantitativeReporting extension / dcmqi in Slicer; highdicom in Python.)</li>
</ol>
<p><strong>Examples you can open in the browser</strong> (source images and segmentation together):</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Example</th>
<th>What it shows</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://viewer.imaging.datacommons.cancer.gov/v3/viewer/?StudyInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.3671.4004.276055617216249523101813141367">RCC-AID, kidney CT</a></td>
<td>Compressed labelmap SEG, 4 segments, ~0.02 MB</td>
</tr>
<tr>
<td><a href="https://viewer.imaging.datacommons.cancer.gov/v3/viewer/?StudyInstanceUIDs=1.2.840.113654.2.55.21869611586140117852707052775371860162">TotalSegmentator, NLST chest CT</a></td>
<td>96 coded anatomical segments in one object (uncompressed, ~130 MB)</td>
</tr>
<tr>
<td><a href="https://viewer.imaging.datacommons.cancer.gov/v3/viewer/?StudyInstanceUIDs=1.3.6.1.4.1.14519.5.2.1.6279.6001.186378343509510052901886052675">LIDC-IDRI, chest CT</a></td>
<td>Each radiologist’s nodule outline as its own SEG on the same scan</td>
</tr>
<tr>
<td><a href="https://viewer.imaging.datacommons.cancer.gov/slim/studies/2.25.64490252589945153782290037746217138493">Pan-Cancer nuclei, TCGA-GBM slide</a></td>
<td>Pathology: SEG mask plus ~55,000 nucleus polygons</td>
</tr>
<tr>
<td><a href="https://viewer.imaging.datacommons.cancer.gov/slim/studies/2.25.192556633057601350687037567350138553949">Stony Brook TIL map, TCGA-STAD slide</a></td>
<td>Fractional (probability) SEG on a whole-slide image</td>
</tr>
</tbody>
</table>
</div><p>To load the CT examples in your own Slicer releases (handy for the round-trip test), paste the study UID into the SlicerIDCBrowser extension.</p>
<p>The same approach is used beyond radiology. IDC has about 27,000 SEGs on pathology slides and about 6.2 billion nucleus polygons stored as DICOM annotation objects.</p>
<p>More detail, including the queries behind these numbers: full <a href="https://claude.ai/share/0c030605-cacb-43c8-829d-d4b96c0338bb">conversation transcript</a>.</p>

---
