---
topic_id: 13433
title: "Show Hide Slice Views Widget"
date: 2020-09-11
url: https://discourse.slicer.org/t/13433
---

# Show/Hide slice views widget

**Topic ID**: 13433
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/show-hide-slice-views-widget/13433

---

## Post #1 by @sogo (2020-09-11 05:03 UTC)

<p>Hi,<br>
This topic is from this discussion previously:<br>
<a href="https://discourse.slicer.org/t/show-hide-slice-views-in-3d-view-using-python/3074/2">Show/Hide Slice Views</a><br>
From this discussion, I found that it is possible to Show/Hide the (‘Red’ ‘Green’ ‘Yellow’) slice view widgets but it is not working for me. I’m trying to hide all the slice view widgets for my loadable module as it does not need it by using this code:</p>
<blockquote>
<p>vtkMRMLNode* node = qSlicerApplication::application()-&gt;mrmlScene()-<br>
GetNodeByID(“vtkMRMLSliceNodeYellow”);<br>
vtkMRMLSliceNode *sliceNode = vtkMRMLSliceNode::SafeDownCast(node);<br>
sliceNode-&gt;SetSliceVisible(0);</p>
</blockquote>
<p>but nothing happens when I call it.<br>
<strong>Note: Currently trying for only yellow and if it works will do for the rest in for loop.</strong><br>
So I tried the above thread and put the commands in python interactor:</p>
<blockquote>
<p>red = getNode(‘vtkMRMLSliceNodeRed’)<br>
red.SetSliceVisible(0)</p>
</blockquote>
<p>But still it does not hide. I wanted to ask is it possible to hide the complete views panel so that the module panel can take all that space? Thanks</p>

---

## Post #2 by @lassoan (2020-09-11 05:13 UTC)

<p><code>SetSliceVisible</code> controls visibility of a slice in the 3D view.</p>
<p>View widgets are standard Qt widgets, so you can call its <code>hide()</code> method to hide it. You can make the entire view layout go away by hiding parent widgets.</p>

---

## Post #3 by @sogo (2020-09-11 08:53 UTC)

<p>Hi Andras,<br>
Thanks for your response. Your comment got me looking for underlying widget. So I found the qSlicerMRMLWidget to be the widget setting up slice views panel and I was able to get underlying handle for the three views like this:</p>
<blockquote>
<p>qSlicerLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();<br>
qMRMLSliceWidget* red = layoutManager-&gt;sliceWidget(“Red”);<br>
qMRMLSliceWidget* yellow = layoutManager-&gt;sliceWidget(“Yellow”);<br>
qMRMLSliceWidget* green = layoutManager-&gt;sliceWidget(“Green”);<br>
red-&gt;hide();<br>
yellow-&gt;hide();<br>
green-&gt;hide();</p>
</blockquote>
<p>Some issues so far are:<br>
1- This works well on linux centOS8 but not on windows 10. I will look into it a little more</p>

---

## Post #4 by @trash_imp (2021-08-22 14:38 UTC)

<aside class="quote no-group quote-modified" data-username="sogo" data-post="3" data-topic="13433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/779978/48.png" class="avatar"> sogo:</div>
<blockquote>
<p>Some issues so far are:<br>
1- This works well on Linux centOS8 but not on windows 10. I will look into it a little more</p>
</blockquote>
</aside>
<p>Could you please tell any updates regarding this issue.</p>

---

## Post #5 by @lassoan (2021-08-23 14:44 UTC)

<p>I can confirm that the code above works perfectly on Windows10, too.</p>
<p>You can copy paste this into the Python console:</p>
<pre><code class="lang-python">layoutManager = slicer.app.layoutManager()
red = layoutManager.sliceWidget("Red")
yellow = layoutManager.sliceWidget("Yellow")
green = layoutManager.sliceWidget("Green")
red.hide()
yellow.hide()
green.hide()
</code></pre>
<p>Most likely that the different behavior that you see is not due to operating system difference but in what layout you create and when you try to hide the widgets inside it. Most likely you hide the widgets before they are even shown, so hiding has no effect.</p>

---

## Post #6 by @sogo (2021-08-31 00:03 UTC)

<p>Hi <a class="mention" href="/u/trash_imp">@trash_imp</a><br>
Not sure if it will help but what I did to hide all the slice views was to get the underlying handle to the frame that populates all the slice views using this code and then hide that frame completely:</p>
<pre><code class="lang-auto">QFrame* frame = qobject_cast&lt;QFrame*&gt;(layout-&gt;sliceWidget("Red")-&gt;parent());
frame-&gt;hide();
</code></pre>
<p>Another way to do it is:</p>
<pre><code class="lang-auto">qSlicerApplication::application()-&gt;mainWindow()-&gt;
            findChild&lt;QWidget*&gt;("CentralWidget")-&gt;findChild&lt;QFrame*&gt;("CentralWidgetLayoutFrame")-&gt;hide();
</code></pre>
<p>I haven’t used the method as I went to do something different, but they both worked for me.</p>

---
