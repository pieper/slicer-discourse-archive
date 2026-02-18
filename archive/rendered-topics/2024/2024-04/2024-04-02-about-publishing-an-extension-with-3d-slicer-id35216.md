# About publishing an extension with 3D Slicer

**Topic ID**: 35216
**Date**: 2024-04-02
**URL**: https://discourse.slicer.org/t/about-publishing-an-extension-with-3d-slicer/35216

---

## Post #1 by @Saima (2024-04-02 03:17 UTC)

<p>Hi,<br>
I submitted extension on github on Feb 13. Its BatchBrainMRTumorSegmentation. I do not know the status of it. And if it is merged I do not see it in extension manager. The issue is closed with the following status.<br>
Successfully merging this pull request may close these issues.</p>
<p>Please help me publish the extension successfully.<br>
Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #2 by @pieper (2024-04-02 20:40 UTC)

<p>Thanks for your patience.  Just so you know, there’s ongoing discussion and work on how to improve the extension process so that review of proposed extensions doesn’t become a bottleneck for progress.  We want to set expectations correctly about how to make extensions available and what users can expect in terms of completeness and support while also simplifying the process for everyone.</p>
<p>You could refer to and perhaps participate in the discussion below to be sure your thoughts as an extension developer are reflected in the design.</p>
<aside class="quote quote-modified" data-post="1" data-topic="34870">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/introduction-of-tiers-for-slicer-extensions/34870">Introduction of "tiers" for Slicer extensions</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    During our last Slicer developer hangout of March 13th 2024, we discussed the issue that review and approval of new extensions often takes very long time. We identified that the main difficulty was that extensions had to meet many requirements to be admitted to the Extensions Catalog. Reducing the requirements could make extensions approval easier but it could result in having lower quality extensions (harder to use, not well documented or tested, etc.). 
To address this problem, we propose orga…
  </blockquote>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7629">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7629" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7629" target="_blank" rel="noopener">Switch extension index entry format from "s4ext" to "json"</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jcfr:transition-extensions-index-build-system-from-s4ext-to-json</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-13" data-time="19:05:52" data-timezone="UTC">07:05PM - 13 Mar 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="5 commits changed 34 files with 479 additions and 429 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7629/files" target="_blank" rel="noopener">
            <span class="added">+479</span>
            <span class="removed">-429</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Implements changes to the Extensions build-system, transitioning from `.s4ext` f<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7629" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">iles to `.json` files for extension catalog entries. Additionally, it updates the ExtensionWizard and module templates to reflect this change and supports contributing `.json` files to the ExtensionsIndex.

As the category is now expected to be defined in the extension catalog entry file, the support for setting the "Category" directly from the ExtensionWizard UI has been removed.

While a .s4ext file is still generated in the built-tree and included in the extension package, this is considered an implementation detail to be addressed in subsequent commits.

The motivations behind these changes include:
* Eliminate redundant and unused information from the "description" file.
* Simplify programmatic parsing of the "description" files
* Decouple the metadata organized in the extension `CMakeLists.txt` from
  the ones organized in this repository and used to drive the build of extensions.
* Enable Slicer maintainers to define and update the extension "category"
  and "enabled" metadata independently of the upstream extension sources.

---- 

It removes the parsing and handling of metadata already defined in the extension `CMakeLists.txt` by the extension index build-system.

The metadata values now extracted from the `&lt;extensionname&gt;.s4ext` file locally generated in the extension build tree are the following:
- "contributors"
- "depends" (runtime dependencies)
- "description"
- "iconurl"
- "homepage"
- "screenshots"

The only metadata values propagated from the `Slicer/ExtensionsIndex` files now formatted as JSON files (`&lt;extensionname.json`) are the following:
- "scm", "scmurl" and "scmrevision"
- "category"
- "build_dependencies"
- "build_subdirectory"
- "enabled"

The extension name is still derived from the catalog entry filename.

Related:
* https://github.com/Slicer/ExtensionsIndex/pull/2011
* https://discourse.slicer.org/t/introduction-of-tiers-for-slicer-extensions/34870</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
