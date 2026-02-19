---
topic_id: 34093
title: "Is It Possible To Change To Dark Mode Style By Code"
date: 2024-02-01
url: https://discourse.slicer.org/t/34093
---

# Is it possible to change to Dark Mode Style by code?

**Topic ID**: 34093
**Date**: 2024-02-01
**URL**: https://discourse.slicer.org/t/is-it-possible-to-change-to-dark-mode-style-by-code/34093

---

## Post #1 by @apparrilla (2024-02-01 13:22 UTC)

<p>I want to put my SlicerCustomApp in Dark Mode by default.<br>
I´m looking for it in the forum and in API but I can´t get it…<br>
What is the CmakeList parameter to add? Should be possible to add it to a module instead?<br>
Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2024-02-01 18:57 UTC)

<p>You can define default settings for existing Slicer settings in your custom application’s settings file:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/a53f0c58dc94a5dab38e87afd35759d1780b6c3c/%7B%7Bcookiecutter.project_name%7D%7D/Applications/%7B%7Bcookiecutter.app_name%7D%7DApp/Resources/Settings/DefaultSettings.ini">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/a53f0c58dc94a5dab38e87afd35759d1780b6c3c/%7B%7Bcookiecutter.project_name%7D%7D/Applications/%7B%7Bcookiecutter.app_name%7D%7DApp/Resources/Settings/DefaultSettings.ini" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/a53f0c58dc94a5dab38e87afd35759d1780b6c3c/%7B%7Bcookiecutter.project_name%7D%7D/Applications/%7B%7Bcookiecutter.app_name%7D%7DApp/Resources/Settings/DefaultSettings.ini" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerCustomAppTemplate/blob/a53f0c58dc94a5dab38e87afd35759d1780b6c3c/{{cookiecutter.project_name}}/Applications/{{cookiecutter.app_name}}App/Resources/Settings/DefaultSettings.ini</a></h4>


      <pre><code class="lang-ini">[General]

[ApplicationUpdate]
ServerUrl=

[MainWindow]
DontConfirmExit=1024
DontConfirmRestart=1024
DontShowDisclaimerMessage=1024
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If I open Slicer go to Edit-&gt;Application Settings-&gt;Appearance-&gt;Style and change it from “Slicer” to “Dark Slicer” you will then notice in the user settings file (%AppData%\slicer.org\SonoEQ.ini), that it will have something like the following section:</p>
<pre><code class="lang-auto">[Styles]
AdditionalPaths=@Invalid()
Style=Dark Slicer
</code></pre>
<p>If you add the same entry into your custom application’s DefaultSettings.ini, that should define it as the new default.</p>

---

## Post #3 by @apparrilla (2024-02-02 07:05 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>.</p>
<p>I´ve compile CustomSlicer over the night with this change in DefaultSettings.ini but I´m still doing something wrong.</p>
<p>MyCustomSlicer.ini is located in:</p>
<blockquote>
<p>C:\USERS\USER\AppData\Roaming\MyCustomCompanuy(I changed Kitware)\MyCustomSlicer.ini</p>
</blockquote>
<p>For my surprise,</p>
<blockquote>
<p>[Styles]<br>
AdditionalPaths=@Invalid()<br>
Style=Slicer</p>
</blockquote>
<p>Is there any other config parameter I miss?<br>
Thank´s</p>

---

## Post #4 by @apparrilla (2024-02-02 07:23 UTC)

<p>Try to forgive me…<br>
As MyCustomSlicer was previosly compiled, I have to delete the existing MyCustomSlicer.ini… My mistake.<br>
I leave the comment to prevent other users not to have same trouble,</p>
<p>Thanks again…</p>

---
