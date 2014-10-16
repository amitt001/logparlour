logparlour
==========

IRC Log Cleaner. Beautiful IRC logs.

Removes all the unnecessary server messages like others joining/leaving, changing nicks etc. Focus on you important messages. Your local messages from server like you join the channel or changing the password etc are not removed.

**Reduced the size of 30.3 MB of logs to 23.4 MB:** 23% disk usage reduction.

**How to use?**

Run it like this::

    python3 logparlour.py -l /destination/of/your/log_file

    python3 logparlour.py -d /destination/of/your/log_directory

or::

    ./logparlour.py -l /destination/of/your/log_file

    ./logparlour.py -l /destination/of/your/log_directory


Instead of -l,-d use -h for help.

**INFO:**

ONLY TESTED WITH XCHAT(should work with hexchat also). 
Can be tried with others also. *Your original logs are never modified. It creates a new file/directory with name "HotnameOfYourLogFile" or "HownameOfYourDirectory" and your original logs remain untouched*.
