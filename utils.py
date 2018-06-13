import hashlib

# Import appropriate modules from the client library.
from googleads import adwords

def upload(list_name, list_desc, list_type, members, app_id=None):
  # Initialize client object.
  client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')

  # Initialize appropriate services.
  user_list_service = client.GetService('AdwordsUserListService', 'v201806')

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
  user_list_id = result['value'][0]['id']

  mutate_members_operation = {
      'operand': {
          'userListId': user_list_id,
          'membersList': members
      },
      'operator': 'ADD'
  }

  response = user_list_service.mutateMembers([mutate_members_operation])

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
  return hashlib.sha256(s.strip().lower()).hexdigest()
