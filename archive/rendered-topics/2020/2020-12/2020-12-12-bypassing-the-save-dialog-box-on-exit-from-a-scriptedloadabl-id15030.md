# Bypassing the save dialog box on exit from a ScriptedLoadableModule

**Topic ID**: 15030
**Date**: 2020-12-12
**URL**: https://discourse.slicer.org/t/bypassing-the-save-dialog-box-on-exit-from-a-scriptedloadablemodule/15030

---

## Post #1 by @hina-shah (2020-12-12 21:54 UTC)

<p>This might be trivial, but I couldn’t find a solution. So am reaching out.</p>
<p>I am writing a small extension that is supposed to help with labeling some images and segmentation editing in Python. The extension loads the data, and saves its own files on exit. The example at <a href="https://github.com/lassoan/SlicerSimpleWorkflows/blob/master/QuickSegment">QuickSegment</a> helped me to remove all the unnecessary Slicer details that I do not want. However, when I exit the Slicer window, it pops up the dialog box for confirmation on the scene modifications and hence saving the changes. Is it possible to not pop that dialog up? What would be the corresponding event?</p>
<p>I’m handling the relevant data export on the widget’s exit (i.e. <code>exit()</code>), so I don’t need that dialog to pop up again and confuse my users.</p>
<p>Thank you!</p>

---

## Post #2 by @jamesobutler (2020-12-13 00:27 UTC)

<p>Hi Hina!</p>
<p>I did some work to override the Slicer drag and drop behavior to do something different that I posted about at</p>
<aside class="quote quote-modified" data-post="4" data-topic="9382">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/add-drag-and-drop-import-to-slicelet/9382/4">Add Drag and drop import to slicelet?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I came across this thread as I was experimenting adding a custom drop action for a custom app using only python.  With the code below I was able to redefine the drop action to execute what I put in dropEvent when I dropped a file path instead of the Slicer default of opening the Add Data Dialog. 
class MyClass(qt.QWidget):
    def eventFilter(self, object, event):
        """
        Custom event filter for Slicer Main Window.

        Inputs: Object (QObject), Event (QEvent)
        """
       …
  </blockquote>
</aside>

<p>You should be able to use this method for overriding the QMainWindow <code>closeEvent</code> to do your own set of actions instead of the Slicer unsaved changes warning.</p>
<p>Here is some <a href="https://github.com/Slicer/Slicer/blob/39fe1598d1fa2e5dcf51a712cdcdcfe7c0ce446e/Modules/Scripted/DICOM/DICOM.py#L479-L525" rel="noopener nofollow ugc">example code</a> that <a class="mention" href="/u/lassoan">@lassoan</a> then used in the DICOM module to override the regular Slicer drag and drop event behavior.</p>

---

## Post #3 by @lassoan (2020-12-13 00:49 UTC)

<p>Excellent idea <a class="mention" href="/u/jamesobutler">@jamesobutler</a>! I’ve added an example for this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Override_application_close_behavior">here</a>.</p>
<p>Note that there is also a solution to override the default save scene behavior (e.g., save/export data automatically, without asking anything from the user), as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Override_default_scene_save_dialog">here</a>.</p>

---

## Post #4 by @hina-shah (2020-12-14 14:15 UTC)

<p>Hi James!<br>
Thanks for the idea! I’ll need to dig into it a little bit deeper, but right now I just modified the behavior of the default dialog box like <a class="mention" href="/u/lassoan">@lassoan</a> suggested.</p>
<p>Hope you’re doing well!</p>

---

## Post #5 by @hina-shah (2020-12-14 14:16 UTC)

<p>Thanks!</p>
<p>I think to completely bypass that dialog, the event trigger should be used. For me just overriding the default save scene behavior works for now!</p>
<p>Thank you for your suggestion!</p>

---

## Post #6 by @lassoan (2020-12-14 14:40 UTC)

<p>I gave complete examples for both customizing the application close behavior (using event filter) and creating a custom save dialog (by adding a new file dialog class). For an optimal user experience probably you want to customize both.</p>

---

## Post #7 by @fbordignon (2021-09-28 17:38 UTC)

<p>Updated links to the script repository<br>
1 - <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-application-close-behavior" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>2- <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-default-scene-save-dialog" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>Thanks for the snippets Andras!</p>

---

## Post #8 by @fbordignon (2021-12-02 17:58 UTC)

<p>I’ve encountered a side effect of filtering the close event, as there are operations that Slicer performs on close that if we accept the event and return True will not be performed such as saving the window geometry when “Save user interface size and position on exit” option on Settings&gt;Appearance.<br>
If the user saves the scene, there is no problem returning False, because Slicer will close as it detects that the scene is not modified. If the user cancel exiting, it is ok also, because we can reject. But when closing without saving, the user wants to close but the developer needs to allow Slicer to perform its on close events minus opening the close dialog again.</p>

---

## Post #9 by @lassoan (2021-12-02 18:21 UTC)

<p>We have recently exposed <code>slicer.util.mainWindow().saveGUIState()</code> method to support this use case. Is there anything else that you would like to do in your custom exit handler?</p>

---

## Post #10 by @fbordignon (2021-12-02 18:42 UTC)

<p>Great, that would solve for us. Thanks!</p>
<p>Would checking the event state on the <a href="https://github.com/Slicer/Slicer/blob/d7870308744af4d98100c26712afa70b3baa78d3/Base/QTApp/qSlicerMainWindow.cxx#L1100" rel="noopener nofollow ugc">closeEvent method</a> like this is desirable?</p>
<p><code>  if (event-&gt;isAccepted() || d-&gt;confirmCloseApplication())</code></p>
<p>This way if the close event is already accepted, slicer performs the normal on close routines.</p>

---

## Post #11 by @lassoan (2021-12-02 18:51 UTC)

<p>I haven’t checked the code but based on what you describe it sounds like setting the accepted state could be an acceptable solution.</p>

---
