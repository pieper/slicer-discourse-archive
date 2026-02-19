---
topic_id: 18018
title: "Shape Analysis Using Mfsda"
date: 2021-06-08
url: https://discourse.slicer.org/t/18018
---

# Shape analysis using MFSDA

**Topic ID**: 18018
**Date**: 2021-06-08
**URL**: https://discourse.slicer.org/t/shape-analysis-using-mfsda/18018

---

## Post #1 by @iyerkrithika21 (2021-06-08 17:43 UTC)

<p>Trying to run the Covariates Significance Test with SlicerSALT 3.0.0</p>
<ol>
<li>The program fails if the selected folder to store the output values is empty</li>
<li>If pvalues.json and output.vtk are some empty files placed in the output folder, the modules closes abruptly<br>
3.I am also seeing this error: <code>Source array too small, requested tuple at index 26101, but there are only 492 tuples in the array.</code>
</li>
</ol>

---

## Post #2 by @bpaniagua (2021-06-08 17:45 UTC)

<p>Hi Krithika,</p>
<p>I am sorry you are having problems with covariance testing. Can you describe your inputs to MSFDA?<br>
Thanks,</p>
<p>Bea</p>

---

## Post #3 by @iyerkrithika21 (2021-06-08 17:47 UTC)

<p>Yes, input.csv which has two columns : VTK File and groups<br>
Using the Shape Population Analyzer I am also able to load the data using the csv file.</p>

---

## Post #4 by @bpaniagua (2021-06-08 17:49 UTC)

<p>Can you check the dimensionality of every sample you have? i.e. in unix systems, by going to the folder where the vtk’s are stated and doing head file.vtk. In bash that would be<br>
<code>for i in ./*vtk ; do head $i ; done</code></p>

---

## Post #5 by @iyerkrithika21 (2021-06-08 17:53 UTC)

<p>I can see that all vtk files have varying number of points. But all of them are in the range of 26000.</p>
<pre><code class="lang-auto">ASCII
DATASET POLYDATA
POINTS 25983 float
</code></pre>

---

## Post #6 by @alexsunny123 (2021-06-13 12:07 UTC)

<aside class="quote no-group" data-username="bpaniagua" data-post="4" data-topic="18018" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>Can you check the dimensionality of every sample you have? i.e. in unix systems, by going to the folder where the vtk’s are stated and doing head file.vtk. In bash that would be<br>
<code>for i in ./*vtk ; do head $i ; done</code></p>
</blockquote>
</aside>
<p>thanks for the awesome information.</p>

---

## Post #7 by @alexsunny123 (2021-09-07 13:11 UTC)

<aside class="quote no-group quote-modified" data-username="alexsunny123" data-post="6" data-topic="18018" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/51bf81/48.png" class="avatar"> alexsunny123:</div>
<blockquote>
<aside class="quote no-group quote-modified" data-username="bpaniagua" data-post="4" data-topic="18018">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bpaniagua/48/20_2.png" class="avatar"> bpaniagua:</div>
<blockquote>
<p>Can you check the dimensionality of every sample you have? i.e. in unix systems, by going to the folder where the vtk’s are stated and doing head file.vtk. In bash that would be</p>
<blockquote>
<p><code>for i in ./*vtk ; do head $i ; done</code>  <a href="https://ometv.onl" rel="noopener nofollow ugc">.</a> <a href="https://chatroulette.top" rel="noopener nofollow ugc">.</a> <a href="https://omegle.wtf" rel="noopener nofollow ugc">.</a></p>
</blockquote>
</blockquote>
</aside>
<p>thanks for the awesome information.</p>
</blockquote>
</aside>
<p>thanks my issue has been fixxed.</p>

---
