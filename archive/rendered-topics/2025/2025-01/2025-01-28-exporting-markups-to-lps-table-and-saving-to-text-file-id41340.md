---
topic_id: 41340
title: "Exporting Markups To Lps Table And Saving To Text File"
date: 2025-01-28
url: https://discourse.slicer.org/t/41340
---

# Exporting markups to LPS table and saving to text file?

**Topic ID**: 41340
**Date**: 2025-01-28
**URL**: https://discourse.slicer.org/t/exporting-markups-to-lps-table-and-saving-to-text-file/41340

---

## Post #1 by @evaherbst (2025-01-28 18:28 UTC)

<p>Hello,</p>
<p>Is there a simple way to</p>
<ol>
<li>export a markups point list to a table in LPS in Python (rather than the GUI) and then</li>
<li>saving that table as a .txt file?</li>
</ol>
<p>I have another program that reads the lps text file and everything works well from the GUI but I would like to automate this step.</p>
<p>For step 1, I saw in the Slicer logic this function:</p>
<blockquote>
<p>static bool ExportControlPointsToTable(vtkMRMLMarkupsNode* markupsNode, vtkMRMLTableNode* tableNode,<br>
int coordinateSystem = vtkMRMLStorageNode::CoordinateSystemRAS);</p>
</blockquote>
<p>I assume I first need to make a new table node, then run the above, but how do I change the coordinate system to LPS?</p>
<p>I saw a post for how to save markups to csv with</p>
<blockquote>
<p>slicer.modules.markups.logic().ExportControlPointsToCSV(markupsNode, “/path/to/MyControlPoints.csv”)</p>
</blockquote>
<p>but I prefer the txt export since I have my pipeline set up to read that.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @muratmaga (2025-01-28 19:23 UTC)

<p><a class="mention" href="/u/evaherbst">@evaherbst</a><br>
All of these should be doable, the question is what is the benefit you will be gaining by exporting the data in yet another format? Did you consider reading the JSON file directly (which already saves the coordinates in LPS)? Going forward you might find your workflow to be more robust if you avoid using these customs codes and outputs and go straight from JSON.</p>
<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="41340">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>t how do I change the coordinate system to LPS?</p>
</blockquote>
</aside>
<p>Did you try</p>
<pre><code class="lang-auto">int coordinateSystem = vtkMRMLStorageNode::CoordinateSystemLPS);
</code></pre>
<p>If this doesn’t work, and since you are building custom code, you can simply multiply the first to coordinates by -1 to convert RAS to LPS (or vice versa).</p>

---

## Post #3 by @evaherbst (2025-01-28 22:26 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>!</p>
<p>Solved.<br>
I used:</p>
<blockquote>
<p>markupsNode = slicer.util.getNode(“myNode”)</p>
<p>if not markupsNode:</p>
<p>raise ValueError(“Markups node not found”)</p>
<p>tableNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”)</p>
<p>tableNode.SetName(markupsNode.GetName())</p>
<p>slicer.modules.markups.logic().ExportControlPointsToTable(markupsNode, tableNode, slicer.vtkMRMLStorageNode.CoordinateSystemLPS)</p>
</blockquote>
<p>And then simply saved that table with the .txt extension</p>
<p>I did not want to use .mrk.json extension because my biomechanical model is in Java and I have a reader method that reads the .txt files.</p>

---

## Post #4 by @muratmaga (2025-01-29 08:41 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="3" data-topic="41340">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>I did not want to use .mrk.json extension because my biomechanical model is in Java and I have a reader method that reads the .txt files.</p>
</blockquote>
</aside>
<p>That is fine, but I highly recommend to develop your json reader instead. That will help you in the long-run both from data management perspective (what if you decide to add/revise new markups?) and data flow (you will have to re-export everything if you modify your dataset).</p>
<p>I have been in a similar situation, and did what you are doing right now which eventually became a burden.</p>

---

## Post #5 by @evaherbst (2025-02-11 09:34 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> for the advice, that is a good point.</p>

---
