---
topic_id: 11877
title: "Vmtk Vessel Centerline Network Extraction In Slicer"
date: 2020-06-05
url: https://discourse.slicer.org/t/11877
---

# VMTK vessel centerline network extraction in Slicer

**Topic ID**: 11877
**Date**: 2020-06-05
**URL**: https://discourse.slicer.org/t/vmtk-vessel-centerline-network-extraction-in-slicer/11877

---

## Post #1 by @Deepa (2020-06-05 10:43 UTC)

<p>I’ve installed Vascular Modelling Toolkit extension in Slicer4.11.<br>
I could find<br>
Centerline computation<br>
Level set segmentation<br>
Vesselness filtering</p>
<p>I couldn’t find vmtknetworkextraction . I’d like to know if there a separate plugin for networkextraction.</p>

---

## Post #2 by @lassoan (2020-06-05 16:23 UTC)

<p>SlicerVMTK extension is available in Slicer-4.11. There are some temporary issues with the extension server today, but you can use a Slicer release from a couple of days before, for the version that you can download from here: <a href="https://download.slicer.org/?date=2020-05-30" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> many extensions reported upload errors - see for example <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1932677">this</a>.</p>
<p>If you installed SlicerVMTK and the modules did not appear then maybe you have closed the application manually before the installation has been completed. The installation is completed when “Restart” button becomes active.</p>
<aside class="quote no-group" data-username="Deepa" data-post="1" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I couldn’t find vmtknetworkextraction . I’d like to know if there a separate plugin for networkextraction</p>
</blockquote>
</aside>
<p>“Centerline Computation” module performs network extraction. You can process the network further and extract additional data by Python code snippets as shown <a href="https://discourse.slicer.org/t/vessel-tree-centerline-branch-extraction-using-vmtk/11867/6">here</a>.</p>
<p>If you can describe the clinical problem you are trying to solve and the analysis that you would like to perform then we can give more specific help with how to achieve that.</p>

---

## Post #4 by @Deepa (2020-06-06 13:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you very much for the recent <a href="https://www.youtube.com/watch?v=caEuwJ7pCWs" rel="noopener nofollow ugc">video</a> that has been shared. I could follow and obtain the centerlines and curve tree root for a test geometry.</p>
<p>I’d like to extract the geometry in the form of a network. In the end, I wish to obtain the length( Abscissas) and radius( MISR) of each branch with the corresponding branch ids and the ids of start and<br>
end points associated with each branch.<br>
So, I tried</p>
<blockquote>
<blockquote>
<blockquote>
<p>import vtkvmtkNetworkExtractionPython as  vmtkNetworkExtraction</p>
</blockquote>
</blockquote>
</blockquote>
<p>But it didn’t work.</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
ModuleNotFoundError: No module named ‘vtkvmtkNetworkExtractionPython’</p>
</blockquote>
<p>The code that I use in python for doing the same task can be found <a href="https://github.com/DeepaMahm/misc/blob/master/trial2.py" rel="noopener nofollow ugc">here</a></p>
<p>Could you please offer suggestions on how to do this in Slicer?</p>

---

## Post #5 by @lassoan (2020-06-06 15:26 UTC)

<p>There is no such module as NetworkExtraction. See list of modules in <a href="https://github.com/vmtk/vmtk/tree/master/vtkVmtk">VMTK repository</a>: Common, ComputationalGeometry, DifferentialGeometry, etc.</p>
<p>You don’t need to run NetworkExtraction, as <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/CenterlineComputation/CenterlineComputation.py#L545">“Centerline computation” module already performs network extraction</a>. The result is available in the polydata of the  it is already done as part of the output “Centerline model” node (call <code>GetPolyData()</code> on this node to access it).</p>
<p>Radius is available as point scalar in “Centerline model” node polydata.</p>
<p>Branch lengths are available in the extracted contour nodes in Markups module, but if you want to have radius and branch length information in a single data structure then you can use <code>vtkvmtkCenterlineAttributesFilter</code>.</p>
<p>How do you plan to process the radius and length information? Are you going to compute some overall statistics?</p>

---

## Post #6 by @Deepa (2020-06-06 16:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is no such module as NetworkExtraction</p>
</blockquote>
</aside>
<p>From what I know, it is <a href="http://www.vmtk.org/vmtkscripts/vmtknetworkextraction.html" rel="noopener nofollow ugc">available</a> as a python class.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you plan to process the radius and length information? Are you going to compute some overall statistics?</p>
</blockquote>
</aside>
<p>I’m interested in using this for CFD simulations.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but if you want to have radius and branch length information in a single data structure then you can use <code>vtkvmtkCenterlineAttributesFilter</code> .</p>
</blockquote>
</aside>
<p>Yes, I would like to have radius and length in a single data structure.<br>
Should I use <code>vtkvmtkCenterlineAttributesFilter</code> on centerline_model node?</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>(call <code>GetPolyData()</code> on this node to access it</p>
</blockquote>
</aside>
<p>I am not sure how to do this?<br>
Could you please add a short video tutorial?</p>

---

## Post #7 by @lassoan (2020-06-06 16:47 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="6" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>From what I know, it is <a href="http://www.vmtk.org/vmtkscripts/vmtknetworkextraction.html">available </a> as a python class.</p>
</blockquote>
</aside>
<p>The page you referred to documentats usage of VMTK’s special “pypes” scripts. These scripts are not Python classes that you import and use, but scripts that you can use via command line. They are very thin wrappers over Python classes, which are useful for people who prefer to work using command-line. For example, you can have a look at <a href="https://github.com/vmtk/vmtk/blob/master/vmtkScripts/vmtknetworkextraction.py">vmtknetworkextraction script</a> and how it calls uses <code>vtkvmtkPolyDataNetworkExtraction</code> class. I would recommend to use the VTK classes directly instead of going through the extra layer of pypes scripts.</p>

---

## Post #8 by @Deepa (2020-06-06 16:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you very much for the clarification. I’m sorry about the confusion, I am really new to all of this.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to use the VTK classes directly instead of going through the extra layer of pypes scripts.</p>
</blockquote>
</aside>
<p>Sure,  I’d like to know how to process the branchids and the ids of endpoints associated with each branch.<br>
For instance, I could do the following on polyData obtained after networkextraction.</p>
<blockquote>
<p>edgeNode0 = edge.GetPointId(0)<br>
edgeNode1 = edge.GetPointId(1)</p>
</blockquote>
<p>This will give information on the topology.</p>

---

## Post #9 by @lassoan (2020-06-06 17:55 UTC)

<p>What would like to compute exactly as end result? Average vessel radius over the entire tree? Average vessel segment length over the entire tree?</p>

---

## Post #10 by @Deepa (2020-06-07 03:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Yes, I would like to compute the average vessel segment length and average vessel segment radius<br>
of all the branches in a tree.<br>
Please check <a href="https://github.com/DeepaMahm/misc/blob/master/data.xlsx" rel="nofollow noopener">sample</a></p>

---

## Post #12 by @lassoan (2020-06-08 06:02 UTC)

<p>I’ve added computation of branch length, average radius, curvature, torsion, and tortuosity to the centerline computation module. All you need to do to compute these metrics is to select a node for “Centerline properties”. This feature will be available in tomorrow’s Slicer Preview Release.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cea7c3be91b02283d6d0f5f82e01f59ab6876f1a.png" data-download-href="/uploads/short-url/tu9NaajqlAYvtWbfymFWY3jQEye.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea7c3be91b02283d6d0f5f82e01f59ab6876f1a_2_690x420.png" alt="image" data-base62-sha1="tu9NaajqlAYvtWbfymFWY3jQEye" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea7c3be91b02283d6d0f5f82e01f59ab6876f1a_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea7c3be91b02283d6d0f5f82e01f59ab6876f1a_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cea7c3be91b02283d6d0f5f82e01f59ab6876f1a_2_1380x840.png 2x" data-dominant-color="E1E2E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 532 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @Deepa (2020-06-08 06:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Excellent! I am super happy to know about this new feature. Thanks a ton. I look forward to use this.</p>
<p>From what I understand, <code>CellId</code> refers to the branchid. It will be super helpful if you could also add<br>
4 more columns branchNode0 and branchNode1, xyz_branchNode0, xyz_branchNode1.</p>
<p>branchNode0 = branch.GetPointId(0) # nodeid of the one end of a branch<br>
branchNode1 = branch.GetPointId(1) # nodeid of the other end of a branch</p>
<p>and xyz_branchNode0, xyz_branchNode1 are the corresponding coordinates.</p>
<p>I had obtained the above in the following manner (<a href="https://github.com/DeepaMahm/misc/blob/master/trial2.py" rel="nofollow noopener">code</a>).</p>
<pre><code> for branchId in range(cleanedGraph.GetNumberOfCells()):
        branch = cleanedGraph.GetCell(branchId )  # this will be a vtkLine, which only has two points

    branchNode0 = branch .GetPointId(0)
    branchNode1 = branch .GetPointId(1)
</code></pre>
<p><a href="https://github.com/DeepaMahm/misc/blob/master/data.xlsx" rel="nofollow noopener">output</a>.<br>
Deepa</p>

---

## Post #14 by @lassoan (2020-06-08 14:04 UTC)

<p>You can cross-reference the displayed curve with the computed properties in the table based on the CellId displayed in parentheses in the widget’s node name, so you can find out quite easily which numbers are for which vessel segment.</p>
<p>Anyway, I have now added branch start and end point positions to the properties table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07349af88fa9aacb0e758b652ab6bb92aaa5afb0.png" data-download-href="/uploads/short-url/11K31nLnb0r7ktJoJFsP2PYqpQA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07349af88fa9aacb0e758b652ab6bb92aaa5afb0_2_690x419.png" alt="image" data-base62-sha1="11K31nLnb0r7ktJoJFsP2PYqpQA" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07349af88fa9aacb0e758b652ab6bb92aaa5afb0_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07349af88fa9aacb0e758b652ab6bb92aaa5afb0_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07349af88fa9aacb0e758b652ab6bb92aaa5afb0_2_1380x838.png 2x" data-dominant-color="D6D7E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 589 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @Deepa (2020-06-08 14:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you very much. This is extremely helpful.</p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can cross-reference the displayed curve with the computed properties in the table based on the CellId displayed in parentheses in the widget’s node name, so you can find out quite easily which numbers are for which vessel segment.</p>
</blockquote>
</aside>
<p>If my understanding is right, the cellId displayed in parentheses are the numbers assigned to the vessel segments/ branches.<br>
In my previous response, <code>nodeid of the one end of a branch</code> - I was referring to the ids of<br>
<code>StartPointPosition</code> and <code>EndPointPosition</code>.</p>
<p>For instance, if I manually map the positions to ids for this simple input structure<br>
CellId    StartPointId  EndPointId<br>
0              0                 1<br>
1              1                  2<br>
2              2                  3<br>
3              2                  4</p>
<p>and so on …</p>
<p>Can we retrieve these ids from the polyData? I think these can be mapped to the indices of the array<br>
that stores these positions.</p>
<p>Thanks a lot again for these extensions!</p>
<p>Deepa</p>

---

## Post #16 by @lassoan (2020-06-08 15:16 UTC)

<p>Parent/child relationships are the easiest to get from the curve hierarchy (you can get list of all immediate or all children nodes, etc.), but of course it is very easy to add any additional columns to the table, too. Could you describe what do you plan to compute and how?</p>

---

## Post #17 by @Deepa (2020-06-08 16:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but of course it is very easy to add any additional columns to the table</p>
</blockquote>
</aside>
<p>Yes, that will be really helpful.</p>
<p>I plan to use this as an input for CFD studies where the endpoint ids will be useful for setting up external inputs.</p>

---

## Post #18 by @lassoan (2020-06-08 16:28 UTC)

<p>What software do you plan to use and how? For CFD analysis, you probably need a couple of more things, such as:</p>
<ul>
<li>use the original surface mesh instead of just centerline&amp;radius (e.g., to model non-circular vessel geometry or aneurysms more accurately)</li>
<li>use a volumetric mesh</li>
<li>add straight extensions so that you can prescribe known boundary conditions at the end of those segments</li>
</ul>
<p>These are all perfectly doable and have all the tools in Slicer and VMTK, but probably it would be better to implement these in a script first. Once you have a working script, it can be easily converted to a scripted module so that it is easier to use (you can select input/output nodes, parameters using a convenient GUI).</p>
<p>Let me know what exactly you would like to do and I’ll help with creating the script, and then with the conversion to scripted module.</p>

---

## Post #19 by @Deepa (2020-06-09 05:29 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you very much for offering to build scripted modules in Slicer for this study.  This will be tremendously helpful for researchers working in this field.</p>
<p>For now, I’ve written my own code that models the underlying physics for performing the CFD analysis. I will be using the centerline properties obtained from Slicer as input. I would be super happy to share more details for developing a scripted module in Slicer in another 1-2 months. From my experience so far, Slicer will serve as a great platform since most of the tools are readily avaiable.</p>
<p>Kindly let me know after the ids of <code>StartPointPosition EndPointPosition</code> are appended to the centerline properties table. I look forward to use this feature.</p>

---

## Post #20 by @Deepa (2020-06-13 16:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>This is a polite reminder about the inclusion of <code>StartPointPosition EndPointPosition</code>  in the centerline properties table. I would like to know if this will be included.</p>
<p>Also, after the CenterlineComputationModel is created can we delete certain branches using the nodes defined in <code>tree</code>? I prefer to delete the branches with free ends, I want to retain only two free ends. Can we do this programmatically?  If we can obtain the ids of all the free nodes from the network that is generated during computation of centerlines , the user can select the free ends to be retained and the branches that are connected to the other free ends can be deleted. The use case would be in CFD simulations where the boundary conditions can be defined. Defining boundary condition gets complicated when there are a lot of boundaries .</p>
<p>If this deletion cannot be directly done in Slicer, I would like to request for a export option that will allow the user to export the generated centerline network. The free ends can be deleted in an external tool by the user. This will be really helpful.</p>

---

## Post #21 by @lassoan (2020-06-20 21:50 UTC)

<p>Branch deleting is now implemented, see:</p>
<aside class="quote quote-modified" data-post="1" data-topic="12117">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">New module: Extract Centerline (in SlicerVMTK extension)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We added a completely new module that makes vessel (or airway or any other tree structure) centerline extraction much faster, flexible, and robust. It can quickly extract a network, determine branch endpoints automatically, allows editing of endpoints, computing centerlines, branches, and quantitative metrics (radius, curvature, torsion, etc). The new “Extract Centerline” module is available in SlicerVMTK extension for latest Slicer-4.11 release (it replaces the old “Centerline Computation” modu…
  </blockquote>
</aside>


---

## Post #22 by @Deepa (2020-07-10 06:11 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Branch deleting works well for updating centerlines (i.e removal of branch in centerline model) when an endpoint is deleted. But the network branch doesn’t get removed.  I’d like to know if it is possible to enable removal of the branches in network model too.</p>

---

## Post #23 by @lassoan (2020-07-10 17:42 UTC)

<p>Network extraction gets all branches. To search a path between two points in a network, you can use the method described here:</p>
<aside class="quote quote-modified" data-post="5" data-topic="12418">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vmtk-centerline-display-by-centerlineid/12418/5">VMTK Centerline Display by CenterlineId</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Choose “Centerline curve” and not “Network curve” to extract centerline between selected endpoints. 
If you extract all the branches then you can use markups curves to find path between two arbitrary points: go to Markups module, drop two points of a curve on the tree, open Curve Settings section, choose Curve type → “Shortest distance on surface” and Model node → the tree model. See this video: 

  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    [Finding shortest path between two points in the bronchial tree]
  </a>
  </blockquote>
</aside>


---

## Post #24 by @Deepa (2020-07-11 01:52 UTC)

<p>Thanks a lot for the response. I would like to know if there is a way to remove a branch in the network model by selecting an endpoint and deleting it .</p>

---

## Post #25 by @lassoan (2020-07-11 03:38 UTC)

<p>If you choose the curve hierarchy representation of the network then you have full control over each point of each branch: you can edit each individual point or remove each branch.</p>
<p>What would you like to achieve?</p>

---

## Post #26 by @Deepa (2020-07-11 04:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to achieve?</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9bc6d70aa56b0c85e0423bf0dfd917e3840951a.png" data-download-href="/uploads/short-url/odyoAod64k57et7fzSJztrWXKOu.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9bc6d70aa56b0c85e0423bf0dfd917e3840951a_2_261x250.png" alt="Untitled" data-base62-sha1="odyoAod64k57et7fzSJztrWXKOu" width="261" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9bc6d70aa56b0c85e0423bf0dfd917e3840951a_2_261x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9bc6d70aa56b0c85e0423bf0dfd917e3840951a_2_391x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9bc6d70aa56b0c85e0423bf0dfd917e3840951a_2_522x500.png 2x" data-dominant-color="A2A6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">595×568 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Endpoint(glyph) in one of the branches is removed using <code>Delete point</code>. Deleting this endpoin has updated the centerline model automatically after hitting apply but the network model has not been updated. I will like to achieve an updated network model(and results displayed in quantification table) as well.</p>
<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="11877">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you choose the curve hierarchy representation of the network then you have full control over each point of each branch: you can edit each individual point or remove each branch.</p>
</blockquote>
</aside>
<p>Thank you.<br>
I could use the hierarchy representation to remove individual branches in the network model. But this doesn’t help in obtaining the corresponding update (i.e deletion of the values in the table) in the quantification results.</p>

---

## Post #27 by @lassoan (2020-07-11 18:02 UTC)

<p>You could write a small script that removes rows from the table that don’t have corresponding markup curve. You can get list of children nodes from the subject hierarchy node and the node has the cell index in a custom attribute. You could collect all the indices and create a new properties table, where you would only include those rows that have its index in the list.</p>

---
