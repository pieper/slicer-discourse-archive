---
topic_id: 18780
title: "Create Pdf Report For Custom Application"
date: 2021-07-17
url: https://discourse.slicer.org/t/18780
---

# Create pdf report for custom application

**Topic ID**: 18780
**Date**: 2021-07-17
**URL**: https://discourse.slicer.org/t/create-pdf-report-for-custom-application/18780

---

## Post #1 by @mau_igna_06 (2021-07-17 12:12 UTC)

<p>Hi. I’m making an application for PedicleScrewPlanning. After the screws positions and orientations has been selected it is useful to make a pdf report showing the different views for each screw for the surgeon to use in the surgery in case it’s needed.</p>
<p>I tried two different approaches without the desired results:<br>
First approach:</p>
<pre><code class="lang-auto">desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
pdfPath = os.path.join(desktopPath, "reportWithoutStyle.pdf")

printer = qt.QPrinter(qt.QPrinter.PrinterResolution)
printer.setOutputFormat(qt.QPrinter.PdfFormat)
printer.setPaperSize(qt.QPrinter.A4)
marginleft = 20
marginright = 20
margintop = 20
marginbottom = 20
printer.setPageMargins(marginleft, marginright, margintop, marginbottom, qt.QPrinter.Millimeter)
printer.setOutputFileName(pdfPath)

doc = qt.QTextDocument()

_stylesheet = """
&lt;style&gt;
  td, th {
    text-align:center; 
  }
  table {
    border: 1px solid black;
  }
&lt;/style&gt;
"""

_html = """
		&lt;html&gt;
      &lt;head&gt;
        &lt;title&gt;PediGuide surgical planning report&lt;/title&gt;
      &lt;/head&gt;  
      &lt;body&gt;
        &lt;table&gt;
        &lt;tr&gt;
          &lt;td&gt;Patient name:&lt;/td&gt;
          &lt;td&gt;&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
          &lt;td&gt;Patient ID:&lt;/td&gt;
          &lt;td&gt;&lt;/td&gt;
        &lt;/tr&gt;
        &lt;/table&gt;
      &lt;/body&gt;
    &lt;/html&gt;
"""

doc.setDefaultStyleSheet(_stylesheet)
doc.setHtml(_html)
doc.setPageSize(qt.QSizeF(printer.pageRect().size()))  # hide the page number
doc.print(printer)
</code></pre>
<p>The problem with this approach is that it ignores stylesheets so the result is not good looking (e.g. the border of the table is not shown) and I cannot set <code>@media print</code> styles. However this approach does set the specified margins.</p>
<p>Here is an example of the result:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gofile.io/d/2osNsE">
  <header class="source">
      <img src="https://gofile.io/dist/img/favicon16.png" class="site-icon" width="16" height="16">

      <a href="https://gofile.io/d/2osNsE" target="_blank" rel="noopener nofollow ugc">gofile.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://gofile.io/d/2osNsE" target="_blank" rel="noopener nofollow ugc">Gofile - Free file sharing and storage platform</a></h3>

  <p>Gofile is a free file sharing and storage platform. You can store and share data of all types. There is no limit and everything is free.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Second approach:</p>
<pre><code class="lang-auto">desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
pdfPath2 = os.path.join(desktopPath, "reportWithoutMargins.pdf")

ww = slicer.qSlicerWebWidget()
_html = """
  &lt;html&gt;
    &lt;style&gt;
      table {
        border: 1px solid black;
      }
    &lt;/style&gt;
    &lt;head&gt;
      &lt;title&gt;PediGuide surgical planning report&lt;/title&gt;
    &lt;/head&gt;  
    &lt;body&gt;
      &lt;table style=border: 1px solid black&gt;
      &lt;tr&gt;
        &lt;td&gt;Patient name:&lt;/td&gt;
        &lt;td&gt;&lt;/td&gt;
      &lt;/tr&gt;
      &lt;tr&gt;
        &lt;td&gt;Patient ID:&lt;/td&gt;
        &lt;td&gt;&lt;/td&gt;
      &lt;/tr&gt;
      &lt;/table&gt;
    &lt;/body&gt;
  &lt;/html&gt;
"""
ww.setHtml(_html)
ww.printToPdf(pdfPath2)
</code></pre>
<p>This approach does use styles but does not have margins which makes it not printer-friendly.</p>
<p>Here is an example of the result:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gofile.io/d/WZCJbG">
  <header class="source">
      <img src="https://gofile.io/dist/img/favicon16.png" class="site-icon" width="16" height="16">

      <a href="https://gofile.io/d/WZCJbG" target="_blank" rel="noopener nofollow ugc">gofile.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://gofile.io/d/WZCJbG" target="_blank" rel="noopener nofollow ugc">Gofile - Free file sharing and storage platform</a></h3>

  <p>Gofile is a free file sharing and storage platform. You can store and share data of all types. There is no limit and everything is free.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Could someone help to improve one of these two approaches? Thank you</p>
<p>PS: please have in mind that the report will probably have more than 1 page so some html tricks to have margins only on the first page will not work.</p>

---

## Post #2 by @lassoan (2021-08-12 05:53 UTC)

<p>HTML is a decidedly medium-independent document format, it has no notion of pages or margins. If you want to create professional-looking PDF reports then you can use PDF creator toolkits instead, such as <a href="https://github.com/PyFPDF/fpdf2">fpdf2</a> or <a href="https://www.reportlab.com/dev/opensource/">reportlab</a>.</p>

---

## Post #3 by @mau_igna_06 (2024-06-13 23:14 UTC)

<p>How is the current situation?</p>
<p>The pdf needs to show data (titles and images) based on a table template</p>

---
