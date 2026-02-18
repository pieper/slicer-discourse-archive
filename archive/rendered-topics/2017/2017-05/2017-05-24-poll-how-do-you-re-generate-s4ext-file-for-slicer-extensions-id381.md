# Poll: How do you (re)generate s4ext file for Slicer ExtensionsIndex?

**Topic ID**: 381
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/poll-how-do-you-re-generate-s4ext-file-for-slicer-extensionsindex/381

---

## Post #1 by @fedorov (2017-05-24 22:29 UTC)

<div class="poll" data-poll-status="open" data-poll-type="multiple" data-poll-min="1" data-poll-max="4" data-poll-public="true" data-poll-name="poll">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="b2d31070773ee92c2a3f4bcd66fb9981">I make my own s4ext file (write from scratch, copy from somewhere and modify it, etc)</li>
<li data-poll-option-id="ec3c72aaaae0336b6168c68cad916204">I use the s4ext file that was generated as part of the extension build process, and re-generate it that way if I need to update s4ext</li>
<li data-poll-option-id="b14e3a339e1260c5f0141ccbc1f8d8b4">If I need to update something in s4ext that is already in ExtensionsIndex, I just edit it manually</li>
<li data-poll-option-id="46bb5bcd1db3953ab2b40b1648d956c3">I use ExtensionWizard to make my extensions, and I use s4ext it creates</li>
<li data-poll-option-id="8db4b0aefa8eeb437c11ceff4c021c98">I use some other approach</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>

---

## Post #2 by @jcfr (2017-05-24 22:33 UTC)

<blockquote>
<p>If I need to update something in s4ext that is already in ExtensionsIndex, I just edit it manually</p>
</blockquote>
<p>I sometime manually edit to only change the git hash.</p>

---

## Post #3 by @fedorov (2017-05-24 22:41 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I sometime manually edit to only change the git hash.</p>
</blockquote>
</aside>
<p>So you should also check the manual edit option too <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>Jokes aside, I hope this is useful, and should also raise awareness of the developers about what is the proper procedure and that they should remember to update the CMakeLists.txt of their extension.</p>

---

## Post #4 by @cpinter (2017-05-25 00:33 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>So you should also check the manual edit option too <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>So as I <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> BUt I edit s4ext’s exactly once: when I change the fixed git hash / svn rev to HEAD. Otherwise generate from CMakeLists</p>

---
