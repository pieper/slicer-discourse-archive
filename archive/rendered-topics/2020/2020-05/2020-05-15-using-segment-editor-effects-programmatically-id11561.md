---
topic_id: 11561
title: "Using Segment Editor Effects Programmatically"
date: 2020-05-15
url: https://discourse.slicer.org/t/11561
---

# Using Segment Editor effects programmatically

**Topic ID**: 11561
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/using-segment-editor-effects-programmatically/11561

---

## Post #1 by @mangotee (2020-05-15 17:02 UTC)

<p>Hi all,<br>
I’m wondering how to script some simple steps from the Segment Editor. I know that there are a few recipes from Andras and others in this forum, which are great, thanks for the continuous support.<br>
In one of the recipes, there is a good example for thresholding:</p>
<pre><code class="lang-auto">#Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","35")
effect.setParameter("MaximumThreshold","695")
effect.self().onApply()
</code></pre>
<p>Now, the effect I wanna use programmatically is “Logical operators”, specifically I wanna create a hull, i.e. one segment that sums up all the other segments (in other words, a logical_or of all segments contained in the segmentation node), which is easy to automate. The steps I need to do are:</p>
<ol>
<li>Create a new segment (via node_seg.GetSegmentation().AddSegment(‘hull’))</li>
<li>Copy the first segment into ‘hull’</li>
<li>Add all other segments into ‘hull’.</li>
</ol>
<p>For this, and other simple steps… Is there a documentation on all the parameters of all effects.<br>
I was trying something like:</p>
<pre><code class="lang-auto">segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter('Operation','Copy')
</code></pre>
<p>But I have no idea whether these parameters are correct (and there are no error messages, even if I enter random strings).</p>
<p>Thanks in advance!</p>

---

## Post #2 by @mangotee (2020-05-15 18:35 UTC)

<p>I found some more information <a href="https://discourse.slicer.org/t/scissors-segment-editor-effects-from-a-script/8348/2">in this thread</a>, and after activating the the “Logical operators” operations one-by-one, I got this list of parameters:</p>
<pre><code class="lang-auto">  Logical operators.BypassMasking:1
  Logical operators.ModifierSegmentID:Segment_11
  Logical operators.Operation:COPY
  Logical operators.Operation:UNION
  Logical operators.Operation:SUBTRACT
  Logical operators.Operation:INTERSECT
  Logical operators.Operation:INVERT
  Logical operators.Operation:CLEAR
  Logical operators.Operation:FILL
</code></pre>
<p>I will try a bit more, but for future reference, is there a documentation page with the full list of these parameters?</p>

---

## Post #3 by @lassoan (2020-05-16 04:46 UTC)

<p>It would be nice to create separate documentation for these - contributions are welcome!</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, do you have any suggestions for documenting segment editor effect parameters? It would be nice if documentation would be available at the same place for C++ and Python effects. I could create a new markdown file in developer_guide and describe parameters of the effects there, but it would be a bit nicer if the description could be in each effect’s .py or .h file. Could ReadTheDocs fetch documentation from segment editor effect source files (currently <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html">Developer guide</a> does not seem to be able to get anything from there).</p>
<p>Until separate documentation is written, then open source code is <em>the</em> documentation. You can find the relevant file by Google search. For example first hit when searching for <code>github slicer Logical operators</code> takes you to <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLogicalEffect.py">SegmentEditorLogicalEffect.py</a>. For all Segment Editor effects, <code>setMRMLDefaults</code> method contains the list of parameters that the effect uses. If there are constants then they are typically defined at the bottom of the file.</p>

---

## Post #4 by @Fangwen_Zhai (2020-08-03 18:00 UTC)

<p>Could you please elaborate a bit more on calling python effects from C++, for example, what is the C++ equivalence of <code>effect.self.OnApply()</code>?</p>

---

## Post #5 by @lassoan (2020-08-03 19:25 UTC)

<p>See this topic for details about how to run Python code from C++:</p>
<aside class="quote quote-modified" data-post="10" data-topic="7841">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/calling-python-from-c/7841/10">Calling Python from C++</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    There are several options for calling Python from C++ (one of them is shown in my comment above, using evalScript) and it is done at many places in Slicer. However, C++ modules provide low-level infrastructure, so it would not make sense for a C++ module to depend on Python. 
If you want to implement some performance-critical processing in C++ but other features are in Python then I would recommend to: 

create a hidden C++ loadable module that just implements performance-critical processing in …
  </blockquote>
</aside>

<p>For more complex Python calls, search for “pythonmanager” in Slicer source code.</p>

---

## Post #6 by @mangotee (2020-08-31 10:33 UTC)

<p>Hi Andras,<br>
few weeks ago, I found an alternative way to solve my problem, but now I had to come back to using segment editor effects, in more detail. This time I managed to solve a few problems, one of them was how to use the “logical operators” effect programmatically. You already provide a lot of examples for scripted effects <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">here</a>, but there is no example for the logical effects. Actually it’s simple, but I needed to sift through the source code a bit. Maybe this example will help others to save some time.</p>
<pre><code># Run segment editor effects from script

# Prerequisites 1/2: 
# Create segment editor widget and node to get scripted access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

# Prerequisites 2/2:
# nvol ... the reference volume node for the segmentation
# nseg ... the segmentation node
# 'tgtseg' is the name of the target segment, i.e. the region that is being edited
# 'srcseg' is the name of the source segment, i.e. the region from which information is being "transferred" by the logical operator
# Setting up the nodes to be edited
segmentEditorWidget.setSegmentationNode(nseg)
segmentEditorWidget.setMasterVolumeNode(nvol)
# Set overwrite mode: 0/1/2 -&gt; overwrite all/visible/none
segmentEditorNode.SetOverwriteMode(2) # i.e. "allow overlap" in UI
# Get the segment IDs
segid_tgt = nseg.GetSegmentation().GetSegmentIdBySegmentName('tgtseg')
segid_src = nseg.GetSegmentation().GetSegmentIdBySegmentName('srcseg')

# Running the effect:
# The logical operation is set via strings
# 'COPY', 'UNION', 'INTERSECT', 'SUBTRACT', 'INVERT', 'CLEAR', 'FILL'
# (see: https://apidocs.slicer.org/master/SegmentEditorLogicalEffect_8py_source.html)    
segmentEditorNode.SetSelectedSegmentID(segid_tgt)
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation","COPY") # change the operation here
effect.setParameter("ModifierSegmentID",segid_src)
effect.self().onApply()</code></pre>

---

## Post #7 by @lassoan (2020-08-31 19:56 UTC)

<p>Thanks a lot for sharing.</p>

---
