# Extending the Markups module

**Topic ID**: 14882
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/extending-the-markups-module/14882

---

## Post #1 by @RafaelPalomar (2020-12-04 12:23 UTC)

<p>Hello. I’m starting this thread to channel the discussions I’ve had with <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> regarding the creation of new markups (possibly in modules other than Makups).</p>
<p>As many other components in Slicer, Markups are extensible. Currently there are two approaches to create new markups:</p>
<ul>
<li>
<p><strong>Adding the new markups to the Markups module</strong>. This approach has no limitations in terms of what type of markups you can add, however, systematically adding all markups here will make the module grow to an unmanageable size for the user (and the developers); only markups that are of general interest for the community should be added here. Furthermore, markups added in the Markups module should be properly developed and well tested, which might mean long integration time.</p>
</li>
<li>
<p><strong>Adding derived markups in other modules</strong>. It is possible to include new markups in modules other than Markups. The limitation of this approach is that the new markups need to be derivative types of the already existing markups in Markup. A new markup derived from <code>vtkMRMLMakupsNode</code> won’t be handled properly, while a new markup derived from <code>vtkMRMLMarkupsCurveNode</code> wil be handled properly. The reason for this is that the handling of the markups in the Markups module is hardcoded to the existing types in the Markups module (and implicitly the derivative types).</p>
</li>
</ul>
<p>An improvement to this could be to modify the Markups infrastructure to allow other modules to register their own markups. One way to to this could be to enable a markups registration functionality in one of the current components (<code>vtkSlicerMarkupsLogic</code> or <code>qSlicerMarkupsModule</code>) and have the components where the markup types are harcoded (<code>vtkMarkupsDisplayableManager</code>, qSlicerWidgets and qMRMLWidgets) adhering to the list of registered markups.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>, please, let me know your thoughts.</p>

---

## Post #2 by @pieper (2020-12-04 15:48 UTC)

<p>This sounds great <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>.  It’s a recurring issue/pattern in Slicer that we need to generalize from hard coded to extensible functionality (that’s why there still a Modules/Core directory even though all modules since the very early days have been created as Loadable for consistency with extension-provided modules).  So it would be good to review the various examples of this and see which patterns make the most sense.  Off hand I can think of Modules, Segment Editor Effects, DICOMPlugins, Subject Hierarchy Plugins, SampleDataSources at least and they all use slightly different mechanisms.</p>
<p>It would be interesting to consider whether it will be possible to write a Markup extension in Python or if C++ will be required.</p>

---

## Post #3 by @lassoan (2020-12-04 16:40 UTC)

<p>In the current Slicer master we haven’t implemented pluggable markups yet. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is now working on adding this, adding a special curve for brain cortical surface segmentation in an extension.</p>
<p>After C++ implementation is complete, we can add scripted markups node base classes (widget, representation, and measurement) that can be used to define custom markups in Python.</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> I think the best would be if you could work directly with <a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a>, telling him what your requirements will be, so that he can take those into account when designing the pluggable interface.</p>

---

## Post #4 by @RafaelPalomar (2020-12-15 14:53 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> I have started looking at  the <code>vtkMRMLMarkupsDisplayableManager</code> to replace the hard-coded markups by a more generic approach.</p>
<p>As I see it , we would need to replace the current <code>Focus</code> member from:</p>
<pre><code class="lang-auto">std::set&lt;std::string&gt; Focus; // keep registry of nodes
</code></pre>
<p>to:</p>
<pre><code class="lang-auto">std::map&lt;std::string, std::string&gt; Focus; // keep registry of nodes and associated vtkmrmlwidgets
</code></pre>
<p>Then we would need to add a function to register the markups nodes and the associated widgets. This is useful because there are functions (e.g., <code>CreateWdiget</code>) creating widgets of a given type according to the node being processed. An alternative to this could be to keep the associated widget in the <code>vtkMRMLMarkupsNode</code>. Any thoughts?</p>
<p>The second point to discuss here is a bit more tricky.  We need to resolve the MRMLWidget sub-type in runtime. I have tried with:</p>
<pre><code class="lang-auto">vtkObject* obj = vtkObjectFactory::CreateInstance(widgetType.c_str());
vtkSlicerMarkupsWidget *widget = vtkSlicerMarkupsWidget::SafeDownCast(obj);
</code></pre>
<p>however, <code>CreateInstance</code> returns always <code>nullptr</code>. I suppose we need to enable a factory for the <code>vtkSlicerMarkupsWidget</code> sub-types. It seems the MRMLDisplayableManagers do something similar. Is this the way to go?</p>

---

## Post #5 by @lassoan (2020-12-15 16:35 UTC)

<p>Usually we don’t rely on the vtkObjectFactory but pass a factory method when we register a custom class (see for example how custom segment editor effects or IO plugins are registered). This may be more robust and flexible than creating a new instance based purely on class name.</p>
<p>For example, if we allow users to create Python scripted widgets they would all use the same C++ base class and so the vtkObjectFactory probably would not work (or we would need to invent some new design).</p>

---

## Post #6 by @RafaelPalomar (2020-12-16 09:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> I made a PR for the modifications of the markups DM to add node registration capabilities (<a href="https://github.com/Slicer/Slicer/pull/5345" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/pull/5345</a>).</p>
<p>The basic idea is to add a factory method to the vtkSlicerMarkupsWidget and derivatives to specify how the instantiation of a given widget should be. The DM was extended with a registration function and the hard-coding of markups was replaced by code that checks the registered nodes.</p>
<p>You will notice that in the constructor there are still hard-coded values. The DM does not need this per se, but as I see it, the registration of the DM on the module setup is based on classes and not instances:</p>
<pre><code class="lang-auto">  // Register displayable managers (same displayable manager handles both slice and 3D views)
  vtkMRMLSliceViewDisplayableManagerFactory::GetInstance()-&gt;RegisterDisplayableManager("vtkMRMLMarkupsDisplayableManager");
  vtkMRMLThreeDViewDisplayableManagerFactory::GetInstance()-&gt;RegisterDisplayableManager("vtkMRMLMarkupsDisplayableManager");
</code></pre>
<p>This means that the configuration of the DM needs to happen in the <code>constructor</code>. Is that how we want it to be?</p>
<p>I’m going to try implementing a new markup in an external module and see how it plays with these changes.</p>
<p>It looks to me that <code>qSlicerMarkupsWidget</code>, <code>qSlicerSubjectHierarchyMarkupsPlugin</code>, <code>vtkMRMLMarkupsFiducialStorageNode</code> and <code>vtkSlicerMarkupsLogic</code> have hard-coded values and would also require changes.</p>
<p>Pleae, let me know your thoughts.</p>

---

## Post #7 by @RafaelPalomar (2020-12-17 12:55 UTC)

<p>For organizational issues on my end I needed to make a new pull request for this topic.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5349" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5349" target="_blank" rel="noopener nofollow ugc">ENH: Removing hard-coded markup types from DM</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>ALive-research:feature/pluggable_markups</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-17" data-time="12:47:56" data-timezone="UTC">12:47PM - 17 Dec 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/RafaelPalomar" target="_blank" rel="noopener nofollow ugc">
          <img alt="RafaelPalomar" src="https://avatars2.githubusercontent.com/u/1978682?v=4" class="onebox-avatar-inline" width="20" height="20">
          RafaelPalomar
        </a>
      </div>

      <div class="lines" title="1 commits changed 17 files with 132 additions and 66 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5349/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+132</span>
          <span class="removed">-66</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @RafaelPalomar (2020-12-17 18:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a> I generated a new markup in an external module (<a href="https://github.com/ALive-research/Slicer-LiverAnalysis" rel="noopener nofollow ugc">https://github.com/ALive-research/Slicer-LiverAnalysis</a>) to test the changes I made in <span class="hashtag">#5349</span>. So far, creating a simple inherited MRML node, MRMLDM and SlicerLogic makes possible adding entirely new markups to the scene.</p>
<p>While this helps the extensibility of markups, I don’t think this is still a completely pluggable architecture. For that it should not be needed to define a new MRMLDM. As mentioned earlier in this thread, this seems to me a limitation of how the MRMLDMs get registered (class-based and not object based).</p>
<p>I’ll continue working on applying similar changes to the widgets side of the Markups, so new markups will be handled by the GUI.</p>
<p>Let me know if you think this is going in the right direction.</p>

---

## Post #9 by @RafaelPalomar (2020-12-21 20:00 UTC)

<p>Hello again <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>I’ve come up with a new design and now the Markups are truly pluggable. To create a new markup a user can:</p>
<ol>
<li>Define a new vtkMRMLMarkupNode</li>
<li>Define the associated vtkSlicerMarkupWidget</li>
<li>Register the new markup and widget, for instance, in the module <code>setup()</code> function or in the logic:</li>
</ol>
<pre><code class="lang-auto">   vtkMRMLMarkupsRegistrationFactory::GetInstance()-&gt;RegisterMarkup(
     vtkMRMLMarkupsAngleNode::New(), vtkSlicerAngleWidget::New());
</code></pre>
<p>I have tested it having an external module defining its own markup and seems to work fine.</p>
<p>I’m not that knowledgeable on the Python infrastructure, but I would think if one can define a vtkMRMLMarkups node and a vtkSlicerMarkupsWidget (which is a vtkMRMLAbstractWidget) in Python, the proposed changes will enable pluggable markups in Python too.</p>
<p>Let me know if you have time tomorrow in the devs meeting to have a discussion on this.</p>

---

## Post #10 by @pieper (2020-12-21 20:52 UTC)

<p>Looks very nice.  Yes, we should have time to discuss this in tomorrow’s meeting.</p>
<p>I’m wondering if we want to support the case where you could more than one possible widget type to operate on a markup node.  For example we might want to have different widgets for different manipulation modes.  For this maybe we’d want to use node attributes like we do for node comboboxes.</p>

---

## Post #11 by @jcfr (2021-04-13 19:05 UTC)

<p>To follow up, associated pull request <a href="https://github.com/Slicer/Slicer/pull/5349">Slicer PR-5349</a> has been integrated.</p>
<p>Many thanks to <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> for his patience and persistence during the review process, and also thanks to everyone who participated to the weekly hangouts and helped review and discuss how to best integrate this feature.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/partying_face.png?v=9" title=":partying_face:" class="emoji only-emoji" alt=":partying_face:"> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji only-emoji" alt=":pray:"></p>

---

## Post #12 by @cpinter (2021-11-09 09:27 UTC)

<p>Hi all,</p>
<p>I’ve created a new <a href="https://github.com/cpinter/SlicerGridSurface/tree/master">extension</a> based on the Bézier surface markup by <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>. I added the NURBS interpolation type to be able to create surfaces more intuitively and made some improvements and generalizations.<br>
We are planning to further improve this markup (fitting to model/segmentation, shared edges, etc.), and expect it to be around for a while.</p>
<p>It is all ready (<a href="https://github.com/Slicer/ExtensionsIndex/pull/1796">see PR</a>), however, questions have arisen about its name. Currently it is called GridSurface, but it does not describe its purpose too well, and seems to be too technical. <strong>I’d like to ask for your help in finding an appropriate name.</strong></p>
<p>Some of the ideas so far:</p>
<ul>
<li>Surface patch</li>
<li>Surface markup</li>
<li>Surface warp</li>
<li>Curved surface</li>
<li>Curved plane</li>
</ul>
<p>Here’s a very short video that shows how it looks:</p><div class="youtube-onebox lazy-video-container" data-video-id="Lh0Dsr_NE6M" data-video-title="3D Slicer surface markup" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Lh0Dsr_NE6M" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Lh0Dsr_NE6M/maxresdefault.jpg" title="3D Slicer surface markup" width="" height="">
  </a>
</div>


---

## Post #13 by @RafaelPalomar (2021-11-09 09:41 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>, this is a great work!</p>
<p>For the naming. I like <strong>Surface markup</strong> or maybe <strong>Deformable surface markup</strong> (longer but more descriptive).</p>

---

## Post #14 by @jamesobutler (2021-11-09 13:18 UTC)

<p>If the term “grid” is not in the name, would that make it indistinguishable from some other future surface that starts out as a circle instead of a rectangular grid? Or would whether it starts out as rectangle or circle be a property of the same markup type?</p>
<p>I would suggest avoiding the use of “markup” in the name as in “surface markup”. This is because we refer to things as “markups line” or “markups curve” as that it is controlled by the Markups module. So it would be weird to then say this is a “markups surface markup”. Instead I would call it simply a “surface” or “curved surface” to more clearly imply that it is more likely not going to be flat in its final form.</p>

---

## Post #15 by @jamesobutler (2021-11-09 13:25 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="14882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Currently it is called GridSurface, but it does not describe its purpose too well</p>
</blockquote>
</aside>
<p>I think one of the things we’ve learned about the markups module is that it is going to need to be a general module. So markups have general names like “Line” which don’t describe their purpose. A “Line” could be used as a Ruler or as a axis of rotation. There are many applications.</p>
<p>In this case, the surface could be used as a patch for something, but it could also be used for something else. Whichever name is chosen, specific application should not be implied in the name.</p>

---

## Post #16 by @cpinter (2021-11-09 14:07 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="14" data-topic="14882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>weird to then say this is a “markups surface markup”</p>
</blockquote>
</aside>
<p>The name of the extension and the name of the markup are two different things! I’d of course not include the word “markup” in the markup name, only in the extension name so that the people browsing the Extension Manager have an idea where it fits.</p>

---

## Post #17 by @jamesobutler (2021-11-09 15:32 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="14882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It is all ready (<a href="https://github.com/Slicer/ExtensionsIndex/pull/1796" rel="noopener nofollow ugc">see PR</a>), however, questions have arisen about its name. Currently it is called GridSurface</p>
</blockquote>
</aside>
<p>Apologies. It was unclear to me what “it” was referring to in this sentence. The markup name vs the extension name.</p>

---

## Post #18 by @muratmaga (2021-11-09 17:32 UTC)

<p>I like <strong>Surface Patch</strong> (as it reminded me a similar functionality in other sofware packages).</p>
<p>Is it possible to have this follow the surface of a 3D model?</p>

---

## Post #19 by @cpinter (2021-11-09 18:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="14882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is it possible to have this follow the surface of a 3D model?</p>
</blockquote>
</aside>
<p>What I have currently is an early version of what is finally imagined. Yes, we do plan to add an approximation feature that can be used to fit the surface to an existing model/segmentation.</p>

---

## Post #20 by @RafaelPalomar (2022-03-04 13:12 UTC)

<p>Hello!</p>
<p>for the Slicer-Liver module we have markups that are “ephimeral”. These markups are temporarily created and can lead to generation of other markpus (in Slicer-Liver we use them to initialize the Bezier Surface that will specify a resection trajectory).</p>
<p>Right now, registration of node, registration of markups widget and registration for adding the UI button happens all in <code>vtkSlicerMarkupsLogic::RegisterMarkupsNode</code>. The problem for us is that we don’t want to show these ephimeral markups in the UI; they don’t make sense by themselves alone. For more flexibility, I would suggest to split the registration of the markups in different functions. So you can support the case of a fully working markup that does not show up in the Markups UI module (add as button). We could still keep the <code>RegisterMarkupsNode</code> function that does it all so the API does not change. What do you think?</p>

---

## Post #21 by @cpinter (2022-03-04 14:26 UTC)

<p>If I understand your question correctly (I think btw it should be a new thread), then I have a simple suggestion.</p>
<p>I recently implemented a similar use case, in which the user clicks a button that says “Add ROI”, but in reality it initiates fiducial placement, which then, by observing the point added event, creates a ROI in the same position as a center. The fiducial node is not used for anything else and I am not interested in seeing it in any list. Is this the same kind of use case?</p>
<p>If so, my solution was just to call <code>HideFromEditorsOn</code> for the fiducials node, and it worked nicely.</p>

---

## Post #22 by @RafaelPalomar (2022-03-04 14:43 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>. Would <code>HideFromEditorsOn</code> prevent the creation of the markups add button in the toolbar and in the Markups module gui? I have a few of these ephimeral markups and it clutters the UI for something the user should never use independently.</p>

---

## Post #23 by @cpinter (2022-03-04 15:06 UTC)

<p>I don’t quite understand. Is it a new markup <em>type</em>? Or why is any button created?</p>

---

## Post #24 by @RafaelPalomar (2022-03-04 15:12 UTC)

<p>In the pluggable architecture, the markups toolbar and the Markups UI get populated with the registered markups. If I register a new markup in an external module a new button for adding a markup of that type is added. I want to avoid having “add markups” buttons for these ephimeral markups, they cannot be used directly and users should not get a button to add something they cannot use. Does it make sense?</p>

---

## Post #25 by @cpinter (2022-03-04 15:21 UTC)

<p>Ah I see, so it is a new type. I got confused by the register function. Anyway, as I see there is a <code>createPushButton</code> argument in the function</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.h#L261">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.h#L261" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.h#L261" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Loadable/Markups/Logic/vtkSlicerMarkupsLogic.h#L261</a></h4>



    <pre class="onebox">      <code class="lang-h">
        <ol class="start lines" start="251" style="counter-reset: li-counter 250 ;">
            <li>vtkMRMLMarkupsJsonStorageNode* AddNewJsonStorageNodeForMarkupsType(std::string markupsType);</li>
            <li>
            </li>
<li>/// Registers a markup and its corresponding widget to be handled by the Markups module.</li>
            <li>/// For a markup to be handled by this module (processed by the displayable</li>
            <li>/// manager, UI and subject hierarchy) it needs to be registered using this method.</li>
            <li>/// The method also registers the markupsNode class in the scene.</li>
            <li>/// \param markupsNode MRMLMarkups node to be registered.</li>
            <li>/// \param markupsWidget vtkSlicerWidget associated to the MRMLMarkups node registered.</li>
            <li>void RegisterMarkupsNode(vtkMRMLMarkupsNode* markupsNode,</li>
            <li>                         vtkSlicerMarkupsWidget* markupsWidget,</li>
            <li class="selected">                         bool createPushButton=true);</li>
            <li>
            </li>
<li>/// Unregisters a markup and its corresponding widget. This will trigger the</li>
            <li>/// vtkSlicerMarkupsLogic::MarkupUnregistered event.</li>
            <li>/// \param markupsNode MRMLMakrups node to be unregistered.</li>
            <li>void UnregisterMarkupsNode(vtkMRMLMarkupsNode*  markupsNode);</li>
            <li>
            </li>
<li>/// This returns an instance to a corresponding vtkSlicerMarkupsWidget associated</li>
            <li>/// to the indicated markups name.</li>
            <li>/// \param markupsType registered class to retrieve the associated widget.</li>
            <li>/// \return pointer to associated vtkSLicerMarkupsWidget or nullptr if the MRML node</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Unless I misunderstand names again…</p>

---

## Post #26 by @RafaelPalomar (2022-03-04 15:24 UTC)

<p>Yes, of couse! Thank you <a class="mention" href="/u/cpinter">@cpinter</a>. The funny thing is that I created that function, but I did not remember about it <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
