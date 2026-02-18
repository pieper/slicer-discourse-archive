# Update of Slicer issue tracker

**Topic ID**: 437
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/update-of-slicer-issue-tracker/437

---

## Post #1 by @jcfr (2017-06-02 21:17 UTC)

<p>Hi Everyone,</p>
<p>Now that <a class="mention" href="/u/freephile">@freephile</a> migrated the issue tracker to its new home:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/260b51cea87582cb4a1284d84aa26d7d76c757b01131b5c8f7aa1b2fca0e65fd/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/issues" target="_blank" rel="noopener">Issues · Slicer/Slicer</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Issues · Slicer/Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(still available from  <a href="http://na-mic.org/Bug">http://na-mic.org/Bug</a> and <a href="http://www.na-mic.org/Bug">http://www.na-mic.org/Bug</a> to ensure existing links work)</p>
<p>We are planning to upgrade the version of the tracker:</p>
<ul>
<li>
<p>You can get a feel for the interface here: <a href="https://www.mantisbt.org/bugs/my_view_page.php" class="inline-onebox">My View - MantisBT</a></p>
</li>
<li>
<p>You will find below a preview of the Slicer interface below.</p>
</li>
<li>
<p>It will be a different user interface but we think that the new UI will improve the overall experience.</p>
</li>
<li>
<p>The update also includes  a lot of security fixes that are long overdue. See <a href="https://www.mantisbt.org/bugs/changelog_page.php" class="inline-onebox">Change Log - MantisBT</a></p>
</li>
</ul>
<p><strong>Note</strong> In the future, we may also transition to using solely the GitHub issue tracker and project features but that will be discussed later.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d63df6a8465acba173e66d3d63b0029bae0ddfb8.jpg" data-download-href="/uploads/short-url/uzgVXEziRej6eYiKwlKYqhPn4o0.jpg?dl=1" title="slicer-new-tracker.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d63df6a8465acba173e66d3d63b0029bae0ddfb8_2_616x500.jpg" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d63df6a8465acba173e66d3d63b0029bae0ddfb8_2_616x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d63df6a8465acba173e66d3d63b0029bae0ddfb8_2_924x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d63df6a8465acba173e66d3d63b0029bae0ddfb8.jpeg 2x" data-dominant-color="E9EAE9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-new-tracker.jpg</span><span class="informations">1046×848 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @ihnorton (2017-06-03 18:33 UTC)

<p>Thanks for this work. <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=5" title=":100:" class="emoji" alt=":100:"> to moving to GitHub (or GitLab). It may be worth considering whether any more effort should be put in Mantis at all – except possibly to migrate content to GitHub (there are some scripts available which could be modified). Leaving the tracker frozen like the old Kitware trackers would also be fine. There is relatively minimal recent activity on the current tracker because of the reliability and email issues, lack of OAuth, etc., though the history is useful to keep.</p>

---

## Post #3 by @lassoan (2017-06-03 18:55 UTC)

<p>Fully agree with moving issue tracking to GitHub.</p>
<p>GitHub’s issue tracker is still very basic, but it should be good enough to manage Slicer issues. When source code hosting will transition to GitHub then we’ll have to use GitHub’s issue tracker anyway (for managing pull requests, etc), so it would be simpler if we don’t need to manage two trackers. It’ll be also great to have integration with source code repository and not requiring separate account.</p>
<p>I think the simplest would be to prevent adding new issues to Mantis, but we should be able to update/close issues. When we closed or migrated all issues, we can make the repository read-only.</p>

---

## Post #4 by @fedorov (2017-06-04 02:22 UTC)

<p>All for moving to GitHub for issue tracking!</p>
<p>Would be nice, but should not be a stopper, to time this with <a href="https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit">migration of the source code to git</a>.</p>

---

## Post #5 by @jcfr (2017-06-06 21:00 UTC)

<p>To follow up, the Slicer issue tracker has been updated.</p>
<p><a href="https://issues.slicer.org" class="onebox" target="_blank">https://issues.slicer.org</a></p>
<p>Make sure to <code>CTRL-F5</code> next time you visit the site.</p>

---

## Post #6 by @jcfr (2017-06-08 04:04 UTC)

<p>While experimenting with the source integration plugin on Mantis, I re-triggered the import of the “correct” repository  (Slicer/Slicer instead of jcfr/Slicer) and this took down the instance.</p>
<p>Waiting my mistake is addressed , the tracker is unavailable.</p>
<p>Cc: <a class="mention" href="/u/freephile">@freephile</a></p>

---

## Post #7 by @freephile (2017-06-08 04:48 UTC)

<p>Actually, the tracker is available.  The source integration plugin has a nasty feature whereby it blocks (queues) all requests by the same client behind the long-running “import” – making it appear that the server is hung.  Meanwhile, any other client <em>can</em> access the tracker and the load is miniscule.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> kill the import and/or use incognito mode and/or another browser.  I can assure you that the server is fine.</p>

---

## Post #8 by @jamesobutler (2018-10-29 19:26 UTC)

<p>Bumping this thread since there’s already been some good conversation on this topic.</p>
<p>I have found it pretty difficult to use the search within the Mantis Tracker to find relevant results.  It’s hard to quickly find if there is already an issue for a bug that I observe.</p>
<p>ITK recently moved from their issue tracker (JIRA) to GitHub issues. See this <a href="https://discourse.itk.org/t/issues-in-github/1218/15" rel="nofollow noopener">post</a> on their forum.  Here is another <a href="https://discourse.itk.org/t/github-issue-labels/1256" rel="nofollow noopener">post</a> they had about using GitHub labels. For the most part I think Github Issues, Labels, and Milestones could replace a lot of primary functionality in the issue tracker.  There isn’t default assigning of issues, but maybe some github apps could supplement any missing features.</p>

---

## Post #9 by @jamesobutler (2018-10-29 20:05 UTC)

<p>Also Github has issue templates which could encourage detailed steps to reproduce, platform, expected behavior, etc. which would be similar to the header fields on the Mantis Tracker.  ITK is also using <a href="https://help.github.com/articles/manually-creating-a-single-issue-template-for-your-repository/" rel="nofollow noopener">github issue templates</a> to encourage users to provide details about bugs/features/etc. See <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/ISSUE_TEMPLATE.md" rel="nofollow noopener">ITK Issue Template</a>.</p>

---

## Post #10 by @lassoan (2018-11-12 19:51 UTC)

<p>Since mantis stores issues in a structured way (not just somewhat encouraging structure by offering a template), I find it much more efficient to locate issues in Mantis compared to GitHub.</p>
<p>However, I agree that probably GitHub’s issue tracker would be sufficient for Slicer, and definitely more accessible to users and developers, because most people are already familiar with GitHub, they don’t need to register yet another account, and the issue tracker integrates well with other GitHub features.</p>
<p>I think we should just first release Slicer-4.10.1, then move Slicer’s official repository to GitHub (still SVN is the official repository) and then switch to GitHub’s issue tracker.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #12 by @phcerdan (2019-08-20 12:37 UTC)

<p>Any ETA on enabling issues in github? Even if not official yet, would be nice to report bugs/issues there.</p>

---

## Post #13 by @lassoan (2019-08-20 13:05 UTC)

<p>It would be nice to switch to github repository and issue tracker at the same time, to be able to leverage all the benefits of integration between github tools. However, there is no strict dependency, so we could start using github’s issue tracker for new issues any time.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what is the planned date for switching to git?</p>

---

## Post #14 by @jcfr (2019-08-20 13:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>what is the planned date for switching to git?</p>
</blockquote>
</aside>
<p>This is the next major Slicer task on my list, we should expect the transition to happen in the next few weeks.</p>

---

## Post #15 by @lassoan (2019-08-21 15:41 UTC)

<p><a class="mention" href="/u/phcerdan">@phcerdan</a> would this timeline work for you? Can you submit issues to <a href="http://issues.slicer.org" rel="nofollow noopener">issues.slicer.org</a>?</p>

---

## Post #16 by @rprueckl (2019-09-06 08:39 UTC)

<p>Yesterday, I tried to register to the bug tracking system without success, I didn’t get back an email that probably should have contained my password. Following the advice of <a class="mention" href="/u/lassoan">@lassoan</a>, I will post some issues I encountered in this thread.</p>

---

## Post #17 by @rprueckl (2019-09-06 08:43 UTC)

<p>Bug report<br>
Summary: Rulers that should be hidden are always visible after loading a scene<br>
Environment: 3DSlicer 4.10.2, Windows 10</p>
<p>Steps to reproduce:</p>
<ul>
<li>open slicer (standard layout)</li>
<li>create a ruler somewhere</li>
<li>hide it by clicking on the eye of the ruler in the Annotations module UI</li>
<li>save the scene as mrb</li>
<li>close scene (via file menu)</li>
<li>load the mrb<br>
ruler is now visible in slice viewers, however the eye in the Annotations module UI is closed</li>
</ul>

---

## Post #18 by @rprueckl (2019-09-06 08:51 UTC)

<p>Bug report<br>
Summary: Missing repeated question for saving scene when ending slicer<br>
Environment: 3DSlicer 4.10.2, Windows 10</p>
<p>Steps to reproduce:</p>
<ul>
<li>open slicer (standard layout)</li>
<li>create a ruler somewhere (or make any other edit)</li>
<li>click File --&gt; Exit</li>
<li>the confirmation dialog appears --&gt; click ‘Cancel exit’</li>
<li>click File --&gt; Exit<br>
program ends without any further question to save the scene</li>
</ul>
<p>This code causes the immediate exit:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTApp/qSlicerMainWindow.cxx#L1104-L1111" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTApp/qSlicerMainWindow.cxx#L1104-L1111" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTApp/qSlicerMainWindow.cxx#L1104-L1111</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1104" style="counter-reset: li-counter 1103 ;">
<li>// This is necessary because of a Qt bug on MacOS.</li>
<li>// (https://bugreports.qt.io/browse/QTBUG-43344).</li>
<li>// This flag prevents a second close event to be handled.</li>
<li>if (d-&gt;IsClosing)</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>d-&gt;IsClosing = true;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p><strong>(And another one in this post as I cannot post more than three consecutive posts):</strong></p>
<p>Bug report<br>
Summary: Broken marker placement cursor in non-standard layouts<br>
Environment: 3DSlicer 4.10.2, Windows 10</p>
<p>Steps to reproduce:</p>
<ul>
<li>open slicer (standard layout)</li>
<li>switch to another layout (e.g. Compare --&gt; 2 viewers)</li>
<li>click on the tool button to create a fiducial</li>
<li>move cursor over the slice views<br>
the cursor does not change to the markup insertion cursor</li>
</ul>
<p>this is caused by this code:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTGUI/qSlicerMouseModeToolBar.cxx#L538-L570" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTGUI/qSlicerMouseModeToolBar.cxx#L538-L570" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTGUI/qSlicerMouseModeToolBar.cxx#L538-L570</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="538" style="counter-reset: li-counter 537 ;">
<li>// Updated all mapped 3D viewers</li>
<li>for (int i=0; i &lt; layoutManager-&gt;threeDViewCount(); ++i)</li>
<li>  {</li>
<li>  qMRMLThreeDView* threeDView = layoutManager-&gt;threeDWidget(i)-&gt;threeDView();</li>
<li>  if (!threeDView-&gt;mrmlViewNode()-&gt;IsMappedInLayout())</li>
<li>    {</li>
<li>    return;</li>
<li>    }</li>
<li>  // Update cursor only if view interaction node corresponds to the one associated with the mouse toolbar</li>
<li>  if (threeDView-&gt;mrmlViewNode()-&gt;GetInteractionNode() != this-&gt;interactionNode())</li>
<li>    {</li>
<li>    continue;</li>
<li>    }</li>
<li>  threeDView-&gt;setViewCursor(cursor);</li>
<li>  threeDView-&gt;setDefaultViewCursor(cursor);</li>
<li>  }</li>
<li>
</li>
<li>// Updated all mapped slicer viewers</li>
<li>foreach(const QString&amp; viewerName, layoutManager-&gt;sliceViewNames())</li>
<li>  {</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/45cf7d262fc07078fa94ece66520b0ac58f321d7/Base/QTGUI/qSlicerMouseModeToolBar.cxx#L538-L570" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>–&gt; lines 544 and 561 should say <code>continue;</code></p>

---

## Post #19 by @pieper (2019-09-06 12:15 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="16" data-topic="437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Yesterday, I tried to register to the bug tracking system without success, I didn’t get back an email that probably should have contained my password</p>
</blockquote>
</aside>
<p>Hi -</p>
<p>I checked and your account exists on <a href="http://issues.slicer.org">issues.slicer.org</a> under the email you used.  I had it send a password reset link so let’s see if that works.</p>
<p>Anyway thanks for the reports.  <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">  One question: have you tried the nightly builds?  The markups have gotten a lot of improvements.</p>

---

## Post #20 by @rprueckl (2019-09-06 12:20 UTC)

<p>I tried the issue with the ruler not being visible after loading a scene also with the nighlty build from 2019-08-29. It was the same there. Regarding the other two issues, the cited source code is unchanged to version 4.10.2 and I debugged those issues, so I assume they are still relevant.</p>
<p>So far no email received.<br>
Please remove my email address from your previous post - thanks!</p>

---

## Post #21 by @pieper (2019-09-06 12:47 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="20" data-topic="437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Please remove my email address from your previous post - thanks!</p>
</blockquote>
</aside>
<p>Sorry about that!</p>
<aside class="quote no-group" data-username="rprueckl" data-post="20" data-topic="437">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>So far no email received.</p>
</blockquote>
</aside>
<p>Not sure what’s up with that - I got the email that said your account was created.  (I guess you checked your spam folder <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20">).</p>
<p>Anyway looks like you’ve found some good fixes.  The best way forward might be to put them in the form of a github pull request so people can easily test and comment.</p>
<p>Regarding the rulers they have always been a bit finicky and that’s why people have been moving functionality over to markups.</p>

---

## Post #22 by @lassoan (2019-09-06 14:37 UTC)

<p>Thanks for the error reports!</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I know we wanted to wait with switching to github’s issue tracker until we fully migrate Slicer to github, but it seems that the git migration takes really long time. Since Mantis has serious issues (multiple reports of people cannot sign up, we don’t get email notifications of new bugs, losing long bug reports because of server timeout, etc.), I think we could start accepting bug reports via GitHub now.</p>

---

## Post #23 by @lassoan (2019-09-14 14:33 UTC)

<p>Right now, users cannot sign up at <a href="http://issues.slicer.org" rel="nofollow noopener">issues.slicer.org</a> and problems end up just reported here at the forum and if we cannot immediately address them then they may become forgotten.</p>
<p>Is there any objection to enabling the issue tracker for <a href="https://github.com/Slicer/Slicer/" rel="nofollow noopener">https://github.com/Slicer/Slicer/</a> on github?</p>

---

## Post #24 by @jcfr (2019-09-16 12:38 UTC)

<blockquote>
<p>users cannot sign up at <a href="http://issues.slicer.org">issues.slicer.org</a></p>
</blockquote>
<p>Could you remind me what is the problem ? We should then report the problem to <a class="mention" href="/u/freephile">@freephile</a> so that he can have a look.</p>

---

## Post #25 by @lassoan (2019-09-16 14:17 UTC)

<p>I’m not sure if it’s worth spending more time with fixing Mantis. Just a couple of issues that come to my mind:</p>
<ul>
<li>Users are not familiar with Mantis but they know and use github</li>
<li>Many people already have github account and prefer not to create another just to report issues or participate in discussion on Mantis</li>
<li>Mantis is not closely integrated with github (git, projects, etc.)</li>
<li>New user sign-up is too complicated or broken (I remember several reports from the last few years)</li>
<li>Email notifications don’t work (despite all my attempts, I could not configure it to deliver email when any issue is submitted)</li>
<li>Mantis UI is not very intuitive and looks quite dated</li>
<li>Mantis needs hosting and occasional technical support, while github’s issue tracker is for free and fully self-administered through web interface</li>
</ul>
<p>Mantis has lot more features than github’s issue tracker and offers more flexibility, but we can do without these (we don’t rely on any advanced feature in our development process).</p>
<p>I think we have already agreed that we transition to github’s issue tracker, the question is just when and how this should happen.</p>
<p>Maybe one thing that we could consider is to create placeholder github issues for the 4624 issues that we have in Mantis. These automatically generated issues could have the same headline of the original issue, content could be a link to the Mantis issue (with permalink such as <a href="http://issues.slicer.org/123" rel="nofollow noopener">issues.slicer.org/123</a> that could be redirected to mantis or github or anything else in the future), and the status would be closed if the Mantis issue was closed.</p>

---

## Post #26 by @jcfr (2019-09-16 14:37 UTC)

<blockquote>
<p>agreed that we transition to github’s issue tracker, the question is just when and how this should happen</p>
</blockquote>
<p>I will have time to make progress on the overall transition to GitHub this week. Expect a follow up in the next few days. Once this happen, let’s also switch to GitHub issue tracker.</p>

---

## Post #27 by @jcfr (2019-09-16 16:00 UTC)

<p>To elaborate: To ensure we have a lightweight source repo for future checkout (few seconds instead of minutes on a regular internet connection), we may have to rename the current one and create a new one with the same name. This week experiments will help understand what makes sense.</p>

---

## Post #28 by @rprueckl (2020-01-30 16:29 UTC)

<p>this is a report about a potential bug in qMRMLColorTableComboBox<br>
(i think the github tracker is not yet active)</p>
<p>platform: windows<br>
version: 3d slicer 4.10.2</p>
<p>steps to reproduce:</p>
<ol>
<li>start slicer</li>
<li>load a scalar volume</li>
<li>go to the volumes module</li>
<li>ensure the loaded volume is the active volume</li>
<li>the lookup table combobox provides a preview of all colormaps (as expected)</li>
<li>close the scene without saving</li>
<li>load the scalar volume again</li>
<li>go to the volumes module</li>
<li>ensure the loaded volume is the active volume</li>
<li>the lookup table combobox does not provide previews of colormaps anymore</li>
</ol>

---

## Post #29 by @lassoan (2020-01-30 21:28 UTC)

<p>Thank you for reporting this. I’ve added an issue in the issue tracker: <a href="https://issues.slicer.org/view.php?id=4721">https://issues.slicer.org/view.php?id=4721</a></p>

---
