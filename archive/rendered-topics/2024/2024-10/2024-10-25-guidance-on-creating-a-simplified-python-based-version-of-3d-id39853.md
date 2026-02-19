---
topic_id: 39853
title: "Guidance On Creating A Simplified Python Based Version Of 3D"
date: 2024-10-25
url: https://discourse.slicer.org/t/39853
---

# Guidance on Creating a Simplified Python-Based Version of 3D Slicer with Custom Modules

**Topic ID**: 39853
**Date**: 2024-10-25
**URL**: https://discourse.slicer.org/t/guidance-on-creating-a-simplified-python-based-version-of-3d-slicer-with-custom-modules/39853

---

## Post #1 by @nih4t (2024-10-25 03:28 UTC)

<p>Hello everyone,</p>
<p>I’ve successfully built 3D Slicer on my computer, and now I am looking to create a highly simplified version of the application. My goal is to remove about 90% of the existing functionality and focus on using Python for the remaining components. I would like to keep just the core parts of the application and add my own custom Python-based modules.</p>
<p>Any guidance or tips on how to get started would be greatly appreciated!</p>
<p>Thank you!</p>
<p>Nihat</p>

---

## Post #2 by @muratmaga (2024-10-25 03:45 UTC)

<p>You should probably start from this thread and checkout the links provided:</p><aside class="quote" data-post="1" data-topic="31578">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/f1d935/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-there-a-more-detailed-tutorial-on-creating-custom-slicer-application/31578">Is there a more detailed tutorial on creating custom slicer application?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The examples provided on the official website are not detailed enough and hard to learn for me, 
so Is there a more detailed tutorial on creating custom slicer application? step by step tutorial and examples, video tutorial will be more better!
  </blockquote>
</aside>


---

## Post #3 by @pieper (2024-10-25 12:41 UTC)

<aside class="quote no-group" data-username="nih4t" data-post="1" data-topic="39853">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nih4t/48/78310_2.png" class="avatar"> nih4t:</div>
<blockquote>
<p>I would like to keep just the core parts of the application and add my own custom Python-based modules.</p>
</blockquote>
</aside>
<p>There’s work underway to make core libraries independent of the rest of the application.  It would be great if you could join forces with that effort e.g. by testing.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8004">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8004" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8004" target="_blank" rel="noopener">Remove Slicer-application specific stuff from Libs, Base and Loadable modules</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>AlexyPellegrini:slicer-as-a-lib-common-edits</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-23" data-time="13:06:45" data-timezone="UTC">01:06PM - 23 Oct 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/AlexyPellegrini" target="_blank" rel="noopener">
            <img alt="AlexyPellegrini" src="https://avatars.githubusercontent.com/u/106516674?v=4" class="onebox-avatar-inline" width="20" height="20">
            AlexyPellegrini
          </a>
        </div>

        <div class="lines" title="6 commits changed 17 files with 121 additions and 91 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8004/files" target="_blank" rel="noopener">
            <span class="added">+121</span>
            <span class="removed">-91</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is the first PR for the future SlicerLibrary support. This PR contains smal<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8004" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">l changes that doesn't break anything in slicer and should be mergeable at any time.

This basically remove all hardcoded paths that only make sense for the Slicer application from the Base/, Libs /and Modules/Loadable/[Logic|MRML|MRMLDM|vtkWidgets] modules so they can used as libraries and still have the right behavior as long as the caller gives them the right informations. To do this, I removed all inclusions of `vtkSlicerConfiguration.h` from these modules!

This enables all these modules to be built the same way outside and inside the Slicer application, which will be important for SlicerLibrary! 

I want to integrate the changes one at a time to limit the size and complexity of the future SlicerLibrary Pull Request :) Next on the list is VTK 9.4 support.

Please review @jcfr @lassoan 
FYI: @Thibault-Pelletier @finetjul</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
