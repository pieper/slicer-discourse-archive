---
topic_id: 27227
title: "Persist New Server In Dicom Query Servers List"
date: 2023-01-13
url: https://discourse.slicer.org/t/27227
---

# Persist new server in DICOM Query Servers list

**Topic ID**: 27227
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/persist-new-server-in-dicom-query-servers-list/27227

---

## Post #1 by @Paula_Moreno (2023-01-13 14:40 UTC)

<p>Hello everyone,</p>
<p>I am woking with Slicer in docker and I would like to save a new server in DICOM networking for the followings session. So I need to find the file where these preferences are stored to use it as a volume in the docker container. I already tried with Slicer.ini but it seems that these preferences are not defined in here.<br>
does somebody have any clue about it ??</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9205ce659aa07e501636d30a79f3e63b841bad6.png" data-download-href="/uploads/short-url/zxSe5NbIFtlMzWqwnch0evgYdg2.png?dl=1" title="Dibujo sin título" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9205ce659aa07e501636d30a79f3e63b841bad6_2_618x500.png" alt="Dibujo sin título" data-base62-sha1="zxSe5NbIFtlMzWqwnch0evgYdg2" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9205ce659aa07e501636d30a79f3e63b841bad6_2_618x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9205ce659aa07e501636d30a79f3e63b841bad6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9205ce659aa07e501636d30a79f3e63b841bad6.png 2x" data-dominant-color="2F2F30"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Dibujo sin título</span><span class="informations">848×685 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-01-13 16:54 UTC)

<p>You’ll find them under the <code>ServerNodes</code> part of the Slicer.ini file.  This is done in CTK using the QSettings infrastructure.  Probably you can just enter the data in one slicer instance and the copy them in encoded form into any custom settings file.</p>
<pre><code class="lang-auto">[ServerNodes]
0=@Variant(\0\0\0\b\0\0\0\x6\0\0\0\b\0P\0o\0r\0t\0\0\0\n\0\0\0\n\0\x31\0\x31\0\x31\0\x31\0\x32\0\0\0\b\0N\0\x61\0m\0\x65\0\0\0\n\0\0\0\x16\0\x45\0x\0\x61\0m\0p\0l\0\x65\0H\0o\0s\0t\0\0\0\x14\0\x43\0h\0\x65\0\x63\0k\0S\0t\0\x61\0t\0\x65\0\0\0\x2\0\0\0\0\0\0\0\b\0\x43\0G\0\x45\0T\0\0\0\x2\0\0\0\0\0\0\0\xe\0\x41\0\x64\0\x64\0r\0\x65\0s\0s\0\0\0\n\0\0\0\"\0\x64\0i\0\x63\0o\0m\0.\0\x65\0x\0\x61\0m\0p\0l\0\x65\0.\0\x63\0o\0m\0\0\0\xe\0\x41\0\x45\0T\0i\0t\0l\0\x65\0\0\0\n\0\0\0\xe\0\x41\0\x45\0T\0I\0T\0L\0\x45)
1=@Variant(\0\0\0\b\0\0\0\x6\0\0\0\b\0P\0o\0r\0t\0\0\0\n\0\0\0\n\0\x31\0\x31\0\x31\0\x31\0\x32\0\0\0\b\0N\0\x61\0m\0\x65\0\0\0\n\0\0\0$\0M\0\x65\0\x64\0i\0\x63\0\x61\0l\0\x43\0o\0n\0n\0\x65\0\x63\0t\0i\0o\0n\0s\0\0\0\x14\0\x43\0h\0\x65\0\x63\0k\0S\0t\0\x61\0t\0\x65\0\0\0\x2\0\0\0\0\0\0\0\b\0\x43\0G\0\x45\0T\0\0\0\x2\0\0\0\x2\0\0\0\xe\0\x41\0\x64\0\x64\0r\0\x65\0s\0s\0\0\0\n\0\0\0\"\0\x64\0i\0\x63\0o\0m\0s\0\x65\0r\0v\0\x65\0r\0.\0\x63\0o\0.\0u\0k\0\0\0\xe\0\x41\0\x45\0T\0i\0t\0l\0\x65\0\0\0\n\0\0\0\n\0\x41\0N\0Y\0\x41\0\x45)
2=@Variant(\0\0\0\b\0\0\0\x6\0\0\0\b\0P\0o\0r\0t\0\0\0\n\0\0\0\x6\0\x31\0\x30\0\x30\0\0\0\b\0N\0\x61\0m\0\x65\0\0\0\n\0\0\0\b\0t\0\x65\0s\0t\0\0\0\x14\0\x43\0h\0\x65\0\x63\0k\0S\0t\0\x61\0t\0\x65\0\0\0\x2\0\0\0\0\0\0\0\b\0\x43\0G\0\x45\0T\0\0\0\x2\0\0\0\x2\0\0\0\xe\0\x41\0\x64\0\x64\0r\0\x65\0s\0s\0\0\0\n\0\0\0\x12\0y\0\x61\0h\0o\0o\0.\0\x63\0o\0m\0\0\0\xe\0\x41\0\x45\0T\0i\0t\0l\0\x65\0\0\0\n\0\0\0\x6\0\x61\0n\0y)
</code></pre>

---

## Post #3 by @Paula_Moreno (2023-01-18 12:22 UTC)

<p>I tried to enter a new server and copy paste [severNodes] part in other Slicer.ini but I don’t see any repercution… I tried aswell just by modifying the first row  in server and no effect neither…<br>
It is strange becouse that configuration have to be saved some where becouse when I stop and then start again the docker container I see the new server … but it seems that is not in Slicer.ini…</p>

---

## Post #4 by @pieper (2023-01-18 23:39 UTC)

<p>Try outside of docker, just create and delete entries in the Query Servers list and see how the Slicer.ini files changes in the [ServerNodes] entry.  Maybe there’s some formatting issue when you are pasting or the right file is not being used in the docker version.</p>

---
