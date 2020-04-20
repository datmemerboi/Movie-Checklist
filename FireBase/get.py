# Get data from Firebase Realtime db


from firebase import firebase

firebase = firebase.FirebaseApplication("https://movie-checklist-6969.firebaseio.com/", authentication=None)

def FirebaseGet(Collection):
	print("Reading", Collection)
	result = firebase.get(Collection+'/', None)
	for row in list(result.values()):
		if 'Remarks' in row.keys():
			print(
				row['Title'],'|',
				row['Director'],'|',
				row['Year'],'|',
				row['Language'],'|',
				row['Remarks']
				)
		else:
			print(
				row['Title'],'|',
				row['Director'],'|',
				row['Year'],'|',
				row['Language']
				)

if __name__ == '__main__':
	FirebaseGet('Checklist')
	FirebaseGet('Recommend')
