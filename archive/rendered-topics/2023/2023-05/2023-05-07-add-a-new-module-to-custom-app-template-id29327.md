# Add a new module to custom app template

**Topic ID**: 29327
**Date**: 2023-05-07
**URL**: https://discourse.slicer.org/t/add-a-new-module-to-custom-app-template/29327

---

## Post #1 by @Anjalimukundan (2023-05-07 12:29 UTC)

<p>Hello everyone ,<br>
I have downloaded source code for slicer custom app template and have build it. Now, how can I add my own module into the application.</p>

---

## Post #2 by @Sam_Horvath (2023-05-08 14:39 UTC)

<p>If you already have the code/framework for the new module, you can skip the next paragraph.</p>
<p>If you do not have the code for the module already, you can create the framework for a module using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html">Extension Wizard</a>  within 3D Slicer (it usually isn’t enabled in custom app builds, so you will want to use a downloaded 3D Slicer).  You create a temporary extension, and then a module of the desired type within it.</p>
<p>Once you have generated the module, you copy the folder of <em>just</em> the module into the custom app source (see example location below) and add it to the CMakeLists of the custom app (see below).</p>
<p>Location of folder in Repo:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/KitwareMedical/SlicerCAT/tree/main/Modules/Scripted/Example">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerCAT/tree/main/Modules/Scripted/Example" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/KitwareMedical/SlicerCAT/tree/main/Modules/Scripted/Example" target="_blank" rel="noopener">SlicerCAT/Modules/Scripted/Example at main · KitwareMedical/SlicerCAT</a></h3>

  <p><a href="https://github.com/KitwareMedical/SlicerCAT/tree/main/Modules/Scripted/Example" target="_blank" rel="noopener">main/Modules/Scripted/Example</a></p>

  <p><span class="label1">Example Application for Slicer Customization - Generated from KitwareMedical/SlicerCustomAppTemplate</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Example of where to add in the CMake: <a href="https://github.com/KitwareMedical/SlicerCAT/blob/e651f197f56e3378ce094378dd29631c08b25a33/CMakeLists.txt#L129" class="inline-onebox">SlicerCAT/CMakeLists.txt at e651f197f56e3378ce094378dd29631c08b25a33 · KitwareMedical/SlicerCAT · GitHub</a></p>

---

## Post #3 by @Anjalimukundan (2023-05-14 12:25 UTC)

<p>Thanks a lot , I was able to add a module successfully.</p>

---

## Post #4 by @software (2025-03-08 21:03 UTC)

<p>Could you tell me? I am facing a similar issue. I have created the same custom 3D Slicer template by following SlicerCAT and then built it using CMake.</p>
<p>Now, I want to add modules. Where should I add them, and how? After adding them, how do I build the project to see the changes?</p>
<p>Also, how do I open the project folder to make changes—in VS Code or Visual Studio?</p>

---
