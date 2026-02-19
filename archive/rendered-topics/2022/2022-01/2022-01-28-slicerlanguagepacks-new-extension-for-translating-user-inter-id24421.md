---
topic_id: 24421
title: "Slicerlanguagepacks New Extension For Translating User Inter"
date: 2022-01-28
url: https://discourse.slicer.org/t/24421
---

# SlicerLanguagePacks: New extension for translating user interface of Slicer to various languages

**Topic ID**: 24421
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/slicerlanguagepacks-new-extension-for-translating-user-interface-of-slicer-to-various-languages/24421

---

## Post #1 by @lassoan (2022-01-28 15:26 UTC)

<p>We added a new extension that allows translators to see the translation results immediately. It can download and install nightly translations with a single click. It can also install latest translations that are downloaded from Crowdin website.</p>
<p><strong>See <a href="https://github.com/Slicer/SlicerLanguagePacks#how-to-use">setup and usage instructions on the extension’s website</a>.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8a9f91e78ccddca78f5b131061a6b29952dee1.png" data-download-href="/uploads/short-url/1MWJbgSVNR3mTBdKPCqPwJFkYSd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8a9f91e78ccddca78f5b131061a6b29952dee1_2_690x419.png" alt="image" data-base62-sha1="1MWJbgSVNR3mTBdKPCqPwJFkYSd" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8a9f91e78ccddca78f5b131061a6b29952dee1_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8a9f91e78ccddca78f5b131061a6b29952dee1_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8a9f91e78ccddca78f5b131061a6b29952dee1_2_1380x838.png 2x" data-dominant-color="BABABF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2237×1361 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Currently, it requires downloading and installing the Qt toolkit, which is not very convenient (it can take 10-15 minutes). In the near future we will remove this requirement - see details <a href="https://github.com/Slicer/SlicerLanguagePacks/issues/1">here</a>.</p>
<p>Any feedback and suggestions are welcome.</p>

---

## Post #2 by @lassoan (2022-03-09 19:54 UTC)

<p>A few updates about recent developments.</p>
<h1><a name="p-75172-h-1-switch-to-weblate-1" class="anchor" href="#p-75172-h-1-switch-to-weblate-1" aria-label="Heading link"></a>1. Switch to Weblate</h1>
<p>After lengthy discussions and testing, we switched the online translation file editing platform from <a href="https://crowdin.com/">Crowdin</a> to <a href="https://weblate.org">Weblate</a>.</p>
<p>Crowdin was simple to set up but even after a few weeks we ran into problems due to limitations in feature set and configurability - which were not issues on Weblate. Crowdin most important limitations for use included:</p>
<ul>
<li>Lack of attribution: While Crowdin internally keeps track of who added a translation, that information is not available in our github repository. Therefore, contributions of translators cannot be properly publicly acknoledged. In contrast, Weblate properly sets contributor information in each commit in our github repository, see <a href="https://github.com/Slicer/SlicerLanguageTranslations/commit/e62cc52f6099d9117cc3f5c05adb51c99f27c5a2">example</a>.</li>
<li>Lack of open access: Crowdin website required registration, even for just viewing the site content. In contrast, <a href="https://hosted.weblate.org/projects/3d-slicer/3d-slicer/">Slicer project on Weblate can be accessed publicly</a>, without user registration.</li>
<li>Limited bulk data download: Crowdin required manual download of translation files and limited multi-language downloads to managers. In contrast, Weblate allows anyone downloading one or more language packs using simple web requests (this allows single-click language file update in LanguagePacks extension).</li>
<li>Insufficient access control granularity. Crowdin only has 3 fixed roles (translator, proofreader, manager), and we could not configure the site to fulfill our requirements (for example glossary was only editable by managers, while we wanted to allow the community to build the glossary). In contrast, Weblate has fine-grained access control, with customizable roles and permissions.</li>
<li>Limitations in size and versioning of translations: Crowdin’s free service only supports 60k words and 1 branch for translation. This would be most likely sufficient for translating Slicer core, but not for translating documentation; and would have required workarounds for managing translations of multiple Slicer versions. In contrast, Weblate supports 10k strings and unlimited number of branches. There are <a href="https://docs.godotengine.org/es/stable/">examples</a> of Weblate being used for translating documentation hosted on read-the-docs.</li>
<li>Crowdin is closed-source, users do not have the option for self-hosting (maybe except some very expensive enterprise contracts). In contrast, Weblate is open-source and can be self-hosted for free.</li>
</ul>
<p>Currently, we still accept translations from Crowdin, but we will close that project in about a week.</p>
<p><strong>From now on, please <a href="https://hosted.weblate.org/projects/3d-slicer/3d-slicer/">add/edit Slicer translations on Weblate</a>.</strong></p>
<p>Instructions for creating and testing translations are provided in the <a href="https://github.com/Slicer/SlicerLanguagePacks#slicerlanguagepacks-extension">LanguagePacks extension documentation</a>. If you have any questions, please post a new topic (use the <code>i18n</code> tag to indicate that your question is related to internationalization).</p>
<h1><a name="p-75172-h-2-new-find-text-tool-for-finding-text-displayed-in-slicer-on-weblate-website-2" class="anchor" href="#p-75172-h-2-new-find-text-tool-for-finding-text-displayed-in-slicer-on-weblate-website-2" aria-label="Heading link"></a>2. New “Find text” tool for finding text displayed in Slicer on Weblate website</h1>
<p>A convenient tool is added to LanguagePacks extension that allows quickly grabbing text from the Slicer user interface and open look it up on the Weblate website:</p>
<p>          <a href="https://raw.githubusercontent.com/SoniaPujolLab/SlicerLanguagePacks/main/Docs/FindText.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/SoniaPujolLab/SlicerLanguagePacks/main/Docs/FindText.png" width="690" height="272">
          </a>
</p>
<p>See detailed instructions <a href="https://github.com/Slicer/SlicerLanguagePacks#find-text-tool">here</a>.</p>
<h1><a name="p-75172-h-3-next-steps-3" class="anchor" href="#p-75172-h-3-next-steps-3" aria-label="Heading link"></a>3. Next steps</h1>
<p>Currently, all text that are marked as translatable in C++ source code and in .ui files are translatable. We are working on making all strings translatable (CLI modules, Python scripts, various dynamically generated strings).</p>
<p>You can track the progress of our work here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SoniaPujolLab/SlicerLanguagePacks/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SoniaPujolLab/SlicerLanguagePacks/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/8ed31bb091b5c596ab0026ab32c98fe0146bf635dce3d92b1d736f7b31e74f67/SoniaPujolLab/SlicerLanguagePacks" class="thumbnail" alt="" width="" height=""></div>

<h3><a href="https://github.com/SoniaPujolLab/SlicerLanguagePacks/issues" target="_blank" rel="noopener">SoniaPujolLab/SlicerLanguagePacks</a></h3>

  <p>3D Slicer extension for creating, editing, and storing translations for Slicer core and extensions - SoniaPujolLab/SlicerLanguagePacks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2022-11-10 18:24 UTC)

<p>2 posts were split to a new topic: <a href="/t/html-code-gets-corrupted-in-language-translation-files/26187">HTML code gets corrupted in language translation files</a></p>

---

## Post #4 by @lassoan (2022-11-23 22:17 UTC)

<p>We are making progress with making more strings translatable. In latest Slicer Preview Releases, all CLI modules are translatable.</p>

---
