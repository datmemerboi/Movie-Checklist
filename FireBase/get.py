# Get data from Firebase Realtime db
# Firebase app from cred.py

from cred import firebase

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
	print("\n=== ===\n")
	FirebaseGet('Recommend')
