---
topic_id: 13138
title: "Hooks Prevents Merge Upstream Master"
date: 2020-08-24
url: https://discourse.slicer.org/t/13138
---

# Hooks prevents "merge upstream/master"

**Topic ID**: 13138
**Date**: 2020-08-24
**URL**: https://discourse.slicer.org/t/hooks-prevents-merge-upstream-master/13138

---

## Post #1 by @joachim (2020-08-24 09:11 UTC)

<p>In Github, I have my own fork of <a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>. Now I want my fork to be synced, i.e. <a href="https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork" rel="noopener nofollow ugc"><code>git fetch upstream</code> and <code>git merge upstream/master</code></a>. But merging fails because of the standard commit message <em>Merge remote-tracking branch ‘upstream/master’</em>. <code>./Utilities/SetupForDevelopment.sh</code> created a git hook to verify that my commit messages are <code>upstream/master</code>-friendly.</p>
<p>Am I doing things wrong? Should I use <em>ENH: Merge remote-tracking branch ‘upstream/master’</em> in for my local repository? I haven’t collaborated much on Github, so I’m unsure how the workflow should be if I want to contribute.</p>

---

## Post #2 by @jcfr (2020-08-24 13:08 UTC)

<p>Since in the upstream project we only accept these two types of merge, commit messages always starts with the expected prefix.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6257c999584e4d096651a5a480ee5bae2cf15533.png" alt="image" data-base62-sha1="e1YSj8GYyqfywwr3wjRb0bfiD4v" width="308" height="151"></p>
<p>If you would like your fork to be synced, consider doing the following instead:</p>
<pre><code class="lang-auto">git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master 
</code></pre>

---

## Post #3 by @joachim (2020-08-25 17:21 UTC)

<p>I understand that <code>upstream</code> commits should start with one of Slicer’s commit prefixes. I guess I had wrong workflow. I had been working on a local branch (let’s call it <code>local-branch</code>), and since <code>upstream/master</code> evolved at the same time, I thought I should merge <code>upstream/master</code> into <code>local-branch</code> as <a href="https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging" rel="nofollow noopener">explained here</a>. But this caused my problem.</p>
<p>How are you doing when working on a fix/feature on your computer and then later adding it to <code>upstream/master</code>? Are you doing <a href="https://www.atlassian.com/git/tutorials/merging-vs-rebasing" rel="nofollow noopener">local rebasing</a> to keep your repository up to date?</p>

---

## Post #4 by @lassoan (2020-08-25 17:57 UTC)

<p>We don’t let merge commits to in the repository because it makes the history very complicated and obscures actual changes in the code. Therefore all commits must flow Slicer coding conventions.</p>
<p>What I do is “fetch and rebase” instead of “fetch and merge” when getting updates from upstream (and before creating a pull request).</p>

---

## Post #5 by @joachim (2020-08-26 07:33 UTC)

<p>Then <a class="mention" href="/u/lassoan">@lassoan</a>’s post should be an answer to this question. Thank you.</p>
<p>Let say you started working on your <code>local-branch</code> for some feature you want to implement (and later push this feature to <code>upstream/master</code>). For larger work you may have intermediate commits to <code>local-branch</code> to keep your work structured (and backed up your work if you push to your <code>origin</code>). And when you are ready, these intermediate commits can be collapsed into 1 commit having a Slicer-friendly commit message by <code>git rebase -i</code>. Do you use Slicer-friendly commit messages for your temporary, intermediate commits?</p>

---

## Post #6 by @lassoan (2020-08-26 13:27 UTC)

<aside class="quote no-group" data-username="joachim" data-post="5" data-topic="13138">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Do you use Slicer-friendly commit messages for your temporary, intermediate commits?</p>
</blockquote>
</aside>
<p>Yes, because the SetupForDevelopment script installs precommit hook that enforces this (and other coding style rules, such as no space at the end of line, maximum line length, etc.).</p>

---
