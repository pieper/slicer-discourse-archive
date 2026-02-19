---
topic_id: 11997
title: "Switching To Json For Markup Files Any Convergence With Bids"
date: 2020-06-12
url: https://discourse.slicer.org/t/11997
---

# Switching to .json for Markup files: any convergence with BIDS?

**Topic ID**: 11997
**Date**: 2020-06-12
**URL**: https://discourse.slicer.org/t/switching-to-json-for-markup-files-any-convergence-with-bids/11997

---

## Post #1 by @jclauneuro (2020-06-12 03:56 UTC)

<p>This is a continuation of discussion from the following thread <a href="https://discourse.slicer.org/t/markupsline-fcsv-loads-as-markupsfiducials/11545/38" class="inline-onebox">MarkupsLine .fcsv loads as MarkupsFiducials</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> brought up the consideration of switching to <code>.json</code> for handling Markup files in Slicer5. I think the simple answer from the perspective of the AFIDs project is that we will adapt to whatever specs are decided on for Slicer5, but ultimately we have interest in easily being able to convert between Slicer’s Markup file format and one that would be compatible with the Brain Imaging Data Structure (BIDS) specifications.</p>
<p>This may be a good time to try to determine if there is a point of convergence between the needs of both Slicer and BIDS for handling coordinates in <code>.json</code> files that might eliminate the need for any conversion tool. However, this can get complicated if we are looking to decide on <code>.json</code> fields that both Slicer and BIDS communities can agree on.</p>
<p>Compared with other aspects of the BIDS specification which are more mature, representation of coordinates remains a work in progress but is <a href="https://groups.google.com/forum/?utm_medium=email&amp;utm_source=footer#!msg/bids-discussion/rQPf6DuVbh0/19cYWTr7DAAJ" rel="nofollow noopener">of interest to the community for different applications</a>. The most recent version describing “Coordinate Systems” in the BIDS specification (v1.4.0) is <a href="https://bids-specification.readthedocs.io/en/stable/99-appendices/08-coordinate-systems.html" rel="nofollow noopener">here</a>.</p>
<p>There have been different modality specific implementations (the one I’m most familiar with being iEEG) where the proposed solution is to use a paired set of files <code>.json</code> and <code>.tsv</code> to specify electrode locations: see <a href="https://www.nature.com/articles/s41597-019-0105-7#Sec4" rel="nofollow noopener">https://www.nature.com/articles/s41597-019-0105-7#Sec4</a> and Figure 1e and 1f, which I’ve included. Having two files for Markups would likely be quite cumbersome in the Slicer environment.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/13212360/84461826-6e316400-ac3b-11ea-99b6-adba44d64167.png" title="Screen Shot 2020-06-11 at 11 28 55 PM" rel="nofollow noopener"><img width="690" alt="Screen Shot 2020-06-11 at 11 28 55 PM" src="https://user-images.githubusercontent.com/13212360/84461826-6e316400-ac3b-11ea-99b6-adba44d64167.png" height="211"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">Screen Shot 2020-06-11 at 11 28 55 PM</span><span class="informations">1928×590</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d appreciate your thoughts and can loop in members of the BIDS community if interested. I also acknowledge that the Slicer user base likely has different needs than the BIDS/neuroimaging base, so having a converter tool as a go-between may be inevitable.</p>

---

## Post #2 by @lassoan (2020-06-12 04:48 UTC)

<p>This two-file format does not seem very appealing for many reasons, including:</p>
<ul>
<li>two files for a single markup would not be practical, especially for simple markups, such as lines or angles, which only contains a few points</li>
<li>even two files could not store the information we need (display properties, measurements, etc.) - would those all be stored in additional files? It would mean that a single line annotation would require at least 4 files (point end positions, coordinate system, display properties, measurement result)</li>
<li>tsv files are very slow to parse and there is no universally accepted standards for their interpretation (how to encode/escape special characters and separators, basic data types, what makes a header valid, etc.)</li>
<li>there is no standard schema for tsv files</li>
<li>we cannot rely on folder structure and filenames to establish links between data sets, as it would be just too rigid and fragile (instead we rather use UIDs for cross-references between information objects: MRML node IDs and DICOM-compliant UIDs)</li>
</ul>
<p>To improve interoperability between BIDS and Slicer, probably the best would be to implement a BIDS importer/exporter module. We have some initial work <a href="https://github.com/PerkLab/NeuroSegmentation">here</a>.</p>

---

## Post #3 by @jclauneuro (2020-06-12 17:17 UTC)

<p>Agree with your assessment. I am also starting to wonder if the coordinate representation in BIDS-iEEG would be better as a single file. I’ll consider proposing that change at some point once I’ve had a chance to think about it more.</p>
<p>For now, let’s just assume that BIDS and Slicer5 representations of points in <code>.json</code> will develop independently and require a converter tool to go between formats.</p>

---
