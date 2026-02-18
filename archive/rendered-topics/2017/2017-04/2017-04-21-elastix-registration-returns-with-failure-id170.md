# Elastix registration returns with failure

**Topic ID**: 170
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/elastix-registration-returns-with-failure/170

---

## Post #1 by @Fernando (2017-04-21 15:57 UTC)

<p>Hi Andras,</p>
<p>This looks promising!</p>
<p>I just tried a general registration and got this:<br>
<code>CalledProcessError: Command 'elastix' returned non-zero exit status 1</code></p>
<p>Also, I have a question: does one have to <code>Create new ScriptedModule</code> in the <code>Parameter set</code> button?</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> I tried uploading the error log but got this message:<br>
<code>Sorry, the file you are trying to upload is not authorized (authorized extensions: jpg, jpeg, png, gif).</code></p>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @lassoan (2017-04-21 15:58 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="2" data-topic="165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165/2">Elastix registration toolbox is now available in Slicer</a></div>
<blockquote>
<p>I tried uploading the error log</p>
</blockquote>
</aside>
<p>You can copy paste the relevant part of the log and a link to the full text of the log (on dropbox, onedrive, …)</p>

---

## Post #3 by @lassoan (2017-04-21 16:01 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="2" data-topic="165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165/2">Elastix registration toolbox is now available in Slicer</a></div>
<blockquote>
<p>Also, I have a question: does one have to Create new ScriptedModule in the Parameter set button?</p>
</blockquote>
</aside>
<p>Good point, the widget is there, but it is not used for anything now. I’ll add saving of node selections into the parameter node (<a href="https://github.com/lassoan/SlicerElastix/issues/1" class="inline-onebox">Save selections in the parameter set node · Issue #1 · lassoan/SlicerElastix · GitHub</a>).</p>

---

## Post #4 by @Fernando (2017-04-21 16:16 UTC)

<p>I was trying to upload the .log file. [Trying from GMail now]</p>

---

## Post #5 by @Fernando (2017-04-21 16:20 UTC)

<p>I see that it didn’t work. I’ll just send you the file by email.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="165" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165/4">Elastix registration toolbox is now available in Slicer</a></div>
<blockquote>
<aside class="quote no-group quote-modified" data-username="Fernando" data-post="2" data-topic="165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165/2">Elastix registration toolbox is now available in Slicer</a></div>
<blockquote>
<p>Also, I have a question: does one have to Create new ScriptedModule in the Parameter set button?</p>
</blockquote>
</aside>
<p>Good point, the widget is there, but it is not used for anything now. I’ll add saving of node selections into the parameter node (<a href="https://github.com/lassoan/SlicerElastix/issues/1" class="inline-onebox" rel="noopener nofollow ugc">Save selections in the parameter set node · Issue #1 · lassoan/SlicerElastix · GitHub</a>).</p>
</blockquote>
</aside>
<p>I confess I have never been sure what a parameter node is. I tried the link <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules" rel="noopener nofollow ugc">in the wiki</a>, but it’s dead.</p>

---

## Post #6 by @lassoan (2017-04-21 16:37 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="6" data-topic="165">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/elastix-registration-toolbox-is-now-available-in-slicer/165/6">Elastix registration toolbox is now available in Slicer</a></div>
<blockquote>
<p>I confess I have never been sure what a parameter node is. I tried the link in the wiki, but it’s dead.</p>
</blockquote>
</aside>
<p>I’ve updated the link, the slides are available here:<br>
<a href="https://www.slicer.org/w/images/7/79/SlicerModulesProgrammingBeyondBasics.pdf" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/w/images/7/79/SlicerModulesProgrammingBeyondBasics.pdf</a></p>
<p>Parameter node stores your node and parameter selection so that if you save the scene and reload it you can just click on Apply to run the processing again.</p>
<p>Parameter nodes allow you to set up complete processing pipelines using CLI modules (select the output of a CLI as in input of another CLI). You just load the scene, select data set as input, and the pipeline is re-executed automatically and you see the output as soon as the processing is completed. It only works for CLI modules though (and for loadable and scripted modules that has auto-run/auto-update feature implemented).</p>

---

## Post #7 by @lassoan (2017-04-21 20:43 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> used a yesterday’s Slicer version that had still some issues. There should be no problem in the latest nightly version.</p>

---

## Post #8 by @Fernando (2017-04-24 14:39 UTC)

<p>Working fine now.</p>
<p>Is there a way to choose the type of registration (rigid/affine, etc.) instead of having to choose a preset?</p>

---

## Post #9 by @lassoan (2017-04-24 15:00 UTC)

<p>Type of registration (and many other parameters) are defined by the preset. It could be possible to add some level of preset editing/saving inside the module, but now it’s manual (editing text files; the presets folder can be opened from the Advanced section).</p>

---

## Post #10 by @lassoan (2021-02-02 16:41 UTC)

<p>A post was split to a new topic: <a href="/t/elastix-registration-fails/15798">Elastix registration fails</a></p>

---
