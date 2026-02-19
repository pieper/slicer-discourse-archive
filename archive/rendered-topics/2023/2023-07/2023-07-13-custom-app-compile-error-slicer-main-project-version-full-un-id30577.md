---
topic_id: 30577
title: "Custom App Compile Error Slicer Main Project Version Full Un"
date: 2023-07-13
url: https://discourse.slicer.org/t/30577
---

# Custom app compile error (Slicer_MAIN_PROJECT_VERSION_FULL undefined)

**Topic ID**: 30577
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/custom-app-compile-error-slicer-main-project-version-full-undefined/30577

---

## Post #1 by @darabi (2023-07-13 09:55 UTC)

<p>Hello,<br>
I created a custom Slicer application using</p>
<pre><code class="lang-auto">cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>two days ago (main branch is at commit daaa550).</p>
<p>Compilation of all dependencies seems to work, but the compilation of Main.cxx of the custom app fails with</p>
<pre><code class="lang-auto">...
/opt/MyApp/Applications/MyAppApp/Main.cxx: In function ‘int {anonymous}::SlicerAppMain(int, char**)’:
/opt/MyApp/Applications/MyAppApp/Main.cxx:50:90: error: ‘Slicer_MAIN_PROJECT_VERSION_FULL’ was not declared in this scope; did you mean ‘Slicer_MAIN_PROJECT_APPLICATION_NAME’?
   50 |     QString windowTitle = QString("%1 %2").arg(Slicer_MAIN_PROJECT_APPLICATION_NAME).arg(Slicer_MAIN_PROJECT_VERSION_FULL);
      |                                                                                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |                                                                                          Slicer_MAIN_PROJECT_APPLICATION_NAME
make[5]: *** [Applications/MyAppApp/CMakeFiles/MyAppApp.dir/build.make:76: Applications/MyAppApp/CMakeFiles/MyAppApp.dir/Main.cxx.o] Error 1
make[4]: *** [CMakeFiles/Makefile2:17646: Applications/MyAppApp/CMakeFiles/MyAppApp.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....
...
</code></pre>
<p>I found the definition in <code>Slicer-build/vtkSlicerVersionConfigure.h</code> but no include directives in header files included directly or indirectly by Main.cxx.</p>
<p>As the last change of the Main.cxx file in the template project is from July 2018, I’m quite puzzled and sure that I’m doing something wrong.</p>
<p>Can someone please point me into the right direction?</p>
<p>Thank you</p>
<p>Kambiz</p>

---

## Post #2 by @cpinter (2023-07-13 15:28 UTC)

<p>This could be related to the recent version macro refactoring. (Sorry I’m from phone now so will post link later)</p>

---

## Post #3 by @darabi (2023-07-13 15:48 UTC)

<p>Thanks to your hint, I found this commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/8c2143ee960e4f3221485c794e943adddbb20963">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/8c2143ee960e4f3221485c794e943adddbb20963" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/8c2143ee960e4f3221485c794e943adddbb20963" target="_blank" rel="noopener nofollow ugc">COMP: Explicitly include version header where associated macros are used</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-05-30" data-time="02:19:54" data-timezone="UTC">02:19AM - 30 May 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/achataigner" target="_blank" rel="noopener nofollow ugc">
          <img alt="achataigner" src="https://avatars.githubusercontent.com/u/3016648?v=4" class="onebox-avatar-inline" width="20" height="20">
          achataigner
        </a>
      </div>

      <div class="lines" title="changed 3 files with 3 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/8c2143ee960e4f3221485c794e943adddbb20963" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">List of files to update were identified using the following script:

```
# Extra<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/8c2143ee960e4f3221485c794e943adddbb20963" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ct macro specific to Slicer version headers
cat CMake/vtkSlicerVersionConfigure.h.in CMake/vtkSlicerVersionConfigureInternal.h.in  | ack "^#define Slicer" | cut -d" " -f2 &gt; /tmp/slicer-version-macros.txt

# Collect source files directly using at least one of the macro define in the version headers
(for macro in $(cat  /tmp/slicer-version-macros.txt); do
    ack $macro -l | ack "\.(cxx|cpp|h|h\.in|txx)$" | ack -v "vtkSlicerVersion";
done) | sort | uniq &gt; /tmp/slicer-file-using-version-macros.txt

# Are these files already including the version header ?
for file in $(cat /tmp/slicer-file-using-version-macros.txt);
do
  echo "$file";
  cat $file | ack  vtkSlicerVersionConfigure &gt; /dev/null &amp;&amp; echo "  yes" || echo "  no";
done
```

Co-authored-by: Andras Lasso &lt;lasso@queensu.ca&gt;
Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As <code>Applications/SlicerApp/Main.cxx</code> is modified in that commit to have</p>
<pre><code class="lang-auto">+#include "vtkSlicerVersionConfigure.h" // For Slicer_VERSION_FULL
</code></pre>
<p>I guess that the same change should be applied to <code> SlicerCustomAppTemplate/{{cookiecutter.project_name}}/Applications/{{cookiecutter.app_name}}App/Main.cxx</code>.</p>
<p>Shall I create a pull request?</p>
<p>Thanks for your help!</p>
<p>Kambiz</p>

---

## Post #4 by @jcfr (2023-07-13 16:37 UTC)

<p><a class="mention" href="/u/darabi">@darabi</a>  and <a class="mention" href="/u/cpinter">@cpinter</a>  Thanks for the investigative work <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/darabi">@darabi</a>  Could you review the following pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerCustomAppTemplate</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53" target="_blank" rel="noopener">COMP: Update Main.cxx to explicitly include configure headers for used macros</a>
      </h4>

    <div class="branches">
      <code>KitwareMedical:main</code> ← <code>jcfr:explicitly-include-vtkSlicerVersionConfigure-header</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-07-13" data-time="16:34:22" data-timezone="UTC">04:34PM - 13 Jul 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 2 additions and 0 deletions">
          <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53/files" target="_blank" rel="noopener">
            <span class="added">+2</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This fixes a regression introduced in 451194ac6 (COMP: Remove obsolete version h<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eader includes) and apply a fix similar to 8c2143ee9 (COMP: Explicitly include version header where associated macros are used)

See https://discourse.slicer.org/t/custom-app-compile-error-slicer-main-project-version-full-undefined/30577</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I also added <code>Co-authored-by: </code> commit message trailers<sup class="footnote-ref"><a href="#footnote-97661-1" id="footnote-ref-97661-1">[1]</a></sup> to provide relevant credits, that said look like I incorrectly referenced your GitHub account, would you mind follow-up on that as well.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-97661-1" class="footnote-item"><p><a href="https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors" class="inline-onebox">Creating a commit with multiple authors - GitHub Docs</a> <a href="#footnote-ref-97661-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @darabi (2023-07-13 19:53 UTC)

<p>LGTM, if you insist on including <code>vtkSlicerConfigure.h</code> (see comment)</p>

---

## Post #6 by @jcfr (2023-07-13 22:17 UTC)

<p>Thanks for the review <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Changes have now been integrated <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>For future reference, see <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/53">KitwareMedical/SlicerCustomAppTemplate#53</a></p>

---

## Post #7 by @darabi (2023-07-14 04:16 UTC)

<p>Many thanks for the quick reaction. Is there any CI process testing the SlicerCAT build? I don’t find anything at <a href="http://slicer.cdash.org" rel="noopener nofollow ugc">slicer.cdash.org</a> (but I don’t even know if I should expect anything there <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> ).</p>

---
