#ensures that class has only one instance 
#provides easy global access to that instance
#control how it is instantitated
#critical regions must be entered serially (serialise the issues)

#singleton used for caching, logging, database connection, configuration access control and so on
#singleton used to control access to a shared resource
#don't allow singleton be used to provide global access to all resources

#considerations
#the class instance should ony be created when it is first needed
#singleton must be always in ready mode and loaded fast
#thread safety to ensure that multi threaded access to enure access is always controlled

