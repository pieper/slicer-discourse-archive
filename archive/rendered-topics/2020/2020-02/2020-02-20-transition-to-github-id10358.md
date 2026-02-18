# Transition to GitHub

**Topic ID**: 10358
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/transition-to-github/10358

---

## Post #1 by @jcfr (2020-02-20 00:01 UTC)

<hr>
<p><s>Here is a preview of what will be the final GitHub repository hosting Slicer sources: <a href="https://github.com/jcfr/Slicer-Git">https://github.com/jcfr/Slicer-Git</a></s><br>
<strong>Update:</strong> Preview repository has been removed. Sources are now available at <a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a></p>
<hr>
<p>Next steps:</p>
<ul>
<li>see details at <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Breakouts/Slicer5/#github-transition">https://projectweek.na-mic.org/PW33_2020_GranCanaria/Breakouts/Slicer5/#github-transition</a>
</li>
</ul>
<p>Waiting we officially transition, please consider reviewing the history and reporting here if authorship or committer is incorrect.</p>
<p>For future reference, scripts and instructions  are archived at <a href="https://github.com/jcfr/Slicer-github-transition-scripts">https://github.com/jcfr/Slicer-github-transition-scripts</a></p>

---

## Post #2 by @lassoan (2020-02-20 04:46 UTC)

<p>This will help us in so many ways, thank you for working on this!</p>
<p>Are you going to add stubs for issues in the bugtracker? (just the subject line, a link to the issue tracker, maybe first N lines of the issue description)</p>
<p>A few tweaks (none of them very important):<br>
-Maybe we could fix links to the SVN repository (e.g., the commit comment contains “git-svn-id: <a href="http://svn.slicer.org/Slicer4/trunk@28773">http://svn.slicer.org/Slicer4/trunk@28773</a>” but this URL is not valid)</p>
<ul>
<li>Maybe add a url to the corresponding commit in the old repository (so that we can easily find a commit based on the old hash)</li>
</ul>

---

## Post #3 by @Davide_Punzo (2020-02-20 07:52 UTC)

<p>That will be great!</p>
<p>not complelty related this, but I was wandering if it would be possible to fix the co-authorship for the following commits:</p>
<ol>
<li>
<p>markups<br>
<a href="https://github.com/jcfr/Slicer-Git/commit/b4098a06bdcbb4ccf33d44c0afc1e201d3590682" rel="nofollow noopener">https://github.com/jcfr/Slicer-Git/commit/b4098a06bdcbb4ccf33d44c0afc1e201d3590682</a><br>
<a href="https://github.com/Slicer/Slicer/commit/23d076495be731efe23cfa1ffdd8a920524a489e" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/23d076495be731efe23cfa1ffdd8a920524a489e</a></p>
</li>
<li>
<p>3d views linking<br>
<a href="https://github.com/jcfr/Slicer-Git/commit/5c04e5c286760eeccf5f02a1eaff8efc77102dd1" rel="nofollow noopener">https://github.com/jcfr/Slicer-Git/commit/5c04e5c286760eeccf5f02a1eaff8efc77102dd1</a><br>
<a href="https://github.com/Slicer/Slicer/commit/3bf8417efd7b949610a8a3765d058e8d3997135f" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/3bf8417efd7b949610a8a3765d058e8d3997135f</a></p>
</li>
</ol>
<p>Andras can confirm my co-authorship for the two commits which I think it was lost in the review/merge process. If it is not possible to add the co-authorship anymore, no problem.<br>
Thanks!</p>

---

## Post #4 by @jcfr (2020-02-22 19:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are you going to add stubs for issues in the bugtracker? (just the subject line, a link to the issue tracker, maybe first N lines of the issue description)</p>
</blockquote>
</aside>
<p>yes</p>
<blockquote>
<p>Maybe we could fix links to the SVN repository (e.g., the commit comment contains “git-svn-id: <a href="http://svn.slicer.org/Slicer4/trunk@28773%E2%80%9D">http://svn.slicer.org/Slicer4/trunk@28773”</a> but this URL is not valid)</p>
</blockquote>
<p>Good point. Instead I was thinking to add an other line of the form:</p>
<pre><code class="lang-auto">svn-url: http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=24838
</code></pre>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="3" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>fix the co-authorship for the following commits:</p>
</blockquote>
</aside>
<p>Of course, I will do.</p>
<p>Note that I will resume work on the transitioning to GitHub when back from traveling after March 1st.</p>

---

## Post #5 by @lassoan (2020-02-22 20:07 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Instead I was thinking to add an other line of the form</p>
</blockquote>
</aside>
<p>Sounds good. Thanks for all your hard work on this.</p>

---

## Post #6 by @hjmjohnson (2020-03-06 02:58 UTC)

<p>Any progress on moving to git.  It is a bit annoying that contributions to svn to not retain attributions very well.</p>

---

## Post #7 by @lassoan (2020-03-06 12:51 UTC)

<p>I really hope that <a class="mention" href="/u/jcfr">@jcfr</a> completes this within days and not weeks.</p>
<p>We save original author in commit comments and use it to look up author when converting the repository to git.</p>

---

## Post #8 by @hjmjohnson (2020-03-06 13:17 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> I appreciate your support.</p>
<p>Sometimes attribution is the only compensation contributors get!</p>

---

## Post #9 by @jcfr (2020-03-06 15:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>completes this within days and not weeks.</p>
</blockquote>
</aside>
<p>Yess, I re-ran all scripts yesterday and will plan on wrapping up next week. (Note: I am out of the office today and Monday)</p>

---

## Post #10 by @hjmjohnson (2020-03-11 14:34 UTC)

<p>Has there been any progress on this transition?</p>

---

## Post #11 by @jcfr (2020-03-11 15:04 UTC)

<p>Working on this today. Stay tuned <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=9" title=":rocket:" class="emoji" alt=":rocket:"></p>
<p>Waiting this is complete, do not commit on either SVN or GitHub</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #12 by @jcfr (2020-03-11 23:28 UTC)

<p>The current repository has been renamed to <a href="https://github.com/Slicer/SlicerGitSVNArchive">https://github.com/Slicer/SlicerGitSVNArchive</a> and a new repository called Slicer has been created.</p>
<ul>
<li>The new <code>Slicer/Slicer</code> is <strong>NOT</strong> yet ready for usage, the history will likely be updated tonight.</li>
<li>Preview build will be disabled tonight and re-enabled tomorrow.</li>
</ul>
<p>Thanks for your patience</p>

---

## Post #13 by @hjmjohnson (2020-03-12 14:24 UTC)

<p>Can we get an update on this process?</p>

---

## Post #14 by @jcfr (2020-03-12 14:25 UTC)

<p>Stub issues mapping with the mantis ones are being created.</p>

---

## Post #15 by @jcfr (2020-03-12 22:00 UTC)

<p>Waiting all stub issues are created do <code>NOT</code> follow the Slicer repository on GitHub, it will spam your inbox.</p>
<p>Cc: <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #16 by @jcfr (2020-03-13 02:01 UTC)

<p>The new repo will be ready to accept contribution (Pull requests, new issue, comments, …) <strong>tomorrow</strong></p>
<p>Nightly build will be re-enabled tonight.</p>
<p>Thanks for your patience</p>
<hr>
<p>In the mean time, what should you do ?</p>
<ul>
<li>Star the new <a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a> repository  <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"> <img src="https://emoji.discourse-cdn.com/twitter/sun_with_face.png?v=9" title=":sun_with_face:" class="emoji" alt=":sun_with_face:">
</li>
<li>Re-fork. See <a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers/FAQ#How_to_update_the_forked_origin_of_your_online_Slicer_fork_.3F">How to update the forked origin of your online Slicer fork ?</a>
</li>
</ul>
<hr>
<p>Details:</p>
<ul>
<li>Updated repository is now available at <a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a>  <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=9" title=":tada:" class="emoji" alt=":tada:">
<ul>
<li>We now have 112 identified GitHub contributors  <img src="https://emoji.discourse-cdn.com/twitter/heart.png?v=9" title=":heart:" class="emoji" alt=":heart:">
</li>
<li>Issue tracker links used in commit message have all been consolidated to use <code>https://issues.slicer.org</code>
</li>
<li>Pull request links used in commit message have been updated to reference <code>Slicer/SlicerGitSVNArchive</code>
</li>
<li>Contributors are properly acknowledged by leveraging the <code>Co-authored-by:</code>  git trailer</li>
<li>Link to svn repository has been added using <code>svn-url:</code> git trailer.</li>
<li>More details available at <a href="https://github.com/jcfr/Slicer-github-transition-scripts#readme">https://github.com/jcfr/Slicer-github-transition-scripts#readme</a>
</li>
</ul>
</li>
<li>Original repository has been renamed to <a href="https://github.com/Slicer/SlicerGitSVNArchive">SlicerGitSVNArchive</a>
</li>
<li>A new FAQ has been created.
<ul>
<li>See <a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers/FAQ#Developer_FAQ:_SVN_to_GitHub">https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers/FAQ#Developer_FAQ:_SVN_to_GitHub</a>
</li>
</ul>
</li>
<li>Issue tracker:
<ul>
<li>All issues from Mantis have a corresponding <a href="https://github.com/Slicer/Slicer/issues">issue in GitHub</a>
</li>
<li>Creation of Mantis issue has been <strong>disabled</strong>
</li>
<li>Moving forward, we will be using GitHub issue tracker</li>
</ul>
</li>
<li>SVN server:
<ul>
<li>commit access has been disabled to all expect <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>
</li>
</ul>
</li>
</ul>
<hr>
<p>Next steps:</p>
<ul>
<li>Update dashboard scripts <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Re-enable nightly dashboard <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Re-enable CircleCI to build PR <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Update script publishing <code>nightly-master</code> branch <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Setup check for commit message prefix. <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">  (see <a href="https://www.commitcheck.com/">https://www.commitcheck.com/</a>)</li>
<li>Setup <code>kwrobot-v1/ghostflow-check-master</code>. See <a href="https://github.com/apps/kwrobot-v1">https://github.com/apps/kwrobot-v1</a>
</li>
<li>Wiki
<ul>
<li>Update <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files">Checkout instructions</a> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Mark<a href="https://www.slicer.org/wiki/Slicer:git-svn"> git-svn instructions</a>  as obsolete.  <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:"> Added Historical template.</li>
<li>Update <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess">ReleaseProcess</a>  <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
<ul>
<li>Update the maintenance guide <a href="https://github.com/Slicer/DashboardScripts/blob/master/maintenance/guides/rename-and-update-release-scripts.md">Rename and update release scripts</a> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
</ul>
</li>
<li>Update <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Source">Source tutorials</a> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
</ul>
</li>
<li>Update <a href="https://github.com/Slicer/Slicer/blob/master/CONTRIBUTING.md">CONTRIBUTING.md</a>  <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Finalize setup of redirects associated with mantis. Will be done by <a class="mention" href="/u/freephile">@freephile</a> and is tracked in <a href="https://discourse.equality-tech.com/t/update-issue-tracker-redirects/1077">https://discourse.equality-tech.com/t/update-issue-tracker-redirects/1077</a> (private link) <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:">
</li>
<li>Enable build of documentation using readthedocs</li>
</ul>

---

## Post #17 by @cpinter (2020-03-13 08:40 UTC)

<p>Thank you so much <a class="mention" href="/u/jcfr">@jcfr</a> for working on the migration! <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"> This was very important and delicate, so also thanks for doing it with such care <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #18 by @lassoan (2020-03-13 16:10 UTC)

<p>This is awesome! <img src="https://emoji.discourse-cdn.com/twitter/champagne.png?v=9" title=":champagne:" class="emoji" alt=":champagne:"></p>
<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> for performing this migration with so much attention to all details. Preserving all the various links, history, contributions, etc. will be very valuable.</p>
<p>Can we start submitting pull requests (and rebase&amp;merge them)?</p>

---

## Post #19 by @hjmjohnson (2020-03-13 16:23 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Awesome!  Waiting for the green light ot make PR’s.</p>
<p>Hans</p>

---

## Post #20 by @lassoan (2020-03-13 17:34 UTC)

<p>Few more things to set up:</p>
<ol>
<li>We should make master branch protected</li>
</ol>
<ul>
<li>“Allow force pushes” and “Allow deletions” unchecked: This make things safer and simpler (at the cost of not being able to cover up potential missteps). It also allows us to use commit count as a monotonously increasing counter for easier revision tracking (instead of SVN revision). It is a minor inconvenience that merge count does not appear in github GUI, but we can determine it quite easily at project build time.</li>
<li>Require pull request reviews before merging: checked (we should try this at least and disable if we find it too annoying or it slows things down too much)</li>
<li>Require status checks to pass before merging: unchecked (for now, until we are confident that checks work very reliably)</li>
<li>Require signed commits: unchecked (I have never used this, but probably not necessary)</li>
<li>Require linear history: checked (non-linear history is just too complicated)</li>
<li>Include administrators: unchecked (there is a warning displayed anyway if you exercise this right, that should be enough)</li>
<li>Restrict who can push to matching branches: checked (have a CoreDevelopers or similar sub category who are allowed to merge changes)</li>
</ul>
<ol start="2">
<li>
<p>Disable “Create a merge commit” option (only allow “Squash and merge” and “Rebase and merge”). Merge commits make reviewing change history a very complicated task.</p>
</li>
<li>
<p>Create Developers group and add people who we want to be able to assign issues to.</p>
</li>
</ol>

---

## Post #21 by @jcfr (2020-03-13 18:10 UTC)

<blockquote>
<p>Can we start submitting pull requests (and rebase&amp;merge them)?</p>
</blockquote>
<p>Yes <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=15" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<h3><a name="p-37284-additional-checks-1" class="anchor" href="#p-37284-additional-checks-1" aria-label="Heading link"></a>additional checks</h3>
<p>Waiting we have automatic testing, let’s make sure not to include large files.</p>
<p>Next week, we will include more pull request checks (reject binary files, etc … see list <a href="https://gitlab.kitware.com/ben.boeckel/rust-ghostflow/blob/github-action/ghostflow-cli/doc/checks.md">here</a>)</p>
<h3><a name="p-37284-master-branch-protected-2" class="anchor" href="#p-37284-master-branch-protected-2" aria-label="Heading link"></a>master branch protected</h3>
<blockquote>
<ol>
<li>We should make master branch protected</li>
</ol>
</blockquote>
<p>I forgot to mention it, but yes the master branch is already protected.</p>
<p>Here is the current configuration for <strong>master</strong> branch:</p>
<pre><code class="lang-plaintext"> [x] Require pull request reviews before merging
   Required approving reviews: 1
   [x] Dismiss stale pull request approvals when new commits are pushed 
   [ ] Require review from Code Owners
   [ ] Restrict who can dismiss pull request reviews

[x] Require status checks to pass before merging 
   [ ] Require branches to be up to date before merging 
   Status checks found in the last week for this repository:
      [x] CommitCheck 
      [ ] ci/circleci: build 

[ ] Require signed commits
[x] Require linear history (Prevent merge commits from being pushed to matching branches. )
[ ] Include administrators (Enforce all configured restrictions above for administrators.)
[ ] Restrict who can push to matching branches 

Rules applied to everyone including administrators 
  [ ] Allow force pushes 
  [ ] Allow deletions
</code></pre>
<h3><a name="p-37284-merge-button-3" class="anchor" href="#p-37284-merge-button-3" aria-label="Heading link"></a>merge button</h3>
<p>Here are the settings for the " Merge button":</p>
<pre><code class="lang-plaintext">[ ] Allow merge commits
[ ] Allow squash merging
[x] Allow rebase merging 

[x] Automatically delete head branches 
</code></pre>
<h3><a name="p-37284-existing-teams-4" class="anchor" href="#p-37284-existing-teams-4" aria-label="Heading link"></a>Existing teams</h3>
<p>Currently we have the following teams:</p>
<ul>
<li>community: Now that we have discourse, I don’t think this is useful. It is also extra maintenance work.</li>
<li>slicer-core: members of this team have admin access to all repository of the Slicer organization.</li>
<li>slicer-website-maintainers: Useful to grant access to only UI/UX folks that are not developers.</li>
<li>localization: Since folks that could contribute translation may not be developer, we should keep this.</li>
</ul>
<p>For reference, here are the current teams:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0726b5f9b09c0bf4faf9514e9abc69a9311b6c4.png" data-download-href="/uploads/short-url/yj5JASARgzGMorOUMDkyd6JzBB2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0726b5f9b09c0bf4faf9514e9abc69a9311b6c4.png" alt="image" data-base62-sha1="yj5JASARgzGMorOUMDkyd6JzBB2" width="341" height="464"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">341×464 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Proposal (updated):</p>
<ul>
<li>Create a <code>slicer-developer</code> team having <strong>write</strong> access to: <code>Slicer</code>, <code>ExtensionsIndex</code> and <code>forks</code></li>
<li>Restrict the number of members in the <code>slicer-core</code> team and change access to <strong>maintain</strong>. This team would have merge right on the master branch.</li>
<li>Create a <code>slicer-admin</code> team with <strong>admin</strong> access to all repos of the Slicer organization</li>
</ul>

---

## Post #22 by @jcfr (2020-03-13 19:02 UTC)

<p>Teams have been consolidated and only member from “slicer-core” team will be able to merge branches into master.</p>
<p>During the upcoming community hangout, we will review this in details.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc232a226aad120ded290f1a2b9f19e8973beac.png" alt="image" data-base62-sha1="vuV6Q8D2cvWx37N6H271km5ZchS" width="336" height="466"></p>

---

## Post #23 by @Sam_Horvath (2020-03-13 20:00 UTC)

<p>What changes (if any) need to be made on <a href="http://download.slicer.org" rel="nofollow noopener">download.slicer.org</a> (since it indexes by svn revision)?</p>

---

## Post #24 by @lassoan (2020-03-14 01:03 UTC)

<p>We can keep generating a revision number from number of commits. See this pull request: <a href="https://github.com/Slicer/Slicer/pull/4731">https://github.com/Slicer/Slicer/pull/4731</a></p>

---

## Post #25 by @ihnorton (2020-03-16 02:23 UTC)

<p>I just pulled up Slicer github to look for something, and noticed all the stars were gone… ouch!</p>
<p>Perhaps this has already been hashed out in depth, but FWIW, throwing away a strong github profile is unfortunate and might be detrimental – users/contributors/granting organizations make a lot of decisions about project viability based on star count …for better or worse. As one example, I think github star count helped to qualify Slicer for free discourse hosting, even though we were somewhat below their listed minimum count.</p>
<p>I guess that a motivation for creating the repo from scratch was to maintain issue number continuity from mantis, but I would suggest transferring the issues from mantis  in to a “github mantis archive” repo instead, which could then be cross-referenced (and the issue transfer seems to only be titles anyway…).</p>
<p>It may also be helpful to know that you can then you can <a href="https://help.github.com/en/github/managing-your-work-on-github/transferring-an-issue-to-another-repository"><em>move</em> issues</a> from the “github mantis archive” to the “real” Slicer repository as needed, maintaining a chain of history (github creates back and forward links), and avoiding the situation where someone will need to triage ~500 issues by going back to mantis (better to triage on-demand).</p>
<p>This would also avoid losing the pull-request history on the existing repo, which seems more valuable than title-only mantis issue numbers.</p>
<p>$.02 from the bleachers!</p>

---

## Post #26 by @jcfr (2020-03-16 03:01 UTC)

<blockquote>
<p>I just pulled up Slicer github to look for something, and noticed all the stars were gone… ouch</p>
</blockquote>
<p>Thanks for the feedback.</p>
<p>This was discussed and we proceeded knowingly. I am confident we will recover our stars <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>There were two main motivations for creating a new repo: (1) filtering history removing large data, the repo is now 5 times smaller, (2) migrating issues.</p>
<p>We will discuss this during the community meeting on Tuesday morning.</p>

---

## Post #27 by @muratmaga (2020-03-16 03:48 UTC)

<p>Sort of follow up on this: On the issues page, mantis links end up with 404. Is this normal?</p>

---

## Post #28 by @jcfr (2020-03-16 12:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="27" data-topic="10358" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Sort of follow up on this: On the issues page, mantis links end up with 404. Is this normal?</p>
</blockquote>
</aside>
<p>Thanks for the report.</p>
<p><a class="mention" href="/u/freephile">@freephile</a> is currently working on setting all redirects.</p>

---

## Post #29 by @ihnorton (2020-03-16 13:12 UTC)

<p>Fair enough, though it took 3+ years to get close to 900 stars. I’ll point out another example where it matters: the Chan-Zuckerberg Initiative EOSS grants are very focused on github metrics (I guess they consider it’s a leading indicator of use/engagement, ahead of citations). If you do proceed with the current plan, I would suggest reaching out to github support to see if they can help in one way or another, but I wouldn’t count on that.</p>
<aside class="quote no-group" data-username="jcfr" data-post="26" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>(1) filtering history removing large data</p>
</blockquote>
</aside>
<p>Just to note that you can do the filtering and force push over the entire history, which will have the same effect as starting from scratch.</p>
<aside class="quote no-group" data-username="jcfr" data-post="26" data-topic="10358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>(2) migrating issues.</p>
</blockquote>
</aside>
<p>If the issue migration included comments, cross-links, etc. then I could see a strong argument, but right now it seems the only benefit is retaining number continuity, at the cost of stars and valuable pull-request comment history.</p>
<p>Anyway, good luck w/ the change-over, and <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"> to everybody.</p>

---

## Post #30 by @cpinter (2020-03-16 13:32 UTC)

<p>I may be naive here, but if we apply for such a grant where GitHub figures matter, then we can mention our recent transition. We have proof of our metrics, because everything is preserved in <a href="https://github.com/Slicer/SlicerGitSVNArchive">https://github.com/Slicer/SlicerGitSVNArchive</a>. I don’t think people generally bother with unstarring… Hopefully the people reviewing the applications can afford an extra click and see the nearly 900 stars, contributors, activity, etc.</p>

---

## Post #31 by @fedorov (2020-03-16 19:35 UTC)

<p>Great to see this done <a class="mention" href="/u/jcfr">@jcfr</a>, thank you and everyone else involved for the hard work on this! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #32 by @freephile (2020-03-18 13:59 UTC)

<h2>
<a href="http://Issues.slicer.org" rel="nofollow noopener">Issues.slicer.org</a> is moved to GitHub</h2>
<ol>
<li>All Mantis URIs not view.php related are served by <a href="http://mantisarchive.slicer.org/" rel="nofollow noopener">mantisarchive.slicer.org/index.php</a>
</li>
<li>The <a href="https://mantisarchive.slicer.org/doc/en-US/Admin_Guide/html-desktop/" rel="nofollow noopener">Admin Guide</a> (2016) reports that there is no feature to make Mantis read-only. There is a threshold to make bugs read-only, so I set this threshold to NOBODY;</li>
</ol>
<h2>Recap</h2>
<ol>
<li>The naked <a href="http://issues.slicer.org/" rel="nofollow noopener">issues.slicer.org</a> domain redirects to GitHub issues.</li>
<li>Any ‘view.php’ related URL like <a href="https://issues.slicer.org/view.php?id=4700" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4700</a> redirects to the equivalent issue at GitHub.</li>
</ol>

---

## Post #33 by @jcfr (2020-03-24 05:26 UTC)

<p>Wiki updates:</p>
<ul>
<li>pages referencing <code>git-svn</code> have been updated. For more details, see <a href="https://discourse.slicer.org/t/transition-to-github/10358/16">previous reply</a>
</li>
<li>
<a href="https://www.slicer.org/wiki/Template:Historical">Historical</a> template has been added to mark page as obsolete while keeping them around for future reference. For example, see obsolete <a href="https://www.slicer.org/wiki/Slicer:git-svn">Slicer:git-svn</a>
</li>
</ul>
<p>Next:</p>
<ul>
<li>Setup <code>kwrobot-v1/ghostflow-check-master</code>. See <a href="https://github.com/apps/kwrobot-v1">https://github.com/apps/kwrobot-v1</a>
</li>
<li>Enable build of documentation using readthedocs</li>
<li>Submit PR to update <a href="https://github.com/Slicer/Slicer/blob/master/CONTRIBUTING.md">CONTRIBUTING</a> guide based on new check configured for master branch.</li>
<li>Wiki:
<ul>
<li>Update reference to issue tracker. GitHub issue tracker supersedes Mantis</li>
</ul>
</li>
</ul>

---
