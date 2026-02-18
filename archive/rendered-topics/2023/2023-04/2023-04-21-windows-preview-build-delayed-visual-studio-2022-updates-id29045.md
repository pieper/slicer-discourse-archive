# Windows preview build delayed & Visual Studio 2022 updates

**Topic ID**: 29045
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/windows-preview-build-delayed-visual-studio-2022-updates/29045

---

## Post #1 by @jcfr (2023-04-21 11:52 UTC)

<h3><a name="p-93862-impact-1" class="anchor" href="#p-93862-impact-1" aria-label="Heading link"></a>Impact</h3>
<p>Slicer <code>Preview</code> application and extension packages of <span class="discourse-local-date" data-date="2023-04-20" data-email-preview="Fri, Apr 21, 2023 3:00 AM UTC" data-time="23:00:00" data-timezone="America/New_York">2023-04-21T03:00:00Z</span> for Windows will be available later than expected.</p>
<h3><a name="p-93862-update-details-2" class="anchor" href="#p-93862-update-details-2" aria-label="Heading link"></a>Update Details</h3>
<h4><a name="p-93862-installed-components-for-uwparm64-development-3" class="anchor" href="#p-93862-installed-components-for-uwparm64-development-3" aria-label="Heading link"></a>Installed components for UWP/ARM64 development</h4>
<p>To support the development of the <code>SlicerMixedReality</code> extension, we needed to install new Visual Studio 2022 workloads  &amp; components to support Universal Windows Platform (UWP) development targeting ARM64.</p>
<h4><a name="p-93862-updated-c-cxx-compilers-4" class="anchor" href="#p-93862-updated-c-cxx-compilers-4" aria-label="Heading link"></a>Updated C &amp; CXX compilers</h4>
<p>In the process, the version of the C &amp; CXX compilers provided by Visual Studio 2022 changed and is summarized below:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>MSVC compiler identification</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Before</td>
<td><code>19.30.30709.0</code></td>
<td><code>C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.30.30705/bin/Hostx64/x64/cl.exe</code></td>
</tr>
<tr>
<td>After</td>
<td><code>19.35.32217.1</code></td>
<td><code>C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215/bin/Hostx64/x64/cl.exe</code></td>
</tr>
</tbody>
</table>
</div><h4><a name="p-93862-impact-on-slicer-extension-stable-builds-5" class="anchor" href="#p-93862-impact-on-slicer-extension-stable-builds-5" aria-label="Heading link"></a>Impact on Slicer extension stable builds</h4>
<p>To support building the <code>Stable</code> extension, the <code>SlicerConfig.make</code>  file<sup class="footnote-ref"><a href="#footnote-93862-1" id="footnote-ref-93862-1">[1]</a></sup> was updated replacing the 4 occurrences of <code>14.30.30705</code> with <code>14.35.32215</code>.</p>
<p>This is required to ensure the updated compiler used to build the nightly <code>Stable</code> extensions matches the one hard-coded in <code>SlicerConfig.cmake</code>. Indeed, there is a consistency check implemented in <code>slicer_config_set_compiler_ep</code> defined and called from within <code>SlicerConfig</code></p>
<p><em>What about the ABI compatibility ?</em></p>
<p>Since binaries are built with the v143 toolset, extensions build with the updated compiler will be compatible<sup class="footnote-ref"><a href="#footnote-93862-2" id="footnote-ref-93862-2">[2]</a></sup> with the stable release built with an older compiler but also targeting the same toolset.</p>
<h4><a name="p-93862-the-infamous-sorry-something-went-wrong-vs2022-update-error-6" class="anchor" href="#p-93862-the-infamous-sorry-something-went-wrong-vs2022-update-error-6" aria-label="Heading link"></a>The infamous <code>"Sorry, something went wrong"</code> VS2022 update error</h4>
<p>When attempting to install new Visual Studio 2022 components (through ), it was failing with <em>Sorry, something went wrong</em>.</p>
<p>Inspecting the log file <code>%temp%\dd_installer_YYYYMMDDHHMMSS.log</code>, there were errors.</p>
<p>The steps are provided for future reference and where adapted from details  provided by Philippe Debayle at <a href="https://developercommunity.visualstudio.com/t/Unable-to-use-VSInstaller-because-it-sys/10323762#T-N10323790-N10323885">https://developercommunity.visualstudio.com/t/Unable-to-use-VSInstaller-because-it-sys/10323762#T-N10323790-N10323885</a></p>
<ol>
<li>
<p>To Fix the communication issue preventing developer news from being displayed:</p>
<ul>
<li>Edit <code>C:\Program Files (x86)\Microsoft Visual Studio\Installer\setup.exe.config</code></li>
<li>Add <code>Switch.System.Net.DontEnableSchUseStrongCrypto=false;</code> to the value attribute<br>
of the <code>AppContextSwitchOverrides</code> element.</li>
</ul>
</li>
<li>
<p>Address the <code>Error 0x80070057: Failed to read instance xxxxxx" (where xxxx is the vs instance number)</code></p>
<ul>
<li>Go to <code>%localappdata%\Microsoft\VisualStudio\Packages\_Channels\&lt;vs instance number&gt;</code></li>
<li>Edit the file <code>channelmanifest.json</code> as administrator (Create a copy of the file first)</li>
<li>Copy the content of the file into an online JSON prettifier (e.g <code>https://codebeautify.org/jsonviewer</code>), then switch the editor mode from <code>View</code> to <code>Text</code>.</li>
<li>Copy the formatted content into the <code>channelmanifest.json</code> file</li>
<li>In editor like “Notepad++”, search for all occurrences <code>"id"</code> in all files (with the double quotes")</li>
<li>Append <code>.arm64</code> to the id of each channel associated with <code>"productArch": "arm64"</code>. The goal is to have all top-level <code>ChannelProduct</code> identifier unique,</li>
</ul>
</li>
<li>
<p>Run <code>setup.exe</code> as described in the <code>dd_installer_*.log</code> file by specifying the additional parameter <code>--channelUri C:\path\to\modifed\channelmanifest.json</code></p>
</li>
</ol>
<p>This allowed to move forward with the update process.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-93862-1" class="footnote-item"><p><code>C:\path\to\S\S-0-build\Slicer-build\SlicerConfig.make</code> <a href="#footnote-ref-93862-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-93862-2" class="footnote-item"><p><a href="https://learn.microsoft.com/en-us/cpp/porting/binary-compat-2015-2017?view=msvc-170" class="inline-onebox">C++ binary compatibility 2015-2026 | Microsoft Learn</a> <a href="#footnote-ref-93862-2" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
