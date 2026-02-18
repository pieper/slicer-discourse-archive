# How to rename segment name or segmentation IDs by label in `ImportLabelmapToSegmentationNode`?

**Topic ID**: 44888
**Date**: 2025-10-26
**URL**: https://discourse.slicer.org/t/how-to-rename-segment-name-or-segmentation-ids-by-label-in-importlabelmaptosegmentationnode/44888

---

## Post #1 by @jumbojing (2025-10-26 23:21 UTC)

<p>Howto rename segment name or segmentation IDs by label instead of color in <code>ImportLabelmapToSegmentationNode</code>?</p>
<p>我发现有时候会返回标签, 有时候却返回颜色…怎么控制呢?</p>
<p>为何用颜色作为默认命名而不是标签呢? 我觉得后者更有意义啊</p>
<p>I noticed that sometimes it returns labels, and sometimes it returns colors… How can I custom or control this?</p>
<p>Why is <code>color name</code> used as the default <code>segment name</code> or <code>segmentationIDs</code> instead of the <code>label</code>? I think the latter is more meaningful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72e6fdae3215c2d2396c5b2260e47ba525375ef.png" data-download-href="/uploads/short-url/wZ7MKI72OqHCQtjOvgu3KAgUDn1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e72e6fdae3215c2d2396c5b2260e47ba525375ef_2_690x397.png" alt="image" data-base62-sha1="wZ7MKI72OqHCQtjOvgu3KAgUDn1" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e72e6fdae3215c2d2396c5b2260e47ba525375ef_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72e6fdae3215c2d2396c5b2260e47ba525375ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72e6fdae3215c2d2396c5b2260e47ba525375ef.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×580 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-10-27 12:18 UTC)

<p>Slicer now supports terminologies by default. What it means is that your segmentation will correspond to one terminology <em>context</em> and the segments will be entries from that context. The “color selector” will, in this default mode, select a terminology entry (information about what structure it is in addition to the color). You can choose not to use terminologies in Application Settings, but it is more correct to use a proper terminology context containing your segment types. It helps with identifying the segments correctly, without the need to type in the segment name manually (which is error prone, and also one structure may be called in different ways, e.g. “femural head left” vs “femural head lt” vs “left femural head”). Read more on this feature <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html">here</a>.</p>

---

## Post #3 by @lassoan (2025-10-29 02:38 UTC)

<p>If you select an appropriate color table when importing a labelmap then all the segments have correct name and terminology (as you specified in the color table). You can easily create a color table .csv file in a text editor or in Excel. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv">here</a>.</p>

---
