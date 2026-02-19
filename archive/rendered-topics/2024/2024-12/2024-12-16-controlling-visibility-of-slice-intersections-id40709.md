---
topic_id: 40709
title: "Controlling Visibility Of Slice Intersections"
date: 2024-12-16
url: https://discourse.slicer.org/t/40709
---

# Controlling visibility of slice intersections

**Topic ID**: 40709
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/controlling-visibility-of-slice-intersections/40709

---

## Post #1 by @shai-ikko (2024-12-16 10:37 UTC)

<p>Hello,</p>
<p>I’m trying to get a layout where one slice view serves as “target” and other slice views serve as “controls”. So, I want to make the target slice (“intersection”) visible in the controls, but not vice versa, and of course I don’t want the control slices visible in each other. In some situations, I also don’t want target slice visible in a specific control slice.</p>
<p>By reading the documentation, it looked like I could have all the control I wanted by using two different methods on the SliceDisplayNodes:</p>
<ul>
<li><code>SetVisibility2D()</code>: Set the 2D visibility of the display node.<br>
would control if a slice can be shown in other slices</li>
<li><code>SetIntersectingSlicesVisibility()</code>: Toggles visibility of intersections of other slices in the slice viewer.<br>
would  control if the slice viewer shows the other slice intersections</li>
</ul>
<p>So I thought the intersection would only be visible if both “sides”, so to speak, are on. But it didn’t quite work this way; playing with these flags caused all sorts of unwanted effects. I finally cheked the source, and found (vtkMRMLSliceDisplayNode.h, line 53):</p>
<pre><code class="lang-auto">void SetIntersectingSlicesVisibility(bool visible) { this-&gt;SetVisibility2D(visible); };
</code></pre>
<p>which explains a lot.</p>
<p>Is the bug in the docs or in the code?</p>

---

## Post #2 by @cpinter (2024-12-16 12:45 UTC)

<p>The function seems to work exactly the way it is documented.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceDisplayNode.h#L51">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceDisplayNode.h#L51" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceDisplayNode.h#L51" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSliceDisplayNode.h#L51</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
          <li>/// Copy node content (excludes basic data, such as name and node references).</li>
          <li>/// \sa vtkMRMLNode::CopyContent</li>
          <li>vtkMRMLCopyContentMacro(vtkMRMLSliceDisplayNode);</li>
          <li></li>
          <li>vtkMRMLNode* CreateNodeInstance() override;</li>
          <li></li>
          <li>/// Get node XML tag name (like Volume, Model)</li>
          <li>const char* GetNodeTagName() override {return "SliceDisplay";}</li>
          <li></li>
          <li>//@{</li>
          <li class="selected">/// Toggles visibility of intersections of other slices in the slice viewer</li>
          <li>bool GetIntersectingSlicesVisibility() { return this-&gt;GetVisibility2D(); };</li>
          <li>void SetIntersectingSlicesVisibility(bool visible) { this-&gt;SetVisibility2D(visible); };</li>
          <li>vtkBooleanMacro(IntersectingSlicesVisibility, bool);</li>
          <li>//@}</li>
          <li></li>
          <li>//@{</li>
          <li>/// Toggles visibility of thick slabs of other slices in the slice viewer</li>
          <li>vtkGetMacro(IntersectingThickSlabVisibility, bool);</li>
          <li>vtkSetMacro(IntersectingThickSlabVisibility, bool);</li>
          <li>vtkBooleanMacro(IntersectingThickSlabVisibility, bool);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The text is<br>
“Toggles visibility of intersections of other slices in the slice viewer”<br>
which means that intersections of the other slices (i.e. the colored lines) will appear in <em>the</em> slice viewer, which is the slice view that uses the display node in question. Seems quite unambiguous to me.</p>

---

## Post #3 by @shai-ikko (2024-12-16 14:17 UTC)

<p>Let me explain more concretely.</p>
<p>Assume the standard view. I want to show the intersection of the red slice in the green slice, and no other intersections.</p>
<p>After reading the documentation, I thought I’d be able to achieve this with:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
r, y, g = (
    lm.sliceWidget(t).sliceLogic().GetSliceDisplayNode()
    for t in ("Red", "Yellow", "Green")
)
g.IntersectingSlicesVisibilityOn()
r.Visibility2DOn()
</code></pre>
<p>But that gives me (after making sure all slices are updated)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd6b6a32a8a429c2dc251ecafa4b06e259374793.jpeg" data-download-href="/uploads/short-url/vALEGp8TxIUPVag27ePvBS1y427.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd6b6a32a8a429c2dc251ecafa4b06e259374793_2_690x293.jpeg" alt="image" data-base62-sha1="vALEGp8TxIUPVag27ePvBS1y427" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd6b6a32a8a429c2dc251ecafa4b06e259374793_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd6b6a32a8a429c2dc251ecafa4b06e259374793_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd6b6a32a8a429c2dc251ecafa4b06e259374793.jpeg 2x" data-dominant-color="514F4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×460 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Also note the setting of the yellow slice:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; y.GetVisibility2D()
0
&gt;&gt;&gt; y.GetSliceIntersectionVisibility()
0
</code></pre>
<p>According to the documentation, I should have seen no intersections in the yellow slice, no matter what happens in the red and green. And in fact, there is no way for me to say “Red, be visible in others but don’t show others; Green, show others in yourself but be invisible to others”.</p>
<p>The piece of code I quoted (and you pointed to as well) shows that, in fact, there is no separation between “am I visible in other slices” and “am I showing other slices” – the interface that is documented to do the latter, does the former.</p>
<p>The question was – is this effect intended? If so, the doc is wrong. If not, it is the code.</p>

---

## Post #4 by @cpinter (2024-12-16 14:56 UTC)

<p>The first 95% of your description stands. There is no “two-sided” definition. The only thing we can turn on and off is whether “the intersections of the <em>other</em> slices in this slice in the layout view group are visible” or not.</p>
<aside class="quote no-group" data-username="shai-ikko" data-post="3" data-topic="40709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<p>If so, the doc is wrong. If not, it is the code.</p>
</blockquote>
</aside>
<p>This part, however, I don’t understand. Do you agree with my previous answer that the documentation of the Get/SetIntersectingSlicesVisibility function is correct?</p>

---

## Post #5 by @shai-ikko (2024-12-16 15:01 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="40709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Do you agree with my previous answer that the documentation of the Get/SetIntersectingSlicesVisibility function is correct?</p>
</blockquote>
</aside>
<p>No.</p>
<p>The documentation, as far as I can get it, and as far as I read your interpretation of it as well, says that when, in my example above, <code>y.GetSliceIntersectionVisibility()</code> returns 0 – that is, when <code>SliceIntersctionVisibility</code> is off for the yellow slice – then you should see no intersections of other slices in the yellow slice.</p>
<p>What actually happens, as exemplified above, is the reverse. It is the intersections of the yellow slice that are hidden elsewhere.</p>

---

## Post #6 by @cpinter (2024-12-16 15:03 UTC)

<p>I think that the description “Toggles visibility of intersections of other slices in the slice viewer” is quite straightforward. I explained it in more detail above. If this bothers you and want to spend some time please issue a PR suggesting a different description.</p>

---

## Post #7 by @shai-ikko (2024-12-16 15:13 UTC)

<p>Please answer this question:</p>
<p>When the display node related to a slice view has <code>SliceIntersectionVisibility</code> off – should I, or shouldn’t I, see intersections of other slices in this view?</p>
<p>(I guess the question is the meaning of “the intersections of the other slices in this slice”. I understand this to mean – the lines representing the other slices in the view for this one. I fail to see how one understands the converse).</p>

---

## Post #8 by @cpinter (2024-12-16 15:22 UTC)

<p>You’re right. I was convinced that it works as described, but I just tried it myself and it works the opposite way, it controls the visibility of the slice intersection of the current slice in the other slice views of the layout view group. I think I never realized this because I always use it on all the slices, and not individually.</p>
<p>At this point I’d update the documentation because many other functions rely on this one.</p>
<p>Here’s a snippet that only turns it on for the red slice:</p>
<pre><code class="lang-auto">import SampleData
mrNode = SampleData.SampleDataLogic().downloadMRHead()

lm = slicer.app.layoutManager()
sw = lm.sliceWidget('Red')
sd = sw.sliceLogic().GetSliceDisplayNode()
sd.SetSliceIntersectionVisibility(True)  # Equivalent to sd.SetVisibility2D(True)
</code></pre>

---

## Post #9 by @shai-ikko (2024-12-16 15:28 UTC)

<p>Thanks for this, and for your patience.</p>
<p>(the example, of course turns on only the red slice’s intersections – but still turns it on in both the green and the yellow slices, so it’s not a solution for my use case)</p>

---

## Post #10 by @cpinter (2024-12-16 15:49 UTC)

<aside class="quote no-group" data-username="shai-ikko" data-post="9" data-topic="40709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<p>but still turns it on in both the green and the yellow slices, so it’s not a solution for my use case</p>
</blockquote>
</aside>
<p>My only idea now is to play with the layout view groups, but I don’t have much faith in that, because I think you can either show the intersection in all slice views in the same group, and nothing in other gropus (this can be confirmed by adding a new layout by the XML text, which defines different view groups).</p>
<p>If you have a suggestion for a better way to define slice intersection visibilities, we’re happy to discuss it.</p>

---

## Post #11 by @shai-ikko (2024-12-16 16:03 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="40709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>My only idea now is to play with the layout view groups</p>
</blockquote>
</aside>
<p>Thanks – I’ll look into that (but not today).</p>
<p>For now, I submitted <a href="https://github.com/Slicer/Slicer/issues/8100" class="inline-onebox" rel="noopener nofollow ugc">vtkMRMLSliceDisplayNode.SetIntersectingSlicesVisibility() doesn't quite · Issue #8100 · Slicer/Slicer · GitHub</a></p>

---

## Post #12 by @shai-ikko (2024-12-18 13:36 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="40709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>My only idea now is to play with the layout view groups, but I don’t have much faith in that, because I think you can either show the intersection in all slice views in the same group, and nothing in other gropus (this can be confirmed by adding a new layout by the XML text, which defines different view groups).</p>
</blockquote>
</aside>
<p>This turned out to be good enough for me – it’s not full control, but it’s enough if you only want to show the intersections of one slice. And it turns out you don’t really need to touch XML, because <code>vtkMRMLSliceNode</code> inherits a <code>GetViewGroup()</code> and a <code>SetViewGroup()</code> from <code>vtkMRMLAbstractViewNode</code>, which let you control the groups <em>dynamically</em> for existing slice views. Putting a slice in a separate view group has some other effects – in my case, they don’t matter, and they may not matter for other users as well. The effects are explained in the <a href="https://apidocs.slicer.org/v5.2/classvtkMRMLAbstractViewNode.html#a896bad470fb25f642165eb6305eee4fc" rel="noopener nofollow ugc">documentation for <code>SetViewGroup()</code></a>.</p>
<p>To summarize, if you want to show the intersection of the Red slice in the Green slice and not in the Yellow:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
rsw, gsw, ysw = [lm.sliceWidget(color) for color in ("Red", "Green", "Yellow")]
# Make Red slice's intersection line visible in other slices
rsd = rsw.sliceLogic().GetSliceDisplayNode()
rsd.SetSliceIntersectionVisibility(True)
# To work with view groups, we need the SliceNode's
rsn, gsn, ysn = [sw.mrmlSliceNode() for sw in (rsw, gsw, ysw)]
# Assume Red and Green are in the default view group
assert rsn.GetViewGroup() == gsn.GetViewGroup() == 0
# Set Yellow to a separate group
ysn.SetViewGroup(1)
# Make sure the slices are updated, otherwise the line appearance is delayed
for sn in (rsn, gsn, ysn): sn.Modified()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12592a5cd06c2542e137e27438b3231c01bd9db0.jpeg" data-download-href="/uploads/short-url/2CjD67E52uEReicpnoKgHPY70Iw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12592a5cd06c2542e137e27438b3231c01bd9db0_2_690x223.jpeg" alt="image" data-base62-sha1="2CjD67E52uEReicpnoKgHPY70Iw" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12592a5cd06c2542e137e27438b3231c01bd9db0_2_690x223.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12592a5cd06c2542e137e27438b3231c01bd9db0_2_1035x334.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12592a5cd06c2542e137e27438b3231c01bd9db0.jpeg 2x" data-dominant-color="42403B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1085×351 87.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
