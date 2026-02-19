---
topic_id: 2338
title: "Fatal Error Qmrmlnodecombobox H No Such File Or Directory"
date: 2018-03-16
url: https://discourse.slicer.org/t/2338
---

# Fatal error: qmrmlnodecombobox.h: No such file or directory

**Topic ID**: 2338
**Date**: 2018-03-16
**URL**: https://discourse.slicer.org/t/fatal-error-qmrmlnodecombobox-h-no-such-file-or-directory/2338

---

## Post #1 by @brhoom (2018-03-16 19:53 UTC)

<p>Dear all,</p>
<p>I think there is a bug related to the error in the title. I found there is still unanswered post <a href="http://slicer-devel-archive.65872.n3.nabble.com/slicer-trunk-not-compiling-td3664132.html" rel="nofollow noopener">here</a></p>
<p>It happens when I compile my extension in Linux (windows users don’t have this problem). I found out that in the source file that caused this error there is this line:</p>
<pre><code>  #include &lt;qmrmlnodecomboBox.h&gt;
</code></pre>
<p>and replacing it with this line solved the problem:</p>
<pre><code>  #include &lt;qMRMLNodeComboBox.h&gt;
</code></pre>
<p>It would be nice to fix this error in slicer source as I don’t know how.</p>
<p>Best!<br>
Ibraheem</p>

---

## Post #2 by @cpinter (2018-03-16 20:22 UTC)

<p>I couldn’t find this lower case include in the current Slicer code. If you’re using an old Slicer, please update to the latest (or at least 4.8.1 if you don’t want the nightly for some reason).</p>

---

## Post #3 by @brhoom (2018-03-16 20:25 UTC)

<p>my Slicer-build is the stable one 4.8.1. Do you think maybe the extension template is old?</p>

---

## Post #4 by @cpinter (2018-03-16 20:41 UTC)

<p>Sorry but I cannot any mention of the combobox in the <a href="https://github.com/Slicer/Slicer/tree/master/Extensions/Testing/LoadableExtensionTemplate/LoadableModuleTemplate">template</a>.</p>
<p>Can you please describe what you want to do in more detail?</p>

---

## Post #5 by @brhoom (2018-03-16 20:54 UTC)

<p>It is strange that I found it in the extension source code and it was correct.</p>
<p>In my extension there is  Resources/UI/ qSlicerBrhoomModuleWidget.ui</p>
<p>In this file there are these lines:</p>
<pre><code>    &lt;layout class="QVBoxLayout" name="verticalLayout"&gt;
        &lt;item&gt;
            &lt;widget class="ctkCollapsibleButton" name="CTKCollapsibleButton" native="true"&gt;
            .
            .
            .

                    &lt;item&gt;
                        &lt;widget class="qMRMLNodeComboBox" name="MRMLNodeComboBox_Model"&gt;
                            &lt;property name="nodeTypes"&gt;
                                &lt;stringlist&gt;
                                    &lt;string&gt;vtkMRMLModelNode&lt;/string&gt;
                                &lt;/stringlist&gt;
                            &lt;/property&gt;
                            &lt;property name="renameEnabled"&gt;
                                &lt;bool&gt;true&lt;/bool&gt;
                            &lt;/property&gt;
                            &lt;property name="removeEnabled"&gt;
                                &lt;bool&gt;false&lt;/bool&gt;
                            &lt;/property&gt;
                        &lt;/widget&gt;
                    &lt;/item&gt;
</code></pre>
<p>This is the only place I found it and it is correct. I think is related to the use of qt wrapping and cmake in slicer as the file ui_qSlicerBrhoomModuleWidget.h is generated after the build in the build folder and generates the mentioned error in my case.</p>

---

## Post #6 by @cpinter (2018-03-17 01:46 UTC)

<p>Yes it seems to be correct. If you do a clean build (delete binary folder, CMake, build), does the same error occur?</p>

---

## Post #7 by @brhoom (2018-03-17 16:14 UTC)

<p>Yes, the error happens with clean build as well. I also tested it in different Linux machines with different Slicer-build versions.</p>

---

## Post #8 by @lassoan (2018-03-17 16:44 UTC)

<p>Have you added the combobox using Qt designer or by manually editing the file in a text editor? If you use custom widgets then you have to add special declarations for them in the .ui file (Qt designer adds those automatically).</p>

---

## Post #9 by @brhoom (2018-03-17 18:03 UTC)

<p>It was added manually.<br>
What are these declaration?<br>
I tried to use the designer but I am not sure how to add the ctk and mrml libs to qt designer. I tried <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner" rel="nofollow noopener">this</a></p>
<p>In order to have the CTK and MRML widgets in Qt Designer, Qt Designer offers 2 options:</p>
<ul>
<li>the first (not detailed here) is to copy (or symlink) the CTK and MRML plugin libraries into %QT_DIR%/plugins/designer,</li>
<li>the second is to set the environment variable QT_PLUGIN_PATH to the directory Slicer-build/bin containing the subdirectory designer with the plugin libraries.   Note: Qt requires that the directory containing the designer plugins is named “designer”.</li>
</ul>
<p>Which files I need to copy? I run</p>
<pre><code>export QT_PLUGIN_PATH=~/SlicerDev-4.8.1/build/Slicer-build/bin/designer
~/SlicerDev-4.8.1/build/Slicer -- designer
but still I can't see the ctk or mrml widgets</code></pre>

---

## Post #10 by @lassoan (2018-03-17 18:10 UTC)

<p>I don’t think you need to export any environment variables. Just running <code>./Slicer --designer</code> (note there is no space before --) should work. What operating system do you use?</p>

---

## Post #11 by @brhoom (2018-03-17 18:40 UTC)

<p>I am using Ubuntu, with no space I get an error bash: ./Slicer–designer: No such file or directory</p>
<p>with space, the designer is opened but I don’t see the widgets. I checked in designer:<br>
Help-&gt;Plugins</p>
<p>there are  paths to my SlicerDev4.8.1/build/CTK-build/bin/designer/lib …</p>

---

## Post #12 by @lassoan (2018-03-17 18:58 UTC)

<p>I’m not sure why --designer is not available on Ubuntu, but it is just a convenience function and it is equivalent to <code>./Slicer --launch full/path/to/designer</code></p>

---

## Post #13 by @brhoom (2018-03-18 17:18 UTC)

<p>I had multiple Qt in my system so I think this is was the problem. I removed all the current Qt installed. Then:</p>
<pre><code>sudo apt install qt4-dev-tools
sudo apt install qt4-qtconfig 
sudo apt install libqtwebkit-dev
</code></pre>
<p>After that I rebuilt Slicer, redesigned the ui using ./Slicer --designer then rebuilt the extension. No more errors.</p>

---

## Post #14 by @Amir_Zolal (2021-01-07 15:54 UTC)

<p>So this is still alive in some extensions in 2021.</p>
<pre><code>/home/zolal/Slicerbuild/SlicerDRRGenerator-build/DRRGeneratorModule/ui_qSlicerDRRGeneratorModuleModuleWidget.h:22:10: fatal error: qmrmlnodecombobox.h: No such file or directory
   22 | #include &lt;qmrmlnodecombobox.h&gt;
      |          ^~~~~~~~~~~~~~~~~~~~~
compilation terminated.
</code></pre>
<p>Solved by replacing with qMRMLNodeComboBox.h</p>

---
