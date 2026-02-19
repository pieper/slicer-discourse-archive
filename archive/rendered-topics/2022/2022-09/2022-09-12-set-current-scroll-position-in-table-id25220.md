---
topic_id: 25220
title: "Set Current Scroll Position In Table"
date: 2022-09-12
url: https://discourse.slicer.org/t/25220
---

# Set current scroll position in table

**Topic ID**: 25220
**Date**: 2022-09-12
**URL**: https://discourse.slicer.org/t/set-current-scroll-position-in-table/25220

---

## Post #1 by @rhodesdante (2022-09-12 16:49 UTC)

<p>I am in the process of creating a custom Python module. When the user clicks on a volume, a table is loaded and shown corresponding to that volume. The tables have many columns, and I would like to initialize this process so that the top of a table view is set (scrolled down) to a specific, predetermined row. For example, a user clicks on a volume, and it brings up a table view, but the top of the view is initialized to the 3rd row, rather than the first.</p>
<p>The module logic contains a table view: “<a href="http://self.tv" rel="noopener nofollow ugc">self.tv</a> = slicer.qmrmlTableView()”, and I would imagine this capability is available in one of its “set” functions, using something like<br>
“self.tv.SETCURRENTROW(3)”<br>
but I could not seem to find such a functionality. Any help on this issue would be greatly appreciated. Thank you!</p>

---

## Post #2 by @rhodesdante (2022-09-16 17:07 UTC)

<p>In addition, is it possible to set the colors of a given cell? I saw there was a “setCellText” function for a table node, but I was not able to find a similar function for color. If any additional information/code would be helpful for this and the above please let me know! I would be happy to provide it. Thanks!</p>

---

## Post #3 by @pieper (2022-09-16 18:12 UTC)

<p><code>qmrmlTableView</code> is a <a href="https://doc.qt.io/qt-5/qtableview.html"><code>QTableView</code></a> so you have a lot of options for controlling the content, display, and style either with the view or the model.</p>

---

## Post #4 by @lassoan (2022-09-16 20:16 UTC)

<aside class="quote no-group" data-username="rhodesdante" data-post="2" data-topic="25220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> rhodesdante:</div>
<blockquote>
<p>I saw there was a “setCellText” function for a table node, but I was not able to find a similar function for color</p>
</blockquote>
</aside>
<p>qMRMLTableView displays content of a color node. You can modify the color name in the MRML node to change the displayed text in the table.</p>

---

## Post #5 by @rhodesdante (2022-09-19 15:27 UTC)

<p>Thank you both for your responses! I am going to try the using the color node route if possible, and regardless of how I solve this, I will make sure to post my solution here.<br>
I had a follow up for <a class="mention" href="/u/lassoan">@lassoan</a><br>
I wanted to clarify that what I am trying to do is change the background color of a specific cell, as opposed to the text color. I could not find the color node associated with my qMRMLTableView. I see that there are some “vtkColorTableNodes” in the subject hierarchy. However, when I went through the member functions of the qMRMLTableNode, I could not find anything that seemed like it would get the color node with which it is associated. What is the best way I can access/modify the color node that the qMRMLTableView displays? Thanks again!</p>

---

## Post #6 by @rhodesdante (2022-09-19 16:17 UTC)

<p>I decided I would also try <a class="mention" href="/u/pieper">@pieper</a> 's approach in the meantime. However, I’m not sure if I’m missing something. I posted my code below. Is there some signal I would have to send? I’m new to Qt. Thanks again–I really appreciate all your help!</p>
<p>% tv = my qMRMLTableView<br>
model = tv.tableModel()<br>
item = qt.QStandardItem()<br>
brush = qt.QBrush()<br>
brsh.setColor(qt.QColor(0,255,0))<br>
item.setBackground(brush)<br>
tv.tableModel().setItem(1,1, item)</p>

---

## Post #7 by @pieper (2022-09-19 17:50 UTC)

<p>Here’s an example from some older code of manually setting colors.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/v4.10.2/Modules/Scripted/EditorLib/ColorBox.py#L75-L128">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/v4.10.2/Modules/Scripted/EditorLib/ColorBox.py#L75-L128" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/v4.10.2/Modules/Scripted/EditorLib/ColorBox.py#L75-L128" target="_blank" rel="noopener">Slicer/Slicer/blob/v4.10.2/Modules/Scripted/EditorLib/ColorBox.py#L75-L128</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="75" style="counter-reset: li-counter 74 ;">
          <li>def addRow(self,c):</li>
          <li>  name = self.colorNode.GetColorName(c)</li>
          <li>  lut = self.colorNode.GetLookupTable()</li>
          <li>  rgb = lut.GetTableValue(c)</li>
          <li>  brush = qt.QBrush()</li>
          <li>  self.brushes.append(brush)</li>
          <li>  color = qt.QColor()</li>
          <li>  color.setRgb(rgb[0]*255,rgb[1]*255,rgb[2]*255)</li>
          <li>  brush.setColor(color)</li>
          <li>
          </li>
<li>  # index</li>
          <li>  item = qt.QStandardItem()</li>
          <li>  item.setText(str(c))</li>
          <li>  self.model.setItem(self.row,0,item)</li>
          <li>  self.items.append(item)</li>
          <li>  # color</li>
          <li>  item = qt.QStandardItem()</li>
          <li>  item.setData(color,1)</li>
          <li>  self.model.setItem(self.row,1,item)</li>
          <li>  self.items.append(item)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/v4.10.2/Modules/Scripted/EditorLib/ColorBox.py#L75-L128" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @rhodesdante (2022-09-19 19:49 UTC)

<p>Thanks again for your help, I pasted the code that worked for my use case below. Adapted from the snippet <a class="mention" href="/u/pieper">@pieper</a> shared.</p>
<p>% turn a cell green in a table:<br>
% tv = my qmrmlTableView</p>
<p>c = 255<br>
cNode = slicer.util.getNode(“Green”)<br>
name = cNode.GetColorName(c)<br>
lut = cNode.GetLookupTable()<br>
rgb = lut.GetTableValue(c)<br>
brush = qt.QBrush()<br>
color = qt.QColor()<br>
color.setRgb(rgb[0]*255,rgb[1]*255,rgb[2]*255)<br>
brush.setColor(color)<br>
item = qt.QStandardItem()<br>
item.setBackground(color)<br>
tv.tableModel().setItem(2,2,item)  % this sets the cell (2,2) green</p>

---
