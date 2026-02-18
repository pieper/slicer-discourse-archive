# Running slicer from mac terminal

**Topic ID**: 18908
**Date**: 2021-07-24
**URL**: https://discourse.slicer.org/t/running-slicer-from-mac-terminal/18908

---

## Post #1 by @Panda (2021-07-24 19:32 UTC)

<p>Hello,</p>
<p>There are two issues I am facing - not really clear what’s happening. Quite basic actually:</p>
<ol>
<li>How do you initiate Slicer from mac terminal and run a python script without GUI -the documentation has stuff for Windows</li>
<li>And more importantly, how to run a python script within slicer (using the python inspector)? I am encountering modulenotfound error all the time</li>
</ol>
<p>Any help would be cool.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-07-25 19:35 UTC)

<p>You can do something like the following:</p>
<p><code>/Applications/Slicer.app/Contents/MacOS/Slicer --no-splash --no-main-window --python-code "print('hello slicer'); exit()"</code></p>
<p>Maybe you can suggest edits to any documentation that’s not clear or is too windows-specific?  (e.g. issue a pull request through github with change suggestions).</p>

---

## Post #3 by @Panda (2021-07-27 06:06 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Thank you for the reply <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:">  Yes, I finally figured it out - let me just wrap up with the whole thing - then i will post my solution - with some more details - might help future Mac 3d slicer users - not sure if what I did is the best way to do it, but that’s what I could manage and get things to work <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=10" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"></p>

---

## Post #4 by @koeglfryderyk (2022-02-23 19:26 UTC)

<p>I didn’t see those instructions added to the docs so I created a <a href="https://github.com/Slicer/Slicer/pull/6217" rel="noopener nofollow ugc">pull request</a> with updated instructions in the script repository.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> could you take a look at it?</p>

---

## Post #5 by @pieper (2022-02-23 19:41 UTC)

<p>Thanks <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a>, request is merged.</p>

---
