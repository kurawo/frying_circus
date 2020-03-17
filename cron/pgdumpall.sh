#!/bin/bash
pg_dumpall -f /tmp/dump.`date "+%Y%m%d_%H%M%S"`.sql -U postgres
