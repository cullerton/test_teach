Background
==========

In this lesson, we start with some motivation and end with an important concept.

--------------
Event Tracking
--------------

Logging allows your application to track events.

This can help you see how your application is actually used.

Event tracking can be used for reporting and to debug problems.

-------------
Variable Data
-------------

Your log statements can contain variable information from the application,
including error messages and exceptions from third parties.

--------------
Logging Levels
--------------

Some of the messages you log will be informational only, while others could tell
you about critical problems with your application.

Most logging systems allow you to differentiate between levels of importance,
and tag your log messages with a specific level.

Python logging levels:
----------------------

======== =========================================================
Level    What
======== =========================================================
Debug    Detailed, for diagnosing problems
Info     Things are working as expected
Warning  Something unexpected happened, application working
Error    Application could not perform function, but still running
Critical Serious error, application may not be working
======== =========================================================

- Logging levels are **ordered**. As an example, if you set the logging level to Info:

    - You see levels Info, Warning, Error and Critical.
    - You do not see level Debug.

- Python defaults to level **Warning**.

----------
Question 1
----------

By default, which logging levels will you see displayed in a Python application?
