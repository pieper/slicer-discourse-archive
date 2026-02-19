---
topic_id: 20686
title: "Exporting Orthogonal Projections As Dicom"
date: 2021-11-18
url: https://discourse.slicer.org/t/20686
---

# Exporting orthogonal projections as DICOM

**Topic ID**: 20686
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/exporting-orthogonal-projections-as-dicom/20686

---

## Post #1 by @alan (2021-11-18 13:42 UTC)

<p>Hello,</p>
<p>I’m looking to:</p>
<ul>
<li>import thin (0.5 mm) slice CT DICOM series (multiple per patient) in the axial projection</li>
<li>create orthogonal coronal and sagittal views of each series</li>
<li>export as DICOM files</li>
<li>so can be viewed in all 3 planes on external viewers without MPR capabilities</li>
</ul>
<p>I’ve tried to follow the guides and even YouTube videos alongside advice on this Discourse but I never seem to actually get the orthogonal projections exported within the DICOM. Please may I ask whether this possible and am I just being silly? If so, please may someone direct me towards any guides for this?</p>
<p>Thanks so much!<br>
Alan</p>

---

## Post #2 by @pieper (2021-11-18 14:28 UTC)

<p>Try the Orient Scalar Volume module to create new volumes and then you can export them to dicom.</p>

---

## Post #3 by @alan (2021-11-18 14:48 UTC)

<p>Dear Steve,</p>
<p>Many thanks, I’ll look into this!</p>
<p>Alan</p>

---
