import os
import sys
import time
import filecmp
import shutil

class Sync: 
    def __init__(self, source_folder, replica_folder, logfile):
        self.source_path = source_folder
        self.replica_path = replica_folder
        self.log_path = logfile

    def sync(self):
        #1 get the extra files in replica and delete them
        directory_cmp = filecmp.dircmp(self.replica_path, self.source_path)
        left_replica = directory_cmp.left_only
        
        file_log = open(self.log_path, 'a')

        # delete extra files in replica and write to log and output
        for file in left_replica:
            delete_file = self.replica_path + "/" + file
            os.remove(delete_file)
            print("The {} was deleted from replica folder\n".format(file))
            file_log.write("The {} was deleted from replica folder\n".format(file))

        #2 if a name of a file exists in replica and in source
        # but the content is not identical, copy from source to replica
        diff = directory_cmp.diff_files

        # copy from source to replica the files found and write to log and output
        for file in diff:
            file_source = self.source_path + "/" + file
            file_replica = self.replica_path + "/" + file
            shutil.copy(file_source, file_replica)
            print("The {}, which is different in replica was copied to replica folder\n".format(file))
            file_log.write("The {}, which is different in replica was copied to replica folder\n".format(file))

        #3 if a file is not existing in replica, copy it in source
        right_source = directory_cmp.right_only

        # copy from source to replica the files found and write to log and output
        for file in right_source:
            file_source = self.source_path + "/" + file
            file_replica = self.replica_path + "/" + file
            shutil.copy(file_source, file_replica)
            print("The {}, which not exist in replica was created to replica folder\n".format(file))
            file_log.write("The {}, which not exist in replica was created to replica folder\n".format(file))


    def existance(self):
        # create source folder if not exists
        if not os.path.exists(self.source_path):
            os.mkdir(self.source_path)
        # create replica folder if not exists
        if not os.path.exists(self.replica_path):
            os.mkdir(self.replica_path)
        # create log folder if not exists
        if not os.path.exists(self.log_path):
            open(self.log_path, 'a').close()


    def sync_func(self):
        # creates files if not exists
        self.existance()
        # sync folders
        self.sync()

if __name__ == "__main__":

    # get absolute path to script
    path = os.getcwd()
    sync = Sync(sys.argv[1], sys.argv[2], sys.argv[3])
    
    # the creation of unexisting files in folders replica and source
    # is did manually by computer user
    while 1:
        sync.sync_func()
        time.sleep(int(sys.argv[4]))
