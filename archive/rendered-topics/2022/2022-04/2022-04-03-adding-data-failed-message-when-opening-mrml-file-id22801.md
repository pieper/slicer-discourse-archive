---
topic_id: 22801
title: "Adding Data Failed Message When Opening Mrml File"
date: 2022-04-03
url: https://discourse.slicer.org/t/22801
---

# "Adding data failed" message when opening MRML file

**Topic ID**: 22801
**Date**: 2022-04-03
**URL**: https://discourse.slicer.org/t/adding-data-failed-message-when-opening-mrml-file/22801

---

## Post #1 by @DIV (2022-04-03 07:40 UTC)

<p>I have gotten a handful of “adding data failed” “Adding data failed” messages lately when opening individual <code>MRML</code> Scene files.</p>
<p>The problematic Scene files would have been created with somewhat older versions of 3D Slicer, <em>circa</em> the second half of 2021.<br>
I had a handful of these messages with<br>
Slicer version: Slicer-4.13.0-2022-01-19<br>
Operating system: Windows 10 Enterprise x64</p>
<p>I have just updated to<br>
Slicer version: Slicer-4.13.0-2022-03-31<br>
and got another of these error messages, as below:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c76571f77cabd6679de24c6b3c2ab8d2887256d8.png" alt="image" data-base62-sha1="srWmrdPS6K8KyvZwtgDM8qva1qE" width="428" height="209"><br>
And upon scrolling down:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b2f33bcc3886942ecc286bb4a81a7c14929cea.png" alt="image" data-base62-sha1="nSlW7iClMaSnVxfFhgFi2dk1wS" width="428" height="209"></p>
<p>I’m not sure what impact this has on what’s loaded.  After I click OK, a whole lot of content (“data”?) is loaded, as I can see many objects in the <strong>Data</strong> module.<br>
I don’t know whether this is caused by a defect in the process of originally creating the <code>MRML</code> file (or other files referred to therein), a defect in the operation of reading the file, or perhaps a problem with my recent installations of 3D Slicer.  I don’t have an idea of how to troubleshoot it either.<br>
I think all of the errors were practically the same, although I didn’t screenshot them all.</p>
<p>Further information:</p>
<ul>
<li>Slicer is installed at <code>E:\Program Files\Slicer 4.13.0-2022-03-31</code>;</li>
<li>the <code>MRML</code> files are located on <code>D:</code>, several directories in, which I have mapped to <code>O:</code> to reduce the length of the path a bit;  and</li>
<li><code>D:\D\P\S-0\[...]</code> does not exist in my directory structure (<em>maybe the statement in the error message isn’t supposed to be interpreted literally?</em>).</li>
</ul>
<p>—DIV</p>

---

## Post #2 by @lassoan (2022-04-03 13:09 UTC)

<p>The errors mean that there are storage nodes in the scene without associated segmentation files. The messages may refer to orphan nodes that are left behind in the scene due to previous failed saving operations or incomplete node deletion operations.</p>
<p>There is currently no automatic cleanup mechanisms (such as deletion of orphan nodes), but I’ve added a feature request for it:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6298">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6298" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6298" target="_blank" rel="noopener">Remove unused nodes from the scene</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-03" data-time="13:03:43" data-timezone="UTC">01:03PM - 03 Apr 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The scene may contain unreferenced, invalid, and empty nodes due to module logic<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> errors, scene saving/loading errors, incomplete node deletions. 

These errors can cause warnings or errors at scene loading, causing distraction and making real scene errors harder to notice. 

## Describe the solution you'd like

Perform automatic checks for common errors during scene loading&amp;saving and either fix the errors automatically or by user confirmation (offer a list of nodes to remove using a checkable node list). 

## Describe alternatives you've considered

Always automatically deleting all invalid nodes may not be desirable because some modules may want to keep around extra nodes, or a node load may fail because some network paths being temporarily not available. 

## Additional context

Related user complaint: https://discourse.slicer.org/t/adding-data-failed-message-when-opening-mrml-file/22801?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Possible workarounds:</p>
<ul>
<li>Load all the data files instead of loading the scene file. This discards data that is stored in the scene file (relationship between nodes, display properties, etc).</li>
<li>Edit the scene file (.mrml) in a text editor: remove lines that refer to problematic nodes.</li>
</ul>

---

## Post #3 by @DIV (2022-04-03 13:27 UTC)

<p>Hello, Andras.</p>
<p>Thanks for the suggestions.<br>
Actually, a while after I posted, I had a further idea that might fit with what you’re describing.</p>
<p>You might remember <a href="https://github.com/Slicer/Slicer/issues/6002" rel="noopener nofollow ugc">a discussion</a> about objects being created ‘immediately’ even when the <code>Cancel</code> button was pressed.<br>
Maybe there was an empty segmentation called <code>Segmentation</code> already present, and I didn’t add any segments to it, because I instead created a new segmentation called (say) <code>Body parts</code> to contain the relevant segments.<br>
Would that cause the behaviours described?</p>
<p>In that case a clean-up of the unwanted <code>Segmentation</code> node could be desirable.  (Or perhaps producing a more low-key warning, rather than a hyped-up “error” message.)<br>
But — if so — please keep in mind that the converse might also apply.  Suppose I create one segmentation called <code>Heart parts</code> and then create several segments in it;  then I create another segmentation called <code>Lung parts</code>, but before creating any segments in it I save the scene &amp; all associated files, close 3D Slicer and go have lunch.  When I come back and try to reload the scene file, I’ll expect to find the empty <code>Lung parts</code> segmentation;  I wouldn’t want to get an error message, but nor would I like to find that an object I’ve expressly created has been covertly deleted.</p>
<p>Per your feature request, this might be a useful addition to the warning:</p>
<ul>
<li>“Warning, empty nodes found”</li>
<li>specify details,</li>
<li>give user option to fix ‘problem’ by deleting unused node, or ignore once, or ignore always,</li>
</ul>
<p>—DIV</p>

---

## Post #4 by @lassoan (2022-04-03 13:39 UTC)

<p>If you can describe any specific scenario that produces invalid/orphan nodes (that cause errors after saving and loading the scene) then let us know and we should be able to fix it.</p>
<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="22801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>“Warning, empty nodes found”</p>
</blockquote>
</aside>
<p>Empty nodes (e.g., markups without control points, segmentation without segments, empty segments, etc.) are not errors because these empty nodes are often used as templates. We don’t report them as errors. If you find that loading an empty node leads to a loading error then let us know.</p>
<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="22801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<ul>
<li>specify details,</li>
<li>give user option to fix ‘problem’ by deleting unused node, or ignore once, or ignore always,</li>
</ul>
</blockquote>
</aside>
<p>The <a href="https://github.com/Slicer/Slicer/issues/6298">feature request</a> was submitted to cover these. Feel free to add more details.</p>

---

## Post #5 by @DIV (2022-04-03 13:59 UTC)

<p>Thanks for the clarification.  It seems that I misinterpreted the Github link preview, which literally mentioned “empty nodes”.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="22801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer/issues/6298" class="inline-onebox" rel="noopener nofollow ugc">Remove unused nodes from the scene · Issue #6298 · Slicer/Slicer · GitHub</a></p>
</blockquote>
</aside>
<p>I have had a quick look inside one offending <code>MRML</code> file [my reference:  00102].</p>
<p>This node produced the reported error:<br>
<code> &lt;Segmentation   id="vtkMRMLSegmentationNode1" name="Segmentation" hideFromEditors="false" selectable="true" selected="false" references="display:vtkMRMLSegmentationDisplayNode1;referenceImageGeometryRef:vtkMRMLScalarVolumeNode1;storage:vtkMRMLSegmentationStorageNode1;" userTags="" MasterRepresentationName="Binary labelmap" segmentListFilterEnabled="false" segmentListFilterOptions="" &gt;&lt;/Segmentation&gt;</code></p>
<p>This node is OK, even though the encoding looks pretty much the same:<br>
<code>&lt;Segmentation   id="vtkMRMLSegmentationNode2" name="ContrastSegmentation" hideFromEditors="false" selectable="true" selected="false" references="display:vtkMRMLSegmentationDisplayNode2;referenceImageGeometryRef:vtkMRMLScalarVolumeNode1;storage:vtkMRMLSegmentationStorageNode2;" userTags="" MasterRepresentationName="Binary labelmap" segmentListFilterEnabled="false" segmentListFilterOptions="" &gt;&lt;/Segmentation&gt;</code></p>
<p><code>vtkMRMLSegmentationNode1</code> is only mentioned as above and here<br>
<code>&lt;SubjectHierarchyItem id="181" dataNode="vtkMRMLSegmentationNode1" parent="3" type="Segmentations" expanded="true" attributes="VirtualBranch^1|"&gt;&lt;/SubjectHierarchyItem&gt;</code></p>
<p>On the other hand, <code>vtkMRMLSegmentationNode2</code> is mentioned as above and also within the <code>SegmentEditor</code> tag, and the <code>ScriptedModule</code> tag, and in<br>
<code> &lt;SubjectHierarchyItem id="182" dataNode="vtkMRMLSegmentationNode2" parent="30" type="Segmentations" expanded="true" attributes="VirtualBranch^1|"&gt;            &lt;SubjectHierarchyItem id="183" name="Rt ICA" parent="182" type="Segments" expanded="true" attributes="Level^VirtualBranch|segmentID^Segment_1|"&gt;&lt;/SubjectHierarchyItem&gt;            &lt;SubjectHierarchyItem id="222" name="Confluence of sinuses" parent="182" type="Segments" expanded="true" attributes="Level^VirtualBranch|segmentID^Segment_2|"&gt;&lt;/SubjectHierarchyItem&gt;&lt;/SubjectHierarchyItem&gt;</code><br>
which shows the hierarchy of usage.</p>
<p>But still not sure what part of the encoding is producing an error, distinct from just an ‘empty’ node.</p>

---

## Post #6 by @lassoan (2022-04-03 14:23 UTC)

<p>If scene loading reports errors then the issue is most likely in the <em>segmentation storage</em> nodes and not in the <em>segmentation</em> nodes.</p>

---

## Post #7 by @jamesobutler (2022-04-03 15:10 UTC)

<p>I can only replicate the situation if I do the following:</p>
<ul>
<li>Launch Slicer, load MRHead, go to Segment Editor module (auto-creates “Segmentation” node), create new segmentation as “MySegmentation”, add a segment and paint in the slice views. Then go to “Save Data” and choose to select all items since the “Segmentation” node was not checked to save.  Save and then close Slicer.</li>
<li>From the saved location, delete the “Segmentation.seg.nrrd” file. Then launch Slicer, load the mrml scene and observe the same error as indicated by <a class="mention" href="/u/div">@DIV</a>. In the Data module there is a “Segmentation” node, but it wasn’t the one actually saved as I had manually deleted that file from the saved location.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d70d53ffd1cafbe95f2abfd9564cc94b6a73bd7c.png" alt="image" data-base62-sha1="uGrd74mKiROV6CrgMBFrNyUOQtS" width="502" height="243"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37f58626ae911ea3ea646a5bfba47b895164c6c.png" alt="image" data-base62-sha1="yK4RoH0lKPxNy5gACoqvHs1dAuM" width="560" height="207"></li>
</ul>

---

## Post #8 by @DIV (2022-04-04 05:57 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="22801">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I can only replicate the situation if I do the following:</p>
</blockquote>
</aside>
<p>Thanks for providing a concrete series of steps to replicate the issue, James.</p>
<p>For the record, I can confidently say that I didn’t knowingly delete any <code>*.seg.nrrd</code> file(s);  however, potentially it might have been corrupted or gone missing for some unknown reason.  As I mentioned though, it seems to have been not only with one single patient:  there were a handful for which I believe this happened, which makes me think it was something ‘systematic’.<br>
I’m open to all possibilities:  maybe 3D Slicer instructed the OS to write the file, but the OS didn’t obey, or it was blocked by an antivirus program that doesn’t trust <code>*.seg.nrrd</code> file(s) — not proposing those as explanations <em>per se</em>, just illustrating that I don’t know for sure it’s a 3D Slicer issue/bug.</p>

---
