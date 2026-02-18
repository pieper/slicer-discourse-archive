# Disable Snapshot and Record push buttons in SequenceBrowserPlayWidget while recordning

**Topic ID**: 19711
**Date**: 2021-09-16
**URL**: https://discourse.slicer.org/t/disable-snapshot-and-record-push-buttons-in-sequencebrowserplaywidget-while-recordning/19711

---

## Post #1 by @Thibaut_Faller (2021-09-16 16:03 UTC)

<p>Hello,</p>
<p>I work on an application in which we use SequenceBrowserPlayWidget to browse sequences. We would like to disable Snapshot (pushButton_Snapshot) and Record (pushButton_VcrRecord) push buttons as we do not use them.<br>
However, in Modules/Loadable/Sequences/Widgets/qMRMLSequenceBrowserPlayWidget.cxx, these buttons are automatically set visible when a node is recording (L. 150-153).</p>
<p>Would it be possible to add a member variable (and the function to set it) to disable this behaviour ?</p>
<p>Thank you !</p>

---

## Post #2 by @lassoan (2021-09-17 00:51 UTC)

<p>The record&amp;snapshot buttons are automatically shown if recording is allowed for any of the sequence nodes. To disable recording for all sequences, you can call <code>sequenceBrowserNode.SetRecording(None, False)</code>.</p>

---

## Post #3 by @Thibaut_Faller (2021-09-17 07:37 UTC)

<p>Hello Andras,</p>
<p>Thank you very much Andras for your quick response !<br>
This command is, indeed, quite useful to disable recording for all sequences.</p>
<p>The point is, we are recording images, but the recording is not controlled through the SequenceBrowserPlayWidget. So, we need to have recording enabled for some sequences, but we would like not to show the recording and snapshot buttons meanwhile.</p>

---

## Post #4 by @lassoan (2021-09-17 13:48 UTC)

<p>Yes, you could add an extra property to the widget (recordingEnabled) that would be required to be set to true to make the record buttons visible (in addition to having recordable sequences). This flag would not be saved into MRML, applied to other widgets, just used by that single widget. If you need any help with getting started with this then let us know. If you send us a pull request then we’ll integrate your changes and maintain it in Slicer core.</p>

---

## Post #5 by @Thibaut_Faller (2021-09-17 14:03 UTC)

<p>Thank you ! I will try to make the corresponding changes; let you know if I need some help and send the pull request.</p>

---

## Post #6 by @Thibaut_Faller (2021-09-17 15:48 UTC)

<p>An option would be to add a member boolean variable to the class, initially set to true to allow enabling the buttons, with two methods to set and get the value.</p>
<pre><code class="lang-auto">if (m_activateButtons)
  {
    d-&gt;pushButton_VcrRecord-&gt;setVisible(recordingAllowed);
    d-&gt;pushButton_VcrRecord-&gt;setEnabled(!playbackActive);
    d-&gt;pushButton_Snapshot-&gt;setVisible(recordingAllowed);
    d-&gt;pushButton_Snapshot-&gt;setEnabled(!playbackActive &amp;&amp; !recordingActive);
  }
</code></pre>
<p>This member variable would be set in qMRMLSequenceBrowserPlayWidget.h.</p>
<p>What do you think about it ?</p>

---

## Post #7 by @lassoan (2021-09-17 20:15 UTC)

<p>Sounds good. A few tips:</p>
<ul>
<li>The member variable name has to be <code>recordingControlsVisible</code> (since there is already <code>setRecordingEnabled</code> method).</li>
<li>Make it a Qt property (by adding <code>Q_PROPERTY(bool recordingControlsVisible READ recordingControlsVisible WRITE setRecordingControlsVisible)</code>) so that you can enable/disable this property in Qt Designer.</li>
<li>Whenever the value is changed then make sure the buttons are immediately shown/hidden as applicable (by calling <code>updateWidgetFromMRML()</code>)</li>
<li>Change the logic in <code>updateWidgetFromMRML()</code> to make record&amp;snapshot buttons visible if <code>recordingAllowed &amp;&amp; d-&gt;recordingControlsVisible</code>
</li>
</ul>
<p>Thanks in advance, looking forward to getting your pull request.</p>

---

## Post #8 by @Thibaut_Faller (2021-09-20 15:26 UTC)

<p>Thank you very much Andras for your tips, they were very useful !</p>

---
