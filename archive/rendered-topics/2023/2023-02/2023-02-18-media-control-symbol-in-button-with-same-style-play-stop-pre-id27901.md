---
topic_id: 27901
title: "Media Control Symbol In Button With Same Style Play Stop Pre"
date: 2023-02-18
url: https://discourse.slicer.org/t/27901
---

# Media control symbol in button with same style - Play Stop Previous and Next

**Topic ID**: 27901
**Date**: 2023-02-18
**URL**: https://discourse.slicer.org/t/media-control-symbol-in-button-with-same-style-play-stop-previous-and-next/27901

---

## Post #1 by @haphantran (2023-02-18 04:55 UTC)

<p>Hi guys,<br>
I’m trying to build an extension that can control the images play back. I made the UI with media control symbol and the timeline slider.<br>
I got one problem where I can’t find the set of unicode symbol that render with same color.<br>
here is the code for play button<br>
self.playSequenceButton = qt.QPushButton(u"\u25B6")<br>
Stop: “\u25A0”<br>
Previous: \u23EA - Next: \u23E9 (I also tried \u23ED and \u23EE<br>
The Play and stop render as gray, and I can change their color by setStyleSheet(“color: red”) function.<br>
But the previous and next button render as blue back ground characters as attached, and I can’t change their color using setStyleSheet. It’s like the characters are color fixed.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8332f3f29ecbb28d0c572f917f52309123d8771.png" alt="image" data-base62-sha1="qhvw3eLtia7rGxNigUlk5ym8WuB" width="677" height="114"><br>
I tried to use png icon, but it will required more work. Just curious if we can just use Unicode character for this.</p>

---

## Post #2 by @jamesobutler (2023-02-18 14:36 UTC)

<p>Hi <a class="mention" href="/u/haphantran">@haphantran</a>, Slicer already has a media control widget for playing sequences that is currently used in the Sequence browser module. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html" class="inline-onebox" rel="noopener nofollow ugc">Sequences — 3D Slicer documentation</a></p>
<p>Did you not like that design of the sequence control widget? Could you provide feedback to how you might change it so it could be improved for all Slicer users?</p>
<p>I’ve not attempted Unicode symbols before but have used the Slicer sequence playback widget. Here is where the icons are defined for the Slicer playback widget. <a href="https://github.com/Slicer/Slicer/tree/v5.2.1/Modules/Loadable/Sequences/Widgets/Resources/Icons" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Loadable/Sequences/Widgets/Resources/Icons at v5.2.1 · Slicer/Slicer · GitHub</a></p>

---
