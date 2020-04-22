Movie Checklist
=
## Python 3 | PyQt5 | MongoDB | MongoClient | Firebase

As an avid movie lover, I have a large list of movies completed and yet to watch. As I had to keep track of them, here's an application to checklist the movies completed.

Built on Linux environment (*elementary OS*)

### Requirements

**Python, PyQt5, MongoDB** software and **PyMongo.MongoClient** and **Firebase** modules.
After installing them, just run *index.py*.
Running *setup.py* would help you install the required softwares (Built for Linux system)

### Note 

Default Mongo connection:`mongodb://localhost:27017`

Database: `Movie`

Collection: `Checklist`, `Recommend`

Firebase Database: paste URL of your Realtime DB in *Firebase/cred.py* as `FirebaseApplication("`App URL`", authentication=None)`. The same url will be used for all Firebase interactions

**Application functionalities**
> - Checklist of Movies (Title, Director, Year, Language, Remarks)
> - Recommend list of Movies
> - Backup Data into JSON file
> - Search Director's Works, by Year, by Language
> - Push checklist to Firebase DB

**Future Additions**
> Portable application