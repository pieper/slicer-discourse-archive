---
topic_id: 39582
title: "Save Scenes In The Same File"
date: 2024-10-08
url: https://discourse.slicer.org/t/39582
---

# Save Scenes in the same file

**Topic ID**: 39582
**Date**: 2024-10-08
**URL**: https://discourse.slicer.org/t/save-scenes-in-the-same-file/39582

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-10-08 11:49 UTC)

<p>Hi to everyone, me and my team are trying to save the scene in the same directory where we  have saved the scene before.</p>
<pre><code class="lang-auto">    def saveScene(self):    
        """
        Saves the current MRML scene to the specified directory.
    
        This method performs the following actions:
        - Displays a message indicating that the scene is being saved.
        - Saves the MRML scene to the directory specified by `self.saveResults_path` under the '2_Slicer' subdirectory.

        """
        slicer.app.processEvents()
        scenePath = os.path.join(self.saveResults_path, '2_Slicer')
        # Verify if the path exist
        if os.path.exists(scenePath):
            # Remove the path
            shutil.rmtree(scenePath)
            # Create the path
            os.makedirs(scenePath)
        else:
            print(f'El directorio {scenePath} no existe.')
        # Save the scene:
        slicer.mrmlScene.SaveScene(scenePath)     
</code></pre>
<p>The problem is that  <code>slicer.mrmlScene.SaveScene()</code> needs empty directories to save properly the data. In case the directory is not empty, the <code> slicer.mrmlScene.SaveScene()</code> apparently removes the files but don’t save anything.<br>
To satisfy this requirement we tried to remove the files before saving but it does not work…</p>
<p>Literally we are trying to emulate the slicer interface when it asks if we want to override the files and clicks in ‘Yes to all’. First:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3aeefa9a32dcad580cf5162b8851f62e0da7f7b.png" alt="Captura de pantalla 2024-10-08 134502" data-base62-sha1="pDygvtmaWQOj5sXKovxrjgEZx0v" width="628" height="329"></p>
<p>, to check all the nodes and data. And second:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b09f9cb53c3a806b1b8c07a3e97bbd300cdf34ee.png" alt="Captura de pantalla 2024-10-08 134522" data-base62-sha1="pcu08A89cWV7BDWANRj4j64PAE6" width="628" height="326"></p>
<p>, to override all the files needed.</p>
<p>My current Slicer version is : 5.7.0 -2024-10-05<br>
My OS version is: Windows 11</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @cpinter (2024-10-08 11:58 UTC)

<p>Have you checked the <code>slicer.mrmlScene.Commit</code> function?</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2024-10-08 12:06 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a>, yes we tried it, but this function (as far as we know) only saves the scene, not all the data contained in the nodes ( for example, centerline curve JSON, volume nodes NRRD, segmentations…)</p>
<p>slicer.mrmlScene.Commit() needs any specific args to override and save all the data?</p>

---

## Post #4 by @bserrano (2024-10-08 14:05 UTC)

<p>Hi all,</p>
<p>Indeed, we are facing problems with <code>slicer.mrmlScene.Commit</code>, <code>slicer.mrmlScene.SaveSceneToSlicerDataBundleDirectory</code>, and <code>slicer.mrmlScene.SaveScene()</code>.</p>
<p>It would be very useful to replicate the behavior of the Ctrl+S shortcut with an overwrite function. Otherwise, we always need to create a new directory to save scenes, unnecessarily increasing the number of files and memory usage.</p>
<p>Does anyone have any ideas on how to achieve this?</p>

---
