# Converting fiducial coordinates from RAS to LPS

**Topic ID**: 9707
**Date**: 2020-01-03
**URL**: https://discourse.slicer.org/t/converting-fiducial-coordinates-from-ras-to-lps/9707

---

## Post #1 by @matt-warkentin (2020-01-03 21:06 UTC)

<p>Hi,</p>
<p>I am working with some chest CT scans and I have some <code>fiducials</code> which denote the 3D centre of a tumour mass. I have saved/exported the <code>fiducials</code> from Slicer as <code>.fcsv</code> files.</p>
<p>I have done some searching online but I am not entirely sure how to convert the <code>fiducial</code> coordinates (in mm) from <code>RAS</code> to <code>LPS</code> using <code>Slicer</code> (assuming its possibile). Hoping someone can point me in the right direction.</p>
<p>Also, if anyone here has any general resources they could point me towards to better understand RAS to LPS (and vice versa) geometric transformations, that would be greatly appreciated. Always looking to better understand these concepts.</p>
<p>Thanks,<br>
Matt</p>

---

## Post #2 by @pieper (2020-01-03 21:20 UTC)

<p>This documentation should help get you started: <a href="https://www.slicer.org/wiki/Coordinate_systems">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>How do you plan to use the fcsv files?</p>

---

## Post #3 by @matt-warkentin (2020-01-03 21:24 UTC)

<p>Thanks for sharing <a class="mention" href="/u/pieper">@pieper</a>. The motivating example is that I have been given fiducials (as <code>.fcsv</code> files) from a radiological colleague where they have denoted the centre of the tumour masses across many CT scans. I was then trying to use <code>plastimatch crop</code> to extract an image subregion surrounding the tumour centroid. It is my understanding that <code>plastimatch</code> uses <code>ITK</code> which is LPS orientation, meanwhile my fiducials are RAS.</p>

---

## Post #4 by @pieper (2020-01-03 22:07 UTC)

<p>Okay, good, makes sense.  Then probably the documentation I referenced should be what you need.</p>

---

## Post #5 by @lassoan (2020-01-03 22:17 UTC)

<p>LPS&lt;-&gt;RAS conversion is just inverting the sign of the first two coordinates. You can use either LPS or RAS when you store the coordinate values in csv (fcsv) file.</p>

---

## Post #6 by @matt-warkentin (2020-01-03 22:22 UTC)

<p>Thanks to both of you. I thought this to be true, but I am glad you confirmed this.</p>
<p>If I already have a long list of RAS fiducials in <code>.fcsv</code>, it is probably just easiest to do the conversion “by-hand” with <code>R</code> or <code>Python</code>, for example? Just flip the signs of the <code>x</code> and <code>y</code> value in the fidicuals file.</p>

---

## Post #7 by @lassoan (2020-01-04 00:37 UTC)

<p>If you specify LPS coordinate system in the fcsv file header then the LPS-&gt;RAS conversion is done automatically when you load the file (but of course it is very simple to do the conversion in any software).</p>
<p>By default, fcsv header uses <code># CoordinateSystem = 0</code>, which means RAS. If you change this to <code># CoordinateSystem = 1</code> then coordinate values are interpreted as LPS.</p>
<p>This header indicates that coordinates are defined in LPS:</p>
<pre><code class="lang-auto"># Markups fiducial file version = 4.11
# CoordinateSystem = 1
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,22.30452734727109,31.445727079759223,0,0,0,0,1,1,1,0,F-1,,
...
</code></pre>
<p>Probably we’ll replace magic numbers (0 and 1) by coordinate system names (RAS and LPS) in future versions of these csv files.</p>

---
