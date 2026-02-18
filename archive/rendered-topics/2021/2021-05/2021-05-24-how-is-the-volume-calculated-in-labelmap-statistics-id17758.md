# How is the volume calculated in Labelmap statistics

**Topic ID**: 17758
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/how-is-the-volume-calculated-in-labelmap-statistics/17758

---

## Post #1 by @Chenglin_Zhu (2021-05-24 12:27 UTC)

<p>Hello!<br>
I am new to Slicer and I’m trying to calculate the volume of the pituitary gland from MRI slides. Now I can segment the pituitary gland out and use segment statistics to calculate its volume. However, I wondering how is the volume calculated out of discrete slides and what assumptions are made?</p>
<p>Appreciate</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-05-24 13:14 UTC)

<p>Hello <a class="mention" href="/u/chenglin_zhu">@Chenglin_Zhu</a></p>
<p>Here is some documentation<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>
<p>Actual code</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/LabelmapSegmentStatisticsPlugin.py#L94-L97" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/LabelmapSegmentStatisticsPlugin.py#L94-L97" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/LabelmapSegmentStatisticsPlugin.py#L94-L97</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="94" style="counter-reset: li-counter 93 ;">
          <li>if "volume_mm3" in requestedKeys:</li>
          <li>  stats["volume_mm3"] = stat.GetVoxelCount() * cubicMMPerVoxel</li>
          <li>if "volume_cm3" in requestedKeys:</li>
          <li>  stats["volume_cm3"] = stat.GetVoxelCount() * cubicMMPerVoxel * ccPerCubicMM</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>-Andinet</p>

---
