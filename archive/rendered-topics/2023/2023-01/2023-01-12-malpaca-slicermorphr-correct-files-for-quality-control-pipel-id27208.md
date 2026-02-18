# MALPACA + slicerMorphR --> correct files for quality control pipeline in R

**Topic ID**: 27208
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/malpaca-slicermorphr-correct-files-for-quality-control-pipeline-in-r/27208

---

## Post #1 by @MrMarkus (2023-01-12 13:55 UTC)

<p>Slicer version: 5.1.0-2022-06-01 r30987 / 177f3b3</p>
<p>Hi,</p>
<p>currently I’m trying to get familiar with the new great features of “MALPACA” of the SlicerMorph module.</p>
<p>I followed the steps according to the Appendix given in the manuscript:<br>
<a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278035" class="onebox" target="_blank" rel="noopener nofollow ugc">https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278035</a></p>
<p>MALPACA works fine using the downloaded sample data (mice &amp; apes).<br>
Also the quality control pipeline using <strong>slicerMorphR</strong> worked out as described in the Appendix (IV. Landmarking Quality Control Pipeline)</p>
<p>Next I tried MALPACA with my data.<br>
In a final step, the QC pipeline was also tested with the new data in R.</p>
<p>Unfortunately the data could not be loaded in R, resulting in the following error message in R:</p>
<p>Error in file(file, “rt”) : cannot open the connection<br>
In addition: Warning message:<br>
In file(file, “rt”) :<br>
cannot open file ‘…/output_target_landmarks/individualEstimates/NA’: No such file or directory</p>
<p>Next I have compared the *.fcsv files of the example data with my data.</p>
<ul>
<li>in the example *.fcsv file: the “relation” is given as “associatedNodeID”  “template - subject”</li>
</ul>
<p>columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID<br>
vtkMRMLMarkupsFiducialNode_0,-72.8187,-127.5815,50.494,0,0,0,1,1,1,1,<strong>USNM084655_LM1-1</strong>,</p>
<p>I guess this information is needed to relate the resulting median &amp; the individual landmarks in order to perform the post hoc QC.</p>
<ul>
<li>this kind of description is missing in the data which was generated using MALPACA with my own data</li>
</ul>
<p>columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID<br>
1,-7.591875076293945,-4.460249423980713,26.58815574645996,0,0,0,1,1,1,0,1 <strong>, , ,</strong>  2,0</p>
<p>Could this be the reason why <strong>SlicerMorphR</strong> causes an error when trying to perform the post-hoc QC?<br>
That an “meaningful” description of the “associatedNodeID” is required?</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2023-01-12 17:57 UTC)

<p>Please try updating your SlicerMorphR package. I believe this  (extra fields in fcsv files) already fixed. Going forward, I suggest using JSON format as output to avoid these fidelity issues. You can now set the output of ALPACA/MALPACA to be json.</p>

---

## Post #3 by @MrMarkus (2023-01-13 10:42 UTC)

<p>Hi,</p>
<p>the following version of SlicerMorphR ist used:</p>
<ul>
<li>Package SlicerMorphR version 0.0.0.9000</li>
</ul>
<p>The software 3D Slicer was updated, now running:</p>
<ul>
<li>3D Slicer 5.2.1 r31317 / 77da381</li>
</ul>
<p>Regarding the format of the landmarks, now using:</p>
<ul>
<li>*.mrk.json format</li>
</ul>
<p>Unfortunately SlicerMorphR still returns an error when trying to read the<br>
estimated landmarks:</p>
<p>LMs ← read.malpaca.estimates(MALPACA_outputDir = MAL_outDir_git, templates_Dir = templates_path_git)<br>
results in:</p>
<ul>
<li>Error in <code>[.data.frame</code>(temp, , 2:4) : undefined columns selected</li>
</ul>
<p>Data used: 2 templates, 3 targets</p>
<p>Any idea how to solve this?</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @muratmaga (2023-01-13 16:32 UTC)

<p>You need to share your MALPACA output for us to see what the issue is.</p>

---

## Post #5 by @chz31 (2023-01-13 20:30 UTC)

<p>Thanks for pointing out the issues and trying our methods. When we just finished the MALPACA output loading functions and the manuscript, we were using the older version of Slicer. Therefore, we tentatively put these functions in my own repository of the development version of SlicerMorphR, which is also listed in the supplementary materials of the manuscript.</p>
<p>For the current Slicer, saving landmarks in fcsv creates an extra empty column at the end. The updated main SlicerMorphR, which can be installed using <code>devtools::install_github('SlicerMorph/SlicerMorphR')</code>, should be able to resolve the loading fscv issue you mentioned with the function <code>read.markups.fcsv</code>. Can you give it a try?</p>
<p>Meanwhile, I am doing some tests and updates about MALPACA results loading functions in my own repo of the development versison of the SlicerMorphR. I’ll then merge it into the main repository. It should be quick.</p>

---

## Post #6 by @chz31 (2023-01-15 23:21 UTC)

<p>I have updated the SlicerMorphR package. Can you please install it via  <code>devtools::install_github('SlicerMorph/SlicerMorphR')</code> a try? The landmark files generated by the new MALPACA/ALPACA module should be in mrk.json format. The new update should work with both mrk.json and fcsv.</p>

---

## Post #7 by @MrMarkus (2023-01-16 07:56 UTC)

<p>Dear Chi,</p>
<p>thanks for your quick response!</p>
<p>The following steps were tried:</p>
<ul>
<li>SlicerMorphR was updated  `devtools::install_github(‘SlicerMorph/SlicerMorphR’)</li>
</ul>
<p>Outcome:</p>
<ul>
<li>fcsv AND mrk.json data can be imported</li>
</ul>
<p>Minor issue:</p>
<ul>
<li>help/SlicerMorphR.rdb is corrupt</li>
</ul>
<p>This might be due to the fact that my R version is 4.2.1 and “jsonlite” was compiled/generated<br>
using R version 4.2.2 ??? (not sure)</p>
<p>Anyway. The post-hoc QC can be performed, e.g. using 2 templates, outliers$estimates_no_out[4:6, , 1, 7] results in:</p>
<pre><code>       x         y        z
</code></pre>
<p>4  -7.163967 -4.116971 17.13764<br>
5 -13.477526 -5.081557 16.88782<br>
6 -10.627498 -3.185812 16.92243</p>
<p>outliers$estimates_no_out[4:6, , 2, 7] results in:</p>
<pre><code>       x         y        z
</code></pre>
<p>4  -7.248554 -4.241855 16.97166<br>
5 -13.474133 -5.052335 16.82217<br>
6 -10.607809 -3.201885 17.07043</p>
<p>(templates are quiet similar, this is known…)</p>
<p>Thanks!</p>
<p>Best regards,<br>
Markus</p>

---

## Post #8 by @chz31 (2023-01-17 17:29 UTC)

<p>Hi Markus,</p>
<p>That’s great! I’ll look into the SlicerMorphR.rdb corrupt issue. What you suggested might be right. Thanks again for trying our method!</p>
<p>Best,<br>
Chi</p>

---
