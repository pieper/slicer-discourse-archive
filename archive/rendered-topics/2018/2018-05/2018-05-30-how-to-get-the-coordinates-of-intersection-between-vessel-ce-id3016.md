# How to get the coordinates of intersection between vessel centerline and sequential MRI/CT slices in markup fiducials?

**Topic ID**: 3016
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/how-to-get-the-coordinates-of-intersection-between-vessel-centerline-and-sequential-mri-ct-slices-in-markup-fiducials/3016

---

## Post #1 by @shahrokh (2018-05-30 12:10 UTC)

<p>Hi Dear developers and users</p>
<p>In the phantom study, I can segment vessel containing contrast agents in MRI and CT images using the option of “Level Set Segment” in the module of “Vascular Modeling Toolkit” with two points (start and end points of vessel).</p>
<p>Using “Centerline Computation” option in this module, I can get centerlines in MRI and CT.</p>
<p>I can do these steps successfully.</p>
<p>At now, I want to get the coordinates of intersection between <em>MRI/CT vessels centerlines</em> <strong>and</strong> <em>MRI/CT slices (plans)</em> in “markup fiducials” format. How can I do it?</p>
<p>Eventually, I want get “B-Spline Transform” from these two sets of fiducials using “ScatteredTranform” module.</p>
<p>Please guide me.<br>
Thenks a lot,<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-05-30 12:50 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="3016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>At now, I want to get the coordinates of intersection between <em>MRI/CT vessels centerlines</em> <strong>and</strong> <em>MRI/CT slices (plans)</em> in “markup fiducials” format. How can I do it?</p>
</blockquote>
</aside>
<p>You get point coordinates of the centerline using <a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util"><code>slicer.util.arrayFromModelPoints()</code></a>, the slice plane position and orientation using <a href="http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html#a888f4614c00f350f4440ac9bde8a3a6d"><code>sliceNode.GetSliceToRAS()</code></a> and compute intersection using Python/numpy (for example, you can transfer all the point coordinates to the slice plane’s coordinate system by a single numpy matrix multiplication and you know the slice intersects the line between the two points where the z coordinate changes sign).</p>

---

## Post #3 by @lassoan (2018-05-30 13:08 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="3016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>Eventually, I want get “B-Spline Transform” from these two sets of fiducials using “ScatteredTranform” module.</p>
</blockquote>
</aside>
<p>That works, as long as you can define a list of corresponding points.</p>
<p>Alternatively, you can get a fully automatic registration by computing a distance map from the model using <a href="https://www.vtk.org/doc/nightly/html/classvtkImplicitModeller.html">vtkImplicitModeller</a> for both vessel trees and register the distance map images using “General registration (BRAINS)” module or SlicerElastix extension.</p>

---

## Post #4 by @shahrokh (2018-05-30 14:38 UTC)

<p>Dear Andras,<br>
Thanks a lot for your reply.</p>
<p>I’m sorry to ask this question.<br>
I try to do your guidance, but I don’t success.<br>
I create “LevelSetSegmentationModel” in the module of “Level Set Segmentation”  with these properties:<br>
Mesh Type: Surface Mesh (vtkPolyData)<br>
Points: 3530<br>
Cells: 1054<br>
Visible: YES</p>
<p>I open “Python Interactor” and type the following command and get the error message:<br>
Python 2.7.13 (default, Dec 20 2017, 00:16:35)<br>
[GCC 4.6.4] on linux2</p>
<blockquote>
<blockquote>
<blockquote>
<p>a = slicer.util.arrayFromModelPoints(‘LevelSetSegmentationModel’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/sn/Slicer-4.8.1-linux-amd64/bin/Python/slicer/util.py”, line 730, in arrayFromModelPoints<br>
pointData = modelNode.GetPolyData().GetPoints().GetData()<br>
AttributeError: ‘str’ object has no attribute ‘GetPolyData’</p>
</blockquote>
</blockquote>
</blockquote>
<p>What’s wrong i do<br>
Thanks a lot.</p>

---

## Post #5 by @lassoan (2018-05-30 14:39 UTC)

<p>slicer.util.arrayFromModelPoints input argument is a node object, not a node name. Something like this should work:</p>
<pre><code>a = slicer.util.arrayFromModelPoints(slicer.util.getNode('LevelSetSegmentationModel'))</code></pre>

---

## Post #6 by @shahrokh (2018-07-04 13:04 UTC)

<p>Dear Andras</p>
<p>I have divided into three steps of the solution that you proposed<br>
Step <span class="hashtag-raw">#1:</span> Get point coordinates of the centerline<br>
Step <span class="hashtag-raw">#2:</span> Get the slice plane position and orientation<br>
Step <span class="hashtag-raw">#3:</span> compute intersection</p>
<p>I can do step <span class="hashtag-raw">#1</span>. Thanks a lot for your guidance. I can get points coordinates of the centerline by two methods:<br>
Method A: Using command suggested by you.<br>
The output I recevied is the following lines:</p>
<blockquote>
<blockquote>
<blockquote>
<p>a = slicer.util.arrayFromModelPoints(slicer.util.getNode(‘CenterlineComputationModel’))<br>
a<br>
array([[ 145.84095764,   35.16293335, -164.67481995],<br>
[ 145.79029846,   35.13619995, -164.64332581],<br>
[ 145.7636261 ,   35.12333679, -164.63772583],<br>
[ 145.73847961,   35.11413574, -164.63140869],<br>
[ 145.71414185,   35.10810852, -164.62069702],<br>
[ 145.67230225,   35.09657669, -164.61920166],<br>
[ 145.61857605,   35.08124542, -164.6227417 ],<br>
[ 145.55818176,   35.0341835 , -164.62219238],<br>
[ 145.47712708,   34.97132111, -164.60922241],<br>
[ 145.36305237,   34.89616394, -164.60148621],<br>
[ 145.14250183,   34.80304337, -164.60087585],<br>
…<br>
[ 136.29968262,   30.57961273,  119.75666809],<br>
[ 136.34971619,   30.54818153,  122.34375   ],<br>
[ 135.77685547,   31.20230293,  124.76610565]], dtype=float32)<br>
Thanks a lot.</p>
</blockquote>
</blockquote>
</blockquote>
<p>Method B: Saving the model of CenterlineComputationModel in vtk file format and open it with text editor. After opening it, I get the following lines inside it:<br>
<code># vtk DataFile Version 4.1</code><br>
vtk output SPACE=RAS<br>
ASCII<br>
DATASET POLYDATA<br>
POINTS 154 float<br>
145.841 35.1629 -164.675 145.79 35.1362 -164.643 145.764 35.1233 -164.638<br>
…<br>
LINES 1 155<br>
154 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153</p>
<p>CELL_DATA 1<br>
FIELD FieldData 1<br>
Topology 2 1 vtkIdType<br>
0 -1<br>
POINT_DATA 154<br>
FIELD FieldData 1<br>
Radius 1 155 double<br>
0 0.93539859067 0.98169177679 1.0529773639 1.1399722485 1.1279945604 1.1710665096 1.3120489148 1.4790625398<br>
1.5613531004 1.5827807416 1.6833454452 1.7331424374 2.4758003289 2.6843646662 2.8318936472 3.0226237442 3.1406634818<br>
3.2299563772 3.3291342158 3.4065516712 3.4812218855 3.558130136 3.6033167794 3.6237193518 3.6420448546 3.6487910235<br>
3.646756415 3.5671632296 3.5345197373 3.6156178149 3.5892311481 3.5454585256 3.5587859741 3.5451988961 3.5659671104<br>
3.5970395968 3.5993437286 3.5626123183 3.5145199888 3.5082920872 3.4765511836 3.3688799134 3.2587559158 3.3173820849<br>
3.3570698617 3.3823053885 3.3323261841 3.3323714364 3.3222690597 3.3258639488 3.3141974444 3.3740845854 3.42227061<br>
3.2932157077 3.1946814846 3.2159209807 3.1234082138 3.0537192217 3.0307876127 3.0736387129 3.1069941974 3.0766833051<br>
3.0464739868 3.0470545098 3.0403655054 3.0116313169 2.9762177261 2.9530425806 2.9602956388 2.9723236359 2.9816882739<br>
2.9728061364 3.0028494712 3.0220091921 3.0711024311 3.1281029641 3.1463048167 3.1366392897 3.1243575617 3.1142074113<br>
3.091457596 3.1092488591 3.1247486255 3.148610963 3.1402409044 3.1902634973 3.2695987862 3.2484048694 3.2246822741<br>
3.2381049868 3.2107577731 3.18916461 3.1834670934 3.192502973 3.2030683332 3.1314524702 3.0870774828 3.0907511031<br>
3.1300404681 3.1447023816 3.1515719341 3.174958119 3.2599369918 3.2984029753 3.2512564972 3.2030528764 3.2006250886<br>
3.1825085274 3.1688352282 3.1323133657 3.1304085566 3.1367795013 3.1228499729 3.1093491959 3.1121296408 3.0806374244<br>
3.0769638698 3.1159708757 3.1032157933 3.0952879332 3.0613003183 3.0197624449 2.9648909979 2.9569908614 2.9897127257<br>
3.0154655444 3.006690353 3.0511237927 3.0857934121 3.1663394771 3.2151247818 3.275425932 3.3145827323 3.3759095419<br>
3.4072440224 3.3584509736 3.3152342845 3.3968093267 3.4845161645 3.541514986 3.4447521872 3.396156225 3.4341717148<br>
3.4326186044 3.3588751135 3.3161116196 3.322315096 3.3851967338 3.3531960108 3.1299476549 2.8655719345 2.1236473996<br>
1.4558911076 0</p>
<p>At now, I have some questions about these lines in CenterlineComputationModel.vtk file.<br>
<strong>Question</strong> 1: I expected that I have the coordinates of the points (as mentioned above POINTS 154) that are equal to the number of MRI axial slices (173 slices, image dimensions: 512<code>*</code>512<code>*</code>173). Why not?</p>
<p><strong>Question</strong> 2: In CenterlineComputationModel.vtk file, I see the following data:<br>
Radius 1 155 double<br>
0 0.93539859067 0.98169177679 1.0529773639 1.1399722485 1.1279945604 1.1710665096 1.3120489148 1.4790625398<br>
…<br>
What are these numbers?<br>
Can these numbers be related to slice plane position and orientation?</p>
<p>In continue…<br>
At now, I am in the second step.<br>
You mentioned that I must use sliceNode.GetSliceToRAS() to get slice plane position and orientation. For doing it, I refer to reply you in <a href="https://discourse.slicer.org/t/2d-views-and-3d-model-transformation/2920" class="inline-onebox">2D views and 3D model transformation</a>. I enter the following commands:<br>
liceViewName = slicer.app.layoutManager().sliceViewNames()[0]<br>
sliceToRAS = slicer.app.layoutManager().sliceWidget(sliceViewName).sliceLogic().GetSliceNode().GetSliceToRAS()<br>
print(sliceToRAS)</p>
<p>Unfortunately, I do not understand to use GetSliceToRAS method for getting the slice plane position and orientation.</p>
<p><strong>Last question</strong>:<br>
How can I save the output of the following command in Python Interactor in a csv file?</p>
<blockquote>
<blockquote>
<blockquote>
<p>a = slicer.util.arrayFromModelPoints(slicer.util.getNode(‘CenterlineComputationModel’))</p>
</blockquote>
</blockquote>
</blockquote>
<p>In other words, what command should I use to do it in Python Interactor?</p>
<p>Please guide me,<br>
Thanks a lot.<br>
Shahrokh</p>

---
