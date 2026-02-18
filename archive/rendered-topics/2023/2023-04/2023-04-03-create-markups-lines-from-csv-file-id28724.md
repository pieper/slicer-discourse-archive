# Create markups lines from .csv file

**Topic ID**: 28724
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/create-markups-lines-from-csv-file/28724

---

## Post #1 by @devD (2023-04-03 09:33 UTC)

<p>Hi,</p>
<p>I have a csv file with the columns ‘label’, ‘start’ and ‘end’. Where ‘start’ and ‘end’ are coordinates for a line. How can I in Python from this csv file create markups lines which corresponds to the ‘start’ and ‘end’ values and display them in Slicer. Furthermore, how can I change the color of each line?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2023-04-03 14:46 UTC)

<p>There are lots of examples of working with Markups in python here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups</a></p>

---

## Post #3 by @devD (2023-04-04 08:00 UTC)

<p>Thank you, I have solved this now. A new problem has arised, The csv file that I have is large with over 10000 rows (which should result in 10000 lines), I used the function “AddControlPointWorld” in order to make a markups line, however with this large amount of data the script gets really slow, is there any other faster way to create markups lines from a large csv file?</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2023-04-04 13:20 UTC)

<p>If you need to add more than a few dozens of points then do all that in a batch using StartModify/EndModify. If you show thousands of points then you may also consider disabling interactive picking and label display.</p>
<p>These are all demonstrated in this test:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Modules/Loadable/Markups/Testing/Python/AddManyMarkupsFiducialTest.py#L175-L202">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Modules/Loadable/Markups/Testing/Python/AddManyMarkupsFiducialTest.py#L175-L202" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Modules/Loadable/Markups/Testing/Python/AddManyMarkupsFiducialTest.py#L175-L202" target="_blank" rel="noopener">Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Modules/Loadable/Markups/Testing/Python/AddManyMarkupsFiducialTest.py#L175-L202</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="175" style="counter-reset: li-counter 174 ;">
          <li>markupsNode = slicer.mrmlScene.AddNewNodeByClass(nodeType)</li>
          <li>markupsNode.CreateDefaultDisplayNodes()</li>
          <li>if locked:</li>
          <li>    markupsNode.SetLocked(True)</li>
          <li>
          </li>
<li>if labelsHidden:</li>
          <li>    markupsNode.GetDisplayNode().SetPropertiesLabelVisibility(False)</li>
          <li>    markupsNode.GetDisplayNode().SetPointLabelsVisibility(False)</li>
          <li>
          </li>
<li>if usefewerModifyCalls:</li>
          <li>    print("Start modify")</li>
          <li>    mod = markupsNode.StartModify()</li>
          <li>
          </li>
<li>for controlPointIndex in range(numberOfControlPoints):</li>
          <li>    #    print "controlPointIndex = ", controlPointIndex, "/", numberOfControlPoints, ", r = ", r, ", a = ", a, ", s = ", s</li>
          <li>    t1 = time.process_time()</li>
          <li>    markupsNode.AddControlPoint(vtk.vtkVector3d(r, a, s))</li>
          <li>    t2 = time.process_time()</li>
          <li>    timeToAddThisFid = t2 - t1</li>
          <li>    dt = timeToAddThisFid - timeToAddLastFid</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/f368210d4a04db1eba0616f3ef88acafcd1ec1a2/Modules/Loadable/Markups/Testing/Python/AddManyMarkupsFiducialTest.py#L175-L202" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, if you don’t need labels and interaction then markups is not the right way to render the points. Instead, you can show them as glyphs in a model node. You can create a 3D model using a few lines of Python code (add your points into points of a polydata and turn the points into glyphs using <a href="https://vtk.org/doc/nightly/html/classvtkGlyph3D.html">vtkGlyph3D</a>) - probably ChatGPT can write the code for you but if you get stuck then let us know.</p>
<p>Reading and writing point coordinates in a text file is also very slow. You can read/write the file about 100x faster if you write into a binary format (e.g., PLY or VTK). It is sufficient to write out just the points, Slicer will read it as a VTK polydata, and you can easily apply the glyph filter in Slicer.</p>

---

## Post #5 by @devD (2023-04-06 10:26 UTC)

<p>Thank you for your reply.</p>
<p>I have managed to display a smaller amount of points (about 100) with both of the methods you have given me. But I still have the same problem.</p>
<p>Maybe I need to formulate my question a bit more detailed. I want to divide these 10000 points into groups of two, this since I want these groups to be displayed with different colors, so for example if I should do it with the first methods you presented to me, then I would assume that “numberOfNodes” would be 5000 and “numberOfControlPoints” would be 2, and then I could change the color of each node. The problem then is that it takes a really long time to execute the script and to create these nodes (the same would happen if i would make 5000 glyphs).</p>
<p>So my question now is if it is possible to display these data points and be able to individually change properties of each point (or in groups of two), so that at the end i will display these points with different colors?</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2023-04-06 11:25 UTC)

<p>Each node will increase the complexity of the screen, so adding hundreds of them will start to impact the performance.</p>
<p>You can use a single point list markup node to display 10000 points with two colors. You can use the “selected” property of the control points to set the group.</p>
<p>You do not need to write any custom script for all these. You can read the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-control-points-table-file-format-csv-tsv">CSV file containing point coordinates and “selected” flag</a> as a table and then import the table into a markup node using Markups module.</p>

---

## Post #7 by @devD (2023-05-04 08:43 UTC)

<p>Thank you, I managed to reduce the number of markup nodes to about 50 so everything worked fine.</p>
<p>Furthermore, I have a csv file which represents a vascular tree where each row in the file is a branch, which has an id and start and end coordinates for that branch. I wish to display this tree in the viewer. The tree consists of about 2000 branches. What is the best way to display this tree? I tried creating markup lines, however it seems that 3Dslicer has a hard time creating 2000 different markups lines. (Note, it is important to represent the branches as lines and not just nodes).</p>
<p>Thank you</p>

---

## Post #8 by @lassoan (2023-07-02 11:50 UTC)

<p>We usually display such trees using model nodes. You can add each branch as a line cell in a vtkPolyData object and then set that object into a model node.</p>
<p>What software creates the CSV file? Very likely it already has the option to save the tree in a standard mesh file format that you can load into Slicer for visualization as is.</p>

---
