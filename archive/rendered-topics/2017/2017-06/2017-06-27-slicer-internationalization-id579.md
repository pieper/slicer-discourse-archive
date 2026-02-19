---
topic_id: 579
title: "Slicer Internationalization"
date: 2017-06-27
url: https://discourse.slicer.org/t/579
---

# Slicer Internationalization

**Topic ID**: 579
**Date**: 2017-06-27
**URL**: https://discourse.slicer.org/t/slicer-internationalization/579

---

## Post #1 by @jcfr (2017-06-27 11:11 UTC)

<h2><a name="p-2246-overview-1" class="anchor" href="#p-2246-overview-1" aria-label="Heading link"></a>Overview</h2>
<p>Following conversation with <a class="mention" href="/u/marilola">@marilola</a> that took place during the 25th Slicer project week, I am summarizing here the current state of the Slicer internationalization framework.</p>
<p>Prior discussion and description of the I18N framework can be found here:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Labs/I18N" class="inline-onebox">Documentation/Labs/I18N - Slicer Wiki</a></li>
<li><a href="https://www.slicer.org/wiki/Slicer4:Internationalization_of_Slicer" class="inline-onebox">Slicer4:Internationalization of Slicer - Slicer Wiki</a></li>
</ul>
<h2><a name="p-2246-technology-2" class="anchor" href="#p-2246-technology-2" aria-label="Heading link"></a>Technology</h2>
<p>Since most of the user facing strings to translate are associated with user interface components implemented using Qt, we standardized on the internationalization framework offered by Qt.</p>
<p>Doing so will allow to:</p>
<ul>
<li>easily manage translation of strings found in Slicer code base and also the strings internally used by Qt widgets.</li>
<li>easily decouple code from translation.</li>
<li>make use of Qt linguist tooling to allow translator to easily provide translation</li>
</ul>
<p>Relevant Qt documentation:</p>
<ul>
<li>Overview: <a href="http://doc.qt.io/qt-4.8/internationalization.html">Qt4</a>, <a href="http://doc.qt.io/qt-5.9/internationalization.html">Qt5</a></li>
<li>Writing Source Code for Translation: <a href="http://doc.qt.io/qt-4.8/i18n-source-translation.html">Qt4</a>, <a href="http://doc.qt.io/qt-5.9/i18n-source-translation.html">Qt5</a></li>
<li>Qt Linguist Manual: <a href="http://doc.qt.io/qt-4/qtlinguist-index.html">Qt4</a>, <a href="http://doc.qt.io/qt-5/qtlinguist-index.html">Qt5</a></li>
<li>Support for layout direction. See <a href="http://doc.qt.io/qt-4.8/qapplication.html#layoutDirection-prop">here</a></li>
</ul>
<p>Considering that we actively working to use Qt5 in Slicer instead of Qt4, links for both are available.</p>
<p>Worth noting that Qt can also work with Localization Interchange File Format (XLIFF).</p>
<h2><a name="p-2246-enabling-the-framework-3" class="anchor" href="#p-2246-enabling-the-framework-3" aria-label="Heading link"></a>Enabling the framework</h2>
<p>Back in 2014, we added a CMake option named <code>Slicer_BUILD_I18N_SUPPORT</code> allowing to build Slicer with internationalization.</p>
<p>When enabled, the following happen:</p>
<ul>
<li>a combo box allowing to select current language will be available in the <strong>General settings</strong></li>
<li>if not already found, translation files for languages associated with <code>Slicer_LANGUAGES</code> variables are generated</li>
<li>if found, translation file associated with the current language are loaded</li>
<li>a new Internalization settings panel allowing to enable/disable internalization will be available</li>
</ul>
<h2><a name="p-2246-known-limitations-4" class="anchor" href="#p-2246-known-limitations-4" aria-label="Heading link"></a>Known limitations</h2>
<p>Because of limitation in VTK/ITK/teem associated with the handling of locals, internationalization was disabled.</p>
<p>To get the full context, consider reading:</p>
<ul>
<li><a href="http://slicer-devel.65872.n3.nabble.com/Re-Rounding-to-integer-tt4027985.html">http://slicer-devel.65872.n3.nabble.com/Re-Rounding-to-integer-tt4027985.html</a></li>
<li><a href="http://slicer-devel.65872.n3.nabble.com/Re-slicer-users-Slicer4-can-t-really-use-it-yet-td4028040.html">http://slicer-devel.65872.n3.nabble.com/Re-slicer-users-Slicer4-can-t-really-use-it-yet-td4028040.html</a></li>
<li><a href="http://slicer-users.65878.n3.nabble.com/Slicer4-DICOM-many-problems-td4025919.html">http://slicer-users.65878.n3.nabble.com/Slicer4-DICOM-many-problems-td4025919.html</a></li>
<li><a href="https://issues.slicer.org/view.php?id=3029" class="inline-onebox">Image spacing not read correctly in Slicer 4.2.2 · Issue #3029 · Slicer/Slicer · GitHub</a></li>
</ul>
<p>To mitigate the issue, we added the following to <code>qSlicerCoreApplication</code>:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/7914527ee7e2e434f1af98b95b17f64d3d668b57/Base/QTCore/qSlicerCoreApplication.cxx#L176-L189" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/7914527ee7e2e434f1af98b95b17f64d3d668b57/Base/QTCore/qSlicerCoreApplication.cxx#L176-L189</a></p>
<p>In order to re-enable internationalization, we should setup dashboard on machine with different languages are confirm images are properly read.</p>
<h2><a name="p-2246-re-generating-translation-files-5" class="anchor" href="#p-2246-re-generating-translation-files-5" aria-label="Heading link"></a>Re-generating translation files</h2>
<p>Once translation files exists, they can be re-generated (to capture changes in the UI) by enabling the CMake option <code>Slicer_UPDATE_TRANSLATION</code>.</p>
<h2><a name="p-2246-differences-between-ts-and-qm-files-6" class="anchor" href="#p-2246-differences-between-ts-and-qm-files-6" aria-label="Heading link"></a>Differences between TS and QM files</h2>
<h3><a name="p-2246-ts-files-7" class="anchor" href="#p-2246-ts-files-7" aria-label="Heading link"></a>TS files</h3>
<p>The TS file format is a simple human-readable XML format that can be used with version control systems if required</p>
<h3><a name="p-2246-qm-files-8" class="anchor" href="#p-2246-qm-files-8" aria-label="Heading link"></a>QM files</h3>
<p>Qt message QM files are generated at build time based on the translation files and are the files distributed with the application and loaded at runtime.</p>
<h2><a name="p-2246-slicer-internationalization-settings-9" class="anchor" href="#p-2246-slicer-internationalization-settings-9" aria-label="Heading link"></a>Slicer internationalization settings</h2>
<h3><a name="p-2246-general-settings-language-combo-box-10" class="anchor" href="#p-2246-general-settings-language-combo-box-10" aria-label="Heading link"></a>General settings: Language combo box</h3>
<p>A combo box allowing to select the current language is available under Edit → Settings → General.</p>
<p>See <a href="http://www.commontk.org/docs/html/classctkLanguageComboBox.html">http://www.commontk.org/docs/html/classctkLanguageComboBox.html</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19ab21ec2e15e323835bb76fc0de5fccf577b4c0.png" data-download-href="/uploads/short-url/3F4AmoXkMeLZ6o0JbyT4SAwIhbO.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19ab21ec2e15e323835bb76fc0de5fccf577b4c0.png" alt="" data-base62-sha1="3F4AmoXkMeLZ6o0JbyT4SAwIhbO" role="presentation" width="120" height="106"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">120×106 4.76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-2246-internationalization-settings-enabledisable-i18n-support-11" class="anchor" href="#p-2246-internationalization-settings-enabledisable-i18n-support-11" aria-label="Heading link"></a>Internationalization settings: Enable/disable I18N support</h3>
<p>Settings panel is available under Edit → Settings → Internationalization</p>
<p>Corresponding settings key used in Slicer settings file is <code>Internationalization/Enabled</code>.</p>
<p>The panel is implemented in  <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/qSlicerSettingsInternationalizationPanel.cxx">qSlicerSettingsInternationalizationPanel.cxx</a> and  <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/Resources/UI/qSlicerSettingsInternationalizationPanel.ui">qSlicerSettingsInternationalizationPanel.ui</a></p>
<h3><a name="p-2246-suggested-improvements-12" class="anchor" href="#p-2246-suggested-improvements-12" aria-label="Heading link"></a>Suggested improvements</h3>
<ul>
<li>language combobox could be moved in the Internationalization settings panel</li>
</ul>
<h2><a name="p-2246-build-infrastructure-13" class="anchor" href="#p-2246-build-infrastructure-13" aria-label="Heading link"></a>Build infrastructure</h2>
<p>Slicer build system includes the <a href="https://github.com/Slicer/Slicer/blob/master/CMake/SlicerMacroTranslation.cmake">SlicerMacroTranslation.cmake</a> CMake module.</p>
<p>This module provides the following CMake macro:</p>
<pre><code class="lang-auto">SlicerMacroTranslation(
  QM_OUTPUT_DIR_VAR
  TS_DIR
  TS_BASEFILENAME
  SRCS
  UI_SRCS
  TS_LANGUAGES
  QM_OUTPUT_FILES_VAR
)

# Parameters :
#
#   SRCS ..................: All sources witch need to be translated
#
#   UI_SRCS ...............: All ui_sources witch need to be translated
#
#   TS_DIR.................: Path to the TS files
#
#   TS_BASEFILENAME........: Name of the librairi
#
#   TS_LANGUAGES...........: Variable with all the languages
#
#   QM_OUTPUT_DIR_VAR .....: Translation's dirs generated by the macro
#
#   QM_OUTPUT_FILES_VAR....: Translation's files generated by the macro
#
</code></pre>
<p>The macro is not used directly by module developers, instead it is indirectly used in more general Slicer CMake function used to build Slicer components (Slicer Application, Slicer library, Slicer modules, …).</p>
<p>Currently it is used in the following macros:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/CMake/SlicerMacroBuildBaseQtLibrary.cmake">SlicerMacroBuildBaseQtLibrary.cmake</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/653f37d1d1f2c1db4603b5f1adca5edea3a2e11f/CMake/SlicerMacroBuildApplication.cmake">SlicerMacroBuildApplication.cmake</a></li>
</ul>
<h3><a name="p-2246-suggested-improvements-14" class="anchor" href="#p-2246-suggested-improvements-14" aria-label="Heading link"></a>Suggested improvements</h3>
<ul>
<li>Update macro used to build Slicer modules (e.g <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/CMake/SlicerMacroBuildModuleQtLibrary.cmake">SlicerMacroBuildModuleQtLibrary.cmake</a>) to also make use of <code>SlicerMacroTranslation</code></li>
</ul>

---

## Post #2 by @mhalle (2017-06-27 13:41 UTC)

<p>Thanks for the update and summary <a class="mention" href="/u/jcfr">@jcfr</a>.</p>
<p>As I have mentioned before, I think a more modest, related, but distinct task is coming up with a “how-to”/“best practices” document for module internationalization. It would be interesting to know how much we can avoid the more risky internationalization of the underlying I18N-naive C++ code and make more progress by first focusing on the UI, Qt, and Python pieces of modules.</p>
<p>Having a good, solid best practices guide for module development is critically important for maintaining code quality and consistency across the extended Slicer code base.  Internationalization is clearly a forward-looking piece of that picture that we would like every module developer to embrace.  It’s just happens to be a bonus that I18N is likely a more tractable problem at the module level than addressing and testing it across all of Slicer.</p>
<p>–Mike</p>

---

## Post #3 by @lassoan (2017-06-27 20:48 UTC)

<p>Is there any solution for translation of CLIs?</p>
<p>Can/do we want to handle translation without first switching to Unicode? (Qt and Python has excellent Unicode support and ITK, VTK has some Unicode support, too)</p>
<p>Do we want to do only translation or other internationalization aspects (number format, date&amp;time format, units, etc.) are in the scope as well?</p>

---

## Post #4 by @Ted_Chen (2017-10-17 03:03 UTC)

<p>Thanks for the information <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I have compiled the slicer with  Slicer_BUILD_I18N_SUPPORT enabled in cmake gui but cannot see the language combobox and international panel in general settings, do I miss something to make it works?</p>
<p>cmake settings<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03e0dc683cb14232968081de6fbeb722af3fd7fa.png" alt="image" data-base62-sha1="yjc4QerMpOKUsOfLFoaGwcuSwi" width="632" height="334"></p>
<p>I also check with visual studo, seems Slicer_BUILD_I18N_SUPPORT is not really enable in codes?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a347e62ef25d7ebf035a7aa9e5119a68e497dd02.png" data-download-href="/uploads/short-url/nirRZMd15Es3rdRXV1P4d4FQGf8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a347e62ef25d7ebf035a7aa9e5119a68e497dd02.png" alt="image" data-base62-sha1="nirRZMd15Es3rdRXV1P4d4FQGf8" width="690" height="334" data-dominant-color="262727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×340 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ted</p>

---

## Post #5 by @jcfr (2019-01-30 12:31 UTC)

<p>To move forward, would be nice to review <a href="https://github.com/Slicer/SlicerGitSVNArchive/pull/898">https://github.com/Slicer/SlicerGitSVNArchive/pull/898</a> and integrate the code allowing to streamline i18n support for python module.</p>
<p>Cc: <a class="mention" href="/u/carlos-luque">@carlos-luque</a></p>

---
