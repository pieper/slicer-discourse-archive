---
topic_id: 31544
title: "Add Series In Subject Hierarchy Tree With Identical Study In"
date: 2023-09-04
url: https://discourse.slicer.org/t/31544
---

# Add series in subject hierarchy tree with identical study instance UID and series description (for example anonymized and not anonymized)

**Topic ID**: 31544
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/add-series-in-subject-hierarchy-tree-with-identical-study-instance-uid-and-series-description-for-example-anonymized-and-not-anonymized/31544

---

## Post #1 by @CertisPoette (2023-09-04 12:28 UTC)

<p>Dear All,</p>
<p>We are currently working on managing patient information in Slicer. A test have been made where we load series with identical instance UID and series description but with a different patient name (anonymized dataset for example).</p>
<p>See screenshot for result: node_1 belongs to the “NOT anonymized” series and node_2 to the “anonymized” series but still node_2 is sorted in the first section because they both have the same instance UID and series description. And the last patient item ID is empty.</p>
<p>If the study instance UID already exists, I expect the patient item ID to exists as well. But in Slicer sources, the patient item ID is created anyway. Is there any scenario where the study instance UID already exists but not the patient item ID ?</p>
<p>This type of scenario is probably unlikely but it can be considered as a weakness especially when dealing with anonymized data. Could you provide information on how to deal with anonymized dataset? Is there some extra checks we could do ?</p>
<p>Thank you for your time!</p>
<p>Cheers,</p>
<p>Christopher</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a35ea4ad8e7988ef42ad8943e5d6ebc0408d121b.png" alt="image" data-base62-sha1="njeBcfv6qCgdcAKeY8E31ycR85J" width="498" height="149"></p>
<p>Operating system: Ubuntu 20.04.6 LTS<br>
Slicer version: 5.2.2<br>
Expected behavior: node_2 is sorted in “anonymized” section.<br>
Actual behavior: node_2 is sorted in the “NOT anonymized” section with the “anonimized” section empty.</p>

---

## Post #2 by @lassoan (2023-09-04 14:50 UTC)

<aside class="quote no-group" data-username="CertisPoette" data-post="1" data-topic="31544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/certispoette/48/66462_2.png" class="avatar"> CertisPoette:</div>
<blockquote>
<p>A test have been made where we load series with identical instance UID and series description but with a different patient name</p>
</blockquote>
</aside>
<p>It is a very serious violation of the DICOM standard if you use different patient name with the same study or series instance UID. When an image is anonymized then all instance UIDs must be replaced, too.</p>
<p>The DICOM standard is extremely complex and it is practically impossible to prepare a software to deal with all possible ways of data corruptions. Some systems may detect some kind of errors, but even then, the only “fix” is to delete all corrupted/inconsistent data objects.</p>
<p>This is why hospital IT administrators typically do not let researchers to upload <em>any</em> data to the clinical PACS - because it is too easy to create inconsistent data sets by using DICOM manipulation tools and it can cause serious issues in the hospital information system.</p>

---

## Post #3 by @CertisPoette (2023-09-04 15:25 UTC)

<p>Thank you very much for your quick response!</p>
<p>In that case, the problem is clearly the way I was anonymizing the DICOMs…</p>
<p>It is noted! Thanks again!</p>
<p>Christopher</p>

---
