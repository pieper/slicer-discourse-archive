---
topic_id: 32870
title: "Convert Tck To Vtk Streamlines"
date: 2023-11-17
url: https://discourse.slicer.org/t/32870
---

# Convert .tck to .vtk streamlines

**Topic ID**: 32870
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/convert-tck-to-vtk-streamlines/32870

---

## Post #1 by @yi_yang (2023-11-17 05:05 UTC)

<p>Hi,<br>
I am trying to convert some tractography data from .tck to .vtk format. But I can’t get the correct results that match the image loaded in slicer. I’m not very familiar to vtk files and<br>
slicer so I’m seeking for help. Here’s the efforts I’ve tried:</p>
<ol>
<li><code>tckconvert -scanner2image</code><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00d2cce925cec36b5a5fdcf148eb0c1b5d00b322.png" alt="image" data-base62-sha1="7hDxS2rX0Y0ki0TZRh4nEcXQjg" width="627" height="127"> Mrtrix provides a command to realize it. TCK files are in world coordinates and <code>2image</code> means changing it to image coordinates(in mm). Then load vtk as<code> models</code> with explicitly set <code>coordinate system</code> as RAS. But the problems are:</li>
</ol>
<ul>
<li>Anterior and Posterior of the image volume seems wrong as you can see in Fig.1.</li>
<li>Tracts(yellow) are above the back right of the image volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca682f0a809c96e1d6d4971218d07b99b95bfbf7.png" data-download-href="/uploads/short-url/sSzF1yg3Y7J2nIic3TCiVccrpNd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca682f0a809c96e1d6d4971218d07b99b95bfbf7_2_690x446.png" alt="image" data-base62-sha1="sSzF1yg3Y7J2nIic3TCiVccrpNd" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca682f0a809c96e1d6d4971218d07b99b95bfbf7_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca682f0a809c96e1d6d4971218d07b99b95bfbf7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca682f0a809c96e1d6d4971218d07b99b95bfbf7.png 2x" data-dominant-color="8E8EBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×463 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b939f3abfec7949de1dc53267e2b597c3af6c2.png" alt="image" data-base62-sha1="c5uX64XScLpsqdmrKiLmTYtXjGi" width="632" height="430"></li>
</ul>
<ol start="2">
<li><code>tckconvert -scanner2voxel</code>, where <code>2voxel</code> means changing it to voxel coordinates. Also load vtk as<code> models</code> with explicitly set <code>coordinate system</code> as RAS. Now :</li>
</ol>
<ul>
<li>Tracts(blue) are smaller than it should be.</li>
<li>different location from tracts(yellow).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fede079220163139669419387fd23a69c5788308.jpeg" data-download-href="/uploads/short-url/AmEYmKKdzYWQ2bJOb1SadskBp7q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fede079220163139669419387fd23a69c5788308_2_690x455.jpeg" alt="image" data-base62-sha1="AmEYmKKdzYWQ2bJOb1SadskBp7q" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fede079220163139669419387fd23a69c5788308_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fede079220163139669419387fd23a69c5788308_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fede079220163139669419387fd23a69c5788308.jpeg 2x" data-dominant-color="898CB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1301×858 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/809fd78599bf32e9c9a3be18bafd1a86ad4d9760.png" alt="image" data-base62-sha1="ilRzHEaWMH1UTy7RWrxacexSJFu" width="655" height="431"></li>
</ul>
<ol start="3">
<li>python vtk package:<br>
<a href="https://mail.python.org/pipermail/neuroimaging/2019-July/002006.html" rel="noopener nofollow ugc">reference here</a> In reference, a TRK file was loaded and converted,here I replaced with a TCK file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c7239c07db1f30391da0087ef49f7b12911378a.png" data-download-href="/uploads/short-url/6lbJCOLI5d5D4LkMbvJtjN2nXWa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c7239c07db1f30391da0087ef49f7b12911378a.png" alt="image" data-base62-sha1="6lbJCOLI5d5D4LkMbvJtjN2nXWa" width="640" height="500" data-dominant-color="222323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×810 37.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Now:</li>
</ol>
<ul>
<li>Tracts(green) is in the back of the volume</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a8116e7612445826ffabd853c561aaebfa2e73c.png" data-download-href="/uploads/short-url/m2O6pjkDxWLjoQ6EtH6FZ9OT4cY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8116e7612445826ffabd853c561aaebfa2e73c_2_690x454.png" alt="image" data-base62-sha1="m2O6pjkDxWLjoQ6EtH6FZ9OT4cY" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8116e7612445826ffabd853c561aaebfa2e73c_2_690x454.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a8116e7612445826ffabd853c561aaebfa2e73c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a8116e7612445826ffabd853c561aaebfa2e73c.png 2x" data-dominant-color="8991B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×456 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0a198714cf72dae44fc8765e4a9ec75bf77ca54.png" alt="image" data-base62-sha1="tLDwTvHwHtVByWHJnjAifkSbKCw" width="645" height="424"></p>
<ol start="4">
<li>python vtk package:I tried to move original coordination in voxel coordinates randomly ( maybe change RAS to LAS, and move tracts backward a little? <code>10</code> is a number I test to match, really painful…) As the same, load it as RAS system.<br>
Now:</li>
</ol>
<ul>
<li>
<p>Tracts(red) seems flipped over in A-P direction<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fda03ea95878faf2d57641f5f3adf4d97655e43a.png" data-download-href="/uploads/short-url/AbG7ChJCVNwblTBtG8izK20aL4m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fda03ea95878faf2d57641f5f3adf4d97655e43a.png" alt="image" data-base62-sha1="AbG7ChJCVNwblTBtG8izK20aL4m" width="690" height="278" data-dominant-color="242524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1054×426 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd5f9fc42ed8cc17ae21635a69f074d3c2eacc7.png" alt="image" data-base62-sha1="2g5Bu6nTJVG9pi9B6c1WC58pHev" width="662" height="439"></p>
</li>
<li>
<p>If I set image as centered when loading image volume, suddenly the tracts(red) can match the volume. However, I still don’t understand the rationale.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df9ad06d380379a69c6ea514fd5fcd6224922509.png" data-download-href="/uploads/short-url/vU6a9nYyb378SQmbZHYGWjwfybL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df9ad06d380379a69c6ea514fd5fcd6224922509.png" alt="image" data-base62-sha1="vU6a9nYyb378SQmbZHYGWjwfybL" width="690" height="195" data-dominant-color="F0EFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">740×210 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79fc5d1fcebcde5d3f2254629a80340475b23dd5.png" alt="image" data-base62-sha1="hp8szjH91xofeDYSt8P68WcKwSN" width="618" height="448"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf4811a757609fd3185f3fd84fca318ee49942dc.png" alt="image" data-base62-sha1="tzHf5H4wll260fd78Ng4Q8ddWPO" width="459" height="414"></p>
</li>
</ul>
<p>It took me a long time try to figure it out, but I failed…  My goal is to convert my tractography to vtk format, then I can use WhiteMatterAnalysis for parcellation. And I want to know:</p>
<ol>
<li>Which coordinate system 3D slicer uses to load and display a nifiti image?</li>
<li>Which coordinate system VTK file could receive ?</li>
<li>Which coordinate system should I choose when sending a VTK file as a <code>model</code>? And what about as <code>Fiberbundles</code>?</li>
</ol>
<p>Anyone’ help will be very much appreciated!</p>
<p>Operating system: Ubuntu<br>
Slicer version: 5.0.3</p>

---

## Post #2 by @pieper (2023-11-17 14:00 UTC)

<p>We can’t really comment on what other software does with coordinates.  Slicer uses RAS for FiberBundles and stores them in the patient space defined by the DICOM headers of the source DWI scans.  If centering the volume on load was required, then whatever software created the tracts threw away the original patient space.  We really try to avoid doing that because it removes the ability to correlate with other scans, like structural of functional scans acquired in the same study.</p>

---

## Post #3 by @yi_yang (2023-11-18 14:28 UTC)

<p>Thanks for your reply! I finally deal with it by extracting b0 volume from the origin 4D volume (I forgot to check if 3D slicer can load 4D image <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20">). Actually I accidently found my T1w image was  symmetric with DWI in the AP direction, and I’m sure headers are the same. According to advice, I load 3D b0 DWI and it matched well with my vtk file achieved here:</p>
<blockquote>
<p>3.python vtk package:<br>
<a href="https://mail.python.org/pipermail/neuroimaging/2019-July/002006.html" rel="noopener nofollow ugc">reference here</a> In reference, a TRK file was loaded and converted,here I replaced with a TCK file.</p>
</blockquote>

---

## Post #4 by @sebastien_dam (2024-02-02 10:32 UTC)

<p>Hi!</p>
<p>I’m also trying to convert my streamlines from .tck to .vtk. I extracted the b0 volume and tried to follow the code you gave in reference. However, I cannot visualize any streamlines from the .vtk once converted (using <a href="https://med.inria.fr/" rel="noopener nofollow ugc">medInria</a>). Here is the snippet from which I call the function (which I did not touch):</p>
<pre><code class="lang-auto">fname="path/to/.tck"
reference="path/to/b0.nii.gz"
streams = load_tck(fname, reference)
streamlines = Streamlines(streams.streamlines)
saveStreamlinesVTK("sl.vtk")
</code></pre>
<p>Is it how you did too ? If not, would you mind sharing how you managed to obtain your .vtk streamlines ?</p>
<p>Thank you,</p>
<p>Sébastien</p>

---
