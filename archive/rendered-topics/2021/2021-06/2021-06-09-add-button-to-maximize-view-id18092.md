---
topic_id: 18092
title: "Add Button To Maximize View"
date: 2021-06-09
url: https://discourse.slicer.org/t/18092
---

# Add button to maximize view

**Topic ID**: 18092
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/add-button-to-maximize-view/18092

---

## Post #1 by @trash_imp (2021-06-09 06:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<ul>
<li>
<p>For accessing <code>qMRMLLayoutManager::setLayout</code> function in <code>qMRMLThreeDViewControllerWidget</code>, I need an instance of <code>qMRMLLayoutManager</code>.</p>
</li>
<li>
<p>So, how can I get the <code>qMRMLLayoutManager</code> instance in <code>qMRMLThreeDViewControllerWidget</code>. Or is there any other way of accessing <code>qMRMLLayoutManager::setLayout</code>.</p>
</li>
</ul>

---

## Post #2 by @lassoan (2021-06-09 21:33 UTC)

<p>How this should probably work is that the widget would set a <code>maximizedLayoutName</code> (layout name of the maximized view) in the <code>vtkMRMLLayoutNode</code>. You can get the layout node from the scene: if <code>ParentLayoutNode</code> is set in the view node then you will use that node, otherwise you will look up the default layout manager node (it is a singleton).</p>
<p>The layout manager gets a notification about the layout node change and it will hide all layout elements from the view except the widget that corresponds to <code>maximizedLayoutName</code>.</p>

---

## Post #3 by @trash_imp (2021-06-10 03:37 UTC)

<p>Instead of creating a new function (<code>maximizedLayoutName</code>) there is already a <code>setLayout</code> function in <code>qMRMLLayoutManager</code>. Will there be any problem if I use that?</p>
<p>code:</p>
<pre><code class="lang-auto">void qMRMLLayoutManager::setLayout(int layout)
{
  Q_D(qMRMLLayoutManager);
  if (this-&gt;layout() == layout)
    {
    return;
    }
  // Update LayoutNode
  if (d-&gt;MRMLLayoutNode)
    {
    if (!d-&gt;MRMLLayoutNode-&gt;IsLayoutDescription(layout))
      {
      layout = vtkMRMLLayoutNode::SlicerLayoutConventionalView;
      }
    d-&gt;MRMLLayoutNode-&gt;SetViewArrangement(layout);
    }
}
</code></pre>
<p><code>MRMLLayoutNode</code> is a pointer of <code>vtkMRMLLayoutNode*      MRMLLayoutNode;</code></p>
<p>code for <code>IsLayoutDescription</code> in <code>vtkMRMLLayoutNode</code>:</p>
<pre><code class="lang-auto">bool vtkMRMLLayoutNode::IsLayoutDescription(int layout)
{
  std::map&lt;int, std::string&gt;::const_iterator it = this-&gt;Layouts.find(layout);
  return it != this-&gt;Layouts.end();
}
</code></pre>
<p>code for <code>SetViewArrangement</code> in <code>vtkMRMLLayoutNode</code>:</p>
<pre><code class="lang-auto">void vtkMRMLLayoutNode::SetViewArrangement(int arrNew)
{
 // if the view arrangement definition has not been changed, return
 if ( this-&gt;ViewArrangement == arrNew
   &amp;&amp; this-&gt;GetCurrentLayoutDescription()
   &amp;&amp; this-&gt;GetCurrentLayoutDescription() == this-&gt;GetLayoutDescription(arrNew) )
   {
   return;
   }
 this-&gt;ViewArrangement = arrNew;
#if 1
 if (!this-&gt;IsLayoutDescription(this-&gt;ViewArrangement))
   {
   vtkWarningMacro(&lt;&lt; "View arrangement " &lt;&lt; this-&gt;ViewArrangement
                   &lt;&lt; " is not recognized, register it with "
                   &lt;&lt; "AddLayoutDescription()");
   }
#endif
 int wasModifying = this-&gt;StartModify();
 this-&gt;UpdateCurrentLayoutDescription();
 this-&gt;Modified();
 this-&gt;EndModify(wasModifying);
}
</code></pre>

---

## Post #4 by @lassoan (2021-06-10 03:57 UTC)

<p>Maximizing a view is a temporary operation. It should be possible to maximize/restore a selected view without changing the layout.</p>

---

## Post #5 by @trash_imp (2021-06-10 11:19 UTC)

<ul>
<li>How can I create an instance of <code>qMRMLLayoutManager</code> in <code>qMRMLThreeDViewControllerWidget</code>.</li>
</ul>

---

## Post #6 by @trash_imp (2021-06-10 15:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<ul>
<li>For accessing <code>vtkMRMLLayoutNode</code> I need an instance, and I can’t figure out how to initialize <code>vtkMRMLLayoutNode</code> pointer.</li>
</ul>

---

## Post #7 by @lassoan (2021-06-10 15:15 UTC)

<p>The qMRMLThreeDViewControllerWidget does not know how many layout managers the application has or how to access them. But it can get the vtkMRMLLayoutNode from the scene, because if its view node’s ParentLayoutNode is nullptr (most of the cases, except when a view is shown outside of the layout) then you can look up the vtkMRMLLayoutNode by its singleton tag (<code>scene-&gt;GetSingletonNode("vtkMRMLLayoutNode","vtkMRMLLayoutNode")</code>). When you change the <code>MaximizedLayoutName</code> property then the layout manager will detect the change and act accordingly. You need to add the new <code>MaximizedLayoutName</code> property to <code>vtkMRMLLayoutNode</code>, along with <code>GetMaximizedLayoutName</code> and <code>SetMaximizedLayoutName</code> methods to get/set it.</p>

---

## Post #8 by @lassoan (2021-06-12 12:06 UTC)

<p>I see that you marked the above answer as Stilton. Did this mean that you are going to implement the temporary maximize/restore view feature or you just switch layouts?</p>

---

## Post #9 by @trash_imp (2021-06-12 12:13 UTC)

<p>I already implemented maximizing/minimizing feature but by using switching layouts</p>
<p>code for 3D Layout:</p>
<pre><code class="lang-auto">    int layout_3D = vtkMRMLLayoutNode::SlicerLayoutOneUp3DView;
    int layout_FourUp = vtkMRMLLayoutNode::SlicerLayoutFourUpView;
    vtkMRMLLayoutNode* layoutNode = vtkMRMLLayoutNode::SafeDownCast(this-&gt;mrmlScene()-&gt;GetSingletonNode("vtkMRMLLayoutNode", "vtkMRMLLayoutNode"));
    if (layoutNode)
    {
        if (!maximumView_ThreeDView) {
            layoutNode-&gt;SetViewArrangement(layout_3D);
            maximumView_ThreeDView = true;
            d-&gt;actionCenter-&gt;setToolTip("Minimize");
        }
        else {
            layoutNode-&gt;SetViewArrangement(layout_FourUp);
            maximumView_ThreeDView = false;
            d-&gt;actionCenter-&gt;setToolTip("Maximize");
        }
    }
</code></pre>
<p>code for Axial, sagittal, cornal:</p>
<pre><code class="lang-auto">    QString x = d-&gt;ViewLabel-&gt;text();
    int layout = vtkMRMLLayoutNode::SlicerLayoutFourUpView;
    int layout_Red = vtkMRMLLayoutNode::SlicerLayoutOneUpRedSliceView;
    int layout_Yellow = vtkMRMLLayoutNode::SlicerLayoutOneUpYellowSliceView;
    int layout_Green = vtkMRMLLayoutNode::SlicerLayoutOneUpGreenSliceView;

    vtkMRMLLayoutNode* layoutNode = vtkMRMLLayoutNode::SafeDownCast(this-&gt;mrmlScene()-&gt;GetSingletonNode("vtkMRMLLayoutNode", "vtkMRMLLayoutNode"));
    if (layoutNode) {
        if (x.contains("R")) {
            if (!maximumView) {
                layoutNode-&gt;SetViewArrangement(layout_Red);
                maximumView = true;
                d-&gt;actionFit_to_window-&gt;setToolTip("Minimize");
            }
            else
            {
                layoutNode-&gt;SetViewArrangement(layout);
                maximumView = false;
                d-&gt;actionFit_to_window-&gt;setToolTip("Maximize");
            }
        }
        else if (x.contains("G")) {
            if (!maximumView) {
                layoutNode-&gt;SetViewArrangement(layout_Green);
                maximumView = true;
                d-&gt;actionFit_to_window-&gt;setToolTip("Minimize");
            }
            else
            {
                layoutNode-&gt;SetViewArrangement(layout);
                maximumView = false;
                d-&gt;actionFit_to_window-&gt;setToolTip("Maximize");
            }
        }
        else if (x.contains("Y")) {
            if (!maximumView) {
                layoutNode-&gt;SetViewArrangement(layout_Yellow);
                maximumView = true;
                d-&gt;actionFit_to_window-&gt;setToolTip("Minimize");
            }
            else
            {
                layoutNode-&gt;SetViewArrangement(layout);
                maximumView = false;
                d-&gt;actionFit_to_window-&gt;setToolTip("Maximize");
            }
        }
    }
</code></pre>
<p>And this method works, but please let me know if this is the right way to do or not.</p>

---

## Post #10 by @lassoan (2021-06-12 13:15 UTC)

<p>Thank you for sharing. This can work for a custom application where to have full control over what view layouts you allow your user to choose. However, this is not a general solution that could be used in Slicer core for several reasons. For example, there is no one-up layout for every view.</p>

---

## Post #11 by @trash_imp (2021-06-12 15:28 UTC)

<p>For implementing “temporary maximize/restore view feature”</p>
<pre><code class="lang-auto">void vtkMRMLLayoutNode::SetMaximizedLayoutName(const char *MaximizedLayoutName)
{
  //do something
}

const char *vtkMRMLLayoutNode::GetMaximizedLayoutName()
{
  //do something
}
</code></pre>
<p>After this I am unable to proceed.</p>

---

## Post #12 by @trash_imp (2021-06-12 20:09 UTC)

<p>Basically I am not able figure out how to notify <code>qMRMLLayoutManager</code> to change the layout.</p>

---

## Post #13 by @lassoan (2021-07-21 01:38 UTC)

<p>Were you able to solve this or you have given up on this? Let us know if you are still interested in implementing this and need help.</p>

---

## Post #14 by @trash_imp (2021-07-21 02:35 UTC)

<p>Yes, I am still interested in implementing this, but need some help.</p>
<p>For implementing “temporary maximize/restore view feature”</p>
<pre><code class="lang-auto">void vtkMRMLLayoutNode::SetMaximizedLayoutName(const char *MaximizedLayoutName)
{
  //do something
}

const char *vtkMRMLLayoutNode::GetMaximizedLayoutName()
{
  //do something
}
</code></pre>
<p>After this, I am unable to proceed.</p>

---

## Post #15 by @lassoan (2021-07-21 12:11 UTC)

<p>In these methods you would just store the name of the layout. Note that the “layout” word can unfortunately used for two different things: A. name of a view arrangement, B. name of a view within a view arrangement (LayoutName property of a view node). In this case “LayoutName” refers to B (the variable stores the name of a view).</p>
<p>You don’t need to write the implementation of these methods, you can just add these lines to vtkMRMLLayoutNode.h:</p>
<pre><code class="lang-auto">vtkGetStringMacro(MaximizedLayoutName);
vtkSetStringMacro(MaximizedLayoutName);
</code></pre>
<p>and create and initialize and delete the member variable:</p>
<ul>
<li>in the header: declare <code>const char* MaximizedLayoutName</code>
</li>
<li>in the constructor set <code>this-&gt;MaximizedLayoutName = nullptr;</code>
</li>
<li>in the destructor call <code>this-&gt;SetMaximizedLayoutName(nullptr);</code>
</li>
</ul>
<p>After this, you need to implement in layoutmanager to observe this MaximizedLayoutName property and hiding of views in CTK.</p>

---

## Post #16 by @jcfr (2021-07-21 16:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="18092">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In these methods you would just store the name of the layout. Note that the “layout” word can unfortunately used for two different things: A. name of a view arrangement, B. name of a view within a view arrangement (LayoutName property of a view node). In this case “LayoutName” refers to B (the variable stores the name of a view).</p>
</blockquote>
</aside>
<p>Would it make sense to add an entry to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary">glossary</a> ?</p>

---

## Post #17 by @trash_imp (2021-08-21 16:48 UTC)

<p>I’m sorry for the late reply, but I would like to complete this “Add button to maximize view” functionality.</p>
<ul>
<li>I’ve completed adding the code in <code>vtkMRMLLayoutNode</code>.</li>
<li>I am not able to understand how to hide the views in CTK?</li>
</ul>
<p>So could you please elaborate</p>

---
