# Custom module icons in SlicerCustomAppTemplateApp missing

**Topic ID**: 34037
**Date**: 2024-01-30
**URL**: https://discourse.slicer.org/t/custom-module-icons-in-slicercustomapptemplateapp-missing/34037

---

## Post #1 by @apparrilla (2024-01-30 06:24 UTC)

<p>I´ve build a SlicerCustomAppTemplateApp with a custom module in Win11.</p>
<p>In Resouces/Icon folder there are many other icons.</p>
<p>I set Slicer_EXTENSION_SOURCE_DIRS    ${SlicerCustomAppTemplate_SOURCE_DIR}/Modules/Scripted/MyCustomModule<br>
but only the main icon was added to the project folder.</p>
<p>Is there any other way to add extra resources to SlicerCustomAppTemplateApp?</p>
<p>Thanks on advance!</p>

---

## Post #2 by @jamesobutler (2024-01-30 15:00 UTC)

<p>The CMakeLists.txt for your given scripted loadable module is where you can define python resources to include in the package.</p>
<p>See for example how the Screen Capture module specifies to include the module icon and another image file for use by the module:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/88d9aab666f48ced72e4696cb1bb1a998f5da040/Modules/Scripted/ScreenCapture/CMakeLists.txt#L9-L12">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/88d9aab666f48ced72e4696cb1bb1a998f5da040/Modules/Scripted/ScreenCapture/CMakeLists.txt#L9-L12" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/88d9aab666f48ced72e4696cb1bb1a998f5da040/Modules/Scripted/ScreenCapture/CMakeLists.txt#L9-L12" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/88d9aab666f48ced72e4696cb1bb1a998f5da040/Modules/Scripted/ScreenCapture/CMakeLists.txt#L9-L12</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
          <li>set(MODULE_PYTHON_RESOURCES</li>
          <li>  Resources/Icons/${MODULE_NAME}.png</li>
          <li>  Resources/SlicerWatermark.png</li>
          <li>  )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @apparrilla (2024-01-30 21:25 UTC)

<p>I need to improve my Cmake skills…<br>
Thank you James!!!</p>

---
