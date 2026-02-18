# Spanish Characters

**Topic ID**: 10333
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/spanish-characters/10333

---

## Post #1 by @Pablo_de_Arriba (2020-02-18 13:42 UTC)

<p>In the beginning of the code write (in the first line):</p>
<p># -<em>- coding: 850 -</em>-</p>
<p>Then, you can use the characters as follows (unicode):</p>
<p>\xe1 = á<br>
\xe9 = é<br>
\xed = í<br>
\xf3 = ó<br>
\xfa = ú<br>
\xc1 = Á<br>
\xc9 = É<br>
\xcd = Í<br>
\xd3 = Ó<br>
\xda = Ú<br>
\xf1 = ñ<br>
\xd1 = Ñ<br>
\xbf = ¿<br>
\xa1 = ¡</p>

---

## Post #2 by @lassoan (2020-02-18 14:05 UTC)

<p>Thanks for the information. Note that code pages are legacy technology. While code pages might still work in certain circumstances, nowadays UTF-8 is the universal standard on all modern editors and most other software, too.</p>
<p>In Slicer we switch to “UTF-8 everywhere” in about a week - see <a href="https://github.com/Slicer/Slicer/pull/1319">https://github.com/Slicer/Slicer/pull/1319</a>.</p>

---

## Post #3 by @timeanddoctor (2020-02-19 13:21 UTC)

<p>This means that we can translate to Chinese more easy(such as in the Gui of a  module)?</p>

---

## Post #4 by @lassoan (2020-02-20 03:45 UTC)

<p>This UTF-8 development will allow usage of special characters in file names, node names, and in general, any strings that the user enters or loads from files.</p>
<p>You can already translate most of the GUI, but there are a few things to do:</p>
<ul>
<li>use <code>tr</code> macro in all translatable text in the Slicer source code (should not be too much work) translation macros can find them</li>
<li>develop translation mechanism for CLI modules and Python scripted modules</li>
<li>update string definition in Python scripted modules to use the new mechanism (or .ui files)</li>
<li>re-enable language selection on GUI (was available at some point but disabled now)</li>
</ul>

---
