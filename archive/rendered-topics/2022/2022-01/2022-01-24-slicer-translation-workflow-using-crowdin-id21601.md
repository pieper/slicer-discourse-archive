---
topic_id: 21601
title: "Slicer Translation Workflow Using Crowdin"
date: 2022-01-24
url: https://discourse.slicer.org/t/21601
---

# Slicer translation workflow using crowdin

**Topic ID**: 21601
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/slicer-translation-workflow-using-crowdin/21601

---

## Post #1 by @lassoan (2022-01-24 19:30 UTC)

<p>During the project week we explored crowding and various options for implementing a translation workflow. I’ve read up on various documentations and see how other projects do this and tested a couple of approaches and came up with the followings.</p>
<details>
<summary>
Requirements</summary>
<ul>
<li>We should minimize the burden of translation on developers. Developers just need to mark strings in their software as translatable. just by adding tr() in C++ and _() in Python should be enough. Developers are not the same people as translators: even if a developer can translate to 1-2 languages, most of the work relies on community effort.</li>
<li>Updated translations must be provided for released Slicer Stable versions, as users should not wait for the next stable release (ideally available in 3 months, but may be up to 6-12 months).</li>
<li>Translators should be able to immediately test their translations, preferably with an offline option, but definitely without committing updates into version controlled repositories - to reduce noise in repositories (too many notifications, hard-to-read change log, etc.).</li>
<li>Translators should be able to start translating new/modified translatable strings soon after developers introduce them.</li>
<li>Crowdin should only add convenience but must remain replaceable to allow private custom applications and extensions to be translated without requiring crowdin (which is only free for open projects).</li>
<li>Extension developers should be able to test translatable string extraction quickly. It should not require building Slicer or the modules, because extension developers who only have scripted modules do not have it. It also makes it easier to set up quick automatic translation workflows in continuous integration if building is not needed. Preferably only Python should be required, installing Slicer and some extension should be OK (that is already needed for development and testing). Installing CMake and Qt may be tolerable, but preferably should be avoided.</li>
</ul>
</details>
<p><strong>Proposed implementation:</strong></p>
<ul>
<li>Create a separate repository: SlicerLanguagePacks
<ul>
<li>Stores .ts files (synchronized with crowdin’s github integration)</li>
<li>Contains an extension: LanguagePacks
<ul>
<li>Offers a module for helping translators (so that they can test out everything without waiting for nightly build actions and offline): update ts template files, download updated ts files, generate qm files, install qm files immediately.</li>
</ul>
</li>
<li>Extension package contains compiled qm files of all extensions. Users can install latest translations via the extensions manager the same way as any other extensions. Later extension auto-update can ensure latest translations are installed.</li>
</ul>
</li>
<li>During nightly builds on factory:
<ul>
<li>Extract translatable strings into source .ts files from Slicer core and all extensions</li>
<li>Commit source .ts files into SlicerLanguagePacks repository</li>
<li>Trigger crowdin synchronization (may just wait for the automatic synchronization): this uploads the updated source .ts files from SlicerLanguagePacks to Crowdin and creates a git pull request to update localized .ts files in SlicerLanguagePacks</li>
<li>Merge Crowdin’s SlicerLanguagePacks pull request</li>
<li>Compile localized .ts files are compiled into .qm files</li>
<li>Include Slicer core qm files into Slicer installer package. The qm files included in the Slicer core install package will be overridden by translations downloaded via SlicerLanguagePacks extension.</li>
<li>Include latest Slicer core qm files and extensions qm files into SlicerLanguagePacks extension.</li>
</ul>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04b742db26b40276eac25131bf949d5a7bfb8d4.png" data-download-href="/uploads/short-url/w0cBYfO2pYBJzNL3c4YJB80IPI0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_690x385.png" alt="image" data-base62-sha1="w0cBYfO2pYBJzNL3c4YJB80IPI0" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_1380x770.png 2x" data-dominant-color="7797BD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1951×1090 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<details>
<summary>
Rationale</summary>
<ul>
<li>Extension name: LanguagePacks (instead of Languages, Translations, Internationalization, Localization) because language pack is strongly suggests that it is a software addons to specify additional spoken languages. Languages could refer to programming languages, Translations could refer to various transformations (spatial, file formats, etc.). It is also easier to search for information (in google, discourse, etc.) with a more specific term as language pack. Internationalization and Localization are technical terms that most users would not know what refers to in this context.</li>
<li>Slicer module replaces the need for continuous integration (e.g., immediately compiling ts to qm file on the server). Continuous integration could continuously look for changes in all extensions, extract translatable strings, and upload to crowdin; but it might not be easy to watch hundreds of repositories and also it could generate lots of commits, while it would still not be real-time enough.</li>
<li>Extensions and Slicer core is updated nightly, so updating qm files more frequently than once a day has limited use (it may be useful for Python scripted modules only). Translators for all languages are not all immediately available, but probably require at least a couple of days. So, if translation can only start the next day (not on the day of the new strings creation) is not a significant delay.</li>
<li>Testing out translation updates in real-time requires downloading from crowdin, compiling to qm, and updating the qm files in the install tree</li>
<li>Qm files are bundled in the install package to make the application self-contained. If we want to allow language selection in the installer or in the application (e.g., popup when the application is first started) then we would already need localized text. Also, users may not find it easy to download language packs separately from the application and then install it in the same location as the application.</li>
<li>There is no need to store source .ts files in Slicer core’s repository, as these files can be easily generated anytime. Also, we would not be able to store these .ts files for extensions in each extension anyway (that would require assistance from the extension developer), so it is easier to store all source .ts files in the SlicerLanguagePacks repository.</li>
</ul>
</details>
<p><strong>Questions:</strong></p>
<ul>
<li>How to translate Python scripted module’s .py files and CLI module descriptor XML files?
<ul>
<li>Option A. Pre-process the .py and .xml files to create intermediate files that Qt’s <code>lupdate</code> tool can parse</li>
<li>Option B: Generate .ts files directly. For example, there are tools that can extract text from <em>_()</em> function calls in Python files. We could probably create an XSL transform that would create a .ts file from the module descriptor .xml file directly (very similarly to how .md files are generated from these files).</li>
</ul>
</li>
<li>How to organize the .ts file and folder structure (what to put in a .ts file, how to organize .ts files into folders)?
<ul>
<li>Option A: Create a separate .ts for each module. There are 150 modules in Slicer core and there are about 200 extensions, each containing typically a couple of modules. A new folder can be added for each extension. Challenges: There would be many files and the file list would change as modules are added/removed/renamed. It is not always clear which module provides text for a specific message on the GUI. It is slightly more complicated to generate per-module .ts files without building the application (creating .ts files without requiring building the application is useful, as it makes continuous/on-demand translation updates much simpler).</li>
<li>Option B: Create a single .ts file for Slicer core, and a separate .ts file for each extension. The Slicer core translation file is about 700KB, which is not too big. Challenges: Slicer core uses about 2600 terms, so it cannot be browsed, only filtered/searched. It is not possible to see percentage completion per module or meaningfully use Crowdin’s priority feature (you can specify low/normal/high priority for each file).</li>
<li>Option C: Have a mix between options A and B - modules could be organized into categories (such as module categories) to have a few dozens of files for Slicer core instead of 150. It would probably still make sense to have a single .ts file per extension.</li>
</ul>
</li>
</ul>
<p>Any comments and suggestions are welcome. I also hope we can discuss this tomorrow at the <a href="https://discourse.slicer.org/c/community/hangout/20">Slicer Weekly meeting</a>.</p>

---

## Post #2 by @Fernando (2022-01-24 23:27 UTC)

<p>Nice! I just “suggested 44 translations into Spanish”.</p>

---

## Post #3 by @cpinter (2022-01-25 09:15 UTC)

<p>Amazing summary <a class="mention" href="/u/lassoan">@lassoan</a>! I like the plan.</p>
<p>Questions:</p>
<ul>
<li>Option B seems like a good choice for XMLs because as you said we already have a proven way of processing them. The question is how easy it is for Python. It’s not hard to write a script but maybe there is a simpler option. By the way above you write <code>_()</code> and here <code>_t()</code> for marking translatable strings. I did a quick search but didn’t find it. Which one is correct? Where does it come from?</li>
<li>Again I prefer Option B, for the simple fact that in that case there would be no duplicate terms, thus the same term is guaranteed to be translated the same way in each module/panel/etc. Also there are parts of Slicer that are not related to modules (main window, extension manager, python window) which could be hard to organize (they could be called <code>Base</code> but probably there are such components outside the Base folder). I don’t consider the lack of browsability an issue - people are used to searching I guess.</li>
</ul>

---

## Post #4 by @lassoan (2022-01-25 15:29 UTC)

<p>Thanks for the feedback.</p>
<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="21601">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>By the way above you write <code>_()</code> and here <code>_t()</code> for marking translatable strings</p>
</blockquote>
</aside>
<p>That was just a typo, I’ve fixed it now.</p>

---

## Post #5 by @lassoan (2022-03-09 20:43 UTC)

<p>Just a quick update: we are switching over from Crowdin to Weblate. See more information about what motivated the move <a href="https://discourse.slicer.org/t/czi-essential-open-source-software-for-science-eoss-award-for-3d-slicer-internationalization/19500/19">here</a>. The architecture remains the same as in the image above.</p>

---
