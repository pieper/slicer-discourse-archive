# Disable automatic scene view generation on save

**Topic ID**: 3888
**Date**: 2018-08-24
**URL**: https://discourse.slicer.org/t/disable-automatic-scene-view-generation-on-save/3888

---

## Post #1 by @lassoan (2018-08-24 18:03 UTC)

<p>Currently, a scene view is added on each scene save, which approximately doubles the scene file size, which may be significant when the scene has hundreds of nodes.</p>
<p>Also, each time when the scene file is loaded and the re-saved one more scene view is added.</p>
<p><strong>Can I go ahead and remove automatic scene view generation on scene save?</strong></p>

---

## Post #2 by @jcfr (2018-08-24 20:58 UTC)

<p>Sounds good to me.</p>
<p>Could you add an option like <code>includeSceneView</code> (or similar name) ?</p>
<p>Such option could be passed as a property to</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Base/Python/slicer/util.py#L476-L496" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Base/Python/slicer/util.py#L476-L496" target="_blank">Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Base/Python/slicer/util.py#L476-L496</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="476" style="counter-reset: li-counter 475 ;">
<li>def saveScene(filename, properties={}):</li>
<li>"""Save the current scene.</li>
<li>
</li>
<li>Based on the value of 'filename', the current scene is saved either</li>
<li>as a MRML file, MRB file or directory.</li>
<li>
</li>
<li>If filename ends with '.mrml', the scene is saved as a single file</li>
<li>without associated data.</li>
<li>
</li>
<li>If filename ends with '.mrb', the scene is saved as a MRML bundle (Zip</li>
<li>archive with scene and data files).</li>
<li>
</li>
<li>In every other case, the scene is saved in the directory</li>
<li>specified by 'filename'. Both MRML scene file and data</li>
<li>will be written to disk. If needed, directories and sub-directories</li>
<li>will be created.</li>
<li>"""</li>
<li>from slicer import app</li>
<li>filetype = 'SceneFile'</li>
<li>properties['fileName'] = filename</li>
<li>return app.coreIOManager().saveNodes(filetype, properties)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Also function <code>saveDefaultSceneView</code> would be a no-op with such property is set to <code>1</code></p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L117" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L117" target="_blank">Slicer/Slicer/blob/cac6db684d0310ec4376c61ab5019183a3525d3c/Modules/Loadable/Data/qSlicerSceneWriter.cxx#L117</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="107" style="counter-reset: li-counter 106 ;">
<li>  res = this-&gt;writeToDirectory(properties);</li>
<li>  }</li>
<li>return res;</li>
<li>}</li>
<li>
</li>
<li>//----------------------------------------------------------------------------</li>
<li>namespace</li>
<li>{</li>
<li>/// Save an explicit default scene view recording the state of the scene when</li>
<li>/// saved to file.</li>
<li class="selected">void saveDefaultSceneView(vtkMRMLScene* mrmlScene, const qSlicerIO::IOProperties&amp; properties)</li>
<li>{</li>
<li>if (!mrmlScene-&gt;IsNodeClassRegistered("vtkMRMLSceneViewNode"))</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>const char *defaultSceneName = "Master Scene View";</li>
<li>vtkSmartPointer&lt;vtkMRMLSceneViewNode&gt; sceneViewNode;</li>
<li>vtkSmartPointer&lt;vtkCollection&gt; oldSceneViewNodes;</li>
<li>oldSceneViewNodes.TakeReference(</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Ideally, the option would also show up in the data dialog</p>

---

## Post #3 by @pieper (2018-08-24 21:22 UTC)

<p>Yes, adding the sceneview automatically hasn’t turned out to have a lot of utility.  It also make it difficult if you have to inspect the mrml file for any reason.  +1 for turning that feature off by default (and while I agree with Jc that a gui option to reenable it would be ideal, I’d be okay with turning it off even if the gui weren’t added).</p>

---

## Post #4 by @jcfr (2018-08-24 21:39 UTC)

<blockquote>
<p>I’d be okay with turning it off even if the gui weren’t added</p>
</blockquote>
<p>Sounds good. Availability from python is sufficient</p>
<p>Should the MRB always be done including scene view then ?</p>

---

## Post #5 by @pieper (2018-08-24 22:01 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="3888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Should the MRB always be done including scene view then ?</p>
</blockquote>
</aside>
<p>I don’t think the sceneviews add anything extra in the mrb case compared to the mrml case, so no, I wouldn’t.</p>
<p>The sceneview does create a screen capture and that could be useful to have if one wanted to have a thumbnail for browsing scenes, like in an open dialog (but we’ve never done that so I’m not sure it’s a valid use case).</p>

---

## Post #6 by @jcfr (2018-08-24 22:20 UTC)

<p>Does this mean that it will not be possible to save MRB like this one: <a href="http://slicer.kitware.com/midas3/slicerdatastore/view?itemId=121588&amp;layout=layout">http://slicer.kitware.com/midas3/slicerdatastore/view?itemId=121588&amp;layout=layout</a></p>

---

## Post #7 by @rkikinis (2018-08-24 22:36 UTC)

<p>That would be a pity</p>

---

## Post #8 by @pieper (2018-08-24 22:38 UTC)

<p>The only difference would be that you would not get the master scene view at the end of that list. The ones you make explicitly would still be there.</p>
<p>But it’s true that if you didn’t make scene views explicitly there wouldn’t be any in the data store.</p>

---

## Post #9 by @lassoan (2018-08-24 23:24 UTC)

<p>The only difference would be that if you needed a scene view then you would need to click on the “Create scene view” button + click OK (two extra clicks) before you save the scene.</p>
<p>I find that these automatically created scene views are more distracting for me than helpful, as they clutter the scene view list.</p>
<p>We can save a screenshot independently of scene views when the scene is saved to enable quick preview without loading the scene.</p>

---

## Post #10 by @jcfr (2018-08-24 23:36 UTC)

<p>Thanks for your patience and for the clarification. The propose change make complete sense. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>automatically created scene views are more distracting for me than helpful,</p>
</blockquote>
<p>agreed. Explicit is better than implicit in that case</p>
<blockquote>
<p>We can save a screenshot independently of scene views when the scene is saved to enable quick preview without loading the scene.</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #11 by @rkikinis (2018-08-24 23:51 UTC)

<p>If I load an mrb, do I get the same look/ configuration like when I saved the mrb?</p>

---

## Post #12 by @lassoan (2018-08-25 03:46 UTC)

<aside class="quote no-group" data-username="rkikinis" data-post="11" data-topic="3888" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rkikinis/48/791_2.png" class="avatar"> rkikinis:</div>
<blockquote>
<p>If I load an mrb, do I get the same look/ configuration like when I saved the mrb?</p>
</blockquote>
</aside>
<p>Yes. The loaded scene will look exactly like the scene looked at the time of saving.</p>
<p>Automatic sceneview creation might have been implemented just because of the screenshot. Storing state of all nodes in scene view is redundant, because that information is already stored in the main scene.</p>

---

## Post #13 by @rkikinis (2018-08-25 10:55 UTC)

<p>Hi,<br>
thanks for the explanation. Preserving the ability to restore the state was the functionality I was concerned about.<br>
Best<br>
Ron</p>

---

## Post #14 by @cpinter (2018-08-25 17:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="3888">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We can save a screenshot independently of scene views when the scene is saved to enable quick preview without loading the scene</p>
</blockquote>
</aside>
<p>Yes I think if this small feature is added to scene saving instead of the scene view capture, then we won’t lose anything by removing the automatic scene views.</p>

---

## Post #15 by @lassoan (2018-08-26 14:09 UTC)

<p>I’ve implemented replaced automatic scene view saving by automatic screenshot saving. I wanted to send a pull request but accidently pushed it directly - <a href="https://github.com/Slicer/Slicer/commit/2dd13d78f9a1b8678593e4f3cd06a127133602ab">see changes here</a>. Let me know if you have any comments, I’ll address them in follow-up commits.</p>

---
