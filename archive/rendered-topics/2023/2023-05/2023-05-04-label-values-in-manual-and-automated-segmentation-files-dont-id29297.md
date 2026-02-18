# Label values in manual and automated segmentation files don't match

**Topic ID**: 29297
**Date**: 2023-05-04
**URL**: https://discourse.slicer.org/t/label-values-in-manual-and-automated-segmentation-files-dont-match/29297

---

## Post #1 by @Js165 (2023-05-04 15:52 UTC)

<p>Hello experts,<br>
I have manual and automated segmentation files in NIFTI format. Now, I am computing some statistical measures, like Jaccard, average distance, etc. But the problem is manual and automated files have different label values. I checked both the files in Slicer and found that “Segment_1” of the automated segmented file matches with “Segment_4” of the manual segmented file. Similarly, “Segment_2” of the automated segmented file matches with “Segment_3” of the manual segmented file. I am assuming due to these issues, I am not getting correct scores.<br>
Is there any way to fix this problem using Slicer? Any help will be highly appreciated.</p>

---

## Post #2 by @lassoan (2023-05-06 17:39 UTC)

<p>Label values can change while you are editing a segmentation, because you can split and merge existing segments, create new segments, delete segments, etc.</p>
<p>We developed a robust method for ensuring that imported and exported label values remain consistent. All you need to do is to create a color table that specifies label value, name, and color for each segment (see the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#discrete-scale-color-lookup-table">file format description here</a>, you can use any text editor to create it). For example, I created this <code>test.txt</code>  file in Notepad:</p>
<pre><code class="lang-txt">1 artery 216 101 79 255
2 bone 241 214 145 255
10 connective_tissue 111 184 210 255
</code></pre>
<p>Load the created color table file into Slicer. Then, select this color node when you load the labelmap image file (e.g., a NIFTI file) into Slicer (see detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">here</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f26e0130ae51423a9a7580b7ee8bbc05a0666557.png" data-download-href="/uploads/short-url/yADemJUUImlQPzX7QCSdY7zIf6T.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26e0130ae51423a9a7580b7ee8bbc05a0666557_2_690x134.png" alt="image" data-base62-sha1="yADemJUUImlQPzX7QCSdY7zIf6T" width="690" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26e0130ae51423a9a7580b7ee8bbc05a0666557_2_690x134.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26e0130ae51423a9a7580b7ee8bbc05a0666557_2_1035x201.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f26e0130ae51423a9a7580b7ee8bbc05a0666557_2_1380x268.png 2x" data-dominant-color="444342"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1930×377 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When you export the segmentation to NIFTI file in Segmentations module, make sure “Use color table values” is enabled and the same color node is selected there (see detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">here</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bba62ef48cccc528586ed4bd5bf5003ec7dd9b0.png" data-download-href="/uploads/short-url/8wnv7lYSNwceOQGgBjJZOp6YB7a.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bba62ef48cccc528586ed4bd5bf5003ec7dd9b0.png" alt="image" data-base62-sha1="8wnv7lYSNwceOQGgBjJZOp6YB7a" width="690" height="434" data-dominant-color="3C3C3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">964×607 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To simplify this import/export process, I would recommend to store segmentations in .seg.nrrd segmentation files (nrrd files with custom attributes that specify segment label values and colors). Using segmentation files have the advantage that you don’t rely on external knowledge about what each label value encodes. This is very useful because for example each project specifies meaning of label values differently, therefore you cannot use the same NIFTI files across different projects, while the same .seg.nrrd files can be safely used in many projects without modifications.</p>

---
