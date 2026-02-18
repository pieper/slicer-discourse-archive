# C++ and C locale are not equal after creation of qSlicerApplication

**Topic ID**: 33718
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/c-and-c-locale-are-not-equal-after-creation-of-qslicerapplication/33718

---

## Post #1 by @aymeric.chataigner (2024-01-10 13:24 UTC)

<p>Hi,</p>
<p>I added some code in Main.cxx to check the values of C and C++ locale settings:</p>
<pre data-code-wrap="c++"><code class="lang-c++">int SlicerAppMain(int argc, char* argv[])
{
  typedef qSlicerAppMainWindow SlicerMainWindowType;
  typedef qSlicerStyle SlicerAppStyle;

  std::cout &lt;&lt; "C locale: " &lt;&lt; std::setlocale(LC_ALL, nullptr) &lt;&lt; std::endl;
  std::cout &lt;&lt; "Cpp locale: " &lt;&lt; std::locale().name() &lt;&lt; std::endl;

  qSlicerApplicationHelper::preInitializeApplication(argv[0], new SlicerAppStyle);

  std::cout &lt;&lt; "C locale: " &lt;&lt; std::setlocale(LC_ALL, nullptr) &lt;&lt; std::endl;
  std::cout &lt;&lt; "Cpp locale: " &lt;&lt; std::locale().name() &lt;&lt; std::endl;

  qSlicerApplication app(argc, argv);
  if (app.returnCode() != -1)
    {
    return app.returnCode();
    }

  std::cout &lt;&lt; "C locale: " &lt;&lt; std::setlocale(LC_ALL, nullptr) &lt;&lt; std::endl;
  std::cout &lt;&lt; "Cpp locale: " &lt;&lt; std::locale().name() &lt;&lt; std::endl;
</code></pre>
<p>On my PC it prints:<br>
C locale: C<br>
Cpp locale: C<br>
C locale: C<br>
Cpp locale: C<br>
C locale: LC_CTYPE=en_US.UTF-8;LC_NUMERIC=C;LC_TIME=C;LC_COLLATE=C;LC_MONETARY=C;LC_MESSAGES=C;LC_PAPER=C;LC_NAME=C;LC_ADDRESS=C;LC_TELEPHONE=C;LC_MEASUREMENT=C;LC_IDENTIFICATION=C<br>
Cpp locale: C</p>
<p>So qSlicerApplication construction set LC_CTYPe to en_US.UTF-8<br>
It is done during Python initialization line 426 in  Python-3.9.10/Python/pylifecycle.c</p>
<p>This difference between C and C++ locale can lead to issues if C++ locale settings are saved/restored using std::global as it is done in vtkDataReader::OpenVTKFile and vtkDataReader::CloseVTKFile:</p>
<p>Before open &amp; save calls:<br>
C locale: LC_CTYPE=en_US.UTF-8;LC_NUMERIC=C;LC_TIME=C;LC_COLLATE=C;LC_MONETARY=C;LC_MESSAGES=C;LC_PAPER=C;LC_NAME=C;LC_ADDRESS=C;LC_TELEPHONE=C;LC_MEASUREMENT=C;LC_IDENTIFICATION=C<br>
Cpp locale: C</p>
<p>After open &amp; save calls:<br>
C locale: C<br>
Cpp locale: C</p>
<p>Because std::global set C++ locale AND C locale.</p>
<p>So I have several questions:</p>
<ul>
<li>Is it ok to let python initialization set LC_CTYPE?
<ul>
<li>If yes: should we synchronize C++ locale using this line after qSlicerApplication creation: std::locale::global(std::locale(std::setlocale(LC_ALL, nullptr))); (this is what we did in our custom app)</li>
<li>If no: so C and C++ locale should always be C, is it not a problem if users type special characters as input ?</li>
</ul>
</li>
</ul>
<p>Regards</p>

---

## Post #2 by @aymeric.chataigner (2024-01-15 13:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have any comment ?</p>

---
