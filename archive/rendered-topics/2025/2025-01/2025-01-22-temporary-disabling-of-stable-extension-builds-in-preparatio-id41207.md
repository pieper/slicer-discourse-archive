# Temporary disabling of Stable extension builds in preparation for Slicer 5.8 Release & Visual Studio update

**Topic ID**: 41207
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/temporary-disabling-of-stable-extension-builds-in-preparation-for-slicer-5-8-release-visual-studio-update/41207

---

## Post #1 by @jcfr (2025-01-22 03:55 UTC)

<p>As discussed in the <a href="https://discourse.slicer.org/t/2025-01-25-weekly-meeting/41174/3">2025-01-25 Weekly Meeting</a>, the builds of Slicer <strong>Stable</strong> extensions will be temporarily disabled this evening.</p>
<p>This step is necessary to facilitate updating the version of Visual Studio installed on the Windows factory (<code>bluestreak</code>). Once the Slicer 5.8 release is completed, this update will ensure that both <strong>Stable</strong> and <strong>Preview</strong> extensions are built using the same compiler, improving consistency across builds.</p>
<h3><a name="p-121556-next-steps-1" class="anchor" href="#p-121556-next-steps-1" aria-label="Heading link"></a><strong>Next Steps:</strong></h3>
<ol>
<li>Pause the build of Stable extensions (happening this evening).</li>
<li>Update Visual Studio on the Windows factory.</li>
<li>Wait for the January 21st preview build to complete.</li>
<li>Begin the release process for Slicer 5.8 on January 22nd.</li>
</ol>
<p>We appreciate your patience and support during this process <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @RafaelPalomar (2025-01-22 05:54 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, thanks for informing. This is an important update.</p>
<p>Have there been any changes in the Linux build factory lately? I observe that the extension catalog is empty for the Linux preview since <code>r33182</code> (<a href="https://extensions.slicer.org/catalog/All/33182/" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/33182/</a>)</p>

---

## Post #3 by @muratmaga (2025-01-22 06:27 UTC)

<p>I think there was about a week where there was no Linux build (and extension). It should be working now:</p>
<p><a href="https://extensions.slicer.org/catalog/All/33198/linux" class="onebox" target="_blank" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/33198/linux</a></p>

---

## Post #4 by @RafaelPalomar (2025-01-22 08:15 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>. You are right, this was only for a short window of time. Now it is working.</p>

---

## Post #5 by @jcfr (2025-01-22 09:18 UTC)

<h3><a name="p-121570-visual-studio-updated-from-1796-to-17124-1" class="anchor" href="#p-121570-visual-studio-updated-from-1796-to-17124-1" aria-label="Heading link"></a>Visual Studio updated from <code>17.9.6</code> to <code>17.12.4</code></h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0c9b287748e71c240a2bb259913f4cc0d30301a.png" data-download-href="/uploads/short-url/mWowQZobVKmcOOQNji7KxyownGi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0c9b287748e71c240a2bb259913f4cc0d30301a.png" alt="image" data-base62-sha1="mWowQZobVKmcOOQNji7KxyownGi" width="513" height="375" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">736×538 13.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-121570-msvc-compiler-version-2" class="anchor" href="#p-121570-msvc-compiler-version-2" aria-label="Heading link"></a>MSVC Compiler Version</h3>
<p>Before:</p>
<pre><code class="lang-auto">[...]
-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19045.
-- The C compiler identification is MSVC 19.39.33523.0
-- The CXX compiler identification is MSVC 19.39.33523.0
[...]
</code></pre>
<p>After:</p>
<pre><code class="lang-auto">[...]
-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19045.
-- The C compiler identification is MSVC 19.42.34436.0
-- The CXX compiler identification is MSVC 19.42.34436.0
[...]
</code></pre>
<h3><a name="p-121570-preview-build-manually-triggered-3" class="anchor" href="#p-121570-preview-build-manually-triggered-3" aria-label="Heading link"></a>Preview build manually triggered</h3>
<p>To check that latest version of <code>main</code> build as expected (<a href="https://github.com/Slicer/Slicer/commit/87d3a309e7e9c48e32dba94894adcc58b377f1f3">Slicer@87d3a309e</a>), the build was manually triggered on the three platform based on <a href="https://github.com/Slicer/DashboardScripts/blob/main/maintenance/guides/re-trigger-nightly-build.md">these instructions</a>.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d064cd2ef14ef589bd7d8ea34a2237e72eae1222.png" data-download-href="/uploads/short-url/tJxhmzx7A7UhjpXJ20TKDr5C0ro.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d064cd2ef14ef589bd7d8ea34a2237e72eae1222_2_690x75.png" alt="image" data-base62-sha1="tJxhmzx7A7UhjpXJ20TKDr5C0ro" width="690" height="75" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d064cd2ef14ef589bd7d8ea34a2237e72eae1222_2_690x75.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d064cd2ef14ef589bd7d8ea34a2237e72eae1222_2_1035x112.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d064cd2ef14ef589bd7d8ea34a2237e72eae1222_2_1380x150.png 2x" data-dominant-color="CBD2DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1950×214 32.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td>See <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-22">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-22</a></td>
</tr>
</tbody>
</table>
</div>

---

## Post #6 by @jcfr (2025-01-23 11:06 UTC)

<p>Updates:</p>
<ul>
<li>The update of MSVC compiler worked as expected. See details in  issue <a href="https://github.com/Slicer/Slicer/issues/7737#issuecomment-2606702891">#7737</a></li>
<li>Fixes related to <code>SampleData</code> have been integrated to fix tests. See <a href="https://github.com/Slicer/Slicer/pull/8162">PR#8162</a>, <a href="https://github.com/Slicer/Slicer/pull/8163">PR#8163</a> and <a href="https://github.com/Slicer/Slicer/pull/8164">PR#8164</a></li>
</ul>

---

## Post #7 by @jcfr (2025-01-23 11:26 UTC)

<p><strong>Update</strong>:</p>
<p>We’ve identified the root cause of the crash occurring after installing binary Python wheels (e.g., ITK wheels). The issue stems from recent wheels being built with the newer <code>std::string</code> ABI, while the official Slicer and Python binaries target the <em>older</em> ABI. This mismatch leads to compatibility issues.</p>
<p>To learn more about the Dual ABI, refer to <a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html">GCC’s Dual ABI Documentation</a>.</p>
<h3><a name="p-121638-proposed-solution-1" class="anchor" href="#p-121638-proposed-solution-1" aria-label="Heading link"></a>Proposed Solution</h3>
<p>To resolve this, we plan to introduce an option that packages a <code>_manylinux.py</code> module specific to the build environment. This module will restrict the latest compatible version of GLIBC, ensuring compatibility with the host system.</p>
<p>For example, adding the following <code>_manylinux.py</code> module to the environment ensures compatibility with <code>manylinux_2_17</code> or older wheels, avoiding the installation of newer, incompatible wheels like <code>manylinux_2_28</code>:</p>
<pre data-code-wrap="py"><code class="lang-py">from typing import NamedTuple


class _GLibCVersion(NamedTuple):
    major: int
    minor: int


def manylinux_compatible(tag_major, tag_minor, tag_arch, **_):  # PEP 600
    if _GLibCVersion(tag_major, tag_minor) &gt; _GLibCVersion(2, 17):
        return False
    return True
</code></pre>
<p>This ensures compatible wheels are installed on Ubuntu systems.</p>
<h3><a name="p-121638-references-2" class="anchor" href="#p-121638-references-2" aria-label="Heading link"></a>References</h3>
<ul>
<li><strong>Dual ABI Documentation</strong>: <a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html">https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html</a></li>
<li><strong>PEP 600: Package Installers</strong>: <a href="https://peps.python.org/pep-0600/#package-installers">https://peps.python.org/pep-0600/#package-installers</a></li>
<li><strong>Discussion on PEP 600</strong>: <a href="https://discuss.python.org/t/pep-600-text-and-example-code-for-package-installers-section-disagree/55329">https://discuss.python.org/t/pep-600-text-and-example-code-for-package-installers-section-disagree/55329</a></li>
</ul>
<p><strong>Next Steps</strong></p>
<p>Later today, we’ll validate this solution by running the full <code>SlicerMorph</code> and <code>SlicerANTs</code> workflows. Once confirmed, we’ll integrate the fix into Slicer and proceed with the release process.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> For now, Preview and Stable builds <strong>remain</strong> disabled. <img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"></p>
<p>Thank you for understanding. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>cc: <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #8 by @jcfr (2025-01-24 01:50 UTC)

<p><strong>Updates:</strong></p>
<blockquote>
<p>To resolve this, we plan to introduce an option that packages a <code>_manylinux.py</code> module</p>
</blockquote>
<p>The corresponding fix has been  reviewed and integrated. For reference, see  pull request <a href="https://github.com/Slicer/Slicer/pull/8168">Slicer#8168</a>.</p>
<h2><a name="p-121679-add-support-for-configuring-_manylinux-module-1" class="anchor" href="#p-121679-add-support-for-configuring-_manylinux-module-1" aria-label="Heading link"></a>Add support for configuring <code>_manylinux</code> module</h2>
<p><em>For convenience and future reference, the associated  <a href="https://github.com/Slicer/Slicer/pull/8168">pull request description</a> is also copied below:</em></p>
<hr>
<blockquote>
<p>This commit introduces the ability to configure a <code>_manylinux</code> module in the Slicer build system to enhance compatibility when installing binary Python wheels.</p>
<p>This update resolves potential issues with installing Python wheels built for newer GLIBC versions or ABIs, which could cause crashes in environments with older configurations.</p>
<p>Specifically, installing <code>manylinux_2_28_x86_64</code> ITK wheels compiled with <code>_GLIBCXX_USE_CXX11_ABI=1</code> was causing segmentation faults in the <em>Stable</em> Slicer version, which is compiled with <code>_GLIBCXX_USE_CXX11_ABI=0</code>. The <code>_manylinux</code> module ensures that <code>manylinux_2_17_x86_64</code> ITK wheels are always installed, even when Slicer and its associated Python interpreter are executed on newer operating systems.</p>
<p>The <code>_manylinux.py</code> module is dynamically generated during the build process and ensures that Python packages installed via <code>pip</code> are compatible with the GLIBC version used in the Slicer build environment.</p>
<h3>Summary of Changes</h3>
<p><strong><code>External_python.cmake</code></strong>:</p>
<ul>
<li>Added logic to configure <code>_manylinux.py</code> for Linux-based build environments.</li>
<li>By default, <code>_manylinux.py</code> is generated. If disabled using the CMake option <code>PYTHON_CONFIGURE_MANYLINUX_MODULE</code>, any existing <code>_manylinux.py</code> module is removed to prevent inadvertent impacts on Python package installations.</li>
<li>Introduced a CMake option <code>PYTHON_REMOVE_MANYLINUX_MODULE_IF_EXISTS</code> to allow users to disable the removal of an existing <code>_manylinux.py</code> module.</li>
</ul>
<p><strong><code>python_configure_manylinux_module.cmake</code></strong>:</p>
<ul>
<li>New CMake script to detect the system’s GLIBC version using <code>ldd</code>.</li>
<li>Dynamically generates the <code>_manylinux.py</code> module, which includes:
<ul>
<li>A <code>manylinux_compatible</code> function to override the default behavior of <code>pip</code> for checking compatibility of manylinux tags.</li>
<li>Embedded documentation and compatibility checks to prevent crashes caused by mismatched ABI or GLIBC versions.</li>
</ul>
</li>
</ul>
<p>By restricting installed packages to compatible manylinux tags, this update ensures stability and reliability for Python packages in the Slicer ecosystem.</p>
<h3>References</h3>
<ul>
<li><a href="https://peps.python.org/pep-0600/">PEP 600: Manylinux Platform Tag</a></li>
<li><a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html">GCC Dual ABI Documentation</a></li>
</ul>
</blockquote>
<hr>

---
