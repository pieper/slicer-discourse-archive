# RFC: Slicer extension end-of-life procedure

**Topic ID**: 6483
**Date**: 2019-04-12
**URL**: https://discourse.slicer.org/t/rfc-slicer-extension-end-of-life-procedure/6483

---

## Post #1 by @fedorov (2019-04-12 15:53 UTC)

<p>In one of the discussions unrelated to Slicer, someone raised a question about how to properly phase out software tools that for one reason or another are no longer supported/needed/working. Martin Morgan from the <a href="http://bioconductor.org/" rel="nofollow noopener">Bioconductor</a> team shared their <a href="http://bioconductor.org/developers/package-end-of-life/" rel="nofollow noopener">“Package End-of-Life Policy”</a>. Bioconductor is a well-established project in many ways similar to Slicer, but from a very different community. I think it makes sense to learn from them.</p>
<p>I think we should consider having something like this for Slicer extensions. I am pretty sure that there are some extensions that have not been touched for a very long time, where developers are no longer around or are not responding, and which are always red on the dashboard. I think those extensions make a dis-service both the users (since the advertisement of the working functionality provided in in the documentation, raising expectations), to the developers (by polluting the dashboard and making it more difficult to identify real problems), and to the whole image of the platform, raising concerns about quality and the level of curation of the content.</p>
<p>Would be great to hear both from the users and from the developers on this!</p>
<div class="poll" data-poll-status="open" data-poll-public="true" data-poll-results="always" data-poll-type="regular" data-poll-name="poll">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="ded760914b22c3f7e8e2e04fac7fa478">YES, we should have End-of-life policy for 3D Slicer extensions</li>
<li data-poll-option-id="ee303ae42d8025b533ed84178dd6864f">NO, we should not have End-of-life policy for 3D Slicer extensions</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-label">voters</span>
</p>
</div>
</div>
</div>

---

## Post #2 by @pieper (2019-04-12 16:31 UTC)

<p>Very good point.  We actually started discussing this the other day on the developer hangout and started working on a standardized scheme for the extension status.</p>
<aside class="quote quote-modified" data-post="3" data-topic="6288">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/2019-03-26-hangout/6288/3">2019.03.26 Hangout</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" style="--category-badge-color: #12A89D; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
  </div>
  <blockquote>
    Notes: 


Thanks to <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, extension status will be standardized to Stable, Experimental and Unmaintained (or similar). The status will be used to dispatch the build results in appropriate groups: 

for <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="nofollow noopener">SlicerPreview</a> dashboard


Stable|Experimental -&gt; Extensions-Nightly


Unmaintained -&gt; Extensions-Nightly-Unmaintained

code to update <a href="https://github.com/Slicer/Slicer/blob/c8fe2bb6706ff042313c335294fd5444f45ce33b/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L128-L134" rel="nofollow noopener">here</a> in master branch


for <a href="http://slicer.cdash.org/index.php?project=Slicer4" rel="nofollow noopener">SlicerStable</a> dashboard


Stable|Experimental -&gt; Extensions-X.Y-Nightly


Unmaintained -&gt; Extensions-X.Y-Nightly-Unmaintained

co…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-04-12 16:48 UTC)

<p>Thanks for the link. The policy makes complete sense and even if the policy is almost trivial, I agree that it could be useful to put it in writing.</p>
<p>We could address some not-so-trivial issues in the policy. For example, we could explicitly state that if the maintainer does not integrate a pull request that fixes a major issue (e.g., build error) within a specific time limit then (after giving notices, waiting, etc.) the extension may be forked and maintenance taken over by others.</p>

---
