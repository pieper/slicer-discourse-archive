# C++11 modernization, update to ITK5, removal of obsolete Qt4 and VTK7 support

**Topic ID**: 6165
**Date**: 2019-03-16
**URL**: https://discourse.slicer.org/t/c-11-modernization-update-to-itk5-removal-of-obsolete-qt4-and-vtk7-support/6165

---

## Post #1 by @jcfr (2019-03-16 18:49 UTC)

<p>This past week we were busy modernizing the Slicer code base to:</p>
<ul>
<li>support only C++11 (including update to use <code>nullptr</code> and <code>override</code> keywords)</li>
<li>use ITKv5</li>
<li>remove obsolete Qt4/VTK7 support.</li>
</ul>
<p>Thanks to <a class="mention" href="/u/phcerdan">@phcerdan</a>, <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> for their contributions.</p>
<p>A new migration guide has also been added. See   <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Obsolete_Code_Removal" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Obsolete_Code_Removal</a></p>

---

## Post #2 by @benzwick (2021-04-16 07:54 UTC)

<p>Does this mean it is now possible to use C++11 features in extension modules? If so, the following on advice on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#Can_I_use_C.2B.2B11.2F14.2F17_language_features_.3F" rel="noopener nofollow ugc">Developers/FAQ</a> should be updated:</p>
<blockquote>
<p>Since Slicer is not built with these features (it used c++98/c++03), you should not use C++11/14/17 language features in your extensions.</p>
</blockquote>

---

## Post #3 by @lassoan (2021-04-18 05:00 UTC)

<p>Yes, C++11 features can be used. I’ve updated the FAQ - thanks for reporting the outdated documentation.</p>

---
