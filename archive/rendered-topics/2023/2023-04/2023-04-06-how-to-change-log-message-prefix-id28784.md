---
topic_id: 28784
title: "How To Change Log Message Prefix"
date: 2023-04-06
url: https://discourse.slicer.org/t/28784
---

# How to change log message prefix

**Topic ID**: 28784
**Date**: 2023-04-06
**URL**: https://discourse.slicer.org/t/how-to-change-log-message-prefix/28784

---

## Post #1 by @ksidis (2023-04-06 14:55 UTC)

<p>Hello all,</p>
<p>I am struggling with adding a common prefix in all logged messages. For example by changing the SlicerApplicationLogHandler, the following messages get a prefix:</p>
<pre><code class="lang-auto">[DEBUG][Python] 06.04.2023 14:05:12 [Python] (C:\ProgramData\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - **PREFIX: - User:** Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 06.04.2023 14:05:12 [Python] (C:\ProgramData\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - **PREFIX: - User:** Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 06.04.2023 14:05:12 [Python] (C:\ProgramData\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - **PREFIX: - User**: Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 06.04.2023 14:05:13 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>
<p>while the rest don’t:</p>
<pre><code class="lang-auto">[CRITICAL][Qt] 06.04.2023 14:40:48 [] (unknown:0) - setting value to 2
[CRITICAL][Qt] 06.04.2023 14:40:48 [] (unknown:0) - setting value to 3
[DEBUG][Qt] 06.04.2023 14:40:48 [] (unknown:0) - GET responses report for study: 1.3.6.1.4.1.14519.5.2.1.4320.7015.858893877330075891307460974850
1 images transferred, and
0 images transferred with warning, and
0 images transfers failed
[CRITICAL][Qt] 06.04.2023 14:40:48 [] (unknown:0) - setting value to 100
[DEBUG][Qt] 06.04.2023 14:40:48 [] (unknown:0) - Retrieve success
[CRITICAL][Stream] 06.04.2023 14:40:53 [] (unknown:0) - I: Releasing Association
</code></pre>
<p>How can I add a prefix or change the logging format of entries like the last ones?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2023-04-06 18:22 UTC)

<p>Formatting of messages written to the log file is done in the <a href="https://github.com/commontk/CTK/blob/master/Libs/Core/ctkErrorLogAbstractModel.h">error log model object</a>. The format is configurable:</p>
<pre><code class="lang-python">&gt;&gt;&gt; slicer.app.errorLogModel().fileLoggingPattern
'[%{level}][%{origin}] %{timestamp} [%{category}] (%{file}:%{line}) - %{msg}'

&gt;&gt;&gt; slicer.app.errorLogModel().fileLoggingPattern = "someprefix " + slicer.app.errorLogModel().fileLoggingPattern
</code></pre>
<p>Formatting of messages displayed in the Python console is implemented <a href="https://github.com/Slicer/Slicer/blob/7d0388b90811acc8a8e6bb40e5deb952726aface/Base/QTGUI/qSlicerApplication.cxx#L1434-L1472">here</a>. The format is very simple (<code>[&lt;origin&gt;] &lt;message&gt;</code>) and not configurable.</p>

---

## Post #3 by @ksidis (2023-04-12 13:52 UTC)

<p>Thank you so much for this <a class="mention" href="/u/lassoan">@lassoan</a>! It was very helpful. On a similar topic: is there an easy way to preprocess all messages before posted by the logger? e.g. I would. like to remove a special character or compact mult-line messages in one single line.</p>
<p>Thank you again for your time.</p>

---

## Post #4 by @lassoan (2023-04-12 16:24 UTC)

<p>To make more sophisticated editing to the messages before logging, you would need to customize the ctkErrorLogAbstractModel class.</p>
<p>Normally the application log is used for diagnostics and so the format and content of the messages should not matter much. Are you trying to use the log file for communication? There are lots of mechanisms in Slicer for interprocess communication that are more robust and has better performance than using the application log file.</p>

---

## Post #5 by @ksidis (2023-04-13 08:23 UTC)

<p>Hello Andras, thank you for your prompt response.</p>
<p>In order to satisfy our Track Trace &amp; Audit requirements I need to produce a single log line with information about the username and the individual image assets that were accessed using the Slicer application. The reason I need this information to be in a single line is that we are using some AWS lambda functions to process the logs line by line.</p>
<p>With your help I have managed to inject the username in every log line by changing just the startup script in python. However in the following log line presenting the GET report there are some carriage returns.</p>
<pre><code class="lang-auto">Administrator/IMG-12345 [DEBUG][Qt] 12.04.2023 11:00:30 [] (unknown:0) - GET responses report for study: 1.3.6.1.4.1.14519.5.2.1.4320.7015.294146073179367570423565184119
69 images transferred, and
0 images transferred with warning, and
0 images transfers failed
</code></pre>
<p>Thus I was looking for an easy way to pre-process that message before posting it to the logger.<br>
Alternatively, is there a way to change this message while it is generated? Could you point me to the right direction?</p>

---

## Post #6 by @lassoan (2023-04-13 12:00 UTC)

<p>There is no reason for logging this specific message in multiple lines, so we can change this easily.</p>
<p>Optionally replacing the newlines with some other character sequence would be no problem either, that could be a useful feature in general.</p>
<p>However, for your specific need, I think the best solution would be to create a separate audit log file where you would log all the relevant information and only the relevant information. You could achieve that by connecting your custom logging function to the CTK DICOM retrieve class. We can add any signals to CTK or Slicer that are needed for this.</p>

---

## Post #7 by @ksidis (2023-04-13 13:55 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for all the suggestions.</p>
<p>I guess since this project is still at the POC stage we could wait for a next release that would address that multiple lines issue, provided it is easy to fix. Can we create a ticket/story so we can have visibility on when this is addressed?</p>
<p>The rest of the suggestions sound also good but maybe more appropriate for a later stage.</p>

---
