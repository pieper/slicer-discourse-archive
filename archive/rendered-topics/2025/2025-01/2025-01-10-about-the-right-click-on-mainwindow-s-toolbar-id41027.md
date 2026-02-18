# About the right click on mainwindow’s toolbar

**Topic ID**: 41027
**Date**: 2025-01-10
**URL**: https://discourse.slicer.org/t/about-the-right-click-on-mainwindow-s-toolbar/41027

---

## Post #1 by @nih4t (2025-01-10 13:07 UTC)

<p>Hi, how can I edit here?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db60a79c484d2ee12b3e09d88e92fb72d53a14c9.png" data-download-href="/uploads/short-url/viHEafMio6BeMo6GogV2rnNxO4x.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db60a79c484d2ee12b3e09d88e92fb72d53a14c9.png" alt="image" data-base62-sha1="viHEafMio6BeMo6GogV2rnNxO4x" width="406" height="293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">406×293 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-01-10 14:50 UTC)

<p>Can you be more specific please? What do you want to edit?</p>

---

## Post #3 by @nih4t (2025-01-10 14:53 UTC)

<p>I’m using SlicerCAT right now and I would like to modify the default checked options in this dropdown menu. Can you guide me on how to configure which items are selected by default when the application starts.</p>

---

## Post #4 by @cpinter (2025-01-10 15:28 UTC)

<p>You can do this for example:<br>
<code>slicer.util.mainWindow().findChildren('qMRMLCaptureToolBar')[0].visible = False</code></p>
<p>But there may be a better way to customize this.</p>

---

## Post #5 by @nih4t (2025-01-10 16:04 UTC)

<p>The code<br>
<code>slicer.util.mainWindow().findChildren('qMRMLCaptureToolBar')[0].visible = False</code><br>
works fine in 3D Slicer to hide the Capture/Restore Toolbar. However, in SlicerCAT, the setting doesn’t persist after restarting the application, and the toolbar reverts to its default visibility.</p>
<p>Do you know what the equivalent name is for the “Favorite Modules” in the code? For example, <code>qMRMLCaptureToolBar</code> is used for the Capture/Restore toolbar—what would it be for the Favorite Modules?</p>

---

## Post #6 by @Esteban_Barreiro (2025-01-11 13:51 UTC)

<p>Did you try drag and drop the module you want to the favorites tab in user preferences?</p>

---

## Post #7 by @nih4t (2025-01-11 14:11 UTC)

<p>I know how to add modules to Favorite Modules, so that’s not my question. I’m currently using SlicerCAT, and in SlicerCAT, the “Favorite Modules” section is not checked by default. I want to change this behavior. I have a few ideas to try, but I’m struggling to find the exact name used in the code to represent this section.</p>
<p>For instance, in the code, they used the name “qMRMLCaptureToolBar” to control the “Capture/Restore” functionality. Similarly, I’m looking for the name they used to represent the “Favorite Modules” section shown in the image below. Could anyone point me in the right direction?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb5daebb6b7ac32c75a5147c9fa7933f27ac323e.jpeg" data-download-href="/uploads/short-url/qJw03tTAsQLPhPAhBrPMpE3DByS.jpeg?dl=1" title="IMG_9856" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb5daebb6b7ac32c75a5147c9fa7933f27ac323e.jpeg" alt="IMG_9856" data-base62-sha1="qJw03tTAsQLPhPAhBrPMpE3DByS" width="406" height="293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_9856</span><span class="informations">406×293 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @jamesobutler (2025-01-11 17:53 UTC)

<p>As you begin your customization journey I would suggest reviewing the following technique:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>Which would lead you to do the following search in the Slicer repository:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/search?q=repo%3ASlicer%2FSlicer%20favorite%20modules&amp;type=code">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/search?q=repo%3ASlicer%2FSlicer%20favorite%20modules&amp;type=code" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img width="500" height="500" src="https://github.githubassets.com/assets/github-logo-55c5b9a1fe52.png" class="thumbnail onebox-avatar">

<h3><a href="https://github.com/search?q=repo%3ASlicer%2FSlicer%20favorite%20modules&amp;type=code" target="_blank" rel="noopener nofollow ugc">Build software better, together</a></h3>

  <p>GitHub is where people build software. More than 100 million people use GitHub to discover, fork, and contribute to over 420 million projects.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Which contains a result for the object name of the QToolBar for that has the display name of “Favorite Modules”.</p>

---

## Post #9 by @nih4t (2025-01-11 18:34 UTC)

<p>Hi, thanks for your response. I’ve already added my own modules and buttons to SlicerCAT, but I’m facing an issue. Even though I’ve found the name of the “Favorite Modules” toolbar, my initial solution didn’t work as expected, so I need some help.</p>
<p>Here’s the situation: I’ve successfully added my custom modules and their buttons, and I’ve also included some 3D Slicer modules to the “Favorite Modules” section. However, in SlicerCAT, “Favorite Modules” is invisible by default. I need to right-click and manually enable them. I’d like to change this default behavior so that the modules are visible by default.</p>
<p>Additionally, I want to disable right-click functionality on the main toolbar to prevent users from modifying the module visibility. This would allow me to hide unnecessary modules from the users.</p>
<p>For reference, here is the source code of SlicerCAT:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/KitwareMedical/SlicerCAT">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCAT" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/b3e9bd9a98d5e6893d4183f9b006945a/KitwareMedical/SlicerCAT" class="thumbnail">

  <h3><a href="https://github.com/KitwareMedical/SlicerCAT" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerCAT: Example Application for Slicer Customization -...</a></h3>

    <p><span class="github-repo-description">Example Application for Slicer Customization - Generated from KitwareMedical/SlicerCustomAppTemplate</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It seems that the file previously named <code>Example.py</code> is now called <code>Home.py</code>.</p>
<p>I’ve been struggling to implement these changes. Do you have any suggestions or guidance on how I can achieve this?</p>

---

## Post #10 by @jamesobutler (2025-01-11 20:07 UTC)

<p>Although you can look at SlicerCAT as an example, it is just a snapshot in time of what <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a> produced over 3 years ago. The Home.py is what SlicerCustomAppTemplate currently creates and has last customization examples.</p>
<p>In the below linked code you can customize which toolbars are set as visible on startup.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/Modules/Scripted/Home/Home.py#L96">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/Modules/Scripted/Home/Home.py#L96" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/Modules/Scripted/Home/Home.py#L96" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/{{cookiecutter.project_name}}/Modules/Scripted/Home/Home.py#L96</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="86" style="counter-reset: li-counter 85 ;">
          <li>        "ViewToolBar",</li>
          <li>        *self.toolbarNames,</li>
          <li>    ]</li>
          <li>    slicer.util.setDataProbeVisible(visible)</li>
          <li>    slicer.util.setMenuBarsVisible(visible, ignore=exemptToolbars)</li>
          <li>    slicer.util.setModuleHelpSectionVisible(visible)</li>
          <li>    slicer.util.setModulePanelTitleVisible(visible)</li>
          <li>    slicer.util.setPythonConsoleVisible(visible)</li>
          <li>    slicer.util.setApplicationLogoVisible(visible)</li>
          <li>    keepToolbars = [slicer.util.findChild(slicer.util.mainWindow(), toolbarName) for toolbarName in exemptToolbars]</li>
          <li class="selected">    slicer.util.setToolbarsVisible(visible, keepToolbars)</li>
          <li></li>
          <li>def modifyWindowUI(self):</li>
          <li>    """Customize the entire user interface to resemble the custom application"""</li>
          <li>    # Custom toolbars</li>
          <li>    self.initializeSettingsToolBar()</li>
          <li></li>
          <li>def insertToolBar(self, beforeToolBarName: str, name: str, title: Optional[str] = None) -&gt; qt.QToolBar:</li>
          <li>    """Helper method to insert a new toolbar between existing ones"""</li>
          <li>    beforeToolBar = slicer.util.findChild(slicer.util.mainWindow(), beforeToolBarName)</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="nih4t" data-post="9" data-topic="41027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nih4t/48/78310_2.png" class="avatar"> nih4t:</div>
<blockquote>
<p>Additionally, I want to disable right-click functionality on the main toolbar to prevent users from modifying the module visibility.</p>
</blockquote>
</aside>
<p>^Regarding this type of customization it is something I’ve never done before. Editing toolbar visibility through right-click is standard Qt behavior. Since this would be standard Qt type customization not unique to Slicer you may be able to search on various Qt forums about how to accomplish this task.</p>
<aside class="quote no-group" data-username="nih4t" data-post="9" data-topic="41027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nih4t/48/78310_2.png" class="avatar"> nih4t:</div>
<blockquote>
<p>This would allow me to hide unnecessary modules from the users.</p>
</blockquote>
</aside>
<p>If there are modules that you don’t need at all, you can modify your Slicer custom application to not include the modules in the first place rather than worrying about trying to hide them. This can be customized at:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L121">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L121" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L121" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerCustomAppTemplate/blob/5a783789781f3c86615d35c41a9db5ac8ade34b1/{{cookiecutter.project_name}}/CMakeLists.txt#L121</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="111" style="counter-reset: li-counter 110 ;">
          <li># Enable Slicer built-in modules</li>
          <li>set(Slicer_CLIMODULES_ENABLED</li>
          <li>  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume</li>
          <li>  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume</li>
          <li>  )</li>
          <li>set(Slicer_QTLOADABLEMODULES_ENABLED</li>
          <li>  )</li>
          <li>set(Slicer_QTSCRIPTEDMODULES_ENABLED</li>
          <li>  )</li>
          <li></li>
          <li class="selected"># Disable Slicer built-in modules</li>
          <li>set(Slicer_CLIMODULES_DISABLED</li>
          <li>  )</li>
          <li>set(Slicer_QTLOADABLEMODULES_DISABLED</li>
          <li>  SceneViews</li>
          <li>  SlicerWelcome</li>
          <li>  ViewControllers</li>
          <li>  )</li>
          <li>set(Slicer_QTSCRIPTEDMODULES_DISABLED</li>
          <li>  DataProbe</li>
          <li>  DMRIInstall</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @nih4t (2025-01-12 13:25 UTC)

<p>Thanks for your response. I actually tried this earlier when you shared the object name for “Favorite Modules.” I believe it’s <code>"ModuleToolBar"</code>. However, I tried it, and it didn’t work as expected. Here’s the code I used:</p>
<pre><code class="lang-auto">def setSlicerUIVisible(self, visible: bool):
    exemptToolbars = [
        "MainToolBar",
        "ViewToolBar",
        "ModuleToolBar",
        *self.toolbarNames,
    ]

    slicer.util.setDataProbeVisible(visible)
    slicer.util.setMenuBarsVisible(visible, ignore=exemptToolbars)
    slicer.util.setModuleHelpSectionVisible(visible)
    slicer.util.setModulePanelTitleVisible(visible)
    slicer.util.setPythonConsoleVisible(visible)
    slicer.util.setApplicationLogoVisible(visible)
    keepToolbars = [
        slicer.util.findChild(slicer.util.mainWindow(), toolbarName) 
        for toolbarName in exemptToolbars
    ]
    slicer.util.setToolbarsVisible(visible, keepToolbars)

</code></pre>
<p>For the <code>CMakeLists.txt</code>, you can see that almost everything is currently disabled. I always thought that we could manage the modules already listed in this file and toggle them between enabled or disabled. My question is: if I add an object name here, will it automatically disable the corresponding module? If that’s the case, I’ll need to identify the object name for every module I want to manage.</p>
<p>Here’s the current configuration of my <code>CMakeLists.txt</code> file:</p>
<pre><code class="lang-auto"># Enable Slicer built-in modules
set(Slicer_CLIMODULES_ENABLED
  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume
  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume
)

set(Slicer_QTLOADABLEMODULES_ENABLED
)

set(Slicer_QTSCRIPTEDMODULES_ENABLED
)

# Disable Slicer built-in modules
set(Slicer_CLIMODULES_DISABLED
)

set(Slicer_QTLOADABLEMODULES_DISABLED
  SceneViews
  SlicerWelcome
  ViewControllers
)

set(Slicer_QTSCRIPTEDMODULES_DISABLED
  DataProbe
  DMRIInstall
  Endoscopy
  LabelStatistics
  PerformanceTests
  SampleData
  VectorToScalarVolume
)
</code></pre>
<p>I’ll include two images below to show you the current version of my configuration and the target version I aim to achieve.</p>
<p>The version that I have right now looks like this. You can riğht click and enable what you want.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c7b88f6e5596ffadbc14ca8797e25192d4218ee.png" data-download-href="/uploads/short-url/dc8BbLxNHgSAYBgVxozWnn2qdv8.png?dl=1" title="Ekran görüntüsü 2025-01-12 132405" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c7b88f6e5596ffadbc14ca8797e25192d4218ee_2_690x365.png" alt="Ekran görüntüsü 2025-01-12 132405" data-base62-sha1="dc8BbLxNHgSAYBgVxozWnn2qdv8" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c7b88f6e5596ffadbc14ca8797e25192d4218ee_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c7b88f6e5596ffadbc14ca8797e25192d4218ee_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c7b88f6e5596ffadbc14ca8797e25192d4218ee_2_1380x730.png 2x" data-dominant-color="5E5E65"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2025-01-12 132405</span><span class="informations">1599×848 26.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this is the version that I want to achive, just these modules enabled (They are currently in Favorite Modules) and I don’t want any other thing. I want to start slicer and see this screen. And I don’t need any other functionality.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f837379d5fe2a89bbbefd2b8a266be8d6ef87f2f.png" data-download-href="/uploads/short-url/zpOIkK0twS63BFCaRgS20F0nSxN.png?dl=1" title="Ekran görüntüsü 2025-01-12 132449" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f837379d5fe2a89bbbefd2b8a266be8d6ef87f2f_2_690x365.png" alt="Ekran görüntüsü 2025-01-12 132449" data-base62-sha1="zpOIkK0twS63BFCaRgS20F0nSxN" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f837379d5fe2a89bbbefd2b8a266be8d6ef87f2f_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f837379d5fe2a89bbbefd2b8a266be8d6ef87f2f_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f837379d5fe2a89bbbefd2b8a266be8d6ef87f2f_2_1380x730.png 2x" data-dominant-color="5E5E65"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2025-01-12 132449</span><span class="informations">1599×848 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @jamesobutler (2025-01-12 14:02 UTC)

<aside class="quote no-group" data-username="nih4t" data-post="11" data-topic="41027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nih4t/48/78310_2.png" class="avatar"> nih4t:</div>
<blockquote>
<p>However, I tried it, and it didn’t work as expected. Here’s the code I used:</p>
</blockquote>
</aside>
<p>Have you confirmed that any edits to the Home.py are working? Have you tried a print statement of some sort to see if it gets executed. There may be a Home.pyc file which I believe you will need to delete first as that is the compiled version that is ultimately run. If no pyc version is present it goes back to using the py version of the file.</p>
<aside class="quote no-group" data-username="nih4t" data-post="11" data-topic="41027">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nih4t/48/78310_2.png" class="avatar"> nih4t:</div>
<blockquote>
<p>My question is: if I add an object name here, will it automatically disable the corresponding module?</p>
</blockquote>
</aside>
<p>If you add a module to the disabled list I would expect that you would first new to delete the module contents that were copied into the Slicer build tree and then run the incremental build of Slicer again. I don’t believe the build process will remove module files already copied into the Slicer-build area. For sure if you run a completely new build of the application would it respect the updated module disabled list. Modifying the CMakeLists.txt and running the application without re-running the build won’t do anything.</p>

---
