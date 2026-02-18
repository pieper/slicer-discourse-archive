# New feature: Search and filter in segments table

**Topic ID**: 7827
**Date**: 2019-07-31
**URL**: https://discourse.slicer.org/t/new-feature-search-and-filter-in-segments-table/7827

---

## Post #1 by @Sunderlandkyl (2019-07-31 15:08 UTC)

<p>Previously, one of the main obstacles to using the segmentations module was that it was difficult to navigate through the table to find a specific segment. With the addition of the filter bar, it is now easier  to use segmentations containing a large number of segments.</p>
<div class="lazyYT" data-youtube-id="Y9TGeOcShzI" data-youtube-title="3D Slicer - Updated Segments Table" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>New features in segments table:</p>
<ul>
<li>
<p>Segment status</p>
<ul>
<li>Displays the current status of the segment (Not started, In progress, Completed, Flagged)</li>
<li>Status can be changed by left-clicking on the status icon (Not started <img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=9" title=":arrow_right:" class="emoji" alt=":arrow_right:"> In progress <img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=9" title=":arrow_right:" class="emoji" alt=":arrow_right:"> Completed <img src="https://emoji.discourse-cdn.com/twitter/left_right_arrow.png?v=9" title=":left_right_arrow:" class="emoji" alt=":left_right_arrow:"> Flagged), or by right-clicking on the table and selecting the status from the context menu</li>
<li>When creating a new segment, the initial state of the segment will be set to the first visible status</li>
<li>Right-clicking on the table and selecting “Clear selected segments” will erase the master representation of the segments and set their status to “Not started”</li>
</ul>
</li>
<li>
<p>Filter bar</p>
<ul>
<li>Allows filtering through the list of segments based on name and status</li>
<li>Hidden by default. Can be shown by right-clicking on the table and selecting “Show filter bar”</li>
<li>Searchable text box will only show matching segments (Either in segment name or in the value of one of the tags)</li>
<li>Enabled status buttons will only show segments with a matching status</li>
</ul>
</li>
<li>
<p>Segment editor</p>
<ul>
<li>Editing a segment in the “Not started” state will set the state to “In progress”</li>
<li>Previous/Next segment shortcuts will only navigate through the list of visible segments that match the filter</li>
</ul>
</li>
</ul>
<p>Development was supported by Brigham and Women’s Hospital through NIH grant R01MH112748.</p>

---
