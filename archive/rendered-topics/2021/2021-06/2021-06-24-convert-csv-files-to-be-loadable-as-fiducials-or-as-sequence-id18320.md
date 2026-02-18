# Convert CSV files to be loadable as Fiducials or as Sequence of Fiducials (JSON)

**Topic ID**: 18320
**Date**: 2021-06-24
**URL**: https://discourse.slicer.org/t/convert-csv-files-to-be-loadable-as-fiducials-or-as-sequence-of-fiducials-json/18320

---

## Post #1 by @hmaguilera (2021-06-24 11:21 UTC)

<p>Hi,<br>
I have several CSV files which contain nodal coordinates of a finite element mesh at different time-points after finite element analysis.</p>
<p>I want to validate the FE-model with echocardiography, and therefore want to import the CSV’s into Slicer and plot it together with the echocardiographic volume. Preferably as fiducial markers, and if possible in a Sequence which is loadable. However, JSON files that could be imported as fiducials would do just fine.</p>
<p>The CSV format currently looks like this, but if another format is better this can change.</p>
<p>0.020008288323879242,0.020008288323879242,0.020008288323879242<br>
-5.5104074478149405,21.592485427856445,11.360527992248535<br>
-3.809137344360352,20.855607986450195,11.380624771118164<br>
-2.173929452896118,20.26450729370117,11.737421989440916<br>
-0.4237257242202759,19.472154617309567,12.046059608459473<br>
1.1728017330169676,18.723459243774414,12.897193908691408<br>
3.3027710914611816,19.262800216674805,13.48173522949219<br>
5.7919020652771,22.181146621704098,11.295902252197264<br>
7.3409905433654785,19.74334526062012,6.751131057739258<br>
5.514996528625488,17.492221832275387,5.892641067504882</p>
<p>Here the first row contains the time during FEA, at the X,Y,Z coordinate. Meaning that each column describes the X,Y,Z coordinate respectively.</p>
<p>If someone has any tips on how this could be done, it would be very appreciated.</p>
<p>Best<br>
Hans Martin</p>

---

## Post #2 by @lassoan (2021-06-24 13:13 UTC)

<p>In recent Slicer Preview Releases, you can use the table import feature in Markups module.</p>
<p>All you need to do is to create a valid csv file from this, by adding a header. If the coordinates are in LPS coordinate system then add <code>l,p,s</code> as column names, if the coordinates are in <code>RAS</code> then use <code>r,a,s</code>. For example:</p>
<pre><code class="lang-plaintext">r, a, s
0.020008288323879242,0.020008288323879242,0.020008288323879242
-5.5104074478149405,21.592485427856445,11.360527992248535
-3.809137344360352,20.855607986450195,11.380624771118164
-2.173929452896118,20.26450729370117,11.737421989440916
-0.4237257242202759,19.472154617309567,12.046059608459473
1.1728017330169676,18.723459243774414,12.897193908691408
3.3027710914611816,19.262800216674805,13.48173522949219
5.7919020652771,22.181146621704098,11.295902252197264
7.3409905433654785,19.74334526062012,6.751131057739258
5.514996528625488,17.492221832275387,5.892641067504882
</code></pre>
<p>You can then save this file as .csv and use it as control point coordinates in Slicer:</p>
<ul>
<li>drag-and-drop the .csv file on the Slicer application window and click “Apply” to load it as a table</li>
<li>go to Markups module</li>
<li>create a markup node (fiducial list, curve, …)</li>
<li>in “Export/import table” section choose “Import” and select the input table</li>
<li>click “Import”</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e054fe8fc304a1397512a1bcb4d65da3d7ffaf5d.png" data-download-href="/uploads/short-url/w0x3hJWbbtwjqsd4qqj91PqQcs5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e054fe8fc304a1397512a1bcb4d65da3d7ffaf5d_2_370x500.png" alt="image" data-base62-sha1="w0x3hJWbbtwjqsd4qqj91PqQcs5" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e054fe8fc304a1397512a1bcb4d65da3d7ffaf5d_2_370x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e054fe8fc304a1397512a1bcb4d65da3d7ffaf5d_2_555x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e054fe8fc304a1397512a1bcb4d65da3d7ffaf5d_2_740x1000.png 2x" data-dominant-color="F2F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">951×1282 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There are a couple of more columns that you can add, such as point labels or selected state. See a complete list <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-control-points-table-file-format-csv-tsv">here</a>.</p>
<p>If you want to import a markup directly from a file and/or specify markup display properties (colors, opacities, glyph size, …) then you can create a .mrk.json file. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json">here</a>.</p>

---

## Post #3 by @hmaguilera (2021-06-24 13:21 UTC)

<p>Thank you! That worked perfectly.<br>
HM</p>

---

## Post #4 by @Lin (2022-05-20 23:23 UTC)

<p>Hi Lassoan, did you mean to use l,p,s as a header if the coords system is LPS in the .csv file? Is it a typo that you wrote " If the coordinates are in LPS coordinate system then add <code>r,a,s</code> as column names, if the coordinates are in <code>RAS</code> then use <code>r,a,s</code> ." ?<br>
Thank you, this is important to me.</p>

---

## Post #5 by @lassoan (2022-05-20 23:42 UTC)

<p>Sorry, the that was just a typo (I’ve fixed it now).</p>
<p>Use column names that match the coordinate system axis names.</p>

---
