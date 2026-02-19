---
topic_id: 14560
title: "Help To Publish New Extension"
date: 2020-11-12
url: https://discourse.slicer.org/t/14560
---

# Help to publish new extension

**Topic ID**: 14560
**Date**: 2020-11-12
**URL**: https://discourse.slicer.org/t/help-to-publish-new-extension/14560

---

## Post #1 by @rbumm (2020-11-12 12:20 UTC)

<p>Hi,</p>
<p>I have created a new extension, created a GIT node but am unable to proceed.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/rbumm/SlicerCTLungAnalyzer" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/18140094?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/rbumm/SlicerCTLungAnalyzer" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerCTLungAnalyzer</a></h3>

<p>This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated and collapsed areas in chest CT examinations.    - rbumm/SlicerCTLungAnalyzer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Could you guys help me ?</p>
<p>What is the easiest way (Windows) to publish (and later update)  this extension and to get it included in Slicers extension library ?</p>
<p>Thank you.<br>
Best regards<br>
rudolf</p>

---

## Post #2 by @jamesobutler (2020-11-12 13:40 UTC)

<p>There are some instructions about how to distribute an extension at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distributing-an-extension" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distributing-an-extension</a>.</p>
<p>There is a main checklist to follow for contributing to the Slicer extensions index that is linked from those instructions.</p>
<p>As part of that process it will detail about creating a S4EXT file which has a line for specifying a git commit branch or hash which can be used for updating the version of your code that is distributed. If you set it to “main”, the name of your only branch, then any updates you push to that branch will be distributed when extensions are built during the next nightly build.</p>

---

## Post #3 by @rbumm (2020-11-12 14:44 UTC)

<p>Thank you James, that is exactly why I asked - I also found the link that you describe, but do not know (because it is not in there) how to create the magical S4EXT file. I also followed the checklist but cannot find an entry for that file. The file is not in my extension directory. The extension wizard has not buttons to create that file <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @jamesobutler (2020-11-12 21:25 UTC)

<p>You can view example S4EXT files that are located in the <a href="https://github.com/Slicer/ExtensionsIndex" rel="noopener nofollow ugc">SlicerExtensionsIndex</a> repo where you will be issuing the PR. You can use the SlicerOpenIGTLink extension’s S4EXT as an <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerOpenIGTLink.s4ext" rel="noopener nofollow ugc">example</a>.</p>

---

## Post #5 by @rbumm (2020-11-13 10:07 UTC)

<p>Thank you, seems to work !</p>

---

## Post #6 by @rbumm (2020-11-14 13:39 UTC)

<p>James, now I have published that extension yesterday and thought it would turn up today in the extension manager (another slicer installation, same version 2020930) on my home computer. But I can not find it there in the extension manager.</p>
<p>It is also not yet present in the slicer app store.<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://slicer.kitware.com/midas3/core/public/images/icons/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://slicer.kitware.com/midas3/slicerappstore" target="_blank" rel="noopener nofollow ugc">slicer.kitware.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://slicer.kitware.com/midas3/slicerappstore" target="_blank" rel="noopener nofollow ugc">Slicer Server by Kitware</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In the slicer appstore I see an upload button. Do I have to upload the extension there or does it get updated automatically ? What format should I use ?</p>
<p>Thank you</p>

---

## Post #7 by @rbumm (2020-11-16 17:02 UTC)

<p>Could somebody help me with this and check the status of CTLungAnalyzer ?<br>
I probably do something wrong but I really would like to get this going.</p>
<p>The extension is here:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/rbumm/SlicerCTLungAnalyzer" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/18140094?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/rbumm/SlicerCTLungAnalyzer" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerCTLungAnalyzer</a></h3>

<p>This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated and collapsed areas in chest CT examinations.    - rbumm/SlicerCTLungAnalyzer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>… and the extension is included here:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/rbumm/ExtensionsIndex" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/18140094?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/rbumm/ExtensionsIndex" target="_blank" rel="noopener nofollow ugc">rbumm/ExtensionsIndex</a></h3>

<p>Slicer extensions index. Contribute to rbumm/ExtensionsIndex development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I think I have created a pull request.</p>
<p>Oh guys - why is this so difficult ?</p>
<p>Thanks for any help</p>

---

## Post #8 by @lassoan (2020-11-16 17:23 UTC)

<p>As you can see, the pull request is open, has not been merged yet: <a href="https://github.com/Slicer/ExtensionsIndex/pull/1747" class="inline-onebox">CTLungAnalyzer added by rbumm · Pull Request #1747 · Slicer/ExtensionsIndex · GitHub</a></p>
<aside class="quote no-group" data-username="rbumm" data-post="7" data-topic="14560">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Oh guys - why is this so difficult ?</p>
</blockquote>
</aside>
<p>We aim to have a quick and simple extension submission process but also ensure that the app store contents is useful and developers get constructive feedback. You created your pull request on Friday and it’s Monday noon now - we just need a bit more time to review your submission.</p>

---

## Post #9 by @rbumm (2020-11-16 19:57 UTC)

<p>Very good, so I seem to have understood the system now …<br>
Thanks both of you for your answers.</p>

---

## Post #10 by @rbumm (2020-11-17 13:34 UTC)

<p>Thank you and please excuse me. I was not aware of the fact that each extension undergoes such a detailed review process.</p>

---

## Post #11 by @pieper (2020-11-17 13:41 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="10" data-topic="14560">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I was not aware of the fact that each extension undergoes such a detailed review process.</p>
</blockquote>
</aside>
<p>We are all lucky when community members have time to share their expertise <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>We do try to be more careful with extensions that will be one-click installable via Slicer’s official extension manager, partly because people will come back here with questions if they don’t understand how/why and extension does or doesn’t work.  If we can’t understand it we can’t help them and it’s trouble for everyone.</p>
<p>On the other hand with some extra effort (and we understand that there is real effort involved) it can be great to see other people using your work and then building on it.</p>
<p>Thanks again for your contribution!</p>

---

## Post #12 by @rbumm (2020-11-25 20:49 UTC)

<p>Hi Steve,</p>
<p>You seem to know the game and process in a great detail and  I - as it is my first Slicer contribution - don’t.</p>
<p>Could you just check the status of the extension ? Is anything more needed from my side ?<br>
Would I get an E-Mail notification if so or if it is published ?<br>
I am starting a clinical trial right now and am already writing the next extension, a semiautomated lung masking script based on segment editor function. It cuts down the total time of manual work for one COVID-19 case to about 10 min. Which is great comapred to the 60 that had to be used so far.</p>
<p>Thanks and greetings</p>

---

## Post #13 by @pieper (2020-11-25 21:02 UTC)

<p>Hi Rudolf -</p>
<p>Thanks for the ping - I think it just fell off the radar so you’ll see I just commented.</p>
<p>And thanks again for the contribution and 'm glad to hear you are able to continue making progress.  Obviously (alas) the world is in ever increasing need of tools to better understand COVID-19.</p>
<p>And yes, indeed I do know the ins and outs of the Slicer process well and I hope is welcoming and at least somewhat transparent to newcomers, but I understand it has unique quirks.  Basically we used to have specific funding to support engineers working on Slicer, but those have ended and we haven’t found a general replacement yet.  Several of us have grants and other projects that use Slicer, we try to keep the processes moving smoothly but it’s not always top on our minds.</p>
<p>Having COVID-19 related extensions will certainly help us make the case for the importance of making Slicer available, so keep them coming!</p>

---

## Post #14 by @Saima (2024-03-28 21:39 UTC)

<p>Hi Andras,<br>
I submitted extension on github on Feb 13. Its BatchBrainMRTumorSegmentation. I do not know the status of it. And if it is merged I do not see it in extension manager. The issue is closed thats why I am asking here.</p>
<p>regards,<br>
Saima</p>

---
