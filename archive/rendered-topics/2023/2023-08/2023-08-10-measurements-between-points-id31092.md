---
topic_id: 31092
title: "Measurements Between Points"
date: 2023-08-10
url: https://discourse.slicer.org/t/31092
---

# Measurements between points

**Topic ID**: 31092
**Date**: 2023-08-10
**URL**: https://discourse.slicer.org/t/measurements-between-points/31092

---

## Post #1 by @Cervantes (2023-08-10 21:53 UTC)

<p>Hello. I need some help. I have looked for an answer, but I must be missing something.<br>
I am doing some research in geometric morphometrics, but I am also collecting numerous measurements that are between various points that I place. To speed things up I have made a list of measurements and am copying and pasting the point locations into the appropriate measurement markup control points once they have been placed. This has helped, but it still seems inefficient.</p>
<p>Is there a faster way? Is there a way to populate these automatically? Also, is there a way to have this list of measurements able to be saved into text/spreadsheet?</p>
<p>In case an example helps: I place the points for the nasion and bregma on the cranium. I need the FRC distance, which is the distance between these two… I have a pre-made (blank) markup called FRC prepared, and I copy the points of the nasion and the bregma into the control points for FRC.<br>
This takes a LONG time when I’ve got a multitude of measurements and have to look up all of these points in differing order (still more efficient than placing the points again). I’m looking for a way to have the nasion and bregma marks automatically populate their locations in the measurement markup when I place the point.</p>
<p>Note that for my workflow, it works much better to place all of the points, one after the other, and then deal with the measurements. I am not great with using Python, but if that is the only way to do this, I may give it a shot.</p>
<p>Suggestions or input are thoroughly appreciated! I have a multitude of scans to go through doing this and hope to find a more efficient approach.</p>

---

## Post #2 by @lassoan (2023-08-10 22:28 UTC)

<p>Yes, you can fully automate all your measurements with a very little Python scripting. There are many examples of what you can do in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and you can ask any specific questions here.</p>
<p>A few tips:</p>
<ul>
<li>You can create a markup list, unset all the point positions, save that to a file, and use this as a template for your landmark point list.</li>
<li>Once you placed all the points, run a Python script by using a keyboard shortcut that adds all the measurements between your points, saves everything in a .mrb file, and maybe also adds the results to a csv file.</li>
<li>You can ask bing chat to generate a script for you - just describe in plain English what you need, for example: <code>write Python code for 3D Slicer that uses code snippets in the script repository that creates markup lines between point positions taken from markup point list</code></li>
</ul>

---

## Post #3 by @Cervantes (2023-08-11 00:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="31092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>l the point positions, save that to a file, and use this as a template for your landmark point list.</li>
<li>Once you placed all the points, run a Python script by using a keyboard shortcut that adds all the measurements between your points, saves everything in a .mrb file, and maybe also adds the results to a csv file.</li>
</ul>
</blockquote>
</aside>
<p>AH! Thank you so much! I’m stunned that I hadn’t thought of using bing chat! I do have all of my points in a list of unset points (three lists, actually, but I can easily make it one since that will probably facilitate this).</p>
<p>I knew there was something I hadn’t thought of. Thanks! I’ll be back with more questions if I run into problems!</p>

---

## Post #4 by @Cervantes (2023-08-11 21:01 UTC)

<p>Hello to anyone who might come looking in the future looking for an answer to this.</p>
<p>I got a script that gives me a list of the distances between <em>every single point</em>. While this is a bit cumbersome, it isn’t the worst. It took a lot of trial and error in bing Chat, but I managed to cobble something together to get what I needed.</p>
<p>I had a premade list of points to be collected from all crania, so I just copied the blank version into each Slicer project and collected them all in the same order. This is important because it ensures the list of measurements is in the same order. I also made sure the code gave me the names for the points that I had given them, not just numbers that it assigned. This helps me confirm that the measurements are for what I intended.</p>
<p>I ran the Python code in Slicer (which will be below)</p>
<p>I take the produced list and paste it into a column in Excel. I had about 37 measurements that I needed, and I made another column to note which ones those were.</p>
<p>For each project I copy and paste the list of measurements into the next column, which is headed by the crania accession number.<br>
At the end, I’ll take all of the text out of the Excel columns, leave the numbers, and just select the ones I need for my research project based on the rows I’ve flagged ahead of time.<br>
I <em>KNOW</em> there are ways to script some of what I am doing further, but I’m admittedly uncomfortable with scripting in Python, but super comfortable manipulating my data in Excel, so this is balancing things and is still more efficient for me. I’m ending up with a ton more data than I intended, but it might be useful… who knows!</p>
<p>I hope this helps somebody eventually!</p>
<p>Here is the script I used to get my list of measurements:</p>
<p>"</p>
<pre><code class="lang-auto">import slicer
import math

# Get the MarkupsFiducial node (change "F" to match the name of your Markups node)
markupsNode = slicer.util.getNode('F')

# Get the point names and coordinates from the Markups node
points = []
for i in range(markupsNode.GetNumberOfFiducials()):
    name = markupsNode.GetNthFiducialLabel(i)
    coordinates = [0.0, 0.0, 0.0]
    markupsNode.GetNthFiducialPosition(i, coordinates)
    points.append((name, coordinates))

# Calculate distances between points
num_points = len(points)
distances = []

for i in range(num_points):
    for j in range(i + 1, num_points):
        name1, point1 = points[i]
        name2, point2 = points[j]
        
        distance = math.sqrt(
            (point1[0] - point2[0])**2 +
            (point1[1] - point2[1])**2 +
            (point1[2] - point2[2])**2
        )
        
        distances.append((name1, name2, distance))

# Print or process the distances as needed
for name1, name2, distance in distances:
    print(f"Distance between point '{name1}' and point '{name2}': {distance}")"


</code></pre>

---

## Post #5 by @lassoan (2023-08-11 21:58 UTC)

<p>Thanks for sharing.</p>
<p>Just a tip: you can ask bing chat to further improve any parts of the code. If it does not do exactly what you need, just ask again, be more specific, write why the generated code is not good enough and what you want instead and it (usually) gets it right in the end. Of course you learn more and more during this process and you’ll rely less on the chatbot and trial and error. It is very much worth it to learn Python scripting, it is a very good complementary skill to data wrangling in Excel.</p>
<p>If you are only interested in specific <code>[i, j]</code> point pairs then you can replace this:</p>
<pre><code class="lang-python">for i in range(num_points):
    for j in range(i + 1, num_points):
</code></pre>
<p>by something like this:</p>
<pre><code class="lang-python">for i, j in [ [0, 1], [0, 3], [2, 4], [5, 8] ]:
</code></pre>
<p>To avoid any manual copy-pasting (that is time-consuming and error-prone), you can add the measurements to an Excel file (in csv format):</p>
<pre><code class="lang-python">with open("c:/tmp/results.csv", "a") as f:
    for name1, name2, distance in distances:
        f.write(str(distance) + "\t")  # write each distance to the file, separated by tab character
    f.write("\n")  # add a new line
</code></pre>
<p>Make sure to always save your landmarks in a scene (you can save everything in a single .mrb file, which is a zip file of all data that is in the scene) so that you can later review your point placement or compute additional metrics.</p>

---

## Post #6 by @Cervantes (2023-08-12 00:30 UTC)

<p>Thank you for the extra tips!! I may try those out on Monday.</p>
<p>I did ask Chat to refine several times, and I had some errors which had to be fixed, some of which Chat had a hard time getting rid of. I finally got frustrated and went with the more simple, straightforward one (with code I was able to actually follow) to get a good basis to move forward.</p>
<p>I will try to remember to return and post the final version of the code if I get it working as intended, just for anyone else who might come along. If I don’t get around to posting, at least I’ve got some fantastic answers, and a good reference will still be here.</p>
<p>Thanks for the help. This community is always amazing!</p>

---
