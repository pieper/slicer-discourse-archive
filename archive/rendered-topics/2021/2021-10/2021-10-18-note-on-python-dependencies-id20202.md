# Note on python dependencies

**Topic ID**: 20202
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/note-on-python-dependencies/20202

---

## Post #1 by @Alex_Vergara (2021-10-18 10:15 UTC)

<p>This note is for python extension developers.</p>
<p>With the introduction of setuptools==58 in the <a href="https://github.com/Slicer/Slicer/pull/5925" rel="noopener nofollow ugc">Slicer pull 5925</a> all dependencies that rely on 2to3 libraries are totally broken as discussed in several python packages like <a href="https://github.com/tikitu/jsmin/pull/34" rel="noopener nofollow ugc">jsmin</a>, <a href="https://github.com/danthedeckie/simpleeval/issues/90" rel="noopener nofollow ugc">simpleeval</a>, etc.</p>
<p>This will lead to errors in CDash as <a href="https://slicer.cdash.org/test/19771184" rel="noopener nofollow ugc">this one</a> that will prevent you from building your extensions. You will not be able to update anymore your extensions if you depend on some package that fall into this issue, as you will not control slicer setuptools package (you can’t downgrade it).</p>
<p>The ONLY solution is to remove all your dependencies to those obsolete packages and find alternative solutions. Some of those packages has been unmantained for a long time.</p>

---

## Post #2 by @jamesobutler (2021-10-18 13:49 UTC)

<p>Yes you will need to begin using packages that have been appropriately ported to python 3 and don’t rely on lib2to3. I would encourage you to update to latest versions of packages that work with the latest setuptools. Including upgrading syntax or choosing a different package that has been maintained for the modern python future.</p>
<p>In the python documentation <a href="https://docs.python.org/3/library/2to3.html#module-lib2to3" class="inline-onebox" rel="noopener nofollow ugc">2to3 — Automated Python 2 to 3 code translation — Python 3.12.1 documentation</a> it details that lib2to3 is marked as fully deprecated with Python 3.11 and will be removed from the standard library in a few versions.</p>
<p>Slicer will be moving to the latest Python version soon as packages have already dropped python 3.6 and even 3.7 support.</p>
<blockquote>
<p>Python 3.10 includes new language syntax that is not parsable by lib2to3’s LL(1) parser</p>
</blockquote>

---
