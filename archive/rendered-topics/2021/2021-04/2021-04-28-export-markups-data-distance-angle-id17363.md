# Export Markups Data (Distance, Angle)?

**Topic ID**: 17363
**Date**: 2021-04-28
**URL**: https://discourse.slicer.org/t/export-markups-data-distance-angle/17363

---

## Post #1 by @lazymark2 (2021-04-28 05:31 UTC)

<p>Operating system:Linux<br>
Slicer version:4.11.20210226<br>
Hi everyone, recently I want to measure the data of crown length and root length. And I used markupsline tool in Markups Mode. But I can’t find a way to export the desired data (distance in this example). So is there a way to directly export the distance of all markupslines? (I need to measure lots of teeth so it will be loads of work if I need to manually record all the data).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a11311400c9cac8c256cc24427d062622a2b4327.png" alt="2021-04-28 13-29-55屏幕截图" data-base62-sha1="mYVIUGkhAbAp1S7mW77xCd0fhJl" width="343" height="264"></p>

---

## Post #2 by @muratmaga (2021-04-28 06:06 UTC)

<p>If you save them as in mrk.json format, measurement fields will be saved. You can either programmatically extract that, or use excel as shown in this thread: <a href="https://discourse.slicer.org/t/export-formats-for-markups/16278/13" class="inline-onebox">Export formats for markups - #13 by lassoan</a></p>

---

## Post #3 by @lazymark2 (2021-04-28 07:46 UTC)

<p>It works, many thanks!</p>

---

## Post #4 by @lassoan (2021-04-28 15:37 UTC)

<p>A few tips that can make your measurement a magnitude faster:</p>
<ul>
<li>If you need to measure the same values in many images then pre-create all the markups using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#pre-populate-the-scene-with-measurements">this script</a>
</li>
<li>Copy all measurement results (along with input filename and measurement name) into an Excel sheet with a single keyboard shortcut using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#copy-all-measurements-in-the-scene-to-excel">this script</a>
</li>
<li>Position the slice view to the correct cross-section much faster: specify the dental arch using a markups curve node, then reslice along that curve using “Cross-section analysis module” (in SlicerVMTK extension) or straighten the arch using “Curved planar reformat module” (in Sandbox extension).</li>
<li>Adjust the cross-section by rotating slice intersections by <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">rotating slice intersections</a>
</li>
</ul>
<p>See this video of how to set up keyboard shortcuts for defining measurements and copy them directly to Excel:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="_mloKGTtLog" data-video-title="Make your 3D measurements faster using Python scripting" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=_mloKGTtLog" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/_mloKGTtLog/maxresdefault.jpg" title="Make your 3D measurements faster using Python scripting" width="" height="">
  </a>
</div>


---
