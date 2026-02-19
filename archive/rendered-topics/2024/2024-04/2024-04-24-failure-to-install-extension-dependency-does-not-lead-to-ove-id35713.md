---
topic_id: 35713
title: "Failure To Install Extension Dependency Does Not Lead To Ove"
date: 2024-04-24
url: https://discourse.slicer.org/t/35713
---

# Failure to install extension dependency does not lead to overall install failure

**Topic ID**: 35713
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/failure-to-install-extension-dependency-does-not-lead-to-overall-install-failure/35713

---

## Post #1 by @fedorov (2024-04-24 17:40 UTC)

<p>I used today’s nightly to install SlicerIDCBrowser extension. When trying to load DICOM segmentations I downloaded from IDC using that extension, I realized that QuantitativeReporting extension, which is its dependency, is not installed (the underlying issue is being tracked here, if anyone is interested: <a href="https://github.com/Slicer/ExtensionsIndex/issues/2041#issuecomment-2075485309">https://github.com/Slicer/ExtensionsIndex/issues/2041#issuecomment-2075485309</a>).</p>
<p>Is this the correct behavior? I would expect the installation of an extension to fail if any of its dependencies are not available.</p>

---

## Post #2 by @lassoan (2024-04-24 20:06 UTC)

<p>Often not all features of all modules requires all dependencies, so Slicer lets the user refuse installation of certain extensions and the user can also uninstall any extensions at any time.</p>
<p>If Slicer can start the module - even though there are some missing dependencies, which is often the case for Python scripted modules - then the module will be started. It is the responsibility of module developers to check if required modules are available  for a certain function and display a meaningful message if they are not. It can be something very simple like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/afb9d94322d2be024afe8fa2c9f7223d49e1549b/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L82-L84">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/afb9d94322d2be024afe8fa2c9f7223d49e1549b/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L82-L84" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/afb9d94322d2be024afe8fa2c9f7223d49e1549b/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L82-L84" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/afb9d94322d2be024afe8fa2c9f7223d49e1549b/CardiacDeviceSimulator/CardiacDeviceSimulator.py#L82-L84</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="82" style="counter-reset: li-counter 81 ;">
          <li>if not hasattr(slicer.modules, 'volumereslicedriver'):</li>
          <li>  slicer.util.messageBox("This modules requires SlicerIGT extension. Install SlicerIGT and restart Slicer.")</li>
          <li>  return</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2024-04-24 20:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If Slicer can start the module - even though there are some missing dependencies, which is often the case for Python scripted modules - then the module will be started. It is the responsibility of module developers to check if required modules are available for a certain function and display a meaningful message if they are not.</p>
</blockquote>
</aside>
<p>I see. I have to say that I do not necessarily agree this is a good approach. In many (most?) other situations (e.g., python packages) dependency (at least usually) means “it will not work if dependency is not satisfied”. I’ve developed a number of extensions, and I had no idea “dependency” has a different semantics in Slicer.</p>
<p>But thank you for the explanation, I should update my modules to deal with this.</p>
<p>In my opinion, if Slicer decided to adopt an unorthodox definition of “dependency”, it would be a lot more useful and intuitive, and a lot less error-prone if the developer could specify in the extension definition file whether dependency is mandatory or not. Otherwise this generic feature you described has to be discovered by every developer and re-implemented in every extension.</p>

---

## Post #4 by @fedorov (2024-04-24 21:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It can be something very simple like this:</p>
</blockquote>
</aside>
<p>Can you clarify - this will prevent the extension from being installed, or it will prevent it from being started?</p>
<p>I want to make sure my extension is not installed if the dependencies are not available.</p>

---

## Post #5 by @lassoan (2024-04-24 21:14 UTC)

<p>This just-in-time installation and requirement checking (for both Slicer extensions and Python packages) is indeed more work for developers but allows much more efficiency and better user experience.</p>
<blockquote>
<p>Can you clarify - this will prevent the extension from being installed, or it will prevent it from being started?</p>
</blockquote>
<p>If you click on the link then you can see those two lines in context. If you put it in your module widget initialization step then you can prevent the module from showing up without the dependency. If you only need a module for a specific feature then you can display the message to the user to let him know that this feature is not available until that extension is installed.</p>

---

## Post #6 by @jamesobutler (2024-04-24 21:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Does this mean that the SegmentEditorExtraEffects extension should not be defining a <code>build_dependency</code> of MarkupsToModel because only 2 effects (DrawTube and SurfaceCut) require MarkupsToModel while other effects such as LocalThreshold does not? Where upon attempting to use the DrawTube and SurfaceCut effect without the MarkupsToModel extension installed should at that time warn about that extension needing to be installed to use those effects?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/c3160a7b4c9b273e5960a33f608dfd793665df74/SegmentEditorExtraEffects.json#L3">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/c3160a7b4c9b273e5960a33f608dfd793665df74/SegmentEditorExtraEffects.json#L3" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/c3160a7b4c9b273e5960a33f608dfd793665df74/SegmentEditorExtraEffects.json#L3" target="_blank" rel="noopener nofollow ugc">Slicer/ExtensionsIndex/blob/c3160a7b4c9b273e5960a33f608dfd793665df74/SegmentEditorExtraEffects.json#L3</a></h4>



    <pre class="onebox"><code class="lang-json">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>{</li>
          <li>  "$schema": "https://raw.githubusercontent.com/Slicer/Slicer/main/Schemas/slicer-extension-catalog-entry-schema-v1.0.0.json#",</li>
          <li class="selected">  "build_dependencies": ["MarkupsToModel"],</li>
          <li>  "build_subdirectory": ".",</li>
          <li>  "category": "Segmentation",</li>
          <li>  "scm_revision": "master",</li>
          <li>  "scm_url": "https://github.com/lassoan/SlicerSegmentEditorExtraEffects"</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2024-04-25 02:36 UTC)

<p>MarkupsToModel is a build dependency if we want to test as part of the build process. But it is true that it is not a strict runtime dependency, because there are many effects that do not require MarkupsToModel extension. And you are right, it would be nicer to show a descriptive error message to the user when MarkupsToModel modules are not available - instead of just logging errors in the application log.</p>

---

## Post #8 by @fedorov (2024-04-25 17:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I did open the link before asking the earlier question. I wanted to confirm there is no mechanism that will try that function at the time extension is being installed.</p>
<p>The example you provided in your snippet is rather different from my situation.</p>
<p>SlicerHeart does not declare <code>volumereslicedriver</code> as a dependency in the former s4ext file (what is now called <code>build_dependency</code>): <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/SlicerHeart.json#L3" class="inline-onebox">ExtensionsIndex/SlicerHeart.json at main · Slicer/ExtensionsIndex · GitHub</a>. SlicerIDCIndex does declare QuantitativeReporting extension as such: <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/IDCBrowser.json#L3" class="inline-onebox">ExtensionsIndex/IDCBrowser.json at main · Slicer/ExtensionsIndex · GitHub</a>.</p>
<p>I would expect that my extensions that have dependencies declared in s4ext/json as such missing, should not be installed at all. If those dependencies are missing, I do not want my extension that depends on them to appear at all in the list of modules. I want the install step to fail. <a class="mention" href="/u/rkikinis">@rkikinis</a> ran into this situation just today, and was confused the same way as me.</p>
<p>But I think this issue may be related to a recent regression that <a class="mention" href="/u/jcfr">@jcfr</a> submitted a fix today: <a href="https://github.com/Slicer/Slicer/pull/7712" class="inline-onebox">COMP: Fix extension build ensuring build dependency directories are passed by jcfr · Pull Request #7712 · Slicer/Slicer · GitHub</a>. I think what should have happened is that IDCBrowser build should have failed, and it should not have appeared in ExtensionsManager at all. Still, if for any reason extensions in the <code>build_dependency</code> list are missing in ExtensionManager, I believe install should fail.</p>

---

## Post #9 by @lassoan (2024-04-25 17:54 UTC)

<p>Soft runtime dependency is a very useful feature, but I agree that it could be useful to add hard runtime dependency, too.</p>
<p>If a dependency is not found during installation of an extension then an error message should be displayed. If no error is displayed then it is a bug. Maybe it was displayed for a couple of seconds, but since the extension was still installed, it may have been easy to overlook.</p>
<p>Still, the dependencies may change, break, modules may be removed or renamed in the dependency, individual modules may be disabled, etc. so whenever a module relies on other module then it makes sense to display a meaningful error message is an expected module or feature is unavailable.</p>

---
