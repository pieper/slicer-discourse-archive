# I want to call api on close event of mainwindow

**Topic ID**: 30387
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/i-want-to-call-api-on-close-event-of-mainwindow/30387

---

## Post #1 by @ssv (2023-07-04 09:23 UTC)

<p>What i want is if multiple instance is opened only the last instance will call the delete machine api  , right now what happen is if i closr the app it get the count of running instance in memory that will give me wrong count if recently last app closed is still in memory</p>
<p>void qSlicerAppMainWindow::closeEvent(QCloseEvent* event)<br>
{<br>
Q_D(qSlicerAppMainWindow);</p>
<pre><code>// This is necessary because of a Qt bug on MacOS.
// (https://bugreports.qt.io/browse/QTBUG-43344).
// This flag prevents a second close event to be handled.
if (d-&gt;IsClosing)
{
    event-&gt;ignore();
    return;
}
d-&gt;IsClosing = true;

if (d-&gt;confirmCloseApplication())
{
    // Proceed with closing the application

    // Exit current module to leave it a chance to change the UI (e.g. layout)
    // before writing settings.
    d-&gt;ModuleSelectorToolBar-&gt;selectModule("");

    this-&gt;saveGUIState();
    event-&gt;accept();

    //delete api call based on running instance
    QTimer::singleShot(0, qApp, SLOT(closeAllWindows()));
    
}
else
{
    // Request is cancelled, application will not be closed
    event-&gt;ignore();
    d-&gt;IsClosing = false;
}
</code></pre>
<p>} can anyone tell me how i can achieve this ?</p>

---

## Post #2 by @ssv (2023-07-05 10:18 UTC)

<p>This was solved usin QSettings</p>

---
