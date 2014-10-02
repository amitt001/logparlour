logparlour
==========

IRC Log Cleaner. Make your IRC logs beautiful. 

Removes all the unnecessary server messages like others joining/leaving, changing nicks etc. Your local messages from server like you join the channel or changing the password etc are not removed.

**How to use?**

Run it like this::

    python3 logparlour.py -l /destination/of/your/log_file

or::

    ./logparlour.py -l /destination/of/your/log_file

Instead of -l use -h for help.

INFO:

ONLY TESTED WITH XCHAT. But your logs will never be modified. It creates a new file with name "HotnameOfYourLogFile" and your original logs remain untouched.
