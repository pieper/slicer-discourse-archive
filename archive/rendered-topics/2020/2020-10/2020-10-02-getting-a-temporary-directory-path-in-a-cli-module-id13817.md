# Getting a temporary directory path in a CLI module

**Topic ID**: 13817
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/getting-a-temporary-directory-path-in-a-cli-module/13817

---

## Post #1 by @Mik (2020-10-02 13:11 UTC)

<p>Input and output volumes are stored in temporary directory, and i need to transform an input volume into MetaImage format for further processing in plastimatch. How setup correctly the mha file name (without parsing the input volume file name), so it will be saved into the Slicer temporary directory?</p>
<p>In loadable module it’s simple:<br>
<code>QString tmpDirName = qSlicerCoreApplication::application()-&gt;temporaryPath();</code></p>
<p>Does a CLI module have anything like that?</p>

---

## Post #2 by @pieper (2020-10-02 15:26 UTC)

<p>The idea of a CLI is that it can be a stand-alone executable that can run as a process external to Slicer but pass info back and forth by our conventions.  But the CLI itself can really be anything.  In the past we have had CLIs that link with their own version of Qt and bring up a GUI.  So you could also link with QtCore to get the tempdir, or find another cross-platform way for that.</p>

---

## Post #3 by @lassoan (2020-10-03 03:20 UTC)

<aside class="quote no-group" data-username="Mik" data-post="1" data-topic="13817">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>In loadable module it’s simple:<br>
<code>QString tmpDirName = qSlicerCoreApplication::application()-&gt;temporaryPath();</code></p>
<p>Does a CLI module have anything like that?</p>
</blockquote>
</aside>
<p>In CLI it is much simpler, since the caller (typically Slicer) passes all input and output filenames as command-line arguments, so your CLI does not have to generate any filenames.</p>

---
