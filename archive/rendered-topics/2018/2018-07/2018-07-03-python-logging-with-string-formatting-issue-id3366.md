---
topic_id: 3366
title: "Python Logging With String Formatting Issue"
date: 2018-07-03
url: https://discourse.slicer.org/t/3366
---

# Python logging with string formatting issue

**Topic ID**: 3366
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/python-logging-with-string-formatting-issue/3366

---

## Post #1 by @jamesobutler (2018-07-03 17:58 UTC)

<p>I’m having issues when writing a debug log message in python while also using the % string formatting operator. It gets interpreted correctly at the info log level, but not at the debug level.</p>
<p>Any idea why the behavior is like this?</p>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 03.07.2018 13:07:23 [] (unknown:0) - Python console user input: a="string"
[DEBUG][Python] 03.07.2018 13:07:36 [Python] (&lt;console&gt;:1) - This is a %s
[DEBUG][Qt] 03.07.2018 13:07:36 [] (unknown:0) - Python console user input: logging.debug("This is a %s", a)
[INFO][Python] 03.07.2018 13:07:40 [Python] (&lt;console&gt;:1) - This is a %s
[DEBUG][Qt] 03.07.2018 13:07:40 [] (unknown:0) - Python console user input: logging.info("This is a %s", a)
[INFO][Stream] 03.07.2018 13:07:40 [] (unknown:0) - This is a string
</code></pre>
<p>There is similar python debug logging in the Slicer repo within <a href="https://github.com/Slicer/Slicer/blob/0d281895d52ca92fb52f2cedbff544f2b87ebc29/Utilities/Scripts/SlicerWizard/ExtensionWizard.py" rel="nofollow noopener">ExtensionWizard.py</a> where I would expect this same issue to happen.</p>

---

## Post #2 by @lassoan (2018-07-03 19:02 UTC)

<p>All parameters are forwarded to the log formatter. It is just a coincidence that info formatter uses the additional argument. If you want to log a string then the proper syntax is:</p>
<pre><code>a="something"
logging.debug("This is a %s" % a)
logging.info("This is a %s" % a)</code></pre>

---

## Post #3 by @jamesobutler (2018-07-03 19:21 UTC)

<p>I’m using pylint as one of my linters and it explicitly warned to do it as:</p>
<pre data-code-wrap="python"><code class="lang-python">logging.debug("This is a %s", a)
</code></pre>
<p>instead of</p>
<pre data-code-wrap="python"><code class="lang-python">logging.debug("This is a %s" % a)
</code></pre>
<blockquote>
<p><strong>logging-not-lazy (W1201)</strong>:<br>
Specify string format arguments as logging function parameters Used when a logging statement has a call form of “logging.(format_string % (format_args…))”. Such calls should leave string interpolation to the logging method itself and be written “logging.(format_string, format_args…)” so that the program may avoid incurring the cost of the interpolation in those cases in which no message will be logged. For more, see <a href="http://www.python.org/dev/peps/pep-0282/" class="inline-onebox" rel="noopener nofollow ugc">PEP 282 – A Logging System | peps.python.org</a>.</p>
</blockquote>

---

## Post #4 by @lassoan (2018-07-03 19:44 UTC)

<p>I see, thanks for the additional information. It’s true that by passing the format specifier and arguments separately, string formatting can be avoided when not needed. Probably we can make the debug formatter to use all the arguments, too. I’ll have a look.</p>

---

## Post #5 by @jamesobutler (2018-07-03 19:55 UTC)

<p>Thanks for looking into this Andras!</p>
<p>I’ve started to actually look at what my linters say to make sure I’m following python standards better.</p>

---

## Post #6 by @lassoan (2018-07-03 20:33 UTC)

<p>Please have a look at <code>slicerqt.py</code>. It uses <code>SlicerApplicationLogHandler</code> class to create a CTK log entry from a Python log record.</p>
<p>By changing the implementation to something like this, the log will contain the full formatted string:</p>
<pre><code>#-----------------------------------------------------------------------------
class SlicerApplicationLogHandler(logging.Handler):
  """
  Writes logging records to Slicer application log.
  """
  def __init__(self):
    logging.Handler.__init__(self)
    if hasattr(ctk, 'ctkErrorLogLevel'):
      self.pythonToCtkLevelConverter = {
        logging.DEBUG : ctk.ctkErrorLogLevel.Debug,
        logging.INFO : ctk.ctkErrorLogLevel.Info,
        logging.WARNING : ctk.ctkErrorLogLevel.Warning,
        logging.ERROR : ctk.ctkErrorLogLevel.Error }
    self.origin = "Python"
    self.category = "Python"
  def emit(self, record):
    try:
      msg = self.format(record)
      context = ctk.ctkErrorLogContext()
      context.setCategory(self.category)
      context.setLine(record.lineno)
      context.setFile(record.pathname)
      context.setFunction(record.funcName)
      context.setMessage(msg)
      threadId = "{0}({1})".format(record.threadName, record.thread)
      slicer.app.errorLogModel().addEntry(qt.QDateTime.currentDateTime(), threadId,
        self.pythonToCtkLevelConverter[record.levelno], self.origin, context, msg)
    except:
      self.handleError(record)
</code></pre>
<p>However, this would log the log level, file name, and line number in the log message.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Could you check how the formatting can be changed to avoid adding log level, file name, and line number in the message?</p>

---

## Post #7 by @jamesobutler (2018-07-03 21:13 UTC)

<p>Sure, I will definitely take a look <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #8 by @jamesobutler (2018-07-03 22:43 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
So with your update I can confirm it logs the full formatted string at the debug level:</p>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 03.07.2018 18:30:40 [] (unknown:0) - Python console user input: a="string"
[DEBUG][Python] 03.07.2018 18:30:51 [Python] (&lt;console&gt;:1) - DEBUG: This is a string (&lt;console&gt;:1)
[DEBUG][Qt] 03.07.2018 18:30:51 [] (unknown:0) - Python console user input: logging.debug("This is a %s", a)
[INFO][Python] 03.07.2018 18:30:55 [Python] (&lt;console&gt;:1) - INFO: This is a string (&lt;console&gt;:1)
[DEBUG][Qt] 03.07.2018 18:30:55 [] (unknown:0) - Python console user input: logging.info("This is a %s", a)
[INFO][Stream] 03.07.2018 18:30:55 [] (unknown:0) - This is a string
</code></pre>
<p>The log formats with log level, file name and line number because of <a href="https://github.com/Slicer/Slicer/blob/3ea26dae3e461899f8ecf51ec7ae02f7bab10d15/Base/Python/slicer/slicerqt.py#L72" rel="nofollow noopener">here</a> in slicerqt.py.  Simplifying that line to the following below appears to remove those extra elements in the message.  Is this the appropriate solution?</p>
<pre><code class="lang-python">applicationLogHandler.setFormatter(logging.Formatter('%(message)s'))
</code></pre>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 03.07.2018 18:22:55 [] (unknown:0) - Python console user input: a="string"
[DEBUG][Python] 03.07.2018 18:23:07 [Python] (&lt;console&gt;:1) - This is a string
[DEBUG][Qt] 03.07.2018 18:23:07 [] (unknown:0) - Python console user input: logging.debug("This is a %s", a)
[INFO][Python] 03.07.2018 18:23:11 [Python] (&lt;console&gt;:1) - This is a string
[DEBUG][Qt] 03.07.2018 18:23:11 [] (unknown:0) - Python console user input: logging.info("This is a %s", a)
[INFO][Stream] 03.07.2018 18:23:11 [] (unknown:0) - This is a string
</code></pre>

---

## Post #9 by @lassoan (2023-04-06 18:10 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-change-log-message-prefix/28784">How to change log message prefix</a></p>

---
