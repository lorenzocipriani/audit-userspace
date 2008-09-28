Starting Test 1, iterate...
auid=4294967295
interp auid=unset
auid=848
interp auid=unknown(848)
auid=848
interp auid=unknown(848)
Test 1 Done

Starting Test 2, walk events, records, and fields...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN (LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=848 (unknown(848))

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=188 (setxattr)
        success=yes (yes)
        exit=0 (0)
        a0=7fffffa9a9f0 (7fffffa9a9f0)
        a1=3958d11333 (3958d11333)
        a2=5131f0 (5131f0)
        a3=20 (20)
        items=1 (1)
        pid=2027 (2027)
        auid=848 (unknown(848))
        uid=0 (root)
        gid=0 (root)
        euid=0 (root)
        suid=0 (root)
        fsuid=0 (root)
        egid=0 (root)
        sgid=0 (root)
        fsgid=0 (root)
        tty=tty3 (tty3)
        comm="login" (login)
        exe="/bin/login" (/bin/login)
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255 (system_u:system_r:local_login_t:s0-s0:c0.c255)

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN (USER_LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=848 (unknown(848))
        uid=848 (unknown(848))
        exe="/bin/login" (/bin/login)
        hostname=? (?)
        addr=? (?)
        terminal=tty3 (tty3)
        res=success (success)

Test 2 Done

Starting Test 3, walk events, records of 1 buffer...
event has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=1 file=None
    event time: 1143146623.879:146, host=(null)

Test 3 Done

Starting Test 4, walk events, records of 1 file...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 25 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (-13(Permission denied))
        a0=5555665d91b0 (5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (5555665d91b8)
        a3=0 (0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty= ()
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir, 730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 4 Done

Starting Test 5, walk events, records of 2 files...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 25 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (-13(Permission denied))
        a0=5555665d91b0 (5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (5555665d91b8)
        a3=0 (0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty= ()
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir, 730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 8 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read (read)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 25 fields
    line=2 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (-13(Permission denied))
        a0=5555665d91b0 (5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (5555665d91b8)
        a3=0 (0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty= ()
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir, 730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 9 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test2.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 10 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test2.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 11 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test2.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 12 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test2.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 13 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test2.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 14 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test2.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 5 Done

Starting Test 6, search...
auid = 500 not found...which is correct
auid exists...which is correct
Testing BUFFER_ARRAY, stop on field
Found auid = 848
Testing BUFFER_ARRAY, stop on record
Found type = SYSCALL
Testing BUFFER_ARRAY, stop on event
Found type = SYSCALL
Testing test.log, stop on field
Found auid = 4294967295
Testing test.log, stop on record
Found type = SYSCALL
Testing test.log, stop on event
Found type = AVC
Test 6 Done

Starting Test 7, compound search...
Found type = USER_START
Found auid = 0
Test 7 Done

Starting Test 8, regex search...
Doing regex match...

Test 8 Done

Starting Test 9, buffer feed...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN (LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=848 (unknown(848))

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=188 (setxattr)
        success=yes (yes)
        exit=0 (0)
        a0=7fffffa9a9f0 (7fffffa9a9f0)
        a1=3958d11333 (3958d11333)
        a2=5131f0 (5131f0)
        a3=20 (20)
        items=1 (1)
        pid=2027 (2027)
        auid=848 (unknown(848))
        uid=0 (root)
        gid=0 (root)
        euid=0 (root)
        suid=0 (root)
        fsuid=0 (root)
        egid=0 (root)
        sgid=0 (root)
        fsgid=0 (root)
        tty=tty3 (tty3)
        comm="login" (login)
        exe="/bin/login" (/bin/login)
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255 (system_u:system_r:local_login_t:s0-s0:c0.c255)

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN (USER_LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=848 (unknown(848))
        uid=848 (unknown(848))
        exe="/bin/login" (/bin/login)
        hostname=? (?)
        addr=? (?)
        terminal=tty3 (tty3)
        res=success (success)

Test 10 Done

Starting Test 10, file feed...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=None
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 25 fields
    line=2 file=None
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (-13(Permission denied))
        a0=5555665d91b0 (5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (5555665d91b8)
        a3=0 (0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty= ()
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=None
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=None
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir, 730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=None
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=None
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=None
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=None
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=None
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=None
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 10 Done

Finished non-admin tests

