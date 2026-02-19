---
topic_id: 24058
title: "Lungctanalyzer In Macos Missing Os Startfile"
date: 2022-06-27
url: https://discourse.slicer.org/t/24058
---

# LungCTAnalyzer in macOS: missing os.startfile

**Topic ID**: 24058
**Date**: 2022-06-27
**URL**: https://discourse.slicer.org/t/lungctanalyzer-in-macos-missing-os-startfile/24058

---

## Post #1 by @ashipde (2022-06-27 01:22 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>In LungCTAnalyzer 2.49 in Slicer 5.0.2 in macOS 12.4 with Python 3.9.10, when generating PDF report: report is generated in LungCTAnalyzerReports but Python Interactor shows</p>
<pre><code class="lang-auto">modules/LungCTAnalyzer.py", line 843, in onCreatePDFReportButton
    os.startfile(reportPath.replace('/', '\\'))
AttributeError: module 'os' has no attribute 'startfile'
</code></pre>
<p>Seems os.startfile is Windows-specific, and macOS may need <code>os.system("open myFile")</code>.</p>
<p>The error is not seen with <em>Create CSV file</em> (after PDF report generation).</p>

---

## Post #2 by @pieper (2022-06-27 16:42 UTC)

<p>Yes, that call is windows specific.  It would be great if someone could contribute a fix to generalize the code.</p>
<p><a href="https://docs.python.org/3/library/os.html#os.startfile" class="onebox" target="_blank" rel="noopener">https://docs.python.org/3/library/os.html#os.startfile</a></p>

---

## Post #3 by @rbumm (2022-06-27 17:48 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> .</p>
<p>I think this <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/commit/0a841f004673e96219e24cd75ccc5d4d6f29df00">fixed the problem</a>.</p>
<p><a class="mention" href="/u/ashipde">@ashipde</a> could you</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22a94f7b1d924bf0820239df34a5e996b21df25a.png" alt="image" data-base62-sha1="4WCYL9EF1izYlXrdLmDS4no1Adc" width="136" height="33"></p>
<p>in the extension manager tomorrow or the day after that, then update the Lung CT Analyzer and test again? I have no MAC or Linux available …</p>
<p>Thank you.</p>

---

## Post #4 by @ashipde (2022-06-27 23:18 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thank you for the quick-fix. The error does not appear, but on macOS, the generated PDF report is not opened automatically, which I believe is the intent. In error messages I see: The file <code>/\Users\ashipde\Documents\LungCTAnalyzerReports\[redacted].pdf</code> does not exist. But the file exists… seems backslashes are the issue (macOS/Unix using forward ones unlike Windows).</p>

---

## Post #5 by @rbumm (2022-06-28 08:34 UTC)

<p>Thank you. I <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/commit/9d7567e9f9a1a56905106f9bc2e29a1abb1166ea">removed the backslash generation</a> in the PDF path for macOS and Linux.<br>
Could you test again?</p>

---

## Post #6 by @ashipde (2022-06-28 21:42 UTC)

<p>The file-missing error is gone after the latest fix. Interactor window shows <code>Starting '/Users/ashipde/Documents/LungCTAnalyzerReports/[redacted].pdf' ...</code>. However, the PDF file does not auto-open. My system Python opens the file in PDF viewer app with <code>subprocess.call(['open', '/Users/ashipde/Documents/LungCTAnalyzerReports/[redacted].pdf'])</code>, so not sure what may be the issue.</p>

---

## Post #7 by @lassoan (2022-06-28 23:30 UTC)

<p><a class="mention" href="/u/ashipde">@ashipde</a> please try if the same subprocess call opens the file in Slicer’s Python interactor. If it does not work then you may need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-external-process-in-startup-environment">use the startup environment</a>.</p>

---

## Post #8 by @ashipde (2022-06-29 01:19 UTC)

<p>My mistake. The report file <em>does</em> auto-open as expected with the latest GitHub download of the extension. May be my extension uninstall/re-install was not done properly by me.</p>

---
