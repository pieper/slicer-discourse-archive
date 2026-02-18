# No extensions in Extension Manager - 4.10.2 build

**Topic ID**: 7262
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/no-extensions-in-extension-manager-4-10-2-build/7262

---

## Post #1 by @MattTroke (2019-06-20 16:03 UTC)

<p>I checked out the master-410 branch of Slicer and built it, but there are no extensions available in the Extension Manager when I run it. Instead I get the message “No extensions found for win:64-bit, revision: ‘670e575’. Please try a different combination”. I had a similar issue with a 4.9.0 build of slicer which is why I decided to upgrade thinking it may solve the problem. I have added my own loadable module to the code base, but have not altered any core code related to extensions.</p>
<p>Not sure if I’m missing an additional build step or configuration to get this working. Any help would be appreciated.</p>
<p>Matt</p>

---

## Post #2 by @lassoan (2019-06-20 16:10 UTC)

<p>Since it is very hard to ensure ABI compatibility between libraries that are built on different computers using potentially different build environment, we do not encourage people to try and use factory-built extensions with their custom Slicer builds (you can still try it, by checking out Slicer from SVN with the official Slicer-4.10.2 revision 28257, but it may or may not work).</p>
<p>Instead, we recommend to build all the extensions that your custom Slicer distribution needs on your own computer. You can very easily create a custom distribution (with your own application name, branding, set of enabled/disabled features, modules, extensions) by using the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">SlicerCustomAppTemplate</a>.</p>

---
