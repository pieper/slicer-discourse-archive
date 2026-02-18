# vmtkcenterlines script profileidlist points order

**Topic ID**: 20667
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/vmtkcenterlines-script-profileidlist-points-order/20667

---

## Post #1 by @scarpma (2021-11-17 17:23 UTC)

<p>Hello everyone,</p>
<p>I am currently trying to automatize the extraction of centerlines in my python script, using vmtk.</p>
<p>From the command line one can specify the id of the source and target points by setting <em>seedselector</em> to “<em>profileidlist</em>”. My problem is to understand how these points are ordered.</p>
<p>In other words, how are the open profiles barycenters computed by the script ordered ? Maybe according to the z coordinate ?</p>
<p>Thanks in advance</p>

---

## Post #2 by @kayarre (2021-11-29 23:37 UTC)

<p><a class="mention" href="/u/scarpma">@scarpma</a> I believe you are right about the ID’s being ordered by Z height.</p>

---

## Post #3 by @scarpma (2021-12-01 17:06 UTC)

<p>I think this is not the case. I tried, but that didn’t work. Has anyone tried this ?</p>

---

## Post #4 by @ramtingh (2021-12-01 18:01 UTC)

<p>It’s not quite clear what you want to do, do you have already have a list of ids you want to supply or you want vmtk to calculate them for you?</p>
<p>If you want them ordered by z-height, you’d have to set the type to <code>carotidprofiles</code>. This would automatically set the lowest z height as the source id if I remember correctly.<br>
The open profile ids themselves are based on whatever <code>vtkvmtkPolyDataBoundaryExtractor</code> returns, which is arbitrary as I don’t think the traversal order is going to have any reliable pattern.</p>

---

## Post #5 by @scarpma (2021-12-01 20:21 UTC)

<p>Thank you very much for the answer.</p>
<p>What I would like to do is to compute centerlines in a specific order across different aortas.</p>
<p>Since every aorta has 5 openings (inlet near the heart, three supraortic vessels and descending part), I would like to choose as source the inlet, and as targets the descending opening and the three supraortic openings.</p>
<p>But I would like to do this automatically in a script. I was wondering if there’s a way to know how the ids are ordered.</p>
<p>Thank you very much !</p>

---

## Post #6 by @kayarre (2021-12-10 21:09 UTC)

<p><a class="mention" href="/u/scarpma">@scarpma</a> apologies If added confusion. I have come across some behaviors that appear to have things ordered by Z height, but it has been a while.</p>
<p>I have thought of this in the past some. I think adding labels to things upstream in the process would make this possible. One thing that I have worked on in the past is using networkX, or some other data structure that allows labeling. Embedding labels in VTK data structures is doable, but my experience has been that it is not as straight forward.</p>
<p>I believe Slicer has some additional constructs that could make this possible as well, but have not investigated.</p>

---

## Post #7 by @scarpma (2021-12-13 09:15 UTC)

<p>What do you mean by “labeling” ?</p>
<p>By the way I solved the problem by giving points coordinates manually, and not point Ids.</p>
<p>This required a little more work because I have to find the coordinates, but at least now I know where these points are.</p>

---

## Post #8 by @kayarre (2021-12-16 03:50 UTC)

<p>I guess the analogy would be if you have ever used CAD or commercial CFD codes, one can label surfaces, lines, planes, and points etc. The example I think of here is labeling the inlet, outlet, and wall surfaces and propagating those labels throughout a workflow.</p>
<p>I implemented something hacky so I could automate generating boundary condition information.</p>
<p>Maybe there is a format that would allow this kind of meta data to be stored more cleanly. I know slicer uses xml, but it’s not exactly easy to read.</p>

---

## Post #9 by @scarpma (2021-12-16 13:44 UTC)

<p>Ah ok, I understand. In this case, yes, surfaces can be labeled via an integer cell array, but VMTK, for what I know, does not interact with such information. One has to manually implement such operations and this is what I did. Knowing the coordinates of the barycenters of open boundaries one can feed these into VMTK and do the computation without the user interaction.</p>
<p>The problem is that the code to implement this is a bit elaborated and in fact useless, since VMTK already knows these coordinates, but without knowing also the ordering, in fact they are useless.</p>

---
