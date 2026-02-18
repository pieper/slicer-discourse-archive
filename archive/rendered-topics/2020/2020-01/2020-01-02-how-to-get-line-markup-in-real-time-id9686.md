# How to get line markup in real time?

**Topic ID**: 9686
**Date**: 2020-01-02
**URL**: https://discourse.slicer.org/t/how-to-get-line-markup-in-real-time/9686

---

## Post #1 by @RayCui (2020-01-02 10:04 UTC)

<p>I want to mark a certain section of blood vessels with some attribute. I thought I could draw line by Markup line widget to get the position of vessels. And read some value of attribues from ComboBox. Finally show the result to table viewer and can save the table with csv format. Some questions occured to me:</p>
<ol>
<li>How can I get Line Markup in real time? That’s means, if I draw a line in current data view, the coordinates of line’s two points can send to table viewer in time.</li>
<li>How can I save the table data with csv format from table viewer ?</li>
</ol>
<p>Many thanks.</p>

---

## Post #2 by @adamrankin (2020-01-02 15:13 UTC)

<ol>
<li>Add an observer to the markup node<br>
Example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function</a><br>
Markup node events:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#a14f8e398ba642299e120de065c0c7dd6a3f3703f43e61e8a3e411cc18278dfda1" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#a14f8e398ba642299e120de065c0c7dd6a3f3703f43e61e8a3e411cc18278dfda1</a>
</li>
<li>Get table model:</li>
</ol>
<pre><code class="lang-python">lm = slicer.app.layoutManager()
tw = lm.tableWidget(0)
tv = tw.tableView()
model = tv.tableModel()
</code></pre>
<p>Output to csv:<br>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/27353026/qtableview-output-save-as-csv-or-txt" target="_blank" rel="nofollow noopener">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/3534854/ricoricochet" target="_blank" rel="nofollow noopener">
    <img alt="RicoRicochet" src="https://i.stack.imgur.com/sDiKU.jpg?s=128&amp;g=1" class="thumbnail onebox-avatar" width="60" height="60">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/27353026/qtableview-output-save-as-csv-or-txt" target="_blank" rel="nofollow noopener">QTableView output save as .csv or .txt</a>
</h4>

<div class="tags">
  <strong>c++, qt, csv, qt4</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/3534854/ricoricochet" target="_blank" rel="nofollow noopener">
    RicoRicochet
  </a>
  on <a href="https://stackoverflow.com/questions/27353026/qtableview-output-save-as-csv-or-txt" target="_blank" rel="nofollow noopener">07:08AM - 08 Dec 14 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @RayCui (2020-01-07 02:39 UTC)

<p>Thank you. <a class="mention" href="/u/adamrankin">@adamrankin</a><br>
Follow your first advice, I add an observer(slicer.vtkMRMLMarkupsNode.PointModifiedEvent) to a vtkMRMLMarkupsLineNode. This can get Line’s two points position when draw a new line in the viewer. But this seem to only can get one line, and I want to get the newly drawn line continuously. Can I add an observer to a volume node that observe whether new vtkMRMLMarkupsLineNode is creating, and this will create a markup folder that contain all markup line node? And also all new LineNode is belong to the volume data, When I switch to another volume node, the observer will switch to a new markup folder.</p>
<p>About table, I found that 3D Slicer supports vtkMRMLTableNode. I realize that can solve my problem. Table can show in the viewer, and I can utilize the data node management in Slicer. There are new problems. How can I bind the table node to the markup folder mentioned above? This means that the table node will be updated when the makup folder changes.</p>
<p>Do you have any suggestions on these questions? Looking forward to your reply.</p>

---
