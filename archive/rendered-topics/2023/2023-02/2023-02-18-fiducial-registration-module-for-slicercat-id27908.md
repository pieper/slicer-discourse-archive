# Fiducial registration module for SlicerCAT

**Topic ID**: 27908
**Date**: 2023-02-18
**URL**: https://discourse.slicer.org/t/fiducial-registration-module-for-slicercat/27908

---

## Post #1 by @Kaubert (2023-02-18 16:23 UTC)

<p>Hi there,</p>
<p>I’m looking for the source code of the module “<a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/fiducialregistration.html" rel="noopener nofollow ugc">Fiducial registration</a>” in order to include it in a SlicerCAT build.</p>
<p>I know that the module “Fiducial Registration Wizard” from IGT extension is very similar but I would like to use a custom module on SlicerCAT which call the module “Fiducial registration”.</p>
<p>If anyone could help me to find the source code or help me to build SlicerCAT with “Fiducial registration” it would be very appreciated.</p>
<p>Thank you,</p>

---

## Post #2 by @jcfr (2023-02-22 06:03 UTC)

<blockquote>
<p>looking for the source code of the module <code>FiducialRegistration</code></p>
</blockquote>
<p>See <a href="https://github.com/Slicer/Slicer/tree/main/Modules/CLI/FiducialRegistration">https://github.com/Slicer/Slicer/tree/main/Modules/CLI/FiducialRegistration</a></p>
<p>By default, the module is expected to be built in your Slicer custom application.</p>

---

## Post #3 by @Sam_Horvath (2023-02-22 22:05 UTC)

<p>Make sure that it is the list of enabled CLIs in the template:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/05e842938f1e9c15f53a13b454efa124958aede6/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L113">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/05e842938f1e9c15f53a13b454efa124958aede6/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L113" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/05e842938f1e9c15f53a13b454efa124958aede6/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L113" target="_blank" rel="noopener">KitwareMedical/SlicerCustomAppTemplate/blob/05e842938f1e9c15f53a13b454efa124958aede6/{{cookiecutter.project_name}}/CMakeLists.txt#L113</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="103" style="counter-reset: li-counter 102 ;">
          <li>option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)</li>
          <li>option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            OFF)</li>
          <li>
          </li>
<li>option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)</li>
          <li>option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)</li>
          <li>option(Slicer_BUILD_CompareVolumes              "Build application with ChangeTrackerPy module"       OFF)</li>
          <li>option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)</li>
          <li>option(Slicer_BUILD_SurfaceToolbox              "Build application with SurfaceToolbox module"        OFF)</li>
          <li>
          </li>
<li># Enable Slicer built-in modules</li>
          <li class="selected">set(Slicer_CLIMODULES_ENABLED</li>
          <li>  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume</li>
          <li>  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume</li>
          <li>  )</li>
          <li>set(Slicer_QTLOADABLEMODULES_ENABLED</li>
          <li>  )</li>
          <li>set(Slicer_QTSCRIPTEDMODULES_ENABLED</li>
          <li>  )</li>
          <li>
          </li>
<li># Disable Slicer built-in modules</li>
          <li>set(Slicer_CLIMODULES_DISABLED</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Kaubert (2023-02-23 16:01 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, for your answers.<br>
I had not thought of using this solution at all.</p>
<p>Everything is working properly now.</p>
<p>Thanks !</p>

---
