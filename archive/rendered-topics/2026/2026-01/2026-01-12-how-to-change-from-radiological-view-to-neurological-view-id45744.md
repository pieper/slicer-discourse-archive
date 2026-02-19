---
topic_id: 45744
title: "How To Change From Radiological View To Neurological View"
date: 2026-01-12
url: https://discourse.slicer.org/t/45744
---

# How to change from Radiological view to Neurological view?

**Topic ID**: 45744
**Date**: 2026-01-12
**URL**: https://discourse.slicer.org/t/how-to-change-from-radiological-view-to-neurological-view/45744

---

## Post #1 by @Suhaim (2026-01-12 05:11 UTC)

<p>Hi,<br>
I have built Slicer and wanted to change the view orientation of the application’s slices. I did what was said <a href="https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883/8">here</a>, where the .ini config file is modified. This is the relevant part of my .config file :-</p>
<pre><code class="lang-auto">[DefaultSliceView]

Orientation=PatientRightIsScreenRight
</code></pre>
<p>My application is still in radiological convention and I don’t know why. The only other things I am doing programatically is modifying the layout to be in the “FourUpView“, “ThreeOverThreeView“ and jumping slices to certain points in space. I don’t know if there is something else I might be doing which could be resetting the view orientation to the radiological convention. Any ideas or suggestions would be really helpful.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2026-01-12 17:19 UTC)

<p>Make sure you modify the correct .ini file. You can get the path by typing this into the Python console:</p>
<pre><code>slicer.app.userSettings().fileName()
</code></pre>
<p>You can confirm that you modified the file correctly by going to the menu → Edit / Application Settings / Views section and check “View orientation” option.</p>

---

## Post #3 by @Suhaim (2026-01-13 04:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="45744">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can confirm that you modified the file correctly by going to the menu → Edit / Application Settings / Views section and check “View orientation” option.</p>
</blockquote>
</aside>
<p>I have checked, and the modification of the option has been made. The “View orientation” option has the value “patient right is screen right”. Yet the slice view is coming with the “patient right is screen left” behaviour.</p>
<p>Would you have any suggestions on what might be something I am doing that could cause such behaviour?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2026-01-13 05:51 UTC)

<p>Is the behavior the same if you use the Slicer Stable Release (5.10) and you load MRHead sample data?</p>

---

## Post #5 by @Suhaim (2026-01-13 06:40 UTC)

<p>I have built Slicer from source on a <a href="https://github.com/search?q=repo%3ASlicer%2FSlicer+7755c94b3432a98e83892ee4625f17b3af6bf56c&amp;type=commits" rel="noopener nofollow ugc">version</a> a few commits ahead of 5.10 using <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a>. Because I used the template(as it fetches the latest commit), I am on this version. I used the MRHead sample data on this built version, and the same behaviour is seen.</p>
<p>The pre-built, packaged slicer binary(5.10) is working properly on my machine. The pre-built application shifts to Neurological convention when I am modifying the “View orientation“ option or the appropriate .ini file.</p>
<p>I suspect that something I might be doing programmatically is unintentionally causing this. Would you have any suggestions on what I might be doing that is flipping the view?</p>

---

## Post #6 by @lassoan (2026-01-13 12:43 UTC)

<p>Probably in your custom application you disabled the ViewControllers module, which initializes the orientation presets based on the application settings:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7463d00422104eddd734c8ec0135c3b665345f8f/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L218">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7463d00422104eddd734c8ec0135c3b665345f8f/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L218" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7463d00422104eddd734c8ec0135c3b665345f8f/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L218" target="_blank" rel="noopener">Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/7463d00422104eddd734c8ec0135c3b665345f8f/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L218" rel="noopener"><code>7463d0042</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="208" style="counter-reset: li-counter 207 ;">
          <li>  settings.setValue("UseDepthPeeling", bool(defaultViewNode-&gt;GetUseDepthPeeling()));</li>
          <li>  settings.setValue("ShadowsVisibility", defaultViewNode-&gt;GetShadowsVisibility());</li>
          <li>  settings.setValue("AmbientShadowsSizeScale", defaultViewNode-&gt;GetAmbientShadowsSizeScale());</li>
          <li>  settings.setValue("AmbientShadowsVolumeOpacityThreshold", defaultViewNode-&gt;GetAmbientShadowsVolumeOpacityThreshold());</li>
          <li>  settings.setValue("AmbientShadowsIntensityScale", defaultViewNode-&gt;GetAmbientShadowsIntensityScale());</li>
          <li>  settings.setValue("AmbientShadowsIntensityShift", defaultViewNode-&gt;GetAmbientShadowsIntensityShift());</li>
          <li>  writeCommonViewSettings(defaultViewNode, settings);</li>
          <li>}</li>
          <li></li>
          <li>//-----------------------------------------------------------------------------</li>
          <li class="selected">void qSlicerViewControllersModule::readDefaultSliceViewSettings(vtkMRMLSliceNode* defaultViewNode)</li>
          <li>{</li>
          <li>  if (!defaultViewNode)</li>
          <li>  {</li>
          <li>    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; " failed: defaultViewNode is invalid";</li>
          <li>    return;</li>
          <li>  }</li>
          <li>  QSettings settings;</li>
          <li>  settings.beginGroup("DefaultSliceView");</li>
          <li>  if (settings.contains("Orientation"))</li>
          <li>  {</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can enable this module or add the relevant lines to one of your modules.</p>

---

## Post #7 by @Suhaim (2026-01-14 04:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="45744">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ViewControllers</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thanks for directing me to the code snippet used to set the default slice orientation. I haven’t modified the view controller. Yet I used the same call in the code you directed me to, in my startup .slicerrc.py script :-</p>
<p><code>slicer.vtkMRMLSliceNode.AddDefaultSliceOrientationPresets(slicer.mrmlScene, False)</code></p>
<p>Thanks a lot for the support!</p>

---

## Post #8 by @lassoan (2026-01-14 05:23 UTC)

<p>In the Slicer Custom Application Template, <a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L114">ViewControllers module is disabled by default</a>, so you either need to initialize the view defaults yourself or enable the module.</p>
<p>I’ve submitted a pull request to not disable this module by default:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerCAT/pull/9">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCAT/pull/9" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerCAT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/KitwareMedical/SlicerCAT/pull/9" target="_blank" rel="noopener">ENH: Do not disable ViewControllers module</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:patch-1</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-14" data-time="05:28:16" data-timezone="UTC">05:28AM - 14 Jan 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 0 additions and 1 deletions">
          <a href="https://github.com/KitwareMedical/SlicerCAT/pull/9/files" target="_blank" rel="noopener">
            <span class="added">+0</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ViewControllers module is responsible for setting default view node properties f<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerCAT/pull/9" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rom application settings.

Developers may rely on this feature - see for example https://discourse.slicer.org/t/how-to-change-from-radiological-view-to-neurological-view/45744/8.

Therefore it is better not to disable this module in the template.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @Suhaim (2026-01-14 05:43 UTC)

<p>That makes sense, I only searched my source code and couldn’t find any ViewController code, I forgot to search the entire directory for the possible CMake configurations. I made the modification to the CMake file and was able to view it in neurological view without the startup code. Thanks a lot once again!<br>
Out of curiosity, I wanted to ask why you have submitted the PR on SlicerCAT and not on <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate#readme" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a>?</p>

---

## Post #10 by @lassoan (2026-01-14 14:18 UTC)

<aside class="quote no-group" data-username="Suhaim" data-post="9" data-topic="45744">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/suhaim/48/81421_2.png" class="avatar"> Suhaim:</div>
<blockquote>
<p>Out of curiosity, I wanted to ask why you have submitted the PR on SlicerCAT and not on <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate#readme">SlicerCustomAppTemplate</a>?</p>
</blockquote>
</aside>
<p>Good catch, that repository has to be updated, too. I’ve submitted a pull request.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/112">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/112" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerCustomAppTemplate</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/112" target="_blank" rel="noopener">ENH: Do not disable ViewControllers module</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:patch-2</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-14" data-time="14:17:03" data-timezone="UTC">02:17PM - 14 Jan 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 0 additions and 1 deletions">
          <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/112/files" target="_blank" rel="noopener">
            <span class="added">+0</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ViewControllers module is responsible for setting default view node properties f<span class="show-more-container"><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/pull/112" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rom application settings.

Developers may rely on this feature - see for example https://discourse.slicer.org/t/how-to-change-from-radiological-view-to-neurological-view/45744/8.

Therefore it is better not to disable this module in the template.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
