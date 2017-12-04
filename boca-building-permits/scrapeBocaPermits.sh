#!/bin/bash

echo

base_url="https://apps.ci.boca-raton.fl.us"

while read p; do
	curl -O "$base_url$p"
	sleep 1
done <issued-links.cleaned.txt