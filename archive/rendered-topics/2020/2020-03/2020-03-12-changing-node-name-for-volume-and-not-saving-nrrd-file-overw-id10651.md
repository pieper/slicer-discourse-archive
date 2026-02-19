---
topic_id: 10651
title: "Changing Node Name For Volume And Not Saving Nrrd File Overw"
date: 2020-03-12
url: https://discourse.slicer.org/t/10651
---

# Changing node name for volume and not saving .nrrd file overwrites file path in the scene

**Topic ID**: 10651
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/changing-node-name-for-volume-and-not-saving-nrrd-file-overwrites-file-path-in-the-scene/10651

---

## Post #1 by @Vincent_C (2020-03-12 03:32 UTC)

<p>Hi all,</p>
<p>I loaded a single slice DICOM - name: “l3.dcm” (say) - as a volume. The node created is “l3.dcm”.</p>
<p>I changed the node name in the Data Module from “l3.dcm” to “subject1” and hit save. I saved the .mrml scene file but NOT the .nrrd. After closing Slicer, I tried to open the .mrml scene and no data is loaded.</p>
<p>I opened the .mrml with Notepad and it looks as if the fileName path is being changed to the node name I designated. It appears if I choose not to save the .nrrd, it is not possible to have different node names and the file names.</p>
<p>I feel this is a bug because typically the expected behaviour would be that node name changes should affect the file path.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-12 04:04 UTC)

<aside class="quote no-group" data-username="Vincent_C" data-post="1" data-topic="10651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_c/48/5759_2.png" class="avatar"> Vincent_C:</div>
<blockquote>
<p>typically the expected behaviour would be that node name changes should affect the file path</p>
</blockquote>
</aside>
<p>This is the current behavior: node name changes affect the file path.</p>
<p>I see how it may be unexpected that you are allowed to edit the filename even when the box is unchecked. I’ll add a note to <a href="https://issues.slicer.org/view.php?id=3890">this related issue</a>.</p>

---

## Post #3 by @Vincent_C (2020-03-12 04:43 UTC)

<p>EDIT:<br>
…expected behaviour would be that node name changes should NOT affect the file path.</p>

---

## Post #4 by @lassoan (2020-03-12 20:03 UTC)

<aside class="quote no-group" data-username="Vincent_C" data-post="3" data-topic="10651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_c/48/5759_2.png" class="avatar"> Vincent_C:</div>
<blockquote>
<p>expected behaviour would be that node name changes should NOT affect the file path</p>
</blockquote>
</aside>
<p>This was the original behavior, but it caused lots of confusion among users. For example, they updated node names in the scene, but they forgot to rename files accordingly when they saved the scene.</p>
<p>As an engineer, I would prefer if node renames did not update the filenames automatically, but as a Slicer user, I have to admit that this mechanism saves time and make things safer.</p>
<aside class="quote no-group" data-username="Vincent_C" data-post="1" data-topic="10651">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_c/48/5759_2.png" class="avatar"> Vincent_C:</div>
<blockquote>
<p>I loaded a single slice DICOM - name: “l3.dcm”</p>
</blockquote>
</aside>
<p>This indicates that you loaded DICOM using “Add data” dialog. This is a loophole that we haven’t closed yet, but you should always load DICOM data using DICOM module. We will disable DICOM loading via “Add data” when we are sure that we sufficiently simplified loading via DICOM module.</p>

---
