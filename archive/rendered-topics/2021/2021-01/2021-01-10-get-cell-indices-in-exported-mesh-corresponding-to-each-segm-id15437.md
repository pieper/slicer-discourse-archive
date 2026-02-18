# Get cell indices in exported mesh corresponding to each segment

**Topic ID**: 15437
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/get-cell-indices-in-exported-mesh-corresponding-to-each-segment/15437

---

## Post #1 by @Elijah_Alexson (2021-01-10 15:37 UTC)

<p>Dear 3D Slicer Team,</p>
<p>I have generated a volumetric heart mesh and now need to extract certain geometry information, that is I want to export indices of nodes on the epicardium, indices of nodes on the left ventricular surface and indices of nodes on the right ventricular surface and save them in three separate files. Is it possible to perform such extraction in the framework of 3D Slicer?</p>
<p>Thank you very much for your attention!</p>

---

## Post #2 by @lassoan (2021-01-10 16:04 UTC)

<p>This should be all doable, but how exactly depends on what would you like to do with it. What is your overall goal? Biomechanical analysis (FEM), electrophysiology mapping, volumetric analysis,…?</p>
<p>By “nodes” do you mean point indices? Have you separated the epicardium, left ventricle, and right ventricle in the segmentation (into different segments)?</p>

---

## Post #3 by @Elijah_Alexson (2021-01-10 16:33 UTC)

<p>Dear Andras,</p>
<p>Thank you for a quick reply. My overall goal is to run a model of myocardial ischemia with heart-torso mesh. Those indices are required for computational reasons (used by mesh constructor and for some algorithm implementation).</p>
<p>Yes, indeed. By “nodes” I mean “points”, so “node index” equals “point index”.</p>
<p>I have not separated epi, lv and rv in the segmentation yet, but will positively do!</p>

---

## Post #4 by @lassoan (2021-01-10 19:29 UTC)

<aside class="quote no-group" data-username="Elijah_Alexson" data-post="3" data-topic="15437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elijah_alexson/48/9488_2.png" class="avatar"> Elijah_Alexson:</div>
<blockquote>
<p>run a model</p>
</blockquote>
</aside>
<p>What kind of model? Biomechanical, electrophysiology, geometrical, visualization? Do you need surface or volumetric mesh? If surface mesh then open or closed?</p>

---

## Post #5 by @Elijah_Alexson (2021-01-10 21:32 UTC)

<p>It is an electrophysiological model. I need a volumetric mesh (Tetgen format).</p>

---

## Post #6 by @lassoan (2021-01-11 06:33 UTC)

<p>You can create the mesh you need by segmenting each structure as a separate segment (see for example this <a href="https://youtu.be/BJoIexIvtGo">tutorial</a>) and then generate volumetric mesh using <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">Segment Mesher</a> extension. I would recommend Cleaver over Tetgen as it works directly from the labelmap image and you don’t need to go through surface mesh representation. Cleaver can output tetgen file format directly.</p>
<p>What software do you use for the EP modeling?</p>

---

## Post #7 by @Elijah_Alexson (2021-01-11 12:35 UTC)

<p>Sure, that’s the way I usually do, and I use Cleaver over Tetgen as well.</p>
<p>For the EP modelling I use <a href="http://www.cs.ox.ac.uk/chaste/" rel="noopener nofollow ugc">Chaste</a>. It uses Tetgen format, so after mesh generation (using Segment Mesher) I convert resulting |.vtk| file into |.node|, |.ele|, |.face| files using script provided with Chaste.</p>

---

## Post #8 by @Elijah_Alexson (2021-01-11 15:31 UTC)

<p>By the way, I have separated epi, lv and rv into different segments in the segmentation and generated a volumetric mesh using Segment Mesher. What should be the next step to obtain the respective indices?</p>

---

## Post #9 by @lassoan (2021-01-11 18:10 UTC)

<p>I know that in VTK file output of segment mesher there is a cell array that specifies which cell belong to which input segment. Probably something like that exists in the tetgen output, too.</p>

---

## Post #11 by @Elijah_Alexson (2021-01-11 22:53 UTC)

<p>Yes, indeed. There is an array that specifies which cell belongs to which input segment but it is not of any use since any array looks like this<br>
<em>…</em><br>
<em>2 2 2 2 2 2 1 1 1</em><br>
<em>1 3 3 3 3 3 3 3 1</em><br>
<em>3 3 3 3 3 3 3 1 1</em><br>
<em>…</em><br>
Furthermore, I need to know which <strong>point</strong> belongs to which input segment but, unfortunately, VTK file output does not contain that information.</p>
<p>If I reformulate my basic question, it will sound like this. For instance, a biventricular model consists of 300k points (and of some number of cells). I need to know that, shall we say, epicardium includes points [1; 70k], left ventricular surface includes points [70001; 85k], right ventricular surface includes points [85001; 100k] and everything else includes points [100001; 200k]. Is there a way to extract such data?</p>

---

## Post #12 by @lassoan (2021-01-11 23:39 UTC)

<aside class="quote no-group" data-username="Elijah_Alexson" data-post="11" data-topic="15437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elijah_alexson/48/9488_2.png" class="avatar"> Elijah_Alexson:</div>
<blockquote>
<p>Furthermore, I need to know which <strong>point</strong> belongs to which input segment but, unfortunately, VTK file output does not contain that information.</p>
</blockquote>
</aside>
<p>In general, points are shared between cells, so segment identifier in a volumetric mesh can only be cell data.</p>
<aside class="quote no-group" data-username="Elijah_Alexson" data-post="11" data-topic="15437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elijah_alexson/48/9488_2.png" class="avatar"> Elijah_Alexson:</div>
<blockquote>
<p>I need to know that, shall we say, epicardium includes points [1; 70k], left ventricular surface includes points [70001; 85k], right ventricular surface includes points [85001; 100k] and everything else includes points [100001; 200k]. Is there a way to extract such data?</p>
</blockquote>
</aside>
<p>Yes, of course, you can do this.</p>
<p>The straightforward implementation would be to get all the cell IDs corresponding to a segment, for example using numpy functions (e.g., <code>np.where</code>) then get point IDs of those cells using VTK methods.</p>
<p>If you have tens of thousands of cells then iterating through all of them in Python would be probably too slow. So, a smarter method would be this:</p>
<ul>
<li>add original point and cell IDs to the result mesh using <a href="https://vtk.org/doc/nightly/html/classvtkIdFilter.html">vtkIdFilter</a></li>
<li>Extract each submesh corresponding to a segment using thresholding (see <a href="https://github.com/lassoan/SlicerSegmentMesher#split-mesh-to-submeshes">example code</a>)</li>
<li>Retrieve point or cell IDs from each submesh (thresholding changes the cell and point IDs, but the original IDs are available in the scalar array that you added using vtkIdFilter)</li>
</ul>

---

## Post #13 by @Elijah_Alexson (2021-01-12 02:07 UTC)

<p>Thank you, I’ll try that.</p>
<p>In case I got completely stuck, would there be a simpler method with using masks, for example?</p>

---

## Post #14 by @lassoan (2021-01-12 03:14 UTC)

<p>The second method that I described is probably 2-3 magnitudes faster then the naive implementation (using for loops in Python, taking fraction of a second instead of minutes) and probably less than 20 lines of code in total (and 10 lines is already available in the example that I gave above). There is nothing Slicer specific, it is just connecting a few VTK filters from Python. Give it a try and let us know if you get stuck.</p>

---

## Post #15 by @Elijah_Alexson (2021-01-13 15:54 UTC)

<p>Dear Andras,</p>
<p>I also found another solution. It is rather similar to what you’ve suggested but can be performed directly in ParaView using Data Analysis. To do so, one should import a volumetric mesh in VTK format into ParaView and then use the relative filters. It might be done through scripting interface and takes less than 20 lines of code as well.</p>
<p>Thank you for a very helpful conversation!</p>

---

## Post #16 by @lassoan (2021-01-13 19:00 UTC)

<p>Both ParaView and Slicer uses the exact same underlying library (VTK) for manipulating meshes, so you can use either software for processing or visualizing meshes. ParaView has more mesh manipulation and visualization features than Slicer, but it is very limited in what it can do with images, transforms, and markups.</p>

---
