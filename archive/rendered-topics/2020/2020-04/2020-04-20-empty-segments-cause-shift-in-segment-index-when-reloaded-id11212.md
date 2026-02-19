---
topic_id: 11212
title: "Empty Segments Cause Shift In Segment Index When Reloaded"
date: 2020-04-20
url: https://discourse.slicer.org/t/11212
---

# Empty segments cause shift in segment index when reloaded

**Topic ID**: 11212
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/empty-segments-cause-shift-in-segment-index-when-reloaded/11212

---

## Post #1 by @muratmaga (2020-04-20 17:28 UTC)

<p>We have a blank segmentation template with 8 segments. Some of the organisms we segment will have all 8 of these distinct structures, and some other will only a subset of it. When I save my segmentation, say with 6 structures (e.g., 3 and 4 is missing), and reload the segmentation back into slicer as a volume (since that’s what we ultimately need), I see segments 5, 6, 7, and 8 are shifted to 3, 4, 5, and 6. Not only we lost the ability to tell the segments are missing, they are now also mapped to incorrect structures. It does not suffer from this problem if the data is loaded as a segmentation.</p>
<p>If this is intentional, I would argue it is a bug. Same segmentation exported as a label map doesn’t suffer from this (e.g., loaded volume has indices 1,2, 5, 6, 7, 8). While saving the output as label map fixes my issue, I think the behavior should be the same for segmentations too.</p>
<p>This is with Slicer r28896 on windows 10.</p>

---

## Post #2 by @lassoan (2020-04-20 18:18 UTC)

<p>Segmentations files (.seg.nrrd) store each segment’s identity inside the same file, using terminology codes. This is much more robust than relying on external files to tell which label value correspond to which structure.</p>
<p>Note that relying on specific labelmap value for representing a structure is not feasible in general. For example, it would prevent you from importing segments from multiple subjects into a single segmentation.</p>
<p>Nevertheless, we implemented mechanism to preserve original label values if possible, e.g., if you only do simple analysis and editing, then label values will not change. For example, having an empty segment should not affect saved label values. Try with latest Slicer Preview Release and if you can reproduce the behavior that you described above then provide a sample scene and description of steps you performed.</p>

---

## Post #3 by @muratmaga (2020-04-20 18:42 UTC)

<p>Thanks Andras. This was with a preview version from 2-3 weeks ago, will try with a later preview version.</p>
<p>Unfortunately we have to use a tool external to Slicer. For example how would ITK-SNap would read the seg.nrrd format? Would it display the segment names or the indices?</p>

---

## Post #4 by @lassoan (2020-04-20 19:11 UTC)

<p>ITK-Snap relies on external color table file to specify what label value corresponds to what structure. If you want, you can implement an importer/exporter for such color table files in 10-20 lines of Python code (that would load them as Slicer color table files). Or we could tune the current color table reader/writer to accept ITK-Snap-style colormaps as well. However, why would you still use ITK-Snap?</p>

---

## Post #5 by @muratmaga (2020-04-20 19:13 UTC)

<p>I just use that as an example, we are not using ITK-snap, but other tools (such as ANTs/R) that rely on ITKIO.</p>

---

## Post #6 by @lassoan (2020-04-21 00:26 UTC)

<p>When you export a particular set of segments to labelmap (so that you can process it in external software) you also get a colormap node that contains the mapping. You can also <a href="http://apidocs.slicer.org/master/classvtkSegment.html#a1ad4dda762acc77760cfb61e547d2c66">retrieve the current label value of a segment</a> anytime.</p>
<p>If you have a particular use case then we can give more specific advice (and it may also help us to understand if we can improve the API to make interfacing with external tools easier).</p>

---

## Post #7 by @S_Arbabi (2023-07-12 14:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I have a specific usecase for it.<br>
Actually, I have a segmentation node with 17 segments (with ids 1 to 17), which we do some manual correction using segment editor module. As you can imagine some of the segments are empty for some images, this makes a bit of issue when I want to save that segmentation node to nii.gz file so then loading it in an standard automatic segmentation library (like nnUNet).<br>
For saving as nii.gz, I first convert segmentation node to labelmap (which I think drops the empty segments in this step). what can be a good ideas on how to handle this situation?</p>

---

## Post #8 by @lassoan (2023-07-12 14:48 UTC)

<p>Proper, long-term, sustainable solution: Since you may want to reuse the same dataset in various projects and you may need to aggregate data from multiple sources in a single project, arbitrarily chosen hardcoded label values could not ever work. Instead of relying on hardcoded labels in the file, I would recommend to rely on the segmentation metadata stored in the file (that specifies what segments are stored in the file, in which layer, what label), and then assign project-specific label value when you read the file. This is implemented in <a href="https://pypi.org/project/slicerio/">slicerio Python package</a>, as shown in <a href="https://github.com/lassoan/slicerio#extract-selected-segments-with-chosen-label-values">this example</a>. If you want, you can save the resulting array into a NIFTI file, but I would recommend to use slicerio in your image reader.</p>
<p>If you are not ready for this yet and you want to keep using hardcoded label values, then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">use a color table</a> (that specifies segment name → label value mapping) when exporting the segmentation.</p>

---
