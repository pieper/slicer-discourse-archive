# Merging Centrelines

**Topic ID**: 16807
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/merging-centrelines/16807

---

## Post #1 by @CJBright (2021-03-28 21:07 UTC)

<p>Hi everyone,</p>
<p>I used a programme to calculate the centrelines of a cardiovascular model I’ve been working on.<br>
I then used a Python script to save each branch individually. It starts at one end of the model and follows each branch, saving them as a new .vtp file.<br>
Therefore, at each point that the vessel splits, the branch leading to the point is saved and two new branch files begin. i.e a ‘Y’ shaped branch has 3 constituent files - 1 coming in, and 2 leaving.</p>
<p>Now I want to look at my data along the longest branch in the model, but due to how the Python script worked, this vessel is saved in 5 parts.<br>
I’m very new to VMTK and Python, however I managed to use ‘vmtkappendsurfaces’ to join each of these together sequentially to get a file of the whole vessel.</p>
<p>The issue, as imaged, is that there is a slight gap where each of these vessels join. The end of one part is not exactly the start of the next. Hence when plotting data from along this line there are strange fluctuations in the graph that are unrealistic and visually unappealing.</p>
<p>Does anybody know of a script that will append my 5 lines together sequentially as I have done, but also interpolate the information inbetween, to create a continuous centreline?<br>
I’ve taken a look at ‘vmtkcenterlinemerge’ although I don’t understand how it works and haven’t been able to successfully test it out. If this is the correct method, can anybody help me understand it please?<br>
Current: <em>—</em>    <em>----</em>    <em>-</em>   <em>-----</em><br>
Desired: <em>—</em> —<em>----</em>----<em>-</em>—<em>-----</em></p>
<p>Any advice would be greatly appreciated.<br>
Charlie<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/613010d019bf085381f9e0d37f42e5c6087406dd.jpeg" data-download-href="/uploads/short-url/dRLihtjRX6Q4SgC8eNPJDFIez7L.jpeg?dl=1" title="Help" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613010d019bf085381f9e0d37f42e5c6087406dd_2_456x500.jpeg" alt="Help" data-base62-sha1="dRLihtjRX6Q4SgC8eNPJDFIez7L" width="456" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613010d019bf085381f9e0d37f42e5c6087406dd_2_456x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613010d019bf085381f9e0d37f42e5c6087406dd_2_684x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/613010d019bf085381f9e0d37f42e5c6087406dd_2_912x1000.jpeg 2x" data-dominant-color="ABA2AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Help</span><span class="informations">1146×1256 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-04-03 02:42 UTC)

<p>You can use <a href="https://vtk.org/doc/nightly/html/classvtkStripper.html">vtkStripper</a> to merge curves that share points. If you miss a connection between branches then you can add it by using vtkLineSource and vtkAppendFilter.</p>

---
