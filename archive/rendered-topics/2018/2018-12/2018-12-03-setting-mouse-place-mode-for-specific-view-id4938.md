# Setting mouse place mode for specific view

**Topic ID**: 4938
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/setting-mouse-place-mode-for-specific-view/4938

---

## Post #1 by @jcfr (2018-12-03 13:39 UTC)

<p>It is currently possible to globally change the interaction mode (PersistentPlaceMode, SinglePlaceMode, ViewTransformMode) by updating the interaction node singleton. This is exposed to the user using the place mode toolbar:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25836f8301a8aee6e3f3e374c97a35f2aa3b0fb3.png" alt="image" data-base62-sha1="5lRgtZ9SOusjZ3e20GSJvtbiLOr" width="213" height="131"></p>
<p>In custom application, it is sometimes needed to disable placing of “annotations” only in specific view.</p>
<p>To support this, I proposed to:</p>
<ul>
<li>
<p>update <code>vtkAbstractViewNode</code> adding a <code>SupportedInteractionMode</code> bit field</p>
<ul>
<li>by default it would be initialized to 0 for all type of view.</li>
<li>and initialized to <code>Place | ViewTransform</code> only for  for  <code>vtkMRMLViewNode</code> and <code>vtkMRMLSliceViewNode</code>.</li>
</ul>
</li>
<li>
<p>the <code>Place</code> and <code>ViewTransform</code> corresponds to values of mouse mode enum in <a href="https://github.com/Slicer/Slicer/blob/f1b55fc99e948629e8a048c619d685a25ac0ba4d/Libs/MRML/Core/vtkMRMLInteractionNode.h#L45-L55">vtkMRMLInteractionNode</a></p>
</li>
</ul>
<p>This would allow to easily disable support for <code>Place</code> mode in specific view.</p>

---

## Post #2 by @jcfr (2018-12-03 14:12 UTC)

<p>In addition to the <code>SupportedInteractionMode</code> bit field, we also need to keep track of the current interaction mode for each view.</p>
<p>There are two possible approaches:</p>
<ol>
<li>add a <code>CurrentInteractionMode</code> property to the view</li>
<li>update <code>vtkMRMLInteractionNode</code> to keep track of interaction mode for all views.</li>
</ol>

---

## Post #3 by @pieper (2018-12-03 14:47 UTC)

<p>(I see Andras is replying too - let’s see if he says the same thing…)</p>
<p>Why not use the list of view names like in the display nodes?</p>

---

## Post #4 by @lassoan (2018-12-03 14:47 UTC)

<p>Currently, difference in behavior is usually managed by using display nodes. For example, we can already show/hide annotations in selected views. We could add a bitfield to display nodes that describe what interactions are allowed in that view.</p>
<p>Alternatively, we could use the technique that we use for connecting layout managers to views using ParentLayoutNode reference (if no parent node is defined then the default layout manager should be used). Implementation would be adding reference to InteractionNode (and maybe also to SelectionNode). If this node reference is undefined then the default interaction node would be used. This method would have the advantage that we could set what annotation to place in which view.</p>

---

## Post #5 by @jcfr (2018-12-03 14:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>display nodes that describe what interactions are allowed in that view</p>
</blockquote>
</aside>
<p>The issue is that corresponding display node do not exist yet.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>adding reference to InteractionNode</p>
</blockquote>
</aside>
<p>I like the idea but currently both interaction and selection node are singleton, these would be quite a disruptive change I think.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Why not use the list of view names like in the display nodes?</p>
</blockquote>
</aside>
<p>I think we need more than  a list. Indeed, the idea is to keep track of:</p>
<ul>
<li>which interaction modes are supported by which view.</li>
<li>current mode of a given view</li>
</ul>

---

## Post #6 by @lassoan (2018-12-03 15:09 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>The issue is that corresponding display node do not exist yet.</p>
</blockquote>
</aside>
<p>If needed, you can pre-create annotation/markup node and corresponding display node. You can definitely do it for markup fiducials but may be some annotation nodes cannot be pre-created with 0 points. Anyway, this is not a good solution anyway, as it would not allow customization of markup/annotation node selection per view.</p>
<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I like the idea but currently both interaction and selection node are singleton, these would be quite a disruptive change I think.</p>
</blockquote>
</aside>
<p>It is similar change as we implemented for managing virtual reality views by non-default layout manager. It does not seem disruptive to me.</p>
<p>I would not even consider any solution that only allows customization of interaction flags and not what markup node to place.</p>
<p>For example, in landmark registration module, we show fixed image in top row, moving image in middle row (and registration result in bottom row). It would be a bad solution to just enable landmark placement in either fixed or moving image views. We must keep placement enabled in all views but we need to place different landmarks in different view groups.</p>

---

## Post #7 by @jcfr (2018-12-03 15:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is similar change as we implemented for managing virtual reality views by non-default layout manager. It does not seem disruptive to me.</p>
</blockquote>
</aside>
<p>In the virtual reality extension, we implemented a custom layout node. This means that we didn’t have to change the  “singleton-ness” of the layout node.</p>
<p>To support different interaction node for different view, we would have to instantiate multiple interaction node.</p>
<p>Are you suggesting we change selection and interaction node to not be singleton anymore ?</p>

---

## Post #8 by @lassoan (2018-12-03 15:25 UTC)

<p>If interaction (and/or selection) node ID is not defined in a view node then the default singleton interaction node is used. If a custom node interaction node ID is defined then that is used. This logic can be implemented at one place (probably in the view node) and can be used everywhere where interaction node for a view is needed.</p>

---

## Post #9 by @cpinter (2018-12-03 15:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We must keep placement enabled in all views but we need to place different landmarks in different view groups</p>
</blockquote>
</aside>
<p>This would be such a great feature! No more switching between placed fiducial groups (markup nodes).</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="4938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If a custom node interaction node ID is defined then that is used</p>
</blockquote>
</aside>
<p>How do you propose to do this without removing the singletonness of the interaction node? If you awnt to have a second interaction node in the scene then it cannot be singleton I think. Or do you propose keeping it out of the scene? It doesn’t seem like a good way to do it.</p>

---

## Post #10 by @lassoan (2018-12-03 15:33 UTC)

<p>Additional selection and interaction nodes would not need to be singletons.</p>

---

## Post #11 by @jcfr (2018-12-03 15:34 UTC)

<p>That would work, doing the following allow to create additional interaction node:</p>
<pre><code class="lang-auto">n = slicer.mrmlScene.CreateNodeByClass("vtkMRMLInteractionNode")
n.SetSingletonOff()
slicer.mrmlScene.AddNode(n)
</code></pre>

---

## Post #12 by @jcfr (2018-12-03 15:35 UTC)

<p>I also suggest to add a reference between interaction and selection node, they both work in pair.</p>

---

## Post #13 by @jcfr (2018-12-03 22:24 UTC)

<p>After adding a selection node reference to the view, it was pretty straightforward to update the code base.</p>
<p>That said, the following three widgets are directly interfaced with the default interaction node:</p>
<ul>
<li><code>qSlicerMarkupsPlaceWidget</code></li>
<li><code>qMRMLSegmentEditorWidget</code></li>
<li>
<code>qSlicerMouseModeToolBar</code>:</li>
</ul>
<p>By default, I suggest the widgets continue to look up the default interaction node but a new <code>SetInteractionNode(vtkMRMLInteractionNode* ...)</code> function will be added.</p>

---

## Post #14 by @jcfr (2018-12-03 23:49 UTC)

<p>Here it is:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1048">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1048" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1048" target="_blank" rel="noopener">GUI issues with "add mode" compositing</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:36:46" data-timezone="UTC">10:36PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:36:47" data-timezone="UTC">10:36PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1048). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
