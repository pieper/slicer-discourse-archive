---
topic_id: 21748
title: "Around Cursor Transforms Blender Like On Slicer"
date: 2022-02-02
url: https://discourse.slicer.org/t/21748
---

# Around cursor transforms (Blender-like) on Slicer

**Topic ID**: 21748
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/around-cursor-transforms-blender-like-on-slicer/21748

---

## Post #1 by @mau_igna_06 (2022-02-02 10:10 UTC)

<p>Hi. I created a script that lets you transform a rigid object very easily inside slicer.</p>
<p>Here is a demo video (hip to mandible manual registration, useful to plan an ileac crest mandible reconstruction):<br>
<a href="https://drive.google.com/file/d/1N_pP0kthYdhncZ0DbjhV17rznQCbJCZU/view?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/file/d/1N_pP0kthYdhncZ0DbjhV17rznQCbJCZU/view?usp=sharing</a></p>
<p>Here is the code:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa">
  <header class="source">

      <a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa</a></h4>

  <h5>transformModel.py</h5>
  <pre><code class="Python">
# This scripts allows you to have a widget placed initially in the model centroid and the 
# direction matching its principal components. Then two modes are possible "Transform mode" 
# and "Local mode" by pressing g key and h key correspondingly.
# You can change the center of rotation by going to Local mode, moving the widget and then 
# returning to Transform mode. This feature that let's move the plane indenpendently of the 
# model on Local mode and then lets you transform it in Transform mode is what makes this 
# feature useful for manual registration.

# Code Starts here</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/manjula">@manjula</a> what do you think about this? Could we achieve a new workflow for BoneReconstructionPlanner with this?</p>
<p>More info → This is how is done on professional planning software</p><div class="youtube-onebox lazy-video-container" data-video-id="7RMermYOOYY" data-video-title="Virtual surgical planning using a DCIA free flap for mandibular reconstruction" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=7RMermYOOYY" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/7RMermYOOYY/maxresdefault.jpg" title="Virtual surgical planning using a DCIA free flap for mandibular reconstruction" width="" height="">
  </a>
</div>


---

## Post #2 by @manjula (2022-02-02 11:25 UTC)

<p>Hi Mauro,</p>
<p>This looks fantastic and actually, i was going to help post asking for the code to do this for the purpose of the Implant planning workflow I  have developed.  This is godsends to me <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="21748">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>what do you think about this? Could we achieve a new workflow for BoneReconstructionPlanner with this?</p>
</blockquote>
</aside>
<p>Yes, we can definitely do a workflow on this for the Iliac crest/ scapula bone. Actually we can plan this and do the POC surgery as well. I will experiment with the code and get back to you on Friday during the meeting.</p>
<p>best<br>
Manjula</p>

---

## Post #3 by @mau_igna_06 (2022-02-02 11:58 UTC)

<blockquote>
<p>This looks fantastic and actually, i was going to help post asking for the code to do this for the purpose of the Implant planning workflow I have developed.</p>
</blockquote>
<p>So achieved dental implant planning in Slicer. Could you show some pictures?</p>
<blockquote>
<p>Yes, we can definitely do a workflow on this for the Iliac crest/ scapula bone.</p>
</blockquote>
<p>May be I can get a student to work on a module for mandible reconstruction with scapula/iliac-crest. Would you like to have meetings about this and give your clinical inputs for this like you did for mandible reconstruction with fibula?</p>
<p>Mauro</p>

---

## Post #4 by @manjula (2022-02-02 12:05 UTC)

<p>i guess the final piece for dental implant planning workflow was this.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="21748">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>So achieved dental implant planning in Slicer. Could you show some pictures?</p>
</blockquote>
</aside>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/118c94fbf34ea5cba23ef8383399e7efcef17460.mp4">
  </div><p></p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="21748">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>May be I can get a student to work on a module for mandible reconstruction with scapula/iliac-crest. Would you like to have meetings about this and give your clinical inputs for this like you did for mandible reconstruction with fibula?</p>
</blockquote>
</aside>
<p>Just to update you, this code does not work in the preview release. Only in the stable release. It gives weird blobs that do nothing.</p>

---

## Post #5 by @mau_igna_06 (2022-02-02 12:30 UTC)

<blockquote>
<p>Just to update you, this code does not work in the preview release. Only in the stable release. It gives weird blobs that do nothing.</p>
</blockquote>
<p>I updated the code. Now it should work on the preview release also.</p>

---

## Post #6 by @mau_igna_06 (2022-02-02 12:31 UTC)

<p>The video about implants doesn’t work could you try with another link?</p>
<p>Thank you</p>

---

## Post #7 by @manjula (2022-02-02 12:47 UTC)

<p>Thanks for the code update. Please see if this works</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1AhWaTHhJs0tBtqZRFeZ-LUX5be5gXcgV/view?usp=drivesdk">
  <header class="source">

      <a href="https://drive.google.com/file/d/1AhWaTHhJs0tBtqZRFeZ-LUX5be5gXcgV/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1AhWaTHhJs0tBtqZRFeZ-LUX5be5gXcgV/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1AhWaTHhJs0tBtqZRFeZ-LUX5be5gXcgV/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc">Screencast 2022-02-02 17_31_41.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @mau_igna_06 (2022-02-02 12:50 UTC)

<blockquote>
<p>Please see if this works</p>
</blockquote>
<p>It doesn’t work. Sorry</p>
<p>Mauro</p>

---

## Post #9 by @manjula (2022-02-02 13:44 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="Fu-pg2a8B1g" data-video-title="implant" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Fu-pg2a8B1g" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Fu-pg2a8B1g/maxresdefault.jpg" title="implant" width="" height="">
  </a>
</div>


---

## Post #10 by @mau_igna_06 (2022-02-02 13:49 UTC)

<p>Great. Thank you.</p>
<p>How did you achieve the registration of the scan and the CBCT?<br>
How are you creating the surgical guides for this?</p>
<p>If you don’t want to explain it publicly, please send me a mail.</p>
<p>Mauro</p>

---
