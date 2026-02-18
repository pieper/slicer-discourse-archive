# Place fiducial button does not work after importing scene

**Topic ID**: 10643
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/place-fiducial-button-does-not-work-after-importing-scene/10643

---

## Post #1 by @cpinter (2020-03-11 14:12 UTC)

<p>Hi all,</p>
<p>I noticed with a very recent nightly that if I do the following:</p>
<ol>
<li>Load a scene</li>
<li>Click the place fiducial button on the toolbar</li>
</ol>
<p>then the preview fiducial does not appear in the viewers under the cursor, and if I click, nothing happens.<br>
If I click the arrow, and select the apparently already selected Fiducial option, then it works, and then every subsequent toolbar button click works as well.</p>
<p>I’m reporting this here because the GitHub transition is supposed to be imminent, and I’m not sure if I should add anything new to Mantis.</p>
<p>First of all, please let me know if you can reproduce it. Second, if someone could fix it, that would be great <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pieper (2020-03-11 14:29 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> -</p>
<p>Maybe it’s something related to the scene.  On a build just updated to master, I can place fiducials as usual on SampleData.</p>

---

## Post #3 by @lassoan (2020-03-11 14:41 UTC)

<p>I cannot reproduce the problem using a recent preview release on Windows either.</p>

---

## Post #4 by @cpinter (2020-03-11 14:53 UTC)

<p>Thank you! I’ll try to see what is special about that scene. There are no fiducials in it, so not sure where to start.</p>

---
