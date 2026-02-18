# Feature Flags for custom Python slicer extensions

**Topic ID**: 22502
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/feature-flags-for-custom-python-slicer-extensions/22502

---

## Post #1 by @Srijeet_Chatterjee (2022-03-14 16:20 UTC)

<p>Hello everyone,</p>
<p>I want to develop a feature flag (possibly in a config file) such that it helps to enable/disable several functionalities of the extension(shows/hides a tab completely from the user). Can anyone please help me with possible ideas to implement this or best approaches to handle this problem.</p>
<p>Would the launcher.ini file be a good starting point? Is there a way I can add a key, or there is something even simplier already existing.</p>
<p>Thanks and Best regards,<br>
Srijeet</p>

---

## Post #2 by @lassoan (2022-03-14 16:36 UTC)

<p>You can store application settings persistently in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location"><code>Slicer.ini</code> file</a> via the <code>slicer.app.userSettings()</code> object. See <a href="https://doc.qt.io/qt-5/qsettings.html">QSettings documentation</a> for API description and <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted">Slicer scripted modules</a> for usage examples.</p>

---

## Post #3 by @Srijeet_Chatterjee (2022-03-28 09:22 UTC)

<p>Thanks a lot, could set the flags via the .ini files and the slicer.app documentation helped along with <a href="https://docs.python.org/3/library/configparser.html" class="inline-onebox" rel="noopener nofollow ugc">configparser — Configuration file parser — Python 3.10.4 documentation</a></p>

---
