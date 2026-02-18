# Can you explain the CMake variables Slicer_<moduleType>MODULES_DISABLED|ENABLED?

**Topic ID**: 7494
**Date**: 2019-07-10
**URL**: https://discourse.slicer.org/t/can-you-explain-the-cmake-variables-slicer-moduletype-modules-disabled-enabled/7494

---

## Post #1 by @MattTroke (2019-07-10 12:12 UTC)

<p>Can you explain how Slicer_QTLOADABLEMODULES_ENABLED/Slicer_QTLOADABLEMODULES_DISABLED works? If the Slicer_QTLOADABLEMODULES_ENABLED list is empty, does it enable all modules excepting those in Slicer_QTLOADABLEMODULES_DISABLED? And if one or more modules are listed in Slicer_QTLOADABLEMODULES_ENABLED are all others disabled by default?</p>

---

## Post #2 by @jcfr (2019-07-10 12:39 UTC)

<p>Reading the documentation associated with the <code>SlicerCheckModuleEnabled</code> module should help.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/3e0ea48e078f2f0b9d501e2ada70d292e96d1de4/CMake/SlicerCheckModuleEnabled.cmake#L21-L62" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3e0ea48e078f2f0b9d501e2ada70d292e96d1de4/CMake/SlicerCheckModuleEnabled.cmake#L21-L62" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/3e0ea48e078f2f0b9d501e2ada70d292e96d1de4/CMake/SlicerCheckModuleEnabled.cmake#L21-L62</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="21" style="counter-reset: li-counter 20 ;">
<li>#</li>
<li># This CMake module provides functions allowing to check if a given Slicer built-in module</li>
<li># should be enabled or disabled.</li>
<li>#</li>
<li># Definitions:</li>
<li>#</li>
<li># * A Slicer built-in module is a module whose source code is found under one of the</li>
<li>#   "Slilcer/Modules/*" subdirectories. These do not include Slicer remote modules or</li>
<li>#   modules associated with bundled extensions.</li>
<li>#</li>
<li># * Enabling (or disabling) a module means that it will (or will not) be built.</li>
<li>#</li>
<li># * Building a module means that the corresponding directory is added using the add_subdirectory</li>
<li>#   CMake command and that the associated CMakeLists.txt is processed.</li>
<li>#</li>
<li># By default, all built-in Slicer modules are assumed to be enabled. Then, based on Slicer</li>
<li># build options, built-in module may be disabled.</li>
<li>#</li>
<li># Setting any of these variables allows to explicitly disable modules of the</li>
<li># corresponding module type ignoring effect of Slicer build options:</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/3e0ea48e078f2f0b9d501e2ada70d292e96d1de4/CMake/SlicerCheckModuleEnabled.cmake#L21-L62" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
