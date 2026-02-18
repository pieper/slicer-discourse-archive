# Create a download button

**Topic ID**: 13772
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/create-a-download-button/13772

---

## Post #1 by @Hugo (2020-09-30 12:25 UTC)

<p>Hello everyone,</p>
<p>I would like to be able to create 3 buttons in my Slicer Jupiter kernel. One that will act just like “save as” (download to the desktop .nrrd files), next an upload button doing exactly like this line does:<br>
<strong>volume = slicer.util.loadVolume(‘Data/image.nrrd’)</strong> but letting the user to choose his .nrrd file.<br>
And a screenshot button that will capture the scene displayed.</p>
<p>Thanks in advance</p>
<p>Hugo</p>

---

## Post #2 by @pierrebusson (2020-10-12 08:47 UTC)

<p>Sorry I can’t help you, I’ve got the same problem</p>

---

## Post #3 by @lassoan (2020-10-12 15:09 UTC)

<p>You can use standard Jupyter widgets for file upload/download, as shown in “File upload/download” section in this example notebook: <a href="https://github.com/Slicer/SlicerNotebooks/blob/master/01_Data_loading_and_display.ipynb">https://github.com/Slicer/SlicerNotebooks/blob/master/01_Data_loading_and_display.ipynb</a></p>
<p>I’ve found that FileUpload widget is not reliable for large files (<a href="https://github.com/jupyter-xeus/xeus-python/issues/272">https://github.com/jupyter-xeus/xeus-python/issues/272</a>), so you either need to upload using Upload button in the main notebook list or try the script posted <a href="https://github.com/jupyter-xeus/xeus-python/issues/272">here</a> and if you find that it still does not work then add a note to that bug report.</p>

---
