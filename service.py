# Import appropriate modules from the client library.
from googleads import adwords

# Initialize client object.
client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')

# Initialize appropriate services.
user_list_service = client.GetService('AdwordsUserListService', 'v201806')

def find(list_name):
  selector = {
      'fields': ['UploadKeyType'],
      'predicates': [{
          'field': 'Name',
          'operator': 'EQUALS',
          'values': [list_name]
      }]
  }

  response = user_list_service.get(selector)

  if response['totalNumEntries']:
    return response['entries'][0]

def clean(user_list_id):
  operation = {
    'operand': {
      'userListId': user_list_id,
      'removeAll': True,
      'membersList': None
    },
    'operator': 'REMOVE'
  }

  response = user_list_service.mutateMembers([operation])
  print 'Removed all members of %d UserList' % len(response['userLists'])

def add(list_name, list_desc, list_type, app_id=None):
  user_list = {
    'xsi_type': 'CrmBasedUserList',
    'name': list_name,
    'description': list_desc,
    'membershipLifeSpan': 10000,
    'uploadKeyType': list_type
  }

  if app_id is not None:
    user_list['appId'] = app_id

  # Create an operation to add the user list.
  operations = [{
      'operator': 'ADD',
      'operand': user_list
  }]

  result = user_list_service.mutate(operations)
  return result['value'][0]

def append(user_list_id, members):
  operation = {
      'operand': {
          'userListId': user_list_id,
          'membersList': members
      },
      'operator': 'ADD'
  }

  response = user_list_service.mutateMembers([operation])

  if 'userLists' in response:
    for user_list in response['userLists']:
      print ('User list with name "%s" and ID "%d" was added.'
             % (user_list['name'], user_list['id']))

def NormalizeAndSHA256(s):
  """Normalizes (lowercase, remove whitespace) and hashes a string with SHA-256.

  Args:
    s: The string to perform this operation on.

  Returns:
    A normalized and SHA-256 hashed string.
  """
  import hashlib
  return hashlib.sha256(s.strip().lower()).hexdigest()
