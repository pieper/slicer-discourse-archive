# Is it possible to change the name and the icon of the [Package] command output?

**Topic ID**: 27220
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/is-it-possible-to-change-the-name-and-the-icon-of-the-package-command-output/27220

---

## Post #1 by @jay1987 (2023-01-13 02:33 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7a6709b9c819e22cd2b635978da786feb5f0a22.png" alt="image" data-base62-sha1="zkOwV78NZzA8lDH7nnhOTeCIu2K" width="681" height="204"><br>
my boss want to change the Slicer.exe icon and name to the company product name<br>
these directory is generate from Slicer [Package] Command<br>
is the action legal ? i don’t known how to Implement this demand</p>

---

## Post #2 by @ebrahim (2023-01-13 02:48 UTC)

<p>You may want to look into SlicerCustomAppTemplate:</p>
<ul>
<li><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></li>
<li><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom 3D Slicer application</a></li>
</ul>
<p>It’s made for your purpose: take slicer, customize it at the deepest level, and cover it with your company branding so it doesn’t look like slicer anymore. There are convenient placeholders for changing the app name and icons/logos.</p>

---

## Post #3 by @jay1987 (2023-01-13 02:50 UTC)

<p>dear ebrahim!<br>
thank you very much !</p>

---

## Post #4 by @ebrahim (2023-01-13 03:01 UTC)

<blockquote>
<p>is the action legal ?</p>
</blockquote>
<p>and yes it is legal to modify and commercially use Slicer; see the <a href="https://github.com/Slicer/Slicer/blob/main/License.txt" rel="noopener nofollow ugc">license</a> for actual details</p>

---
