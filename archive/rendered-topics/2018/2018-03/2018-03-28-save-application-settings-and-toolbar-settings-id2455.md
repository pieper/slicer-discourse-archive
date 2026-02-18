# Save application settings and toolbar settings

**Topic ID**: 2455
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/save-application-settings-and-toolbar-settings/2455

---

## Post #1 by @MancaZerovnik (2018-03-28 11:34 UTC)

<p>Hello,<br>
is it possible to save the state of toolbar and application settings (specifically I am interested in favorites Modules), so that some other user would be able to load those settings and get the same toolbar view as me?</p>

---

## Post #2 by @lassoan (2018-03-28 13:41 UTC)

<p>These information are saved in to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DirectoryStructure#API">Slicer.ini</a> file. You can copy it over to another user’s profile. However, there are probably some other folder names that you don’t want to move over (such as temporary file folders, which may not be accessible to the other user).</p>
<p>You can also write a short Python script that the user can copy-paste into the Python console (or create batch file that is executed by Slicer) to update settings. For example, to add “Segmentations” module to the favorite module list:</p>
<pre><code>favoriteModules = list(qt.QSettings().value('Modules/FavoriteModules'))
if 'Segmentations' not in favoriteModules and slicer.util.confirmOkCancelDisplay("Update favorite modules list and restart the application?"):
  favoriteModules.append('Segmentations')
  favoriteModules = qt.QSettings().setValue('Modules/FavoriteModules', favoriteModules)
  slicer.app.restart()</code></pre>

---
