# Support for keyframe based animation

**Topic ID**: 6885
**Date**: 2019-05-21
**URL**: https://discourse.slicer.org/t/support-for-keyframe-based-animation/6885

---

## Post #1 by @jcfr (2019-05-21 19:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="6862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/is-there-interest-in-higher-quality-rendering-for-slicer/6862/2">Is there interest in higher quality rendering for Slicer?</a></div>
<blockquote>
<p>can benefit from some sort of a keyframe rendering</p>
</blockquote>
</aside>
<p>This reminds me of the following project put together by <a class="mention" href="/u/agirault">@agirault</a> and  <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a></p><div class="youtube-onebox lazy-video-container" data-video-id="UNOwVAQsvBg" data-video-title=" - YouTube" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UNOwVAQsvBg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="" title=" - YouTube" width="" height="">
  </a>
</div>

<p>Edit: Updated link to video publicly available.</p>
<p>Edit 2: More details are available on this page: <a href="https://www.slicer.org/wiki/Documentation/Labs/FlyThroughNavigation" class="inline-onebox">Documentation/Labs/FlyThroughNavigation - Slicer Wiki</a></p>

---

## Post #2 by @agirault (2019-05-22 14:51 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/hherhold">@hherhold</a> I think we should open a separate thread for the keyframe animation so we can focus on answering <a class="mention" href="/u/dave_demarle">@Dave_DeMarle</a> question regarding photorealistic rendering, like <a class="mention" href="/u/lassoan">@lassoan</a> did here.</p>

---

## Post #3 by @pieper (2019-05-22 22:51 UTC)

<p>iVSPlan looks cool <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> and I have been talking for a while about the possibility for keyframing support and I had in mind something kind of like what’s shown in the video, but I was also thinking of making it handle potentially any node, not just camera nodes.  For example clipping planes and volume rendering transfer functions.</p>
<p>I was thinking of doing something based on the Sequences infrastructure, since that already has multi-node animation abilities.  But what’s missing is the way to interpolate various node types between keyframes.  I don’t have a specific implementation plan at this point, but I hope to try some experiments and report back with ideas about how to make something with a clean and extensible architecture.</p>

---

## Post #4 by @agirault (2019-05-23 14:01 UTC)

<blockquote>
<p>I had in mind something kind of like what’s shown in the video, but I was also thinking of making it handle potentially any node, not just camera nodes</p>
</blockquote>
<p>I think that would make a lot of sense. Like you brought up, the interpolation is then the question (it was easy to use vtkSplines for the camera position and orientation). My understanding is that the main use case would be for the camera, so maybe it’s worth not over-engineering a fit-all solution but start building around the camera?</p>

---

## Post #5 by @pieper (2019-05-23 14:24 UTC)

<p>I agree about not over-engineering - but still, I don’t think it’s enough to do just the camera.  I’d thought about adding a virtual method like <code>vtkMRMLDisplayableNode::Interpolate()</code> so that any displayable could expose it’s own interpolation method but I don’t like that for a number of reasons (mainly because it would make MRML depend on Sequences but also because some animations should set up relations between objects - like the camera’s lookat is tied to another object’s location).</p>
<p>Instead I think the place to start is with some custom scripts that handle some specific animation styles, basically as an extension of the current ScreenCapture module.</p>
<p>For reference, here’s a video that <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested as an inspiration:</p>
<div class="lazyYT" data-youtube-id="juRJEkTRUhE" data-youtube-title="Ears of wheat - micro-CT visualisation" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Here the things we would need to keyframe are:</p>
<ul>
<li>Camera parameters (or object transform parameters)</li>
<li>volume rendering lookup table</li>
<li>cutting plane or cropping ROI</li>
</ul>
<p>These are all fairly easy values to interpolate.</p>

---

## Post #6 by @lassoan (2019-05-31 11:13 UTC)

<p>We plan to merge Sequences extension features into Slicer core, so interpolation of any node will be available. If interpolation is implemented for a node then Sequence browser can use it quite easily. The main difficulty is to implement a simple yet powerful user interface. What is in Paraview or MITK seems to have taken a lot of work and still very hard to use.</p>
<p>If we need to change only one parameter at a time then we can easily add those as animation modes to screen capture module.</p>
<p>Camera animation is a special case, as you may not want to specify it by saving current camera positions as key frames, but instead by specifying a curve and maybe a look-at point. This can be managed in the endoscopy module. We should probably rename the module to something that reflects that it is a general “curve to transform” module (Camera path might be good, or maybe something even more general). We should update it to use the new curve widget, add option to export to sequence, etc.</p>

---

## Post #7 by @pieper (2019-06-03 21:07 UTC)

<p>What’s the timeframe for merging Sequences to the core?</p>

---

## Post #8 by @lassoan (2019-06-04 02:24 UTC)

<p>Sequences should be in its final place in Slicer5. Since Slicer5 is scheduled for next RSNA and we need time for stabilization and testing, Sequences should be moved by the end of summer.</p>

---

## Post #10 by @agirault (2019-06-11 12:25 UTC)

<p>I’m obviously biased, but the interface I created for IVSPlan (linked by <a class="mention" href="/u/jcfr">@jcfr</a> in the top comment) was really intuitive and easy to use.</p>

---

## Post #11 by @pieper (2019-06-11 12:37 UTC)

<p><a class="mention" href="/u/agirault">@agirault</a> agreed, it looks nice.  Is the code available for reuse?</p>

---

## Post #12 by @agirault (2019-06-11 22:30 UTC)

<p>Now yes!</p>
<p>With the help of <a class="mention" href="/u/jcfr">@jcfr</a>, we’ve pulled out the code for that module, added a LICENSE and README files, and published it to GitHub:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/KitwareMedical/Slicer-CameraPath" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2717525?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="59" height="59">

<h3><a href="https://github.com/KitwareMedical/Slicer-CameraPath" target="_blank" rel="nofollow noopener">KitwareMedical/Slicer-CameraPath</a></h3>

<p>Slicer module for Intelligent Virtual Surgical Planning - KitwareMedical/Slicer-CameraPath</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>JC described it in the README of the repository above, but it depends on an old fork of Slicer with some small changes (which also includes a “flying” as an option that could be toggled in the UI, which worked pretty well):<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://github.com/KitwareMedical/Slicer/tree/ivsplan-v4.4.0-2015-11-06-05f8365ee" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2717525?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="59" height="59">

<h3><a href="https://github.com/KitwareMedical/Slicer/tree/ivsplan-v4.4.0-2015-11-06-05f8365ee" target="_blank" rel="nofollow noopener">KitwareMedical/Slicer</a></h3>

<p>Fork for Slicer Custom application. Contribute to KitwareMedical/Slicer development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Keep in mind that I wrote this as an intern who discovered Slicer 4 years ago <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>Also, here was the full demo I had created (14min+):</p>
<div class="lazyYT" data-youtube-id="ZVP5oXJ0-cQ" data-youtube-title="iVSPlan - Camera Path module [Full Demo]" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Hth</p>

---

## Post #14 by @jamesobutler (2019-06-11 23:25 UTC)

<p>I’ve seen in the past spam accounts that will copy and paste another user’s response. Likely to gain higher discourse forum privileges by making a post. I’m guessing the post/account was later deleted.</p>

---

## Post #15 by @lassoan (2019-06-11 23:35 UTC)

<p>Yes, it was a spammer. But it accidentally did something useful by reviving the topic. <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #18 by @pieper (2019-06-13 14:46 UTC)

<p>Hi <a class="mention" href="/u/agirault">@agirault</a> - thanks for sharing the example <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  Just to confirm, this is not expected to compile with current slicer and you aren’t planning to work on it, right?  I ask because with <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/jcfr">@jcfr</a> we’re trying to get a ballpark idea of the effort involved in getting the keyframing features in place.</p>

---

## Post #19 by @jcfr (2019-06-13 15:01 UTC)

<p>Not expected to build against current Slicer.</p>
<p>I anticipate updating code and backporting changes to Slicer should be straightforward.</p>
<p>We will account for this in project with <a href="http://u/muratmaga" rel="nofollow noopener">@muratmaga</a>.</p>

---

## Post #20 by @agirault (2019-06-13 15:05 UTC)

<p>Correct <a class="mention" href="/u/pieper">@pieper</a>, this worked with Slicer 4.4, and I don’t have funding to update it to latest Slicer. Are you looking into the effort needed to implement this on top of Sequence, or to simply update it as-is to latest Slicer? I presume the later shouldn’t be much work, there weren’t many functionalities missing in Slicer.</p>

---

## Post #21 by @pieper (2019-06-13 15:32 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/agirault">@agirault</a> - yes, at this point we’re still trying to scope out all the options so we know what we have to work with and what to build off of.  Yes, I’m thinking that we would want to build on top of Sequences but expose a very high level UI to create the specific types of animations described above (not just camera, but also volume rendering transfer functions and cropping) and a simple timeline editor.</p>

---

## Post #22 by @Dave_DeMarle (2019-06-17 19:05 UTC)

<p>I think the way this takes whatever camera positions you have and makes key frames from them for you is important. That is you move the camera the same way you normally do and then when you hit Add Keyframe the details are filled in for you. You have to hunt a bit to find the similar interface in ParaView’s animation view and most people have to confront the awkward “Enter camera positions manually” interface instead.</p>
<p>In both ParaView and Slicer we should make it so that more/all of the controls (not just the camera) that vary over the animation are set up in this user friendly way and then manually editable after the fact.</p>

---

## Post #23 by @jcfr (2019-07-09 13:41 UTC)

<aside class="quote no-group" data-username="Dave_DeMarle" data-post="22" data-topic="6885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dave_demarle/48/3772_2.png" class="avatar"> Dave_DeMarle:</div>
<blockquote>
<p>we should make it so that more/all of the controls (not just the camera) that vary over the animation are set up in this user friendly way and then manually editable after the fact.</p>
</blockquote>
</aside>
<p>Agreed, this is critical for usability.</p>

---

## Post #24 by @jcfr (2019-07-09 13:52 UTC)

<p>To add support for interpolation and associated UI for key frame edition, here is what I was thinking (based on what we <a href="https://github.com/NA-MIC/ProjectWeek/tree/master/PW31_2019_Boston/Breakouts/Infrastructure">discussed</a> during the last project week).</p>
<h2><a name="p-26340-the-key-frame-editor-1" class="anchor" href="#p-26340-the-key-frame-editor-1" aria-label="Heading link"></a>The Key Frame editor</h2>
<p>from a high level, I suggest we keep things simple and support the following:</p>
<p>(1) a <strong>master timeline</strong> to drive the animation. (at first we would only have “Real-time” mode where we set the the duration in seconds).</p>
<p>We could reuse the <a href="https://github.com/nci/drishti/">Drishti</a> widget (MIT License) or the one from Paraview, or an improved version getting the best of both.</p>
<ul>
<li>Drishti timeline (I was able to compile it … and it was not straightforward)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e0bcb593d4ef1bf3a15edb3eaffe5a9b99e4f1d.png" data-download-href="/uploads/short-url/kgB4lexjeOlwQ2eaIE6TLnuyfvL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e0bcb593d4ef1bf3a15edb3eaffe5a9b99e4f1d_2_690x104.png" alt="image" data-base62-sha1="kgB4lexjeOlwQ2eaIE6TLnuyfvL" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e0bcb593d4ef1bf3a15edb3eaffe5a9b99e4f1d_2_690x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e0bcb593d4ef1bf3a15edb3eaffe5a9b99e4f1d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e0bcb593d4ef1bf3a15edb3eaffe5a9b99e4f1d.png 2x" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">904×137 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Paraview timeline</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f916863a3fe0f9364f5100dce5d335e6b6cc72c3_2_690x25.png" alt="image" data-base62-sha1="zxx9c1gZNeOih4FVHvDbV7daWiv" width="690" height="25" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f916863a3fe0f9364f5100dce5d335e6b6cc72c3_2_690x25.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f916863a3fe0f9364f5100dce5d335e6b6cc72c3_2_1035x37.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f916863a3fe0f9364f5100dce5d335e6b6cc72c3_2_1380x50.png 2x" data-dominant-color="EAEAEA"></p>
<p>(2) three pre-defined tracks:</p>
<ul>
<li>
<p>camera path</p>
</li>
<li>
<p>ROINode (the one allowing to crop volume rendering)</p>
</li>
<li>
<p>transfer function</p>
</li>
</ul>
<p>where keyframe can explicitly be added/removed only for ROINode and transfer function</p>
<p>The “camera path” would be defined using an improved version of the endoscopy module (as describe <a href="https://discourse.slicer.org/t/support-for-keyframe-based-animation/6885/6">here</a>).</p>
<h2><a name="p-26340-suggested-approach-2" class="anchor" href="#p-26340-suggested-approach-2" aria-label="Heading link"></a>Suggested approach</h2>
<p>This section describe a possible way to more forward by updating the sequences modules to be user in Key Frame editor.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences</a></p>
<h3><a name="p-26340-features-already-available-in-sequences-extension-3" class="anchor" href="#p-26340-features-already-available-in-sequences-extension-3" aria-label="Heading link"></a>Features already available in sequences extension</h3>
<p>Given the current sequences implementation where:</p>
<ul>
<li>
<p>A given <code>vtkMRMLSequenceNode</code> is associated with a collection of data nodes.</p>
</li>
<li>
<p>A <code>vtkMRMLSequenceBrowserNode</code> is associated with a collection of <code>vtkMRMLSequenceNode</code></p>
</li>
<li>
<p>The entrypoint for updating all proxy nodes is the function <code>vtkSlicerSequenceBrowserLogic::UpdateProxyNodesFromSequences</code></p>
</li>
<li>
<p>The “time steps” available in a given sequence browser corresponds to the number of “items” associated with a browser node, itself corresponding to the number data nodes in the associated master node.</p>
</li>
<li>
<p>if a synchronized sequence node  (different from the master sequence) doesn’t have a data node corresponding to the requested “step” (call “indexValue” in the code), the closest data node is used to update the proxy node.  This is implemented in</p>
<ul>
<li>
<p><code>vtkMRMLSequenceNode::GetItemNumberFromIndexValue(const std::string&amp; indexValue, bool exactMatchRequired /* =true */)</code></p>
</li>
<li>
<p><code>vtkMRMLSequenceNode::GetDataNodeAtValue(const std::string&amp; indexValue, bool exactMatchRequired /* =true */)</code></p>
</li>
</ul>
</li>
</ul>
<p>We need a way to map:</p>
<ul>
<li>
<p>the concept of track and key frame with vtkMRMLSequenceNode,  vtkMRMLSequenceBrowserNode and data node</p>
</li>
<li>
<p>have a container to store time for a key frame, and interpolation function used between two frames</p>
</li>
</ul>
<p>Good news, key frames are data node within a <code>vtkMRMLSequenceNode</code></p>
<h3><a name="p-26340-support-for-interpolation-4" class="anchor" href="#p-26340-support-for-interpolation-4" aria-label="Heading link"></a>Support for interpolation</h3>
<p>To support <strong>interpolation</strong> , I was then thinking of the following:</p>
<ul>
<li>
<p>update the parameter exactMatchRequired from  “GetDataNodeAtValue” function to be something like “interpolationMode” accepting the following values:</p>
<ul>
<li>
<p>ExactMatch</p>
</li>
<li>
<p>ClosestMatch</p>
</li>
<li>
<p><s>ExactMatchOrInterpolated</s> Interpolated</p>
</li>
</ul>
</li>
<li>
<p>In case of ExactMatchOrInterpolated mode, if not an exact match GetDataNodeAtValue would have to perform the interpolation (or retrieved a cached value of the interpolated data node)</p>
</li>
<li>
<p>the interpolation function would have the following paramerters: fromDataNode, toDataNode, nodeInterpolator, fromTime, toTime and currentTime (or fromStep, toStep and currentStep)</p>
</li>
<li>
<p>within each sequence node we would store a vector of “node interpolators”. This would corresponds to the function applies when performing an interpolation between two data nodes.</p>
</li>
<li>
<p>update the vtkMRMLNodeSequencer::NodeSequencer base class adding interpolation method :  GetInterplatedNode(vtkMRMLNode* from, vtkMRMLNode* to, vtkMRMLNodeSequencer::NodeInterpolator* interpolator, double fromTime, double toTime, double currentTime)</p>
</li>
</ul>
<h3><a name="p-26340-reusing-paraview-code-5" class="anchor" href="#p-26340-reusing-paraview-code-5" aria-label="Heading link"></a>Reusing Paraview code</h3>
<p>I was initially thinking to extract some of the <a href="https://github.com/Kitware/ParaView/tree/master/ParaViewCore/Animation">code of Paraview</a> and add it to VTK so that we can reuse some in both Slicer and Paraview:</p>
<pre><code class="lang-plaintext">  vtkPVKeyFrame
  vtkPVCompositeKeyFrame
  vtkPVBooleanKeyFrame
  vtkPVSinusoidKeyFrame
  vtkPVExponentialKeyFrame
  vtkPVRampKeyFrame
  vtkPVKeyFrameCueManipulator (and base class vtkPVCueManipulator)
  vtkRealtimeAnimationPlayer
  vtkSequenceAnimationPlayer
  vtkTimestepsAnimationPlayer
  vtkCompositeAnimationPlayer
  vtkSMAnimationScene (investigate if changes can be integrated with vtkAnimationScene)
  Note that vtkAnimationCue and vtkAnimationScene are already part of VTK.
</code></pre>
<p>But it seems the API available in the sequences module doesn’t really overlap with what was done in Paraview.</p>

---

## Post #25 by @lassoan (2019-09-18 18:22 UTC)

<p>I have come across <a href="http://www.mitk.org/wiki/Downloads">MITK’s</a> “Movie Maker” widget and it is quite nice. It mimics animation editing in Powerpoint - quite simple and intuitive. It does not support keyframes but allows timeline editing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5971ad2e1885ab64281ae7bf0b0094c179c9723f.png" data-download-href="/uploads/short-url/cLg2PlkJx5L3YCMpB79CfqzcDX9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5971ad2e1885ab64281ae7bf0b0094c179c9723f.png" alt="image" data-base62-sha1="cLg2PlkJx5L3YCMpB79CfqzcDX9" width="690" height="417" data-dominant-color="343538"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×482 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We could share this component between MITK and Slicer via CTK as we do it with many other widgets.</p>

---

## Post #26 by @muratmaga (2019-09-18 18:29 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> drafted a prototype for keyframe editor (<a href="https://github.com/pieper/SlicerAnimator" rel="nofollow noopener">https://github.com/pieper/SlicerAnimator</a>)<br>
We need the keyframes to edit the transfer functions, but perhaps there might be a way to combine them.</p>

---

## Post #27 by @pieper (2019-09-21 19:36 UTC)

<p>Yes, the SlicerAnimator extension is a first pass, but it covers a lot of our target goals, like integration with mrml and sequences, extensibility, pretty simple to use, etc.  I’m planning to polish off a few of the things listed in the issues, but then wait and see if we get some more development resources.</p>

---

## Post #28 by @muratmaga (2020-11-17 17:39 UTC)

<p>The main code for SlicerAnimator is now located at:<br>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Animator" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/45026482?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Animator" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph</a></h3>

<p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
