# Is app store down?

**Topic ID**: 1368
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/is-app-store-down/1368

---

## Post #1 by @muratmaga (2017-11-03 20:07 UTC)

<p>Extension manager hangs at 85% and doesn’t display any plugins.<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a> also times out for me.</p>

---

## Post #2 by @pieper (2017-11-03 20:34 UTC)

<p>I had this issue earlier, but eventually it worked.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> maybe ping the sysadmins?</p>

---

## Post #3 by @jcfr (2017-11-03 22:16 UTC)

<p>Thanks for the note. We will have a look shortly.</p>
<p>The server hosting the app store is up and running (<a href="http://slicer.kitware.com/">http://slicer.kitware.com/</a>), it looks like the issue is specific to the appstore application running from the same server.</p>
<p>More specifically, using an URL requesting a set of extension associated with a specific <code>os/arch/revision</code> works:</p>
<p><code>http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=26054</code></p>
<p>but accessing the app store without specifying a revision hangs:</p>
<p><code>http://slicer.kitware.com/midas3/slicerappstore</code><br>
<code>http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64</code></p>

---
