---
topic_id: 14378
title: "How To Get Hu Values At Each Fiducial Points"
date: 2020-11-02
url: https://discourse.slicer.org/t/14378
---

# How to get HU values at each fiducial points

**Topic ID**: 14378
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/how-to-get-hu-values-at-each-fiducial-points/14378

---

## Post #1 by @MasatoshiOBA (2020-11-02 10:57 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11.20200930</p>
<p>How can I get the HU (CT) value at each fiducial placed on a model surface?<br>
I could convert vertices of an STL model to a group of fiducials as shown in the attached image.<br>
Then I would like to add another column next to the RAS coordinate table of the fiducial group.</p>
<p>Thank you for your assistance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfa248cbf2813c35a4c01c3ffab2791c2625734.jpeg" data-download-href="/uploads/short-url/zX5LXl2lTXScchasaMlaQuOcLmA.jpeg?dl=1" title="example1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfa248cbf2813c35a4c01c3ffab2791c2625734_2_690x436.jpeg" alt="example1" data-base62-sha1="zX5LXl2lTXScchasaMlaQuOcLmA" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfa248cbf2813c35a4c01c3ffab2791c2625734_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfa248cbf2813c35a4c01c3ffab2791c2625734_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbfa248cbf2813c35a4c01c3ffab2791c2625734_2_1380x872.jpeg 2x" data-dominant-color="9C9DA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example1</span><span class="informations">1447×915 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Expected behavior:</p>
<p>Actual behavior:</p>

---

## Post #2 by @MasatoshiOBA (2020-11-02 12:52 UTC)

<p>I would like to know how I can get HU values at multiple fiducial points in the same group.<br>
Ultimately, I’d like to get the HU values of the pixels corresponding to the vertices of the STL model placed in the CT volume data in a tabular format.</p>
<p>I was able to convert each vertex of the STL model to fiducial, as shown in the attached figure.</p>
<p>For these fiducial, is it possible to get the HU value and coordinate values of the pixels in which each of them is located in a table format?</p>
<p>I appriciate all supports from comunity members.</p>
<p><a href="/uploads/short-url/d4qVz1cWWlDjsyrf97wrxWjWuoB.jpeg">example|690x388</a></p>

---

## Post #3 by @lassoan (2020-11-02 19:27 UTC)

<p>You can sample a CT volume with at each point of a mesh using “Probe volume with model” module, and get the point coordinates and density values as numpy arrays by typing these into the Python console:</p>
<pre><code class="lang-auto">modelNode = getNode('Output Model')
coords = slicer.util.arrayFromModelPoints(modelNode)
densities = slicer.util.arrayFromModelPointData(modelNode, 'NRRDImage')
</code></pre>
<p>If you need the CT density values for FEM analysis then an STL file will not be sufficient, as it is a surface mesh, so it will not contain density information in the bone. You can generate a volumetric mesh from a segmentation using <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">SegmentMesher extension</a>.</p>

---

## Post #4 by @MasatoshiOBA (2020-11-03 07:41 UTC)

<p>Dear Andras Lasso.</p>
<p>Thank you for your kind reply. In addition, I would like to thank you for teaching me how to obtain the data for finite element analysis.</p>
<p>And I could get the list of coordinates of the model vertices. (I confirmed that by typing “print (coords)” in console window.)<br>
However, I only could get the error in your code line3.</p>
<p>It says</p>
<blockquote>
<blockquote>
<blockquote>
<p>modelNode = getNode(‘Dishreg3’)<br>
coords = slicer.util.arrayFromModelPoints(modelNode)<br>
densities = slicer.util.arrayFromModelPointData(modelNode, ‘ikeimage’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\MasatoshiOba\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 1293, in arrayFromModelPointData<br>
narray = vtk.util.numpy_support.vtk_to_numpy(arrayVtk)<br>
File “C:\Users\MasatoshiOba\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Lib\site-packages\vtkmodules\util\numpy_support.py”, line 216, in vtk_to_numpy<br>
typ = vtk_array.GetDataType()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetDataType’</p>
</blockquote>
</blockquote>
</blockquote>
<p>Is there something wrong with the way I installed Slicer?  Or am I specifying the files in my NRRDimage the wrong way?</p>

---

## Post #5 by @lassoan (2020-11-03 16:03 UTC)

<aside class="quote no-group" data-username="MasatoshiOBA" data-post="4" data-topic="14378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b487fb/48.png" class="avatar"> MasatoshiOBA:</div>
<blockquote>
<p>densities = slicer.util.arrayFromModelPointData(modelNode, ‘ikeimage’)</p>
</blockquote>
</aside>
<p>Can you try to use the code that I wrote above (‘NRRDImage’ instead of ‘ikeimage’)?</p>

---

## Post #6 by @MasatoshiOBA (2020-11-03 22:20 UTC)

<p>Thank you again.<br>
I tried that</p>
<blockquote>
<blockquote>
<blockquote>
<p>densities = slicer.util.arrayFromModelPointData(modelNode, ‘NRRDImage’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\MasatoshiOba\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py”, line 1293, in arrayFromModelPointData<br>
narray = vtk.util.numpy_support.vtk_to_numpy(arrayVtk)<br>
File “C:\Users\MasatoshiOba\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Lib\site-packages\vtkmodules\util\numpy_support.py”, line 216, in vtk_to_numpy<br>
typ = vtk_array.GetDataType()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetDataType’</p>
</blockquote>
</blockquote>
</blockquote>
<p>If I type<br>
print(modelNode) and print(coords) after I typed line 2, they return what I want.<br>
So something wrong with executing line3.</p>

---

## Post #7 by @lassoan (2020-11-03 22:44 UTC)

<p>Do you run this on the output of “Probe volume with model”?<br>
Do you see the ‘NRRDImage’ array in Models module Scalars section?</p>

---

## Post #8 by @MasatoshiOBA (2020-11-03 23:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="14378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you run this on the output of “Probe volume with model”?</p>
</blockquote>
</aside>
<blockquote>
<p>Do you run this on the output of “Probe volume with model”?</p>
</blockquote>
<p>Thank you so much, it resolved!<br>
I didn’t run “Probe volume with model” module first, and that was the reason of failure.</p>
<blockquote>
<blockquote>
<blockquote>
<p>modelNode = getNode(‘Output Model’)<br>
coords = slicer.util.arrayFromModelPoints(modelNode)<br>
densities = slicer.util.arrayFromModelPointData(modelNode, ‘NRRDImage’)<br>
print(densities)<br>
[ 376  320   83  541  523  420  488  537  364  508  532  260  168  244<br>
171  651  948  203  166  438  422  135   32  136  145  216  263   79<br>
471  252   42   15  493  620  492  537  428  537  573  117  287   35 …</p>
</blockquote>
</blockquote>
</blockquote>

---
