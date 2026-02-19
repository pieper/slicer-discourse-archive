---
topic_id: 34870
title: "Introduction Of Tiers For Slicer Extensions"
date: 2024-03-13
url: https://discourse.slicer.org/t/34870
---

# Introduction of "tiers" for Slicer extensions

**Topic ID**: 34870
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/introduction-of-tiers-for-slicer-extensions/34870

---

## Post #1 by @lassoan (2024-03-13 16:56 UTC)

<p><em>The definition of tiers was revisited during July 16th weekly meeting<sup class="footnote-ref"><a href="#footnote-108214-1" id="footnote-ref-108214-1">[1]</a></sup> and this post was updated accordingly.</em></p>
<p>During our last Slicer developer hangout of March 13th 2024, we discussed the issue that review and approval of new extensions often takes very long time. We identified that the main difficulty was that extensions had to meet many requirements to be admitted to the Extensions Catalog. Reducing the requirements could make extensions approval easier but it could result in having lower quality extensions (harder to use, not well documented or tested, etc.).</p>
<p>To address this problem, we propose organization of Slicer extensions into “tiers”. This helps users understand how mature, well tested, and well supported an extension is and allows extension developers to choose the amount of effort that they are comfortable with investing into the extension.</p>
<p>By default, the Extensions Manager would only show extensions that are in Tier &gt;=3 and users would need to click somewhere in the Extensions Manager to see all extensions. This allows new users to more easily find relevant extensions and less likely to come across experimental extensions that may be hard to use or not well documented.</p>
<p>The proposed tiers are the following:</p>
<h2><a name="p-108214-tier-5-1" class="anchor" href="#p-108214-tier-5-1" aria-label="Heading link"></a>Tier 5</h2>
<p>Critically important extensions, supported by Slicer core developers.</p>
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Slicer core developers accept the responsibility of fixing any issues caused by Slicer core changes; at least one Slicer core developer (anyone who has commit right to Slicer core) must be granted commit right to the extension’s repository</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Automated tests for all critical features</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Maintainers respond to questions related to the extension on the <a href="https://discourse.slicer.org">Slicer Forum</a></li>
<li>All requirements of tiers &lt; 5</li>
</ul>
<h2><a name="p-108214-tier-3-2" class="anchor" href="#p-108214-tier-3-2" aria-label="Heading link"></a>Tier 3</h2>
<p>Community-supported extensions.</p>
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Documentation, tutorial, and test data are provided for most modules. A tutorial provides step-by-step description of at least the most typical use case, include a few screenshots. Any sample data sets that is used in tutorials must be registered with the Sample Data module to provide easy access to the user.</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Follows programming and user interface conventions of 3D Slicer (e.g., GUI and logic are separated, usage of popups is minimized, no unnecessary custom GUI styling, etc.)</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Maintainers respond to issues and pull request submitted to the extension’s repository</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Maintainers respond to questions directly addressed to him/her via <span class="mention">@mention</span> on the <a href="https://discourse.slicer.org">Slicer Forum</a></li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Permissive license is used for the main functions of the extension (recommended Apache or MIT). The extension can provide additional functionality in optional components that are distributed with non-permissive license, but the user has to explicitly approve those before using them (e.g., a pop-up can be displayed that explains the licensing terms and the user has to acknowledge them to proceed).</li>
<li>All requirements of tiers &lt; 3</li>
</ul>
<h2><a name="p-108214-tier-1-3" class="anchor" href="#p-108214-tier-1-3" aria-label="Heading link"></a>Tier 1</h2>
<p>Experimental extensions.</p>
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Extension has a reasonable name (not too general, not too narrow, suggests what the extension is for)</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Repository name is Slicer+ExtensionName</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Repository is associated with <code>3d-slicer-extension</code> GitHub topic so that it is listed <a href="https://github.com/topics/3d-slicer-extension">here</a>. To edit topics, click the settings icon in the right side of “About” section header and enter <code>3d-slicer-extension</code> in “Topics” and click “Save changes”. To learn more about topics, read <a href="https://help.github.com/en/articles/about-topics" class="inline-onebox">Classifying your repository with topics - GitHub Docs</a></li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Extension description summarizes in 1-2 sentences what the extension is usable (should be understandable for non-experts)</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Any known related patents must be mentioned in the extension description.</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> LICENSE.txt is present in the repository root. MIT  (<a href="https://choosealicense.com/licenses/mit/" class="inline-onebox">MIT License | Choose a License</a>) or Apache (<a href="https://choosealicense.com/licenses/apache-2.0/" class="inline-onebox">Apache License 2.0 | Choose a License</a>) license is recommended. If source code license is more restrictive for users than MIT, BSD, Apache, or 3D Slicer license then the name of the used license must be mentioned in the extension description.</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Extension URL and revision (scmurl, scmrevision) is correct, consider using a branch name (main, release, …) instead of a specific git hash to avoid re-submitting pull request whenever the extension is updated</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Extension icon URL is correct (do not use the icon’s webpage but the raw data download URL that you get from the download button - it should look something like this: <a href="https://raw.githubusercontent.com/user/repo/main/SomeIcon.png">https://raw.githubusercontent.com/user/repo/main/SomeIcon.png</a>)</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Screenshot URLs (screenshoturls) are correct, contains at least one</li>
<li>Homepage URL points to valid webpage containing the following:
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Extension name</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Short description: 1-2 sentences, which summarizes what the extension is usable for</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> At least one nice, informative image, that illustrates what the extension can do. It may be a screenshot.</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Description of contained modules: at one sentence for each module</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Publication: link to publication and/or to PubMed reference (if available)</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> License: We suggest you use a permissive license that includes patent and contribution clauses.  This will help protect developers and ensure the code remains freely available.  We suggest you use the <a href="https://github.com/Slicer/Slicer/blob/main/License.txt">Slicer License</a> or the <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0</a>. Always mention in your README file the license you have chosen.  If you choose a different license, explain why to the extension maintainers. Depending on the license we may not be able to host your work. Read <a href="https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project">here</a> to learn more about licenses.</li>
</ul>
</li>
<li>Hide unused github features (such as Wiki, Projects, and Discussions, Releases, Packages) in the repository to reduce noise/irrelevant information:
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Click <code>Settings</code> and in repository settings uncheck <code>Wiki</code>, <code>Projects</code>, and <code>Discussions</code> (if they are currently not used).</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Click the settings icon next to <code>About</code> in the top-right corner of the repository main page and uncheck <code>Releases</code> and <code>Packages</code> (if they are currently not used)</li>
</ul>
</li>
<li>The extension is safe
<ul>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Does not include or download binaries from unreliable sources</li>
<li><span class="chcklst-box fa fa-square-o fa-fw"></span> Does not send any information anywhere without user consent (explicit opt-in is required)</li>
</ul>
</li>
</ul>
<hr>
<p>Extension tier 2 and 4 are reserved for future use, to allow defining intermediate steps between the initially defined tiers without reclassifying every extension.</p>
<h2><a name="p-108214-extensions-catalog-entry-file-4" class="anchor" href="#p-108214-extensions-catalog-entry-file-4" aria-label="Heading link"></a>Extensions catalog entry file</h2>
<p>We also propose to switch from the “Extension description (.s4ext)” file format to a simpler, standard JSON format that only contain necessary information. This file will be called <code>Extensions Catalog entry</code> json file. The filename is the exension’s name (e.g., SlicerOpenIGTLink.json) and it contains the following content:</p>
<pre><code class="lang-auto">{
    "scmurl": "https://github.com/openigtlink/SlicerOpenIGTLink.git",
    "scmrevision": "master",
    "depends": [],
    "category": "IGT"
    "maintainers": ["https://discourse.slicer.org/u/lassoan", "https://discourse.slicer.org/u/sunderlandkyl"]
    "tier": 5
}
</code></pre>
<hr>
<p>Any comments and suggestions are welcome.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-108214-1" class="footnote-item"><p><a href="https://discourse.slicer.org/t/2024-07-16-weekly-meeting/37386" class="inline-onebox">2024.07.16 Weekly Meeting</a> <a href="#footnote-ref-108214-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #2 by @rbumm (2024-03-13 17:29 UTC)

<p>This is great.</p>
<p>It will help to filter the extension manager for older or unsupported extensions.<br>
Concerning the opt-in for sending information from extensions  it would be nice to have demo source code available including the don’t ask again feature, maybe in the script repo.</p>

---

## Post #3 by @jcfr (2024-03-13 19:07 UTC)

<p>For reference, corresponding changes are being implemented in the following pull requests:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/7629" class="inline-onebox">Switch extension index entry format from "s4ext" to "json" by jcfr · Pull Request #7629 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://github.com/Slicer/ExtensionsIndex/pull/2011" class="inline-onebox">CI: Transition from s4ext to json by jcfr · Pull Request #2011 · Slicer/ExtensionsIndex · GitHub</a></li>
</ul>

---

## Post #4 by @jcfr (2024-03-13 19:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>depends</code></p>
</blockquote>
</aside>
<p>Since we will be able to decouple built-time from runtime dependencies, I suggest we rename <code>depends</code> to <code>build_depends</code></p>
<p>The “depends”  metadata currently set in the extension <code>CMakeLists</code> would then correspond to the runtime dependencies (aka extension expected to be installed after clicking on the “install” button)</p>

---

## Post #5 by @lassoan (2024-03-13 19:34 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Since we will be able to decouple built-time from runtime dependencies, I suggest we rename <code>depends</code> to <code>build_depends</code></p>
</blockquote>
</aside>
<p>Renaming sounds good. I would slightly prefer using full words, such as <code>build_dependencies</code>.</p>
<p>In the long term, both build and runtime dependencies should be specified in the repository, in a separate json file so that the both the extension build script can easily read it (to determine the order of build) and CMake files in the extension can access it (so that it can check that all required directories are set, etc.). At that point, the dependencies can be removed from the extensions catalog entry file.</p>

---

## Post #6 by @chir.set (2024-03-13 20:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we discussed the issue that review and approval of <strong>new extensions</strong> often takes very long time</p>
</blockquote>
</aside>
<p>Does this concern extensions already in the extension repository?</p>

---

## Post #7 by @lassoan (2024-03-13 21:17 UTC)

<p>Yes, we’ll need to assign every extension to a tier. I would expect that most extensions that are currently actively maintained will be in Tier 3.</p>

---

## Post #8 by @jamesobutler (2024-05-01 17:14 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="3" data-topic="34870" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>For reference, corresponding changes are being implemented in the following pull requests:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/7629" rel="noopener nofollow ugc">Switch extension index entry format from “s4ext” to “json” by jcfr · Pull Request #7629 · Slicer/Slicer · GitHub </a></li>
<li><a href="https://github.com/Slicer/ExtensionsIndex/pull/2011" rel="noopener nofollow ugc">CI: Transition from s4ext to json by jcfr · Pull Request #2011 · Slicer/ExtensionsIndex · GitHub </a></li>
</ul>
</blockquote>
</aside>
<p>Will setting tiers for all the existing extensions and changing the extensions review process to be more flexible for lower tier extensions happening soon? It appears that the above mentioned PRs regarding switch to the new json format have been completed.</p>

---

## Post #9 by @jamesobutler (2024-05-01 19:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><span class="chcklst-box fa fa-square-o fa-fw"></span> Maintainers respond to issues and pull request submitted to the extension’s repository<br>
<span class="chcklst-box fa fa-square-o fa-fw"></span> Maintainers respond to questions directly addressed to him/her via <span class="mention">@mention</span> on the <a href="https://discourse.slicer.org">Slicer Forum</a></p>
</blockquote>
</aside>
<p>^ These requirements in Tier 3 probably exclude any new developer or a new extension from starting out being published at Tier 3. This is because there isn’t a record yet if the maintainer will respond to questions on the forum and also unclear if the maintainer responds to issues and PR with a brand new extension that hasn’t been used yet.</p>

---

## Post #10 by @lassoan (2024-05-02 05:11 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>These requirements in Tier 3 probably exclude any new developer or a new extension from starting out being published at Tier 3.</p>
</blockquote>
</aside>
<p>We could accept a promise from newcomers to be responsive (and downgrade the extension if the developer turns out not to be committed enough).</p>
<p>But I would also find it reasonable to limit accessible tiers for extensions that don’t have any established community member among its developers (and the extension would be upgraded over time if the developer team proves to be responsive).</p>

---

## Post #11 by @jcfr (2024-05-02 13:34 UTC)

<blockquote>
<p>Will setting tiers for all the existing extensions and changing the extensions review process to be more flexible for lower tier extensions happening soon?</p>
</blockquote>
<p>Now that we just finalized the update of all <a href="https://github.com/Slicer/ExtensionsIndex/pulls?q=is%3Aopen+is%3Apr">opened pull-requests</a> so that they include a <code>json</code> file instead of a <code>s4ext</code> file, this will happen next <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>In the meantime, you can also see <a href="https://github.com/Slicer/ExtensionsIndex/issues/2041#issuecomment-2088786459">here</a> the list of pull requests consolidating extension metadata based on the corresponding s4ext that was contributed.</p>

---

## Post #12 by @jcfr (2024-07-16 18:29 UTC)

<p><strong>Update:</strong> The definition of tiers was revisited during <a href="#footnote-108214-1">July 16th weekly meeting</a> and this post was updated accordingly.</p>

---

## Post #13 by @lassoan (2024-11-25 17:52 UTC)

<p>A pull request has been submitted that assigns tier value for each extension. By default, tier 3 is used for all extensions - except extensions that are not maintained or has other issues are assigned tier 1, and highly important extensions are assigned tier 5. It is expected that tiers will be finalized within about a week. Please review and if you have any comments (e.g., suggest changing tier of a specific extension) then submit it to the pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/2123">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/2123" target="_blank" rel="noopener">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/2123" target="_blank" rel="noopener">Specify "tier" for each extension</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:add-tier</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-11-25" data-time="17:47:26" data-timezone="UTC">05:47PM - 25 Nov 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 200 files with 647 additions and 417 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/2123/files" target="_blank" rel="noopener">
            <span class="added">+647</span>
            <span class="removed">-417</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">By default, Tier 3 is assigned to all extensions - see list of exceptions (that <span class="show-more-container"><a href="https://github.com/Slicer/ExtensionsIndex/pull/2123" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">assigned tier 1 or tier 5 instead) in the commit message.

Associated schema update: https://github.com/Slicer/Slicer/pull/8066

Required for https://github.com/Slicer/Slicer/issues/7474</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @mau_igna_06 (2024-11-25 21:23 UTC)

<p>Just like to put my grain of sand here. For me the extension tiers would mean:<br>
5 → Updated documentation and works well on stable release<br>
4 → Old documentation but works well on stable release<br>
3 → Works well on earlier release and has old documentation<br>
2 → Works well on earlier release but no documentation<br>
1 → Does not work</p>

---

## Post #15 by @lassoan (2024-11-25 21:57 UTC)

<blockquote>
<p>1 → Does not work</p>
</blockquote>
<p>If an extension does not work then it is archived (extension description is moved to the <code>ARCHIVE</code> folder.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="14" data-topic="34870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>5 → Updated documentation and works well on stable release<br>
4 → Old documentation but works well on stable release<br>
3 → Works well on earlier release and has old documentation<br>
2 → Works well on earlier release but no documentation</p>
</blockquote>
</aside>
<p>All these will be mapped to the same tier (Tier 3) because it would be very expensive (thousands of dollars) to test all 200+ extensions or check their documentation after each release. Even if we had the funding to do this now, it would not be sustainable and it would not scale. We already have trouble keeping up with just reviewing new extensions. In contrast, we can easily assess available support: we can see when users ask questions or report problems and developers do not respond. If this happens then we can downgrade an extension’s tier. If a developer requests it and the requirements are met then we can raise an extension’s tier.</p>
<p>Tier 5 is distinguished from tier 3 by their maintainers (same people as Slicer core), long term availability, and quality (additional quality requirements in addition to tier 3). These could be independent attributes. However, it is simpler for users if we can map all properties to a single linear scale. We can revisit in the future if we find that is too much of an oversimplification.</p>

---
