# Play Macro, Error

**Topic ID**: 2649
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/play-macro-error/2649

---

## Post #1 by @tbest (2018-04-20 14:04 UTC)

<p>Hello everybody,</p>
<p>I am trying to setup macros on a MacOS 10.13.4 using Slicer 4.8.1. As a first try I recorded a macro that only changes from the “Welcome to Slicer” module to the “Segment Editor” module.</p>
<p>After recording the macro I closed Slicer, started it again and tried to play the macro. Unfortunately, when playing it it does not work. Instead I get an error message and 3 “critical” log messages. I cannot interpret those and would be happy to find out what the problem is!</p>
<p>Thank you very much for your help!</p>
<blockquote>
<p><strong>Here the 3 Log Messages:</strong></p>
<blockquote>
<ol>
<li><code>objc[2372]: Class FIFinderSyncExtensionHost is implemented in both /System/Library/PrivateFrameworks/FinderKit.framework/Versions/A/FinderKit (0x7fffaddc0c90) and /System/Library/PrivateFrameworks/FileProvider.framework/OverrideBundles/FinderSyncCollaborationFileProviderOverride.bundle/Contents/MacOS/FinderSyncCollaborationFileProviderOverride (0x14dfe9cd8). One of the two will be used. Which one is undefined.</code></li>
</ol>
<p>2.<code> "/Users/.../Desktop/test_macro.xml" invalid xml file for qtTesting !</code></p>
<ol start="3">
<li><code>Error XSDError in file:///Users/.../Desktop/test_macro.xml, at line 12, column 138: Element event contains unknown attribute eventType.</code></li>
</ol>
</blockquote>
</blockquote>
<blockquote>
<p><strong>Additional Information:</strong></p>
<p>A.) Only after starting 3D Slicer I already get several error messages in the log message which do not seem to affect the program otherwise.</p>
<p>B.) XML code:<br>
see next post</p>
</blockquote>

---

## Post #2 by @tbest (2018-04-20 14:10 UTC)

<p><strong>xml code:</strong></p>
<blockquote>
<pre><code>&lt;?xml version="1.0"?&gt;
&lt;QtTesting&gt;
    &lt;settings&gt;
        &lt;name widget="qApp" command="applicationName" arguments="Slicer"/&gt;
        &lt;version widget="qApp" command="applicationVersion" arguments="4.8.1"/&gt;
        &lt;geometry widget="MainWindow" command="mainWindowGeometry" arguments="01d9d0cb000100000000000000000017000009ff000005290000000000000000fffffffefffffffe000000000200"/&gt;
        &lt;state widget="MainWindow" command="mainWindowState" arguments="000000ff00000000fd0000000200000000000003700000047cfc0200000001fb0000001e00500061006e0065006c0044006f0063006b005700690064006700650074010000005e0000047c0000015000ffffff0000000300000a00000000d8fc0100000001fb0000002e0050007900740068006f006e0043006f006e0073006f006c00650044006f0063006b005700690064006700650074000000000000000a000000004d00ffffff0000068a0000047c00000004000000040000000800000008fc00000001000000020000000800000016004d00610069006e0054006f006f006c0042006100720100000000ffffffff00000000000000000000002a004d006f00640075006c006500530065006c006500630074006f00720054006f006f006c00420061007201000001100000025600000000000000000000001a004d006f00640075006c00650054006f006f006c0042006100720100000366ffffffff00000000000000000000001600560069006500770054006f006f006c004200610072010000062100000062000000000000000000000020004d006f007500730065004d006f006400650054006f006f006c00420061007201000006830000006c00000000000000000000001c00430061007000740075007200650054006f006f006c00420061007200000006ef0000015000000000000000000000001c00560069006500770065007200730054006f006f006c00420061007201000006ef0000007200000000000000000000001a004400690061006c006f00670054006f006f006c0042006100720100000761000001580000000000000000"/&gt;
        &lt;appsetting widget="qSlicerModulesMenu" command="currentModule" arguments="Welcome"/&gt;
        &lt;appsetting widget="qSlicerLayoutManager" command="layout" arguments="29"/&gt;
    &lt;/settings&gt;
    &lt;events&gt;
        &lt;event widget="qSlicerAppMainWindow/ModuleSelectorToolBar/1ctkMenuComboBox0" command="show_popup" arguments="true" eventType="0"/&gt;
        &lt;event widget="qSlicerAppMainWindow/ModuleSelectorToolBar/1ctkMenuComboBox0" command="show_popup" arguments="false" eventType="0"/&gt;
        &lt;event widget="qSlicerAppMainWindow/ModuleSelectorToolBar/1ctkMenuComboBox0" command="triggered" arguments="Segment Editor" eventType="0"/&gt;
        &lt;event widget="qSlicerAppMainWindow/ModuleSelectorToolBar/1ctkMenuComboBox0" command="triggered" arguments="Segment Editor" eventType="0"/&gt;
        &lt;event widget="qSlicerAppMainWindow/ModuleSelectorToolBar/1ctkMenuComboBox0" command="triggered" arguments="Segment Editor" eventType="0"/&gt;
    &lt;/events&gt;
&lt;/QtTesting&gt;
</code></pre>
</blockquote>

---

## Post #3 by @lassoan (2018-04-20 21:14 UTC)

<p>Macro recording is kind of obsolete since we have extensive support for Python scripting. <code>slicer.util.</code>… methods contain many utility functions, including switching between modules. Check out the script repository and all the Python tests for automation examples.</p>
<p><a href="http://slicer.readthedocs.io/en/latest/developer_guide/api.html#python" class="onebox" target="_blank">http://slicer.readthedocs.io/en/latest/developer_guide/api.html#python</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #4 by @YH3DS (2018-07-26 14:59 UTC)

<p>Hello,<br>
I planned to use the macro ability to record some kind of User scenarios (without any additional writings). Is there any tool that can be equivalent to the macro recordings (which fits perfectly this purpose) ?</p>
<p>Thanks a lot</p>

---

## Post #5 by @Bartolomejka (2019-06-27 08:22 UTC)

<p>In my case the deletion of all occurrences of:  eventType=“0” in the macro xml-file helped.</p>

---

## Post #6 by @Bartolomejka (2019-06-27 08:50 UTC)

<p>Additionally, in my case of visualizing BSpline composite transform (splitting it, inversion of transforms and setting a new order of transforms), there were also other problems, so I had to delete some of the nonsense events in the xml file. And it was necessary to avoid any usage of treeview during recording of the macro.</p>

---
