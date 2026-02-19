---
topic_id: 20017
title: "Slicer Wont Start"
date: 2021-10-05
url: https://discourse.slicer.org/t/20017
---

# Slicer won't start

**Topic ID**: 20017
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/slicer-wont-start/20017

---

## Post #1 by @Nayra_Pumar (2021-10-05 12:15 UTC)

<p>Happened to me before and solved with a windows reinstall (something I’d like to avoid right now).<br>
There are no log files and no Windows event log entry. When I start Slicer nothing happens. But if I log in with a different user, it starts flawlessly.<br>
I’ve already tried desinstalling and reinstalling Slicer, but doesn’t help.</p>

---

## Post #2 by @RafaelPalomar (2021-10-05 12:21 UTC)

<p><a class="mention" href="/u/nayra_pumar">@Nayra_Pumar</a>, maybe there is a problem in the settings? does it help if you start Slicer with the <code>--disable-settings</code> flag?</p>

---

## Post #3 by @lassoan (2021-10-05 16:04 UTC)

<p>This page may also help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start" class="inline-onebox">Get Help — 3D Slicer documentation</a></p>

---

## Post #4 by @lassoan (2021-10-05 17:33 UTC)

<p>I’ve also noted that the very latest Slicer (Slicer 4.13.0-2021-10-04) does not start due to <em>Qt5MultimediaWidgets.dll was not found</em> error. This is caused by a change that we made yesterday and we’ll fix this error in tomorrow’s release. Until then the installer that created from the day before can be downloaded from <a href="https://download.slicer.org/?date=2021-10-04">here</a>.</p>

---
