# Trouble loading custom scripted module (HallerIndex) in Slicer 5.8.1 on macOS

**Topic ID**: 42918
**Date**: 2025-05-14
**URL**: https://discourse.slicer.org/t/trouble-loading-custom-scripted-module-hallerindex-in-slicer-5-8-1-on-macos/42918

---

## Post #1 by @giovaniwm (2025-05-14 05:24 UTC)

<p>Hello everyone,</p>
<p>I’m trying to load a custom scripted module called <strong>HallerIndex</strong> into <strong>3D Slicer 5.8.1</strong> on <strong>macOS</strong>, but the module is not being recognized by the application.</p>
<h3><a name="p-125090-my-goals-1" class="anchor" href="#p-125090-my-goals-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/wrench.png?v=15" title=":wrench:" class="emoji" alt=":wrench:" loading="lazy" width="20" height="20"> My goals:</h3>
<p>The module aims to calculate the <strong>Haller Index</strong> from CT images, using a simple UI built in Qt Designer. It is structured as a standard ScriptedLoadableModule.</p>
<h3><a name="p-125090-my-folder-structure-2" class="anchor" href="#p-125090-my-folder-structure-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/file_folder.png?v=15" title=":file_folder:" class="emoji" alt=":file_folder:" loading="lazy" width="20" height="20"> My folder structure:</h3>
<p>objectivec</p>
<p>CopiarEditar</p>
<pre><code class="lang-auto">HallerIndex_Extracted/
├── CMakeLists.txt
└── HallerIndex/
    ├── CMakeLists.txt
    ├── HallerIndex.py
    ├── __init__.py
    └── Resources/
        └── UI/
            └── HallerIndex.ui
</code></pre>
<h3><a name="p-125090-steps-already-taken-3" class="anchor" href="#p-125090-steps-already-taken-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Steps already taken:</h3>
<ul>
<li>I added the path in <strong>Application Settings &gt; Modules &gt; Additional module paths</strong>.</li>
<li>Restarted Slicer.</li>
<li>Searched for the module using the <strong>Module Finder</strong>.</li>
<li>Tried loading via <code>slicer.modules.hallerindex</code> in the Python console.</li>
<li>Also tested with Slicer 5.8.0 and 5.6.2.</li>
<li>Verified naming, indentation, and ScriptedLoadableModule compliance.</li>
</ul>
<h3><a name="p-125090-result-4" class="anchor" href="#p-125090-result-4" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/cross_mark.png?v=15" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> Result:</h3>
<ul>
<li>The module doesn’t appear in the module list.</li>
<li>The Python console returns:<br>
<code>AttributeError: module 'modules' has no attribute 'hallerindex'</code></li>
<li>When trying to load it via the Extension Wizard, I get:<br>
<code>KeyError: script does not set 'EXTENSION_HOMEPAGE'</code> or<br>
<code>EOFError: could not find project</code></li>
</ul>
<h3><a name="p-125090-what-i-need-5" class="anchor" href="#p-125090-what-i-need-5" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/sos_button.png?v=15" title=":sos_button:" class="emoji" alt=":sos_button:" loading="lazy" width="20" height="20"> What I need:</h3>
<p>I’d like help identifying what might be wrong in the setup or code that’s preventing the module from loading. Has anyone successfully installed a custom ScriptedLoadableModule in Slicer 5.8.1 on macOS recently?</p>
<p>Thank you in advance!<br>
—Giovani</p>

---

## Post #2 by @jamesobutler (2025-05-14 11:20 UTC)

<aside class="quote no-group" data-username="giovaniwm" data-post="1" data-topic="42918">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/48db29/48.png" class="avatar"> giovaniwm:</div>
<blockquote>
<p>Searched for the module using the <strong>Module Finder</strong>.</p>
</blockquote>
</aside>
<p>Did you find the entry “HallerIndex” in the module finder dialog and did it indicate not loaded?</p>
<aside class="quote no-group" data-username="giovaniwm" data-post="1" data-topic="42918">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/48db29/48.png" class="avatar"> giovaniwm:</div>
<blockquote>
<p>I added the path in <strong>Application Settings &gt; Modules &gt; Additional module paths</strong>.</p>
</blockquote>
</aside>
<p>What was the full path that you added?</p>

---

## Post #3 by @giovaniwm (2025-05-14 16:26 UTC)

<p>Good morning, I’ll send it now</p>
<p>The full path I added in <strong>Application Settings &gt; Modules &gt; Additional module paths</strong> was:</p>
<pre><code class="lang-auto">
swift

/Users/giovaniwaltrickmezzalira/Desktop/HallerIndex_Extracted

</code></pre>
<p>Inside this folder, I have:</p>
<pre><code class="lang-auto">
objectivec

HallerIndex_Extracted/
├── CMakeLists.txt
└── HallerIndex/
    ├── CMakeLists.txt
    ├── HallerIndex.py
    ├── __init__.py
    └── Resources/
        └── UI/
            └── HallerIndex.ui

</code></pre>
<p>Let me know if I should change the structure or path. Thanks for your help!</p>
<p>“Here is a screenshot of the folder I added as the module path.</p>
<p>(Attachment CMakeLists.txt is missing)</p>
<p>(Attachment HallerIndex.py is missing)</p>
<p>(Attachment HallerIndex.zip is missing)</p>

---

## Post #4 by @jamesobutler (2025-05-14 17:36 UTC)

<aside class="quote no-group" data-username="giovaniwm" data-post="3" data-topic="42918">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/48db29/48.png" class="avatar"> giovaniwm:</div>
<blockquote>
<pre><code class="lang-auto">/Users/giovaniwaltrickmezzalira/Desktop/HallerIndex_Extracted
</code></pre>
</blockquote>
</aside>
<p>Instead of a path to the extension directory, try specifying the path to the module directory.</p>
<p><code>/Users/giovaniwaltrickmezzalira/Desktop/HallerIndex_Extracted/HallerIndex</code></p>

---
