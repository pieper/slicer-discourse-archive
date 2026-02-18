# Odd ID for vtkMRMLLayoutNode

**Topic ID**: 9649
**Date**: 2019-12-29
**URL**: https://discourse.slicer.org/t/odd-id-for-vtkmrmllayoutnode/9649

---

## Post #1 by @jamesobutler (2019-12-29 23:23 UTC)

<p>I noticed that the layout node has an odd ID with a duplicate naming scheme (“vtkMRMLLayoutNodevtkMRMLLayoutNode”) as seen below.  It appears to have had this ID since at least 2012 as an old testing file references it, but I was trying to look into where in the code it gets set as I’m assuming it was intended to have an ID of simply “vtkMRMLLayoutNode”. Does anyone have any insight of what might be causing it to be set to this odd ID?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ebb92f74229aa564f9816f9fb3981c54373df7.png" alt="layout-node-id" data-base62-sha1="jG6rNTGYqic9tVx8MGLbrOn5iCP" width="485" height="186"></p>
<p>I searched for “vtkMRMLLayoutNodevtkMRMLLayoutNode” in the code base, but only found it being referenced in a few MRML testing files.<br>
<a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/Annotations/Testing/Data/Input/ruler.mrml" rel="noopener nofollow ugc">Modules/Loadable/Annotations/Testing/Data/Input/ruler.mrml</a><br>
<a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/Markups/Testing/Data/Input/AnnotationTest/AnnotationFiducialsTest.mrml" rel="noopener nofollow ugc">Modules/Loadable/Markups/Testing/Data/Input/AnnotationTest/AnnotationFiducialsTest.mrml</a><br>
<a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/VolumeRendering/Testing/Data/Input/volRender.mrml" rel="noopener nofollow ugc">Modules/Loadable/VolumeRendering/Testing/Data/Input/volRender.mrml</a></p>

---

## Post #2 by @pieper (2020-01-02 17:10 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a> -  Since it’s a singleton, there is only one in the scene so the ID can be any unique string.  The SingletonTag and basename are used by default and the original author used the class name as the SingletonTag, so that explains the odd pattern.  It’s not exactly pretty, but it shouldn’t cause any problems.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.cxx#L2262" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.cxx#L2262" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.cxx#L2262</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2252" style="counter-reset: li-counter 2251 ;">
<li>
</li>
<li>//------------------------------------------------------------------------------</li>
<li>std::string vtkMRMLScene::GenerateUniqueID(vtkMRMLNode* node)</li>
<li>{</li>
<li>  if (!node)</li>
<li>    {</li>
<li>    vtkWarningMacro("vtkMRMLScene::GenerateUniqueID: invalid node");</li>
<li>    return this-&gt;GenerateUniqueID("Node");</li>
<li>    }</li>
<li>  std::string baseID = node-&gt;GetClassName();</li>
<li class="selected">  if (node-&gt;GetSingletonTag())</li>
<li>    {</li>
<li>    return baseID + node-&gt;GetSingletonTag();</li>
<li>    }</li>
<li>  return this-&gt;GenerateUniqueID(baseID);</li>
<li>}</li>
<li>
</li>
<li>//------------------------------------------------------------------------------</li>
<li>std::string vtkMRMLScene::GenerateUniqueID(const std::string&amp; baseID)</li>
<li>{</li>
<li>  int uniqueIDIndex = this-&gt;GetUniqueIDIndex(baseID);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2020-01-02 17:55 UTC)

<p>Changing the code to <code>this-&gt;SetSingletonTag("Default")</code> would result in node ID <code>vtkMRMLLayoutNodeDefault</code> which would be much nicer but then for backward compatibility we would need to introduce a mechanism in scene loading that would replace the singleton tag on-the-fly. Singleton tag initialization on scene loading is already somewhat complicated and changing the ID would not have any direct benefits for users or developers, so I’m not sure if this is worth the trouble. Most likely we’ll need to make changes in the layout node when we add multi-monitor support to layouts. It would be a good opportunity to change the singleton tag then.</p>

---
