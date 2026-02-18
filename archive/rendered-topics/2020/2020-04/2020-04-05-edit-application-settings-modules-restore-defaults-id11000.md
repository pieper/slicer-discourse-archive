# Edit/Application Settings/Modules/Restore defaults

**Topic ID**: 11000
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/edit-application-settings-modules-restore-defaults/11000

---

## Post #1 by @MarcDeSantJoan (2020-04-05 17:06 UTC)

<p>Hello, I tryed to customize the initial menu, and I would like to restore defaluts and there is not work. I unninstall program, delete Temp…and allways shows my customized menu. I don’t know what to do to solve the problem.</p>

---

## Post #2 by @lassoan (2020-04-05 17:18 UTC)

<p>Could you describe what did you do exactly?<br>
You may need to delete your <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location">application settings files</a> (Slicer.ini and/or Slicer-NNN.ini).</p>

---

## Post #3 by @MarcDeSantJoan (2020-04-07 08:38 UTC)

<p>Good morning Andras,</p>
<p>Finally I select all checkbox manually and the problem is solved. My be usefull to improve a new “select all” checkbox.</p>
<p>I see for example that the “Crop Volume” checkbox is not able to select alone. What other menus are required to select to allow “Crop Volume” module?</p>
<p>Thank you very much</p>
<p>Marc</p>
<p>Enviat des del meu iPhone</p>

---

## Post #4 by @lassoan (2020-04-09 00:07 UTC)

<p>Deselecting modules is an advanced feature and it is expected that you know the modules that you disable and what the consequences are.</p>
<p>Many modules depend on other modules. For example Crop Volume module depends on Volumes and ResampleScalarVectorDWIVolume modules. You can get that information by typing this into the Python console: <code>slicer.modules.cropvolume.dependencies</code></p>

---
