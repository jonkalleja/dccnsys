#!/usr/bin/env bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout dccn-staging.voidhost.xyz-2019.key -out dccn-staging.voidhost.xyz-2019.crt -config dccn-staging.voidhost.xyz.conf
