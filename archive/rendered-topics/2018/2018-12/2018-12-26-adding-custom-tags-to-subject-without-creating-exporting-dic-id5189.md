---
topic_id: 5189
title: "Adding Custom Tags To Subject Without Creating Exporting Dic"
date: 2018-12-26
url: https://discourse.slicer.org/t/5189
---

# Adding custom tags to subject without creating/exporting DICOMs

**Topic ID**: 5189
**Date**: 2018-12-26
**URL**: https://discourse.slicer.org/t/adding-custom-tags-to-subject-without-creating-exporting-dicoms/5189

---

## Post #1 by @muratmaga (2018-12-26 05:21 UTC)

<p>Is it possible to set and display some of the DICOM tags from the subject hierarchy without actually having a dicom volume ? E.g., I organized this mockup MRB file. It contains everything I need in terms of imaging data (an NRRD file), segmentation and exported model, fiducials etc. I still need to describe the genus/species/strains/sex (and few other things as well) of this subject AMNH123456. If I choose to export one of the volume as a DICOM, I get to specify some of those. But I don’t want to do that, but retain my volumes as NRRD/NII for convenience and skip the unnecessary export step.</p>
<p>What I was looking/hoping for is some sort of functionality, where I right click on the subject, and then choose something like ‘<strong>create custom tag/metadata field</strong>’, and then start populating them as I need. Or even a way to specify/declare these custom tags only once, so that we don’t make typos entering them manually all the time (species vs speices kind of thing). Then, these tags gets stored in the mrml/mrb file. My goal is being able to access this information programmatically for batch processing, as well as making sure some metadata travels with the dataset.</p>
<p>I am not sure if this is currently possible. How difficult would it be to implement something this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27483400296be999405983174fc5d3f839102e83.png" data-download-href="/uploads/short-url/5BvjA4fepft25osA206CRMHtl0D.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27483400296be999405983174fc5d3f839102e83_2_690x342.png" alt="image" data-base62-sha1="5BvjA4fepft25osA206CRMHtl0D" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27483400296be999405983174fc5d3f839102e83_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27483400296be999405983174fc5d3f839102e83.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27483400296be999405983174fc5d3f839102e83.png 2x" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">857×426 56.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-12-27 06:16 UTC)

<p>You can set subject hierarchy attributes using <code>shNode.SetItemAttribute</code> method as shown in this post: <a href="https://discourse.slicer.org/t/hausdorff-distance-calculation-in-segmentcomparison-module/4300/18?u=lassoan" class="inline-onebox">Hausdorff distance calculation in SegmentComparison module</a></p>
<p>If this scripting interface is not convenient enough then you can add items add an item to the right-click menu that shows a popup where you can add/edit/delete item attributes. You can add menu items using Subject Hierarchy plugin, using either Python or C++. See <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SubjectHierarchyPlugins/SegmentStatisticsSubjectHierarchyPlugin.py" rel="nofollow noopener">this example</a> that adds a “Calculate statistics…” menu item. If we find that this need comes up often then we can add the plugin in Slicer core or maybe add an attribute editor similar to the node attribute editor in the Data module.</p>

---

## Post #3 by @pieper (2019-01-09 19:43 UTC)

<p>Another approach could be to just create a table node in the scene that contains whatever information you think is important to track.  This would save/restore with the MRB, but could also be easily exported as csv (or cut and paste) for use with Excel or whatever.  You could also create a template and part of the workflow would be to create the table either in Slicer or elsewhere when accessioning the study.</p>

---

## Post #4 by @muratmaga (2019-01-10 19:13 UTC)

<p>Actually tables might work. However, when I save as csv/tsv file and reload it in the scene, it doesn’t remember the customization I did (like locking columns, rows so those values cannot be manually changed). Are those handled by the mrml scene?</p>

---

## Post #5 by @lassoan (2019-01-10 19:14 UTC)

<p>Locking columns and rows should be saved in the scene. Let me know if you find that it is not.</p>

---
