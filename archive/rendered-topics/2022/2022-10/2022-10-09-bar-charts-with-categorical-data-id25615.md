---
topic_id: 25615
title: "Bar Charts With Categorical Data"
date: 2022-10-09
url: https://discourse.slicer.org/t/25615
---

# Bar charts with categorical data

**Topic ID**: 25615
**Date**: 2022-10-09
**URL**: https://discourse.slicer.org/t/bar-charts-with-categorical-data/25615

---

## Post #1 by @rbumm (2022-10-09 14:42 UTC)

<p>vtkMRMLChartNode is no longer supported in Slicer 5 - how are we supposed to realize somting like</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4c432c5816e3c8d2b3f550114033d311da1de9.png" data-download-href="/uploads/short-url/xReydBb5IOcphqXOV2vdQwVFKid.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4c432c5816e3c8d2b3f550114033d311da1de9_2_540x500.png" alt="image" data-base62-sha1="xReydBb5IOcphqXOV2vdQwVFKid" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4c432c5816e3c8d2b3f550114033d311da1de9_2_540x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4c432c5816e3c8d2b3f550114033d311da1de9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4c432c5816e3c8d2b3f550114033d311da1de9.png 2x" data-dominant-color="EEEDE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">655×606 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>as it was (is) described in</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Charts" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Charts</a></p>
<p>?<br>
Thank you.</p>

---

## Post #2 by @ebrahim (2022-10-09 16:53 UTC)

<p><a href="https://gist.github.com/ebrahimebrahim/8b899552da072fdd22727cfbf0e3a804" rel="noopener nofollow ugc">Here’s how I approached plotting recenetly.</a></p>
<p>In the last line of that gist you can set <code>plot_type='bar'</code> to get a bar chart.</p>

---

## Post #3 by @rbumm (2022-10-09 17:22 UTC)

<p>Thank you.<br>
`How would you set the x axis labels (“tissue”, “bone” etc)  in your</p>
<pre><code class="lang-auto"># Use set_plot_data to update what is shown in the plot view:
slicer_plot_data.set_plot_data(np.random.normal(size=(10,2)))
</code></pre>
<p>line? Could you even set the bar colors?</p>

---

## Post #4 by @ebrahim (2022-10-09 17:32 UTC)

<p>There is a <code>labels</code> argument in <code>set_plot_data</code> but it doesn’t appear to show labels at the bottom, but rather only when you mouse over the bars.</p>
<p>I don’t know if there is a way to set colors of individual bars they way you show above.</p>
<p>If you see a way to do either of these things then please share <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
It may be a limitation in <code>vtkMRMLPlotChartNode</code>’s bar plotting functionality.</p>

---

## Post #5 by @pieper (2022-10-09 22:24 UTC)

<p>There’s a lot of <a href="https://www.na-mic.org/w/img_auth.php/1/18/NA-MIC-VTK-Charts-2011.pdf">underlying functionality</a> and it could be extended and exposed in Slicer.</p>
<p>If you are feeling adventurous <a href="https://discourse.slicer.org/t/pythonqt-properties-shadowing-methods/16992/9">this pyqtgraph example</a> apparently works.</p>
<p>But maybe the safest and easiest would be to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#using-matplotlib">use maplotlib</a> maybe with <a href="https://seaborn.pydata.org/generated/seaborn.barplot.html">seaborn</a>.  It’s not fully integrated with slicer though, so some extra work would be required to make it show up in a layout.</p>

---

## Post #6 by @rbumm (2022-10-10 16:32 UTC)

<p>Thanks, Steve.<br>
Very interesting links.<br>
This is to make CIP_ParenchymaAnalysis fully compatible again  …<br>
Would it not be better to have a simple slicer.util based solution for such a simple and frequently used graph if vtkMRMLChartNode is suddenly not supported any longer? Even analyzing this has cost hours.</p>

---

## Post #7 by @pieper (2022-10-10 17:10 UTC)

<p>Yes, I agree it would be good to have a solid answer to make this easy.  Making these scientific visualizations is a complicated topic and all the options are incomplete or have drawbacks of one kind or another.  My approach would be to make it easy to use one of the mainstream packages like seaborn for this purpose, although extending the VTK-based approach is also an option.</p>

---
