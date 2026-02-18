# Cannot open files or folders from within Slicer on Linux

**Topic ID**: 30134
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/cannot-open-files-or-folders-from-within-slicer-on-linux/30134

---

## Post #1 by @benzwick (2023-06-20 03:01 UTC)

<p>I’m using Slicer (stable 5.2.2 and preview 5.3.0-2023-06-17) on Debian 12 (bookworm) Linux with KDE. When I try to open a file using the “Edit” button in a ScriptedLoadableModule or a directory in e.g. the SlicerElastix module I get the following error and the file or directory is not opened:</p>
<pre><code class="lang-plaintext">[CRITICAL][FD] 19.06.2023 22:28:27 [] (unknown:0) - kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
</code></pre>
<p>If I do the same using Slicer that I compiled myself I get the same error (with some additional errors), but the file or directory is opened:</p>
<pre><code class="lang-plaintext">[CRITICAL][FD] 19.06.2023 22:52:12 [] (unknown:0) - kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
[CRITICAL][FD] 19.06.2023 22:52:12 [] (unknown:0) - Hspell: can't open /usr/share/hspell/hebrew.wgz.sizes.
[CRITICAL][FD] 19.06.2023 22:52:12 [] (unknown:0) - kf.sonnet.clients.hspell: HSpellDict::HSpellDict: Init failed
</code></pre>
<p>The relevant lines in the code are these in ScriptedLoadableModule:</p>
<pre><code class="lang-python">    def onEditSource(self):
        filePath = slicer.util.modulePath(self.moduleName)
        qt.QDesktopServices.openUrl(qt.QUrl("file:///" + filePath, qt.QUrl.TolerantMode))
</code></pre>
<p>and these in SlicerElastix:</p>
<pre><code class="lang-python">  def onShowTemporaryFilesFolder(self):
    qt.QDesktopServices().openUrl(qt.QUrl("file:///" + self.logic.getTempDirectoryBase(), qt.QUrl.TolerantMode))
</code></pre>
<p>Does anyone have any ideas about what might be happening here?</p>

---

## Post #2 by @benzwick (2023-06-20 15:38 UTC)

<p>Here is the output I get if I run the same commands in the Python console of the pre-built Slicer 5.3.0-2023-06-17 (the files do not open):</p>
<pre><code class="lang-plaintext">&gt;&gt;&gt; qt.QDesktopServices.openUrl(qt.QUrl("file:///home/ben", qt.QUrl.TolerantMode))
True
&gt;&gt;&gt; 
[FD] kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
&gt;&gt;&gt; qt.QDesktopServices.openUrl(qt.QUrl("file:///home/ben/test.txt", qt.QUrl.TolerantMode))
True
&gt;&gt;&gt; 
[FD] kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
</code></pre>
<p>If I run the same commands using Slicer that I compiled myself I get the same output but the files are opened as expected.</p>
<p>The following <code>xdg-open</code> commands also work as expected even though they produce similar warnings/errors:</p>
<pre><code class="lang-plaintext">ben@p1:~$ xdg-open "/home/ben"
kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
kf.coreaddons: Expected a KPluginFactory, got a KIOPluginForMetaData
kf.coreaddons: Expected a KPluginFactory, got a KIOPluginForMetaData
kf.coreaddons: Expected a KPluginFactory, got a KIOPluginForMetaData
kf.coreaddons: Expected a KPluginFactory, got a KIOPluginForMetaData

ben@p1:~$ cat "/home/ben/test.txt"
hello

ben@p1:~$ xdg-open "/home/ben/test.txt"
kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found
Hspell: can't open /usr/share/hspell/hebrew.wgz.sizes.
kf.sonnet.clients.hspell: HSpellDict::HSpellDict: Init failed
</code></pre>
<p>See also the discussion on the Debian forum <a href="https://forums.debian.net/viewtopic.php?p=775312" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #3 by @benzwick (2023-06-20 15:40 UTC)

<p>In today’s developer meeting <a class="mention" href="/u/jcfr">@jcfr</a> suggested to look at the following:</p>
<p>Relevant function on linux <code>QDBusMessage xdgDesktopPortalOpenUrl(const QUrl &amp;url)</code></p>
<p>In Qt 6: <a href="https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fqt%2Fqtbase%2Fblob%2F0235de994be7e04aca3456f1260b18313dd45b74%2Fsrc%2Fgui%2Fplatform%2Funix%2Fqgenericunixservices.cpp%23L204-L232&amp;data=05%7C01%7Cbenjamin.zwick%40uwa.edu.au%7Ceea6a7781a91403550f808db719d46ff%7C05894af0cb2846d8871674cdb46e2226%7C0%7C0%7C638228692547253810%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=AZBDVCarN1rRBeVOEfv3YjTJMAhTtntLrBxkIDNY7Yo%3D&amp;reserved=0" rel="noopener nofollow ugc">https://github.com/qt/qtbase/blob/0235de994be7e04aca3456f1260b18313dd45b74/src/gui/platform/unix/qgenericunixservices.cpp#L204-L232</a></p>
<p>May be related to <a href="https://aus01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgithub.com%2Fqt%2Fqtbase%2Fcommit%2Ffbfaf5d38b3455bb561e739271986be91a7c7169&amp;data=05%7C01%7Cbenjamin.zwick%40uwa.edu.au%7Ceea6a7781a91403550f808db719d46ff%7C05894af0cb2846d8871674cdb46e2226%7C0%7C0%7C638228692547253810%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=iMrLqu5UKXZls8TCgjiOqkKnQ1w62AzOgzsd096rYwA%3D&amp;reserved=0" rel="noopener nofollow ugc">https://github.com/qt/qtbase/commit/fbfaf5d38b3455bb561e739271986be91a7c7169</a></p>
<p>as well as XDG_ACTIVATION_TOKEN</p>

---

## Post #4 by @benzwick (2023-06-20 20:51 UTC)

<p>I tested this again today on a fresh install of Debian 12 Bookworm in a VirtualBox machine. To test the behavior I clicked the “Open Slicer resource file” in the “General” Application Settings. In the GNOME desktop environment, the slicerrc.py file is opened with LibreOffice writer (although the software used can be configured by the user), but in the KDE/Plasma desktop environment, I get the same behavior as described above.</p>
<p>Also, my Debian installation and self-built Slicer are using Qt 5.15.8 (which is working) whereas the pre-compiled stable and preview Slicer are using 5.15.2 (which is NOT working).</p>
<p>I am guessing that this is a bug in Qt or KDE, which may have been fixed in Qt &gt; 5.15.2. I’ll list any relevant links here:</p>
<ul>
<li><a href="https://bugs.kde.org/show_bug.cgi?id=442721" class="inline-onebox" rel="noopener nofollow ugc">442721 – kf.service.services: KApplicationTrader: mimeType "x-scheme-handler/file" not found</a></li>
</ul>

---
