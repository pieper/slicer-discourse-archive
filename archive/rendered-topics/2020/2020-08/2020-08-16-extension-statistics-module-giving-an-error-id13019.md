# Extension statistics module giving an error

**Topic ID**: 13019
**Date**: 2020-08-16
**URL**: https://discourse.slicer.org/t/extension-statistics-module-giving-an-error/13019

---

## Post #1 by @muratmaga (2020-08-16 03:07 UTC)

<p>This is r29263 on windows.</p>
<p>I am trying to compile SlicerMorph download statistics and after a certain of data retrieval, I get this error:</p>
<pre><code>Retrieving package info 223/828 for extension SlicerMorph: rev 28498 downloaded 5 times (midas itemid: 459971)
Retrieving package info 224/828 for extension SlicerMorph: rev 28498 downloaded 6 times (midas itemid: 460008)
Traceback (most recent call last):
  File "C:/Users/murat/AppData/Roaming/NA-MIC/Extensions-29263/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 153, in onApplyButton
    release_downloads = self.logic.getExtensionDownloadStats(extensionName)
  File "C:/Users/murat/AppData/Roaming/NA-MIC/Extensions-29263/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 615, in getExtensionDownloadStats
    rev_downloads = self.getExtensionSlicerRevisionAndDownloads(url, extensionName)
  File "C:/Users/murat/AppData/Roaming/NA-MIC/Extensions-29263/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 552, in getExtensionSlicerRevisionAndDownloads
    item_rev_downloads[itemid] = [self.getItemById(url, itemid)['download'], self.getExtensionById(url, extensionid)['slicer_revision']]
  File "C:/Users/murat/AppData/Roaming/NA-MIC/Extensions-29263/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 527, in getItemById
    return self._call_midas_url(url, data)
  File "C:/Users/murat/AppData/Roaming/NA-MIC/Extensions-29263/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 489, in _call_midas_url
    response_data = response_dict['data']
KeyError: 'data'
</code></pre>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @lassoan (2020-08-16 14:31 UTC)

<p>This error was caused by getting an unexpected answer from the server. I’ve tried 2-3 times and could not reproduce the error. Nevertheless, I’ve pushed a <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/commit/ae975a1249e59d1de0022b7e788a8ff076240821">fix</a> to retry a request a few times if it fails for any reason (previously, it was only retried if the request failed, not when the response content was invalid).</p>

---
