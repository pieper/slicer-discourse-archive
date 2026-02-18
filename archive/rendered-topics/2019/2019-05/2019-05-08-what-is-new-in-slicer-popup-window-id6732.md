# What is new in Slicer popup window

**Topic ID**: 6732
**Date**: 2019-05-08
**URL**: https://discourse.slicer.org/t/what-is-new-in-slicer-popup-window/6732

---

## Post #1 by @muratmaga (2019-05-08 15:38 UTC)

<p>As far as I can tell, there is really no good mechanism to make aware of changes to existing modules and extensions in terms of functionalities (e.g., new features, behavior change etc) to the end user.</p>
<p>I am wondering if there can be a feature in Slicer splash window for people to click and see what’s new and changes in a separate window. I am not sure how infrastructure wise it will work, but perhaps extension developers and core maintainers can self-report in few sentences.</p>

---

## Post #2 by @pieper (2019-05-08 15:58 UTC)

<p>That’s a good point <a href="https://discourse.slicer.org/t/slicer-4-10-1-summary-highlights-and-changelog/5452">the release notes</a> are very comprehensive, but we don’t have a direct link to them in the Welcome module.</p>

---

## Post #3 by @muratmaga (2019-05-08 16:03 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, yes those are very useful, but I am not talking about just feature releases. For example that list lacks the new markup features such as curves, which were after the 4.10.1, I think.</p>
<p>So, someone switching from 4.10.1 to a nightly wouldn’t know that those were added immediately unless they pay close attention to the forum.</p>

---

## Post #4 by @pieper (2019-05-08 16:33 UTC)

<p>True - maybe we should start a discourse topic on “new in the nightly” and encourage people to post there when they update core code to extensions.  We could link that from the Welcome module (or splast screen) too.  It would simplify the task of collecting release notes when the actual release happens.</p>

---

## Post #5 by @muratmaga (2019-05-08 16:45 UTC)

<p>Yes, I think that will work.</p>

---

## Post #6 by @jcfr (2019-05-08 17:33 UTC)

<p>To compile the release notes, I was initially thinking of the following:</p>
<ul>
<li>Developer could add a <code>name-of-the-topic.rst</code> file for each topic branch making a noteworthy change.
<ul>
<li>Before each release, these files would be merged into one release note document.</li>
<li>A <code>Next Release</code> section would be automatically generated with links to each document</li>
<li>This is now documented in <a href="https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit#Setup_infrastructure_to_streamline_writing_of_release_notes" class="inline-onebox">Documentation/Labs/TransitionToGit - Slicer Wiki</a></li>
</ul>
</li>
</ul>
<blockquote>
<p>start a discourse topic on “new in the nightly”</p>
</blockquote>
<p>This is also an interesting idea. Before each release, should we automatically scrap and combing the markdown of each discourse post  ?  I can foresee some challenge in managing this.</p>
<p>What do you mean exactly by <em>encourage people to post there when they update core code to extensions</em> ?</p>
<blockquote>
<p>We could link that from the Welcome module</p>
</blockquote>
<p>Adding a link to the summary of features and fixes added since the last release makes sense.</p>

---

## Post #7 by @pieper (2019-05-08 18:35 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="6732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>What do you mean exactly by <em>encourage people to post there when they update core code to extensions</em> ?</p>
</blockquote>
</aside>
<p>Oops, that was a typo - I meant “update core code or extensions” <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>I like the idea of including the blurb about new functionality directly in the pull request and then adding automatically to the documentation.  This sounds easier to manage, since it can be part of the code review before merging.</p>

---
