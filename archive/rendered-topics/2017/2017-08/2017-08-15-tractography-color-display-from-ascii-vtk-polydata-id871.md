# Tractography color display from ASCII .vtk Polydata

**Topic ID**: 871
**Date**: 2017-08-15
**URL**: https://discourse.slicer.org/t/tractography-color-display-from-ascii-vtk-polydata/871

---

## Post #1 by @bartbols (2017-08-15 11:58 UTC)

<p>Hi,</p>
<p>I’m trying to visualize some fibre tracts in 3D slicer form a ASCII vtkPolydata file that I generate through Matlab. The file reads in well and displays the fibres in the correct position, however, I cannot assign colors based on the scalar-values assigned to each line segment (as defined in the .vtk Polydata file). In the ‘Tractography display’ module my scalar variable is recognized because it shows up in the dropdown list next to “Of scalar value”, but when I select it the color does not change. I’m wondering if I haven’t defined the color-specs correctly in my VTK file, or if this is a (known?) bug in 3D slicer. I’ve copied an example .vtk ASCII file below (copy/paste it into a text editor and save with extension .vtk, then open in 3D slicer). I’m using Slicer 4.5.0-1 r24735.</p>
<p>Any help is greatly appreciated!</p>
<p>Bart</p>
<h1>vtk DataFile Version 3.0</h1>
<p>example data<br>
ASCII<br>
DATASET POLYDATA<br>
POINTS 46 float<br>
-73.482 69.594 181.997<br>
-73.848 69.446 181.078<br>
-74.203 69.283 180.157<br>
-74.529 69.070 179.236<br>
-74.835 68.828 178.316<br>
-75.134 68.577 177.395<br>
-75.422 68.322 176.472<br>
-75.701 68.057 175.549<br>
-75.976 67.788 174.626<br>
-76.254 67.515 173.705<br>
-76.540 67.246 172.785<br>
-76.852 66.976 171.874<br>
-77.198 66.704 170.977<br>
-77.581 66.431 170.094<br>
-77.987 66.159 169.221<br>
-78.392 65.887 168.349<br>
-78.807 65.611 167.481<br>
-79.226 65.332 166.617<br>
-79.634 65.049 165.749<br>
-80.027 64.759 164.877<br>
-82.538 67.717 165.874<br>
-82.298 67.992 166.805<br>
-82.054 68.267 167.735<br>
-81.816 68.547 168.665<br>
-81.588 68.831 169.596<br>
-81.360 69.115 170.528<br>
-81.127 69.398 171.458<br>
-80.886 69.680 172.387<br>
-80.633 69.958 173.313<br>
-80.359 70.228 174.236<br>
-80.084 70.499 175.159<br>
-79.790 70.760 176.078<br>
-79.476 71.008 176.995<br>
-79.146 71.238 177.910<br>
-78.813 71.446 178.830<br>
-78.486 71.622 179.758<br>
-78.161 71.769 180.693<br>
-77.835 71.884 181.631<br>
-77.509 71.967 182.573<br>
-77.176 72.021 183.514<br>
-76.845 72.057 184.457<br>
-76.517 72.079 185.401<br>
-76.233 72.049 186.360<br>
-75.978 71.990 187.325<br>
-75.754 71.913 188.296<br>
-75.541 71.810 189.268</p>
<p>LINES 2 48<br>
20 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>
26 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45</p>
<p>CELL_DATA 2<br>
SCALARS scalar_value int 1<br>
LOOKUP_TABLE my_table<br>
2<br>
2<br>
LOOKUP_TABLE my_table 8<br>
0.2 0.8 0.4 0.0<br>
0.8 0.1 0.5 0.9<br>
0.9 1.0 0.9 0.3<br>
1.0 0.7 0.3 0.1<br>
0.2 0.3 0.8 0.7<br>
0.5 0.4 0.4 0.4<br>
0.9 0.0 0.8 0.7<br>
0.6 0.7 0.0 0.3</p>

---

## Post #2 by @ljod (2017-08-15 15:02 UTC)

<p>Hi you are seeing the expected behavior. Currently the support is for coloring point data, not cell data, since that is the typical use case (e.g. color by FA at all points on the polyline or fiber). You can easily store your desired scalars as point data (one scalar per point) instead of cell data (one scalar per line). Also, in your vtk example, I don’t actually see any scalar array data, so that can be another issue. There is no need to include a lookup table, since you can choose from the options in Slicer for lookup color options.</p>

---

## Post #3 by @bartbols (2017-08-15 22:32 UTC)

<p>Ok, that works! Thanks!<br>
Is it also possible to append multiple scalar sets to the same point dataset, so you can then select from the dropdown menu in Slicer which value you want to display? I’ve only figured out how to append one scalar so far.<br>
Bart</p>

---

## Post #4 by @lassoan (2017-08-15 23:15 UTC)

<p>Yes, you can add any number of scalars and choose which one to display in the Scalars section of Models module.</p>

---

## Post #5 by @bartbols (2017-08-16 00:01 UTC)

<p>Ok, so how do you add that to the vtk file then? When I append something like this at the end of the ASCII-file, it only reads in scalar1:</p>
<p>POINT_DATA 40<br>
SCALARS scalar1 float 1<br>
LOOKUP_TABLE default</p>
<p>POINT_DATA 40<br>
SCALARS scalar2 float 1<br>
LOOKUP_TABLE default</p>
<p>Any suggestions on how to also get scalar2 to show up in Slicer?<br>
Bart</p>

---

## Post #6 by @lassoan (2017-08-16 02:32 UTC)

<p>You can choose which scalar to display in the Scalars section of Models module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d967661055ccace8b17055c3dde43d11ad136c7e.png" data-download-href="/uploads/short-url/v1f8MTv4neZHR5HSxBbX9JdwuFE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d967661055ccace8b17055c3dde43d11ad136c7e_2_690x458.png" alt="image" data-base62-sha1="v1f8MTv4neZHR5HSxBbX9JdwuFE" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d967661055ccace8b17055c3dde43d11ad136c7e_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d967661055ccace8b17055c3dde43d11ad136c7e_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d967661055ccace8b17055c3dde43d11ad136c7e_2_1380x916.png 2x" data-dominant-color="C7C6DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1750×1163 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There are lots of sample data sets in <a href="https://github.com/naucoin/VTKData/tree/master/Data" class="inline-onebox">VTKData/Data at master · naucoin/VTKData · GitHub</a></p>
<p>For example, this data set has lots of scalars: <a href="https://raw.githubusercontent.com/naucoin/VTKData/master/Data/blow.vtk">https://raw.githubusercontent.com/naucoin/VTKData/master/Data/blow.vtk</a></p>

---

## Post #7 by @bartbols (2017-08-16 05:12 UTC)

<p>Hi Andras,<br>
thanks for your response again. I understand how I should be able to select a different scalar, but the problem is that only the first scalar defined in my .vtk file shows up. The other scalars do not appear in the dropdown menu. There is no error when loading the file. Also, when I open the file in ParaView it does detect all the scalars, which makes me think there’s something wrong with 3D slicer’s vtkreader.</p>
<p>For example, in the following file, only ‘scalar1’ shows up. Is my syntax wrong?</p>
<h1>vtk DataFile Version 3.0</h1>
<p>Title<br>
ASCII<br>
DATASET POLYDATA<br>
POINTS 24 float<br>
-84.232 52.932 175.120<br>
-87.560 56.327 181.491<br>
-88.757 57.499 183.553<br>
-90.092 58.723 185.504<br>
-91.515 59.973 187.384<br>
-92.980 61.223 189.239<br>
-94.440 62.448 191.110<br>
-95.847 63.620 193.040<br>
-97.154 64.714 195.073<br>
-98.313 65.703 197.252<br>
-99.278 66.563 199.618<br>
-107.554 74.195 223.673<br>
-75.512 59.065 109.771<br>
-75.664 59.053 109.885<br>
-77.933 58.896 111.714<br>
-80.054 58.804 113.678<br>
-82.043 58.783 115.758<br>
-83.915 58.839 117.936<br>
-85.689 58.980 120.195<br>
-87.381 59.212 122.517<br>
-89.006 59.542 124.882<br>
-90.582 59.975 127.275<br>
-92.126 60.520 129.675<br>
-93.754 61.160 132.225</p>
<p>LINES 2 26<br>
12 0 1 2 3 4 5 6 7 8 9 10 11<br>
12 12 13 14 15 16 17 18 19 20 21 22 23<br>
POINT_DATA 24<br>
SCALARS scalar1 float<br>
LOOKUP_TABLE default<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
58.538<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
29.324<br>
SCALARS scalar2 float<br>
LOOKUP_TABLE default<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
14.789<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250<br>
35.250</p>

---

## Post #8 by @bartbols (2017-08-16 05:44 UTC)

<p>UPDATE: issue resolved</p>
<p>After upgrading to the latest Slicer version (4.7.0) it does recognise all the scalars stored in the vtk-file. So it was a problem with my previous Slicer version (4.5) which has been resolved now.<br>
Bart</p>

---
