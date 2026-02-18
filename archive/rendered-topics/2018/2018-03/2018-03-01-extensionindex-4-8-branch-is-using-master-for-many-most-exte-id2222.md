# ExtensionIndex 4.8 branch is using master for many (most?) extensions

**Topic ID**: 2222
**Date**: 2018-03-01
**URL**: https://discourse.slicer.org/t/extensionindex-4-8-branch-is-using-master-for-many-most-extensions/2222

---

## Post #1 by @fedorov (2018-03-01 17:35 UTC)

<p>I noticed that many of the extensions in the ExtensionsIndex <code>4.8</code> branch are using <code>master</code> for the extension repo. I initially thought I missed this, but it applies to many popular extensions. This is a big issue considering the breaking changes in Slicer post-4.8.</p>
<p>I am assuming the 4.8 branch was just forked from the master of ExtensionsIndex? Should we establish a process to automatically update all references to <code>master</code> to the latest hash at the time ExtensionsIndex release branch is forked, or at least ask the extensions developers to update the index files?</p>
<p>Problem is, right now it is not straightforward to find the latest hash that was working and was tested against 4.8 branch of Slicer.</p>
<p>8-/</p>

---

## Post #2 by @lassoan (2018-03-01 18:03 UTC)

<p>For the extensions that we maintain, we try to keep them compatible with both 4.8 and master as long as it is possible. It is not by mistake but to reduce maintenance effort: we don’t have to keep applying fixes and improvements to two branches. About half of our extensions still use the same branch for 4.8 and master version of Slicer, but as there are more and more differences, probably eventually all of them will have two branches.</p>

---

## Post #3 by @fedorov (2018-03-01 18:08 UTC)

<p>I see. On our side, it was definitely not intentional. We just missed the update in the 4.8. For some of the extensions, switch to the updated DCMTK is breaking due to changes in the API, and in other extensions there are modifications/improvements which are not yet working, and the result is that the extension is broken both in the nightly and latest stable.</p>
<p>I think it is also important for managing user expectations - master by definition is the place for experiments. It is often not possible to test under the conditions of the dashboard before committing to master, and once you committed, and the result is not working, extension will be broken in stable, which is, well, NOT stable.</p>

---

## Post #4 by @jcfr (2018-03-01 18:47 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>On our side, it was definitely not intentional. We just missed the update in the 4.8.</p>
</blockquote>
</aside>
<p>Choosing to use <code>master</code> branch instead of explicitly updating the hash implies great responsibilities, that is why this is not the default.</p>
<blockquote>
<p>Problem is, right now it is not straightforward to find the latest hash that was working and was tested against 4.8 branch of Slicer.</p>
</blockquote>
<p>Exactly, using <code>master</code> branch prevents from doing any forensic and understanding when things break.</p>

---

## Post #5 by @fedorov (2018-03-01 19:18 UTC)

<p>No question - we screwed up big time, we are to blame, and we have to fix it.</p>
<p>But still, automatic replacement of all references to master with a current (at the time release is cut) master hash would be relatively easy to implement, and would probably improve user experience.</p>

---

## Post #6 by @jcfr (2018-03-01 19:19 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>automatic replacement of all references to master with a current (at the time release is cut) master hash would be relatively easy to implement, and would probably improve user experience.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> This would be great</p>

---

## Post #7 by @cpinter (2018-03-01 19:21 UTC)

<p>I agree with Andrey, updating the extension hashes to the one that was latest at the time of releasing Slicer stable would be an easy solution for this. For extensions that are actively maintained, this hash fixation would make sure that the extension works for the stable, which they can update at their own leisure later. For extensions that are broken… they will remain broken either way.</p>

---

## Post #8 by @fedorov (2018-03-01 20:07 UTC)

<p>I am glad we are in agreement!</p>
<p>I will take the initial pass on the script and make the PR to the ExtensionsIndex repo.</p>

---

## Post #9 by @jcfr (2018-03-01 20:07 UTC)

<p>To summarize, the release checklist could include an extra step:</p>
<ul>
<li>Trigger build for Slicer release</li>
<li>Next day, on one of the factory, run script <code>updateExtensionIndex</code> in extension index build directory.</li>
</ul>
<p>Pseudo code for <code>updateExtensionIndex</code> script:</p>
<pre><code>Input parameters are:
    extensionindex_build_dir .. : Contains a checkout of the extension index
                                                 as well as all source and build dir of each extensions
    release  ...................: Version to associate with the next extension index release branch

(0) Set extensonindex_dir based on extensionindex_build_dir

(1) Get ${extensionName} associated with all ${extensonindex_dir}/*.s4ext

(2) for each ${extensionName}
        cd ${extensionName}
        latest_scmrevision=$(git rev-list -n1 HEAD)
        sed -e "s/scmrevision.*/scmrevision ${latest_scmrevision}/" -i ${extensionName}.s4ext

(3) cd ${extensonindex_dir}

(4) git checkout -b master-${release}

(5) git add -A

(6) git commit -m "Ensure all description files references a specific revision"   # done by slicerbot user

(7) git push origin master-${release}</code></pre>

---

## Post #10 by @jcfr (2018-03-01 20:09 UTC)

<p>Assumptions for the script would be:</p>
<ul>
<li>
<p>all extension source were successfully checked out and are using <code>git</code></p>
</li>
<li>
<p>extension maintainer will be responsible to update the file to use <code>master-X.Z</code> or similar afterward</p>
</li>
</ul>

---

## Post #11 by @fedorov (2018-03-01 21:06 UTC)

<p>PR for discussion/testing etc: <a href="https://github.com/Slicer/ExtensionsIndex/pull/1529">https://github.com/Slicer/ExtensionsIndex/pull/1529</a></p>

---

## Post #12 by @fedorov (2018-03-01 22:19 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> the assumptions you make are not compatible with what I had in mind.</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>all extension source were successfully checked out and are using git</p>
</blockquote>
</aside>
<p>What I had in mind is a script that does not assume that all extensions are checked out, and leave it to the person cutting the release to run it after the branch is created.</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>extension maintainer will be responsible to update the file to use master-X.Z or similar afterward</p>
</blockquote>
</aside>
<p>I think at the time release is prepared, the authority should be with the release maintainer. The release process should not be interrupted by lack of response from the extension maintainer. I also think that it is the courtesy to the future user to “freeze” the functionality of the extension as the default behavior as it was at the time of the release. Advanced extension developers can always revert back.</p>

---

## Post #13 by @jcfr (2018-03-01 23:12 UTC)

<blockquote>
<p>leave it to the person cutting the release to run it after the branch is created.</p>
</blockquote>
<p>Makes sense.</p>
<p>When the script will be finalized and tested (e.g on a fork of the extension index), I suggest we update <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Update_ExtensionsIndex">this step</a> of the release process</p>
<aside class="quote no-group quote-modified" data-username="fedorov" data-post="12" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I think at the time release is prepared, the authority should be with the release maintainer. […]</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @fedorov (2018-03-01 23:26 UTC)

<p>Great, thanks! I will revise the script to add some documentation comments, will test with a fork, and will update the issue then.</p>
<p>Also, as I was going through this process, I discovered that some extension use <code>scmversion release</code> which is a misnomer considering Slicer release process. We should probably follow up with issues for those extensions to resolve this ambiguity…</p>
<pre><code class="lang-auto">fedorov@radiobeat [18:22:14] [~/github/ExtensionsIndex] [master]
% grep release *
DTI-Reg.s4ext:scmrevision release
DTIAtlasBuilder.s4ext:scmrevision release
DTIAtlasFiberAnalyzer.s4ext:scmrevision release
DTIPrep.s4ext:scmrevision release
DTIProcess.s4ext:scmrevision release
DatabaseInteractor.s4ext:scmrevision release
SPHARM-PDM.s4ext:scmrevision release
ShapePopulationViewer.s4ext:scmrevision release
ShapeVariationAnalyzer.s4ext:scmrevision release
</code></pre>

---

## Post #15 by @fedorov (2018-03-08 03:51 UTC)

<p>I updated the PR, it is ready for review now. Once merged, I will update the wiki instructions.</p>

---

## Post #16 by @fedorov (2018-11-16 21:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I just realized <a href="https://github.com/Slicer/ExtensionsIndex/pull/1529">the PR I proposed to help addressing this issue</a> was never reviewed/acted upon, and we’ve just had another release where extensions in the release branch are still using “master” for their versions (e.g., see QuantitativeReporting in 4.10 <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/QuantitativeReporting.s4ext#L10">here</a>).</p>
<p>Given we reached consensus back in Spring, can you consider this PR?</p>
<p>Whatever is the decision on the PR, we should definitely fix references to master in the extensions included in <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.10">https://github.com/Slicer/ExtensionsIndex/tree/4.10</a>!</p>

---

## Post #17 by @lassoan (2018-11-16 22:39 UTC)

<p>Projects that are not maintained anymore will not get new revisions and therefore remain compatible with latest stable. Actively maintained projects are assumed to maintain their ExtensionsIndex entries, too. When versions diverge, then typically separate branch is created (hash is not used even then).</p>
<p><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">Custom Slicer applications</a> do not use the ExtensionsIndex but all extension versions are listed in the main application repository.</p>
<p>Pinning specific git hashes would only help developers, who use branch name in ExtensionsIndex, maintain their extensions, introduce backward incompatible changes, and forget about creating a separate stable branch in their extension repository. This is probably affects just a few extensions.</p>
<p>Anyway, I think it may still worth pinning extension versions using hashes, as it seems simple to do and I don’t see any disadvantages.</p>

---

## Post #18 by @fedorov (2018-11-16 23:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Projects that are not maintained anymore will not get new revisions and therefore remain compatible with latest stable.</p>
</blockquote>
</aside>
<p>Except when there are changes that are not backwards compatible, which did happen for us as I discussed in one of the earlier posts (backwards incompatible API change in DCMTK).</p>
<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Actively maintained projects are assumed to maintain their ExtensionsIndex entries, too.</p>
</blockquote>
</aside>
<p>I would not assume that. People forget. I did forget about the need to freeze hash or make a branch once the release was cut, and I don’t think there was any reminder sent out. But hey - I may well be an outlier! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> It may well be other developers have longer memory.</p>
<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is probably affects just a few extensions.</p>
</blockquote>
</aside>
<p>I do not have any data to support or refute that statement.</p>
<p>Anyway, enough trying to “save the world”! For the sake of expediency, I am just going to update the extensions I maintain, and send reminders to the developers for the extensions I collaborated on.</p>

---

## Post #19 by @lassoan (2018-11-16 23:40 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="18" data-topic="2222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Except when there are changes that are not backwards compatible, which did happen for us</p>
</blockquote>
</aside>
<p>How it is possible? If you don’t make any incompatible change in your extension then it will not break. You can keep using the same branch for both master and stable, and users will keep getting updates. If course things can change in the master branch, which may force you to make changes, but you may still manage that in the same code (e.g., using version checks/ifdefs).</p>
<p>If you are not sure if a change is backward-compatible and don’t have the capacity to test it, then you may decide to stop maintaining the stable branch. I would still not freeze it with a hash but instead create a stable branch in your repository and writing that branch name in the ExtensionsIndex. It would be very clear in your repository (much more explicit than some git hash in another repository) and you could also backport any fixes easily into this branch.</p>

---
