# Is the sandbox extension failing for windows

**Topic ID**: 9534
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/is-the-sandbox-extension-failing-for-windows/9534

---

## Post #1 by @muratmaga (2019-12-17 20:57 UTC)

<p>It is not available within the extension manager for the last couple days?<br>
<a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #2 by @Sam_Horvath (2019-12-17 21:07 UTC)

<p>No failures on the dashboard: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Sandbox" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Sandbox</a></p>
<p>Was able to download package and manually install</p>

---

## Post #3 by @Sam_Horvath (2019-12-17 21:10 UTC)

<p>Search function may be buggy - I was able to find it under the Examples section in the side bar.</p>

---

## Post #4 by @muratmaga (2019-12-17 21:17 UTC)

<p>Oh, yes now I found it.  Weird the top level search wasn’t returning it.</p>
<p>Also as a comment, would it be possible to sort the extensions by name? It will make easier to find an extension, if you know the name. It is easy to overlook the icons and they seemed to be randomly sorted.</p>

---

## Post #5 by @Sam_Horvath (2019-12-17 21:21 UTC)

<p>So, the extensions list seems to be <em>almost</em> in alphabetical order, which is weird.  If you are scrolling through the “All” category, the Sandbox also isn’t visible, which is why it doesn’t pop up in the main search (also weird).  It is only visible in the Examples category view.</p>

---

## Post #6 by @muratmaga (2019-12-17 21:22 UTC)

<p>It starts kind of sorted, then sorting breaks in the 3-4th row for me. With 100+ extension we need to a good mechanism.</p>

---

## Post #7 by @Sam_Horvath (2019-12-17 21:23 UTC)

<p>As far as making changes to the Extension Manager functionality, we need to / are planning to revamp the whole front-end.</p>

---

## Post #8 by @Sam_Horvath (2019-12-17 21:24 UTC)

<p>Ok, so the order actually isn’t a sorting, its the order in which the extensions were uploaded.  The build order is alphabetical with rearrangements to accommodate dependencies.  Yes, we need an actual list sort.</p>

---

## Post #9 by @lassoan (2019-12-17 21:25 UTC)

<p>It would be also great if the migration of the backend from midas3 to girder could be completed. I would expect it would make the server faster and more robust and make all investments into frontend more secure. I guess SlicerMorph, PerkLab, and other groups could contribute to the funding.</p>

---

## Post #10 by @Sam_Horvath (2019-12-17 21:28 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> is planning to look at redoing the manager over the Project Week.  The new-front end will be written to support girder to allow the switch over.</p>

---

## Post #11 by @Aya_El_Gebaly (2021-03-14 18:18 UTC)

<p>THANKS , it works</p>

---
