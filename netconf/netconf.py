#!/usr/bin/env python3
import ncclient

host="ip"
from ncclient import manager
with manager.connect(host=host, port=830, timeout=None, username="developer", password="C1sco12345", hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % host, 'w') as f:
        f.write(c)
