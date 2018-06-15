#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys, yaml
from service import find, add, clean, append, NormalizeAndSHA256

type = sys.argv[1]
field = {
  'email': 'hashedEmail',
  'phone_number': 'hashedPhoneNumber',
  'user_id': 'userId',
  'mobile_id': 'mobileId'
}[type]
f = lambda r: NormalizeAndSHA256(r) if type in ['email', 'phone_number'] else r.strip()

conf = yaml.load(open('config/%s.yaml' % type))
mode = conf.get('mode', 'append')

rows = tuple(open('fixtures/%s.txt' % type, 'r'))
members = [{field: f(r) } for r in rows]

found = find(conf['list_name'])
if found is not None:
  if found['uploadKeyType'] != conf['list_type']:
    raise ValueError('Incompatible uploadKeyType, expecting "%s", and received: "%s"' % (conf['list_type'], found['uploadKeyType']))
  if mode == 'replace':
    clean(found['id'])
else:
  found = add(conf['list_name'], conf['list_desc'], conf['list_type'], conf.get('app_id', None))

append(found['id'], members)
