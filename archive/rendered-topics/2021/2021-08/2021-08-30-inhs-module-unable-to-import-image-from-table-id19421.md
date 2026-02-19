---
topic_id: 19421
title: "Inhs Module Unable To Import Image From Table"
date: 2021-08-30
url: https://discourse.slicer.org/t/19421
---

# INHS module: unable to import image from table. 

**Topic ID**: 19421
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/inhs-module-unable-to-import-image-from-table/19421

---

## Post #1 by @megbalk (2021-08-30 23:48 UTC)

<p>Sorry if this is the wrong forum to ask for advice, but I recently installed slicer on my arch build and installed 3dSlicer. I’m trying to load an image in slicer morph from a table that has a URL. The URL resolves outside of slicer morph, however when selecting the image to load, the terminal output is:</p>
<pre><code class="lang-auto">    &lt;b&gt;	Download failed: &lt;urlopen error [Errno 110] Connection timed out&gt;&lt;/b&gt;
    &lt;b&gt;Download failed (attempt 1 of 3)...&lt;/b&gt; 
    &lt;b&gt;	Download failed: &lt;urlopen error [Errno 110] Connection timed out&gt;&lt;/b&gt;
    &lt;b&gt;Download failed (attempt 2 of 3)...&lt;/b&gt;
    error: [/opt/3dslicer/bin/SlicerApp-real] exit abnormally - Report the problem.</code></pre>
<p>(full stacktrace)</p>
<pre><code class="lang-auto">    Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use             
    QT_QPA_PLATFORM=wayland to run on Wayland anyway.
    Switch to module:  "Welcome"
    Switch to module:  "INHSTools"
    "Table" Reader has successfully read the file 
    "/home/megbalk/Documents/Slicer/iDigBioImagesNeeded.csv" "[0.02s]"
    setViewLabel should be called before setViewNode !
    setViewLabel should be called before setViewNode !
    setViewLabel should be called before setViewNode !
    setViewLabel should be called before setViewNode !
    setViewLabel should be called before setViewNode !
    setViewLabel should be called before setViewNode !
    &lt;b&gt;	Download failed: &lt;urlopen error [Errno 110] Connection timed out&gt;&lt;/b&gt;
    &lt;b&gt;Download failed (attempt 1 of 3)...&lt;/b&gt;
    &lt;b&gt;	Download failed: &lt;urlopen error [Errno 110] Connection timed out&gt;&lt;/b&gt;
    &lt;b&gt;Download failed (attempt 2 of 3)...&lt;/b&gt;
    error: [/opt/3dslicer/bin/SlicerApp-real] exit abnormally - Report the problem.</code></pre>
<p>This happens when building from source, downloading the binary from AUR and downloading package from archlinuxrepocn.</p>
<pre><code class="lang-auto">uname -r -&gt; 5.12.12-arch1-1</code></pre>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @muratmaga (2021-08-31 04:21 UTC)

<p><a class="mention" href="/u/megbalk">@megbalk</a><br>
I suspect <strong>iDigBioImagesNeeded.csv</strong> is not in the format/order that this module expects and is probably not pulling the right URL from the table. Alternatively, you are behind a corporate firewall and trying to download https:// links and encountering an issue similar to <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361">this</a>.</p>
<p>In any event this is not a general purpose module and the issues are better discussed on our project slack channel.</p>

---
