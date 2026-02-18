# How to programmatically export data from segment statistics?

**Topic ID**: 17390
**Date**: 2021-04-30
**URL**: https://discourse.slicer.org/t/how-to-programmatically-export-data-from-segment-statistics/17390

---

## Post #1 by @akshay_pillai (2021-04-30 07:02 UTC)

<p>Operating system: Windows 10</p>
<p>I use segment statistics to generate a table of all the information I need.<br>
My question is how can I export the table of information from slicer programmatically after I use segment statistics. Ideally, I would run a command that would just export the table.<br>
Also, how can I generate a graph or histogram from segment statistics and export that as well(programmatically)</p>

---

## Post #2 by @rbumm (2021-05-01 11:17 UTC)

<p>You can use</p>
<pre><code>slicer.util.saveNode(tablenode,filename)
</code></pre>
<p>A “test.csv” filename will export it in the CSV format.</p>

---

## Post #3 by @akshay_pillai (2021-05-04 05:59 UTC)

<p>Great, thanks. Also, do you know how I can generate a graph of all the segments and the info?</p>

---

## Post #4 by @rbumm (2021-05-04 08:05 UTC)

<p>The segment statistics module generates a result table (find it in the Data module).<br>
If you open this result table in the “Table” module, you can directly create a plot chart.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c4e255c45cf2bd40c95e1954e92700886c37065.jpeg" data-download-href="/uploads/short-url/42oNm70rlyNBQfN62LnYJAd9ijX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c4e255c45cf2bd40c95e1954e92700886c37065_2_690x388.jpeg" alt="image" data-base62-sha1="42oNm70rlyNBQfN62LnYJAd9ijX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c4e255c45cf2bd40c95e1954e92700886c37065_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c4e255c45cf2bd40c95e1954e92700886c37065_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c4e255c45cf2bd40c95e1954e92700886c37065_2_1380x776.jpeg 2x" data-dominant-color="B2B4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>More sophisticated plotting requires Python scripting:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></p>

---
