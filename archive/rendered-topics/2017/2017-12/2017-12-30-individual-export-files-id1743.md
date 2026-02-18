# Individual export files

**Topic ID**: 1743
**Date**: 2017-12-30
**URL**: https://discourse.slicer.org/t/individual-export-files/1743

---

## Post #1 by @ihnorton (2017-12-30 02:21 UTC)

<p>I was wondering about the export header files created for targets built by the <code>SlicerMacroBuild*</code> suite of cmake scripts. Is there a reason for all of these to be separate and configured?</p>
<pre><code class="lang-auto">Slicer-build$ find ./ -name *Export.h | wc -l
119
</code></pre>
<p>Some are unique or custom, but the significant majority are templated from <code>CMake/qSlicerExport.h.in</code>, or a slightly-different template from CTK for plugins.</p>
<p>I took a quick look through them:</p>
<pre><code class="lang-auto">$ cat `find ./ -name *Export.h | grep -v Plugin` | less
</code></pre>
<p>They all look identical – except for the actual name, of course – so they could potentially be replaced with a single <code>slicer_export.h</code> which defines <code>Slicer_EXPORT</code>.</p>

---

## Post #2 by @lassoan (2017-12-30 03:19 UTC)

<p>I think the current implementation is necessary if we want to allow building a module that depends on another module.</p>
<p>Example: Module A depends on module B. When you build module A, symbols of module A must be exported (using <code>__declspec(dllexport)</code>), while symbols of module B must be imported (using <code>__declspec(dllimport)</code>). If you used a single <code>Slicer_EXPORT</code> then both module symbols would be imported or both would be exported.</p>
<p>Do you have a specific idea how the current implementation could be simplified?</p>

---

## Post #3 by @ihnorton (2017-12-30 17:36 UTC)

<p>I forgot that CMake is automatically adding <code>-D{LIBNAME}_EXPORTS</code> at compile time to do the switch. Thanks, it makes more sense.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have a specific idea how the current implementation could be simplified?</p>
</blockquote>
</aside>
<p>In light of above, I agree this is nice and simple. We could probably make a single-header version with <code>-DLIBNAME=NAME</code> and some preprocessor substitution, but that just adds a different kind of magic, and this is overall a small point. So not worth the effort/churn.</p>

---

## Post #4 by @lassoan (2017-12-30 22:12 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="3" data-topic="1743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>CMake is automatically adding -D{LIBNAME}_EXPORTS at compile time</p>
</blockquote>
</aside>
<p>We’ve discussed this a bit more with <a class="mention" href="/u/ihnorton">@ihnorton</a>.</p>
<p>Here is how CMake adds the compiler definition when it generates the target:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Kitware/CMake/blob/258e6f1b1e1d20bc48a5892f5d9d339269fa2704/Source/cmGeneratorTarget.cxx#L1685">
  <header class="source">

      <a href="https://github.com/Kitware/CMake/blob/258e6f1b1e1d20bc48a5892f5d9d339269fa2704/Source/cmGeneratorTarget.cxx#L1685" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/CMake/blob/258e6f1b1e1d20bc48a5892f5d9d339269fa2704/Source/cmGeneratorTarget.cxx#L1685" target="_blank" rel="noopener">Kitware/CMake/blob/258e6f1b1e1d20bc48a5892f5d9d339269fa2704/Source/cmGeneratorTarget.cxx#L1685</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1675" style="counter-reset: li-counter 1674 ;">
          <li>const char* cmGeneratorTarget::GetExportMacro() const</li>
          <li>{</li>
          <li>  // Define the symbol for targets that export symbols.</li>
          <li>  if (this-&gt;GetType() == cmStateEnums::SHARED_LIBRARY ||</li>
          <li>      this-&gt;GetType() == cmStateEnums::MODULE_LIBRARY ||</li>
          <li>      this-&gt;IsExecutableWithExports()) {</li>
          <li>    if (const char* custom_export_name = this-&gt;GetProperty("DEFINE_SYMBOL")) {</li>
          <li>      this-&gt;ExportMacro = custom_export_name;</li>
          <li>    } else {</li>
          <li>      std::string in = this-&gt;GetName();</li>
          <li class="selected">      in += "_EXPORTS";</li>
          <li>      this-&gt;ExportMacro = cmSystemTools::MakeCidentifier(in);</li>
          <li>    }</li>
          <li>    return this-&gt;ExportMacro.c_str();</li>
          <li>  }</li>
          <li>  return nullptr;</li>
          <li>}</li>
          <li></li>
          <li>class cmTargetCollectLinkLanguages</li>
          <li>{</li>
          <li>public:</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The same mechanism is implemented in Visual Studio IDE, so very similar macros are used when projects are created without CMake: “By default, the New Project template for a DLL adds PROJECTNAME_EXPORTS to the defined preprocessor symbols for the DLL project.” (<a href="https://msdn.microsoft.com/en-us/library/ms235636.aspx">source</a>).</p>

---
