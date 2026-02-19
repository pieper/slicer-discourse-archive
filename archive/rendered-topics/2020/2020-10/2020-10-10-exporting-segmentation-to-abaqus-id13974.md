---
topic_id: 13974
title: "Exporting Segmentation To Abaqus"
date: 2020-10-10
url: https://discourse.slicer.org/t/13974
---

# Exporting segmentation to Abaqus

**Topic ID**: 13974
**Date**: 2020-10-10
**URL**: https://discourse.slicer.org/t/exporting-segmentation-to-abaqus/13974

---

## Post #1 by @Jeff_S (2020-10-10 13:23 UTC)

<p>Dear Andras,<br>
as I had troubles with FEBio, I am trying now to use the segmentation of the vertebra (in vtk format) to load into ABAQUS and do the simulation with that program. But it seems, that ABAQUS does not support vtk format (which I thought is the format for volumetric objects and also includes the HU-values from the CT-data). Do you know a cheap solution (without using another expansive software) to convert the vtk format to a format, which ABAQUS can read and without loosing the HU-values, which I think might be important to calculate the stiffness in certain points in the bone. I hope you can help me, thanks a lot in advance! Best regards Jeff</p>

---

## Post #2 by @lassoan (2020-10-10 14:34 UTC)

<p>You can convert volumetric mesh from VTK format to Abaqus .inp file using the free <a href="https://github.com/nschloe/meshio">meshio</a> Python package.</p>
<p>I am not sure if material ID is included in the output file, but if you find that it is not, then you can submit a feature request to meshio.</p>

---

## Post #3 by @Jeff_S (2020-10-10 14:42 UTC)

<p>Thanks a lot for your quick reply, even on weekend, I am impressed!<br>
Where can I find this Python package or how can I implement it into Slicer (I have never worked with Python before)?</p>

---

## Post #4 by @lassoan (2020-10-10 14:57 UTC)

<p>You can open the Python console in Slicer, type <code>pip_install('meshio')</code> to download&amp;install meshio, and you are good to go. You can find command examples for reading a mesh and writing into another format on meshio website.</p>

---

## Post #5 by @Jeff_S (2020-10-13 15:01 UTC)

<p>Hi Andras,<br>
thanks a lot again! I installed the newest version of 3DSlicer and was able to run pip_install(‘meshio’).</p>
<p>According to the documentation of meshio, I was trying to use the following syntax:<br>
<em>m = meshio.Mesh.read(filename, “vtk”)  # same arguments as meshio.read</em><br>
<em>m.write(“foo.vtk”)  # same arguments as meshio.write, besides <code>mesh</code></em></p>
<p>and changed to the following:<br>
<em>m=meshio.Mesh.read(C:\Users\Admin\Documents\Jeffs-Data\test.vtk, “vtk”)</em><br>
<em>m.write(“output.inp”)</em></p>
<p>But unfortunately it does not work, what am I doing wrong?</p>

---

## Post #6 by @lassoan (2020-10-13 16:04 UTC)

<p>What is the error message?</p>
<p>You may run into trouble because using backslash (<code>\</code>) in Python string literals. Have a look at <a href="https://discourse.slicer.org/t/subprocess-call-does-not-work/2837/14">this post</a> for details.</p>

---

## Post #7 by @Jeff_S (2020-10-17 12:46 UTC)

<p>Now I have changed the backslash to (/) as Unix-type separators:<br>
<em>m= meshio.Mesh.read(C:/Users/Admin/Documents/Jeffs-Data/test.vtk, “vtk”)</em></p>
<p>and the following error message appeared:</p>
<pre><code>m= meshio.Mesh.read(C:/Users/Admin/Documents/Jeffs-Data/test.vtk, "vtk")
                     ^
</code></pre>
<p>SyntaxError: invalid syntax</p>

---

## Post #8 by @lassoan (2020-10-17 13:37 UTC)

<p>You missed the quotes.</p>

---

## Post #9 by @Jeff_S (2020-10-17 14:09 UTC)

<p>I am sorry,<br>
what quotes do you mean?</p>

---

## Post #10 by @muratmaga (2020-10-18 20:34 UTC)

<aside class="quote no-group" data-username="Jeff_S" data-post="7" data-topic="13974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p><code>m= meshio.Mesh.read(C:/Users/Admin/Documents/Jeffs-Data/test.vtk, "vtk")</code></p>
</blockquote>
</aside>
<p>Your filepath should have <code>""</code>s around.</p>

---

## Post #11 by @Jeff_S (2020-10-28 12:12 UTC)

<p>Thank you all for your help! Finally I could solve the problem!</p>
<p>for those who have the same problem and want to exchange a .vtk to a .inp file the following steps have to be done:</p>
<ul>
<li>Even though there is already a newer version of Python (28.10.2020) use the version 3.7.(as an interpreter). I used PyCharme Community edition 2020.2.3 to run the following program:<br>
<em>import meshio<br>
meshio.write(“output_name.inp”, meshio.read(“input_name.vtk”))</em>
</li>
<li>The Python program and the .vtk file have to be in the same folder</li>
</ul>
<p>By the way you need to install the meshio via: <em>pip_install(‘meshio’)</em> before running the program above</p>

---

## Post #12 by @Jeff_S (2020-10-28 12:16 UTC)

<p>Dear Mr. Lasso,<br>
do you maybe know, how I can check if the material ID have been included in the output file?<br>
I could load the .inp vertebra into ABAQUS but it seems, that there is only a surfacemesh but not a volumetric mesh. Am I missing something?<br>
Thanks a lot for your help in advance</p>

---

## Post #13 by @lassoan (2020-10-28 12:58 UTC)

<aside class="quote no-group" data-username="Jeff_S" data-post="11" data-topic="13974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>import meshio<br>
meshio.write(“output_name.inp”, meshio.read(“input_name.vtk”))</p>
</blockquote>
</aside>
<p>Note that you don’t need to install anything for this (Python, PyCharm, …), but you can run these few lines directly in Slicer’s Python console, too (hit Ctrl-3 to see it).</p>
<aside class="quote no-group" data-username="Jeff_S" data-post="12" data-topic="13974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>do you maybe know, how I can check if the material ID have been included in the output file?</p>
</blockquote>
</aside>
<p>Please check this in meshio documentation and if you don’t find any information on it then ask its developers (submit an <a href="https://github.com/nschloe/meshio/issues">issue</a> and post the link to the issue here for reference).</p>

---
