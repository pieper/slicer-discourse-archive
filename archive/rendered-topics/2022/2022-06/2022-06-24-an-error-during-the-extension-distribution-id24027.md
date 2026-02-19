---
topic_id: 24027
title: "An Error During The Extension Distribution"
date: 2022-06-24
url: https://discourse.slicer.org/t/24027
---

# An error during the extension distribution

**Topic ID**: 24027
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/an-error-during-the-extension-distribution/24027

---

## Post #1 by @CharlesChen (2022-06-24 14:01 UTC)

<p>System: Win 10<br>
Version: 5.0.2<br>
Hello,<br>
I’m new to 3DSlicer, I developed a python scripted extension, which is for computing the percentage of colocalization(Spatial overlap between different channels) of Z-stack TIFF images.</p>
<p>I followed the steps provided in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension" rel="noopener nofollow ugc">Distribute an extension</a> section to submit my extension to the extension index.</p>
<p>Since I want to make the extension appear in the latest stable version of the slicer, I chose to upload my extension description (s4ext) file to the 5.0 branch on the Slicer Extensions Index page.</p>
<p>Here are the steps I took:</p>
<ol>
<li>
<p>Click the “Fork” button on the <a href="https://github.com/Slicer/ExtensionsIndex/tree/5.0" rel="noopener nofollow ugc">Slicer Extensions Index 5.0 branch</a> to create a fork in my personal account.</p>
</li>
<li>
<p>Switch to the 5.0 branch on my forked repository and clicked the “Upload Files” button to upload my extension description (s4ext) file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/862b994cb38613a2016fc71302dcbabae6abd332.png" data-download-href="/uploads/short-url/j8VofmZ2PHEYS3HEZ1vQNG1jrua.png?dl=1" title="figure2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/862b994cb38613a2016fc71302dcbabae6abd332_2_517x229.png" alt="figure2" data-base62-sha1="j8VofmZ2PHEYS3HEZ1vQNG1jrua" width="517" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/862b994cb38613a2016fc71302dcbabae6abd332_2_517x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/862b994cb38613a2016fc71302dcbabae6abd332_2_775x343.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/862b994cb38613a2016fc71302dcbabae6abd332_2_1034x458.png 2x" data-dominant-color="F5F7F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure2</span><span class="informations">1858×824 83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cd658c57c4039978d0e6e40e6629763da04e097.png" data-download-href="/uploads/short-url/mnrIIlafr6PbIltTmZ3FtcDzMdp.png?dl=1" title="figure3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd658c57c4039978d0e6e40e6629763da04e097_2_517x297.png" alt="figure3" data-base62-sha1="mnrIIlafr6PbIltTmZ3FtcDzMdp" width="517" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd658c57c4039978d0e6e40e6629763da04e097_2_517x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd658c57c4039978d0e6e40e6629763da04e097_2_775x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd658c57c4039978d0e6e40e6629763da04e097_2_1034x594.png 2x" data-dominant-color="FAFBFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure3</span><span class="informations">1442×829 35.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>However, I encountered an error while creating the pull request:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9bea9fed863c4a98c2de4c998aad1c666d15e55.png" data-download-href="/uploads/short-url/v4g6CZWuCKx3qvjb6bPgxNIh6g5.png?dl=1" title="figure5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9bea9fed863c4a98c2de4c998aad1c666d15e55_2_517x157.png" alt="figure5" data-base62-sha1="v4g6CZWuCKx3qvjb6bPgxNIh6g5" width="517" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9bea9fed863c4a98c2de4c998aad1c666d15e55_2_517x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9bea9fed863c4a98c2de4c998aad1c666d15e55_2_775x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9bea9fed863c4a98c2de4c998aad1c666d15e55_2_1034x314.png 2x" data-dominant-color="F4F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure5</span><span class="informations">1112×340 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b001906eb7556ece90ee04f02a48d556a9e7951.png" data-download-href="/uploads/short-url/m7cdtAa04ttnmEv5V9kccKiTH8d.png?dl=1" title="figure6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b001906eb7556ece90ee04f02a48d556a9e7951_2_517x199.png" alt="figure6" data-base62-sha1="m7cdtAa04ttnmEv5V9kccKiTH8d" width="517" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b001906eb7556ece90ee04f02a48d556a9e7951_2_517x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b001906eb7556ece90ee04f02a48d556a9e7951_2_775x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b001906eb7556ece90ee04f02a48d556a9e7951_2_1034x398.png 2x" data-dominant-color="4D4A4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure6</span><span class="informations">1568×605 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">#!/bin/bash -eo pipefail
if [[ $CIRCLE_PULL_REQUEST != "" ]]; then
  for base_branch in origin/master $(git branch -r | grep -E "origin\/[0-9](\.[0-9])+" | sort -r); do
    differences=$(git diff $base_branch --name-only)
    if [[ $differences != "" ]]; then
      break
    fi
  done
else
  base_branch=$CIRCLE_BRANCH
fi
echo "export BASE_BRANCH=\"$base_branch\"" &gt;&gt; $BASH_ENV

fatal: ambiguous argument 'origin/master': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git &lt;command&gt; [&lt;revision&gt;...] -- [&lt;file&gt;...]'

Exited with code exit status 128
CircleCI received exit code 128
</code></pre>
<p>Are there any specific solutions and suggestions?<br>
Really appreciate your help in advance!</p>

---

## Post #2 by @lassoan (2022-06-24 15:09 UTC)

<p>We just switched over from changing the main branch name from <code>master</code> to <code>main</code> yesterday. Maybe you got the error message because of that. You now need to create a pull request to merge into the <code>main</code> branch.</p>

---

## Post #3 by @CharlesChen (2022-06-24 15:28 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you so much for your kind reply.<br>
According to your suggestion, here are the steps I will do:</p>
<ol>
<li>
<p>Click the “Fork” button on the <a href="https://github.com/Slicer/ExtensionsIndex/" rel="noopener nofollow ugc">Slicer Extensions Index main branch</a> to create a fork in my personal account.</p>
</li>
<li>
<p>Switch to the main branch on my forked repository and click the “Upload Files” button to upload my extension description (s4ext) file.</p>
</li>
<li>
<p>Create a pull request</p>
</li>
</ol>
<p>Is that correct for me to make the extension appear in the latest stable version of the slicer(5.0)?<br>
In addition, do I also need to change the ‘scmrevision’ in my extension description (s4ext) file <strong>from 5.0 to main</strong>?<br>
Thank you!</p>

---

## Post #4 by @lassoan (2022-06-24 16:46 UTC)

<p>Your current submission (for Slicer-5.0) is already <a href="https://github.com/Slicer/ExtensionsIndex/pull/1847">under review</a>. If the review is completed then we can add it for both the <code>main</code> and <code>5.0</code> branches.</p>

---

## Post #5 by @CharlesChen (2022-06-24 17:21 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>，<br>
Thank you very much for your help and affirmation! First of all, I’ll get back to you after consulting with my supervisor about the license issue, and I’ll follow your tips to address those few tweaks. Also, I really willing to learn how to make the computation faster during the coming project week.<br>
Best regards!</p>

---

## Post #6 by @CharlesChen (2022-06-24 18:27 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
It seems I missed the last preparation meeting, which was held on June 21st.<br>
Therefore, is it still possible for me to create my project page and share it with slicer experts during the coming week?<br>
Thanks!</p>

---

## Post #7 by @lassoan (2022-06-24 18:36 UTC)

<p>Yes, you can still register and add your project page.</p>

---

## Post #8 by @CharlesChen (2022-06-30 13:12 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<blockquote>
<p>Your current submission (for Slicer-5.0) is already <a href="https://github.com/Slicer/ExtensionsIndex/pull/1847" rel="noopener nofollow ugc">under review </a>. If the review is completed then we can add it for both the <code>main</code> and <code>5.0</code> branches.</p>
</blockquote>
<p>I’ve just changed the license of my extension to MIT.<br>
Is this allow the extension to be distributed to 3D Slicer now? Once my extension is distributed, it can be searched and downloaded from the ‘Extension manager’, is that correct?<br>
Thanks!</p>

---

## Post #9 by @lassoan (2022-07-01 04:04 UTC)

<p>Thank you. Your extension is now added to the Extensions Index and it will appear in the Extensions Manager in Slicer from tomorrow or the day after. Check the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a> for any errors related to your extension tomorrow.</p>

---

## Post #10 by @CharlesChen (2022-07-01 12:43 UTC)

<p>Thanks a lot for your help! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
