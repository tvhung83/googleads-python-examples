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

from utils import upload, NormalizeAndSHA256

# Change me!
list_name = 'PHONE_NUMBER UserList #%d' % uuid.uuid4()
list_desc = 'A list of customers that originated from PHONE_NUMBER, exported by Python example'
file_path = 'fixtures/phone_number.txt'
list_type = 'CONTACT_INFO'

phone_numbers = tuple(open(file_path, 'r'))
members = [{'hashedPhoneNumber': NormalizeAndSHA256(pn)} for pn in phone_numbers]

upload(list_name, list_desc, list_type, members)
