# Optimize segment editor effect speed for larger segments

**Topic ID**: 9223
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/optimize-segment-editor-effect-speed-for-larger-segments/9223

---

## Post #1 by @Netta_Z (2019-11-19 23:37 UTC)

<p>Hi,</p>
<p>I’m trying to enable continuous cutting of segments by another segment, specifically in virtual reality, which I’m implementing using the subtraction logical operator and the slicerVirtualReality extension. Ideally I should be able to “grind” away segments using a modifier segment. This works quite efficiently when editing smaller segments. However there is a short lag after editing larger segments for the model to update. I have set smoothing in the conversion rules to 0, selected bypassMasking, but it’s still not fast enough for my purpose. This behavior is quite noticeable when I’m in virtual reality view, as the slow update causes the entire model to “jitter” a little. In 3D view on the PC, the lag is there but more difficult to see.</p>
<p>Steps to reproduce on PC:</p>
<ol>
<li>Create segmentation nodes containing sample segments of contrasting sizes</li>
<li>Import model and convert to binary labelmap, import this to a new segmentation node which will be the modifier segment for the logical operator</li>
<li>Transform the modifier segmentation node so that it overlaps with the sample segments</li>
<li>Copy the modifier segment into a node containing a sample segment</li>
<li>Apply subtraction logical operator to the sample segment and notice the update speed in 3D window. Compare between sample segments of various sizes. In my Python implementation, the application of editor effect can be triggered at very high frequency if the user wants to cut away on a segment continuously.</li>
</ol>
<p>I ran profiler against a slicer build, SetBinaryLabelmapToSegment() -&gt; ConvertSegmentsUsingPath() -&gt; Convert() -&gt; Update() is taking most of the CPU time when editor effect is applied. It makes sense that this process is proportional to the sizes of the segments. How I can further improve the conversion update speed so that I don’t see the lag? Is there a faster way to edit segments than the logical operator? Any ideas are greatly appreciated.</p>
<p>Operating system: Windows 10<br>
Slicer version: Nightly 4.11<br>
Expected behavior: Instantaneous update of modified segments in virtual reality view<br>
Actual behavior: Short lag after modifying a larger segment with segment editor, preventing continuous application of the effect.</p>

---

## Post #2 by @lassoan (2019-11-20 20:47 UTC)

<p>Probably the only reliable way to keep the virtual reality view refreshing uninterrupted is to avoid doing time-consuming operation on the main thread.</p>
<p>Conversion from binary labelmap to closed surface is a time-consuming operation and it is performed automatically (on the main thread) if the binary labelmap representation is changed by an effect. To avoid this, you could do the following:</p>
<ul>
<li>clone an existing editor effect and change it so that it does not immediately update the binary labelmap representation (which would trigger the lengthy processing on the main thread)</li>
<li>the effect would start a background thread to compute the updated labelmap and the corresponding closed surface representation without blocking the main thread</li>
<li>when the computation is done then the effect would set the updated representations into the segment at once (this update is done on the main thread, but since it is just changing a pointer value, it would happen instantly)</li>
</ul>
<p>Threading in Python is a difficult topic and it is further complicated by the fact that Slicer is running an embedded Python interpreter, so most probably you would be better of implementing this effect in a loadable module in C++.</p>

---

## Post #3 by @Netta_Z (2019-11-21 16:54 UTC)

<p>Thank you for the detailed response, Andras. I will be trying this out. Are there any existing implementation of threading for editor effects, updates etc. that I could refer to?</p>

---

## Post #4 by @lassoan (2019-11-21 18:43 UTC)

<p>Most multithreading are done inside filters. There are some background processing in CLI module execution logic (vtkSlicerCLIModuleLogic) and background network communication in OpenIGTLink extension, but they are both somewhat different and quite complicated, so you cannot reuse much from them.</p>
<p>You need to decide what programming language would you use (I would recommend C++ for this) and if you want to use VTK or Qt for multithreading (probably VTK would suffice, but Qt has many more features and better documented and there are more examples), and then just start working on it. If you develop the editing effect in a public repository then we can help with specific questions about the code.</p>

---

## Post #5 by @Netta_Z (2019-12-11 18:03 UTC)

<p>Thank you for the suggestion. I’ve started writing the editor effect as part of an extension in C++ and I’m having difficulties deciding on the module architecture. My new effect is written similar to the existing loadable effects such as paint and scissors, but I notice that these effects are registered using <code>qSlicerSegmentEditorEffectFactory</code> during <code>qSlicerSegmentationsModule::setup()</code>. Does this mean I should implement the new effect as part of a new module so that it can be registered properly?  I wasn’t sure as this seemed redundant, it would make more sense to utilize the existing Segmentations module. However, I couldn’t figure out how to get my new editor effect to load in Slicer like the others, showing up in Segment Editor GUI and getting called by segment editor widget etc. Another thought is to implement the base functionalities of the effect in C++ (specifically the processing that requires multithreading) then call these functions from a Python script, in which editor effect implementation is better supported. Which approach would be better?</p>

---

## Post #6 by @lassoan (2019-12-11 18:19 UTC)

<aside class="quote no-group" data-username="Netta_Z" data-post="5" data-topic="9223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/netta_z/48/4697_2.png" class="avatar"> Netta_Z:</div>
<blockquote>
<p>Does this mean I should implement the new effect as part of a new module so that it can be registered properly? I wasn’t sure as this seemed redundant,</p>
</blockquote>
</aside>
<p>You need to package all features into a module (otherwise Slicer would have no way of determining what is inside a library and how to use it, what are the dependencies, etc.). The module does not have to have a GUI -it can be hidden from the user. You just need to add a module class (and maybe an empty logic class). The module class can register the Segment Editor plugin.</p>
<aside class="quote no-group" data-username="Netta_Z" data-post="5" data-topic="9223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/netta_z/48/4697_2.png" class="avatar"> Netta_Z:</div>
<blockquote>
<p>Another thought is to implement the base functionalities of the effect in C++ (specifically the processing that requires multithreading) then call these functions from a Python script, in which editor effect implementation is better supported. Which approach would be better?</p>
</blockquote>
</aside>
<p>You can certainly do this. Registering a segment editor effect is a single method call, so it does not matter much what language you use. Overall, it is pro a ly somewhat simpler to put everything (effect registration, effect class, processing logic) in a single C++ loadable module.</p>

---
