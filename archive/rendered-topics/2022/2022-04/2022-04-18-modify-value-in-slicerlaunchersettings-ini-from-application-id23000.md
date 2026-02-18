# Modify value in `SlicerLauncherSettings.ini` from application

**Topic ID**: 23000
**Date**: 2022-04-18
**URL**: https://discourse.slicer.org/t/modify-value-in-slicerlaunchersettings-ini-from-application/23000

---

## Post #1 by @keri (2022-04-18 13:28 UTC)

<p>Hi,</p>
<p>Is it possible to set value to <code>SlicerLauncherSettings.ini</code> from application?<br>
For example:</p>
<pre><code class="lang-auto">slicer.app.setEnvironmentVariable("SLICER_HOME", "/my/path")
</code></pre>
<p>will modify <code>SLICER_HOME</code> env var but it doesn’t change the value in <code>SlicerLauncherSettings.ini</code>.</p>

---

## Post #2 by @lassoan (2022-04-18 16:41 UTC)

<p>You can access/modify the SlicerLauncherSettings.ini file at multiple levels:</p>
<ul>
<li>as any other text file, using standard file read/write functions</li>
<li>as a Qt settings file (<code>QSettings settings(fileName, QSettings::IniFormat);</code>)</li>
<li>as a CTK launcher settings ini file, using CTKApLauncherLib’s ctkAppLauncherSettings class</li>
</ul>

---

## Post #3 by @keri (2022-04-19 14:24 UTC)

<p>Thank you for the response,</p>
<p>First I tried to use <code>ctkAppLauncherSettings</code> as it is done in <a href="https://github.com/Slicer/Slicer/blob/cad13ad1f57ffd25f75e3c59c6e32394056b3fad/Base/QTCore/qSlicerCoreApplication.cxx#L255-L261" rel="noopener nofollow ugc">qSlicerCoreApplication</a> but then I understood that <code>ctkAppLauncherSettings</code> doesn’t privide API to overwrite values in file. To do that I would need to work with settings as with usual textual file.</p>
<p>I decided to use <code>userSettings</code> (QSettings class) for now:</p>
<pre><code class="lang-auto">QSettings* settings = app-&gt;userSettings();
settings-&gt;setValue("MyKey", "FALSE");
</code></pre>

---

## Post #4 by @keri (2022-04-19 14:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="23000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>as a Qt settings file ( <code>QSettings settings(fileName, QSettings::IniFormat);</code> )</p>
</blockquote>
</aside>
<p>By the way I don’t know should this work or not but it doesn’t:</p>
<pre data-code-wrap="python"><code class="lang-python">settings=qt.QSettings(slicer.app.launcherSettingsFilePath, 1)  # 1 is QSettings::IniFormat I could not find this enum in python
</code></pre>
<p>I expected that <code>settings</code> retrieves information from <code>slicer.app.launcherSettingsFilePath</code> <strong>.ini</strong> file and I could work with it as with QSettings.</p>
<p>But <code>settings.allKeys()</code> returns empty list.</p>
<p>And <code>settings.fileName()</code> shows<br>
<code>'/home/kerim/.config/home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/ColadaLauncherSettings.ini/1.conf'</code></p>
<p>While <code>slicer.app.launcherSettingsFilePath</code> returns<br>
<code>'/home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../bin/ColadaLauncherSettings.ini'</code></p>
<p>As you can see <code>settings.fileName()</code> adds <code>/1.conf</code> at the end.<br>
Am I misunderstanding something?</p>
<p>As I understand there is a constructor <a href="https://doc.qt.io/qt-5/qsettings.html" rel="noopener nofollow ugc">QSettings(const QString &amp; <em>fileName</em> , QSettings::Format <em>format</em> , QObject * <em>parent</em> = nullptr)</a> but it works somehow strange</p>

---

## Post #5 by @lassoan (2022-04-25 12:49 UTC)

<p>It works for me perfectly if I use the proper Qt constant:</p>
<pre><code class="lang-python">&gt;&gt;&gt; settings=qt.QSettings(slicer.app.launcherSettingsFilePath, qt.QSettings.IniFormat)
&gt;&gt;&gt; settings.allKeys()
('Application/arguments', 'Application/name', 'Application/organizationDomain', 'Application/organizationName', 'Application/path', 'Application/revision', 'Environment/additionalPathVariables', 'EnvironmentVariables/ITK_AUTOLOAD_PATH', 'EnvironmentVariables/PIP_REQUIRE_VIRTUALENV', 'EnvironmentVariables/PYTHONHOME', 'EnvironmentVariables/PYTHONNOUSERSITE', ...
</code></pre>

---

## Post #6 by @keri (2022-04-25 12:56 UTC)

<p>Thank you very much!</p>
<p>Your approach works<br>
I didn’t know that there might be a difference between passing the value <code>1</code> and <code>qt.QSettings.IniFormat</code>.</p>

---
