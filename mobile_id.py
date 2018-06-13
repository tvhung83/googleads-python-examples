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


import uuid

from utils import upload

# Change me!
list_name = 'MOBILE_ID UserList #%d' % uuid.uuid4()
list_desc = 'A list of customers that originated from MOBILE_ID, exported by Python example'
file_path = 'fixtures/mobile_id.txt'
list_type = 'MOBILE_ADVERTISING_ID'
app_id = '476943146' # Flood-It! 2 example app from AdWords doc

mobile_ids = tuple(open(file_path, 'r'))
members = [{'mobileId': mid.strip()} for mid in mobile_ids]

upload(list_name, list_desc, list_type, members, app_id)
