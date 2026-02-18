# Are Qt4 and Qt5 still supported?

**Topic ID**: 2233
**Date**: 2018-03-03
**URL**: https://discourse.slicer.org/t/are-qt4-and-qt5-still-supported/2233

---

## Post #1 by @jcfr (2018-03-03 00:40 UTC)

<p>Technically, as of 2018/03/02, both Qt4 and Qt5 are still supported and we have not updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a> on the wiki.</p>
<p>Rational: For now, it allows us at Kitware to keep using the latest version of Slicer while our customers to transition their Slicer-based applications to Qt5.</p>
<p>That said, this will change very soon (few weeks) as we will remove the support for Qt4 from the code base and support building only against Qt 5.9 and beyond.</p>
<p>Before doing so, we will create a tag to identify the last revision working with Qt4.</p>
<p>To summarize, the next steps are:</p>
<ul>
<li>Complete the transition of daily Linux build to use Qt5</li>
<li>Finalize update of build instructions on the wiki</li>
<li>Remove Qt4 support from the code base</li>
</ul>

---
