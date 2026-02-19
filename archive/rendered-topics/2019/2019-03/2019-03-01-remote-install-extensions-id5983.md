---
topic_id: 5983
title: "Remote Install Extensions"
date: 2019-03-01
url: https://discourse.slicer.org/t/5983
---

# Remote install extensions?

**Topic ID**: 5983
**Date**: 2019-03-01
**URL**: https://discourse.slicer.org/t/remote-install-extensions/5983

---

## Post #1 by @nagy.attila (2019-03-01 13:10 UTC)

<p>Hi all,</p>
<p>we maintain several classrooms with Slicer installs. It is okay, I can do it remotely from a command line, in “silent mode”, I’ve been doing it for years <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>But… is there a way to install extensions remotely? By “remotely” I mean either silent installers or any scripted method that’s output can be supressed.</p>
<p>It would be great if I could both install (/upgrade in this case) Slicer itself and also add extensions somehow from a command line.<br>
At the moment there are no extensions installed on the machines just bare Slicer (and some example datasets)<br>
We use wpkg (<a href="http://wpkg.org" rel="nofollow noopener">wpkg.org</a>)</p>
<p>Many thanks,<br>
Attila</p>

---

## Post #2 by @pieper (2019-03-01 13:36 UTC)

<p>Hi Attila -</p>
<p>Probably the easiest is to follow the steps here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_create_a_custom_Slicer_version_with_selected_extensions_pre-installed.3F" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_create_a_custom_Slicer_version_with_selected_extensions_pre-installed.3F</a></p>
<p>You can make a slicer folder yourself that has all the extensions you want, and then just copy that to all the computers.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @nagy.attila (2019-03-01 22:57 UTC)

<p>Hi Steve,</p>
<p>thanks for the pointer!<br>
So if I understand correctly, this will act as a “portable” install.</p>
<p>But now we have a system-wide (“normal”) install. So would it work if I would upgrade the current Slicer version with the installer, and then overwrite the installed one with the same but with the extensions?</p>
<p>This may seem a bit complicated but this way I don’t have to remove that system-wide install and then re-add as a portable one.<br>
Because there are several users and also the directory structure is strictly regulated.<br>
So if I would have to add as a portable I would need to download it at least 4 times per machine: 3 users + a teacher account.</p>
<p>Okay, I will look into this once I get to the classroom computers <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Attila</p>

---

## Post #4 by @pieper (2019-03-01 23:18 UTC)

<p>Yep, that should work - just overwrite the system installed Slicer with the new one that includes the desired extensions in the appropriate directory and you should be all set.  Good luck and have a great weekend!</p>

---
