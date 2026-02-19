---
topic_id: 42428
title: "Problem With Stereo Viewing Mode In 3D View"
date: 2025-04-04
url: https://discourse.slicer.org/t/42428
---

# Problem with Stereo viewing mode in 3d view

**Topic ID**: 42428
**Date**: 2025-04-04
**URL**: https://discourse.slicer.org/t/problem-with-stereo-viewing-mode-in-3d-view/42428

---

## Post #1 by @alientex (2025-04-04 03:32 UTC)

<p>Hello,</p>
<p>I am experiencing strange behavior in the 3D view when pressing the ‘3’ key. It displays a ‘Red/Blue’ stereo effect, even though the Stereo Viewing option is set to ‘No Stereo’. Why does it still show the ‘Red/Blue’ effect?</p>
<p><strong>Version:</strong> Slicer 5.8.1 r33241 / 11eaf62</p>

---

## Post #2 by @muratmaga (2025-04-04 05:32 UTC)

<p>Looks like it is an undocumented shortcut for red/blue stereo rendering. Hitting it again disables it.</p>
<p>What do you expect it key 3 to do? Are planning to use it for a custom shortcut?</p>

---

## Post #3 by @alientex (2025-04-04 10:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="42428">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Are planning to use it for a custom shortcut?</p>
</blockquote>
</aside>
<p>Yes, that’s why I don’t want this shortcut to activate when I press the ‘3’ key.</p>

---

## Post #4 by @muratmaga (2025-04-04 17:02 UTC)

<p>I think if you define your custom shortcut, it overrides it but not sure… You may want to open an issue in slicers github repo (or better yet) make the change and submit a PR. Given that it is undocuments (as far as I can tell), it will probably be approved.</p>

---

## Post #5 by @alientex (2025-04-10 05:40 UTC)

<p>I have raised an <a href="https://github.com/Slicer/Slicer/issues/8368" rel="noopener nofollow ugc">issue</a> to the GitHub.</p>

---
