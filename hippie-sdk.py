import requests
import simplejson

class Hippie(object):
	
	# TODO: Support XML
	# TODO: Break into user and room classes that make requests through Hippie
	# TODO: Error handling
	
	def __init__(self, api_token):
		self.token = api_token
		self.base_url = 'http://api.hipchat.com/v1'
		
	def list_rooms(self):
		return requests.get("%s/rooms/list?auth_token=%s" % (self.base_url, self.token)).content
		
	def show_room(self, room_id):
		return requests.get("%s/rooms/show?room_id=%s&format=json&auth_token=%s" %(self.base_url, room_id, self.token)).content
		
	def message_room(self, room_id, from_name, message, notify=0, color='yellow'):
		# TODO: enforce from contraints
		# TODO: Escape HTML/XML for message
		payload = {
			'room_id': room_id,
			'from': from_name,
			'message': message,
			'notify': notify,
			'color': color,
		}
		return requests.post("%s/rooms/message?format=json&auth_token=%s" % (self.base_url, self.token), data=payload).content
		
	def show_room_history(self, room_id, date='recent', timezone='UTC'):
		# TODO: Check if valid PHP timezone
		return requests.get("%s/rooms/history?room_id=%s&date=%s&timezone=%s&format=json&auth_token=%s" % (self.base_url, room_id, date, timezone, self.token)).content

	def create_room(self, room_name, owner_user_id, topic, guest_access=0, privacy='public'):
		payload = {
			'name': room_name,
			'owner_user_id': owner_user_id,
			'privacy': privacy,
			'topic': topic,
			'guest_access': guest_access
		}
		return requests.post("%s/rooms/create?format=json&auth_token=%s" % (self.base_url, self.token), data=payload).content
	
	def delete_room(self, room_id):
		return requests.post("%s/rooms/delete?format=json&auth_token=%s" % (self.base_url, self.token), data={ 'room_id': room_id }).content
	
	def list_users(self):
		return requests.get("%s/users/list?format=json&auth_token=%s" % (self.base_url, self.token)).content
		
	def show_user(self, user_id):
		return requests.get("%s/users/show?user_id=%s&format=json&auth_token=%s" % (self.base_url, user_id, self.token)).content
		
	def update_user(self, options = {}):
		# TODO: Improve this implementation because it sucks
		# options: user_id, email, name, title, is_group_admin, password, timezone
		return requests.post("%s/users/update?format=json&auth_token=%s" % (self.base_url, self.token), data=options).content
		
	def create_user(self, email, name, title, password, is_group_admin=0, timezone='UTC'):
		payload = {
			'email': email,
			'name': name,
			'title': title,
			'password': password,
			'is_group_admin': is_group_admin,
			'timezone': timezone
		}
		return requests.post("%s/users/create?format=json&auth_token=%s" % (self.base_url, self.token), data=payload).content
		
	def delete_user(self, user_id):
		return requests.post("%s/users/delete?format=json&auth_token=%s" % (self.base_url, self.token), data={'user_id': user_id}).content
