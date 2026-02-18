# Label Color Changed after saving

**Topic ID**: 33070
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/label-color-changed-after-saving/33070

---

## Post #1 by @Reza (2023-11-27 18:56 UTC)

<p>Hi,</p>
<p>After segmenting with Segment Editor Module and saving it, I closed 3D slicer and then I tried to reload my segmentation, but I noticed that the label colors have been changed. For example, I segmented a tumor with label color 31, necrosis with label color 15, and fat with label color 12. After saving my work, I re-opened the saved files (label and etc.) in 3D slicer and found out that the labels have changed to 1, 2, and 3! How can I fix this issue?</p>
<p>Thank you,</p>

---

## Post #2 by @muratmaga (2023-11-27 20:09 UTC)

<p>Are you exporting your segmentation to a labelmap, or are you saving them as seg.nrrd?</p>

---

## Post #3 by @Reza (2023-11-27 20:15 UTC)

<p>Hi, I am segmenting to a labelmap. Also, I tried saving as seg.nrrd, but same the issue happend.</p>

---

## Post #4 by @muratmaga (2023-11-27 20:46 UTC)

<p>This should not happen if you keep the segmentation in seg.nrrd format. Make sure you are saving the original segmentation, not the exported labelmap in this format.</p>

---

## Post #5 by @Reza (2023-11-28 13:09 UTC)

<p>Okay. I will try that. Thanks.</p>

---

## Post #6 by @Reza (2023-11-28 14:25 UTC)

<p>When I save it in seg.nrrd, there would be no issue. But the thing is that I want to save it in Nifti format, because the algorithm we use for feature extraction is based on Nifti format(nii). So, after I am done with the segmentation in “Segment Editor Module”, I go to “Import\export nodes”, then I go to the Export/Import models and labelmaps and put the <strong>Operation</strong> on <strong>Export</strong> and the <strong>Output type</strong> on <strong>Labelmap</strong> and then I click on Export. Then for saving the segmentation, I uncheck the “Segmentation.seg.nrrd” box and I change the “Segmentation-label.nrrd”'s format to <strong>Nifti</strong>. After I am done with saving, and when I re-open my segmentation, I see that the labels have been changed.<br>
Which part did I do wrong and what can I do to fix it?<br>
Is there any way to save my segmentation in Nifti format?</p>
<p>Thank you,</p>

---

## Post #7 by @muratmaga (2023-11-28 15:43 UTC)

<p>If you need to export your label with assigning specific indices, then you need to create a color table and specify that. Specifically you need to use this section of the <code>Segmentations</code> module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e881e9de15343c683363747e9b9d0cbb816159d.png" alt="image" data-base62-sha1="i3lNmsW8FYBjZTsEIlzTzrhNzYx" width="611" height="318"></p>
<p>Also see this <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">Segmentations — 3D Slicer documentation</a></p>
<p><strong>The label value is index of the color table entry that has the same name as the segment name.</strong></p>

---
