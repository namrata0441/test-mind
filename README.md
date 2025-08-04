# 55-506951 OO-Programming (Professional Solutions). Designing and Implementing OO Applications (with Python) 
## Coursework 1: Simple Quiz Application 


### Task
For this initial coursework, you should just focus on creating and running Maths Quizzes and Multiple-choice tests across a single class.

Tests/Questions should be created/run/reviewed through GUIs created in pyQT. For this c/w, these can be separate GUI’s, run as different applications.

Teachers should be able to view the results of a test at a later date by class.

All relevant data must be stored in 'pickled' objects.

Appropriate software testing techniques should be used.

### WIP
Due to time constraints, I was unable to get all the required functionality in. I did however, try to demonstrate the full scope of skills learned during the module so far, including unit testing and persistence with pickle.

### Running the application

To run this application from the command line, change into the project directory and run the following command:

`python app.py`

If this gives an error, you may need to run the command with your specific python version. For example, I had to run `python3.6 app.py`

### Running the tests

To run the test suite for this project, navigate in to the `tests` directory and run the following command:

`python tests.py`

### Class diagram and changes during implementation

The class diagram can be found in the `assets` directory.

After studying the use case diagram, I decided to change the implementation from the class diagram by also adopting the singleton pattern with a central TestBank repository and associated TestCollection.

Singleton prevents other objects from instantiating their own copies of the Singleton object, ensuring that all objects access the single instance. This means that since the TestBank class controls the instantiation process of itself, the class has the flexibility to change the instantiation process.

This was particularly useful when introducing persistence using pickle. 

However, most importantly in this particular application, I felt a TestBank singleton was especially appropriate, because as the application grows in complexity there may be a situation where various parts of an application concurrently try to access a shared resource.

An example of this would be a teacher adding or removing questions from a test whilst a student tries to take said test. In this case the singleton would ensure that both users access the same Test instance.


Other negligible changes to the class diagram also include a few minor naming changes, just to try and improve semantics and more closely mirror domain specific terminology.

### References
http://manpages.ubuntu.com/manpages/trusty/man1/pyuic5.1.html