---
topic_id: 8242
title: "Fiber Related Features In Models Module"
date: 2019-08-30
url: https://discourse.slicer.org/t/8242
---

# Fiber related features in Models module

**Topic ID**: 8242
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/fiber-related-features-in-models-module/8242

---

## Post #1 by @cpinter (2019-08-30 19:55 UTC)

<p>Hi all,</p>
<p>I’m working on refactoring the way model hierarchies are handled in Slicer, which ultimately means getting rid of the current concept of model hierarchies altogether.</p>
<p>In the process I bumped into the Fibers feature in the Models module. When the user clicks the Include Fibers checkbox, three tabs appear: Line, Tube, Glyph. It seems to do two things: show the fiber bundle nodes in the tree, and turn on visibility of the nodes of the type of the active tab.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a0ee913e9c509c8b789195dd2d0b2b39f2019fd.png" alt="image" data-base62-sha1="3IwmiRkCweLMOMk7Fo6kl0CQ6ol" width="502" height="32"></p>
<p>Does anyone know</p>
<ol>
<li>Exactly how this feature should work?<br>
a. And whther it works correctly in the latest nightly?</li>
<li>If this feature is needed, or what are the expectations about this in 5.0?</li>
</ol>
<p>Thanks a lot!</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> (I couldn’t find Lauren’s user name here but I think she should definitely chime in)</p>

---

## Post #2 by @fedorov (2019-08-31 01:01 UTC)

<p>I really have no experience with anything fiber, so cannot comment on the actual issue, but Lauren is <a class="mention" href="/u/ljod">@ljod</a>, and I am 110% sure <a class="mention" href="/u/rkikinis">@rkikinis</a> will want to comment on this!</p>

---

## Post #3 by @pieper (2019-08-31 15:44 UTC)

<p>This is a holdover from when <a>SlicerDMRI</a> was extracted from the core and moved to the extension.  At the time I guess people couldn’t find a good way to make the model hierarchies and Models module extensible so some of the fiberbundle-specific code remained in the Models module.  I wasn’t directly involved, but I understand that the fiberbundle infrstructure is still needed for the dmri extension.  On the other hand there’s also a Tractography Display module, so maybe the Models module options are no longer needed.  I agree <a class="mention" href="/u/ljod">@ljod</a> is the best to comment.</p>
<p>The tractography use case tends to really stress the infrastructure since it may generate thousands of fiber bundles grouped into dozen or hundreds of clusters.  We wouldn’t want to break existing functionality unless there is a viable alternative.</p>
<p>It’s great that you are looking into this <a class="mention" href="/u/cpinter">@cpinter</a> and maybe there’s a way to get have a fresh approach that works better than the model hierarchies.  Do you think the subject hierarchy can scale to handle such large numbers of nodes?</p>

---

## Post #4 by @cpinter (2019-08-31 23:13 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="8242">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/rkikinis">@rkikinis</a> will want to comment on this</p>
</blockquote>
</aside>
<p>Just to avoid any confusion, just the model hierarchy nodes and the related old code will disappear, not the option of arranging models into hierarchies <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> It will be taken care of by subject hierarchy, and instead of creating Model Hierarchy nodes, you create Folder items.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="8242">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>maybe there’s a way to get have a fresh approach that works better than the model hierarchies.</p>
</blockquote>
</aside>
<p>A possibility what this feature chould convert into are subject hierarchy options (i.e. in the right-click menu) in the tractography plugin that offers filtering for certain nodes, and/or changing visibility of all nodes of certain types (since the original features seem to do these two things).</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="8242">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Do you think the subject hierarchy can scale to handle such large numbers of nodes?</p>
</blockquote>
</aside>
<p>Yes, SH is faster than SceneModel. So if it used to work with that, then it will work with SH.<br>
Part of the motivation for this change is better handling of atlases (I’m doing it in terms of the OpenAnatomy project).</p>

---

## Post #5 by @pieper (2019-09-01 15:13 UTC)

<p>Sounds great <a class="mention" href="/u/cpinter">@cpinter</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #6 by @ljod (2019-09-01 16:29 UTC)

<p>Hi! Yes we actively use the fiber hierarchies in all our work with fiber bundle atlases. We definitely need this functionality moving forward. Before Alex implemented this functionality as part of my U01, is was virtually impossible to visualize the results of applying our atlases to subject data. It’s great if large numbers of nodes can become more practical since that is a challenge for us.</p>
<p>We don’t have this functionality currently in tractography display, just in the Models module.</p>

---

## Post #7 by @cpinter (2019-09-03 16:13 UTC)

<p>Thanks, <a class="mention" href="/u/ljod">@ljod</a>!</p>
<aside class="quote no-group" data-username="ljod" data-post="6" data-topic="8242">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ljod/48/652_2.png" class="avatar"> ljod:</div>
<blockquote>
<p>We definitely need this functionality moving forward</p>
</blockquote>
</aside>
<p>I will need to re-implement these features, and it would be great to get them right for the first try. If you could define exactly what your current needs are (even if slightly or very different from that of the past), then I could provide a solution that accommodates more the actual situation.</p>
<p>I know you have a very different “upcoming project” <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> So if you don’t have the time, then I’ll do something simple that covers the original setup (for example what I described above). I will get to it on Thursday probably.</p>

---

## Post #8 by @ljod (2019-09-05 19:33 UTC)

<p>Hi Csaba! Steve and I talked about this today. We’d like to have a hangout sometime soon. I will send us all an email now.</p>

---
